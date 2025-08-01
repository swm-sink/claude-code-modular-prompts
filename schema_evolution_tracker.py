#!/usr/bin/env python3
"""
Step 15: Schema Evolution Tracking - Analyze how XML complexity grew over time
"""

import subprocess
import re
from pathlib import Path
from collections import defaultdict, Counter
import json
from datetime import datetime

def get_git_commit_history():
    """Get git commit history with file changes"""
    try:
        # Get commit history with file stats
        result = subprocess.run([
            'git', 'log', '--oneline', '--name-status', '--since="2024-01-01"'
        ], capture_output=True, text=True, cwd='.')
        
        if result.returncode != 0:
            print(f"Git log failed: {result.stderr}")
            return []
        
        return result.stdout.split('\n')
    except Exception as e:
        print(f"Error getting git history: {e}")
        return []

def parse_commit_history(git_log_lines):
    """Parse git commit history into structured data"""
    commits = []
    current_commit = None
    
    for line in git_log_lines:
        line = line.strip()
        if not line:
            continue
        
        # Check if this is a commit line (starts with hash)
        commit_match = re.match(r'^([a-f0-9]+)\s+(.+)$', line)
        if commit_match:
            if current_commit:
                commits.append(current_commit)
            
            current_commit = {
                'hash': commit_match.group(1),
                'message': commit_match.group(2),
                'files': []
            }
        elif current_commit and re.match(r'^[AMD]\s+', line):
            # File change line (Added, Modified, Deleted)
            parts = line.split('\t', 1)
            if len(parts) == 2:
                action, filepath = parts
                current_commit['files'].append({
                    'action': action,
                    'path': filepath
                })
    
    if current_commit:
        commits.append(current_commit)
    
    return commits

def analyze_xml_metadata_evolution(commits):
    """Analyze how XML metadata evolved over time"""
    results = {
        'total_commits': len(commits),
        'xml_related_commits': [],
        'metadata_growth_timeline': [],
        'xml_file_creation_timeline': [],
        'schema_complexity_evolution': defaultdict(list),
        'commit_patterns': {
            'xml_metadata_additions': 0,
            'ai_metadata_commits': 0,
            'component_metadata_commits': 0,
            'schema_changes': 0,
            'tag_proliferation_commits': 0
        }
    }
    
    print(f"Analyzing XML evolution across {len(commits)} commits...")
    
    xml_keywords = [
        'xml', 'metadata', 'ai_document_metadata', 'component_metadata',
        'context_engineering', 'ai_navigation', 'schema', 'tag', 'element'
    ]
    
    for i, commit in enumerate(commits):
        if i % 50 == 0:
            print(f"  Processing commit {i+1}/{len(commits)}")
        
        commit_message = commit['message'].lower()
        is_xml_related = any(keyword in commit_message for keyword in xml_keywords)
        
        # Check if files modified are XML-heavy
        xml_files_modified = []
        for file_change in commit['files']:
            filepath = file_change['path']
            if (filepath.endswith('.md') and 
                ('.claude/components/' in filepath or 
                 '.claude/commands/' in filepath or
                 'CLAUDE.md' in filepath)):
                xml_files_modified.append(file_change)
        
        if is_xml_related or xml_files_modified:
            commit_analysis = {
                'hash': commit['hash'],
                'message': commit['message'],
                'xml_files_modified': len(xml_files_modified),
                'xml_related_keywords': [kw for kw in xml_keywords if kw in commit_message],
                'files': xml_files_modified,
                'analysis': analyze_commit_xml_impact(commit)
            }
            results['xml_related_commits'].append(commit_analysis)
            
            # Update pattern counters
            if 'metadata' in commit_message:
                results['commit_patterns']['xml_metadata_additions'] += 1
            if 'ai_' in commit_message or 'AI_METADATA' in commit['message']:
                results['commit_patterns']['ai_metadata_commits'] += 1
            if 'component' in commit_message:
                results['commit_patterns']['component_metadata_commits'] += 1
            if 'schema' in commit_message:
                results['commit_patterns']['schema_changes'] += 1
            if any(word in commit_message for word in ['tag', 'element', 'xml']):
                results['commit_patterns']['tag_proliferation_commits'] += 1
    
    return results

