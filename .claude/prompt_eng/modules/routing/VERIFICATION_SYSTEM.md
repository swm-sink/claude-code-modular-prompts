# Routing Verification & Audit System v1.0.0

## Overview

Every routing decision must be verifiable, auditable, and reproducible. This system ensures transparency and accountability in all command selections.

## Verification Components

### 1. Pre-Routing Verification
```yaml
pre_routing_checks:
  requirement_clarity:
    - check: "Is user request specific?"
    - check: "Are success criteria defined?"
    - check: "Is scope clearly bounded?"
    
  component_countability:
    - check: "Can we identify affected files?"
    - check: "Can we count required changes?"
    - check: "Are dependencies identifiable?"
    
  safety_validation:
    - check: "No destructive operations?"
    - check: "No security risks?"
    - check: "Reversible changes?"
```

### 2. Component Counting Verification
```yaml
counting_verification:
  file_identification:
    method: "grep_and_glob"
    verify: "All identified files exist"
    record:
      - files_found: []
      - files_missing: []
      - search_patterns: []
      
  dependency_analysis:
    method: "import_parsing"
    verify: "All dependencies resolved"
    record:
      - internal_deps: []
      - external_deps: []
      - circular_refs: []
      
  change_estimation:
    method: "ast_analysis"
    verify: "Functions identified correctly"
    record:
      - functions_affected: []
      - classes_affected: []
      - line_ranges: []
```

### 3. Threshold Application Verification
```yaml
threshold_verification:
  for_each_command:
    - load_thresholds()
    - check_each_condition()
    - record_pass_fail()
    - generate_score()
    
  verification_record:
    command: "/task"
    checks:
      - condition: "total_files <= 3"
        expected: true
        actual: true
        passed: true
      - condition: "cross_module_deps == 0"
        expected: true
        actual: false
        passed: false
    overall: failed
    reason: "Cross-module dependencies detected"
```

### 4. Post-Routing Verification
```yaml
post_routing_checks:
  decision_validation:
    - check: "Selected command can handle request"
    - check: "No better alternative exists"
    - check: "Decision follows guidelines"
    
  audit_trail_complete:
    - check: "All counts recorded"
    - check: "Rationale documented"
    - check: "Alternatives considered"
```

## Audit Trail Structure

### Routing Decision Audit
```yaml
routing_audit:
  audit_id: "audit-2025-07-08-abc123"
  timestamp: "2025-07-08T12:00:00Z"
  version: "1.0.0"
  
  request_analysis:
    original_request: "Add user authentication to the API"
    parsed_intent: "Create authentication system"
    identified_components:
      nouns: ["user", "authentication", "API"]
      verbs: ["add", "create"]
      scope: "feature"
      
  component_counts:
    files:
      to_create: 4
      to_modify: 2
      to_read: 6
      total: 6
    code:
      functions_affected: 8
      new_functions: 4
      modified_functions: 4
    tests:
      to_write: 6
      to_modify: 2
    dependencies:
      internal: 3
      cross_module: 1
      external: 2
      
  threshold_evaluation:
    commands_evaluated:
      - command: "/task"
        conditions_met: 0
        conditions_failed: 3
        fail_reasons:
          - "total_files (6) > max_allowed (3)"
          - "cross_module_deps (1) > max_allowed (0)"
          - "files_to_create (4) > max_allowed (1)"
          
      - command: "/feature"
        conditions_met: 4
        conditions_failed: 0
        suitable: true
        
      - command: "/swarm"
        conditions_met: 1
        conditions_failed: 2
        suitable: false
        
  routing_decision:
    selected_command: "/feature"
    confidence: 0.95
    rationale: |
      - 6 total files affected (within /feature range 2-10)
      - Design decisions needed for auth system
      - Clear feature specification provided
      - Cross-module deps (1) within limit (2)
    
  alternatives_considered:
    - command: "/task"
      rejected_because: "Exceeds file count limits"
    - command: "/swarm"
      rejected_because: "Unnecessary complexity for this scope"
      
  verification_status:
    pre_routing: "passed"
    counting: "passed"
    threshold: "passed"
    post_routing: "passed"
    overall: "verified"
```

## Audit Query System

### Query Examples
```sql
-- Find all routing decisions for a session
SELECT * FROM routing_audits 
WHERE session_id = 'session-123'
ORDER BY timestamp;

-- Find decisions that selected /swarm
SELECT * FROM routing_audits
WHERE selected_command = '/swarm'
AND timestamp > '2025-07-01';

-- Find failed verifications
SELECT * FROM routing_audits
WHERE verification_status.overall != 'verified';

-- Analyze threshold effectiveness
SELECT 
  selected_command,
  COUNT(*) as usage_count,
  AVG(confidence) as avg_confidence
FROM routing_audits
GROUP BY selected_command;
```

### Audit Reports
```yaml
daily_routing_report:
  date: "2025-07-08"
  total_routings: 156
  
  by_command:
    /task: 89 (57%)
    /feature: 34 (22%)
    /swarm: 12 (8%)
    /query: 15 (10%)
    /auto: 6 (3%)
    
  verification_status:
    verified: 154 (98.7%)
    failed: 2 (1.3%)
    
  average_confidence: 0.93
  
  threshold_violations: 2
  manual_overrides: 0
```

## Verification Rules

### Mandatory Verification
1. Every routing decision must generate an audit record
2. All component counts must be verifiable
3. Threshold evaluations must be recorded
4. Rejected alternatives must include reasons

### Verification Failures
```yaml
on_verification_failure:
  immediate_actions:
    - Log detailed failure reason
    - Create error artifact
    - Route to /auto for analysis
    
  recovery_protocol:
    - Re-analyze request
    - Re-count components
    - Consider manual override
    - Document recovery path
```

### Continuous Improvement
```yaml
improvement_metrics:
  track:
    - Routing accuracy (expected vs actual outcomes)
    - Threshold effectiveness
    - Verification failure patterns
    - User satisfaction
    
  adjust:
    - Update thresholds based on outcomes
    - Refine counting methods
    - Improve verification checks
    - Document pattern changes
```

## Implementation

### Verification Module
Location: `.claude/routing/verification/verifier.py`

### Audit Storage
Location: `.claude/routing/audits/`

### Query Interface
Location: `.claude/routing/verification/query.py`