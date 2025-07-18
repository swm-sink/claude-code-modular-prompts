# Auto Command - Let Claude decide the best approach

**Description**: Let Claude decide the best approach for your request

────────────────────────────────────────────────────────────────────────────────

| version | last_updated | status | readiness |
|---------|--------------|--------|----------|
| 3.0.0   | 2025-07-18   | stable | 95%      |

────────────────────────────────────────────────────────────────────────────────

## Command Orchestration

```xml
<command_orchestration>
  <delegation_target>modules/patterns/intelligent-routing.md</delegation_target>
  <orchestration_flow>
    1. Analyze request complexity and intent
    2. Delegate to intelligent routing module
    3. Route to optimal command based on analysis
    4. Provide routing rationale to user
  </orchestration_flow>
  <routing_options>
    <simple_task>Route to /task for single component work</simple_task>
    <complex_feature>Route to /feature for multi-component development</complex_feature>
    <research_needed>Route to /query for analysis without modifications</research_needed>
    <multi_coordination>Route to /swarm for parallel development</multi_coordination>
    <production_work>Route to /protocol for deployment safety</production_work>
  </routing_options>
</command_orchestration>
```

## Usage

**Let Claude choose the best approach:**
```
/auto "I need to add user authentication to my app"
```

**When you're not sure which command to use:**
```
/auto "Fix performance issues in my application"
```

**For complex or unclear requirements:**
```
/auto "Implement a notification system with email and SMS"
```

## What This Command Does

- **Analyzes complexity**: Determines the scope and technical requirements
- **Intelligent routing**: Selects the optimal command based on analysis
- **Explains choice**: Provides rationale for the routing decision
- **Handles uncertainty**: Perfect when you're not sure which approach to take
- **Optimizes workflow**: Routes to the most efficient development path

## Examples

- `/auto "Add search functionality"` - Might route to /task for simple search or /feature for complex search
- `/auto "My app is slow"` - Routes to /query first to analyze, then appropriate development command
- `/auto "Deploy to production"` - Routes to /protocol for safe deployment procedures