def analyze_commit_xml_impact(commit):
    """Analyze the XML impact of a specific commit"""
    analysis = {
        'likely_xml_impact': 'unknown',
        'metadata_change_type': 'unknown',
        'complexity_impact': 'neutral'
    }
    
    message = commit['message'].lower()
    
    # Classify likely XML impact
    if any(word in message for word in ['add', 'new', 'create']):
        if any(word in message for word in ['metadata', 'tag', 'element']):
            analysis['likely_xml_impact'] = 'addition'
            analysis['complexity_impact'] = 'increase'
    
    elif any(word in message for word in ['remove', 'delete', 'clean']):
        analysis['likely_xml_impact'] = 'removal'
        analysis['complexity_impact'] = 'decrease'
    
    elif any(word in message for word in ['update', 'modify', 'change']):
        analysis['likely_xml_impact'] = 'modification'
        analysis['complexity_impact'] = 'neutral'
    
    elif any(word in message for word in ['refactor', 'restructure']):
        analysis['likely_xml_impact'] = 'restructure'
        analysis['complexity_impact'] = 'potentially_decrease'
    
    # Classify metadata change type
    if 'ai_metadata' in message or 'AI_METADATA' in commit['message']:
        analysis['metadata_change_type'] = 'ai_system_metadata'
    elif 'component' in message:
        analysis['metadata_change_type'] = 'component_metadata'
    elif 'command' in message:
        analysis['metadata_change_type'] = 'command_metadata'
    elif 'context' in message:
        analysis['metadata_change_type'] = 'context_metadata'
    elif 'navigation' in message:
        analysis['metadata_change_type'] = 'navigation_metadata'
    
    return analysis

def identify_complexity_growth_phases(xml_commits):
    """Identify distinct phases of XML complexity growth"""
    phases = []
    
    # Group commits by patterns and timing
    metadata_addition_commits = [c for c in xml_commits if 'add' in c['message'].lower() and 'metadata' in c['message'].lower()]
    ai_metadata_commits = [c for c in xml_commits if 'ai_metadata' in c['message'].lower() or 'AI_METADATA' in c['message']]
    component_commits = [c for c in xml_commits if 'component' in c['message'].lower()]
    
    if ai_metadata_commits:
        phases.append({
            'phase': 'AI Metadata Introduction',
            'commit_count': len(ai_metadata_commits),
            'description': 'Introduction of comprehensive AI document metadata system',
            'complexity_impact': 'HIGH',
            'example_commits': ai_metadata_commits[:3]
        })
    
    if component_commits:
        phases.append({
            'phase': 'Component Metadata Expansion',
            'commit_count': len(component_commits),
            'description': 'Addition of detailed component metadata and cross-references',
            'complexity_impact': 'MEDIUM',
            'example_commits': component_commits[:3]
        })
    
    if metadata_addition_commits:
        phases.append({
            'phase': 'General Metadata Proliferation',
            'commit_count': len(metadata_addition_commits),
            'description': 'Ongoing addition of various metadata elements',
            'complexity_impact': 'CUMULATIVE',
            'example_commits': metadata_addition_commits[:3]
        })
    
    return phases

def analyze_file_creation_patterns(commits):
    """Analyze when XML-heavy files were created"""
    file_creation_timeline = []
    
    for commit in commits:
        for file_change in commit['files']:
            if file_change['action'] == 'A':  # Added file
                filepath = file_change['path']
                if (filepath.endswith('.md') and 
                    ('.claude/components/' in filepath or 
                     '.claude/commands/' in filepath)):
                    file_creation_timeline.append({
                        'commit': commit['hash'],
                        'message': commit['message'],
                        'file': filepath,
                        'category': categorize_file_path(filepath)
                    })
    
    return file_creation_timeline

def categorize_file_path(file_path):
    """Categorize file based on path"""
    if '.claude/components/atomic' in file_path:
        return 'Atomic Component'
    elif '.claude/components/security' in file_path:
        return 'Security Component'
    elif '.claude/components/orchestration' in file_path:
        return 'Orchestration Component'
    elif '.claude/components/' in file_path:
        return 'Other Component'
    elif '.claude/commands/core' in file_path:
        return 'Core Command'
    elif '.claude/commands/meta' in file_path:
        return 'Meta Command'
    elif '.claude/commands/' in file_path:
        return 'Other Command'
    else:
        return 'Other'

