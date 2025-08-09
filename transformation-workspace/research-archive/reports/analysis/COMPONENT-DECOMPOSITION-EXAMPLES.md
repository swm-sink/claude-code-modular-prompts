# Component Decomposition Examples
## Concrete Examples of Breaking Down Complex Components

*Generated: 2025-07-31*
*Purpose: Demonstrate how to achieve "many small prompt components"*

## Example 1: Decomposing workflow-coordinator.md

### Current Component (Multi-Purpose)
```markdown
# Workflow Coordinator Component

Coordinate multi-step workflow execution:
- Accept and parse input data or parameters
- Define workflow step sequence and dependencies  
- Execute steps in proper order
- Process step failures and recovery
- Coordinate parallel step execution when possible
- Ensure workflow completion criteria are met
```

### Decomposed Components (Single-Purpose)

#### 1. workflow-input-parser.md
```markdown
# Workflow Input Parser Component

Parse and validate workflow input:
- Accept raw input data or parameters
- Validate required fields are present
- Convert input to standardized format
- Return parsed configuration object
```

#### 2. workflow-sequencer.md
```markdown
# Workflow Sequencer Component

Define workflow step sequence:
- Accept list of workflow steps
- Identify step dependencies
- Generate execution order
- Return sequenced step array
```

#### 3. step-executor.md
```markdown
# Step Executor Component

Execute a single workflow step:
- Accept step definition and context
- Execute step operation
- Capture step result or error
- Return execution outcome
```

#### 4. step-failure-handler.md
```markdown
# Step Failure Handler Component

Handle individual step failures:
- Accept failure context and error
- Determine retry eligibility
- Execute retry with backoff if appropriate
- Return recovery action or escalate
```

#### 5. parallel-coordinator.md
```markdown
# Parallel Coordinator Component

Coordinate parallel execution:
- Accept list of parallelizable steps
- Spawn concurrent executions
- Monitor parallel progress
- Aggregate results when complete
```

#### 6. workflow-completion-checker.md
```markdown
# Workflow Completion Checker Component

Verify workflow completion:
- Accept workflow state and criteria
- Check all required steps completed
- Validate success conditions met
- Return completion status
```

## Example 2: Decomposing data-transformer.md

### Current Component (Multi-Purpose)
```markdown
# Data Transformer Component

Transform data between different formats:
- Parse input data format
- Validate data structure
- Apply transformation rules
- Format output data
- Handle transformation errors
```

### Decomposed Components (Single-Purpose)

#### 1. data-parser.md
```markdown
# Data Parser Component

Parse input data:
- Detect data format (JSON, XML, CSV, etc.)
- Parse data using appropriate parser
- Return parsed data structure
```

#### 2. data-validator.md
```markdown
# Data Validator Component

Validate data structure:
- Accept data and schema
- Validate against schema rules
- Return validation result
```

#### 3. transformation-rule-engine.md
```markdown
# Transformation Rule Engine Component

Apply transformation rules:
- Accept data and transformation rules
- Execute rules in sequence
- Return transformed data
```

#### 4. data-formatter.md
```markdown
# Data Formatter Component

Format data for output:
- Accept data and target format
- Apply formatting rules
- Return formatted data
```

#### 5. transformation-error-handler.md
```markdown
# Transformation Error Handler Component

Handle transformation errors:
- Accept error context
- Log error details
- Return error response
```

## Example 3: Decomposing git-operations.md

### Current Component (All Git Operations)
```markdown
# Git Operations Component

Handle git operations:
- Git add files
- Git commit with message
- Git push to remote
- Git pull from remote
- Git status check
- Git branch operations
```

### Decomposed Components (Single Git Operation Each)

#### 1. git-add.md
```markdown
# Git Add Component

Stage files for commit:
- Accept file paths or patterns
- Execute git add command
- Return staging result
```

#### 2. git-commit.md
```markdown
# Git Commit Component

Create git commit:
- Accept commit message
- Execute git commit
- Return commit hash
```

