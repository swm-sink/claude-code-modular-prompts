#!/usr/bin/env python3
"""
Integration Security Assessment Runner
Analyzes the actual casablanca project structure for security validation
"""

import json
import os
import re
from pathlib import Path
from typing import Dict, List, Any
from integration_security_validation import (
    create_integration_security_suite,
    SecurityRisk,
    OWASPLLMCategory
)


def extract_command_configuration(commands_dir: Path) -> List[Dict[str, Any]]:
    """Extract command configurations from .claude/commands directory"""
    commands = []
    
    if not commands_dir.exists():
        return commands
    
    for command_file in commands_dir.rglob("*.md"):
        if command_file.name == "README.md" or "deprecated" in str(command_file):
            continue
            
        try:
            content = command_file.read_text(encoding='utf-8')
            
            # Extract YAML front matter
            yaml_match = re.search(r'^---\n(.*?)\n---', content, re.MULTILINE | re.DOTALL)
            command_config = {"name": command_file.stem, "file": str(command_file)}
            
            if yaml_match:
                yaml_content = yaml_match.group(1)
                
                # Parse basic YAML fields
                for line in yaml_content.split('\n'):
                    if ':' in line:
                        key, value = line.split(':', 1)
                        key = key.strip()
                        value = value.strip()
                        
                        if key == "allowed-tools":
                            # Parse tools list
                            tools = [tool.strip() for tool in value.split(',')]
                            command_config["allowed-tools"] = tools
                        else:
                            command_config[key] = value
            
            # Extract tool usage from content
            tools_in_content = []
            tool_patterns = ['Read', 'Write', 'Edit', 'Bash', 'WebFetch', 'WebSearch', 'Grep', 'Glob', 'LS']
            for tool in tool_patterns:
                if tool in content:
                    tools_in_content.append(tool)
            
            if tools_in_content and "allowed-tools" not in command_config:
                command_config["allowed-tools"] = tools_in_content
            
            commands.append(command_config)
            
        except Exception as e:
            print(f"Error processing {command_file}: {e}")
            continue
    
    return commands


def extract_component_configuration(components_dir: Path) -> List[Dict[str, Any]]:
    """Extract component configurations from .claude/components directory"""
    components = []
    
    if not components_dir.exists():
        return components
    
    for component_file in components_dir.rglob("*.md"):
        if component_file.name == "README.md":
            continue
            
        try:
            content = component_file.read_text(encoding='utf-8')
            
            component_config = {
                "name": component_file.stem,
                "category": component_file.parent.name,
                "file": str(component_file),
                "content_length": len(content)
            }
            
            # Analyze security-related content
            security_keywords = ['security', 'auth', 'validation', 'sanitize', 'encrypt']
            if any(keyword in content.lower() for keyword in security_keywords):
                component_config["security_related"] = True
            
            components.append(component_config)
            
        except Exception as e:
            print(f"Error processing {component_file}: {e}")
            continue
    
    return components


def extract_integration_points(project_dir: Path) -> List[Dict[str, Any]]:
    """Extract integration points from project structure"""
    integration_points = []
    
    # Command-to-command routing integrations
    integration_points.append({
        "name": "command_routing",
        "type": "internal",
        "description": "Command routing through /auto",
        "risk_factors": ["privilege_escalation", "permission_inheritance"]
    })
    
    # External tool integrations
    integration_points.append({
        "name": "bash_integration", 
        "type": "system",
        "description": "System command execution via Bash tool",
        "risk_factors": ["command_injection", "system_access"]
    })
    
    integration_points.append({
        "name": "web_integration",
        "type": "external", 
        "description": "External web access via WebFetch/WebSearch",
        "risk_factors": ["data_exfiltration", "supply_chain"]
    })
    
    # Component integration points
    integration_points.append({
        "name": "component_includes",
        "type": "internal",
        "description": "Component inclusion and dependency chain",
        "risk_factors": ["state_pollution", "boundary_violations"]
    })
    
    return integration_points


