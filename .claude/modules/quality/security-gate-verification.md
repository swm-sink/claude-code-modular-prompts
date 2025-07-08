| version | last_updated | status |
|---------|--------------|--------|
| 1.0.0   | 2025-07-08   | stable |

# Security Gate Verification Module

────────────────────────────────────────────────────────────────────────────────

<thinking_pattern>
Identify security requirements → Run threat modeling → Scan for vulnerabilities → Verify mitigations → Generate evidence → Block if failed
</thinking_pattern>

<module>
  <name>security-gate-verification</name>
  <version>1.0.0</version>
  <description>Automated security verification with threat modeling enforcement</description>
  <dependencies>
    <required>threat-modeling.md</required>
    <required>audit.md</required>
    <required>production-standards.md</required>
  </dependencies>
</module>

────────────────────────────────────────────────────────────────────────────────

## Security Verification Workflow

```xml
<security_verification>
  <workflow>
    <phase name="ThreatModeling" required="true">
      <step>1. Identify assets and data flows</step>
      <step>2. Enumerate potential threats (STRIDE)</step>
      <step>3. Risk assessment and prioritization</step>
      <step>4. Document mitigation strategies</step>
      <output>threat-model-{task_id}.json</output>
    </phase>
    
    <phase name="VulnerabilityScanning" required="true">
      <step>1. Static code analysis (SAST)</step>
      <step>2. Dependency vulnerability check</step>
      <step>3. Secret detection scan</step>
      <step>4. Configuration security review</step>
      <output>vulnerability-report-{task_id}.json</output>
    </phase>
    
    <phase name="MitigationVerification" required="true">
      <step>1. Verify all high-risk threats addressed</step>
      <step>2. Confirm security controls implemented</step>
      <step>3. Validate authentication/authorization</step>
      <step>4. Test security boundaries</step>
      <output>mitigation-evidence-{task_id}.json</output>
    </phase>
  </workflow>
</security_verification>
```

────────────────────────────────────────────────────────────────────────────────

## Threat Modeling Automation

```python
# Automated Threat Modeling Engine
class ThreatModelVerifier:
    def __init__(self):
        self.threats = []
        self.mitigations = {}
        self.risk_threshold = "HIGH"
        
    def model_threats(self, component_analysis):
        """Apply STRIDE methodology automatically"""
        threats = {
            "Spoofing": self.check_authentication(component_analysis),
            "Tampering": self.check_data_integrity(component_analysis),
            "Repudiation": self.check_audit_logging(component_analysis),
            "Information Disclosure": self.check_data_exposure(component_analysis),
            "Denial of Service": self.check_resource_limits(component_analysis),
            "Elevation of Privilege": self.check_authorization(component_analysis)
        }
        
        # Generate threat model
        threat_model = {
            "component": component_analysis["name"],
            "data_flows": self.map_data_flows(component_analysis),
            "threats": threats,
            "risk_ratings": self.calculate_risks(threats),
            "required_mitigations": self.generate_mitigations(threats)
        }
        
        return threat_model
        
    def verify_mitigations(self, threat_model, implementation):
        """Verify all required mitigations are implemented"""
        evidence = {
            "threat_model_id": threat_model["id"],
            "timestamp": datetime.utcnow().isoformat(),
            "mitigations_verified": []
        }
        
        for threat, mitigation in threat_model["required_mitigations"].items():
            verification = {
                "threat": threat,
                "mitigation": mitigation,
                "implemented": self.check_mitigation_implementation(
                    mitigation, implementation
                ),
                "evidence": self.collect_mitigation_evidence(mitigation)
            }
            evidence["mitigations_verified"].append(verification)
            
        return evidence
```

────────────────────────────────────────────────────────────────────────────────

## Security Scanning Integration

```xml
<security_scanning>
  <static_analysis>
    <tool name="bandit" language="python">
      <severity_threshold>MEDIUM</severity_threshold>
      <ignore_rules>[]</ignore_rules>
      <output_format>json</output_format>
    </tool>
    
    <tool name="semgrep" language="multi">
      <rulesets>
        <ruleset>security</ruleset>
        <ruleset>secrets</ruleset>
        <ruleset>owasp</ruleset>
      </rulesets>
    </tool>
  </static_analysis>
  
  <dependency_scanning>
    <tool name="safety" type="python">
      <check>Known vulnerabilities</check>
      <check>License compliance</check>
      <check>Outdated packages</check>
    </tool>
    
    <tool name="npm-audit" type="javascript">
      <severity_threshold>moderate</severity_threshold>
      <auto_fix>false</auto_fix>
    </tool>
  </dependency_scanning>
  
  <secret_detection>
    <tool name="gitleaks">
      <scan_history>true</scan_history>
      <entropy_threshold>4.5</entropy_threshold>
      <custom_patterns>config/secret-patterns.toml</custom_patterns>
    </tool>
  </secret_detection>
</security_scanning>
```

────────────────────────────────────────────────────────────────────────────────

## Security Gates

