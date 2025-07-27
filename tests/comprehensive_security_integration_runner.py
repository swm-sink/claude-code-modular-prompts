#!/usr/bin/env python3
"""
Comprehensive Security Integration Assessment
Combines OWASP LLM validation with Constitutional AI assessment for complete security analysis
"""

import json
import sys
from pathlib import Path
from run_integration_security_assessment import (
    extract_command_configuration,
    extract_component_configuration, 
    extract_integration_points,
    analyze_settings_security
)
from integration_security_validation import create_integration_security_suite
from constitutional_ai_security_validation import run_constitutional_ai_validation


def run_comprehensive_security_assessment():
    """Run complete security assessment combining all frameworks"""
    print("🔒 COMPREHENSIVE INTEGRATION SECURITY ASSESSMENT")
    print("Security Integration Agent - Full Spectrum Analysis")
    print("=" * 80)
    
    # Project paths
    project_dir = Path("/Users/smenssink/conductor/repo/claude-code-modular-prompts/casablanca")
    commands_dir = project_dir / ".claude" / "commands"
    components_dir = project_dir / ".claude" / "components"
    settings_file = project_dir / ".claude" / "settings.json"
    
    # Extract actual project configuration
    print("📊 Extracting comprehensive project configuration...")
    commands = extract_command_configuration(commands_dir)
    components = extract_component_configuration(components_dir)
    integration_points = extract_integration_points(project_dir)
    settings_security = analyze_settings_security(settings_file)
    
    print(f"✓ Commands: {len(commands)}")
    print(f"✓ Components: {len(components)}")
    print(f"✓ Integration Points: {len(integration_points)}")
    print(f"✓ Security Settings Analysis Complete")
    
    # Create comprehensive integration configuration
    integration_config = {
        "commands": commands,
        "components": components,
        "workflows": [
            {
                "name": "auto_routing_workflow",
                "steps": ["analyze_request", "route_command", "execute", "report"],
                "commands_involved": ["/auto", "/task", "/query"],
                "autonomy_level": "high"
            },
            {
                "name": "tdd_development_workflow", 
                "steps": ["analyze", "test", "implement", "validate", "deploy"],
                "commands_involved": ["/task"],
                "autonomy_level": "medium"
            },
            {
                "name": "security_assessment_workflow",
                "steps": ["scan", "assess", "validate", "report"],
                "commands_involved": ["/secure-assess"],
                "autonomy_level": "low"
            }
        ],
        "integration_points": integration_points,
        "settings_security": settings_security
    }
    
    # Run OWASP LLM Security Validation
    print("\n🛡️  Running OWASP LLM Security Assessment...")
    security_suite = create_integration_security_suite()
    owasp_report = security_suite.run_comprehensive_integration_security_tests(integration_config)
    
    # Run Constitutional AI Validation
    print("🏛️  Running Constitutional AI Assessment...")
    constitutional_report = run_constitutional_ai_validation(integration_config)
    
    # Combine assessments
    combined_assessment = combine_security_assessments(owasp_report, constitutional_report, integration_config)
    
    # Display comprehensive results
    display_comprehensive_results(combined_assessment)
    
    # Save comprehensive report
    save_comprehensive_report(combined_assessment, project_dir)
    
    return combined_assessment


def combine_security_assessments(owasp_report, constitutional_report, config):
    """Combine OWASP LLM and Constitutional AI assessments"""
    
    # Calculate weighted security scores
    owasp_score = owasp_report['integration_security_assessment']['overall_security_score']
    constitutional_score = constitutional_report['constitutional_compliance_assessment']['overall_compliance_score']
    
    # Weight: OWASP 60%, Constitutional 40% (both critical)
    combined_score = (owasp_score * 0.6) + (constitutional_score * 0.4)
    
    # Determine overall compliance status
    if combined_score >= 90:
        compliance_status = "EXCELLENT"
    elif combined_score >= 80:
        compliance_status = "GOOD"
    elif combined_score >= 70:
        compliance_status = "ACCEPTABLE"
    elif combined_score >= 50:
        compliance_status = "NEEDS_IMPROVEMENT"
    else:
        compliance_status = "CRITICAL"
    
    # Combine critical issues
    critical_issues = []
    
    # OWASP critical vulnerabilities
    for vuln in owasp_report.get('critical_vulnerabilities', []):
        critical_issues.append({
            "type": "owasp_vulnerability",
            "category": vuln['owasp_category'],
            "description": vuln['description'],
            "risk_level": vuln['risk'],
            "mitigation": vuln['mitigation']
        })
    
    # Constitutional critical violations
    for violation in constitutional_report.get('critical_constitutional_violations', []):
        critical_issues.append({
            "type": "constitutional_violation",
            "category": violation['type'],
            "description": violation['description'],
            "risk_level": violation['severity'],
            "mitigation": violation['remediation']
        })
    
    # Generate unified recommendations
    unified_recommendations = generate_unified_recommendations(owasp_report, constitutional_report)
    
    # Calculate risk metrics
    total_critical_risks = len([issue for issue in critical_issues if issue['risk_level'] in ['critical', 'severe']])
    total_high_risks = len([issue for issue in critical_issues if issue['risk_level'] in ['high', 'serious']])
    
    return {
        "comprehensive_security_assessment": {
            "overall_security_score": combined_score,
            "compliance_status": compliance_status,
            "owasp_llm_score": owasp_score,
            "constitutional_ai_score": constitutional_score,
            "total_critical_risks": total_critical_risks,
            "total_high_risks": total_high_risks,
            "assessment_scope": {
                "commands_assessed": len(config['commands']),
                "components_assessed": len(config['components']),
                "workflows_assessed": len(config['workflows']),
                "integration_points": len(config['integration_points'])
            }
        },
        "detailed_assessments": {
            "owasp_llm_assessment": owasp_report,
            "constitutional_ai_assessment": constitutional_report
        },
        "critical_security_issues": critical_issues,
        "unified_security_recommendations": unified_recommendations,
        "security_frameworks_applied": [
            "OWASP LLM Top 10 2025",
            "Constitutional AI Principles",
            "Integration Security Patterns",
            "Tool Permission Security Matrix"
        ],
        "project_configuration": config
    }