def analyze_settings_security(settings_file: Path) -> Dict[str, Any]:
    """Analyze .claude/settings.json for security configuration"""
    security_analysis = {
        "tools_enabled": [],
        "high_risk_tools": [],
        "security_controls": [],
        "recommendations": []
    }
    
    try:
        if settings_file.exists():
            with open(settings_file, 'r') as f:
                settings = json.load(f)
            
            tools = settings.get('tools', {})
            for tool, permission in tools.items():
                if permission == "allow":
                    security_analysis["tools_enabled"].append(tool)
                    
                    # Identify high-risk tools
                    if tool in ["Bash", "WebFetch", "WebSearch"]:
                        security_analysis["high_risk_tools"].append(tool)
            
            # Check for security controls
            if settings.get('hooks', {}).get('enabled'):
                security_analysis["security_controls"].append("hooks_enabled")
            
            if settings.get('memory', {}).get('enabled'):
                security_analysis["security_controls"].append("memory_enabled")
        
        # Generate recommendations
        if "Bash" in security_analysis["high_risk_tools"]:
            security_analysis["recommendations"].append("CRITICAL: Implement Bash command filtering")
        
        if len(security_analysis["high_risk_tools"]) > 2:
            security_analysis["recommendations"].append("HIGH: Review necessity of multiple high-risk tools")
        
        if not security_analysis["security_controls"]:
            security_analysis["recommendations"].append("MEDIUM: Enable security hooks and monitoring")
            
    except Exception as e:
        security_analysis["error"] = str(e)
    
    return security_analysis


