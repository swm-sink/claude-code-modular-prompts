| version | last_updated | status |
|---------|--------------|--------|
| 1.0.0   | 2025-07-08   | stable |

# Quality Gate Verification Module

────────────────────────────────────────────────────────────────────────────────


────────────────────────────────────────────────────────────────────────────────

```xml
<module name="gate_verification" category="quality">
  
  <purpose>
    Automated quality gate verification system with evidence requirements, non-bypassable enforcement, and real-time quality monitoring.
  </purpose>
  
  <thinking_pattern enforcement="MANDATORY">
    <step>1. Parse quality requirements from production-standards.md</step>
    <step>2. Execute TDD verification with evidence collection</step>
    <step>3. Run security gate verification and threat modeling</step>
    <step>4. Perform performance benchmark testing</step>
    <step>5. Validate quality gate compliance with evidence</step>
    <step>6. Generate automated pass/fail reports</step>
    <step>7. Block progression if ANY gate fails</step>
    <step>8. Archive evidence for audit trail</step>
  </thinking_pattern>
  
  <trigger_conditions>
    <condition type="automatic">Pre-commit hooks, CI/CD pipeline integration</condition>
    <condition type="explicit">Quality verification requests, production deployment gates</condition>
  </trigger_conditions>
  
  <implementation>
    
    <quality_gate_engine>
      
      <gate_definitions>
        <gate name="TDD_COMPLIANCE" priority="CRITICAL" blocking="true">
          <requirements>
            <requirement>RED phase evidence: failing test BEFORE implementation</requirement>
            <requirement>GREEN phase evidence: test passes with minimal implementation</requirement>
            <requirement>REFACTOR phase evidence: improved code quality, tests still pass</requirement>
            <requirement>Coverage evidence: 90%+ test coverage with meaningful assertions</requirement>
          </requirements>
          <evidence_collection>
            <artifact>test-failure-output-{timestamp}.json</artifact>
            <artifact>test-success-output-{timestamp}.json</artifact>
            <artifact>coverage-report-{timestamp}.html</artifact>
            <artifact>refactor-metrics-{timestamp}.json</artifact>
          </evidence_collection>
          <verification_script>scripts/verify_tdd_compliance.py</verification_script>
        </gate>
        
        <gate name="SECURITY_VERIFICATION" priority="CRITICAL" blocking="true">
          <requirements>
            <requirement>Threat model completed and approved</requirement>
            <requirement>SAST scan passed: zero HIGH severity issues</requirement>
            <requirement>Dependency scan clean: no known vulnerabilities</requirement>
            <requirement>Secret scan clean: no hardcoded credentials</requirement>
            <requirement>Security controls implemented and tested</requirement>
          </requirements>
          <evidence_collection>
            <artifact>threat-model-{timestamp}.json</artifact>
            <artifact>sast-scan-results-{timestamp}.json</artifact>
            <artifact>dependency-scan-{timestamp}.json</artifact>
            <artifact>secret-scan-{timestamp}.json</artifact>
            <artifact>security-test-results-{timestamp}.json</artifact>
          </evidence_collection>
          <verification_script>scripts/verify_security_compliance.py</verification_script>
        </gate>
        
        <gate name="PERFORMANCE_BENCHMARKS" priority="HIGH" blocking="true">
          <requirements>
            <requirement>p95 response time under 200ms</requirement>
            <requirement>Memory usage within defined limits</requirement>
            <requirement>CPU utilization under 80% sustained</requirement>
            <requirement>Load testing passed: 10x expected traffic</requirement>
            <requirement>No performance regressions vs baseline</requirement>
          </requirements>
          <evidence_collection>
            <artifact>performance-baseline-{timestamp}.json</artifact>
            <artifact>load-test-results-{timestamp}.json</artifact>
            <artifact>memory-profile-{timestamp}.json</artifact>
            <artifact>cpu-profile-{timestamp}.json</artifact>
            <artifact>regression-analysis-{timestamp}.json</artifact>
          </evidence_collection>
          <verification_script>scripts/verify_performance_benchmarks.py</verification_script>
        </gate>
        
        <gate name="CODE_QUALITY" priority="HIGH" blocking="true">
          <requirements>
            <requirement>Zero linting errors</requirement>
            <requirement>Cyclomatic complexity under 10</requirement>
            <requirement>Code duplication under 3%</requirement>
            <requirement>Technical debt ratio under 5%</requirement>
            <requirement>Dependency health score above 90%</requirement>
          </requirements>
          <evidence_collection>
            <artifact>lint-results-{timestamp}.json</artifact>
            <artifact>complexity-analysis-{timestamp}.json</artifact>
            <artifact>duplication-report-{timestamp}.json</artifact>
            <artifact>technical-debt-{timestamp}.json</artifact>
            <artifact>dependency-health-{timestamp}.json</artifact>
          </evidence_collection>
          <verification_script>scripts/verify_code_quality.py</verification_script>
        </gate>
        
        <gate name="DOCUMENTATION_COMPLIANCE" priority="MEDIUM" blocking="false">
          <requirements>
            <requirement>API documentation generated and current</requirement>
            <requirement>Code comments for complex functions</requirement>
            <requirement>README updated with new features</requirement>
            <requirement>Architecture decision records updated</requirement>
          </requirements>
          <evidence_collection>
            <artifact>api-docs-{timestamp}.html</artifact>
            <artifact>code-coverage-docs-{timestamp}.json</artifact>
            <artifact>readme-changes-{timestamp}.diff</artifact>
            <artifact>architecture-decisions-{timestamp}.md</artifact>
          </evidence_collection>
          <verification_script>scripts/verify_documentation.py</verification_script>
        </gate>
        
      </gate_definitions>
      
      <enforcement_engine>
        <blocking_gates>
          <rule>ANY gate marked as blocking=true MUST pass to proceed</rule>
          <rule>Critical priority gates cannot be bypassed without manual override</rule>
          <rule>Override requires explicit justification and audit trail</rule>
          <rule>Failed gates prevent commit, merge, and deployment</rule>
        </blocking_gates>
        
        <evidence_requirements>
          <rule>ALL evidence artifacts MUST be generated and stored</rule>
          <rule>Evidence retention: 3 years for compliance</rule>
          <rule>Evidence tampering detection via checksums</rule>
          <rule>Audit trail for all gate executions and results</rule>
        </evidence_requirements>
        
        <automation_hooks>
          <pre_commit>Run TDD and code quality gates</pre_commit>
          <pre_merge>Run all gates including performance</pre_merge>
          <pre_deploy>Full gate suite with security emphasis</pre_deploy>
          <continuous>Performance monitoring and regression detection</continuous>
        </automation_hooks>
      </enforcement_engine>
      
      <real_time_monitoring>
        <dashboard_integration>
          <metric>Gate pass/fail rates by type</metric>
          <metric>Evidence collection completeness</metric>
          <metric>Override frequency and justifications</metric>
          <metric>Time to resolution for failed gates</metric>
        </dashboard_integration>
        
        <alerting_system>
          <alert condition="gate_failure_rate > 20%">Quality degradation detected</alert>
          <alert condition="override_frequency > 5%">Gate bypassing concerning</alert>
          <alert condition="evidence_missing > 1%">Audit trail incomplete</alert>
          <alert condition="resolution_time > 2_hours">Gate failures blocking progress</alert>
        </alerting_system>
        
        <predictive_analytics>
          <prediction>Gate failure probability based on code changes</prediction>
          <prediction>Quality debt accumulation rate</prediction>
          <prediction>Optimal gate timing for minimal disruption</prediction>
          <prediction>Resource requirements for gate execution</prediction>
        </predictive_analytics>
      </real_time_monitoring>
      
    </quality_gate_engine>
    
    <verification_workflows>
      
      <tdd_evidence_workflow>
        <phase name="RED_VERIFICATION">
          <step>1. Detect test file creation/modification</step>
          <step>2. Execute tests and capture failure output</step>
          <step>3. Verify test fails for expected reasons</step>
          <step>4. Confirm no implementation exists yet</step>
          <step>5. Store RED phase evidence</step>
          <output>evidence/tdd/{task_id}/red-phase-evidence.json</output>
        </phase>
        
        <phase name="GREEN_VERIFICATION">
          <step>1. Detect implementation file creation/modification</step>
          <step>2. Execute tests and capture success output</step>
          <step>3. Verify minimal implementation approach</step>
          <step>4. Measure code coverage increase</step>
          <step>5. Store GREEN phase evidence</step>
          <output>evidence/tdd/{task_id}/green-phase-evidence.json</output>
        </phase>
        
        <phase name="REFACTOR_VERIFICATION">
          <step>1. Detect code quality improvements</step>
          <step>2. Verify tests still pass</step>
          <step>3. Measure quality metrics improvement</step>
          <step>4. Confirm no new functionality added</step>
          <step>5. Store REFACTOR phase evidence</step>
          <output>evidence/tdd/{task_id}/refactor-evidence.json</output>
        </phase>
      </tdd_evidence_workflow>
      
      <security_verification_workflow>
        <phase name="THREAT_MODELING">
          <step>1. Analyze component architecture and data flows</step>
          <step>2. Apply STRIDE methodology for threat identification</step>
          <step>3. Calculate risk ratings and prioritization</step>
          <step>4. Define required security controls</step>
          <step>5. Store threat model evidence</step>
          <output>evidence/security/{task_id}/threat-model.json</output>
        </phase>
        
        <phase name="VULNERABILITY_SCANNING">
          <step>1. Execute SAST scan with security rules</step>
          <step>2. Run dependency vulnerability check</step>
          <step>3. Perform secret detection scan</step>
          <step>4. Analyze configuration security</step>
          <step>5. Store scan evidence</step>
          <output>evidence/security/{task_id}/vulnerability-scan.json</output>
        </phase>
        
        <phase name="MITIGATION_VERIFICATION">
          <step>1. Verify security controls implementation</step>
          <step>2. Test authentication and authorization</step>
          <step>3. Validate data protection measures</step>
          <step>4. Confirm audit logging functionality</step>
          <step>5. Store verification evidence</step>
          <output>evidence/security/{task_id}/mitigation-verification.json</output>
        </phase>
      </security_verification_workflow>
      
      <performance_verification_workflow>
        <phase name="BASELINE_ESTABLISHMENT">
          <step>1. Measure current performance metrics</step>
          <step>2. Establish performance baselines</step>
          <step>3. Define performance targets</step>
          <step>4. Configure monitoring infrastructure</step>
          <step>5. Store baseline evidence</step>
          <output>evidence/performance/{task_id}/baseline.json</output>
        </phase>
        
        <phase name="BENCHMARK_TESTING">
          <step>1. Execute load testing scenarios</step>
          <step>2. Measure response time distributions</step>
          <step>3. Monitor resource utilization</step>
          <step>4. Test failure modes and recovery</step>
          <step>5. Store benchmark evidence</step>
          <output>evidence/performance/{task_id}/benchmarks.json</output>
        </phase>
        
        <phase name="REGRESSION_ANALYSIS">
          <step>1. Compare against historical baselines</step>
          <step>2. Identify performance regressions</step>
          <step>3. Analyze root causes of degradation</step>
          <step>4. Validate optimization effectiveness</step>
          <step>5. Store analysis evidence</step>
          <output>evidence/performance/{task_id}/regression-analysis.json</output>
        </phase>
      </performance_verification_workflow>
      
    </verification_workflows>
    
    <reporting_engine>
      
      <automated_reports>
        <report name="GATE_EXECUTION_SUMMARY">
          <format>JSON + HTML dashboard</format>
          <content>
            <section>Gate execution results with pass/fail status</section>
            <section>Evidence artifacts collected with verification</section>
            <section>Performance metrics and quality scores</section>
            <section>Action items for failed gates</section>
            <section>Compliance certificate or blocking reasons</section>
          </content>
          <frequency>Per execution + scheduled daily</frequency>
        </report>
        
        <report name="QUALITY_TREND_ANALYSIS">
          <format>Interactive dashboard</format>
          <content>
            <section>Quality metrics trends over time</section>
            <section>Gate failure patterns and root causes</section>
            <section>Performance regression analysis</section>
            <section>Security posture evolution</section>
            <section>Predictive quality forecasting</section>
          </content>
          <frequency>Weekly with monthly deep-dive</frequency>
        </report>
        
        <report name="COMPLIANCE_AUDIT_TRAIL">
          <format>Immutable audit log</format>
          <content>
            <section>All gate executions with timestamps</section>
            <section>Evidence collection and verification</section>
            <section>Override events with justifications</section>
            <section>Quality improvement actions taken</section>
            <section>Regulatory compliance status</section>
          </content>
          <frequency>Continuous with quarterly certification</frequency>
        </report>
      </automated_reports>
      
      <real_time_notifications>
        <notification trigger="gate_failure">
          <recipient>Development team</recipient>
          <content>Failed gate details, evidence links, remediation steps</content>
          <urgency>immediate</urgency>
        </notification>
        
        <notification trigger="quality_degradation">
          <recipient>Technical leadership</recipient>
          <content>Quality trend analysis, root cause, recommended actions</content>
          <urgency>daily_digest</urgency>
        </notification>
        
        <notification trigger="compliance_risk">
          <recipient>Compliance team</recipient>
          <content>Audit trail gaps, override frequency, risk assessment</content>
          <urgency>weekly_report</urgency>
        </notification>
      </real_time_notifications>
      
    </reporting_engine>
    
  </implementation>
  
  <integration_points>
    <depends_on>
      quality/tdd-verification.md for TDD evidence collection
      quality/security-gate-verification.md for security verification
      quality/performance-gates.md for performance benchmarking
      quality/production-standards.md for quality standards enforcement
      patterns/enforcement-verification.md for checkpoint templates
    </depends_on>
    <provides_to>
      development/task-management.md for task-level quality gates
      planning/feature-workflow.md for feature-level quality gates
      patterns/multi-agent.md for swarm-level quality gates
      All commands for unified quality gate enforcement
    </provides_to>
  </integration_points>
  
</module>
```

