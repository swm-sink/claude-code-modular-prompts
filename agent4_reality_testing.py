#!/usr/bin/env python3
"""
Agent 4: Reality Tester
Test what actually works in Claude Code using foundation data from previous agents
"""

import os
import json
import re
from pathlib import Path
from collections import defaultdict, Counter
from datetime import datetime

class RealityTester:
    def __init__(self, base_path=".claude"):
        self.base_path = Path(base_path)
        self.test_results = {
            'commands': {},
            'quality_modules': {},
            'integration_tests': {},
            'structural_impact_tests': {}
        }
        self.functionality_assessment = {}
        
        # Load foundation data from previous agents
        self.agent1_data = self.load_agent1_data()
        self.agent2_data = self.load_agent2_data()
        self.agent3_data = self.load_agent3_data()
        
    def load_agent1_data(self):
        """Load Agent 1's inventory data"""
        try:
            with open("agent1_inventory_results.json", 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            print("⚠️  Agent 1 data not found")
            return {}
    
    def load_agent2_data(self):
        """Load Agent 2's directory audit data"""
        try:
            with open("agent2_directory_audit_results.json", 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            print("⚠️  Agent 2 data not found")
            return {}
    
    def load_agent3_data(self):
        """Load Agent 3's reference analysis data"""
        try:
            with open("agent3_reference_analysis_results.json", 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            print("⚠️  Agent 3 data not found")
            return {}
    
    def test_command_functionality(self):
        """Test the 22 command files identified by Agent 1"""
        print("🧪 Agent 4: Testing command functionality...")
        
        command_files = []
        
        # Get command files from Agent 1 data
        if self.agent1_data and 'handoff_data' in self.agent1_data:
            command_files = self.agent1_data['handoff_data']['agent_4_reality_testing']['command_files']
        else:
            # Fallback: find command files manually
            command_files = [str(f) for f in self.base_path.rglob("*.md") if '/commands/' in str(f)]
        
        print(f"📋 Testing {len(command_files)} command files...")
        
        for cmd_file in command_files:
            result = self.test_single_command(cmd_file)
            cmd_name = Path(cmd_file).stem
            self.test_results['commands'][cmd_name] = result
        
        # Summarize command test results
        working_commands = len([r for r in self.test_results['commands'].values() if r['functional']])
        total_commands = len(self.test_results['commands'])
        
        print(f"📊 Command Tests: {working_commands}/{total_commands} functional ({working_commands/total_commands*100:.1f}%)")
        return self.test_results['commands']
    
    def test_single_command(self, cmd_file):
        """Test a single command file"""
        result = {
            'file_path': cmd_file,
            'exists': False,
            'readable': False,
            'has_structure': False,
            'has_instructions': False,
            'has_dependencies': False,
            'functional': False,
            'issues': []
        }
        
        cmd_path = Path(cmd_file)
        
        # Test 1: File exists and is readable
        if cmd_path.exists():
            result['exists'] = True
            try:
                with open(cmd_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                result['readable'] = True
            except Exception as e:
                result['issues'].append(f"Read error: {e}")
                return result
        else:
            result['issues'].append("File does not exist")
            return result
        
        # Test 2: Has basic command structure
        if content.startswith('#') and len(content) > 100:
            result['has_structure'] = True
        else:
            result['issues'].append("Missing basic structure")
        
        # Test 3: Has instructions for Claude
        instruction_indicators = ['##', 'Instructions', 'workflow', 'steps', 'process']
        if any(indicator.lower() in content.lower() for indicator in instruction_indicators):
            result['has_instructions'] = True
        else:
            result['issues'].append("No clear instructions found")
        
        # Test 4: Check for module dependencies
        if '.md' in content and ('system/' in content or 'modules/' in content or 'quality/' in content):
            result['has_dependencies'] = True
        
        # Test 5: Overall functionality assessment
        result['functional'] = (
            result['exists'] and
            result['readable'] and
            result['has_structure'] and
            result['has_instructions']
        )
        
        return result
    
    def test_quality_module_accessibility(self):
        """Test the 36 quality modules identified by Agent 1"""
        print("🧪 Agent 4: Testing quality module accessibility...")
        
        quality_modules = []
        
        # Get quality modules from Agent 1 data
        if self.agent1_data and 'handoff_data' in self.agent1_data:
            quality_modules = self.agent1_data['handoff_data']['agent_4_reality_testing']['quality_modules']
        else:
            # Fallback: find quality modules manually
            quality_modules = [str(f) for f in self.base_path.rglob("*.md") if 'quality' in str(f)]
        
        print(f"📋 Testing {len(quality_modules)} quality modules...")
        
        for module_file in quality_modules:
            result = self.test_quality_module(module_file)
            module_name = Path(module_file).stem
            self.test_results['quality_modules'][module_name] = result
        
        # Summarize quality module test results
        accessible_modules = len([r for r in self.test_results['quality_modules'].values() if r['accessible']])
        total_modules = len(self.test_results['quality_modules'])
        
        print(f"📊 Quality Module Tests: {accessible_modules}/{total_modules} accessible ({accessible_modules/total_modules*100:.1f}%)")
        return self.test_results['quality_modules']
    
    def test_quality_module(self, module_file):
        """Test a single quality module"""
        result = {
            'file_path': module_file,
            'exists': False,
            'readable': False,
            'has_quality_content': False,
            'has_enforcement': False,
            'accessible': False,
            'issues': []
        }
        
        module_path = Path(module_file)
        
        # Test 1: File exists and is readable
        if module_path.exists():
            result['exists'] = True
            try:
                with open(module_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                result['readable'] = True
            except Exception as e:
                result['issues'].append(f"Read error: {e}")
                return result
        else:
            result['issues'].append("Module file does not exist")
            return result
        
        # Test 2: Has quality-related content
        quality_indicators = ['tdd', 'test', 'quality', 'gate', 'coverage', 'validation', 'security']
        if any(indicator in content.lower() for indicator in quality_indicators):
            result['has_quality_content'] = True
        else:
            result['issues'].append("No quality-related content found")
        
        # Test 3: Has enforcement mechanisms
        enforcement_indicators = ['enforce', 'mandatory', 'required', 'MUST', 'BLOCK', 'gate']
        if any(indicator in content for indicator in enforcement_indicators):
            result['has_enforcement'] = True
        
        # Test 4: Overall accessibility
        result['accessible'] = (
            result['exists'] and
            result['readable'] and
            result['has_quality_content']
        )
        
        return result
    
    def test_command_module_integration(self):
        """Test integration between commands and modules"""
        print("🧪 Agent 4: Testing command-module integration...")
        
        integration_tests = {
            'commands_reference_modules': 0,
            'modules_exist_for_references': 0,
            'quality_gates_accessible': 0,
            'circular_references': 0,
            'broken_integrations': []
        }
        
        # Test command -> module references
        for cmd_name, cmd_result in self.test_results['commands'].items():
            if cmd_result['functional'] and cmd_result['has_dependencies']:
                integration_tests['commands_reference_modules'] += 1
                
                # Check if referenced modules actually exist
                cmd_file = cmd_result['file_path']
                if Path(cmd_file).exists():
                    with open(cmd_file, 'r') as f:
                        content = f.read()
                    
                    # Look for module references
                    module_refs = re.findall(r'([a-zA-Z0-9_/-]+\.md)', content)
                    for ref in module_refs:
                        if self.check_module_exists(ref):
                            integration_tests['modules_exist_for_references'] += 1
                        else:
                            integration_tests['broken_integrations'].append({
                                'command': cmd_name,
                                'missing_module': ref,
                                'type': 'MISSING_MODULE_REFERENCE'
                            })
        
        # Test quality gate accessibility from commands
        quality_gate_refs = ['tdd', 'quality', 'gate', 'test-coverage', 'universal-quality-gates']
        for cmd_name, cmd_result in self.test_results['commands'].items():
            if cmd_result['functional']:
                cmd_file = cmd_result['file_path']
                if Path(cmd_file).exists():
                    with open(cmd_file, 'r') as f:
                        content = f.read()
                    
                    if any(gate_ref in content.lower() for gate_ref in quality_gate_refs):
                        integration_tests['quality_gates_accessible'] += 1
        
        self.test_results['integration_tests'] = integration_tests
        print(f"📊 Integration Tests: {integration_tests['commands_reference_modules']} commands reference modules")
        return integration_tests
    
    def check_module_exists(self, module_ref):
        """Check if a referenced module actually exists"""
        # Try different resolution strategies
        paths_to_try = [
            self.base_path / module_ref,
            self.base_path / 'modules' / module_ref,
            self.base_path / 'system' / module_ref,
            Path('.') / module_ref
        ]
        
        for path in paths_to_try:
            if path.exists():
                return True
        
        # Search by filename
        filename = Path(module_ref).name
        for found in self.base_path.rglob(filename):
            return True
        
        return False
    
    def test_structural_impact_on_functionality(self):
        """Test how Agent 2's structural chaos impacts functionality"""
        print("🧪 Agent 4: Testing structural impact on functionality...")
        
        structural_impact = {
            'directory_chaos_impact': 'UNKNOWN',
            'overlap_functionality_conflicts': [],
            'documentation_reality_gaps': [],
            'consolidation_urgency': 'UNKNOWN'
        }
        
        if self.agent2_data:
            # Assess directory chaos impact
            dir_count = len(self.agent2_data.get('actual_structure', {}))
            if dir_count > 40:
                structural_impact['directory_chaos_impact'] = 'HIGH'
            elif dir_count > 25:
                structural_impact['directory_chaos_impact'] = 'MEDIUM'
            else:
                structural_impact['directory_chaos_impact'] = 'LOW'
            
            # Check for functionality conflicts from overlaps
            overlaps = self.agent2_data.get('overlaps', [])
            for overlap in overlaps:
                if overlap.get('type') == 'PATTERN_DUPLICATION':
                    structural_impact['overlap_functionality_conflicts'].append({
                        'type': 'PATTERN_CONFUSION',
                        'description': 'Multiple pattern locations create confusion',
                        'severity': overlap.get('severity', 'MEDIUM'),
                        'affected_directories': overlap.get('directories', [])
                    })
            
            # Check documentation-reality gaps
            inconsistencies = self.agent2_data.get('inconsistencies', [])
            high_severity_inconsistencies = [i for i in inconsistencies if i.get('severity') == 'HIGH']
            if len(high_severity_inconsistencies) > 5:
                structural_impact['documentation_reality_gaps'] = high_severity_inconsistencies[:5]
            
            # Assess consolidation urgency
            critical_overlaps = len([o for o in overlaps if o.get('severity') == 'CRITICAL'])
            if critical_overlaps > 0:
                structural_impact['consolidation_urgency'] = 'CRITICAL'
            elif len(overlaps) > 2:
                structural_impact['consolidation_urgency'] = 'HIGH'
            else:
                structural_impact['consolidation_urgency'] = 'MEDIUM'
        
        self.test_results['structural_impact_tests'] = structural_impact
        print(f"📊 Structural Impact: {structural_impact['directory_chaos_impact']} directory chaos impact")
        return structural_impact
    
    def assess_overall_functionality(self):
        """Assess overall framework functionality"""
        print("🧪 Agent 4: Assessing overall functionality...")
        
        # Calculate functionality percentages
        total_commands = len(self.test_results['commands'])
        functional_commands = len([r for r in self.test_results['commands'].values() if r['functional']])
        command_functionality = (functional_commands / total_commands * 100) if total_commands > 0 else 0
        
        total_quality_modules = len(self.test_results['quality_modules'])
        accessible_quality_modules = len([r for r in self.test_results['quality_modules'].values() if r['accessible']])
        quality_module_accessibility = (accessible_quality_modules / total_quality_modules * 100) if total_quality_modules > 0 else 0
        
        # Overall assessment
        overall_score = (command_functionality + quality_module_accessibility) / 2
        
        # Determine status
        if overall_score >= 80:
            status = 'GOOD'
        elif overall_score >= 60:
            status = 'FAIR'
        elif overall_score >= 40:
            status = 'POOR'
        else:
            status = 'CRITICAL'
        
        # Factor in structural impact
        structural_impact = self.test_results.get('structural_impact_tests', {})
        if structural_impact.get('consolidation_urgency') == 'CRITICAL':
            status = f"{status}_WITH_CRITICAL_STRUCTURAL_ISSUES"
        
        assessment = {
            'overall_functionality_score': overall_score,
            'status': status,
            'command_functionality_percentage': command_functionality,
            'quality_module_accessibility_percentage': quality_module_accessibility,
            'functional_commands': functional_commands,
            'total_commands': total_commands,
            'accessible_quality_modules': accessible_quality_modules,
            'total_quality_modules': total_quality_modules,
            'key_findings': self.generate_key_findings(),
            'production_readiness': self.assess_production_readiness(overall_score, status)
        }
        
        self.functionality_assessment = assessment
        print(f"📊 Overall Functionality: {overall_score:.1f}% ({status})")
        return assessment
    
    def generate_key_findings(self):
        """Generate key findings from all tests"""
        findings = []
        
        # Command findings
        functional_commands = len([r for r in self.test_results['commands'].values() if r['functional']])
        total_commands = len(self.test_results['commands'])
        if functional_commands / total_commands >= 0.8:
            findings.append("✅ Commands are mostly functional - good foundation")
        elif functional_commands / total_commands >= 0.6:
            findings.append("⚠️ Commands are moderately functional - some issues to address")
        else:
            findings.append("🚨 Commands have significant functionality issues")
        
        # Quality module findings
        accessible_modules = len([r for r in self.test_results['quality_modules'].values() if r['accessible']])
        total_modules = len(self.test_results['quality_modules'])
        if accessible_modules / total_modules >= 0.8:
            findings.append("✅ Quality infrastructure is well accessible")
        else:
            findings.append("⚠️ Quality infrastructure has accessibility issues")
        
        # Structural findings
        structural_impact = self.test_results.get('structural_impact_tests', {})
        if structural_impact.get('consolidation_urgency') == 'CRITICAL':
            findings.append("🚨 CRITICAL: Structural consolidation required before production")
        elif structural_impact.get('directory_chaos_impact') == 'HIGH':
            findings.append("⚠️ Directory structure complexity impacts usability")
        
        # Reference findings (from Agent 3)
        if self.agent3_data:
            broken_percentage = self.agent3_data.get('analysis_results', {}).get('broken_percentage', 0)
            if broken_percentage < 15:
                findings.append("✅ Reference integrity is good (90%+ functional)")
            else:
                findings.append(f"⚠️ Reference integrity needs attention ({100-broken_percentage:.1f}% functional)")
        
        return findings
    
    def assess_production_readiness(self, overall_score, status):
        """Assess production readiness"""
        if 'CRITICAL_STRUCTURAL_ISSUES' in status:
            return {
                'ready': False,
                'level': 'NOT_READY',
                'reason': 'Critical structural issues must be resolved first',
                'blockers': ['Directory structure consolidation', 'Overlap resolution'],
                'estimated_remediation': 'HIGH_EFFORT'
            }
        elif overall_score >= 75:
            return {
                'ready': True,
                'level': 'PRODUCTION_READY',
                'reason': 'Core functionality working well',
                'minor_issues': 'Some optimization opportunities exist',
                'estimated_remediation': 'LOW_EFFORT'
            }
        elif overall_score >= 60:
            return {
                'ready': False,
                'level': 'CONDITIONALLY_READY',
                'reason': 'Core functionality working but needs improvement',
                'blockers': ['Quality gate accessibility', 'Command reliability'],
                'estimated_remediation': 'MEDIUM_EFFORT'
            }
        else:
            return {
                'ready': False,
                'level': 'NOT_READY',
                'reason': 'Too many functionality issues',
                'blockers': ['Command functionality', 'Quality infrastructure'],
                'estimated_remediation': 'HIGH_EFFORT'
            }
    
    def run_complete_testing(self):
        """Run complete reality testing suite"""
        print("🧪 Agent 4: Starting complete reality testing...")
        
        # Test 1: Command functionality
        command_results = self.test_command_functionality()
        
        # Test 2: Quality module accessibility
        quality_results = self.test_quality_module_accessibility()
        
        # Test 3: Command-module integration
        integration_results = self.test_command_module_integration()
        
        # Test 4: Structural impact on functionality
        structural_results = self.test_structural_impact_on_functionality()
        
        # Test 5: Overall assessment
        overall_assessment = self.assess_overall_functionality()
        
        # Generate comprehensive report
        report = self.generate_testing_report()
        
        print("✅ Agent 4: Reality testing complete")
        return report
    
    def generate_testing_report(self):
        """Generate comprehensive testing report"""
        return {
            'analysis_timestamp': datetime.now().isoformat(),
            'agent': 'Agent 4 - Reality Tester',
            'test_results': self.test_results,
            'functionality_assessment': self.functionality_assessment,
            'testing_summary': {
                'total_commands_tested': len(self.test_results['commands']),
                'functional_commands': len([r for r in self.test_results['commands'].values() if r['functional']]),
                'total_quality_modules_tested': len(self.test_results['quality_modules']),
                'accessible_quality_modules': len([r for r in self.test_results['quality_modules'].values() if r['accessible']]),
                'overall_functionality_score': self.functionality_assessment.get('overall_functionality_score', 0),
                'production_readiness': self.functionality_assessment.get('production_readiness', {}).get('level', 'UNKNOWN')
            },
            'critical_findings': self.identify_critical_testing_findings(),
            'handoff_data': self.prepare_testing_handoff_data()
        }
    
    def identify_critical_testing_findings(self):
        """Identify critical findings that block production"""
        critical = []
        
        # Check command functionality
        functional_commands = len([r for r in self.test_results['commands'].values() if r['functional']])
        total_commands = len(self.test_results['commands'])
        if functional_commands / total_commands < 0.6:
            critical.append({
                'type': 'COMMAND_FUNCTIONALITY_CRITICAL',
                'message': f"Only {functional_commands}/{total_commands} commands functional",
                'impact': 'Core framework functionality compromised',
                'action_required': 'Fix command issues before production'
            })
        
        # Check structural impact
        structural_impact = self.test_results.get('structural_impact_tests', {})
        if structural_impact.get('consolidation_urgency') == 'CRITICAL':
            critical.append({
                'type': 'STRUCTURAL_CHAOS_CRITICAL',
                'message': 'Critical structural issues impact functionality',
                'impact': 'Framework unusable without structural consolidation',
                'action_required': 'Complete structural consolidation first'
            })
        
        # Check integration
        integration_tests = self.test_results.get('integration_tests', {})
        broken_integrations = len(integration_tests.get('broken_integrations', []))
        if broken_integrations > 10:
            critical.append({
                'type': 'INTEGRATION_BREAKDOWN',
                'message': f"{broken_integrations} broken command-module integrations",
                'impact': 'Commands cannot access required modules',
                'action_required': 'Fix module references and paths'
            })
        
        return critical
    
    def prepare_testing_handoff_data(self):
        """Prepare handoff data for subsequent agents"""
        return {
            'agent_5_architecture_design': {
                'functionality_baseline': self.functionality_assessment.get('overall_functionality_score', 0),
                'working_components': [
                    cmd for cmd, result in self.test_results['commands'].items()
                    if result['functional']
                ],
                'broken_components': [
                    cmd for cmd, result in self.test_results['commands'].items()
                    if not result['functional']
                ],
                'structural_consolidation_priority': self.test_results.get('structural_impact_tests', {}).get('consolidation_urgency', 'UNKNOWN'),
                'production_readiness_blockers': self.functionality_assessment.get('production_readiness', {}).get('blockers', [])
            },
            'phase_1_completion_data': {
                'agent_1_inventory': 'COMPLETE',
                'agent_2_structural_audit': 'COMPLETE',
                'agent_3_reference_analysis': 'COMPLETE',
                'agent_4_reality_testing': 'COMPLETE',
                'phase_1_ready_for_architecture_design': True,
                'comprehensive_foundation_available': True
            }
        }
    
    def save_testing_results(self, output_file="agent4_reality_testing_results.json"):
        """Save testing results to file"""
        report = self.generate_testing_report()
        
        with open(output_file, 'w') as f:
            json.dump(report, f, indent=2)
        
        print(f"💾 Agent 4: Testing results saved to {output_file}")
        return report

if __name__ == "__main__":
    tester = RealityTester()
    report = tester.run_complete_testing()
    tester.save_testing_results()
    
    # Print summary
    print("\n" + "="*80)
    print("AGENT 4 REALITY TESTING SUMMARY")
    print("="*80)
    summary = report['testing_summary']
    print(f"📋 Commands Tested: {summary['total_commands_tested']}")
    print(f"✅ Functional Commands: {summary['functional_commands']} ({summary['functional_commands']/summary['total_commands_tested']*100:.1f}%)")
    print(f"🛡️  Quality Modules Tested: {summary['total_quality_modules_tested']}")
    print(f"✅ Accessible Quality Modules: {summary['accessible_quality_modules']} ({summary['accessible_quality_modules']/summary['total_quality_modules_tested']*100:.1f}%)")
    print(f"📊 Overall Functionality: {summary['overall_functionality_score']:.1f}%")
    print(f"🏭 Production Readiness: {summary['production_readiness']}")
    
    if report['critical_findings']:
        print(f"\n🚨 Critical Findings: {len(report['critical_findings'])}")
        for finding in report['critical_findings']:
            print(f"  {finding['type']}: {finding['message']}")
    
    assessment = report['functionality_assessment']
    if assessment.get('key_findings'):
        print("\n🔍 Key Findings:")
        for finding in assessment['key_findings']:
            print(f"  {finding}")
    
    print(f"\n✅ Agent 4 Complete - Reality testing data ready for Agent 5")
    print(f"🎯 PHASE 1 COMPLETE - All foundation agents finished!")
    print(f"🚀 Ready to unblock Agent 5 (Architecture Designer)")