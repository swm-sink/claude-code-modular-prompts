#!/usr/bin/env python3
"""
Agent V15: Module Documentation Auditor
Analyzes modules for documentation quality and completeness
"""

import os
import re
from pathlib import Path
from collections import defaultdict
import json

class ModuleDocAuditor:
    def __init__(self, base_path=".claude"):
        self.base_path = Path(base_path)
        self.modules = []
        self.doc_stats = defaultdict(dict)
        
    def find_modules(self):
        """Find all .md module files"""
        patterns = ["modules/**/*.md", "patterns/**/*.md", "prompt_eng/**/*.md"]
        
        for pattern in patterns:
            for path in self.base_path.glob(pattern):
                if path.name != "README.md":
                    self.modules.append(path)
                    
    def check_module_documentation(self, module_path):
        """Check documentation quality of a module"""
        with open(module_path, 'r') as f:
            content = f.read()
            
        stats = {
            'path': str(module_path),
            'name': module_path.stem,
            'category': module_path.parts[2] if len(module_path.parts) > 2 else 'root',
            'has_title': bool(re.search(r'^#\s+\w+', content, re.MULTILINE)),
            'has_purpose': bool(re.search(r'(?i)(purpose|overview|description):', content)),
            'has_usage_examples': bool(re.search(r'(?i)(usage|example|how to use):', content)),
            'has_interface': bool(re.search(r'(?i)(interface|input|output|parameters):', content)),
            'has_dependencies': bool(re.search(r'(?i)(dependencies|requires|imports):', content)),
            'has_error_handling': bool(re.search(r'(?i)(error|exception|failure|recovery):', content)),
            'has_thinking_pattern': bool(re.search(r'<thinking_pattern>', content)),
            'has_implementation': bool(re.search(r'<implementation>', content)),
            'line_count': len(content.splitlines()),
            'has_xml_structure': '<' in content and '>' in content,
            'readme_exists': (module_path.parent / 'README.md').exists()
        }
        
        # Calculate documentation score
        criteria = ['has_title', 'has_purpose', 'has_usage_examples', 'has_interface',
                   'has_dependencies', 'has_error_handling']
        stats['doc_score'] = sum(1 for c in criteria if stats[c]) / len(criteria) * 100
        
        # Check for critical modules (based on previous agent findings)
        critical_patterns = ['tdd', 'routing', 'multi-agent', 'session', 'quality', 
                           'thinking-pattern', 'module-composition']
        stats['is_critical'] = any(pattern in str(module_path).lower() for pattern in critical_patterns)
        
        return stats
        
    def analyze_all_modules(self):
        """Analyze all modules"""
        self.find_modules()
        
        for module in self.modules:
            stats = self.check_module_documentation(module)
            category = stats['category']
            self.doc_stats[category][stats['name']] = stats
            
    def generate_summary(self):
        """Generate summary statistics"""
        summary = {
            'total_modules': len(self.modules),
            'categories': {},
            'overall_stats': {
                'avg_doc_score': 0,
                'with_examples': 0,
                'with_interface': 0,
                'with_dependencies': 0,
                'with_error_handling': 0,
                'critical_well_documented': 0,
                'critical_poorly_documented': 0
            },
            'missing_docs': {
                'no_purpose': [],
                'no_examples': [],
                'no_interface': [],
                'no_error_handling': []
            }
        }
        
        all_scores = []
        
        for category, modules in self.doc_stats.items():
            cat_scores = []
            for name, stats in modules.items():
                all_scores.append(stats['doc_score'])
                cat_scores.append(stats['doc_score'])
                
                # Track overall stats
                if stats['has_usage_examples']:
                    summary['overall_stats']['with_examples'] += 1
                if stats['has_interface']:
                    summary['overall_stats']['with_interface'] += 1
                if stats['has_dependencies']:
                    summary['overall_stats']['with_dependencies'] += 1
                if stats['has_error_handling']:
                    summary['overall_stats']['with_error_handling'] += 1
                    
                # Track critical modules
                if stats['is_critical']:
                    if stats['doc_score'] >= 80:
                        summary['overall_stats']['critical_well_documented'] += 1
                    else:
                        summary['overall_stats']['critical_poorly_documented'] += 1
                
                # Track missing documentation
                if not stats['has_purpose']:
                    summary['missing_docs']['no_purpose'].append(stats['path'])
                if not stats['has_usage_examples']:
                    summary['missing_docs']['no_examples'].append(stats['path'])
                if not stats['has_interface']:
                    summary['missing_docs']['no_interface'].append(stats['path'])
                if not stats['has_error_handling']:
                    summary['missing_docs']['no_error_handling'].append(stats['path'])
                    
            summary['categories'][category] = {
                'count': len(modules),
                'avg_doc_score': sum(cat_scores) / len(cat_scores) if cat_scores else 0
            }
            
        summary['overall_stats']['avg_doc_score'] = sum(all_scores) / len(all_scores) if all_scores else 0
        
        # Convert counts to percentages
        total = len(self.modules)
        for key in ['with_examples', 'with_interface', 'with_dependencies', 'with_error_handling']:
            summary['overall_stats'][f'{key}_pct'] = (summary['overall_stats'][key] / total * 100) if total > 0 else 0
            
        return summary
        
    def generate_report(self):
        """Generate detailed documentation report"""
        summary = self.generate_summary()
        
        report = []
        report.append("# Module Documentation Audit Report")
        report.append(f"\nTotal Modules Analyzed: {summary['total_modules']}")
        report.append(f"Average Documentation Score: {summary['overall_stats']['avg_doc_score']:.1f}%")
        report.append("\n## Documentation Coverage")
        report.append(f"- With usage examples: {summary['overall_stats']['with_examples_pct']:.1f}%")
        report.append(f"- With interface docs: {summary['overall_stats']['with_interface_pct']:.1f}%")
        report.append(f"- With dependencies: {summary['overall_stats']['with_dependencies_pct']:.1f}%")
        report.append(f"- With error handling: {summary['overall_stats']['with_error_handling_pct']:.1f}%")
        
        report.append("\n## Critical Modules")
        report.append(f"- Well documented: {summary['overall_stats']['critical_well_documented']}")
        report.append(f"- Poorly documented: {summary['overall_stats']['critical_poorly_documented']}")
        
        report.append("\n## Category Breakdown")
        for category, stats in sorted(summary['categories'].items()):
            report.append(f"- {category}: {stats['count']} modules, {stats['avg_doc_score']:.1f}% avg score")
            
        report.append("\n## Modules Needing Documentation")
        
        if summary['missing_docs']['no_purpose']:
            report.append(f"\n### Missing Purpose ({len(summary['missing_docs']['no_purpose'])} modules)")
            for path in summary['missing_docs']['no_purpose'][:10]:
                report.append(f"- {path}")
            if len(summary['missing_docs']['no_purpose']) > 10:
                report.append(f"- ... and {len(summary['missing_docs']['no_purpose']) - 10} more")
                
        if summary['missing_docs']['no_examples']:
            report.append(f"\n### Missing Examples ({len(summary['missing_docs']['no_examples'])} modules)")
            for path in summary['missing_docs']['no_examples'][:10]:
                report.append(f"- {path}")
            if len(summary['missing_docs']['no_examples']) > 10:
                report.append(f"- ... and {len(summary['missing_docs']['no_examples']) - 10} more")
                
        # Save detailed stats
        with open('module-doc-stats.json', 'w') as f:
            json.dump({
                'summary': summary,
                'detailed': dict(self.doc_stats)
            }, f, indent=2)
            
        return '\n'.join(report)
        
    def find_critical_modules(self):
        """Identify critical modules based on usage patterns and dependencies"""
        critical = []
        
        for category, modules in self.doc_stats.items():
            for name, stats in modules.items():
                if stats['is_critical'] and stats['doc_score'] < 80:
                    critical.append({
                        'path': stats['path'],
                        'score': stats['doc_score'],
                        'missing': [
                            k.replace('has_', '') for k, v in stats.items() 
                            if k.startswith('has_') and not v
                        ]
                    })
                    
        return sorted(critical, key=lambda x: x['score'])

if __name__ == "__main__":
    auditor = ModuleDocAuditor()
    auditor.analyze_all_modules()
    
    print(auditor.generate_report())
    
    # List critical modules needing attention
    critical = auditor.find_critical_modules()
    if critical:
        print("\n## Critical Modules Needing Documentation")
        for module in critical[:10]:
            print(f"- {module['path']} (score: {module['score']:.0f}%, missing: {', '.join(module['missing'])})")