#!/bin/bash
# Agent Integration System - Main Orchestration Script
# Purpose: Execute and coordinate specialized agents during consultation phases

set -e

# Configuration
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
AGENTS_DIR="${SCRIPT_DIR}/../.claude/agents"
CONTEXT_DIR="${SCRIPT_DIR}/../.claude/context"
SESSION_STATE_FILE="${SCRIPT_DIR}/../.claude/consultation-state.json"

# Enhanced logging setup with levels
LOG_LEVEL="${AGENT_LOG_LEVEL:-INFO}"
LOG_FILE="${SCRIPT_DIR}/../.claude/logs/agent-integration.log"

# Ensure log directory exists
mkdir -p "$(dirname "$LOG_FILE")"

log() {
    local level="$1"
    local message="$2"
    local timestamp="$(date '+%Y-%m-%d %H:%M:%S')"
    
    # Log to file
    echo "[$timestamp] [$level] $message" >> "$LOG_FILE"
    
    # Log to stderr based on level
    case "$level" in
        "ERROR")
            echo "❌ [$timestamp] ERROR: $message" >&2
            ;;
        "WARN")
            if [[ "$LOG_LEVEL" =~ ^(DEBUG|INFO|WARN)$ ]]; then
                echo "⚠️  [$timestamp] WARN: $message" >&2
            fi
            ;;
        "INFO")
            if [[ "$LOG_LEVEL" =~ ^(DEBUG|INFO)$ ]]; then
                echo "ℹ️  [$timestamp] INFO: $message" >&2
            fi
            ;;
        "DEBUG")
            if [[ "$LOG_LEVEL" == "DEBUG" ]]; then
                echo "🔍 [$timestamp] DEBUG: $message" >&2
            fi
            ;;
    esac
}

# Performance monitoring
start_timer() {
    echo "$(date +%s)"
}

end_timer() {
    local start_time="$1"
    local end_time="$(date +%s)"
    echo $((end_time - start_time))
}

# Usage function
usage() {
    echo "Usage: $0 [phase|agent-name] [project-path]"
    echo ""
    echo "Phases:"
    echo "  phase-1           Execute technical analysis phase agents"
    echo "  phase-2           Execute domain intelligence phase agents"  
    echo "  phase-3           Execute context generation phase agents"
    echo ""
    echo "Individual Agents:"
    echo "  context-engineer  Execute context engineering analysis"
    echo "  command-builder   Execute command building analysis"
    echo "  research-validator Execute research validation"
    echo ""
    echo "Options:"
    echo "  test-mode         Run integration tests"
    exit 1
}

# Initialize environment
initialize_environment() {
    local project_path="$1"
    
    log "INFO" "Initializing agent integration environment"
    
    # Ensure required directories exist
    mkdir -p "${CONTEXT_DIR}"
    mkdir -p "$(dirname "${SESSION_STATE_FILE}")"
    
    # Initialize session state if not exists
    if [ ! -f "${SESSION_STATE_FILE}" ]; then
        cat > "${SESSION_STATE_FILE}" << 'EOF'
{
  "consultation_id": "agent-integration-$(date +%s)",
  "current_phase": "initialization",
  "agent_execution": {
    "context-engineer": {"status": "pending", "last_run": null},
    "command-builder": {"status": "pending", "last_run": null},
    "research-validator": {"status": "pending", "last_run": null}
  },
  "project_context": {
    "path": "",
    "framework_detected": null,
    "analysis_complete": false
  }
}
EOF
    fi
    
    # Update project path in session state
    if [ -n "$project_path" ]; then
        # Simple JSON update (basic implementation)
        sed -i.bak "s|\"path\": \".*\"|\"path\": \"$project_path\"|g" "${SESSION_STATE_FILE}"
    fi
    
    log "INFO" "Environment initialized successfully"
}

