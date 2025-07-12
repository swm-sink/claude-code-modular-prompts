| version | last_updated | status |
|---------|--------------|--------|
| 1.0.0   | 2025-07-08   | stable |

# TDD Enforcement Module

────────────────────────────────────────────────────────────────────────────────


────────────────────────────────────────────────────────────────────────────────

```xml
<module name="tdd_enforcement" category="quality">
  
  <purpose>
    Non-bypassable TDD enforcement with evidence requirements for RED-GREEN-REFACTOR cycle. Blocks all progression without proof of test-first development.
  </purpose>
  
  <thinking_pattern enforcement="MANDATORY">
    <step>1. Monitor file system for code changes</step>
    <step>2. Detect test creation vs implementation timing</step>
    <step>3. Verify RED phase: test exists and FAILS</step>
    <step>4. Block implementation until RED evidence collected</step>
    <step>5. Verify GREEN phase: minimal code makes test PASS</step>
    <step>6. Monitor REFACTOR phase: quality improvements without functionality changes</step>
    <step>7. Enforce 90%+ coverage with meaningful assertions</step>
    <step>8. Generate non-repudiable evidence trail</step>
  </thinking_pattern>
  
  <trigger_conditions>
    <condition type="automatic">File modification detection, pre-commit hooks</condition>
    <condition type="explicit">TDD compliance verification requests</condition>
  </trigger_conditions>
  
  <implementation>
    
    <tdd_enforcement_engine>
      
      <phase_detection>
        <red_phase_detector>
          <trigger>Test file creation or modification</trigger>
          <requirements>
            <requirement>Test file must exist BEFORE corresponding implementation</requirement>
            <requirement>Test must fail when executed (proper RED state)</requirement>
            <requirement>Failure must be for expected reason (not syntax error)</requirement>
            <requirement>No implementation code present in target module</requirement>
          </requirements>
          <blocking_conditions>
            <condition>Implementation file exists without prior test</condition>
            <condition>Test passes immediately (no RED phase)</condition>
            <condition>Test fails for wrong reasons (syntax, imports)</condition>
          </blocking_conditions>
          <evidence_collection>
            <artifact>test-creation-timestamp.json</artifact>
            <artifact>test-failure-output.json</artifact>
            <artifact>implementation-absence-proof.json</artifact>
            <artifact>failure-reason-analysis.json</artifact>
          </evidence_collection>
        </red_phase_detector>
        
        <green_phase_detector>
          <trigger>Implementation file creation or modification after RED</trigger>
          <requirements>
            <requirement>RED phase evidence must exist and be valid</requirement>
            <requirement>Implementation makes previously failing test pass</requirement>
            <requirement>Implementation is minimal (no gold-plating)</requirement>
            <requirement>No additional functionality beyond test requirements</requirement>
            <requirement>All tests still pass (no regressions)</requirement>
          </requirements>
          <blocking_conditions>
            <condition>No valid RED phase evidence</condition>
            <condition>Implementation too complex for test requirements</condition>
            <condition>New functionality not covered by tests</condition>
            <condition>Previous tests broken by implementation</condition>
          </blocking_conditions>
          <evidence_collection>
            <artifact>test-success-output.json</artifact>
            <artifact>implementation-minimality-analysis.json</artifact>
            <artifact>regression-test-results.json</artifact>
            <artifact>code-coverage-delta.json</artifact>
          </evidence_collection>
        </green_phase_detector>
        
        <refactor_phase_detector>
          <trigger>Code modification without test changes after GREEN</trigger>
          <requirements>
            <requirement>GREEN phase evidence must exist and be valid</requirement>
            <requirement>All tests continue to pass</requirement>
            <requirement>Code quality metrics improve</requirement>
            <requirement>No new functionality added</requirement>
            <requirement>API contracts remain unchanged</requirement>
          </requirements>
          <blocking_conditions>
            <condition>Tests start failing during refactor</condition>
            <condition>Code quality metrics degrade</condition>
            <condition>New functionality detected</condition>
            <condition>API breaking changes introduced</condition>
          </blocking_conditions>
          <evidence_collection>
            <artifact>refactor-test-stability.json</artifact>
            <artifact>quality-metrics-improvement.json</artifact>
            <artifact>api-contract-preservation.json</artifact>
            <artifact>functionality-unchanged-proof.json</artifact>
          </evidence_collection>
        </refactor_phase_detector>
      </phase_detection>
      
      <enforcement_mechanisms>
        <file_system_watcher>
          <monitor_patterns>
            <pattern>**/*.py</pattern>
            <pattern>**/*.js</pattern>
            <pattern>**/*.ts</pattern>
            <pattern>**/*.java</pattern>
            <pattern>**/*.go</pattern>
            <pattern>**/*.rs</pattern>
          </monitor_patterns>
          <exclusions>
            <exclude>**/node_modules/**</exclude>
            <exclude>**/venv/**</exclude>
            <exclude>**/target/**</exclude>
            <exclude>**/__pycache__/**</exclude>
          </exclusions>
          <event_handlers>
            <on_create>validate_tdd_sequence</on_create>
            <on_modify>validate_phase_compliance</on_modify>
            <on_delete>update_evidence_archive</on_delete>
          </event_handlers>
        </file_system_watcher>
        
        <git_hook_integration>
          <pre_commit_hook>
            <validation>Verify TDD compliance for all staged changes</validation>
            <blocking>Prevent commit if evidence incomplete</blocking>
            <reporting>Generate compliance report for review</reporting>
          </pre_commit_hook>
          
          <pre_push_hook>
            <validation>Full TDD audit trail verification</validation>
            <blocking>Prevent push if any violations detected</blocking>
            <archival>Archive evidence for remote tracking</archival>
          </pre_push_hook>
          
          <pre_merge_hook>
            <validation>Cross-reference all TDD evidence</validation>
            <blocking>Prevent merge without complete evidence</blocking>
            <certification>Generate TDD compliance certificate</certification>
          </pre_merge_hook>
        </git_hook_integration>
        
        <ide_integration>
          <real_time_monitoring>
            <feature>Live TDD phase detection and feedback</feature>
            <feature>Visual indicators for compliance status</feature>
            <feature>Blocking warnings for TDD violations</feature>
            <feature>Evidence collection automation</feature>
          </real_time_monitoring>
          
          <editor_extensions>
            <vscode>TDD Enforcer extension with live feedback</vscode>
            <intellij>TDD compliance plugin with blocking</intellij>
            <vim>TDD status line integration</vim>
            <emacs>TDD mode with enforcement hooks</emacs>
          </editor_extensions>
        </ide_integration>
      </enforcement_mechanisms>
      
      <evidence_verification>
        <authenticity_checks>
          <timestamp_verification>
            <requirement>All evidence timestamps must be sequential</requirement>
            <requirement>No backdated evidence allowed</requirement>
            <requirement>Timestamp source must be trusted</requirement>
          </timestamp_verification>
          
          <integrity_verification>
            <requirement>Evidence files signed with cryptographic hashes</requirement>
            <requirement>Tampering detection through checksum validation</requirement>
            <requirement>Immutable evidence storage with audit trail</requirement>
          </integrity_verification>
          
          <logical_consistency>
            <requirement>Evidence must form coherent TDD narrative</requirement>
            <requirement>Phase transitions must be logical and complete</requirement>
            <requirement>No gaps or inconsistencies in evidence chain</requirement>
          </logical_consistency>
        </authenticity_checks>
        
        <coverage_requirements>
          <minimum_coverage>90% line coverage required</minimum_coverage>
          <meaningful_assertions>
            <requirement>Tests must contain behavioral assertions</requirement>
            <requirement>No empty or trivial test cases</requirement>
            <requirement>Edge cases and error conditions covered</requirement>
          </meaningful_assertions>
          
          <test_quality_metrics>
            <metric name="assertion_density" target=">2_per_test">
              <description>Average assertions per test method</description>
              <measurement>Total assertions / Test methods</measurement>
            </metric>
            
            <metric name="cyclomatic_coverage" target="100%">
              <description>All code paths exercised by tests</description>
              <measurement>Covered paths / Total paths</measurement>
            </metric>
            
            <metric name="mutation_test_score" target=">80%">
              <description>Tests detect injected code mutations</description>
              <measurement>Killed mutations / Total mutations</measurement>
            </metric>
          </test_quality_metrics>
        </coverage_requirements>
      </evidence_verification>
      
    </tdd_enforcement_engine>
    
    <violation_detection_and_response>
      
      <violation_types>
        <violation name="IMPLEMENTATION_FIRST" severity="CRITICAL" blocking="true">
          <description>Implementation code created before corresponding test</description>
          <detection>File creation timestamps, git history analysis</detection>
          <response>Block commit, require test creation, move implementation to staging</response>
          <remediation>Create failing test, move implementation, re-run TDD cycle</remediation>
        </violation>
        
        <violation name="TEST_NOT_FAILING" severity="CRITICAL" blocking="true">
          <description>Test passes immediately without implementation (no RED phase)</description>
          <detection>Test execution results, assertion analysis</detection>
          <response>Block progression, require proper failing test</response>
          <remediation>Revise test to fail appropriately, document expected failure</remediation>
        </violation>
        
        <violation name="EXCESSIVE_IMPLEMENTATION" severity="HIGH" blocking="true">
          <description>Implementation includes functionality beyond test requirements</description>
          <detection>Code complexity analysis, functionality mapping</detection>
          <response>Block commit, require implementation reduction</response>
          <remediation>Remove excess functionality, create additional tests if needed</remediation>
        </violation>
        
        <violation name="INSUFFICIENT_COVERAGE" severity="HIGH" blocking="true">
          <description>Test coverage below 90% threshold</description>
          <detection>Coverage analysis, gap identification</detection>
          <response>Block merge, require additional tests</response>
          <remediation>Add tests for uncovered code paths, verify meaningful assertions</remediation>
        </violation>
        
        <violation name="REFACTOR_REGRESSION" severity="HIGH" blocking="true">
          <description>Tests fail during refactoring phase</description>
          <detection>Test execution monitoring, failure pattern analysis</detection>
          <response>Block progression, require regression fix</response>
          <remediation>Fix refactoring to maintain test compatibility</remediation>
        </violation>
        
        <violation name="EVIDENCE_TAMPERING" severity="CRITICAL" blocking="true">
          <description>Evidence files modified or corrupted</description>
          <detection>Checksum validation, integrity monitoring</detection>
          <response>Block all operations, require evidence regeneration</response>
          <remediation>Re-execute TDD cycle with fresh evidence collection</remediation>
        </violation>
      </violation_types>
      
      <escalation_procedures>
        <level_1_automatic>
          <condition>Standard TDD violations detected</condition>
          <response>Block operation, display guidance, suggest remediation</response>
          <timeout>30 minutes for developer self-correction</timeout>
        </level_1_automatic>
        
        <level_2_team_lead>
          <condition>Repeated violations or override attempts</condition>
          <response>Notify team lead, require manual review, document justification</response>
          <timeout>2 hours for team lead intervention</timeout>
        </level_2_team_lead>
        
        <level_3_architecture>
          <condition>Multiple override attempts or systematic violations</condition>
          <response>Escalate to architecture team, process review, training required</response>
          <timeout>24 hours for architecture review</timeout>
        </level_3_architecture>
        
        <level_4_compliance>
          <condition>Evidence tampering or process circumvention attempts</condition>
          <response>Compliance audit, security review, disciplinary action</response>
          <timeout>Indefinite pending investigation</timeout>
        </level_4_compliance>
      </escalation_procedures>
      
    </violation_detection_and_response>
    
    <bypass_prevention>
      
      <technical_controls>
        <git_hooks_enforcement>
          <protection>Hooks cannot be skipped without authentication</protection>
          <monitoring>All hook bypass attempts logged and alerted</monitoring>
          <fallback>Server-side hooks as ultimate enforcement</fallback>
        </git_hooks_enforcement>
        
        <file_system_protection>
          <protection>Evidence directory write-protected after creation</protection>
          <monitoring>File system events monitored for tampering</monitoring>
          <backup>Evidence automatically backed up to immutable storage</backup>
        </file_system_protection>
        
        <network_enforcement>
          <protection>Push to main branch requires TDD evidence validation</protection>
          <monitoring>All push attempts logged with evidence verification</monitoring>
          <fallback>Branch protection rules with status checks</fallback>
        </network_enforcement>
      </technical_controls>
      
      <process_controls>
        <code_review_requirements>
          <requirement>All code changes require TDD evidence review</requirement>
          <requirement>Reviewers must verify evidence authenticity</requirement>
          <requirement>Evidence gaps must be addressed before approval</requirement>
        </code_review_requirements>
        
        <deployment_gates>
          <gate>TDD compliance certificate required for staging deployment</gate>
          <gate>Full evidence audit required for production deployment</gate>
          <gate>Evidence retention verified for compliance requirements</gate>
        </deployment_gates>
        
        <audit_trails>
          <logging>All TDD enforcement actions logged immutably</logging>
          <reporting>Regular compliance reports generated automatically</reporting>
          <monitoring>Anomaly detection for unusual patterns</monitoring>
        </audit_trails>
      </process_controls>
      
    </bypass_prevention>
    
  </implementation>
  
  <integration_points>
    <depends_on>
      quality/tdd-verification.md for evidence collection patterns
      quality/gate-verification.md for quality gate integration
      patterns/enforcement-verification.md for checkpoint templates
      development/task-management.md for development workflow integration
    </depends_on>
    <provides_to>
      development/task-management.md for TDD-enforced development
      planning/feature-workflow.md for feature-level TDD compliance
      patterns/multi-agent.md for swarm TDD coordination
      All commands for mandatory TDD enforcement
    </provides_to>
  </integration_points>
  
</module>
```