────────────────────────────────────────────────────────────────────────────────

## Gate Verification Commands

```bash
#!/bin/bash
# Quality Gate Verification Engine

# Main gate verification command
verify_quality_gates() {
    local task_id=$1
    local gate_profile=${2:-"standard"}  # minimal, standard, enterprise
    local blocking_mode=${3:-"strict"}   # strict, advisory
    
    echo "🚦 Starting Quality Gate Verification"
    echo "Task: $task_id | Profile: $gate_profile | Mode: $blocking_mode"
    
    local evidence_dir="evidence/quality-gates/$task_id"
    mkdir -p "$evidence_dir"
    
    # Initialize gate execution log
    local execution_log="$evidence_dir/gate-execution-$(date +%Y%m%d-%H%M%S).json"
    cat > "$execution_log" << EOF
{
  "task_id": "$task_id",
  "execution_start": "$(date -u +%Y-%m-%dT%H:%M:%S.000Z)",
  "gate_profile": "$gate_profile",
  "blocking_mode": "$blocking_mode",
  "gates": [],
  "overall_status": "RUNNING"
}
EOF
    
    local overall_status="PASS"
    local gate_results=()
    
    # Execute TDD Compliance Gate
    if execute_tdd_gate "$task_id" "$evidence_dir"; then
        gate_results+=('{"gate": "TDD_COMPLIANCE", "status": "PASS", "blocking": true}')
        echo "✅ TDD Compliance: PASSED"
    else
        gate_results+=('{"gate": "TDD_COMPLIANCE", "status": "FAIL", "blocking": true}')
        echo "❌ TDD Compliance: FAILED"
        overall_status="FAIL"
        if [[ "$blocking_mode" == "strict" ]]; then
            echo "🚫 BLOCKING: TDD compliance required"
            return 1
        fi
    fi
    
    # Execute Security Verification Gate
    if execute_security_gate "$task_id" "$evidence_dir"; then
        gate_results+=('{"gate": "SECURITY_VERIFICATION", "status": "PASS", "blocking": true}')
        echo "✅ Security Verification: PASSED"
    else
        gate_results+=('{"gate": "SECURITY_VERIFICATION", "status": "FAIL", "blocking": true}')
        echo "❌ Security Verification: FAILED"
        overall_status="FAIL"
        if [[ "$blocking_mode" == "strict" ]]; then
            echo "🚫 BLOCKING: Security verification required"
            return 1
        fi
    fi
    
    # Execute Performance Benchmarks Gate
    if execute_performance_gate "$task_id" "$evidence_dir"; then
        gate_results+=('{"gate": "PERFORMANCE_BENCHMARKS", "status": "PASS", "blocking": true}')
        echo "✅ Performance Benchmarks: PASSED"
    else
        gate_results+=('{"gate": "PERFORMANCE_BENCHMARKS", "status": "FAIL", "blocking": true}')
        echo "❌ Performance Benchmarks: FAILED"
        overall_status="FAIL"
        if [[ "$blocking_mode" == "strict" ]]; then
            echo "🚫 BLOCKING: Performance benchmarks required"
            return 1
        fi
    fi
    
    # Execute Code Quality Gate
    if execute_code_quality_gate "$task_id" "$evidence_dir"; then
        gate_results+=('{"gate": "CODE_QUALITY", "status": "PASS", "blocking": true}')
        echo "✅ Code Quality: PASSED"
    else
        gate_results+=('{"gate": "CODE_QUALITY", "status": "FAIL", "blocking": true}')
        echo "❌ Code Quality: FAILED"
        overall_status="FAIL"
        if [[ "$blocking_mode" == "strict" ]]; then
            echo "🚫 BLOCKING: Code quality standards required"
            return 1
        fi
    fi
    
    # Finalize execution log
    local gate_results_json=$(printf '%s\n' "${gate_results[@]}" | jq -s .)
    jq --argjson gates "$gate_results_json" \
       --arg status "$overall_status" \
       --arg end_time "$(date -u +%Y-%m-%dT%H:%M:%S.000Z)" \
       '.gates = $gates | .overall_status = $status | .execution_end = $end_time' \
       "$execution_log" > "${execution_log}.tmp" && mv "${execution_log}.tmp" "$execution_log"
    
    # Generate final report
    generate_gate_report "$task_id" "$evidence_dir" "$overall_status"
    
    if [[ "$overall_status" == "PASS" ]]; then
        echo "🎉 All quality gates PASSED"
        echo "📊 Evidence stored in: $evidence_dir"
        echo "📋 Report: $evidence_dir/quality-gate-report.html"
        return 0
    else
        echo "🚨 Quality gates FAILED"
        echo "📊 Evidence stored in: $evidence_dir"
        echo "📋 Report: $evidence_dir/quality-gate-report.html"
        return 1
    fi
}

# TDD Gate Execution
execute_tdd_gate() {
    local task_id=$1
    local evidence_dir=$2
    
    echo "🔍 Executing TDD Compliance Gate..."
    
    # Verify TDD evidence exists
    local tdd_evidence="evidence/tdd/$task_id"
    if [[ ! -d "$tdd_evidence" ]]; then
        echo "❌ No TDD evidence found"
        return 1
    fi
    
    # Check for RED phase evidence
    if [[ ! -f "$tdd_evidence/red-phase-evidence.json" ]]; then
        echo "❌ Missing RED phase evidence"
        return 1
    fi
    
    # Check for GREEN phase evidence
    if [[ ! -f "$tdd_evidence/green-phase-evidence.json" ]]; then
        echo "❌ Missing GREEN phase evidence"
        return 1
    fi
    
    # Verify test coverage
    local coverage_threshold=90
    local coverage_file="$tdd_evidence/coverage-report.json"
    if [[ -f "$coverage_file" ]]; then
        local coverage=$(jq -r '.totals.percent_covered // 0' "$coverage_file")
        if (( $(echo "$coverage < $coverage_threshold" | bc -l) )); then
            echo "❌ Test coverage $coverage% below threshold $coverage_threshold%"
            return 1
        fi
    else
        echo "❌ Missing coverage report"
        return 1
    fi
    
    # Copy evidence to gate evidence directory
    cp -r "$tdd_evidence" "$evidence_dir/tdd-evidence"
    return 0
}

# Security Gate Execution
execute_security_gate() {
    local task_id=$1
    local evidence_dir=$2
    
    echo "🔒 Executing Security Verification Gate..."
    
    # Run security verification
    python -m quality.security_gate_verifier \
        --task-id "$task_id" \
        --evidence-dir "$evidence_dir/security-evidence" \
        --strict-mode
    
    return $?
}

# Performance Gate Execution
execute_performance_gate() {
    local task_id=$1
    local evidence_dir=$2
    
    echo "⚡ Executing Performance Benchmarks Gate..."
    
    # Run performance verification
    python -m quality.performance_gate_verifier \
        --task-id "$task_id" \
        --evidence-dir "$evidence_dir/performance-evidence" \
        --p95-threshold 200
    
    return $?
}

# Code Quality Gate Execution
execute_code_quality_gate() {
    local task_id=$1
    local evidence_dir=$2
    
    echo "📏 Executing Code Quality Gate..."
    
    # Run code quality checks
    python -m quality.code_quality_verifier \
        --task-id "$task_id" \
        --evidence-dir "$evidence_dir/code-quality-evidence" \
        --complexity-threshold 10 \
        --duplication-threshold 3
    
    return $?
}

# Generate comprehensive gate report
generate_gate_report() {
    local task_id=$1
    local evidence_dir=$2
    local overall_status=$3
    
    python -m quality.gate_report_generator \
        --task-id "$task_id" \
        --evidence-dir "$evidence_dir" \
        --overall-status "$overall_status" \
        --output "$evidence_dir/quality-gate-report.html"
}

# Pre-commit hook integration
pre_commit_quality_gates() {
    local task_id="pre-commit-$(date +%Y%m%d-%H%M%S)"
    
    echo "🚦 Running pre-commit quality gates..."
    
    if verify_quality_gates "$task_id" "minimal" "strict"; then
        echo "✅ Pre-commit quality gates passed"
        return 0
    else
        echo "❌ Pre-commit quality gates failed"
        echo "🚫 COMMIT BLOCKED"
        return 1
    fi
}

# Export functions for use in other scripts
export -f verify_quality_gates
export -f execute_tdd_gate
export -f execute_security_gate
export -f execute_performance_gate
export -f execute_code_quality_gate
export -f generate_gate_report
export -f pre_commit_quality_gates
```