```xml
<security_gates>
  <gate name="PreDevelopment" blocking="true">
    <requirement>Threat model completed</requirement>
    <requirement>Security requirements defined</requirement>
    <requirement>Risk assessment approved</requirement>
    <evidence>threat-model-approved.json</evidence>
  </gate>
  
  <gate name="PreCommit" blocking="true">
    <requirement>No HIGH severity vulnerabilities</requirement>
    <requirement>No hardcoded secrets</requirement>
    <requirement>Security tests passing</requirement>
    <evidence>security-scan-clean.json</evidence>
  </gate>
  
  <gate name="PreMerge" blocking="true">
    <requirement>All mitigations implemented</requirement>
    <requirement>Security review completed</requirement>
    <requirement>Penetration test passed (if applicable)</requirement>
    <evidence>security-clearance.json</evidence>
  </gate>
</security_gates>
```

────────────────────────────────────────────────────────────────────────────────

## Verification Commands

```bash
# Run complete security verification
verify_security() {
    local task_id=$1
    local code_path=$2
    
    echo "🔒 Starting Security Verification for $task_id"
    
    # Phase 1: Threat Modeling
    echo "📊 Generating threat model..."
    python -m security.threat_modeler \
        --component "$code_path" \
        --output "evidence/security/$task_id/threat-model.json"
    
    # Phase 2: Vulnerability Scanning
    echo "🔍 Running security scans..."
    
    # SAST
    bandit -r "$code_path" -f json \
        -o "evidence/security/$task_id/bandit-report.json"
    
    # Secrets
    gitleaks detect --source "$code_path" \
        --report-path "evidence/security/$task_id/secrets-scan.json"
    
    # Dependencies
    safety check --json \
        --output "evidence/security/$task_id/dependency-scan.json"
    
    # Phase 3: Verification
    echo "✓ Verifying mitigations..."
    python -m security.mitigation_verifier \
        --threat-model "evidence/security/$task_id/threat-model.json" \
        --scan-results "evidence/security/$task_id/" \
        --output "evidence/security/$task_id/verification-report.json"
}

# Pre-commit security check
pre_commit_security() {
    local violations=$(verify_security "pre-commit" ".")
    if [[ $? -ne 0 ]]; then
        echo "🚫 SECURITY GATE FAILED"
        echo "$violations"
        exit 1
    fi
}
```

────────────────────────────────────────────────────────────────────────────────

## Evidence Collection

```xml
<evidence_collection>
  <threat_model_evidence>
    <artifact>Component diagram with trust boundaries</artifact>
    <artifact>Data flow diagram with security annotations</artifact>
    <artifact>STRIDE analysis matrix</artifact>
    <artifact>Risk rating justifications</artifact>
    <store>evidence/security/{task_id}/threat-model/</store>
  </threat_model_evidence>
  
  <scan_evidence>
    <artifact>SAST scan results</artifact>
    <artifact>Dependency vulnerability report</artifact>
    <artifact>Secret scan results</artifact>
    <artifact>Configuration review findings</artifact>
    <store>evidence/security/{task_id}/scans/</store>
  </scan_evidence>
  
  <mitigation_evidence>
    <artifact>Implementation proof for each threat</artifact>
    <artifact>Security control test results</artifact>
    <artifact>Penetration test report (if applicable)</artifact>
    <store>evidence/security/{task_id}/mitigations/</store>
  </mitigation_evidence>
</evidence_collection>
```

────────────────────────────────────────────────────────────────────────────────

## Compliance Report Template

```markdown
# Security Compliance Report

**Task ID**: {task_id}
**Date**: {date}
**Security Review**: {reviewer}

## Threat Model ✓
- Components Analyzed: {component_count}
- Threats Identified: {threat_count}
- Risk Ratings: {high}/{medium}/{low}
- [Full Threat Model](evidence/security/{task_id}/threat-model.json)

## Vulnerability Scan Results ✓
- SAST Issues: {sast_count} (High: {high}, Medium: {medium})
- Dependency Vulnerabilities: {dep_vulns}
- Secrets Found: {secrets_count}
- [Scan Reports](evidence/security/{task_id}/scans/)

## Mitigation Status ✓
- Required Mitigations: {required_count}
- Implemented: {implemented_count}
- Verified: {verified_count}
- [Verification Evidence](evidence/security/{task_id}/mitigations/)

## Security Gates
- ✅ Pre-Development: Threat model approved
- ✅ Pre-Commit: No critical vulnerabilities
- ✅ Pre-Merge: All mitigations verified

## Compliance Certificate
Security requirements met. All gates PASSED.
```

────────────────────────────────────────────────────────────────────────────────

  <integration_points>
    <depends_on>
      security/threat-modeling.md for automated threat generation
      security/audit.md for security audit procedures
      quality/production-standards.md for security standards integration
      quality/gate-verification.md for quality gate orchestration
    </depends_on>
    <provides_to>
      quality/gate-verification.md for security gate results
      development/task-management.md for security-aware development
      planning/feature-workflow.md for security planning
      patterns/multi-agent.md for cross-agent security verification
    </provides_to>
  </integration_points>
  
</module>
```

## Integration Points

```xml
<integration>
  <with module="threat-modeling.md">
    <hook>Automated threat generation</hook>
    <hook>Risk calculation engine</hook>
    <hook>Mitigation templates</hook>
  </with>
  
  <with module="production-standards.md">
    <hook>Gate enforcement</hook>
    <hook>Compliance tracking</hook>
    <hook>Evidence archival</hook>
  </with>
  
  <with module="git-operations.md">
    <hook>Pre-commit security scan</hook>
    <hook>PR security review</hook>
    <hook>Merge protection rules</hook>
  </with>
</integration>
```