────────────────────────────────────────────────────────────────────────────────

## TDD Enforcement Commands

```bash
#!/bin/bash
# TDD Enforcement Engine

# Global TDD enforcement state
TDD_ENFORCEMENT_ENABLED=true
TDD_EVIDENCE_DIR="evidence/tdd"
TDD_STATE_FILE=".tdd_state.json"

# Initialize TDD enforcement for a task
init_tdd_enforcement() {
    local task_id=$1
    local working_dir=${2:-.}
    
    echo "🔒 Initializing TDD Enforcement for task: $task_id"
    
    # Create evidence directory
    local evidence_dir="$TDD_EVIDENCE_DIR/$task_id"
    mkdir -p "$evidence_dir"
    
    # Initialize TDD state tracking
    cat > "$working_dir/$TDD_STATE_FILE" << EOF
{
  "task_id": "$task_id",
  "enforcement_enabled": true,
  "current_phase": "READY",
  "evidence_dir": "$evidence_dir",
  "phase_history": [],
  "violations": [],
  "started_at": "$(date -u +%Y-%m-%dT%H:%M:%S.000Z)"
}
EOF
    
    # Set up file system watcher
    setup_tdd_watcher "$working_dir" "$task_id"
    
    # Install git hooks
    install_tdd_git_hooks "$working_dir"
    
    echo "✅ TDD Enforcement initialized"
    echo "📁 Evidence directory: $evidence_dir"
    echo "⚡ File system monitoring active"
    echo "🔗 Git hooks installed"
}

# File system watcher for TDD compliance
setup_tdd_watcher() {
    local watch_dir=$1
    local task_id=$2
    
    # Use inotifywait or fswatch depending on platform
    if command -v inotifywait >/dev/null 2>&1; then
        # Linux
        inotifywait -m -r --format '%w%f %e %T' --timefmt '%Y-%m-%d %H:%M:%S' \
            -e create,modify,moved_to \
            --exclude '__pycache__|\.pyc$|node_modules|\.git' \
            "$watch_dir" | while read file event time; do
                handle_file_change "$file" "$event" "$time" "$task_id"
            done &
    elif command -v fswatch >/dev/null 2>&1; then
        # macOS
        fswatch -0 -r --event Created --event Updated --event MovedTo \
            --exclude '__pycache__|\.pyc$|node_modules|\.git' \
            "$watch_dir" | while IFS= read -r -d '' file; do
                handle_file_change "$file" "modify" "$(date '+%Y-%m-%d %H:%M:%S')" "$task_id"
            done &
    else
        echo "⚠️  No file watcher available, using polling mode"
        # Fallback to polling
        while true; do
            check_tdd_compliance_polling "$watch_dir" "$task_id"
            sleep 5
        done &
    fi
    
    # Store watcher PID for cleanup
    echo $! > "$watch_dir/.tdd_watcher.pid"
}

# Handle file system changes
handle_file_change() {
    local file=$1
    local event=$2
    local timestamp=$3
    local task_id=$4
    
    # Skip non-source files
    if [[ ! "$file" =~ \.(py|js|ts|java|go|rs)$ ]]; then
        return
    fi
    
    # Skip test files and generated files
    if [[ "$file" =~ test_|_test\.|\.test\.|spec\.|generated ]]; then
        handle_test_file_change "$file" "$event" "$timestamp" "$task_id"
        return
    fi
    
    # Handle implementation file change
    handle_implementation_file_change "$file" "$event" "$timestamp" "$task_id"
}

# Handle test file changes
handle_test_file_change() {
    local test_file=$1
    local event=$2
    local timestamp=$3
    local task_id=$4
    
    echo "🧪 Test file changed: $test_file"
    
    # Update TDD state
    update_tdd_state "$task_id" "test_file_changed" "$test_file" "$timestamp"
    
    # Validate RED phase
    if ! validate_red_phase "$test_file" "$task_id"; then
        block_progression "RED phase validation failed for $test_file" "$task_id"
        return 1
    fi
    
    # Collect RED phase evidence
    collect_red_phase_evidence "$test_file" "$task_id" "$timestamp"
    
    echo "✅ RED phase validated for $test_file"
}

# Handle implementation file changes
handle_implementation_file_change() {
    local impl_file=$1
    local event=$2
    local timestamp=$3
    local task_id=$4
    
    echo "⚙️  Implementation file changed: $impl_file"
    
    # Check if corresponding test exists and has RED evidence
    local test_file=$(find_corresponding_test "$impl_file")
    if [[ -z "$test_file" ]]; then
        block_progression "No corresponding test found for $impl_file" "$task_id"
        return 1
    fi
    
    # Verify RED phase evidence exists
    local evidence_dir="$TDD_EVIDENCE_DIR/$task_id"
    if [[ ! -f "$evidence_dir/red-phase-evidence.json" ]]; then
        block_progression "No RED phase evidence found for $impl_file" "$task_id"
        return 1
    fi
    
    # Update TDD state
    update_tdd_state "$task_id" "implementation_file_changed" "$impl_file" "$timestamp"
    
    # Validate GREEN phase
    if ! validate_green_phase "$impl_file" "$test_file" "$task_id"; then
        block_progression "GREEN phase validation failed for $impl_file" "$task_id"
        return 1
    fi
    
    # Collect GREEN phase evidence
    collect_green_phase_evidence "$impl_file" "$test_file" "$task_id" "$timestamp"
    
    echo "✅ GREEN phase validated for $impl_file"
}

# Validate RED phase requirements
validate_red_phase() {
    local test_file=$1
    local task_id=$2
    
    echo "🔍 Validating RED phase for $test_file"
    
    # Run the test and capture output
    local test_output_file="$TDD_EVIDENCE_DIR/$task_id/test-output-$(date +%s).txt"
    
    # Determine test runner based on file type
    local test_command=""
    case "$test_file" in
        *.py)
            test_command="pytest $test_file -v"
            ;;
        *.js|*.ts)
            test_command="npm test -- $test_file"
            ;;
        *.java)
            test_command="mvn test -Dtest=$(basename ${test_file%.java})"
            ;;
        *.go)
            test_command="go test $test_file -v"
            ;;
        *)
            echo "❌ Unsupported test file type: $test_file"
            return 1
            ;;
    esac
    
    # Execute test and capture result
    if $test_command > "$test_output_file" 2>&1; then
        echo "❌ Test passed - RED phase violation (test should fail first)"
        record_violation "$task_id" "TEST_NOT_FAILING" "$test_file" "Test passed without implementation"
        return 1
    fi
    
    # Verify test failed for the right reason (not syntax error)
    if grep -q "SyntaxError\|ImportError\|NameError" "$test_output_file"; then
        echo "❌ Test failed due to syntax/import error - not proper RED phase"
        record_violation "$task_id" "INVALID_TEST_FAILURE" "$test_file" "Test failed due to syntax error"
        return 1
    fi
    
    # Check that implementation doesn't exist yet
    local impl_file=$(find_corresponding_implementation "$test_file")
    if [[ -n "$impl_file" && -f "$impl_file" ]]; then
        # Check if implementation has actual code (not just stubs)
        if has_substantial_implementation "$impl_file"; then
            echo "❌ Implementation already exists - TDD violation"
            record_violation "$task_id" "IMPLEMENTATION_FIRST" "$impl_file" "Implementation exists before test"
            return 1
        fi
    fi
    
    echo "✅ RED phase validated: test fails appropriately"
    return 0
}

# Validate GREEN phase requirements
validate_green_phase() {
    local impl_file=$1
    local test_file=$2
    local task_id=$3
    
    echo "🔍 Validating GREEN phase for $impl_file"
    
    # Run tests and verify they pass
    local test_output_file="$TDD_EVIDENCE_DIR/$task_id/green-test-output-$(date +%s).txt"
    
    # Determine test runner
    local test_command=""
    case "$test_file" in
        *.py)
            test_command="pytest $test_file -v"
            ;;
        *.js|*.ts)
            test_command="npm test -- $test_file"
            ;;
        *.java)
            test_command="mvn test -Dtest=$(basename ${test_file%.java})"
            ;;
        *.go)
            test_command="go test $test_file -v"
            ;;
    esac
    
    # Execute test
    if ! $test_command > "$test_output_file" 2>&1; then
        echo "❌ Tests failed - GREEN phase violation"
        record_violation "$task_id" "GREEN_PHASE_FAILURE" "$test_file" "Tests still failing after implementation"
        return 1
    fi
    
    # Verify implementation is minimal
    if ! verify_minimal_implementation "$impl_file" "$test_file"; then
        echo "❌ Implementation is excessive - violates minimal implementation principle"
        record_violation "$task_id" "EXCESSIVE_IMPLEMENTATION" "$impl_file" "Implementation beyond test requirements"
        return 1
    fi
    
    # Run full test suite to check for regressions
    if ! run_full_test_suite; then
        echo "❌ Regression detected - existing tests now failing"
        record_violation "$task_id" "REGRESSION_INTRODUCED" "$impl_file" "Implementation broke existing tests"
        return 1
    fi
    
    echo "✅ GREEN phase validated: tests pass with minimal implementation"
    return 0
}

# Block progression when TDD violations detected
block_progression() {
    local reason=$1
    local task_id=$2
    
    echo ""
    echo "🚫 ========================================"
    echo "🚫 TDD VIOLATION DETECTED"
    echo "🚫 ========================================"
    echo "🚫 Reason: $reason"
    echo "🚫 Task: $task_id"
    echo "🚫 Time: $(date)"
    echo "🚫 ========================================"
    echo "🚫 PROGRESSION BLOCKED"
    echo "🚫 ========================================"
    echo ""
    
    # Update TDD state
    update_tdd_state "$task_id" "violation_detected" "$reason" "$(date -u +%Y-%m-%dT%H:%M:%S.000Z)"
    
    # Send notifications
    notify_tdd_violation "$task_id" "$reason"
    
    # Block git operations
    create_git_block "$task_id" "$reason"
    
    # Exit with error
    exit 1
}

# Install TDD enforcement git hooks
install_tdd_git_hooks() {
    local repo_dir=$1
    local hooks_dir="$repo_dir/.git/hooks"
    
    # Pre-commit hook
    cat > "$hooks_dir/pre-commit" << 'EOF'
#!/bin/bash
# TDD Enforcement Pre-commit Hook

echo "🔍 Running TDD compliance check..."

# Source TDD enforcement functions
source "$(dirname "$0")/../../scripts/tdd-enforcement.sh" 2>/dev/null || {
    echo "❌ TDD enforcement scripts not found"
    exit 1
}

# Check for active TDD state
if [[ ! -f ".tdd_state.json" ]]; then
    echo "❌ No TDD state found. Run: init_tdd_enforcement <task_id>"
    exit 1
fi

task_id=$(jq -r '.task_id' .tdd_state.json)

# Validate TDD compliance for staged changes
if ! validate_staged_changes_tdd_compliance "$task_id"; then
    echo "🚫 TDD compliance check failed"
    echo "📋 Fix violations and try again"
    exit 1
fi

echo "✅ TDD compliance check passed"
EOF
    
    # Pre-push hook
    cat > "$hooks_dir/pre-push" << 'EOF'
#!/bin/bash
# TDD Enforcement Pre-push Hook

echo "🔍 Running comprehensive TDD audit..."

# Source TDD enforcement functions
source "$(dirname "$0")/../../scripts/tdd-enforcement.sh" 2>/dev/null || {
    echo "❌ TDD enforcement scripts not found"
    exit 1
}

if [[ ! -f ".tdd_state.json" ]]; then
    echo "❌ No TDD state found"
    exit 1
fi

task_id=$(jq -r '.task_id' .tdd_state.json)

# Full TDD evidence audit
if ! audit_tdd_evidence "$task_id"; then
    echo "🚫 TDD evidence audit failed"
    exit 1
fi

echo "✅ TDD audit passed"
EOF
    
    # Make hooks executable
    chmod +x "$hooks_dir/pre-commit"
    chmod +x "$hooks_dir/pre-push"
    
    echo "✅ TDD git hooks installed"
}

# Collect RED phase evidence
collect_red_phase_evidence() {
    local test_file=$1
    local task_id=$2
    local timestamp=$3
    
    local evidence_dir="$TDD_EVIDENCE_DIR/$task_id"
    local evidence_file="$evidence_dir/red-phase-evidence.json"
    
    echo "📊 Collecting RED phase evidence..."
    
    # Gather evidence
    cat > "$evidence_file" << EOF
{
  "phase": "RED",
  "task_id": "$task_id",
  "timestamp": "$timestamp",
  "test_file": "$test_file",
  "test_content_hash": "$(sha256sum "$test_file" | cut -d' ' -f1)",
  "test_execution": {
    "command": "$(get_test_command "$test_file")",
    "exit_code": 1,
    "output_file": "test-output-$(date +%s).txt",
    "failure_reason": "$(extract_failure_reason "$test_file")"
  },
  "implementation_status": {
    "implementation_exists": false,
    "verification_timestamp": "$timestamp"
  },
  "compliance_checks": {
    "test_fails_appropriately": true,
    "no_syntax_errors": true,
    "no_premature_implementation": true,
    "proper_failure_reason": true
  },
  "evidence_integrity": {
    "checksum": "$(calculate_evidence_checksum "$evidence_file")",
    "signature": "$(sign_evidence "$evidence_file")"
  }
}
EOF
    
    echo "✅ RED phase evidence collected: $evidence_file"
}

# Collect GREEN phase evidence
collect_green_phase_evidence() {
    local impl_file=$1
    local test_file=$2
    local task_id=$3
    local timestamp=$4
    
    local evidence_dir="$TDD_EVIDENCE_DIR/$task_id"
    local evidence_file="$evidence_dir/green-phase-evidence.json"
    
    echo "📊 Collecting GREEN phase evidence..."
    
    # Run coverage analysis
    run_coverage_analysis "$test_file" "$task_id"
    
    cat > "$evidence_file" << EOF
{
  "phase": "GREEN",
  "task_id": "$task_id",
  "timestamp": "$timestamp",
  "implementation_file": "$impl_file",
  "implementation_hash": "$(sha256sum "$impl_file" | cut -d' ' -f1)",
  "test_file": "$test_file",
  "test_execution": {
    "command": "$(get_test_command "$test_file")",
    "exit_code": 0,
    "output_file": "green-test-output-$(date +%s).txt"
  },
  "coverage_analysis": {
    "line_coverage": "$(get_coverage_percentage "$task_id")",
    "branch_coverage": "$(get_branch_coverage "$task_id")",
    "coverage_report": "coverage-report-$(date +%s).html"
  },
  "implementation_analysis": {
    "is_minimal": "$(verify_minimal_implementation "$impl_file" "$test_file")",
    "complexity_score": "$(calculate_complexity "$impl_file")",
    "lines_of_code": "$(wc -l < "$impl_file")"
  },
  "regression_testing": {
    "all_tests_pass": "$(run_full_test_suite && echo true || echo false)",
    "test_count": "$(count_total_tests)",
    "execution_time": "$(measure_test_execution_time)"
  },
  "compliance_checks": {
    "tests_pass": true,
    "minimal_implementation": true,
    "no_regressions": true,
    "coverage_adequate": true
  },
  "evidence_integrity": {
    "checksum": "$(calculate_evidence_checksum "$evidence_file")",
    "signature": "$(sign_evidence "$evidence_file")"
  }
}
EOF
    
    echo "✅ GREEN phase evidence collected: $evidence_file"
}

# Utility functions
find_corresponding_test() {
    local impl_file=$1
    local base_name=$(basename "${impl_file%.*}")
    local dir_name=$(dirname "$impl_file")
    
    # Common test file patterns
    local test_patterns=(
        "$dir_name/test_${base_name}.*"
        "$dir_name/${base_name}_test.*"
        "$dir_name/${base_name}.test.*"
        "tests/test_${base_name}.*"
        "test/test_${base_name}.*"
        "__tests__/${base_name}.test.*"
    )
    
    for pattern in "${test_patterns[@]}"; do
        local matches=($(ls $pattern 2>/dev/null))
        if [[ ${#matches[@]} -gt 0 ]]; then
            echo "${matches[0]}"
            return
        fi
    done
}

# Clean up TDD enforcement
cleanup_tdd_enforcement() {
    local working_dir=${1:-.}
    
    echo "🧹 Cleaning up TDD enforcement..."
    
    # Kill file watcher
    if [[ -f "$working_dir/.tdd_watcher.pid" ]]; then
        kill $(cat "$working_dir/.tdd_watcher.pid") 2>/dev/null
        rm "$working_dir/.tdd_watcher.pid"
    fi
    
    # Archive evidence
    if [[ -f "$working_dir/$TDD_STATE_FILE" ]]; then
        local task_id=$(jq -r '.task_id' "$working_dir/$TDD_STATE_FILE")
        archive_tdd_evidence "$task_id"
    fi
    
    echo "✅ TDD enforcement cleanup complete"
}

# Export functions
export -f init_tdd_enforcement
export -f setup_tdd_watcher
export -f handle_file_change
export -f validate_red_phase
export -f validate_green_phase
export -f block_progression
export -f cleanup_tdd_enforcement
```