#### 3. git-push.md
```markdown
# Git Push Component

Push to remote:
- Accept remote and branch
- Execute git push
- Return push result
```

#### 4. git-pull.md
```markdown
# Git Pull Component

Pull from remote:
- Accept remote and branch
- Execute git pull
- Return pull result
```

#### 5. git-status.md
```markdown
# Git Status Component

Check repository status:
- Execute git status
- Parse status output
- Return status object
```

#### 6. git-branch-create.md
```markdown
# Git Branch Create Component

Create new branch:
- Accept branch name
- Execute git branch
- Return creation result
```

#### 7. git-branch-switch.md
```markdown
# Git Branch Switch Component

Switch branches:
- Accept target branch
- Execute git checkout
- Return switch result
```

## Example 4: Creating New Atomic Components from Commands

### From /test Command → Testing Components

#### 1. test-discoverer.md
```markdown
# Test Discoverer Component

Discover test files:
- Accept test directory path
- Find test files by pattern
- Return test file list
```

#### 2. test-filter.md
```markdown
# Test Filter Component

Filter tests to run:
- Accept test list and criteria
- Apply inclusion/exclusion rules
- Return filtered test list
```

#### 3. test-executor.md
```markdown
# Test Executor Component

Execute single test:
- Accept test file path
- Run test with framework
- Return test result
```

#### 4. test-reporter.md
```markdown
# Test Reporter Component

Generate test report:
- Accept test results
- Format results as report
- Return formatted report
```

## Assembly Example: Building Commands from Components

### Before (Monolithic Command)
```yaml
name: /test
description: Run all tests with coverage

implementation: |
  1. Find all test files
  2. Filter based on arguments
  3. Set up test environment
  4. Run tests sequentially or in parallel
  5. Collect coverage data
  6. Generate report
  7. Clean up environment
```

### After (Component Assembly)
```yaml
name: /test
description: Run tests using component assembly

components:
  - test-discoverer
  - test-filter
  - environment-setup
  - test-executor
  - parallel-coordinator (if --parallel)
  - coverage-collector
  - test-reporter
  - environment-cleanup

assembly_flow: |
  1. Use test-discoverer to find tests
  2. Use test-filter to apply criteria
  3. Use environment-setup to prepare
  4. If parallel:
     - Use parallel-coordinator with test-executor
  5. Else:
     - Use test-executor for each test
  6. Use coverage-collector to gather metrics
  7. Use test-reporter to format results
  8. Use environment-cleanup to clean up
```

## Benefits of Decomposition

### 1. Increased Reusability
- `test-executor` can be used by any testing command
- `parallel-coordinator` can be used for any parallel work
- `data-parser` can be used wherever data parsing is needed

### 2. Easier Testing
- Each component has single responsibility to test
- Clear inputs and outputs
- Isolated functionality

### 3. Better AI Understanding
- AI can learn what each small component does
- AI can suggest appropriate components for tasks
- AI can assemble novel combinations

### 4. Improved Maintainability
- Changes isolated to specific components
- Clear dependency tracking
- Version components independently

### 5. Enhanced Discoverability
- Users can find specific functionality
- Clear naming indicates purpose
- Smaller components easier to understand

## Decomposition Guidelines

### 1. Single Responsibility Rule
Each component should do ONE thing well

### 2. Clear Input/Output
Define what goes in and what comes out

### 3. No Hidden Dependencies
Explicitly declare all requirements

### 4. Composable Design
Components should work well together

### 5. Descriptive Naming
Name should indicate exact function

## Target Metrics After Decomposition

### Current State
- 91 components (many multi-purpose)
- Average 6-7 responsibilities per component
- Low reusability

### Target State
- 150-200 components (all single-purpose)
- 1 responsibility per component
- High reusability (>60% used multiple times)

This decomposition approach will achieve the goal of "many small prompt components and fewer example commands built using them."