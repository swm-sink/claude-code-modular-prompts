#!/usr/bin/env python3
"""
Integration Security Validation Framework
Security Integration Agent - Comprehensive OWASP LLM Security Validation

This module provides comprehensive security validation for all integration patterns
to ensure OWASP compliance and secure component interactions.
"""

import json
import re
import hashlib
import secrets
import time
from dataclasses import dataclass, field
from typing import Dict, List, Any, Optional, Tuple, Set, Union
from enum import Enum
import urllib.parse
from pathlib import Path


class SecurityRisk(Enum):
    """Security risk levels aligned with OWASP LLM Top 10 2025"""
    INFORMATIONAL = "informational"
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


class OWASPLLMCategory(Enum):
    """OWASP LLM Top 10 2025 Security Categories"""
    LLM01_PROMPT_INJECTION = "LLM01_Prompt_Injection"
    LLM02_INSECURE_OUTPUT = "LLM02_Insecure_Output_Handling"
    LLM03_TRAINING_DATA_POISONING = "LLM03_Training_Data_Poisoning"
    LLM04_MODEL_DOS = "LLM04_Model_Denial_of_Service"
    LLM05_SUPPLY_CHAIN = "LLM05_Supply_Chain_Vulnerabilities"
    LLM06_SENSITIVE_INFO_DISCLOSURE = "LLM06_Sensitive_Information_Disclosure"
    LLM07_INSECURE_PLUGIN_DESIGN = "LLM07_Insecure_Plugin_Design"
    LLM08_EXCESSIVE_AGENCY = "LLM08_Excessive_Agency"
    LLM09_OVERRELIANCE = "LLM09_Overreliance"
    LLM10_MODEL_THEFT = "LLM10_Model_Theft"


@dataclass
class SecurityIntegrationResult:
    """Result of integration security validation"""
    test_name: str
    integration_pattern: str
    risk_level: SecurityRisk
    owasp_category: OWASPLLMCategory
    description: str
    evidence: Dict[str, Any] = field(default_factory=dict)
    mitigation: List[str] = field(default_factory=list)
    compliance_score: float = 0.0
    passed: bool = False


@dataclass
class ComponentSecurityBoundary:
    """Security boundary analysis between components"""
    component_a: str
    component_b: str
    interaction_type: str
    security_controls: List[str]
    vulnerabilities: List[str]
    risk_assessment: SecurityRisk


