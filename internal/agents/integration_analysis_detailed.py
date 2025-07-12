#!/usr/bin/env python3
"""
Comprehensive Integration Analysis for Claude Code Modular Prompts Framework 3.0
Performs detailed analysis of all integration points and generates actionable reports.
"""

import os
import json
import xml.etree.ElementTree as ET
from pathlib import Path
from datetime import datetime
import re

class FrameworkIntegrationAnalyzer:
    def __init__(self):
        self.claude_dir = Path('.claude')
        self.results = {
            'timestamp': datetime.now().isoformat(),
            'framework_version': '3.0.0',
            'analysis_type': 'comprehensive_integration',
            'components': {},
            'integration_points': {},
            'broken_references': [],
            'recommendations': []
        }
    
    def analyze_command_module_integration(self):
        """Analyze command-to-module delegation integrity"""
        print("=== Command-to-Module Integration Analysis ===")
        
        integration_data = {
            'total_commands': 0,
            'working_delegations': 0,
            'broken_delegations': 0,
            'delegations': {}
        }
        
        # Check core commands
        core_commands_dir = self.claude_dir / 'prompt_eng' / 'commands' / 'core'
        if core_commands_dir.exists():
            for command_file in core_commands_dir.glob('*.md'):
                integration_data['total_commands'] += 1
                command_name = command_file.stem
                
                # Read command file and extract delegation target
                try:
                    with open(command_file, 'r') as f:
                        content = f.read()
                    
                    # Find delegation target
                    delegation_match = re.search(r'<delegation target="([^"]+)">', content)
                    if delegation_match:
                        target_path = delegation_match.group(1)
                        full_target_path = self.claude_dir / target_path
                        
                        delegation_status = {
                            'target_path': target_path,
                            'target_exists': full_target_path.exists(),
                            'command_path': str(command_file.relative_to(Path.cwd()))
                        }
                        
                        if delegation_status['target_exists']:
                            integration_data['working_delegations'] += 1
                            print(f"✓ {command_name} → {target_path}")
                        else:
                            integration_data['broken_delegations'] += 1
                            print(f"✗ {command_name} → {target_path} (MISSING)")
                            self.results['broken_references'].append({
                                'type': 'command_delegation',
                                'command': command_name,
                                'missing_target': target_path
                            })
                        
                        integration_data['delegations'][command_name] = delegation_status
                    else:
                        print(f"? {command_name} → No delegation target found")
                        
                except Exception as e:
                    print(f"✗ Error reading {command_file}: {e}")
        
        # Check init commands
        init_commands_dir = self.claude_dir / 'start_here'
        if init_commands_dir.exists():
            for init_file in init_commands_dir.glob('*.md'):
                integration_data['total_commands'] += 1
                # Similar analysis for init commands
        
        self.results['components']['command_integration'] = integration_data
    
    def analyze_module_dependencies(self):
        """Analyze module dependency chains"""
        print("\\n=== Module Dependency Analysis ===")
        
        dependency_data = {
            'total_modules': 0,
            'modules_with_dependencies': 0,
            'dependency_chains': {},
            'orphaned_modules': [],
            'missing_dependencies': []
        }
        
        # Find all modules
        for module_file in self.claude_dir.rglob('*.md'):
            if 'archive' in str(module_file):
                continue
                
            dependency_data['total_modules'] += 1
            
            try:
                with open(module_file, 'r') as f:
                    content = f.read()
                
                # Look for dependency references
                depends_on_match = re.search(r'<depends_on>(.*?)</depends_on>', content, re.DOTALL)
                if depends_on_match:
                    dependencies = depends_on_match.group(1).strip()
                    dependency_data['modules_with_dependencies'] += 1
                    
                    # Extract individual dependencies
                    dep_lines = [line.strip() for line in dependencies.split('\\n') if line.strip()]
                    module_deps = []
                    
                    for dep_line in dep_lines:
                        if dep_line and not dep_line.startswith('#'):
                            # Extract module path
                            dep_match = re.search(r'([^\\s]+\\.md)', dep_line)
                            if dep_match:
                                dep_path = dep_match.group(1)
                                dep_full_path = self.claude_dir / dep_path
                                
                                dep_info = {
                                    'path': dep_path,
                                    'exists': dep_full_path.exists(),
                                    'description': dep_line
                                }
                                
                                if not dep_info['exists']:
                                    dependency_data['missing_dependencies'].append({
                                        'module': str(module_file.relative_to(self.claude_dir)),
                                        'missing_dependency': dep_path
                                    })
                                
                                module_deps.append(dep_info)
                    
                    dependency_data['dependency_chains'][str(module_file.relative_to(self.claude_dir))] = module_deps
                    
            except Exception as e:
                print(f"Error analyzing {module_file}: {e}")
        
        self.results['components']['module_dependencies'] = dependency_data
        print(f"Found {dependency_data['total_modules']} modules, {dependency_data['modules_with_dependencies']} with dependencies")
    
    def analyze_configuration_integration(self):
        """Analyze PROJECT_CONFIG integration"""
        print("\\n=== Configuration Integration Analysis ===")
        
        config_data = {
            'config_file_exists': False,
            'config_parseable': False,
            'placeholder_count': 0,
            'placeholders_by_file': {},
            'config_values': {},
            'template_resolution_exists': False
        }
        
        # Check PROJECT_CONFIG.xml
        config_file = Path('PROJECT_CONFIG.xml')
        if config_file.exists():
            config_data['config_file_exists'] = True
            
            try:
                tree = ET.parse(config_file)
                root = tree.getroot()
                config_data['config_parseable'] = True
                
                # Extract some key values
                for elem in root.iter():
                    if elem.text and elem.text.strip():
                        config_data['config_values'][elem.tag] = elem.text.strip()
                        
            except Exception as e:
                print(f"Error parsing PROJECT_CONFIG.xml: {e}")
        
        # Check for template resolution module
        template_resolution = self.claude_dir / 'system' / 'context' / 'template-resolution.md'
        config_data['template_resolution_exists'] = template_resolution.exists()
        
        # Find all PROJECT_CONFIG placeholders
        for file_path in self.claude_dir.rglob('*.md'):
            if 'archive' in str(file_path):
                continue
                
            try:
                with open(file_path, 'r') as f:
                    content = f.read()
                
                placeholders = re.findall(r'\\[PROJECT_CONFIG: ([^\\]]+)\\]', content)
                if placeholders:
                    config_data['placeholder_count'] += len(placeholders)
                    config_data['placeholders_by_file'][str(file_path.relative_to(self.claude_dir))] = placeholders
                    
            except Exception as e:
                continue
        
        self.results['components']['configuration_integration'] = config_data
        print(f"Found {config_data['placeholder_count']} PROJECT_CONFIG placeholders across {len(config_data['placeholders_by_file'])} files")
    
    def analyze_quality_gates(self):
        """Analyze quality gate integration"""
        print("\\n=== Quality Gate Integration Analysis ===")
        
        quality_data = {
            'quality_modules': [],
            'tdd_references': [],
            'quality_gate_references': [],
            'enforcement_patterns': {}
        }
        
        # Find quality modules
        quality_dir = self.claude_dir / 'system' / 'quality'
        if quality_dir.exists():
            for quality_file in quality_dir.glob('*.md'):
                quality_data['quality_modules'].append(str(quality_file.relative_to(self.claude_dir)))
        
        # Find TDD references
        for file_path in self.claude_dir.rglob('*.md'):
            if 'archive' in str(file_path):
                continue
                
            try:
                with open(file_path, 'r') as f:
                    content = f.read()
                
                # Look for TDD references
                tdd_matches = re.findall(r'quality/tdd\\.md[^\\s]*', content)
                if tdd_matches:
                    quality_data['tdd_references'].extend([{
                        'file': str(file_path.relative_to(self.claude_dir)),
                        'reference': match
                    } for match in tdd_matches])
                
                # Look for quality gate references
                if 'quality_gates' in content.lower() or 'gate.*enforcement' in content.lower():
                    quality_data['quality_gate_references'].append(str(file_path.relative_to(self.claude_dir)))
                    
            except Exception as e:
                continue
        
        self.results['components']['quality_gates'] = quality_data
        print(f"Found {len(quality_data['quality_modules'])} quality modules, {len(quality_data['tdd_references'])} TDD references")
    
    def generate_recommendations(self):
        """Generate actionable recommendations"""
        print("\\n=== Generating Recommendations ===")
        
        recommendations = []
        
        # Command delegation issues
        if self.results['broken_references']:
            recommendations.append({
                'priority': 'CRITICAL',
                'category': 'Command Integration',
                'issue': 'Broken command-to-module delegations',
                'action': 'Create missing delegation target modules',
                'details': [ref['missing_target'] for ref in self.results['broken_references'] if ref['type'] == 'command_delegation']
            })
        
        # Module dependency issues
        if 'module_dependencies' in self.results['components']:
            missing_deps = self.results['components']['module_dependencies']['missing_dependencies']
            if missing_deps:
                recommendations.append({
                    'priority': 'HIGH',
                    'category': 'Module Dependencies',
                    'issue': 'Missing module dependencies',
                    'action': 'Create or fix missing dependency modules',
                    'details': missing_deps
                })
        
        # TDD integration issues
        if 'quality_gates' in self.results['components']:
            tdd_refs = self.results['components']['quality_gates']['tdd_references']
            if tdd_refs:
                recommendations.append({
                    'priority': 'HIGH',
                    'category': 'Quality Gates',
                    'issue': 'TDD module references but module may not exist',
                    'action': 'Verify and create quality/tdd.md module',
                    'details': f"{len(tdd_refs)} references found"
                })
        
        self.results['recommendations'] = recommendations
        
        for rec in recommendations:
            print(f"{rec['priority']}: {rec['issue']}")
            print(f"  Action: {rec['action']}")
    
    def run_analysis(self):
        """Run complete integration analysis"""
        print("Claude Code Modular Prompts Framework 3.0 - Integration Analysis")
        print("=" * 70)
        
        self.analyze_command_module_integration()
        self.analyze_module_dependencies()
        self.analyze_configuration_integration()
        self.analyze_quality_gates()
        self.generate_recommendations()
        
        # Save results
        with open('integration_analysis_results.json', 'w') as f:
            json.dump(self.results, f, indent=2)
        
        print("\\n" + "=" * 70)
        print("Analysis complete. Results saved to integration_analysis_results.json")
        
        # Summary
        print("\\nSUMMARY:")
        print(f"- Total commands analyzed: {self.results['components'].get('command_integration', {}).get('total_commands', 0)}")
        print(f"- Broken delegations: {len(self.results['broken_references'])}")
        print(f"- Critical recommendations: {len([r for r in self.results['recommendations'] if r['priority'] == 'CRITICAL'])}")
        print(f"- High priority recommendations: {len([r for r in self.results['recommendations'] if r['priority'] == 'HIGH'])}")

if __name__ == "__main__":
    analyzer = FrameworkIntegrationAnalyzer()
    analyzer.run_analysis()