def main():
    """Run comprehensive integration security assessment"""
    print("🔒 INTEGRATION SECURITY VALIDATION - COMPREHENSIVE ASSESSMENT")
    print("=" * 70)
    
    # Project paths
    project_dir = Path("/Users/smenssink/conductor/repo/claude-code-modular-prompts/casablanca")
    commands_dir = project_dir / ".claude" / "commands"
    components_dir = project_dir / ".claude" / "components" 
    settings_file = project_dir / ".claude" / "settings.json"
    
    # Extract actual project configuration
    print("📊 Extracting project configuration...")
    commands = extract_command_configuration(commands_dir)
    components = extract_component_configuration(components_dir)
    integration_points = extract_integration_points(project_dir)
    settings_security = analyze_settings_security(settings_file)
    
    print(f"✓ Found {len(commands)} commands")
    print(f"✓ Found {len(components)} components")
    print(f"✓ Identified {len(integration_points)} integration points")
    print(f"✓ Analyzed security settings")
    
    # Create integration configuration
    integration_config = {
        "commands": commands,
        "components": components,
        "workflows": [  # Extracted from common patterns
            {
                "name": "tdd_workflow",
                "steps": ["analyze", "test", "implement", "validate"],
                "commands_involved": ["/task", "/auto"]
            },
            {
                "name": "routing_workflow", 
                "steps": ["analyze_request", "select_command", "execute", "report"],
                "commands_involved": ["/auto"]
            }
        ],
        "integration_points": integration_points,
        "settings_security": settings_security
    }
    
    # Run security validation
    print("\n🔍 Running integration security validation...")
    security_suite = create_integration_security_suite()
    report = security_suite.run_comprehensive_integration_security_tests(integration_config)
    
    # Display comprehensive results
    print("\n" + "=" * 70)
    print("🛡️  INTEGRATION SECURITY ASSESSMENT RESULTS")
    print("=" * 70)
    
    assessment = report['integration_security_assessment']
    print(f"Overall Security Score: {assessment['overall_security_score']:.1f}%")
    print(f"Tests: {assessment['passed_tests']}/{assessment['total_tests']} passed")
    print(f"Compliance Status: {assessment['compliance_status']}")
    
    # OWASP LLM Compliance breakdown
    print(f"\n📋 OWASP LLM TOP 10 2025 COMPLIANCE:")
    owasp_compliance = report['owasp_llm_compliance']
    for category, metrics in owasp_compliance.items():
        if metrics['total_tests'] > 0:
            compliance_pct = metrics['compliance_percentage']
            status = "✅" if compliance_pct >= 85 else "⚠️" if compliance_pct >= 60 else "❌"
            print(f"  {status} {category}: {compliance_pct:.1f}% ({metrics['failed_tests']} failures)")
    
    # Risk distribution
    print(f"\n⚠️  RISK DISTRIBUTION:")
    risk_dist = report['risk_distribution']
    for risk_level, count in risk_dist.items():
        if count > 0:
            emoji = "🚨" if risk_level == "critical" else "⚠️" if risk_level == "high" else "🟡" if risk_level == "medium" else "ℹ️"
            print(f"  {emoji} {risk_level.upper()}: {count} issues")
    
    # Critical vulnerabilities
    critical_vulns = report['critical_vulnerabilities']
    if critical_vulns:
        print(f"\n🚨 CRITICAL VULNERABILITIES ({len(critical_vulns)}):")
        for i, vuln in enumerate(critical_vulns[:5], 1):  # Show top 5
            print(f"  {i}. {vuln['test']}")
            print(f"     Pattern: {vuln['pattern']}")
            print(f"     Risk: {vuln['risk'].upper()}")
            print(f"     OWASP: {vuln['owasp_category']}")
            print(f"     Description: {vuln['description']}")
            print(f"     Mitigation: {', '.join(vuln['mitigation'][:2])}")  # First 2 mitigations
            print()
    
    # Integration pattern analysis
    print(f"🔗 INTEGRATION PATTERN ANALYSIS:")
    pattern_analysis = report['integration_pattern_analysis']
    for pattern, metrics in pattern_analysis.items():
        if metrics['total'] > 0:
            failure_rate = (metrics['failed'] / metrics['total']) * 100
            status = "❌" if failure_rate > 50 else "⚠️" if failure_rate > 25 else "✅"
            print(f"  {status} {pattern}: {metrics['failed']}/{metrics['total']} failed ({failure_rate:.1f}%)")
    
    # Security recommendations
    print(f"\n💡 SECURITY RECOMMENDATIONS:")
    recommendations = report['security_recommendations']
    for i, rec in enumerate(recommendations, 1):
        priority = "🚨" if "CRITICAL" in rec else "⚠️" if "HIGH" in rec else "🟡" if "MEDIUM" in rec else "ℹ️"
        print(f"  {i}. {priority} {rec}")
    
    # Configuration summary
    config_assessed = report['configuration_assessed']
    print(f"\n📈 ASSESSMENT SCOPE:")
    print(f"  Commands Assessed: {config_assessed['commands_count']}")
    print(f"  Components Assessed: {config_assessed['components_count']}")
    print(f"  Workflows Assessed: {config_assessed['workflows_count']}")
    print(f"  Integration Points: {config_assessed['integration_points_count']}")
    
    # Settings security analysis
    print(f"\n⚙️  SETTINGS SECURITY ANALYSIS:")
    print(f"  High-Risk Tools Enabled: {len(settings_security['high_risk_tools'])}")
    if settings_security['high_risk_tools']:
        print(f"    Tools: {', '.join(settings_security['high_risk_tools'])}")
    print(f"  Security Controls: {len(settings_security['security_controls'])}")
    if settings_security['security_controls']:
        print(f"    Controls: {', '.join(settings_security['security_controls'])}")
    
    # Final status
    print("\n" + "=" * 70)
    overall_score = assessment['overall_security_score']
    if overall_score >= 85:
        print("🟢 INTEGRATION SECURITY STATUS: ACCEPTABLE")
    elif overall_score >= 60:
        print("🟡 INTEGRATION SECURITY STATUS: NEEDS IMPROVEMENT")
    else:
        print("🔴 INTEGRATION SECURITY STATUS: CRITICAL - IMMEDIATE ACTION REQUIRED")
    
    print("=" * 70)
    
    # Save detailed report
    report_file = project_dir / "tests" / "results" / "integration_security_validation_comprehensive.json"
    report_file.parent.mkdir(exist_ok=True)
    
    with open(report_file, 'w') as f:
        json.dump({
            **report,
            "project_configuration": integration_config,
            "assessment_metadata": {
                "timestamp": "2025-07-27",
                "agent": "security_integration",
                "scope": "comprehensive_integration_security"
            }
        }, f, indent=2, default=str)
    
    print(f"📄 Detailed report saved to: {report_file}")


if __name__ == "__main__":
    main()