class CrossCommandSecurityValidator:
    """Validates security across command chains and tool permission inheritance"""
    
    def __init__(self):
        self.command_permissions = {}
        self.tool_risk_matrix = {
            "Bash": SecurityRisk.CRITICAL,
            "WebFetch": SecurityRisk.HIGH,
            "WebSearch": SecurityRisk.HIGH,
            "Write": SecurityRisk.MEDIUM,
            "Edit": SecurityRisk.MEDIUM,
            "Read": SecurityRisk.LOW,
            "Grep": SecurityRisk.LOW,
            "Glob": SecurityRisk.LOW,
            "LS": SecurityRisk.LOW
        }
        
    def validate_permission_inheritance(self, command_chain: List[Dict[str, Any]]) -> List[SecurityIntegrationResult]:
        """Validate that permission inheritance doesn't lead to privilege escalation"""
        results = []
        
        for i, command in enumerate(command_chain):
            command_name = command.get('name', f'command_{i}')
            allowed_tools = command.get('allowed-tools', [])
            
            # Check for privilege escalation through tool chaining
            escalation_risk = self._assess_privilege_escalation(allowed_tools, command_chain[:i])
            
            if escalation_risk.risk_level in [SecurityRisk.HIGH, SecurityRisk.CRITICAL]:
                results.append(SecurityIntegrationResult(
                    test_name="privilege_escalation_detection",
                    integration_pattern="command_chaining",
                    risk_level=escalation_risk.risk_level,
                    owasp_category=OWASPLLMCategory.LLM08_EXCESSIVE_AGENCY,
                    description=f"Potential privilege escalation in command chain at {command_name}",
                    evidence={
                        "command": command_name,
                        "tools": allowed_tools,
                        "escalation_path": escalation_risk.evidence
                    },
                    mitigation=[
                        "Implement least privilege principle",
                        "Add explicit permission validation",
                        "Review tool combination risks",
                        "Implement tool usage monitoring"
                    ],
                    compliance_score=25.0,
                    passed=False
                ))
            
            # Validate tool permission boundaries
            tool_validation = self._validate_tool_boundaries(allowed_tools)
            results.extend(tool_validation)
            
        return results
    
    def _assess_privilege_escalation(self, tools: List[str], previous_commands: List[Dict]) -> SecurityIntegrationResult:
        """Assess if tool combination creates privilege escalation risk"""
        risk_score = 0
        evidence = {}
        
        # Calculate cumulative risk
        for tool in tools:
            tool_risk = self.tool_risk_matrix.get(tool, SecurityRisk.LOW)
            risk_score += self._risk_to_score(tool_risk)
        
        # Check for dangerous tool combinations
        dangerous_combinations = [
            ("Bash", "WebFetch"),  # Command injection + network access
            ("Bash", "Write"),     # Command injection + file system
            ("WebFetch", "Write")  # Network access + file system
        ]
        
        for combo in dangerous_combinations:
            if all(tool in tools for tool in combo):
                risk_score += 50
                evidence[f"dangerous_combo_{combo[0]}_{combo[1]}"] = True
        
        # Determine risk level
        if risk_score >= 100:
            risk_level = SecurityRisk.CRITICAL
        elif risk_score >= 75:
            risk_level = SecurityRisk.HIGH
        elif risk_score >= 50:
            risk_level = SecurityRisk.MEDIUM
        else:
            risk_level = SecurityRisk.LOW
            
        return SecurityIntegrationResult(
            test_name="privilege_escalation_assessment",
            integration_pattern="tool_combination",
            risk_level=risk_level,
            owasp_category=OWASPLLMCategory.LLM08_EXCESSIVE_AGENCY,
            description="Tool combination privilege escalation assessment",
            evidence=evidence,
            passed=risk_level not in [SecurityRisk.HIGH, SecurityRisk.CRITICAL]
        )
    
    def _risk_to_score(self, risk: SecurityRisk) -> int:
        """Convert risk level to numeric score"""
        risk_scores = {
            SecurityRisk.INFORMATIONAL: 5,
            SecurityRisk.LOW: 10,
            SecurityRisk.MEDIUM: 25,
            SecurityRisk.HIGH: 50,
            SecurityRisk.CRITICAL: 100
        }
        return risk_scores.get(risk, 10)
    
    def _validate_tool_boundaries(self, tools: List[str]) -> List[SecurityIntegrationResult]:
        """Validate individual tool security boundaries"""
        results = []
        
        for tool in tools:
            if tool == "Bash":
                results.append(self._validate_bash_security())
            elif tool in ["WebFetch", "WebSearch"]:
                results.append(self._validate_web_tool_security(tool))
            elif tool in ["Write", "Edit"]:
                results.append(self._validate_file_tool_security(tool))
                
        return results
    
    def _validate_bash_security(self) -> SecurityIntegrationResult:
        """Validate Bash tool security implementation"""
        return SecurityIntegrationResult(
            test_name="bash_security_validation",
            integration_pattern="system_command_execution",
            risk_level=SecurityRisk.CRITICAL,
            owasp_category=OWASPLLMCategory.LLM08_EXCESSIVE_AGENCY,
            description="Bash tool enables system command execution",
            evidence={"tool": "Bash", "capabilities": "full_system_access"},
            mitigation=[
                "Implement command allowlist",
                "Add input sanitization",
                "Enable command logging",
                "Restrict execution context",
                "Add approval workflow for dangerous commands"
            ],
            compliance_score=20.0,
            passed=False
        )
    
    def _validate_web_tool_security(self, tool: str) -> SecurityIntegrationResult:
        """Validate web access tool security"""
        return SecurityIntegrationResult(
            test_name=f"{tool.lower()}_security_validation",
            integration_pattern="external_network_access",
            risk_level=SecurityRisk.HIGH,
            owasp_category=OWASPLLMCategory.LLM05_SUPPLY_CHAIN,
            description=f"{tool} enables external network access",
            evidence={"tool": tool, "risk": "external_data_access"},
            mitigation=[
                "Implement URL allowlist",
                "Add request validation",
                "Enable network monitoring",
                "Validate response content",
                "Implement rate limiting"
            ],
            compliance_score=40.0,
            passed=False
        )
    
    def _validate_file_tool_security(self, tool: str) -> SecurityIntegrationResult:
        """Validate file system tool security"""
        return SecurityIntegrationResult(
            test_name=f"{tool.lower()}_security_validation",
            integration_pattern="file_system_access",
            risk_level=SecurityRisk.MEDIUM,
            owasp_category=OWASPLLMCategory.LLM07_INSECURE_PLUGIN_DESIGN,
            description=f"{tool} enables file system modification",
            evidence={"tool": tool, "risk": "file_system_access"},
            mitigation=[
                "Implement path validation",
                "Add file type restrictions",
                "Enable file operation logging",
                "Validate write permissions",
                "Implement backup mechanisms"
            ],
            compliance_score=60.0,
            passed=True
        )


