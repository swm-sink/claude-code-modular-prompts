#!/usr/bin/env python3
"""
Framework Integration Validation Script for Claude Framework
Validates end-to-end integration, workflows, and quality gate enforcement
"""

from pathlib import Path
from typing import Dict, List, Set, Tuple
import re
import json

class IntegrationValidator:
    def __init__(self, framework_root: str):
        self.framework_root = Path(framework_root)
        
    def test_command_module_delegation(self) -> Dict:
        """Test command-to-module delegation flows"""
        results = {
            'delegation_flows': [],
            'broken_flows': [],
            'orphaned_modules': [],
            'commands_tested': 0
        }
        
        command_files = list((self.framework_root / "commands").glob("*.md"))
        
        for cmd_file in command_files:
            try:
                content = cmd_file.read_text(encoding='utf-8')
                cmd_name = cmd_file.stem
                results['commands_tested'] += 1
                
                # Find module references in command
                module_refs = re.findall(r'modules/([^.\s]+\.md)', content)
                
                flow = {
                    'command': cmd_name,
                    'references': module_refs,
                    'valid_references': [],
                    'broken_references': []
                }
                
                for ref in module_refs:
                    module_path = self.framework_root / "modules" / ref
                    if module_path.exists():
                        flow['valid_references'].append(ref)
                    else:
                        flow['broken_references'].append(ref)
                        results['broken_flows'].append({
                            'command': cmd_name,
                            'broken_ref': ref
                        })
                
                results['delegation_flows'].append(flow)
                
            except Exception as e:
                results['broken_flows'].append({
                    'command': cmd_file.stem,
                    'error': str(e)
                })
        
        # Find orphaned modules (not referenced by any command)
        all_modules = set()
        referenced_modules = set()
        
        for module_file in (self.framework_root / "modules").rglob("*.md"):
            rel_path = module_file.relative_to(self.framework_root / "modules")
            all_modules.add(str(rel_path))
        
        for flow in results['delegation_flows']:
            referenced_modules.update(flow['valid_references'])
        
        results['orphaned_modules'] = list(all_modules - referenced_modules)
        
        return results
    
    def verify_module_interdependencies(self) -> Dict:
        """Verify module interdependencies and integration points"""
        results = {
            'dependency_map': {},
            'circular_dependencies': [],
            'missing_dependencies': [],
            'modules_analyzed': 0
        }
        
        module_files = list((self.framework_root / "modules").rglob("*.md"))
        
        for module_file in module_files:
            try:
                content = module_file.read_text(encoding='utf-8')
                rel_path = module_file.relative_to(self.framework_root / "modules")
                module_name = str(rel_path)
                results['modules_analyzed'] += 1
                
                # Find dependencies
                dependencies = []
                
                # Look for integration_points
                integration_section = re.search(r'<integration_points>(.*?)</integration_points>', content, re.DOTALL)
                if integration_section:
                    depends_on = re.findall(r'([^/\s]+\.md)', integration_section.group(1))
                    dependencies.extend(depends_on)
                
                # Also check for direct module references
                module_refs = re.findall(r'modules/([^.\s]+\.md)', content)
                dependencies.extend(module_refs)
                
                # Remove duplicates and self-references
                dependencies = list(set(dep for dep in dependencies if dep != module_name))
                
                results['dependency_map'][module_name] = dependencies
                
                # Check if dependencies exist
                for dep in dependencies:
                    dep_path = self.framework_root / "modules" / dep
                    if not dep_path.exists():
                        results['missing_dependencies'].append({
                            'module': module_name,
                            'missing_dependency': dep
                        })
                
            except Exception as e:
                results['missing_dependencies'].append({
                    'module': str(module_file.relative_to(self.framework_root)),
                    'error': str(e)
                })
        
        # Check for circular dependencies
        results['circular_dependencies'] = self._find_circular_dependencies(results['dependency_map'])
        
        return results
    
    def _find_circular_dependencies(self, dependency_map: Dict[str, List[str]]) -> List[List[str]]:
        """Find circular dependencies in module map"""
        def dfs(node, path, visited, rec_stack):
            visited.add(node)
            rec_stack.add(node)
            
            for neighbor in dependency_map.get(node, []):
                if neighbor not in visited:
                    cycle = dfs(neighbor, path + [neighbor], visited, rec_stack)
                    if cycle:
                        return cycle
                elif neighbor in rec_stack:
                    # Found cycle
                    cycle_start = path.index(neighbor)
                    return path[cycle_start:] + [neighbor]
            
            rec_stack.remove(node)
            return None
        
        visited = set()
        cycles = []
        
        for node in dependency_map:
            if node not in visited:
                cycle = dfs(node, [node], visited, set())
                if cycle and cycle not in cycles:
                    cycles.append(cycle)
        
        return cycles
    
    def check_session_creation_workflows(self) -> Dict:
        """Check session creation workflow patterns"""
        results = {
            'session_triggers': [],
            'workflow_patterns': [],
            'missing_session_integration': [],
            'files_checked': 0
        }
        
        md_files = list(self.framework_root.rglob("*.md"))
        
        for file_path in md_files:
            try:
                content = file_path.read_text(encoding='utf-8')
                results['files_checked'] += 1
                
                # Check for session integration patterns
                session_patterns = [
                    r'<session_integration>',
                    r'session.*created.*automatically',
                    r'GitHub.*session',
                    r'issue.*tracking',
                    r'mandatory.*session'
                ]
                
                has_session_integration = False
                for pattern in session_patterns:
                    if re.search(pattern, content, re.IGNORECASE):
                        has_session_integration = True
                        results['session_triggers'].append({
                            'file': str(file_path.relative_to(self.framework_root)),
                            'pattern': pattern
                        })
                        break
                
                # Check for workflow patterns
                workflow_indicators = [
                    r'<phase[^>]*order=',
                    r'<workflow>',
                    r'multi-agent',
                    r'swarm.*execution'
                ]
                
                for pattern in workflow_indicators:
                    if re.search(pattern, content, re.IGNORECASE):
                        results['workflow_patterns'].append({
                            'file': str(file_path.relative_to(self.framework_root)),
                            'pattern': pattern
                        })
                
                # Files that should have session integration but don't
                should_have_session = (
                    'swarm' in file_path.name or 
                    'multi-agent' in content.lower() or
                    'protocol' in file_path.name
                )
                
                if should_have_session and not has_session_integration:
                    results['missing_session_integration'].append(str(file_path.relative_to(self.framework_root)))
                
            except Exception as e:
                pass
        
        return results
    
    def test_multi_agent_coordination(self) -> Dict:
        """Test multi-agent coordination patterns"""
        results = {
            'multi_agent_files': [],
            'coordination_patterns': [],
            'task_patterns': 0,
            'batch_patterns': 0,
            'swarm_patterns': 0
        }
        
        md_files = list(self.framework_root.rglob("*.md"))
        
        for file_path in md_files:
            try:
                content = file_path.read_text(encoding='utf-8')
                
                # Check for multi-agent indicators
                multi_agent_indicators = [
                    r'multi.agent',
                    r'Task\(\)',
                    r'Batch\(\)',
                    r'swarm',
                    r'coordination',
                    r'parallel.*execution'
                ]
                
                has_multi_agent = False
                for pattern in multi_agent_indicators:
                    if re.search(pattern, content, re.IGNORECASE):
                        has_multi_agent = True
                        break
                
                if has_multi_agent:
                    results['multi_agent_files'].append(str(file_path.relative_to(self.framework_root)))
                    
                    # Count specific patterns
                    results['task_patterns'] += len(re.findall(r'Task\(\)', content))
                    results['batch_patterns'] += len(re.findall(r'Batch\(\)', content))
                    results['swarm_patterns'] += len(re.findall(r'swarm', content, re.IGNORECASE))
                    
                    # Look for coordination patterns
                    coordination_indicators = [
                        r'sequential.*mode',
                        r'parallel.*execution',
                        r'agent.*coordination',
                        r'task.*distribution'
                    ]
                    
                    for pattern in coordination_indicators:
                        if re.search(pattern, content, re.IGNORECASE):
                            results['coordination_patterns'].append({
                                'file': str(file_path.relative_to(self.framework_root)),
                                'pattern': pattern
                            })
                
            except Exception as e:
                pass
        
        return results
    
    def validate_quality_gate_enforcement(self) -> Dict:
        """Validate quality gate enforcement across framework"""
        results = {
            'quality_gates_found': 0,
            'enforcement_levels': {},
            'gate_types': {},
            'files_with_gates': [],
            'missing_gates': []
        }
        
        md_files = list(self.framework_root.rglob("*.md"))
        
        for file_path in md_files:
            try:
                content = file_path.read_text(encoding='utf-8')
                
                # Find quality gates
                quality_gate_patterns = [
                    r'<quality_gates[^>]*>',
                    r'<gate[^>]*>',
                    r'<mandatory_quality_gates[^>]*>'
                ]
                
                has_gates = False
                for pattern in quality_gate_patterns:
                    gates = re.findall(pattern, content)
                    if gates:
                        has_gates = True
                        results['quality_gates_found'] += len(gates)
                        
                        # Extract enforcement levels
                        for gate in gates:
                            enforcement_match = re.search(r'enforcement="([^"]*)"', gate)
                            if enforcement_match:
                                level = enforcement_match.group(1)
                                results['enforcement_levels'][level] = results['enforcement_levels'].get(level, 0) + 1
                            
                            # Extract gate types
                            name_match = re.search(r'name="([^"]*)"', gate)
                            if name_match:
                                gate_type = name_match.group(1)
                                results['gate_types'][gate_type] = results['gate_types'].get(gate_type, 0) + 1
                
                if has_gates:
                    results['files_with_gates'].append(str(file_path.relative_to(self.framework_root)))
                
                # Check if files that should have gates are missing them
                should_have_gates = (
                    'quality' in str(file_path) or
                    'production' in file_path.name or
                    'protocol' in file_path.name or
                    'security' in str(file_path)
                )
                
                if should_have_gates and not has_gates:
                    results['missing_gates'].append(str(file_path.relative_to(self.framework_root)))
                
            except Exception as e:
                pass
        
        return results
    
    def validate_all(self) -> Dict:
        """Run complete integration validation"""
        results = {
            'command_module_delegation': self.test_command_module_delegation(),
            'module_interdependencies': self.verify_module_interdependencies(),
            'session_workflows': self.check_session_creation_workflows(),
            'multi_agent_coordination': self.test_multi_agent_coordination(),
            'quality_gate_enforcement': self.validate_quality_gate_enforcement()
        }
        
        return results
    
    def generate_report(self, results: Dict) -> str:
        """Generate comprehensive integration validation report"""
        report = []
        report.append("=" * 80)
        report.append("FRAMEWORK INTEGRATION VALIDATION REPORT")
        report.append("=" * 80)
        report.append("")
        
        # Command-Module Delegation
        cmd_results = results['command_module_delegation']
        report.append("COMMAND-TO-MODULE DELEGATION:")
        report.append("-" * 40)
        report.append(f"✅ Commands tested: {cmd_results['commands_tested']}")
        report.append(f"✅ Delegation flows: {len(cmd_results['delegation_flows'])}")
        
        if cmd_results['broken_flows']:
            report.append(f"❌ Broken flows: {len(cmd_results['broken_flows'])}")
            for broken in cmd_results['broken_flows']:
                if 'broken_ref' in broken:
                    report.append(f"  ❌ {broken['command']} → {broken['broken_ref']}")
                else:
                    report.append(f"  ❌ {broken['command']}: {broken.get('error', 'Unknown error')}")
        else:
            report.append("✅ No broken delegation flows")
        
        if cmd_results['orphaned_modules']:
            report.append(f"⚠️  Orphaned modules: {len(cmd_results['orphaned_modules'])}")
            for orphan in cmd_results['orphaned_modules'][:3]:  # Show first 3
                report.append(f"  ⚠️  {orphan}")
        else:
            report.append("✅ No orphaned modules")
        
        report.append("")
        
        # Module Interdependencies
        dep_results = results['module_interdependencies']
        report.append("MODULE INTERDEPENDENCIES:")
        report.append("-" * 40)
        report.append(f"✅ Modules analyzed: {dep_results['modules_analyzed']}")
        report.append(f"✅ Dependency relationships: {len(dep_results['dependency_map'])}")
        
        if dep_results['circular_dependencies']:
            report.append(f"❌ Circular dependencies: {len(dep_results['circular_dependencies'])}")
            for cycle in dep_results['circular_dependencies']:
                report.append(f"  ❌ {' → '.join(cycle)}")
        else:
            report.append("✅ No circular dependencies")
        
        if dep_results['missing_dependencies']:
            report.append(f"❌ Missing dependencies: {len(dep_results['missing_dependencies'])}")
        else:
            report.append("✅ All dependencies valid")
        
        report.append("")
        
        # Session Workflows
        session_results = results['session_workflows']
        report.append("SESSION CREATION WORKFLOWS:")
        report.append("-" * 40)
        report.append(f"✅ Files checked: {session_results['files_checked']}")
        report.append(f"✅ Session triggers: {len(session_results['session_triggers'])}")
        report.append(f"✅ Workflow patterns: {len(session_results['workflow_patterns'])}")
        
        if session_results['missing_session_integration']:
            report.append(f"⚠️  Missing session integration: {len(session_results['missing_session_integration'])}")
        else:
            report.append("✅ Session integration complete")
        
        report.append("")
        
        # Multi-Agent Coordination
        agent_results = results['multi_agent_coordination']
        report.append("MULTI-AGENT COORDINATION:")
        report.append("-" * 40)
        report.append(f"✅ Multi-agent files: {len(agent_results['multi_agent_files'])}")
        report.append(f"✅ Task() patterns: {agent_results['task_patterns']}")
        report.append(f"✅ Batch() patterns: {agent_results['batch_patterns']}")
        report.append(f"✅ Swarm patterns: {agent_results['swarm_patterns']}")
        report.append(f"✅ Coordination patterns: {len(agent_results['coordination_patterns'])}")
        report.append("")
        
        # Quality Gate Enforcement
        gate_results = results['quality_gate_enforcement']
        report.append("QUALITY GATE ENFORCEMENT:")
        report.append("-" * 40)
        report.append(f"✅ Quality gates found: {gate_results['quality_gates_found']}")
        report.append(f"✅ Files with gates: {len(gate_results['files_with_gates'])}")
        
        if gate_results['enforcement_levels']:
            report.append("Enforcement levels:")
            for level, count in gate_results['enforcement_levels'].items():
                report.append(f"  • {level}: {count}")
        
        if gate_results['missing_gates']:
            report.append(f"⚠️  Missing gates: {len(gate_results['missing_gates'])}")
        else:
            report.append("✅ Quality gate coverage complete")
        
        report.append("")
        
        # Overall Assessment
        report.append("INTEGRATION HEALTH SCORE:")
        report.append("-" * 40)
        
        score = 0
        total_checks = 5
        
        if not cmd_results['broken_flows']:
            score += 1
            report.append("✅ Command delegation: HEALTHY")
        else:
            report.append("❌ Command delegation: ISSUES FOUND")
        
        if not dep_results['circular_dependencies'] and not dep_results['missing_dependencies']:
            score += 1
            report.append("✅ Module dependencies: HEALTHY")
        else:
            report.append("❌ Module dependencies: ISSUES FOUND")
        
        if len(session_results['session_triggers']) > 0:
            score += 1
            report.append("✅ Session workflows: HEALTHY")
        else:
            report.append("❌ Session workflows: NEEDS IMPROVEMENT")
        
        if len(agent_results['multi_agent_files']) > 0:
            score += 1
            report.append("✅ Multi-agent coordination: HEALTHY")
        else:
            report.append("❌ Multi-agent coordination: NEEDS IMPROVEMENT")
        
        if gate_results['quality_gates_found'] > 0:
            score += 1
            report.append("✅ Quality gate enforcement: HEALTHY")
        else:
            report.append("❌ Quality gate enforcement: NEEDS IMPROVEMENT")
        
        report.append("")
        report.append(f"INTEGRATION SCORE: {score}/{total_checks} ({(score/total_checks)*100:.0f}%)")
        
        if score == total_checks:
            report.append("🎉 EXCELLENT FRAMEWORK INTEGRATION!")
        elif score >= total_checks * 0.8:
            report.append("👍 STRONG FRAMEWORK INTEGRATION")
        else:
            report.append("⚠️  FRAMEWORK INTEGRATION NEEDS ATTENTION")
        
        report.append("")
        report.append("=" * 80)
        
        return "\n".join(report)

def main():
    framework_root = "/Users/smenssink/Documents/Github personal projects/claude-code-modular-agents/.claude"
    
    validator = IntegrationValidator(framework_root)
    results = validator.validate_all()
    report = validator.generate_report(results)
    
    print(report)
    
    # Save detailed results
    results_file = Path(framework_root) / "integration_validation.json"
    with open(results_file, 'w') as f:
        json.dump(results, f, indent=2, default=str)
    
    # Save report
    report_file = Path(framework_root) / "integration_report.txt"
    report_file.write_text(report)
    
    print(f"\nDetailed results saved to: {results_file}")
    print(f"Report saved to: {report_file}")
    
    return 0

if __name__ == "__main__":
    import sys
    sys.exit(main())