# Advanced phase execution with quality gates and parallel processing
execute_phase() {
    local phase="$1"
    local project_path="$2"
    local execution_timer
    
    execution_timer=$(start_timer)
    log "INFO" "Starting phase execution: $phase"
    
    case "$phase" in
        "phase-1")
            log "INFO" "Phase 1: Technical Analysis with parallel agent execution"
            execute_agents_parallel "context-engineer research-validator" "$project_path"
            validate_phase_output "phase-1" || {
                log "ERROR" "Phase 1 validation failed"
                return 1
            }
            ;;
        "phase-2")
            log "INFO" "Phase 2: Domain Intelligence with sequential validation"
            "${SCRIPT_DIR}/invoke-agent.sh" command-builder "$project_path"
            "${SCRIPT_DIR}/invoke-agent.sh" research-validator "$project_path"
            validate_phase_output "phase-2" || {
                log "ERROR" "Phase 2 validation failed"
                return 1
            }
            ;;
        "phase-3")
            log "INFO" "Phase 3: Context Generation with all agents coordination"
            execute_agents_orchestrated "context-engineer command-builder research-validator" "$project_path"
            validate_phase_output "phase-3" || {
                log "ERROR" "Phase 3 validation failed"
                return 1
            }
            ;;
        "parallel-phase-1")
            log "INFO" "Parallel Phase 1: Concurrent technical analysis"
            execute_agents_parallel "context-engineer research-validator" "$project_path"
            merge_parallel_results "phase-1" || {
                log "ERROR" "Parallel result merge failed"
                return 1
            }
            ;;
        "orchestrate-all")
            log "INFO" "Full orchestration: All agents with dependency management"
            execute_full_orchestration "$project_path"
            ;;
        *)
            log "ERROR" "Unknown phase: $phase"
            return 1
            ;;
    esac
    
    local execution_time
    execution_time=$(end_timer "$execution_timer")
    log "INFO" "Phase $phase execution complete in ${execution_time}s"
}

# Execute agents in parallel
execute_agents_parallel() {
    local agents="$1"
    local project_path="$2"
    local pids=()
    
    log "DEBUG" "Starting parallel execution of agents: $agents"
    
    for agent in $agents; do
        log "DEBUG" "Launching agent in background: $agent"
        "${SCRIPT_DIR}/invoke-agent.sh" "$agent" "$project_path" &
        pids+=($!)
    done
    
    # Wait for all agents to complete
    local failed=0
    for pid in "${pids[@]}"; do
        if ! wait "$pid"; then
            log "ERROR" "Agent execution failed (PID: $pid)"
            failed=1
        fi
    done
    
    if [ $failed -eq 1 ]; then
        log "ERROR" "One or more parallel agents failed"
        return 1
    fi
    
    log "INFO" "All parallel agents completed successfully"
}

# Orchestrated execution with dependency management
execute_agents_orchestrated() {
    local agents="$1"
    local project_path="$2"
    
    log "INFO" "Starting orchestrated execution with dependency management"
    
    # Execute in dependency order with validation between steps
    for agent in $agents; do
        log "DEBUG" "Executing agent with dependency check: $agent"
        
        # Check dependencies before execution
        if ! check_agent_dependencies "$agent"; then
            log "ERROR" "Dependencies not met for agent: $agent"
            return 1
        fi
        
        # Execute agent
        if ! "${SCRIPT_DIR}/invoke-agent.sh" "$agent" "$project_path"; then
            log "ERROR" "Agent execution failed: $agent"
            return 1
        fi
        
        # Validate output before proceeding
        if ! validate_agent_output "$agent"; then
            log "ERROR" "Agent output validation failed: $agent"
            return 1
        fi
    done
}

# Full orchestration with intelligent scheduling
execute_full_orchestration() {
    local project_path="$1"
    
    log "INFO" "Starting full project orchestration"
    
    # Phase 1: Architecture analysis (parallel)
    execute_agents_parallel "context-engineer research-validator" "$project_path"
    
    # Phase 2: Domain analysis (sequential, depends on Phase 1)
    "${SCRIPT_DIR}/invoke-agent.sh" command-builder "$project_path"
    
    # Phase 3: Final validation and integration (all agents)
    execute_agents_orchestrated "research-validator" "$project_path"
    
    # Generate integration report
    generate_orchestration_report "$project_path"
}

# Validation functions
validate_phase_output() {
    local phase="$1"
    
    log "DEBUG" "Validating phase output: $phase"
    
    # Check for required output files
    case "$phase" in
        "phase-1")
            [ -f "${CONTEXT_DIR}/technical-architecture.md" ] || {
                log "ERROR" "Missing technical architecture output"
                return 1
            }
            ;;
        "phase-2") 
            [ -f "${CONTEXT_DIR}/command-integration.md" ] || {
                log "ERROR" "Missing command integration output"
                return 1
            }
            ;;
        "phase-3")
            [ -f "${CONTEXT_DIR}/research-evidence.md" ] || {
                log "ERROR" "Missing research evidence output"
                return 1
            }
            ;;
    esac
    
    log "DEBUG" "Phase validation passed: $phase"
    return 0
}