class ComponentSecurityBoundaryValidator:
    """Validates security isolation between components"""
    
    def __init__(self):
        self.component_boundaries = {}
        
    def validate_component_boundaries(self, components: List[Dict[str, Any]]) -> List[SecurityIntegrationResult]:
        """Validate security boundaries between components"""
        results = []
        
        # Analyze component interactions
        for i, comp_a in enumerate(components):
            for comp_b in components[i+1:]:
                boundary_analysis = self._analyze_component_boundary(comp_a, comp_b)
                if boundary_analysis.risk_assessment in [SecurityRisk.HIGH, SecurityRisk.CRITICAL]:
                    results.append(SecurityIntegrationResult(
                        test_name="component_boundary_violation",
                        integration_pattern="component_interaction",
                        risk_level=boundary_analysis.risk_assessment,
                        owasp_category=OWASPLLMCategory.LLM07_INSECURE_PLUGIN_DESIGN,
                        description=f"Security boundary risk between {comp_a['name']} and {comp_b['name']}",
                        evidence={
                            "component_a": comp_a['name'],
                            "component_b": comp_b['name'],
                            "vulnerabilities": boundary_analysis.vulnerabilities
                        },
                        mitigation=[
                            "Implement strict component isolation",
                            "Add interface validation",
                            "Enable interaction monitoring",
                            "Implement access controls"
                        ],
                        passed=False
                    ))
        
        return results
    
    def _analyze_component_boundary(self, comp_a: Dict, comp_b: Dict) -> ComponentSecurityBoundary:
        """Analyze security boundary between two components"""
        vulnerabilities = []
        security_controls = []
        
        # Check for shared sensitive data
        if self._shares_sensitive_data(comp_a, comp_b):
            vulnerabilities.append("shared_sensitive_data")
        
        # Check for privilege sharing
        if self._shares_privileges(comp_a, comp_b):
            vulnerabilities.append("shared_privileges")
        
        # Assess overall risk
        if len(vulnerabilities) >= 2:
            risk = SecurityRisk.HIGH
        elif len(vulnerabilities) == 1:
            risk = SecurityRisk.MEDIUM
        else:
            risk = SecurityRisk.LOW
            
        return ComponentSecurityBoundary(
            component_a=comp_a.get('name', 'unknown'),
            component_b=comp_b.get('name', 'unknown'),
            interaction_type="direct",
            security_controls=security_controls,
            vulnerabilities=vulnerabilities,
            risk_assessment=risk
        )
    
    def _shares_sensitive_data(self, comp_a: Dict, comp_b: Dict) -> bool:
        """Check if components share sensitive data inappropriately"""
        # Simplified analysis - would be enhanced with actual component analysis
        sensitive_keywords = ['password', 'token', 'key', 'secret', 'auth', 'credential']
        
        comp_a_content = str(comp_a).lower()
        comp_b_content = str(comp_b).lower()
        
        return any(keyword in comp_a_content and keyword in comp_b_content 
                  for keyword in sensitive_keywords)
    
    def _shares_privileges(self, comp_a: Dict, comp_b: Dict) -> bool:
        """Check if components inappropriately share privileges"""
        # Simplified analysis - would be enhanced with actual privilege analysis
        return (comp_a.get('category') == comp_b.get('category') and 
                'security' in str(comp_a).lower() and 
                'security' in str(comp_b).lower())


