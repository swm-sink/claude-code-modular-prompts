| version | last_updated | status |
|---------|--------------|--------|
| 1.0.0   | 2025-07-08   | stable |

# Worktree Isolation Module

────────────────────────────────────────────────────────────────────────────────

**PURPOSE**: Git worktree isolation for conflict-free parallel agent execution

────────────────────────────────────────────────────────────────────────────────

```xml
<module purpose="Implement worktree-based isolation for multi-agent development">
  
  <worktree_architecture>
    <structure>
      ```
      main-repo/
      ├── .git/
      └── code...
      
      ../worktrees/
      ├── swarm-{session}-{agent1}/
      ├── swarm-{session}-{agent2}/
      └── swarm-{session}-{agent3}/
      ```
    </structure>
    
    <naming_convention>
      <pattern>swarm-{session_id}-{agent_type}</pattern>
      <examples>
        - swarm-185-backend
        - swarm-185-frontend
        - swarm-185-testing
      </examples>
    </naming_convention>
    
    <lifecycle>
      <creation>At swarm initialization</creation>
      <usage>Throughout agent execution</usage>
      <cleanup>After successful merge</cleanup>
      <retention>Failed worktrees kept for debugging</retention>
    </lifecycle>
  </worktree_architecture>
  
  <isolation_guarantees>
    <file_system_isolation>
      <description>Each agent has separate file system view</description>
      <implementation>Git worktree with unique branch</implementation>
      <benefit>No file conflicts between agents</benefit>
    </file_system_isolation>
    
    <branch_isolation>
      <description>Each agent works on independent branch</description>
      <naming>swarm-{agent_type}-{session}</naming>
      <protection>Branch protection rules applied</protection>
    </branch_isolation>
    
    <commit_isolation>
      <description>Agents commit independently</description>
      <identity>Agent-specific commit identity</identity>
      <history>Clean, linear history per agent</history>
    </commit_isolation>
  </isolation_guarantees>
  
  <coordination_mechanisms>
    <initialization_protocol>
      ```bash
      # Create worktree for each agent
      git worktree add ../worktrees/swarm-$SESSION-$AGENT -b swarm-$AGENT
      
      # Set agent-specific git config
      cd ../worktrees/swarm-$SESSION-$AGENT
      git config user.name "Agent-$AGENT"
      git config user.email "agent-$AGENT@swarm.local"
      ```
    </initialization_protocol>
    
    <synchronization_points>
      <checkpoint_sync>Agents sync at defined checkpoints</checkpoint_sync>
      <dependency_notification>Notify when dependencies complete</dependency_notification>
      <merge_coordination>Orchestrated merge back to main</merge_coordination>
    </synchronization_points>
    
    <communication_channels>
      <shared_registry>.claude/swarm-decisions/session-{id}.json</shared_registry>
      <status_tracking>Agent status in worktree metadata</status_tracking>
      <artifact_sharing>Via registry, not direct file access</artifact_sharing>
    </communication_channels>
  </coordination_mechanisms>
  
  <merge_strategy>
    <preparation>
      <step>1. Verify all agents complete</step>
      <step>2. Run integration tests in each worktree</step>
      <step>3. Check for conflicts between branches</step>
      <step>4. Validate ownership rules maintained</step>
    </preparation>
    
    <merge_order>
      <strategy>Dependency-ordered merge</strategy>
      <sequence>
        1. Infrastructure/config changes first
        2. Backend changes
        3. Frontend changes  
        4. Tests last (verify everything)
      </sequence>
    </merge_order>
    
    <conflict_resolution>
      <automatic>Simple conflicts resolved by ownership rules</automatic>
      <manual>Complex conflicts escalated to orchestrator</manual>
      <fallback>Preserve both versions for human review</fallback>
    </conflict_resolution>
    
    <verification>
      <post_merge_tests>Full test suite in merged state</post_merge_tests>
      <integration_validation>Cross-component integration tests</integration_validation>
      <quality_gates>All gates must pass post-merge</quality_gates>
    </verification>
  </merge_strategy>
  
  <error_handling>
    <worktree_failures>
      <creation_failure>Fallback to sequential execution</creation_failure>
      <corruption>Recreate from main branch</corruption>
      <disk_space>Alert and clean old worktrees</disk_space>
    </worktree_failures>
    
    <merge_failures>
      <conflict_detection>Early detection via pre-merge check</conflict_detection>
      <rollback>Preserve worktrees for analysis</rollback>
      <recovery>Manual intervention with clear instructions</recovery>
    </merge_failures>
  </error_handling>
  
  <performance_optimization>
    <shallow_clones>Use --depth=1 for faster creation</shallow_clones>
    <sparse_checkout>Only check out agent's domain</sparse_checkout>
    <parallel_operations>Create all worktrees concurrently</parallel_operations>
    <resource_limits>Monitor disk usage and cleanup</resource_limits>
  </performance_optimization>
  
</module>
```

────────────────────────────────────────────────────────────────────────────────

## Worktree Commands

```bash
# Create worktree
git worktree add ../worktrees/swarm-$SESSION-$AGENT -b swarm-$AGENT

# List worktrees
git worktree list

# Remove worktree
git worktree remove ../worktrees/swarm-$SESSION-$AGENT

# Prune stale worktrees
git worktree prune
```

────────────────────────────────────────────────────────────────────────────────

*True isolation enables fearless parallel development.*