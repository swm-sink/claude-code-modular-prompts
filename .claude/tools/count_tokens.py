#!/usr/bin/env python3
"""
Token Counting and Optimization Validation Script for Claude Framework
Counts tokens and validates adherence to budget constraints
"""

from pathlib import Path
from typing import Dict, List, Tuple
import json
import re

class TokenCounter:
    def __init__(self, framework_root: str):
        self.framework_root = Path(framework_root)
        self.results = {}
        
    def count_tokens(self, text: str) -> int:
        """Estimate tokens using word-based approximation (1 token ≈ 0.75 words)"""
        # Remove extra whitespace and split into words
        words = re.findall(r'\S+', text)
        # Rough approximation: 1 token ≈ 0.75 words, or ~1.33 tokens per word
        return int(len(words) * 1.33)
    
    def analyze_file(self, file_path: Path) -> Dict:
        """Analyze a single file for token count and metadata"""
        try:
            content = file_path.read_text(encoding='utf-8')
            token_count = self.count_tokens(content)
            
            # Get relative path, handling files outside framework root
            try:
                relative_path = file_path.relative_to(self.framework_root)
                path_str = str(relative_path)
            except ValueError:
                # File is outside framework root (like CLAUDE.md)
                relative_path = file_path.name
                path_str = f"../{file_path.name}"
            
            category = self.categorize_file(Path(path_str))
            
            return {
                'path': path_str,
                'tokens': token_count,
                'category': category,
                'size_bytes': len(content.encode('utf-8')),
                'lines': len(content.split('\n'))
            }
        except Exception as e:
            return {
                'path': str(file_path.name),
                'tokens': 0,
                'category': 'error',
                'error': str(e)
            }
    
    def categorize_file(self, relative_path: Path) -> str:
        """Categorize file based on path"""
        path_str = str(relative_path)
        
        if path_str in ['README.md', '../CLAUDE.md', 'PERMISSION_VALIDATION.md'] or path_str.endswith('CLAUDE.md'):
            return 'foundation'
        elif path_str.startswith('commands/'):
            return 'command'
        elif path_str.startswith('modules/'):
            return 'module'
        elif path_str.startswith('archive/'):
            return 'archive'
        else:
            return 'other'
    
    def analyze_all_files(self) -> Dict:
        """Analyze all markdown files in the framework"""
        md_files = list(self.framework_root.rglob("*.md"))
        
        # Also analyze CLAUDE.md in parent directory
        claude_md = self.framework_root.parent / "CLAUDE.md"
        if claude_md.exists():
            md_files.append(claude_md)
        
        results = {
            'files': [],
            'summary': {
                'total_files': 0,
                'total_tokens': 0,
                'by_category': {}
            }
        }
        
        for file_path in md_files:
            file_result = self.analyze_file(file_path)
            results['files'].append(file_result)
        
        # Calculate summary statistics
        self.calculate_summary(results)
        
        return results
    
    def calculate_summary(self, results: Dict):
        """Calculate summary statistics"""
        summary = results['summary']
        summary['total_files'] = len(results['files'])
        summary['total_tokens'] = sum(f['tokens'] for f in results['files'])
        
        # Group by category
        by_category = {}
        for file_data in results['files']:
            category = file_data['category']
            if category not in by_category:
                by_category[category] = {
                    'count': 0,
                    'tokens': 0,
                    'files': []
                }
            
            by_category[category]['count'] += 1
            by_category[category]['tokens'] += file_data['tokens']
            by_category[category]['files'].append(file_data)
        
        summary['by_category'] = by_category
    
    def validate_budgets(self, results: Dict) -> List[str]:
        """Validate token budgets against targets"""
        violations = []
        
        # Budget constraints
        budgets = {
            'foundation': 3000,  # Foundation files <3k each
            'command': 4000,     # Command files <4k each  
            'module': 2000,      # Module files <2k each
            'total': 120000      # Total framework <120k
        }
        
        # Check total budget
        total_tokens = results['summary']['total_tokens']
        if total_tokens > budgets['total']:
            violations.append(f"Total framework tokens ({total_tokens:,}) exceeds budget ({budgets['total']:,})")
        
        # Check per-category budgets
        for category, budget in budgets.items():
            if category == 'total':
                continue
                
            if category in results['summary']['by_category']:
                category_data = results['summary']['by_category'][category]
                
                # Check individual files in category
                for file_data in category_data['files']:
                    if file_data['tokens'] > budget:
                        violations.append(
                            f"{category.title()} file '{file_data['path']}' "
                            f"({file_data['tokens']:,} tokens) exceeds budget ({budget:,})"
                        )
        
        return violations
    
    def generate_report(self, results: Dict) -> str:
        """Generate comprehensive token analysis report"""
        report = []
        report.append("=" * 80)
        report.append("CLAUDE FRAMEWORK TOKEN ANALYSIS REPORT")
        report.append("=" * 80)
        report.append("")
        
        # Summary
        summary = results['summary']
        report.append("SUMMARY STATISTICS:")
        report.append(f"- Total files analyzed: {summary['total_files']}")
        report.append(f"- Total tokens: {summary['total_tokens']:,}")
        report.append("")
        
        # By category
        report.append("TOKEN DISTRIBUTION BY CATEGORY:")
        report.append("-" * 40)
        
        for category, data in summary['by_category'].items():
            report.append(f"{category.upper()}:")
            report.append(f"  Files: {data['count']}")
            report.append(f"  Tokens: {data['tokens']:,}")
            report.append(f"  Average: {data['tokens'] // data['count']:,} tokens/file")
            report.append("")
        
        # Budget validation
        violations = self.validate_budgets(results)
        if violations:
            report.append("BUDGET VIOLATIONS:")
            report.append("-" * 40)
            for violation in violations:
                report.append(f"  ❌ {violation}")
            report.append("")
        else:
            report.append("✅ ALL BUDGET CONSTRAINTS MET")
            report.append("")
        
        # Detailed file listing
        report.append("DETAILED FILE ANALYSIS:")
        report.append("-" * 40)
        
        # Sort files by token count (highest first)
        sorted_files = sorted(results['files'], key=lambda x: x['tokens'], reverse=True)
        
        for file_data in sorted_files:
            if 'error' in file_data:
                report.append(f"❌ {file_data['path']}: {file_data['error']}")
            else:
                tokens = file_data['tokens']
                category = file_data['category']
                
                # Determine status
                status = "✅"
                if category == 'foundation' and tokens > 3000:
                    status = "❌"
                elif category == 'command' and tokens > 4000:
                    status = "❌"
                elif category == 'module' and tokens > 2000:
                    status = "❌"
                
                report.append(
                    f"{status} {file_data['path']} "
                    f"({tokens:,} tokens, {category})"
                )
        
        report.append("")
        report.append("=" * 80)
        
        return "\n".join(report)
    
    def save_detailed_results(self, results: Dict, output_file: Path):
        """Save detailed results as JSON for further analysis"""
        with open(output_file, 'w') as f:
            json.dump(results, f, indent=2)

def main():
    framework_root = "/Users/smenssink/Documents/Github personal projects/claude-code-modular-agents/.claude"
    
    counter = TokenCounter(framework_root)
    results = counter.analyze_all_files()
    report = counter.generate_report(results)
    
    print(report)
    
    # Save detailed results
    results_file = Path(framework_root) / "token_analysis.json"
    counter.save_detailed_results(results, results_file)
    
    # Save report
    report_file = Path(framework_root) / "token_report.txt"
    report_file.write_text(report)
    
    print(f"\nDetailed results saved to: {results_file}")
    print(f"Report saved to: {report_file}")
    
    # Return appropriate exit code
    violations = counter.validate_budgets(results)
    return 1 if violations else 0

if __name__ == "__main__":
    import sys
    sys.exit(main())