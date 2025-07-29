---
name: /map-reduce
description: "Distribute work across parallel agents then aggregate results using map-reduce pattern"
usage: /map-reduce [large task to parallelize and aggregate]
tools: Task, TodoWrite, Read, Write, Edit, Bash, Grep, Glob
test_coverage: 0%
---
<command_file>
<purpose>
Implement map-reduce pattern to distribute large tasks across multiple parallel agents and aggregate their results into a unified output.
</purpose>
<arguments>
- task: The large task to be parallelized
- chunks: Optional number of chunks to split the work into
- aggregation: Optional aggregation strategy
</arguments>
<examples>
/map-reduce Analyze all 500 files in the codebase for security vulnerabilities
/map-reduce Refactor all components to use new API with 10 parallel agents
/map-reduce Generate comprehensive test suite for entire project in parallel
</examples>
<claude_prompt>
You are implementing a Map-Reduce orchestration pattern. Your role is to divide work into chunks, distribute to parallel agents, and aggregate their results.
Task: $ARGUMENTS
<include>components/validation/validation-framework.md</include>
## Map-Reduce Orchestration Protocol
### Phase 1: Work Analysis and Partitioning
Analyze the task to determine optimal partitioning:
```json
{
  "mapreduce_id": "unique_identifier",
  "task": "main_objective",
  "partitioning": {
    "strategy": "file|directory|module|size|count",
    "chunks": [
      {
        "chunk_id": "chunk_001",
        "scope": "specific_work_unit",
        "estimated_size": "complexity_measure",
        "assigned_agent": null,
        "status": "pending|mapped|reduced",
        "result": null
      }
    ],
    "total_chunks": 0,
    "chunk_size_target": "balanced|fixed|adaptive"
  },
  "agents": {
    "mapper_count": 0,
    "reducer_count": 1,
    "coordinator": "self"
  }
}
```
### Phase 2: Mapping Strategy
Define how to split the work:
#### Partitioning Strategies
1. **File-based Partitioning**:
   ```python
   # Split by files
   chunks = []
   for i in range(0, len(files), chunk_size):
       chunks.append(files[i:i+chunk_size])
   ```
2. **Size-based Partitioning**:
   ```python
   # Split by total size
   current_chunk = []
   current_size = 0
   for item in items:
       if current_size + item.size > max_chunk_size:
           chunks.append(current_chunk)
           current_chunk = [item]
           current_size = item.size
       else:
           current_chunk.append(item)
           current_size += item.size
   ```
3. **Complexity-based Partitioning**:
   ```python
   # Split by estimated complexity
   def estimate_complexity(item):
       # Return complexity score
       pass
   # Balance chunks by complexity
   ```
4. **Logical Partitioning**:
   ```python
   # Split by logical boundaries (modules, features, etc.)
   chunks = group_by_module(items)
   ```
### Phase 3: Map Phase Execution
Distribute chunks to mapper agents:
```
for each chunk in chunks:
  1. Create mapper agent specification
  2. Assign chunk to mapper
  3. Define expected output format
  4. Spawn mapper agent with Task tool
  5. Track mapper progress
```
#### Mapper Agent Template
```
You are a mapper agent processing chunk {chunk_id} of {total_chunks}.
Your specific scope: {chunk_scope}
Task: {specific_task_for_chunk}
Process your chunk and return results in this format:
{
  "chunk_id": "your_chunk_id",
  "processed_items": count,
  "results": [...],
  "metrics": {...},
  "issues": [...]
}
```
### Phase 4: Progress Monitoring
Track parallel execution:
1. **Active Mappers**: Monitor running agents
2. **Completed Chunks**: Track finished work
3. **Failed Chunks**: Handle and retry failures
4. **Performance Metrics**: Measure throughput
```python
# Monitoring state
monitoring = {
    "start_time": timestamp,
    "active_mappers": [],
    "completed_chunks": [],
    "failed_chunks": [],
    "retry_queue": [],
    "metrics": {
        "avg_chunk_time": 0,
        "throughput": 0,
        "success_rate": 0
    }
}
```
### Phase 5: Reduce Phase
Aggregate results from all mappers:
#### Reduction Strategies
1. **Simple Aggregation**:
   - Collect all results into a list
   - Concatenate outputs
   - Sum metrics
2. **Merge Strategy**:
   - Combine overlapping results
   - Resolve conflicts
   - Maintain consistency
3. **Hierarchical Reduction**:
   - Group related results
   - Apply reduction rules
   - Build final structure
4. **Statistical Aggregation**:
   - Calculate averages
   - Find patterns
   - Generate summary statistics
### Phase 6: Result Synthesis
Produce final aggregated output:
```json
{
  "mapreduce_result": {
    "total_items_processed": 0,
    "total_time": 0,
    "parallel_efficiency": 0.0,
    "aggregated_results": {},
    "summary_metrics": {},
    "identified_patterns": [],
    "recommendations": []
  }
}
```
## Load Balancing Strategies
### Static Load Balancing
- Equal chunk sizes
- Predetermined distribution
- Simple but may be inefficient
### Dynamic Load Balancing
- Monitor agent performance
- Redistribute work from slow agents
- Spawn additional agents for large chunks
### Work Stealing
- Idle agents take work from busy ones
- Maintains high utilization
- Reduces overall completion time
## Fault Tolerance
1. **Chunk Checkpointing**: Save intermediate results
2. **Failure Detection**: Monitor agent health
3. **Automatic Retry**: Reprocess failed chunks
4. **Partial Results**: Return what succeeded
## Quality Gates
- All chunks must be processed
- No data loss during mapping
- Reduction maintains consistency
- Performance improvement over sequential
- Results validation passes
Report map-reduce execution with:
- Partitioning strategy and chunk distribution
- Parallel execution metrics
- Individual mapper performance
- Reduction process summary
- Final aggregated results
- Performance comparison vs sequential approach
</claude_prompt>
</command_file>