---
name: /swarm
description: Orchestrate a swarm of specialized agents working in parallel on complex (v1.0)
version: "1.0"
usage: '/swarm [task description and agent roles]'
category: specialized
allowed-tools:
- Task
- TodoWrite
- Read
- Write
- Edit
- Bash
- Grep
- Glob
dependencies:
- /help
- /welcome
validation:
  pre-execution: Validate input parameters and execution context
  during-execution: Monitor progress and maintain safety checks
  post-execution: Verify successful completion and cleanup
progressive-disclosure:
  layer-integration: Integrated command for specialized workflows
  escalation-path: Basic usage → advanced options → full customization
  de-escalation: Simplify to essential functionality
safety-measures:
  - Validate all inputs before execution
  - Create backups when modifying files
  - Confirm destructive operations
  - Maintain system integrity
error-recovery:
  input-error: Provide clear usage examples and syntax
  execution-failure: Show detailed context and recovery steps
  system-error: Fallback to safe mode operation
---
<command_file>
<purpose>
Coordinate multiple specialized agents working as a collaborative AI development team using swarm intelligence patterns.
</purpose>
<arguments>
- task: The complex task to be accomplished by the swarm
- roles: Optional specific agent roles (e.g., architect, coder, tester, reviewer)
</arguments>
<examples>
/swarm Refactor the authentication module with architect, security, and testing agents
/swarm Implement a new feature across frontend and backend with parallel development
/swarm Analyze codebase for performance issues using multiple analysis agents
</examples>
<claude_prompt>
You are orchestrating a swarm of specialized AI agents to accomplish a complex task. Your role is the Queen/Orchestrator agent coordinating worker agents.
Task: $ARGUMENTS
<include>components/validation/validation-framework.md</include>
<include>components/orchestration/task-planning.md</include>
## Swarm Intelligence Protocol
### Phase 1: Task Analysis and Role Assignment
1. Analyze the provided task to identify distinct work streams
2. Determine optimal agent roles based on task requirements:
   - **Architect Agent**: System design and architectural decisions
   - **Coder Agent**: Implementation and code writing
   - **Tester Agent**: Test creation and quality assurance
   - **Security Agent**: Security analysis and vulnerability checking
   - **Reviewer Agent**: Code review and best practices enforcement
   - **Documentation Agent**: Documentation and knowledge capture
### Phase 2: Swarm Initialization
Create a structured task plan for the swarm:
```json
{
  "swarm_id": "unique_identifier",
  "task": "main_objective",
  "agents": [
    {
      "role": "agent_type",
      "objective": "specific_goal",
      "dependencies": ["other_agents"],
      "status": "pending|active|complete"
    }
  ],
  "coordination": {
    "parallel_streams": [],
    "synchronization_points": []
  }
}
```
### Phase 3: Parallel Agent Execution
Use the Task tool to spawn specialized agents for parallel work:
1. **Independent Tasks**: Spawn agents that can work without dependencies
2. **Coordinated Tasks**: Manage agent dependencies and data flow
3. **Progress Tracking**: Monitor agent status and results
<include>components/actions/parallel-execution.md</include>
### Phase 4: Swarm Coordination
As the orchestrator:
1. Monitor agent progress through shared context
2. Resolve conflicts between agent outputs
3. Ensure consistency across parallel work streams
4. Aggregate results from all agents
### Phase 5: Result Synthesis
1. Collect outputs from all worker agents
2. Resolve any conflicts or inconsistencies
3. Integrate changes into a cohesive solution
4. Verify complete task accomplishment
<include>components/workflow/error-handling.md</include>
<include>components/orchestration/progress-tracking.md</include>
## Quality Gates
- All agent tasks must complete successfully
- No conflicts in parallel changes
- Comprehensive test coverage from tester agents
- Security clearance from security agent
- Documentation complete from documentation agent
Report the swarm execution results with:
- Summary of work accomplished
- Agent performance metrics
- Any issues encountered and resolutions
- Final integrated solution
</claude_prompt>
</command_file>