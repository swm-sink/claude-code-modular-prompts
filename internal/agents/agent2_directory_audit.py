#!/usr/bin/env python3
"""
Agent 2: Directory Auditor
Map directory structure vs. documentation claims to identify organizational chaos
"""

import os
import json
import re
from pathlib import Path
from collections import defaultdict, Counter
from datetime import datetime

class DirectoryAuditor:
    def __init__(self, base_path=".claude"):
        self.base_path = Path(base_path)
        self.directory_analysis = {}
        self.documentation_claims = {}
        self.inconsistencies = []
        self.overlaps = []
        self.recommendations = []
        
        # Load Agent 1 data for context
        self.agent1_data = self.load_agent1_data()
        
    def load_agent1_data(self):
        """Load Agent 1's inventory results for context"""
        try:
            with open("agent1_inventory_results.json", 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            print("⚠️  Agent 1 data not found - continuing without context")
            return {}
    
    def analyze_actual_directory_structure(self):
        """Analyze the actual directory structure in .claude"""
        print("🔍 Agent 2: Analyzing actual directory structure...")
        
        structure = {}
        
        # Walk all directories under .claude
        for root, dirs, files in os.walk(self.base_path):
            relative_path = Path(root).relative_to(Path('.'))
            
            # Skip hidden directories and files
            dirs[:] = [d for d in dirs if not d.startswith('.')]
            md_files = [f for f in files if f.endswith('.md')]
            
            if md_files or dirs:  # Only include directories with content
                structure[str(relative_path)] = {
                    'subdirectories': dirs.copy(),
                    'md_files': md_files,
                    'file_count': len(md_files),
                    'total_size': self.calculate_directory_size(root, md_files),
                    'depth': len(Path(root).parts) - len(self.base_path.parts),
                    'purpose': self.infer_directory_purpose(relative_path, md_files)
                }
        
        self.directory_analysis = structure
        print(f"📁 Found {len(structure)} directories with content")
        return structure
    
    def calculate_directory_size(self, root, md_files):
        """Calculate total size of markdown files in directory"""
        total_size = 0
        for file in md_files:
            try:
                file_path = Path(root) / file
                total_size += file_path.stat().st_size
            except:
                pass
        return total_size
    
    def infer_directory_purpose(self, dir_path, md_files):
        """Infer the purpose of a directory based on location and content"""
        path_str = str(dir_path).lower()
        
        # Known directory purposes
        purpose_map = {
            'commands': 'Command definitions for Claude Code',
            'system/quality': 'Quality gates and TDD enforcement',
            'system/git': 'Git operations and worktree management',
            'system/session': 'Session management and persistence',
            'system/context': 'Context management and artifacts',
            'system/security': 'Security validation and threat modeling',
            'modules/patterns': 'Reusable pattern modules',
            'modules/development': 'Development workflow modules',
            'modules/meta': 'Meta-framework capabilities',
            'modules/quality': 'Quality validation modules',
            'prompt_eng/patterns': 'Prompt engineering patterns',
            'prompt_eng/frameworks': 'Advanced prompt frameworks',
            'prompt_eng/personas': 'Specialized AI personas',
            'prompt_eng/modules': 'Prompt engineering modules',
            'domain': 'Domain-specific templates and adaptation',
            'meta': 'Meta-framework evolution and learning',
            'development': 'Development support modules',
            'planning': 'Planning and strategy modules',
            'testing': 'Testing and validation frameworks',
            'archive': 'Archived or deprecated components'
        }
        
        # Find matching purpose
        for pattern, purpose in purpose_map.items():
            if pattern in path_str:
                return purpose
        
        # Infer from file names if no pattern match
        if any('command' in f.lower() for f in md_files):
            return 'Command-related functionality'
        elif any('test' in f.lower() for f in md_files):
            return 'Testing-related functionality'
        elif any('pattern' in f.lower() for f in md_files):
            return 'Pattern definitions'
        elif any('quality' in f.lower() for f in md_files):
            return 'Quality assurance'
        
        return 'Unknown purpose - needs classification'
    
    def extract_documentation_claims(self):
        """Extract directory structure claims from CLAUDE.md"""
        print("📋 Agent 2: Extracting documentation claims from CLAUDE.md...")
        
        claude_md_path = Path("CLAUDE.md")
        if not claude_md_path.exists():
            print("⚠️  CLAUDE.md not found - cannot verify claims")
            return {}
        
        with open(claude_md_path, 'r') as f:
            content = f.read()
        
        claims = {}
        
        # Extract directory structure enforcement section
        structure_match = re.search(
            r'<directory_structure.*?>(.*?)</directory_structure>',
            content, re.DOTALL
        )
        
        if structure_match:
            structure_content = structure_match.group(1)
            
            # Extract location claims
            location_patterns = re.findall(
                r'location\s*=\s*["\']([^"\']+)["\']',
                structure_content
            )
            
            for location in location_patterns:
                claims[location] = {
                    'claimed_purpose': self.extract_purpose_from_context(structure_content, location),
                    'enforcement_level': 'MANDATORY' if 'MANDATORY' in structure_content else 'NORMAL'
                }
        
        # Extract architecture section claims
        arch_match = re.search(
            r'<architecture>(.*?)</architecture>',
            content, re.DOTALL
        )
        
        if arch_match:
            arch_content = arch_match.group(1)
            
            # Extract command location claims
            cmd_match = re.search(r'location\s*=\s*["\']([^"\']+)["\']', arch_content)
            if cmd_match:
                claims[cmd_match.group(1)] = {
                    'claimed_purpose': 'Command definitions with delegation',
                    'enforcement_level': 'MANDATORY'
                }
            
            # Extract module location claims
            mod_match = re.search(r'modules.*?location\s*=\s*["\']([^"\']+)["\']', arch_content)
            if mod_match:
                claims[mod_match.group(1)] = {
                    'claimed_purpose': 'Implementation modules',
                    'enforcement_level': 'MANDATORY'
                }
        
        self.documentation_claims = claims
        print(f"📝 Extracted {len(claims)} directory claims from documentation")
        return claims
    
    def extract_purpose_from_context(self, content, location):
        """Extract purpose description for a location from surrounding context"""
        # Find the section containing this location
        location_index = content.find(location)
        if location_index == -1:
            return "Purpose not specified"
        
        # Look for purpose descriptions nearby
        context = content[max(0, location_index-200):location_index+200]
        
        purpose_patterns = [
            r'<(\w+)>([^<]+)',
            r'>([^<]+)</',
            r'location.*?>([^<]+)'
        ]
        
        for pattern in purpose_patterns:
            matches = re.findall(pattern, context)
            if matches:
                # Return the most descriptive match
                for match in matches:
                    text = match[1] if isinstance(match, tuple) else match
                    if len(text.strip()) > 10:  # Meaningful description
                        return text.strip()
        
        return "Purpose not clearly specified"
    
    def identify_structure_inconsistencies(self):
        """Identify inconsistencies between actual structure and documentation"""
        print("🔍 Agent 2: Identifying structure inconsistencies...")
        
        inconsistencies = []
        
        # Check claimed directories vs actual
        for claimed_dir, claim_info in self.documentation_claims.items():
            claimed_path = str(Path(claimed_dir))
            
            # Look for actual directory
            actual_matches = [
                path for path in self.directory_analysis.keys()
                if claimed_path in path or path.endswith(claimed_path)
            ]
            
            if not actual_matches:
                inconsistencies.append({
                    'type': 'MISSING_CLAIMED_DIRECTORY',
                    'severity': 'HIGH',
                    'claimed': claimed_dir,
                    'message': f"Documentation claims directory '{claimed_dir}' exists but not found",
                    'enforcement': claim_info.get('enforcement_level', 'NORMAL')
                })
            elif len(actual_matches) > 1:
                inconsistencies.append({
                    'type': 'MULTIPLE_MATCHES',
                    'severity': 'MEDIUM',
                    'claimed': claimed_dir,
                    'actual': actual_matches,
                    'message': f"Multiple directories match claim '{claimed_dir}': {actual_matches}"
                })
        
        # Check for unexpected directories
        expected_patterns = set(self.documentation_claims.keys())
        for actual_dir in self.directory_analysis.keys():
            if not any(pattern in actual_dir for pattern in expected_patterns):
                # Skip archive directories (expected to be undocumented)
                if 'archive' not in actual_dir:
                    inconsistencies.append({
                        'type': 'UNDOCUMENTED_DIRECTORY',
                        'severity': 'MEDIUM',
                        'actual': actual_dir,
                        'message': f"Directory '{actual_dir}' exists but not documented",
                        'files': self.directory_analysis[actual_dir]['file_count']
                    })
        
        self.inconsistencies = inconsistencies
        print(f"⚠️  Found {len(inconsistencies)} structure inconsistencies")
        return inconsistencies
    
    def detect_organizational_overlaps(self):
        """Detect overlapping functionality across directories"""
        print("🔍 Agent 2: Detecting organizational overlaps...")
        
        overlaps = []
        
        # Group directories by similar purposes
        purpose_groups = defaultdict(list)
        for dir_path, dir_info in self.directory_analysis.items():
            purpose = dir_info['purpose'].lower()
            
            # Categorize by key terms
            if 'pattern' in purpose:
                purpose_groups['patterns'].append(dir_path)
            elif 'quality' in purpose:
                purpose_groups['quality'].append(dir_path)
            elif 'module' in purpose:
                purpose_groups['modules'].append(dir_path)
            elif 'development' in purpose:
                purpose_groups['development'].append(dir_path)
            elif 'command' in purpose:
                purpose_groups['commands'].append(dir_path)
            elif 'prompt' in purpose:
                purpose_groups['prompt_engineering'].append(dir_path)
        
        # Identify overlaps
        for category, directories in purpose_groups.items():
            if len(directories) > 1:
                total_files = sum(
                    self.directory_analysis[d]['file_count'] 
                    for d in directories
                )
                
                overlaps.append({
                    'type': 'FUNCTIONAL_OVERLAP',
                    'category': category,
                    'directories': directories,
                    'total_files': total_files,
                    'severity': 'HIGH' if total_files > 20 else 'MEDIUM',
                    'message': f"Multiple directories handle {category}: {directories}"
                })
        
        # Special check for modules vs prompt_eng duplication
        modules_patterns = [d for d in self.directory_analysis.keys() if 'modules/patterns' in d]
        prompt_patterns = [d for d in self.directory_analysis.keys() if 'prompt_eng/patterns' in d]
        
        if modules_patterns and prompt_patterns:
            overlaps.append({
                'type': 'PATTERN_DUPLICATION',
                'severity': 'CRITICAL',
                'directories': modules_patterns + prompt_patterns,
                'message': 'Pattern functionality duplicated across modules/ and prompt_eng/',
                'impact': 'Creates confusion about single source of truth'
            })
        
        self.overlaps = overlaps
        print(f"🔄 Found {len(overlaps)} organizational overlaps")
        return overlaps
    
    def generate_consolidation_recommendations(self):
        """Generate recommendations for structure consolidation"""
        print("💡 Agent 2: Generating consolidation recommendations...")
        
        recommendations = []
        
        # Analyze the overlap patterns to suggest consolidation
        for overlap in self.overlaps:
            if overlap['type'] == 'FUNCTIONAL_OVERLAP':
                category = overlap['category']
                directories = overlap['directories']
                
                if category == 'patterns':
                    recommendations.append({
                        'priority': 'HIGH',
                        'action': 'CONSOLIDATE_PATTERNS',
                        'description': 'Merge all pattern directories into single location',
                        'source_dirs': directories,
                        'target_dir': '.claude/patterns/',
                        'rationale': 'Eliminate pattern duplication and establish single source',
                        'estimated_effort': 'HIGH'
                    })
                
                elif category == 'quality':
                    recommendations.append({
                        'priority': 'MEDIUM',
                        'action': 'CONSOLIDATE_QUALITY',
                        'description': 'Merge quality modules into system/quality/',
                        'source_dirs': directories,
                        'target_dir': '.claude/system/quality/',
                        'rationale': 'Quality infrastructure should be centralized',
                        'estimated_effort': 'MEDIUM'
                    })
                
                elif category == 'modules':
                    recommendations.append({
                        'priority': 'HIGH',
                        'action': 'STANDARDIZE_MODULES',
                        'description': 'Establish single module hierarchy',
                        'source_dirs': directories,
                        'target_dir': '.claude/modules/',
                        'rationale': 'Modules scattered across multiple hierarchies',
                        'estimated_effort': 'HIGH'
                    })
        
        # Address specific inconsistencies
        high_severity_issues = [i for i in self.inconsistencies if i['severity'] == 'HIGH']
        for issue in high_severity_issues:
            if issue['type'] == 'MISSING_CLAIMED_DIRECTORY':
                recommendations.append({
                    'priority': 'CRITICAL',
                    'action': 'RECONCILE_DOCUMENTATION',
                    'description': f"Either create missing directory or update documentation",
                    'issue': issue['claimed'],
                    'rationale': 'Documentation claims directory that does not exist',
                    'estimated_effort': 'LOW'
                })
        
        # Suggest overall structure simplification
        total_dirs = len(self.directory_analysis)
        if total_dirs > 30:  # Arbitrary threshold for "too complex"
            recommendations.append({
                'priority': 'MEDIUM',
                'action': 'SIMPLIFY_HIERARCHY',
                'description': f"Reduce directory count from {total_dirs} to <25",
                'rationale': 'Current structure too complex for maintainability',
                'estimated_effort': 'HIGH'
            })
        
        self.recommendations = recommendations
        print(f"📋 Generated {len(recommendations)} consolidation recommendations")
        return recommendations
    
    def run_complete_audit(self):
        """Run complete directory audit analysis"""
        print("🏗️  Agent 2: Starting complete directory structure audit...")
        
        # Step 1: Analyze actual structure
        actual_structure = self.analyze_actual_directory_structure()
        
        # Step 2: Extract documentation claims
        doc_claims = self.extract_documentation_claims()
        
        # Step 3: Identify inconsistencies
        inconsistencies = self.identify_structure_inconsistencies()
        
        # Step 4: Detect overlaps
        overlaps = self.detect_organizational_overlaps()
        
        # Step 5: Generate recommendations
        recommendations = self.generate_consolidation_recommendations()
        
        # Generate comprehensive report
        report = self.generate_audit_report()
        
        print("✅ Agent 2: Directory audit complete")
        return report
    
    def generate_audit_report(self):
        """Generate comprehensive audit report"""
        return {
            'analysis_timestamp': datetime.now().isoformat(),
            'agent': 'Agent 2 - Directory Auditor',
            'audit_summary': {
                'total_directories': len(self.directory_analysis),
                'documented_claims': len(self.documentation_claims),
                'inconsistencies_found': len(self.inconsistencies),
                'overlaps_detected': len(self.overlaps),
                'recommendations_generated': len(self.recommendations)
            },
            'actual_structure': self.directory_analysis,
            'documentation_claims': self.documentation_claims,
            'inconsistencies': self.inconsistencies,
            'overlaps': self.overlaps,
            'recommendations': self.recommendations,
            'critical_findings': self.identify_critical_audit_findings(),
            'handoff_data': self.prepare_audit_handoff_data()
        }
    
    def identify_critical_audit_findings(self):
        """Identify critical findings for escalation"""
        critical = []
        
        # Critical structural issues
        critical_overlaps = [o for o in self.overlaps if o['severity'] == 'CRITICAL']
        if critical_overlaps:
            critical.append({
                'type': 'CRITICAL_DUPLICATION',
                'message': f"{len(critical_overlaps)} critical organizational overlaps found",
                'impact': 'Framework has competing organizational schemes',
                'action_required': 'Immediate consolidation needed'
            })
        
        # High-priority inconsistencies
        high_inconsistencies = [i for i in self.inconsistencies if i['severity'] == 'HIGH']
        if len(high_inconsistencies) > 5:
            critical.append({
                'type': 'DOCUMENTATION_MISMATCH',
                'message': f"{len(high_inconsistencies)} high-severity documentation mismatches",
                'impact': 'Documentation does not reflect reality',
                'action_required': 'Documentation overhaul required'
            })
        
        # Complexity threshold exceeded
        if len(self.directory_analysis) > 35:
            critical.append({
                'type': 'EXCESSIVE_COMPLEXITY',
                'message': f"{len(self.directory_analysis)} directories exceeds maintainable threshold",
                'impact': 'Structure too complex for practical use',
                'action_required': 'Significant simplification needed'
            })
        
        return critical
    
    def prepare_audit_handoff_data(self):
        """Prepare handoff data for subsequent agents"""
        return {
            'agent_3_reference_analysis': {
                'directory_overlap_impact': len(self.overlaps),
                'reference_path_complications': [
                    overlap for overlap in self.overlaps 
                    if overlap['type'] in ['PATTERN_DUPLICATION', 'FUNCTIONAL_OVERLAP']
                ],
                'structure_complexity_score': len(self.directory_analysis)
            },
            'agent_4_testing_priorities': {
                'critical_structure_issues': [
                    finding for finding in self.identify_critical_audit_findings()
                    if finding['type'] == 'CRITICAL_DUPLICATION'
                ],
                'command_directory_status': any(
                    'command' in claim for claim in self.documentation_claims.keys()
                ),
                'quality_infrastructure_scattered': len([
                    d for d in self.directory_analysis.keys() 
                    if 'quality' in d
                ]) > 1
            },
            'agent_5_architecture_design': {
                'consolidation_recommendations': self.recommendations,
                'current_complexity': len(self.directory_analysis),
                'overlap_categories': list(set(
                    overlap['category'] for overlap in self.overlaps
                    if 'category' in overlap
                )),
                'documentation_alignment_issues': len(self.inconsistencies)
            }
        }
    
    def save_audit_results(self, output_file="agent2_directory_audit_results.json"):
        """Save audit results to file"""
        report = self.generate_audit_report()
        
        with open(output_file, 'w') as f:
            json.dump(report, f, indent=2)
        
        print(f"💾 Agent 2: Audit results saved to {output_file}")
        return report

if __name__ == "__main__":
    auditor = DirectoryAuditor()
    report = auditor.run_complete_audit()
    auditor.save_audit_results()
    
    # Print summary for immediate visibility
    print("\n" + "="*80)
    print("AGENT 2 DIRECTORY AUDIT SUMMARY")
    print("="*80)
    print(f"📁 Total Directories: {report['audit_summary']['total_directories']}")
    print(f"📝 Documentation Claims: {report['audit_summary']['documented_claims']}")
    print(f"⚠️  Inconsistencies: {report['audit_summary']['inconsistencies_found']}")
    print(f"🔄 Overlaps Detected: {report['audit_summary']['overlaps_detected']}")
    print(f"💡 Recommendations: {report['audit_summary']['recommendations_generated']}")
    
    if report['critical_findings']:
        print(f"\n🚨 Critical Findings: {len(report['critical_findings'])}")
        for finding in report['critical_findings']:
            print(f"  {finding['type']}: {finding['message']}")
    
    print(f"\n✅ Agent 2 Complete - Directory audit data ready for Agent 5")