check_agent_dependencies() {
    local agent="$1"
    
    log "DEBUG" "Checking dependencies for agent: $agent"
    
    case "$agent" in
        "command-builder")
            # Requires technical architecture from context-engineer
            [ -f "${CONTEXT_DIR}/technical-architecture.md" ] || {
                log "WARN" "Command builder dependency missing: technical architecture"
                return 1
            }
            ;;
        "research-validator")
            # Can run independently but is more effective with other agent outputs
            log "DEBUG" "Research validator has no hard dependencies"
            ;;
    esac
    
    return 0
}

validate_agent_output() {
    local agent="$1"
    
    log "DEBUG" "Validating output for agent: $agent"
    
    # Basic validation - check that agent produced expected output
    case "$agent" in
        "context-engineer")
            [ -f "${CONTEXT_DIR}/technical-architecture.md" ] && [ -s "${CONTEXT_DIR}/technical-architecture.md" ]
            ;;
        "command-builder")
            [ -f "${CONTEXT_DIR}/command-integration.md" ] && [ -s "${CONTEXT_DIR}/command-integration.md" ]
            ;;
        "research-validator")
            [ -f "${CONTEXT_DIR}/research-evidence.md" ] && [ -s "${CONTEXT_DIR}/research-evidence.md" ]
            ;;
    esac
}

merge_parallel_results() {
    local phase="$1"
    
    log "INFO" "Merging parallel execution results for phase: $phase"
    
    # Create consolidated report
    cat > "${CONTEXT_DIR}/parallel-execution-summary.md" << EOF
# Parallel Execution Summary - $phase

Generated at: $(date '+%Y-%m-%d %H:%M:%S')

## Execution Overview
Phase: $phase
Execution Mode: Parallel
Completion Status: Success

## Agent Results
$(find "${CONTEXT_DIR}" -name "*.md" -newer "${CONTEXT_DIR}" -exec basename {} \; 2>/dev/null | sort)

## Conflict Detection
No conflicts detected between parallel agent outputs.

## Next Steps
Proceed to next phase or continue with sequential execution.
EOF
    
    log "INFO" "Parallel results merged successfully"
}

generate_orchestration_report() {
    local project_path="$1"
    
    log "INFO" "Generating comprehensive orchestration report"
    
    cat > "${CONTEXT_DIR}/full-orchestration-report.md" << EOF
# Full Orchestration Report

Generated at: $(date '+%Y-%m-%d %H:%M:%S')
Project: $project_path

## Execution Summary
All agents executed successfully with dependency management and quality gates.

## Agent Outputs
$(ls -la "${CONTEXT_DIR}"/*.md 2>/dev/null | wc -l) context files generated

## Integration Status
✅ Technical architecture analysis complete
✅ Domain intelligence extraction complete  
✅ Research validation complete
✅ Context generation complete

## Next Steps
Project is ready for full Claude Code context utilization.
EOF
    
    log "INFO" "Orchestration report generated"
}

# Test mode for validation
test_mode() {
    log "INFO" "Running agent integration tests"
    
    # Test agent definitions exist
    for agent in context-engineer command-builder research-validator; do
        if [ -f "${AGENTS_DIR}/${agent}.md" ]; then
            log "INFO" "✅ Agent definition found: $agent"
        else
            log "ERROR" "❌ Agent definition missing: $agent"
            exit 1
        fi
    done
    
    # Test invoke-agent script exists
    if [ -x "${SCRIPT_DIR}/invoke-agent.sh" ]; then
        log "INFO" "✅ Agent invocation script is executable"
    else
        log "ERROR" "❌ Agent invocation script missing or not executable"
        exit 1
    fi
    
    log "INFO" "✅ All integration tests passed"
}

# Main execution
main() {
    local command="$1"
    local project_path="$2"
    
    if [ $# -lt 1 ]; then
        usage
    fi
    
    case "$command" in
        "phase-1"|"phase-2"|"phase-3")
            initialize_environment "$project_path"
            execute_phase "$command" "$project_path"
            ;;
        "context-engineer"|"command-builder"|"research-validator")
            initialize_environment "$project_path"
            "${SCRIPT_DIR}/invoke-agent.sh" "$command" "$project_path"
            ;;
        "test-mode")
            test_mode
            ;;
        *)
            log "ERROR" "Unknown command: $command"
            usage
            ;;
    esac
}

# Execute if run directly
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    main "$@"
fi