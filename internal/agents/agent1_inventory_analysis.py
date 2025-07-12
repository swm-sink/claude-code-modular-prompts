#!/usr/bin/env python3
"""
Agent 1: Inventory Specialist
Complete catalog of all 241 markdown files with metadata extraction
"""

import os
import re
import json
from pathlib import Path
from datetime import datetime
from collections import defaultdict, Counter

class FrameworkInventoryAnalyst:
    def __init__(self, base_path=".claude"):
        self.base_path = Path(base_path)
        self.inventory = {}
        self.categories = defaultdict(list)
        self.stats = defaultdict(int)
        self.progress = 0
        self.total_files = 0
        
    def analyze_file_metadata(self, file_path):
        """Extract comprehensive metadata from a single file"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
            metadata = {
                'path': str(file_path),
                'relative_path': str(file_path.relative_to(Path('.'))),
                'size_bytes': file_path.stat().st_size,
                'size_kb': round(file_path.stat().st_size / 1024, 2),
                'line_count': len(content.splitlines()),
                'category': self.classify_file_purpose(file_path, content),
                'version': self.extract_version(content),
                'last_updated': self.extract_last_updated(content),
                'status': self.extract_status(content),
                'dependencies': self.extract_dependencies(content),
                'module_type': self.determine_module_type(file_path, content),
                'complexity_score': self.calculate_complexity(content),
                'has_xml_structure': '<module' in content or '<command' in content,
                'has_version_table': '| version |' in content,
                'reference_count': len(re.findall(r'\.md(?:\)|])', content)),
                'thinking_patterns': bool(re.search(r'thinking.*pattern|<thinking_pattern', content, re.IGNORECASE)),
                'quality_gates': bool(re.search(r'quality.*gate|tdd|test.*coverage', content, re.IGNORECASE)),
            }
            
            return metadata
            
        except Exception as e:
            return {
                'path': str(file_path),
                'error': str(e),
                'category': 'ERROR',
                'size_bytes': 0
            }
    
    def classify_file_purpose(self, file_path, content):
        """Classify file by its actual purpose"""
        path_str = str(file_path).lower()
        content_lower = content.lower()
        
        # Command files
        if '/commands/' in path_str:
            return 'COMMAND'
        
        # System infrastructure
        if '/system/' in path_str:
            if '/quality/' in path_str:
                return 'QUALITY_MODULE'
            elif '/git/' in path_str:
                return 'GIT_MODULE'
            elif '/session/' in path_str:
                return 'SESSION_MODULE'
            elif '/context/' in path_str:
                return 'CONTEXT_MODULE'
            elif '/security/' in path_str:
                return 'SECURITY_MODULE'
            else:
                return 'SYSTEM_MODULE'
        
        # Module categories
        if '/modules/' in path_str:
            if '/patterns/' in path_str:
                return 'PATTERN_MODULE'
            elif '/development/' in path_str:
                return 'DEVELOPMENT_MODULE'
            elif '/meta/' in path_str:
                return 'META_MODULE'
            elif '/quality/' in path_str:
                return 'QUALITY_MODULE'
            else:
                return 'MODULE'
        
        # Prompt engineering
        if '/prompt_eng/' in path_str:
            if '/patterns/' in path_str:
                return 'PROMPT_PATTERN'
            elif '/frameworks/' in path_str:
                return 'PROMPT_FRAMEWORK'
            elif '/personas/' in path_str:
                return 'PERSONA'
            elif '/modules/' in path_str:
                return 'PROMPT_MODULE'
            else:
                return 'PROMPT_ENGINEERING'
        
        # Development files
        if '/development/' in path_str:
            return 'DEVELOPMENT_MODULE'
        
        # Meta framework
        if '/meta/' in path_str:
            return 'META_MODULE'
        
        # Planning
        if '/planning/' in path_str:
            return 'PLANNING_MODULE'
        
        # Domain specific
        if '/domain/' in path_str:
            return 'DOMAIN_MODULE'
        
        # Archive
        if '/archive/' in path_str:
            return 'ARCHIVED'
        
        # Templates
        if '/template' in path_str:
            return 'TEMPLATE'
            
        # Documentation
        if 'readme' in path_str or content_lower.startswith('# '):
            return 'DOCUMENTATION'
            
        return 'UNKNOWN'
    
    def extract_version(self, content):
        """Extract version from version table or metadata"""
        # Look for version table
        version_match = re.search(r'\|\s*version\s*\|.*?\n\|[^|]*\|\s*([^|]+)\s*\|', content, re.IGNORECASE)
        if version_match:
            return version_match.group(1).strip()
        
        # Look for version in metadata
        version_match = re.search(r'version[:\s]+([0-9]+\.[0-9]+\.[0-9]+)', content, re.IGNORECASE)
        if version_match:
            return version_match.group(1)
            
        return None
    
    def extract_last_updated(self, content):
        """Extract last updated date"""
        date_match = re.search(r'\|\s*last_updated\s*\|.*?\n\|[^|]*\|\s*([^|]+)\s*\|', content, re.IGNORECASE)
        if date_match:
            return date_match.group(1).strip()
        
        # Look for other date patterns
        date_match = re.search(r'(20\d{2}-\d{2}-\d{2})', content)
        if date_match:
            return date_match.group(1)
            
        return None
    
    def extract_status(self, content):
        """Extract status from version table"""
        status_match = re.search(r'\|\s*status\s*\|.*?\n\|[^|]*\|\s*([^|]+)\s*\|', content, re.IGNORECASE)
        if status_match:
            return status_match.group(1).strip()
        return None
    
    def extract_dependencies(self, content):
        """Extract file dependencies (references to other .md files)"""
        # Find all .md references
        md_refs = re.findall(r'([a-zA-Z0-9_/-]+\.md)', content)
        
        # Clean and deduplicate
        dependencies = []
        for ref in md_refs:
            if ref not in dependencies and not ref.startswith('http'):
                dependencies.append(ref)
        
        return dependencies
    
    def determine_module_type(self, file_path, content):
        """Determine if this is a module, command, or other type"""
        if '<module' in content:
            return 'XML_MODULE'
        elif '<command' in content:
            return 'XML_COMMAND'
        elif '/commands/' in str(file_path):
            return 'COMMAND_FILE'
        elif '/modules/' in str(file_path):
            return 'MODULE_FILE'
        elif 'thinking_pattern' in content:
            return 'THINKING_PATTERN'
        else:
            return 'DOCUMENT'
    
    def calculate_complexity(self, content):
        """Calculate complexity score based on various factors"""
        score = 0
        
        # Base size factor
        score += len(content) // 1000  # 1 point per KB
        
        # XML structure adds complexity
        if '<module' in content or '<command' in content:
            score += 5
        
        # Many dependencies add complexity
        deps = len(re.findall(r'\.md', content))
        score += deps // 2
        
        # Code blocks add complexity
        code_blocks = len(re.findall(r'```', content))
        score += code_blocks
        
        # Sections add complexity
        sections = len(re.findall(r'^#', content, re.MULTILINE))
        score += sections
        
        return score
    
    def run_complete_analysis(self):
        """Run complete inventory analysis of all files"""
        print("🔍 Agent 1: Starting complete framework inventory analysis...")
        
        # Find all markdown files
        md_files = list(self.base_path.rglob("*.md"))
        self.total_files = len(md_files)
        
        print(f"📊 Found {self.total_files} markdown files to analyze")
        
        # Process each file
        for i, file_path in enumerate(md_files):
            self.progress = (i + 1) / self.total_files * 100
            
            if (i + 1) % 25 == 0:  # Progress updates
                print(f"⏳ Progress: {self.progress:.1f}% ({i+1}/{self.total_files}) - Current: {file_path.name}")
            
            metadata = self.analyze_file_metadata(file_path)
            self.inventory[str(file_path)] = metadata
            
            # Categorize for analysis
            category = metadata.get('category', 'UNKNOWN')
            self.categories[category].append(str(file_path))
            self.stats[category] += 1
        
        print(f"✅ Agent 1: Inventory analysis complete - {self.total_files} files processed")
        
        return self.generate_report()
    
    def generate_report(self):
        """Generate comprehensive inventory report"""
        report = {
            'analysis_timestamp': datetime.now().isoformat(),
            'agent': 'Agent 1 - Inventory Specialist',
            'total_files_analyzed': self.total_files,
            'progress_percentage': 100.0,
            'inventory': self.inventory,
            'category_distribution': dict(self.stats),
            'category_files': dict(self.categories),
            'summary_statistics': self.generate_summary_stats(),
            'critical_findings': self.identify_critical_findings(),
            'handoff_data': self.prepare_handoff_data()
        }
        
        return report
    
    def generate_summary_stats(self):
        """Generate summary statistics"""
        files = list(self.inventory.values())
        
        total_size = sum(f.get('size_bytes', 0) for f in files)
        total_lines = sum(f.get('line_count', 0) for f in files)
        
        complexity_scores = [f.get('complexity_score', 0) for f in files if 'error' not in f]
        
        return {
            'total_size_mb': round(total_size / (1024 * 1024), 2),
            'total_lines': total_lines,
            'average_file_size_kb': round(total_size / len(files) / 1024, 2),
            'average_complexity': round(sum(complexity_scores) / len(complexity_scores), 2) if complexity_scores else 0,
            'files_with_versions': len([f for f in files if f.get('version')]),
            'files_with_dependencies': len([f for f in files if f.get('dependencies')]),
            'xml_structured_files': len([f for f in files if f.get('has_xml_structure')]),
            'quality_gate_files': len([f for f in files if f.get('quality_gates')]),
            'largest_files': sorted(files, key=lambda x: x.get('size_bytes', 0), reverse=True)[:10],
            'most_complex_files': sorted(files, key=lambda x: x.get('complexity_score', 0), reverse=True)[:10]
        }
    
    def identify_critical_findings(self):
        """Identify critical issues for other agents"""
        findings = []
        
        files = list(self.inventory.values())
        
        # Check for expected critical components
        command_files = [f for f in files if f.get('category') == 'COMMAND']
        quality_modules = [f for f in files if f.get('category') == 'QUALITY_MODULE']
        
        if len(command_files) < 10:
            findings.append({
                'severity': 'HIGH',
                'type': 'MISSING_COMMANDS',
                'message': f"Only {len(command_files)} command files found, expected more",
                'impact': 'Agent 4 (Reality Tester) will find limited functionality'
            })
        
        # Check for broken files
        error_files = [f for f in files if 'error' in f]
        if error_files:
            findings.append({
                'severity': 'CRITICAL',
                'type': 'CORRUPTED_FILES',
                'message': f"{len(error_files)} files could not be read",
                'files': [f['path'] for f in error_files]
            })
        
        # Check for size anomalies  
        huge_files = [f for f in files if f.get('size_bytes', 0) > 100000]  # >100KB
        if huge_files:
            findings.append({
                'severity': 'MEDIUM',
                'type': 'OVERSIZED_FILES',
                'message': f"{len(huge_files)} files are unusually large (>100KB)",
                'files': [(f['path'], f.get('size_kb', 0)) for f in huge_files]
            })
        
        # Check category distribution
        if self.stats.get('UNKNOWN', 0) > self.total_files * 0.1:  # >10% unknown
            findings.append({
                'severity': 'MEDIUM',
                'type': 'CLASSIFICATION_ISSUES',
                'message': f"{self.stats['UNKNOWN']} files could not be classified ({self.stats['UNKNOWN']/self.total_files*100:.1f}%)"
            })
        
        return findings
    
    def prepare_handoff_data(self):
        """Prepare data needed by subsequent agents"""
        return {
            'agent_2_directory_audit': {
                'directory_categories': self.categories,
                'category_distribution': dict(self.stats),
                'structure_complexity': len(set(str(Path(f['path']).parent) for f in self.inventory.values()))
            },
            'agent_3_reference_analysis': {
                'files_with_dependencies': {
                    path: data['dependencies'] 
                    for path, data in self.inventory.items() 
                    if data.get('dependencies')
                },
                'reference_patterns': self.extract_reference_patterns(),
                'total_reference_count': sum(len(data.get('dependencies', [])) for data in self.inventory.values())
            },
            'agent_4_reality_testing': {
                'command_files': [
                    path for path, data in self.inventory.items() 
                    if data.get('category') == 'COMMAND'
                ],
                'quality_modules': [
                    path for path, data in self.inventory.items() 
                    if data.get('category') == 'QUALITY_MODULE'
                ],
                'integration_critical_files': self.identify_integration_critical_files()
            }
        }
    
    def extract_reference_patterns(self):
        """Extract patterns in how files reference each other"""
        patterns = defaultdict(int)
        
        for data in self.inventory.values():
            for dep in data.get('dependencies', []):
                # Count reference patterns
                if dep.startswith('system/'):
                    patterns['system_references'] += 1
                elif dep.startswith('patterns/'):
                    patterns['pattern_references'] += 1
                elif dep.startswith('modules/'):
                    patterns['module_references'] += 1
                elif '../' in dep:
                    patterns['relative_references'] += 1
                else:
                    patterns['other_references'] += 1
        
        return dict(patterns)
    
    def identify_integration_critical_files(self):
        """Identify files critical for integration testing"""
        critical = []
        
        for path, data in self.inventory.items():
            # Critical if it's a command
            if data.get('category') == 'COMMAND':
                critical.append({
                    'path': path,
                    'reason': 'Command file - must work in Claude Code',
                    'priority': 'HIGH'
                })
            
            # Critical if it has many dependencies
            elif len(data.get('dependencies', [])) > 5:
                critical.append({
                    'path': path,
                    'reason': f"High dependency count ({len(data['dependencies'])})",
                    'priority': 'MEDIUM'
                })
            
            # Critical if it's a quality gate
            elif data.get('quality_gates'):
                critical.append({
                    'path': path,
                    'reason': 'Quality gate - framework functionality depends on this',
                    'priority': 'HIGH'
                })
        
        return critical
    
    def save_results(self, output_file="agent1_inventory_results.json"):
        """Save analysis results to file"""
        report = self.generate_report()
        
        with open(output_file, 'w') as f:
            json.dump(report, f, indent=2)
        
        print(f"💾 Agent 1: Results saved to {output_file}")
        return report

if __name__ == "__main__":
    analyst = FrameworkInventoryAnalyst()
    report = analyst.run_complete_analysis()
    analyst.save_results()
    
    # Print summary for immediate visibility
    print("\n" + "="*80)
    print("AGENT 1 INVENTORY ANALYSIS SUMMARY")
    print("="*80)
    print(f"📊 Total Files: {report['total_files_analyzed']}")
    print(f"📁 Categories: {len(report['category_distribution'])}")
    print(f"⚖️  Total Size: {report['summary_statistics']['total_size_mb']} MB")
    print(f"🔗 Files with Dependencies: {report['summary_statistics']['files_with_dependencies']}")
    print(f"⚠️  Critical Findings: {len(report['critical_findings'])}")
    
    print("\nCategory Distribution:")
    for category, count in sorted(report['category_distribution'].items()):
        print(f"  {category}: {count} files")
    
    if report['critical_findings']:
        print("\n🚨 Critical Findings:")
        for finding in report['critical_findings']:
            print(f"  {finding['severity']}: {finding['message']}")
    
    print(f"\n✅ Agent 1 Complete - Ready for handoff to Agents 2, 3, and 4")