class WorkflowSecurityValidator:
    """Validates secure state management across workflow steps"""
    
    def __init__(self):
        self.workflow_states = {}
        
    def validate_workflow_security(self, workflow_steps: List[Dict[str, Any]]) -> List[SecurityIntegrationResult]:
        """Validate security across workflow execution"""
        results = []
        
        # Validate state transition security
        for i, step in enumerate(workflow_steps):
            if i > 0:
                transition_security = self._validate_state_transition(
                    workflow_steps[i-1], step, i
                )
                results.extend(transition_security)
        
        # Validate workflow completion security
        completion_security = self._validate_workflow_completion(workflow_steps)
        results.extend(completion_security)
        
        return results
    
    def _validate_state_transition(self, prev_step: Dict, current_step: Dict, step_index: int) -> List[SecurityIntegrationResult]:
        """Validate security of state transitions between workflow steps"""
        results = []
        
        # Check for state poisoning
        if self._has_state_poisoning_risk(prev_step, current_step):
            results.append(SecurityIntegrationResult(
                test_name="workflow_state_poisoning",
                integration_pattern="workflow_state_transition",
                risk_level=SecurityRisk.HIGH,
                owasp_category=OWASPLLMCategory.LLM03_TRAINING_DATA_POISONING,
                description=f"State poisoning risk at workflow step {step_index}",
                evidence={
                    "previous_step": prev_step.get('name', 'unknown'),
                    "current_step": current_step.get('name', 'unknown'),
                    "step_index": step_index
                },
                mitigation=[
                    "Implement state validation",
                    "Add state sanitization",
                    "Enable state monitoring",
                    "Implement rollback capabilities"
                ],
                passed=False
            ))
        
        return results
    
    def _has_state_poisoning_risk(self, prev_step: Dict, current_step: Dict) -> bool:
        """Check if state transition has poisoning risk"""
        # Simplified analysis - would be enhanced with actual state analysis
        risky_patterns = ['modify', 'update', 'change', 'alter']
        
        prev_content = str(prev_step).lower()
        current_content = str(current_step).lower()
        
        return (any(pattern in prev_content for pattern in risky_patterns) and
                any(pattern in current_content for pattern in risky_patterns))
    
    def _validate_workflow_completion(self, workflow_steps: List[Dict[str, Any]]) -> List[SecurityIntegrationResult]:
        """Validate security of workflow completion"""
        results = []
        
        # Check for incomplete security validation
        has_security_validation = any('security' in str(step).lower() 
                                    for step in workflow_steps)
        
        if not has_security_validation:
            results.append(SecurityIntegrationResult(
                test_name="missing_security_validation",
                integration_pattern="workflow_completion",
                risk_level=SecurityRisk.MEDIUM,
                owasp_category=OWASPLLMCategory.LLM07_INSECURE_PLUGIN_DESIGN,
                description="Workflow lacks security validation step",
                evidence={"workflow_steps": len(workflow_steps)},
                mitigation=[
                    "Add security validation step",
                    "Implement security testing",
                    "Add compliance checking",
                    "Enable security monitoring"
                ],
                passed=False
            ))
        
        return results


class IntegrationAttackSurfaceAnalyzer:
    """Analyzes security vulnerabilities in component interactions"""
    
    def __init__(self):
        self.attack_vectors = {
            "prompt_injection": {
                "patterns": ["ignore", "override", "system", "jailbreak"],
                "risk": SecurityRisk.CRITICAL,
                "owasp": OWASPLLMCategory.LLM01_PROMPT_INJECTION
            },
            "data_exfiltration": {
                "patterns": ["export", "dump", "leak", "extract"],
                "risk": SecurityRisk.HIGH,
                "owasp": OWASPLLMCategory.LLM06_SENSITIVE_INFO_DISCLOSURE
            },
            "command_injection": {
                "patterns": [";", "&&", "|", "`", "$"],
                "risk": SecurityRisk.CRITICAL,
                "owasp": OWASPLLMCategory.LLM08_EXCESSIVE_AGENCY
            }
        }
    
    def analyze_attack_surface(self, integration_points: List[Dict[str, Any]]) -> List[SecurityIntegrationResult]:
        """Analyze attack surface across integration points"""
        results = []
        
        for integration in integration_points:
            # Analyze each attack vector
            for vector_name, vector_config in self.attack_vectors.items():
                vector_analysis = self._analyze_attack_vector(
                    integration, vector_name, vector_config
                )
                if not vector_analysis.passed:
                    results.append(vector_analysis)
        
        return results
    
    def _analyze_attack_vector(self, integration: Dict, vector_name: str, 
                             vector_config: Dict) -> SecurityIntegrationResult:
        """Analyze specific attack vector against integration point"""
        integration_content = str(integration).lower()
        
        # Check for attack vector patterns
        found_patterns = [pattern for pattern in vector_config["patterns"] 
                         if pattern in integration_content]
        
        if found_patterns:
            return SecurityIntegrationResult(
                test_name=f"{vector_name}_vulnerability",
                integration_pattern="attack_surface",
                risk_level=vector_config["risk"],
                owasp_category=vector_config["owasp"],
                description=f"{vector_name.title()} vulnerability in integration",
                evidence={
                    "integration": integration.get('name', 'unknown'),
                    "patterns_found": found_patterns
                },
                mitigation=[
                    f"Implement {vector_name} prevention",
                    "Add input validation",
                    "Enable monitoring",
                    "Implement rate limiting"
                ],
                compliance_score=30.0,
                passed=False
            )
        else:
            return SecurityIntegrationResult(
                test_name=f"{vector_name}_safe",
                integration_pattern="attack_surface",
                risk_level=SecurityRisk.LOW,
                owasp_category=vector_config["owasp"],
                description=f"No {vector_name} vulnerability detected",
                compliance_score=90.0,
                passed=True
            )