────────────────────────────────────────────────────────────────────────────────

## TDD Evidence Schema

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "TDD Evidence Schema",
  "type": "object",
  "properties": {
    "red_phase_evidence": {
      "type": "object",
      "required": ["phase", "task_id", "timestamp", "test_file", "compliance_checks"],
      "properties": {
        "phase": {"const": "RED"},
        "task_id": {"type": "string"},
        "timestamp": {"type": "string", "format": "date-time"},
        "test_file": {"type": "string"},
        "test_content_hash": {"type": "string"},
        "test_execution": {
          "type": "object",
          "properties": {
            "command": {"type": "string"},
            "exit_code": {"const": 1},
            "output_file": {"type": "string"},
            "failure_reason": {"type": "string"}
          }
        },
        "compliance_checks": {
          "type": "object",
          "properties": {
            "test_fails_appropriately": {"const": true},
            "no_syntax_errors": {"const": true},
            "no_premature_implementation": {"const": true}
          }
        }
      }
    },
    "green_phase_evidence": {
      "type": "object",
      "required": ["phase", "task_id", "timestamp", "implementation_file", "compliance_checks"],
      "properties": {
        "phase": {"const": "GREEN"},
        "task_id": {"type": "string"},
        "timestamp": {"type": "string", "format": "date-time"},
        "implementation_file": {"type": "string"},
        "coverage_analysis": {
          "type": "object",
          "properties": {
            "line_coverage": {"type": "number", "minimum": 90},
            "branch_coverage": {"type": "number", "minimum": 80}
          }
        },
        "compliance_checks": {
          "type": "object",
          "properties": {
            "tests_pass": {"const": true},
            "minimal_implementation": {"const": true},
            "no_regressions": {"const": true},
            "coverage_adequate": {"const": true}
          }
        }
      }
    }
  }
}
```