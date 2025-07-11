#!/usr/bin/env python3
"""
Script Validation Tool for Claude Code Modular Prompts Framework

Triple checks all scripts for duplications, conflicts, and overlapping functionality
to ensure clean, non-redundant codebase.

Author: Claude Code Framework  
Version: 1.0.0
Date: 2025-07-11
"""

import ast
import os
import re
import hashlib
from pathlib import Path
from typing import Dict, List, Any, Set, Tuple, Optional
import logging
from collections import defaultdict
import difflib


class ScriptValidator:
    """
    Validates scripts for duplications, conflicts, and overlapping functionality.
    """
    
    def __init__(self, scripts_dir: Optional[str] = None):
        """
        Initialize script validator.
        
        Args:
            scripts_dir: Path to scripts directory (default: auto-detect)
        """
        if scripts_dir:
            self.scripts_dir = Path(scripts_dir)
        else:
            # Auto-detect scripts directory
            current = Path.cwd()
            while current != current.parent:
                candidate = current / 'scripts'
                if candidate.exists():
                    self.scripts_dir = candidate
                    break
                current = current.parent
            else:
                self.scripts_dir = Path.cwd() / 'scripts'
        
        self.logger = logging.getLogger(__name__)
        
        # Track script analysis results
        self.script_metadata = {}
        self.function_signatures = defaultdict(list)
        self.class_signatures = defaultdict(list)
        self.import_patterns = defaultdict(list)
        self.code_hashes = defaultdict(list)
    
    def analyze_all_scripts(self) -> Dict[str, Any]:
        """
        Analyze all Python scripts in the scripts directory.
        
        Returns:
            Comprehensive analysis results
        """
        analysis = {
            'total_scripts': 0,
            'analyzed_scripts': 0,
            'failed_analysis': [],
            'duplications': [],
            'conflicts': [],
            'overlaps': [],
            'recommendations': [],
            'script_details': {}
        }
        
        # Find all Python scripts
        python_files = list(self.scripts_dir.rglob('*.py'))
        analysis['total_scripts'] = len(python_files)
        
        # Analyze each script
        for script_path in python_files:
            try:
                script_analysis = self._analyze_script(script_path)
                analysis['script_details'][str(script_path)] = script_analysis
                analysis['analyzed_scripts'] += 1
            except Exception as e:
                analysis['failed_analysis'].append({
                    'script': str(script_path),
                    'error': str(e)
                })
                self.logger.warning(f"Failed to analyze {script_path}: {e}")
        
        # Check for duplications and conflicts
        analysis['duplications'] = self._find_duplications()
        analysis['conflicts'] = self._find_conflicts()
        analysis['overlaps'] = self._find_functionality_overlaps()
        analysis['recommendations'] = self._generate_recommendations(analysis)
        
        return analysis
    
    def _analyze_script(self, script_path: Path) -> Dict[str, Any]:
        """Analyze a single Python script."""
        with open(script_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Parse AST
        try:
            tree = ast.parse(content)
        except SyntaxError as e:
            return {
                'error': f"Syntax error: {e}",
                'valid': False
            }
        
        analysis = {
            'path': str(script_path),
            'name': script_path.stem,
            'size_bytes': len(content),
            'line_count': len(content.split('\n')),
            'valid': True,
            'functions': [],
            'classes': [],
            'imports': [],
            'main_function': False,
            'cli_interface': False,
            'docstring': None,
            'purpose': None,
            'code_hash': hashlib.md5(content.encode()).hexdigest()
        }
        
        # Extract docstring and purpose
        if tree.body and isinstance(tree.body[0], ast.Expr) and isinstance(tree.body[0].value, ast.Constant):
            analysis['docstring'] = tree.body[0].value.value
            analysis['purpose'] = self._extract_purpose_from_docstring(analysis['docstring'])
        
        # Analyze AST nodes
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                func_info = {
                    'name': node.name,
                    'args': [arg.arg for arg in node.args.args],
                    'lineno': node.lineno,
                    'is_private': node.name.startswith('_'),
                    'has_docstring': (node.body and isinstance(node.body[0], ast.Expr) 
                                    and isinstance(node.body[0].value, ast.Constant))
                }
                analysis['functions'].append(func_info)
                
                # Track function signatures globally
                signature = f"{node.name}({', '.join(func_info['args'])})"
                self.function_signatures[signature].append(str(script_path))
                
                if node.name == 'main':
                    analysis['main_function'] = True
                    
            elif isinstance(node, ast.ClassDef):
                class_info = {
                    'name': node.name,
                    'lineno': node.lineno,
                    'methods': [],
                    'has_docstring': (node.body and isinstance(node.body[0], ast.Expr) 
                                    and isinstance(node.body[0].value, ast.Constant))
                }
                
                # Extract methods
                for item in node.body:
                    if isinstance(item, ast.FunctionDef):
                        class_info['methods'].append(item.name)
                
                analysis['classes'].append(class_info)
                
                # Track class signatures globally
                self.class_signatures[node.name].append(str(script_path))
                
            elif isinstance(node, ast.Import):
                for alias in node.names:
                    import_info = {
                        'module': alias.name,
                        'alias': alias.asname,
                        'type': 'import'
                    }
                    analysis['imports'].append(import_info)
                    self.import_patterns[alias.name].append(str(script_path))
                    
            elif isinstance(node, ast.ImportFrom):
                if node.module:
                    for alias in node.names:
                        import_info = {
                            'module': node.module,
                            'name': alias.name,
                            'alias': alias.asname,
                            'type': 'from_import'
                        }
                        analysis['imports'].append(import_info)
                        self.import_patterns[f"{node.module}.{alias.name}"].append(str(script_path))
        
        # Check for CLI interface patterns
        if any('argparse' in imp.get('module', '') for imp in analysis['imports']):
            analysis['cli_interface'] = True
        
        # Store in global metadata
        self.script_metadata[str(script_path)] = analysis
        
        # Track code similarity
        content_hash = hashlib.md5(content.encode()).hexdigest()
        self.code_hashes[content_hash].append(str(script_path))
        
        return analysis
    
    def _extract_purpose_from_docstring(self, docstring: str) -> Optional[str]:
        """Extract purpose from module docstring."""
        if not docstring:
            return None
        
        lines = docstring.strip().split('\n')
        # Look for the first substantial line as purpose
        for line in lines:
            line = line.strip()
            if line and not line.startswith('"""') and len(line) > 10:
                return line
        
        return None
    
    def _find_duplications(self) -> List[Dict[str, Any]]:
        """Find duplicate code and functionality."""
        duplications = []
        
        # Check for identical code hashes
        for code_hash, scripts in self.code_hashes.items():
            if len(scripts) > 1:
                duplications.append({
                    'type': 'identical_code',
                    'severity': 'high',
                    'scripts': scripts,
                    'description': 'Scripts with identical code content'
                })
        
        # Check for duplicate function signatures
        for signature, scripts in self.function_signatures.items():
            if len(scripts) > 1:
                duplications.append({
                    'type': 'duplicate_function',
                    'severity': 'medium',
                    'function': signature,
                    'scripts': scripts,
                    'description': f'Function {signature} defined in multiple scripts'
                })
        
        # Check for duplicate class names
        for class_name, scripts in self.class_signatures.items():
            if len(scripts) > 1:
                duplications.append({
                    'type': 'duplicate_class',
                    'severity': 'medium',
                    'class': class_name,
                    'scripts': scripts,
                    'description': f'Class {class_name} defined in multiple scripts'
                })
        
        return duplications
    
    def _find_conflicts(self) -> List[Dict[str, Any]]:
        """Find potential conflicts between scripts."""
        conflicts = []
        
        # Check for naming conflicts
        script_names = defaultdict(list)
        for script_path in self.script_metadata.keys():
            name = Path(script_path).stem
            script_names[name].append(script_path)
        
        for name, scripts in script_names.items():
            if len(scripts) > 1:
                conflicts.append({
                    'type': 'naming_conflict',
                    'severity': 'low',
                    'name': name,
                    'scripts': scripts,
                    'description': f'Multiple scripts with similar names: {name}'
                })
        
        # Check for import conflicts
        common_imports = ['logging', 'argparse', 'pathlib', 'json']
        for import_name, scripts in self.import_patterns.items():
            if import_name not in common_imports and len(scripts) > 3:
                conflicts.append({
                    'type': 'import_pattern',
                    'severity': 'low',
                    'import': import_name,
                    'scripts': scripts,
                    'description': f'Import {import_name} used in many scripts - consider shared module'
                })
        
        return conflicts
    
    def _find_functionality_overlaps(self) -> List[Dict[str, Any]]:
        """Find overlapping functionality between scripts."""
        overlaps = []
        
        # Group scripts by purpose keywords
        purpose_groups = defaultdict(list)
        keywords = ['config', 'validate', 'template', 'optimize', 'monitor', 'test', 'performance']
        
        for script_path, metadata in self.script_metadata.items():
            purpose = metadata.get('purpose') or ''
            name = metadata.get('name') or ''
            
            for keyword in keywords:
                if keyword in purpose.lower() or keyword in name.lower():
                    purpose_groups[keyword].append({
                        'script': script_path,
                        'name': name,
                        'purpose': purpose
                    })
        
        # Check for potential overlaps
        for keyword, scripts in purpose_groups.items():
            if len(scripts) > 1:
                # Check if scripts have similar purposes
                purposes = [s['purpose'] for s in scripts if s['purpose']]
                if len(purposes) > 1:
                    similarity_found = False
                    for i, purpose1 in enumerate(purposes):
                        for purpose2 in purposes[i+1:]:
                            if purpose1 and purpose2:
                                similarity = difflib.SequenceMatcher(None, purpose1.lower(), purpose2.lower()).ratio()
                                if similarity > 0.6:  # 60% similarity threshold
                                    similarity_found = True
                                    break
                        if similarity_found:
                            break
                    
                    if similarity_found:
                        overlaps.append({
                            'type': 'functionality_overlap',
                            'severity': 'medium',
                            'keyword': keyword,
                            'scripts': [s['script'] for s in scripts],
                            'purposes': purposes,
                            'description': f'Scripts with potentially overlapping {keyword} functionality'
                        })
        
        return overlaps
    
    def _generate_recommendations(self, analysis: Dict[str, Any]) -> List[str]:
        """Generate recommendations based on analysis."""
        recommendations = []
        
        # Recommendations based on duplications
        if analysis['duplications']:
            high_severity = [d for d in analysis['duplications'] if d['severity'] == 'high']
            if high_severity:
                recommendations.append("CRITICAL: Remove identical duplicate scripts immediately")
            
            medium_severity = [d for d in analysis['duplications'] if d['severity'] == 'medium']
            if medium_severity:
                recommendations.append("Consolidate duplicate functions/classes into shared modules")
        
        # Recommendations based on overlaps
        if analysis['overlaps']:
            recommendations.append("Review scripts with overlapping functionality for consolidation opportunities")
        
        # General recommendations
        failed_count = len(analysis['failed_analysis'])
        if failed_count > 0:
            recommendations.append(f"Fix {failed_count} scripts with analysis failures")
        
        # Script organization recommendations
        total_scripts = analysis['total_scripts']
        if total_scripts > 20:
            recommendations.append("Consider organizing scripts into subdirectories by functionality")
        
        return recommendations
    
    def generate_validation_report(self, analysis: Dict[str, Any]) -> str:
        """Generate comprehensive validation report."""
        
        report = f"""# Script Validation Report

**Date:** 2025-07-11  
**Scripts Directory:** {self.scripts_dir}  
**Total Scripts:** {analysis['total_scripts']}  
**Successfully Analyzed:** {analysis['analyzed_scripts']}  
**Analysis Failures:** {len(analysis['failed_analysis'])}

## Summary

**Duplications Found:** {len(analysis['duplications'])}  
**Conflicts Found:** {len(analysis['conflicts'])}  
**Functionality Overlaps:** {len(analysis['overlaps'])}

## Validation Status

{'🟢 PASS - No critical issues found' if not any(d['severity'] == 'high' for d in analysis['duplications']) else '🔴 FAIL - Critical duplications found'}

"""
        
        # Report duplications
        if analysis['duplications']:
            report += "\n## 🔍 Duplications Found\n\n"
            for dup in analysis['duplications']:
                severity_icon = {'high': '🔴', 'medium': '🟡', 'low': '🟡'}.get(dup['severity'], '🟡')
                report += f"### {severity_icon} {dup['type'].replace('_', ' ').title()}\n"
                report += f"**Severity:** {dup['severity'].upper()}  \n"
                report += f"**Description:** {dup['description']}  \n"
                if 'scripts' in dup:
                    report += f"**Scripts:**\n"
                    for script in dup['scripts']:
                        script_name = Path(script).name
                        report += f"- `{script_name}`\n"
                report += "\n"
        
        # Report conflicts
        if analysis['conflicts']:
            report += "\n## ⚠️ Conflicts Found\n\n"
            for conflict in analysis['conflicts']:
                report += f"### {conflict['type'].replace('_', ' ').title()}\n"
                report += f"**Description:** {conflict['description']}  \n"
                if 'scripts' in conflict:
                    report += f"**Affected Scripts:** {len(conflict['scripts'])}  \n"
                report += "\n"
        
        # Report overlaps
        if analysis['overlaps']:
            report += "\n## 🔄 Functionality Overlaps\n\n"
            for overlap in analysis['overlaps']:
                report += f"### {overlap['keyword'].title()} Functionality\n"
                report += f"**Scripts:** {len(overlap['scripts'])}  \n"
                report += f"**Description:** {overlap['description']}  \n"
                report += "\n"
        
        # Report analysis failures
        if analysis['failed_analysis']:
            report += "\n## ❌ Analysis Failures\n\n"
            for failure in analysis['failed_analysis']:
                script_name = Path(failure['script']).name
                report += f"- **{script_name}:** {failure['error']}\n"
        
        # Recommendations
        if analysis['recommendations']:
            report += "\n## 💡 Recommendations\n\n"
            for i, rec in enumerate(analysis['recommendations'], 1):
                report += f"{i}. {rec}\n"
        
        # Script inventory
        report += f"\n## 📋 Script Inventory\n\n"
        report += f"**Total Scripts:** {analysis['total_scripts']}\n\n"
        
        # Group scripts by category
        categories = defaultdict(list)
        for script_path, details in analysis['script_details'].items():
            script_name = Path(script_path).name
            if 'framework' in script_path:
                categories['Framework'].append(script_name)
            elif 'routing' in script_path:
                categories['Routing'].append(script_name)
            elif any(keyword in script_name for keyword in ['test', 'validate']):
                categories['Testing'].append(script_name)
            elif any(keyword in script_name for keyword in ['monitor', 'performance']):
                categories['Monitoring'].append(script_name)
            else:
                categories['General'].append(script_name)
        
        for category, scripts in categories.items():
            if scripts:
                report += f"### {category} ({len(scripts)} scripts)\n"
                for script in sorted(scripts):
                    report += f"- `{script}`\n"
                report += "\n"
        
        return report
    
    def check_specific_duplications(self) -> Dict[str, Any]:
        """Check for specific types of duplications the user is concerned about."""
        
        # Scripts that might be duplicated based on functionality
        config_scripts = []
        validation_scripts = []
        template_scripts = []
        
        for script_path, metadata in self.script_metadata.items():
            name = (metadata.get('name') or '').lower()
            purpose = (metadata.get('purpose') or '').lower()
            
            if 'config' in name or 'config' in purpose:
                config_scripts.append(script_path)
            if 'valid' in name or 'valid' in purpose:
                validation_scripts.append(script_path)
            if 'template' in name or 'template' in purpose:
                template_scripts.append(script_path)
        
        results = {
            'config_related': {
                'count': len(config_scripts),
                'scripts': config_scripts,
                'potential_overlap': len(config_scripts) > 2
            },
            'validation_related': {
                'count': len(validation_scripts),
                'scripts': validation_scripts,
                'potential_overlap': len(validation_scripts) > 2
            },
            'template_related': {
                'count': len(template_scripts),
                'scripts': template_scripts,
                'potential_overlap': len(template_scripts) > 1
            }
        }
        
        return results


def main():
    """CLI interface for script validation."""
    import argparse
    import json
    
    parser = argparse.ArgumentParser(description="Script Validation Tool")
    parser.add_argument('--scripts-dir', help="Scripts directory path")
    parser.add_argument('--report', help="Generate validation report to file")
    parser.add_argument('--check-duplications', action='store_true', help="Check specific duplications")
    parser.add_argument('--json', action='store_true', help="Output results as JSON")
    parser.add_argument('--verbose', '-v', action='store_true', help="Verbose output")
    
    args = parser.parse_args()
    
    # Setup logging
    level = logging.DEBUG if args.verbose else logging.INFO
    logging.basicConfig(level=level, format='%(levelname)s: %(message)s')
    
    validator = ScriptValidator(scripts_dir=args.scripts_dir)
    
    try:
        if args.check_duplications:
            results = validator.check_specific_duplications()
            if args.json:
                print(json.dumps(results, indent=2))
            else:
                print("Specific Duplication Check Results:")
                for category, data in results.items():
                    print(f"\n{category.replace('_', ' ').title()}:")
                    print(f"  Count: {data['count']}")
                    print(f"  Potential Overlap: {data['potential_overlap']}")
                    if data['scripts']:
                        print(f"  Scripts:")
                        for script in data['scripts']:
                            print(f"    - {Path(script).name}")
        
        else:
            analysis = validator.analyze_all_scripts()
            
            if args.json:
                print(json.dumps(analysis, indent=2))
            elif args.report:
                report = validator.generate_validation_report(analysis)
                with open(args.report, 'w') as f:
                    f.write(report)
                print(f"Validation report saved to {args.report}")
            else:
                # Brief summary
                print(f"Script Validation Summary:")
                print(f"  Total Scripts: {analysis['total_scripts']}")
                print(f"  Analyzed: {analysis['analyzed_scripts']}")
                print(f"  Duplications: {len(analysis['duplications'])}")
                print(f"  Conflicts: {len(analysis['conflicts'])}")
                print(f"  Overlaps: {len(analysis['overlaps'])}")
                
                critical_issues = [d for d in analysis['duplications'] if d['severity'] == 'high']
                if critical_issues:
                    print(f"  🔴 CRITICAL: {len(critical_issues)} high-severity duplications found!")
                else:
                    print(f"  🟢 No critical duplications found")
    
    except Exception as e:
        logging.error(f"Error: {e}")
        return 1
    
    return 0


if __name__ == "__main__":
    exit(main())