────────────────────────────────────────────────────────────────────────────────

## Evidence Archive Structure

```
evidence/
├── quality-gates/
│   └── {task_id}/
│       ├── gate-execution-{timestamp}.json
│       ├── quality-gate-report.html
│       ├── tdd-evidence/
│       │   ├── red-phase-evidence.json
│       │   ├── green-phase-evidence.json
│       │   ├── refactor-evidence.json
│       │   └── coverage-report.json
│       ├── security-evidence/
│       │   ├── threat-model.json
│       │   ├── vulnerability-scan.json
│       │   └── mitigation-verification.json
│       ├── performance-evidence/
│       │   ├── baseline.json
│       │   ├── benchmarks.json
│       │   └── regression-analysis.json
│       └── code-quality-evidence/
│           ├── lint-results.json
│           ├── complexity-analysis.json
│           └── technical-debt.json
```

────────────────────────────────────────────────────────────────────────────────

## Quality Gate Dashboard Template

```html
<!DOCTYPE html>
<html>
<head>
    <title>Quality Gates Report - {{task_id}}</title>
    <style>
        .gate-pass { color: green; }
        .gate-fail { color: red; }
        .gate-warning { color: orange; }
        .evidence-link { margin-left: 20px; }
    </style>
</head>
<body>
    <h1>Quality Gates Report</h1>
    <p><strong>Task ID:</strong> {{task_id}}</p>
    <p><strong>Execution Time:</strong> {{execution_time}}</p>
    <p><strong>Overall Status:</strong> <span class="gate-{{overall_status}}">{{overall_status}}</span></p>
    
    <h2>Gate Results</h2>
    {{#each gates}}
    <div class="gate-result">
        <h3 class="gate-{{status}}">{{gate}}: {{status}}</h3>
        <div class="evidence-link">
            <a href="{{evidence_path}}">View Evidence</a>
        </div>
        {{#if blocking}}
        <p><em>This gate is blocking and must pass for progression.</em></p>
        {{/if}}
    </div>
    {{/each}}
    
    <h2>Quality Metrics</h2>
    <ul>
        <li>Test Coverage: {{coverage}}%</li>
        <li>Performance p95: {{performance_p95}}ms</li>
        <li>Security Score: {{security_score}}/100</li>
        <li>Code Quality Score: {{code_quality_score}}/100</li>
    </ul>
    
    <h2>Evidence Archive</h2>
    <p>All evidence artifacts are preserved for audit purposes:</p>
    <ul>
        <li><a href="tdd-evidence/">TDD Evidence</a></li>
        <li><a href="security-evidence/">Security Evidence</a></li>
        <li><a href="performance-evidence/">Performance Evidence</a></li>
        <li><a href="code-quality-evidence/">Code Quality Evidence</a></li>
    </ul>
    
    <footer>
        <p>Generated by Quality Gate Verification Module v1.0.0</p>
        <p>Framework: Claude Code Modular Agents</p>
    </footer>
</body>
</html>
```