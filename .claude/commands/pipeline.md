---
name: /pipeline
description: Execute sequential processing pipeline with specialized agents at each stage
usage: /pipeline [multi-stage workflow description]
tools: Task, TodoWrite, Read, Write, Edit, Bash, Grep, Glob
test_coverage: 0%
---

<command_file>
<purpose>
Orchestrate a linear flow of tasks through specialized agent stages, with each stage processing and transforming data for the next.
</purpose>

<arguments>
- stages: Description of pipeline stages and their purposes
- data: Initial data or context to process through the pipeline
</arguments>

<examples>
/pipeline Code Analysis → Security Scan → Test Generation → Documentation → Deployment
/pipeline Feature Request → Design → Implementation → Review → Testing → Release
/pipeline Raw Data → Validation → Transformation → Analysis → Visualization → Report
</examples>

<claude_prompt>
You are implementing a Pipeline Pattern for sequential agent processing. Each stage has a specialized agent that processes input and produces output for the next stage.

Pipeline: $ARGUMENTS

<include>.claude/components/validation/input-validation.md</include>
<include>.claude/components/pipeline-validation.md</include>

## Pipeline Orchestration Protocol

### Phase 1: Pipeline Definition
Analyze and structure the pipeline:

```json
{
  "pipeline_id": "unique_identifier",
  "stages": [
    {
      "stage_id": "stage_name",
      "agent_role": "specialized_agent_type",
      "input_schema": {
        "required": ["field1", "field2"],
        "optional": ["field3"]
      },
      "output_schema": {
        "produces": ["result1", "result2"]
      },
      "processing": {
        "timeout": 300,
        "retry_count": 3,
        "error_handling": "fail|skip|default"
      },
      "status": "pending|running|complete|failed"
    }
  ],
  "data_flow": {
    "initial_input": {},
    "stage_outputs": {},
    "final_output": {}
  },
  "execution_mode": "strict|flexible"
}
```

### Phase 2: Stage Configuration
Configure each pipeline stage:

1. **Analysis Stage**: Understand and validate input
2. **Processing Stage**: Transform data according to rules
3. **Quality Stage**: Verify output meets requirements
4. **Handoff Stage**: Prepare data for next stage

### Phase 3: Pipeline Execution
Execute the pipeline with proper flow control:

#### Sequential Execution Flow
```
for each stage in pipeline:
  1. Validate stage input against schema
  2. Spawn specialized agent for stage
  3. Execute stage processing
  4. Validate stage output
  5. Transform output for next stage
  6. Handle errors and retries
  7. Update pipeline state
```

#### Stage Agent Templates

**Code Analysis Agent**:
- Parse and analyze code structure
- Identify patterns and issues
- Generate analysis report

**Security Scan Agent**:
- Scan for vulnerabilities
- Check compliance rules
- Produce security report

**Test Generation Agent**:
- Create test cases from specs
- Generate test fixtures
- Validate test coverage

**Documentation Agent**:
- Extract documentation needs
- Generate API docs
- Create user guides

**Deployment Agent**:
- Prepare deployment artifacts
- Execute deployment steps
- Verify deployment success

<include>.claude/components/stage-templates.md</include>

### Phase 4: Data Transformation
Manage data flow between stages:

1. **Input Validation**: Ensure data meets stage requirements
2. **Transformation Rules**: Apply stage-specific transformations
3. **Output Formatting**: Prepare data for next stage
4. **State Preservation**: Maintain context across stages

```python
# Transformation example
def transform_stage_output(stage_output, next_stage_schema):
    transformed = {}
    for field in next_stage_schema['required']:
        if field in stage_output:
            transformed[field] = stage_output[field]
        else:
            transformed[field] = derive_field(stage_output, field)
    return transformed
```

### Phase 5: Pipeline Monitoring
Track pipeline execution:

1. **Stage Progress**: Monitor each stage completion
2. **Data Lineage**: Track data transformations
3. **Performance Metrics**: Measure stage execution times
4. **Error Tracking**: Log and handle failures

<include>.claude/components/pipeline-monitoring.md</include>

## Pipeline Patterns

### Strict Pipeline
- Each stage must complete before next begins
- No stage skipping allowed
- Failed stage stops pipeline

### Flexible Pipeline
- Stages can be skipped based on conditions
- Parallel stages where possible
- Graceful degradation on failures

### Branching Pipeline
- Conditional paths based on stage outputs
- Multiple terminal stages possible
- Dynamic stage selection

## Error Handling Strategies

1. **Fail Fast**: Stop pipeline on first error
2. **Fail Safe**: Continue with defaults on error
3. **Retry Logic**: Attempt failed stages with backoff
4. **Circuit Breaker**: Skip stages after repeated failures

<include>.claude/components/error-strategies.md</include>

## Quality Gates
- Each stage input validation passes
- Stage processing completes within timeout
- Output schema validation succeeds
- No data loss between stages
- Pipeline completes end-to-end

Report pipeline execution with:
- Stage-by-stage execution summary
- Data transformation audit trail
- Performance metrics per stage
- Any errors and recovery actions
- Final pipeline output and success metrics
</claude_prompt>
</command_file>