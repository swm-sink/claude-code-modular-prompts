| version | last_updated | status |
|---------|--------------|--------|
| 1.0.0   | 2025-07-14   | stable |

# Component Counting System v1.0.0

## Overview

Replace fuzzy complexity scoring with deterministic component counting. Every routing decision is based on explicit, countable metrics.

## Component Categories

### 1. File Components
```yaml
file_metrics:
  files_to_read: 0          # Count of files that need reading
  files_to_modify: 0        # Count of files to edit
  files_to_create: 0        # Count of new files
  files_to_delete: 0        # Count of deletions
  total_files_affected: 0   # Sum of all file operations
```

### 2. Code Components
```yaml
code_metrics:
  functions_to_modify: 0    # Count of functions affected
  classes_to_modify: 0      # Count of classes affected
  modules_imported: 0       # Count of new imports needed
  lines_to_change: 0        # Estimated lines affected
  breaking_changes: 0       # Count of API changes
```

### 3. Test Components
```yaml
test_metrics:
  tests_to_write: 0         # New test count
  tests_to_modify: 0        # Existing test updates
  test_files_affected: 0    # Test file count
  test_suites_involved: 0   # Test suite count
  integration_tests: 0      # Integration test count
```

### 4. Dependency Components
```yaml
dependency_metrics:
  internal_deps: 0          # Project module dependencies
  external_deps: 0          # External package dependencies
  circular_deps: 0          # Circular dependency count
  breaking_deps: 0          # Breaking dependency changes
  cross_module_deps: 0      # Cross-module dependencies
```

### 5. Architecture Components
```yaml
architecture_metrics:
  design_decisions: 0       # Architecture choices needed
  pattern_changes: 0        # Design pattern modifications
  structure_changes: 0      # Project structure changes
  interface_changes: 0      # API/Interface modifications
  data_model_changes: 0     # Schema/Model changes
```

### 6. Integration Components
```yaml
integration_metrics:
  systems_involved: 0       # External system count
  api_endpoints: 0          # API endpoint count
  database_operations: 0    # DB operation count
  service_interactions: 0   # Service call count
  event_handlers: 0         # Event handler count
```

## Counting Rules

### Explicit Counting
```python
def count_components(request):
    components = ComponentCounter()
    
    # File counting
    components.files_to_read = len(find_files_to_read(request))
    components.files_to_modify = len(find_files_to_modify(request))
    components.files_to_create = len(determine_new_files(request))
    
    # Code counting
    for file in files_to_modify:
        components.functions_to_modify += count_affected_functions(file)
        components.classes_to_modify += count_affected_classes(file)
        components.lines_to_change += estimate_line_changes(file)
    
    # Test counting
    components.tests_to_write = calculate_required_tests(request)
    components.test_files_affected = len(find_test_files(request))
    
    # Dependency counting
    components.internal_deps = count_internal_dependencies(request)
    components.cross_module_deps = count_cross_module_deps(request)
    
    return components
```

### No Estimates or Weights
- Count actual components, not estimates
- No subjective weights or multipliers
- Every component counts as 1
- Binary decisions only (present/absent)

## Component Thresholds

### Deterministic Rules
```yaml
routing_rules:
  use_task_when:
    total_files_affected: "≤ 3"
    cross_module_deps: "= 0"
    architecture_decisions: "= 0"
    breaking_changes: "= 0"
    
  use_feature_when:
    total_files_affected: "> 3 AND ≤ 10"
    cross_module_deps: "≤ 2"
    architecture_decisions: "≤ 2"
    design_required: "true"
    
  use_swarm_when:
    total_files_affected: "> 10"
    OR cross_module_deps: "> 2"
    OR systems_involved: "> 1"
    OR breaking_changes: "> 0"
    
  use_query_when:
    files_to_read: "> 0"
    AND files_to_modify: "= 0"
    AND research_needed: "true"
    
  use_auto_when:
    unclear_requirements: "true"
    OR cannot_count_components: "true"
```

## Counting Workflow

### 1. Parse Request
```yaml
parse_step:
  extract_nouns: ["user", "authentication", "database"]
  extract_verbs: ["create", "update", "refactor"]
  identify_scope: ["module", "feature", "system"]
```

### 2. Map Components
```yaml
mapping_step:
  nouns_to_files:
    "user": ["models/user.py", "tests/test_user.py"]
    "authentication": ["auth/login.py", "auth/logout.py"]
    
  verbs_to_operations:
    "create": ["files_to_create", "tests_to_write"]
    "update": ["files_to_modify", "tests_to_modify"]
    "refactor": ["functions_to_modify", "structure_changes"]
```

### 3. Count Explicitly
```yaml
counting_step:
  for_each_file:
    - check_exists()
    - count_functions()
    - count_dependencies()
    - identify_tests()
    
  for_each_operation:
    - count_affected_components()
    - check_breaking_changes()
    - assess_cross_module_impact()
```

### 4. Apply Thresholds
```yaml
threshold_step:
  total_components: sum(all_counts)
  
  if total_files ≤ 3 AND no_cross_module:
    route_to: "/task"
  elif total_files ≤ 10 AND has_design:
    route_to: "/feature"
  elif total_files > 10 OR cross_module > 2:
    route_to: "/swarm"
  else:
    route_to: "/auto"
```

## Audit Trail

### Every Count Recorded
```yaml
counting_audit:
  timestamp: "2025-07-08T12:00:00Z"
  request: "Add user authentication"
  
  counts:
    files_to_create: 4
    files_to_modify: 2
    functions_to_modify: 6
    tests_to_write: 8
    cross_module_deps: 1
    
  threshold_checks:
    - rule: "total_files ≤ 3"
      result: false
      actual: 6
    - rule: "cross_module_deps = 0"
      result: false
      actual: 1
      
  routing_decision: "/feature"
  rationale: "6 files affected, design required"
```

## Benefits

1. **Predictable**: Same input → same output always
2. **Auditable**: Every count is recorded
3. **Verifiable**: Counts can be validated
4. **Transparent**: Clear routing rules
5. **Objective**: No subjective scoring