def generate_unified_recommendations(owasp_report, constitutional_report):
    """Generate unified security recommendations from both assessments"""
    
    unified_recommendations = []
    
    # Critical actions from both assessments
    owasp_recommendations = owasp_report.get('security_recommendations', [])
    constitutional_recommendations = constitutional_report.get('constitutional_recommendations', [])
    
    # Prioritize critical recommendations
    critical_patterns = ['CRITICAL', 'critical', 'IMMEDIATE']
    high_patterns = ['HIGH', 'high', 'URGENT']
    
    # Combine and deduplicate critical recommendations
    all_recommendations = set(owasp_recommendations + constitutional_recommendations)
    
    # Sort by priority
    for rec in all_recommendations:
        if any(pattern in rec for pattern in critical_patterns):
            unified_recommendations.append(f"🚨 CRITICAL: {rec}")
        elif any(pattern in rec for pattern in high_patterns):
            unified_recommendations.append(f"⚠️ HIGH: {rec}")
        else:
            unified_recommendations.append(f"📋 MEDIUM: {rec}")
    
    # Add unified framework recommendations
    unified_recommendations.extend([
        "🛡️ FRAMEWORK: Implement comprehensive security governance",
        "🏛️ CONSTITUTIONAL: Deploy constitutional AI safety framework",
        "🔍 MONITORING: Enable continuous security monitoring and assessment",
        "📚 TRAINING: Implement security awareness and constitutional AI training",
        "🔄 VALIDATION: Establish regular security validation processes"
    ])
    
    return sorted(unified_recommendations, key=lambda x: (
        0 if "CRITICAL" in x else 1 if "HIGH" in x else 2 if "MEDIUM" in x else 3
    ))