class IntegrationSecurityTestSuite:
    """Comprehensive integration security test suite"""
    
    def __init__(self):
        self.cross_command_validator = CrossCommandSecurityValidator()
        self.boundary_validator = ComponentSecurityBoundaryValidator()
        self.workflow_validator = WorkflowSecurityValidator()
        self.attack_surface_analyzer = IntegrationAttackSurfaceAnalyzer()
        
    def run_comprehensive_integration_security_tests(self, 
                                                    integration_config: Dict[str, Any]) -> Dict[str, Any]:
        """Run complete integration security validation"""
        all_results = []
        
        # Extract test data from configuration
        commands = integration_config.get('commands', [])
        components = integration_config.get('components', [])
        workflows = integration_config.get('workflows', [])
        integration_points = integration_config.get('integration_points', [])
        
        # Run all security validations
        cross_command_results = self.cross_command_validator.validate_permission_inheritance(commands)
        all_results.extend(cross_command_results)
        
        boundary_results = self.boundary_validator.validate_component_boundaries(components)
        all_results.extend(boundary_results)
        
        workflow_results = self.workflow_validator.validate_workflow_security(workflows)
        all_results.extend(workflow_results)
        
        attack_surface_results = self.attack_surface_analyzer.analyze_attack_surface(integration_points)
        all_results.extend(attack_surface_results)
        
        # Generate comprehensive report
        return self._generate_integration_security_report(all_results, integration_config)
    
    def _generate_integration_security_report(self, results: List[SecurityIntegrationResult], 
                                            config: Dict[str, Any]) -> Dict[str, Any]:
        """Generate comprehensive integration security report"""
        passed_tests = [r for r in results if r.passed]
        failed_tests = [r for r in results if not r.passed]
        
        # Categorize by OWASP LLM categories
        owasp_summary = {}
        for category in OWASPLLMCategory:
            category_results = [r for r in results if r.owasp_category == category]
            category_failed = [r for r in category_results if not r.passed]
            owasp_summary[category.value] = {
                "total_tests": len(category_results),
                "failed_tests": len(category_failed),
                "compliance_percentage": ((len(category_results) - len(category_failed)) / len(category_results) * 100) if category_results else 100
            }
        
        # Calculate overall security score
        total_tests = len(results)
        security_score = (len(passed_tests) / total_tests * 100) if total_tests > 0 else 0
        
        # Risk level distribution
        risk_distribution = {}
        for risk in SecurityRisk:
            risk_count = len([r for r in failed_tests if r.risk_level == risk])
            risk_distribution[risk.value] = risk_count
        
        # Integration pattern analysis
        pattern_analysis = {}
        for result in results:
            pattern = result.integration_pattern
            if pattern not in pattern_analysis:
                pattern_analysis[pattern] = {"total": 0, "failed": 0}
            pattern_analysis[pattern]["total"] += 1
            if not result.passed:
                pattern_analysis[pattern]["failed"] += 1
        
        return {
            "integration_security_assessment": {
                "overall_security_score": security_score,
                "total_tests": total_tests,
                "passed_tests": len(passed_tests),
                "failed_tests": len(failed_tests),
                "compliance_status": "PASS" if security_score >= 85 else "FAIL"
            },
            "owasp_llm_compliance": owasp_summary,
            "risk_distribution": risk_distribution,
            "integration_pattern_analysis": pattern_analysis,
            "critical_vulnerabilities": [
                {
                    "test": r.test_name,
                    "pattern": r.integration_pattern,
                    "risk": r.risk_level.value,
                    "owasp_category": r.owasp_category.value,
                    "description": r.description,
                    "mitigation": r.mitigation
                }
                for r in failed_tests if r.risk_level in [SecurityRisk.HIGH, SecurityRisk.CRITICAL]
            ],
            "security_recommendations": self._generate_security_recommendations(failed_tests),
            "configuration_assessed": {
                "commands_count": len(config.get('commands', [])),
                "components_count": len(config.get('components', [])),
                "workflows_count": len(config.get('workflows', [])),
                "integration_points_count": len(config.get('integration_points', []))
            }
        }
    
    def _generate_security_recommendations(self, failed_tests: List[SecurityIntegrationResult]) -> List[str]:
        """Generate security recommendations based on failed tests"""
        recommendations = []
        
        # Group by OWASP category for targeted recommendations
        owasp_issues = {}
        for test in failed_tests:
            category = test.owasp_category.value
            if category not in owasp_issues:
                owasp_issues[category] = []
            owasp_issues[category].append(test)
        
        # Generate category-specific recommendations
        if OWASPLLMCategory.LLM01_PROMPT_INJECTION.value in owasp_issues:
            recommendations.append("CRITICAL: Implement prompt injection prevention framework")
            recommendations.append("Add input sanitization and validation for all user inputs")
            recommendations.append("Implement constitutional AI safety constraints")
        
        if OWASPLLMCategory.LLM08_EXCESSIVE_AGENCY.value in owasp_issues:
            recommendations.append("CRITICAL: Review and restrict tool permissions")
            recommendations.append("Implement least privilege principle across all commands")
            recommendations.append("Add approval workflows for high-risk operations")
        
        if OWASPLLMCategory.LLM06_SENSITIVE_INFO_DISCLOSURE.value in owasp_issues:
            recommendations.append("HIGH: Implement sensitive data filtering and sanitization")
            recommendations.append("Add information disclosure prevention controls")
            recommendations.append("Enable secure error handling without data leakage")
        
        if OWASPLLMCategory.LLM07_INSECURE_PLUGIN_DESIGN.value in owasp_issues:
            recommendations.append("MEDIUM: Strengthen component security boundaries")
            recommendations.append("Implement secure integration patterns")
            recommendations.append("Add component interaction monitoring")
        
        # Add general recommendations if no specific issues found
        if not recommendations:
            recommendations.append("Maintain current security posture with regular assessments")
            recommendations.append("Implement continuous security monitoring")
            recommendations.append("Regular security training and awareness programs")
        
        return recommendations


