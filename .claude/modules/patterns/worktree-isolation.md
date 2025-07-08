| version | last_updated | status |
|---------|--------------|--------|
| 1.0.0   | 2025-07-08   | stable |

# Worktree Isolation Module

────────────────────────────────────────────────────────────────────────────────

```xml
<module name="worktree_isolation" category="patterns">
  
  <purpose>
    Implement worktree-based isolation for multi-agent work to eliminate file conflicts
  </purpose>
  
  <thinking_pattern enforcement="MANDATORY">
    <step>1. Create isolated worktree for each agent/task</step>
    <step>2. Configure worktree with appropriate branch</step>
    <step>3. Set up agent-specific environment in worktree</step>
    <step>4. Execute agent work in isolated context</step>
    <step>5. Coordinate merges back to main branch</step>
    <step>6. Clean up worktrees after completion</step>
  </thinking_pattern>
  
  <implementation>
    
    <phase name="worktree_setup" order="1">
      <requirements>
        Unique worktree created for each agent
        Branch strategy supports parallel work
        Environment properly configured
      </requirements>
      <actions>
        Create worktree with unique identifier
        Set up feature branch for agent work
        Configure agent-specific settings
        Initialize required dependencies
      </actions>
      <validation>
        Worktree successfully created
        Branch properly configured
        Environment ready for agent
      </validation>
    </phase>
    
    <phase name="isolation_enforcement" order="2">
      <requirements>
        Agent work confined to worktree
        No cross-worktree interference
        Resource isolation maintained
      </requirements>
      <actions>
        Restrict agent to worktree directory
        Monitor for boundary violations
        Prevent shared resource conflicts
        Track worktree-specific changes
      </actions>
      <validation>
        Isolation boundaries enforced
        No cross-contamination detected
        Changes tracked properly
      </validation>
    </phase>
    
    <phase name="coordination_merge" order="3">
      <requirements>
        Changes merged without conflicts
        Integration testing performed
        Main branch integrity maintained
      </requirements>
      <actions>
        Prepare changes for integration
        Run pre-merge validation
        Execute merge with conflict resolution
        Verify post-merge integrity
      </actions>
      <validation>
        Merge completed successfully
        No integration issues
        Main branch stable
      </validation>
    </phase>
    
  </implementation>
  
  <worktree_patterns>
    <naming_convention>
      <format>{command}-{issue}-{agent}</format>
      <examples>
        swarm-123-backend
        swarm-123-frontend
        feature-456-api
        task-789-refactor
      </examples>
      <uniqueness>Timestamp suffix if needed</uniqueness>
    </naming_convention>
    
    <branch_strategy>
      <feature_branches>
        Create from main/master
        Named after worktree
        Deleted after merge
      </feature_branches>
      
      <protection_rules>
        No direct commits to main
        All work through worktrees
        PR required for merge
      </protection_rules>
      
      <cleanup_policy>
        Prune merged branches
        Archive old worktrees
        Maintain clean structure
      </cleanup_policy>
    </branch_strategy>
    
    <directory_structure>
      ```
      worktrees/
      ├── swarm-123-backend/      # Backend agent workspace
      ├── swarm-123-frontend/     # Frontend agent workspace
      ├── swarm-123-devops/       # DevOps agent workspace
      ├── feature-456-api/        # Single feature work
      └── .worktree-metadata/     # Tracking and coordination
          ├── active.json         # Active worktrees
          ├── locks.json          # Resource locks
          └── history.json        # Completed work
      ```
    </directory_structure>
  </worktree_patterns>
  
  <isolation_mechanisms>
    <filesystem_isolation>
      <separate_directories>
        Each agent works in own directory
        No shared file access between worktrees
        Clear ownership boundaries
      </separate_directories>
      
      <git_isolation>
        Separate git index per worktree
        Independent staging areas
        No commit conflicts
      </git_isolation>
      
      <dependency_isolation>
        Separate node_modules, venv, etc.
        Independent package installations
        No version conflicts
      </dependency_isolation>
    </filesystem_isolation>
    
    <process_isolation>
      <execution_context>
        Separate shell sessions
        Independent environment variables
        Isolated process trees
      </execution_context>
      
      <resource_limits>
        CPU/memory limits per worktree
        Disk quota enforcement
        Network isolation if needed
      </resource_limits>
      
      <monitoring>
        Track resource usage per worktree
        Detect runaway processes
        Enforce cleanup on completion
      </monitoring>
    </process_isolation>
  </isolation_mechanisms>
  
  <coordination_layer>
    <worktree_registry>
      <active_tracking>
        ```json
        {
          "worktrees": [
            {
              "id": "swarm-123-backend",
              "agent": "backend",
              "branch": "swarm-123-backend",
              "created": "2025-07-08T10:00:00Z",
              "status": "active",
              "owner": "agent-backend-1",
              "issue": 123
            }
          ]
        }
        ```
      </active_tracking>
      
      <lock_management>
        Prevent duplicate worktrees
        Coordinate shared resources
        Track ownership and access
      </lock_management>
      
      <lifecycle_events>
        Creation, activation, completion
        Merge readiness, cleanup
        Error and recovery states
      </lifecycle_events>
    </worktree_registry>
    
    <merge_coordination>
      <sequencing>
        Order merges by dependency
        Backend before frontend
        Infrastructure last
      </sequencing>
      
      <validation>
        Pre-merge testing required
        Integration tests must pass
        No regression allowed
      </validation>
      
      <conflict_resolution>
        Automatic for simple conflicts
        Agent coordination for complex
        Escalation to human if needed
      </conflict_resolution>
    </merge_coordination>
  </coordination_layer>
  
  <lifecycle_management>
    <creation>
      ```bash
      # Worktree creation pattern
      create_agent_worktree() {
        local agent_type="$1"
        local issue_id="$2"
        local worktree_name="${command}-${issue_id}-${agent_type}"
        
        # Create worktree with new branch
        git worktree add "worktrees/${worktree_name}" -b "${worktree_name}"
        
        # Register in tracking system
        register_worktree "${worktree_name}" "${agent_type}" "${issue_id}"
        
        # Configure agent environment
        setup_agent_environment "worktrees/${worktree_name}" "${agent_type}"
        
        echo "${worktree_name}"
      }
      ```
    </creation>
    
    <execution>
      ```bash
      # Agent execution in worktree
      execute_in_worktree() {
        local worktree_path="$1"
        local agent_command="$2"
        
        # Ensure isolation
        cd "${worktree_path}"
        
        # Set agent-specific environment
        export AGENT_WORKTREE="${worktree_path}"
        export AGENT_ISOLATION="enforced"
        
        # Execute with monitoring
        monitor_agent_execution "${agent_command}"
      }
      ```
    </execution>
    
    <cleanup>
      ```bash
      # Worktree cleanup pattern
      cleanup_worktree() {
        local worktree_name="$1"
        
        # Ensure work is complete
        verify_worktree_complete "${worktree_name}"
        
        # Remove worktree
        git worktree remove "worktrees/${worktree_name}"
        
        # Clean up branch if merged
        cleanup_merged_branch "${worktree_name}"
        
        # Update registry
        mark_worktree_completed "${worktree_name}"
      }
      ```
    </cleanup>
  </lifecycle_management>
  
  <monitoring_metrics>
    <isolation_effectiveness>
      <conflict_rate>File conflicts between agents</conflict_rate>
      <isolation_violations>Boundary crossing attempts</isolation_violations>
      <merge_success_rate>Clean merges percentage</merge_success_rate>
    </isolation_effectiveness>
    
    <resource_usage>
      <disk_usage>Space per worktree</disk_usage>
      <process_count>Active processes per agent</process_count>
      <memory_usage>RAM consumption tracking</memory_usage>
    </resource_usage>
    
    <coordination_metrics>
      <setup_time>Worktree creation duration</setup_time>
      <merge_time>Integration duration</merge_time>
      <cleanup_time>Removal and cleanup duration</cleanup_time>
    </coordination_metrics>
  </monitoring_metrics>
  
  <integration_points>
    <depends_on>
      patterns/multi-agent.md for agent coordination
      patterns/file-ownership.md for ownership rules
      quality/error-recovery.md for failure handling
    </depends_on>
    <provides_to>
      patterns/multi-agent.md for isolation mechanism
      patterns/session-management.md for worktree tracking
      commands/swarm.md for execution environment
    </provides_to>
  </integration_points>
  
</module>
```