def display_comprehensive_results(assessment):
    """Display comprehensive security assessment results"""
    
    overall = assessment['comprehensive_security_assessment']
    
    print("\n" + "=" * 80)
    print("🔒 COMPREHENSIVE SECURITY ASSESSMENT RESULTS")
    print("=" * 80)
    
    # Overall scores
    print(f"🎯 OVERALL SECURITY SCORE: {overall['overall_security_score']:.1f}%")
    print(f"📊 COMPLIANCE STATUS: {overall['compliance_status']}")
    print(f"🛡️  OWASP LLM Score: {overall['owasp_llm_score']:.1f}%")
    print(f"🏛️  Constitutional AI Score: {overall['constitutional_ai_score']:.1f}%")
    
    # Risk summary
    print(f"\n⚠️  RISK SUMMARY:")
    print(f"   🚨 Critical Risks: {overall['total_critical_risks']}")
    print(f"   ⚠️ High Risks: {overall['total_high_risks']}")
    
    # Assessment scope
    scope = overall['assessment_scope']
    print(f"\n📈 ASSESSMENT SCOPE:")
    print(f"   Commands: {scope['commands_assessed']}")
    print(f"   Components: {scope['components_assessed']}")
    print(f"   Workflows: {scope['workflows_assessed']}")
    print(f"   Integration Points: {scope['integration_points']}")
    
    # Critical security issues (top 10)
    critical_issues = assessment['critical_security_issues']
    if critical_issues:
        print(f"\n🚨 CRITICAL SECURITY ISSUES (Top 10):")
        for i, issue in enumerate(critical_issues[:10], 1):
            risk_emoji = "🚨" if issue['risk_level'] in ['critical', 'severe'] else "⚠️"
            print(f"   {i}. {risk_emoji} [{issue['type'].upper()}] {issue['description']}")
    
    # Top recommendations (first 15)
    recommendations = assessment['unified_security_recommendations']
    print(f"\n💡 UNIFIED SECURITY RECOMMENDATIONS (Top 15):")
    for i, rec in enumerate(recommendations[:15], 1):
        print(f"   {i}. {rec}")
    
    # Security frameworks applied
    frameworks = assessment['security_frameworks_applied']
    print(f"\n🔧 SECURITY FRAMEWORKS APPLIED:")
    for framework in frameworks:
        print(f"   ✓ {framework}")
    
    # Final security determination
    print("\n" + "=" * 80)
    score = overall['overall_security_score']
    if score >= 85:
        print("🟢 SECURITY DETERMINATION: ACCEPTABLE FOR PRODUCTION")
        print("   Regular monitoring and maintenance required")
    elif score >= 70:
        print("🟡 SECURITY DETERMINATION: IMPROVEMENTS REQUIRED")
        print("   Address high-priority issues before production deployment")
    elif score >= 50:
        print("🟠 SECURITY DETERMINATION: SIGNIFICANT IMPROVEMENTS REQUIRED")
        print("   Major security work needed before production consideration")
    else:
        print("🔴 SECURITY DETERMINATION: CRITICAL - DO NOT DEPLOY")
        print("   Immediate and comprehensive security remediation required")
    
    print("=" * 80)


def save_comprehensive_report(assessment, project_dir):
    """Save comprehensive security assessment report"""
    
    # Save JSON report
    json_file = project_dir / "tests" / "results" / "comprehensive_security_assessment.json"
    json_file.parent.mkdir(exist_ok=True)
    
    with open(json_file, 'w') as f:
        json.dump(assessment, f, indent=2, default=str)
    
    print(f"📄 Comprehensive assessment saved: {json_file}")
    
    # Generate executive summary
    executive_summary = generate_executive_summary(assessment)
    
    summary_file = project_dir / "SECURITY-EXECUTIVE-SUMMARY.md"
    with open(summary_file, 'w') as f:
        f.write(executive_summary)
    
    print(f"📋 Executive summary saved: {summary_file}")


def generate_executive_summary(assessment):
    """Generate executive summary of security assessment"""
    
    overall = assessment['comprehensive_security_assessment']
    
    summary = f"""# Security Assessment Executive Summary

**Security Integration Agent - Comprehensive Assessment**
**Date**: 2025-07-27
**Status**: {overall['compliance_status']}

## Key Findings

### Security Scores
- **Overall Security Score**: {overall['overall_security_score']:.1f}%
- **OWASP LLM Compliance**: {overall['owasp_llm_score']:.1f}%
- **Constitutional AI Compliance**: {overall['constitutional_ai_score']:.1f}%

### Risk Summary
- **Critical Risks**: {overall['total_critical_risks']}
- **High Risks**: {overall['total_high_risks']}

### Assessment Scope
- **Commands Assessed**: {overall['assessment_scope']['commands_assessed']}
- **Components Assessed**: {overall['assessment_scope']['components_assessed']}
- **Workflows Assessed**: {overall['assessment_scope']['workflows_assessed']}
- **Integration Points**: {overall['assessment_scope']['integration_points']}

## Executive Recommendation

"""
    
    score = overall['overall_security_score']
    if score >= 85:
        summary += "✅ **APPROVED FOR PRODUCTION** with regular security monitoring.\n"
    elif score >= 70:
        summary += "🟡 **CONDITIONAL APPROVAL** - Address high-priority security issues.\n"
    elif score >= 50:
        summary += "⚠️ **SIGNIFICANT WORK REQUIRED** - Major security improvements needed.\n"
    else:
        summary += "❌ **DO NOT DEPLOY** - Critical security vulnerabilities must be resolved.\n"
    
    summary += f"""
## Top Priority Actions

"""
    
    # Add top 5 recommendations
    for i, rec in enumerate(assessment['unified_security_recommendations'][:5], 1):
        summary += f"{i}. {rec}\n"
    
    summary += f"""
## Security Frameworks Applied
- OWASP LLM Top 10 2025
- Constitutional AI Principles  
- Integration Security Patterns
- Tool Permission Security Matrix

---
*Security Integration Agent - Comprehensive Assessment Complete*
"""
    
    return summary


if __name__ == "__main__":
    try:
        assessment = run_comprehensive_security_assessment()
        sys.exit(0)
    except Exception as e:
        print(f"❌ Security assessment failed: {e}")
        sys.exit(1)