def generate_evolution_report(results):
    """Generate comprehensive schema evolution report"""
    print("\n" + "=" * 60)
    print("STEP 15: SCHEMA EVOLUTION TRACKING RESULTS")
    print("=" * 60)
    
    total_commits = results['total_commits']
    xml_commits = len(results['xml_related_commits'])
    
    print(f"Total Commits Analyzed: {total_commits}")
    print(f"XML-Related Commits: {xml_commits} ({xml_commits/total_commits*100:.1f}%)")
    
    # Commit pattern analysis
    print(f"\nXML Evolution Patterns:")
    patterns = results['commit_patterns']
    for pattern, count in patterns.items():
        percentage = (count / xml_commits * 100) if xml_commits > 0 else 0
        print(f"  {pattern.replace('_', ' ').title()}: {count} commits ({percentage:.1f}%)")
    
    # Most impactful commits
    print(f"\nMost Impactful XML-Related Commits:")
    impact_commits = sorted(results['xml_related_commits'], 
                           key=lambda x: x['xml_files_modified'], reverse=True)
    
    for i, commit in enumerate(impact_commits[:10], 1):
        files_modified = commit['xml_files_modified']
        print(f"  {i:2d}. {commit['hash'][:8]} - {files_modified:2d} XML files - {commit['message'][:60]}...")
    
    # Complexity growth phases
    phases = identify_complexity_growth_phases(results['xml_related_commits'])
    if phases:
        print(f"\nXML Complexity Growth Phases:")
        for i, phase in enumerate(phases, 1):
            print(f"  {i}. {phase['phase']} ({phase['commit_count']} commits)")
            print(f"     Impact: {phase['complexity_impact']}")
            print(f"     Description: {phase['description']}")
    
    # File creation analysis
    file_timeline = analyze_file_creation_patterns(results['xml_related_commits'])
    if file_timeline:
        print(f"\nXML File Creation Timeline (Recent):")
        category_counts = Counter(item['category'] for item in file_timeline)
        for category, count in category_counts.most_common():
            print(f"  {category}: {count} files created")
    
    # Evolution insights
    print(f"\nKey Evolution Insights:")
    
    ai_metadata_ratio = patterns['ai_metadata_commits'] / xml_commits if xml_commits > 0 else 0
    if ai_metadata_ratio > 0.3:
        print(f"  🚨 AI metadata system represents {ai_metadata_ratio:.1%} of XML evolution")
        print(f"     - Major contributor to current complexity crisis")
    
    component_ratio = patterns['component_metadata_commits'] / xml_commits if xml_commits > 0 else 0
    if component_ratio > 0.2:
        print(f"  ⚠️ Component metadata expansion represents {component_ratio:.1%} of changes")
        print(f"     - Drove atomic component content inversion")
    
    if patterns['schema_changes'] < 5:
        print(f"  🚨 Schema changes: {patterns['schema_changes']} commits")
        print(f"     - Lack of schema governance contributed to tag proliferation")
    
    # Recommendations
    print(f"\nEvolution-Based Recommendations:")
    print(f"  1. SCHEMA GOVERNANCE: Implement schema change controls")
    print(f"  2. METADATA REVIEW: Audit AI metadata system additions")
    print(f"  3. COMPONENT SIMPLIFICATION: Reverse component metadata expansion")
    print(f"  4. COMMIT PATTERNS: Review metadata addition processes")
    
    print("=" * 60)

def main():
    """Main schema evolution tracking analysis"""
    git_history = get_git_commit_history()
    
    if not git_history:
        print("No git history found or git not available!")
        return
    
    commits = parse_commit_history(git_history)
    
    if not commits:
        print("No commits found to analyze!")
        return
    
    results = analyze_xml_metadata_evolution(commits)
    generate_evolution_report(results)
    
    # Save detailed results
    # Convert any sets to lists for JSON serialization
    json_safe_results = json.loads(json.dumps(results, default=str))
    
    with open('schema_evolution_results.json', 'w') as f:
        json.dump(json_safe_results, f, indent=2)
    
    print(f"\nDetailed results saved to: schema_evolution_results.json")

if __name__ == "__main__":
    main()