def create_integration_security_suite() -> IntegrationSecurityTestSuite:
    """Create a new integration security test suite instance"""
    return IntegrationSecurityTestSuite()


def validate_integration_security(integration_config: Dict[str, Any]) -> Dict[str, Any]:
    """Convenience function to validate integration security"""
    suite = create_integration_security_suite()
    return suite.run_comprehensive_integration_security_tests(integration_config)


if __name__ == "__main__":
    # Example integration configuration for testing
    example_config = {
        "commands": [
            {
                "name": "/auto",
                "allowed-tools": ["Read", "Write", "Edit", "Bash", "WebFetch"],
                "category": "routing"
            },
            {
                "name": "/task", 
                "allowed-tools": ["Read", "Write", "Edit", "Grep", "Glob", "Bash"],
                "category": "development"
            }
        ],
        "components": [
            {"name": "authentication", "category": "security"},
            {"name": "validation", "category": "security"},
            {"name": "reporting", "category": "output"}
        ],
        "workflows": [
            {"name": "tdd_workflow", "steps": ["analyze", "test", "implement", "validate"]},
            {"name": "security_review", "steps": ["scan", "assess", "remediate"]}
        ],
        "integration_points": [
            {"name": "command_routing", "type": "internal"},
            {"name": "external_api", "type": "external"},
            {"name": "file_system", "type": "system"}
        ]
    }
    
    # Run integration security validation
    security_suite = create_integration_security_suite()
    report = security_suite.run_comprehensive_integration_security_tests(example_config)
    
    print("=== INTEGRATION SECURITY VALIDATION REPORT ===")
    print(f"Overall Security Score: {report['integration_security_assessment']['overall_security_score']:.1f}%")
    print(f"Tests: {report['integration_security_assessment']['passed_tests']}/{report['integration_security_assessment']['total_tests']} passed")
    print(f"Compliance Status: {report['integration_security_assessment']['compliance_status']}")
    
    if report['critical_vulnerabilities']:
        print(f"\n🚨 CRITICAL VULNERABILITIES: {len(report['critical_vulnerabilities'])}")
        for vuln in report['critical_vulnerabilities'][:3]:  # Show top 3
            print(f"- {vuln['test']}: {vuln['description']}")
    
    print(f"\n📋 SECURITY RECOMMENDATIONS:")
    for rec in report['security_recommendations'][:5]:  # Show top 5
        print(f"- {rec}")