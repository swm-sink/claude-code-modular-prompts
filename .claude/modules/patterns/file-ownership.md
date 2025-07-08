| version | last_updated | status |
|---------|--------------|--------|
| 1.0.0   | 2025-07-08   | stable |

# File Ownership Module

────────────────────────────────────────────────────────────────────────────────

```xml
<module name="file_ownership" category="patterns">
  
  <purpose>
    Define and enforce file ownership patterns for multi-agent coordination to prevent conflicts
  </purpose>
  
  <thinking_pattern enforcement="MANDATORY">
    <step>1. Analyze agent type and determine ownership domains</step>
    <step>2. Map file paths to appropriate ownership patterns</step>
    <step>3. Check for conflicts before file operations</step>
    <step>4. Enforce ownership rules during execution</step>
    <step>5. Coordinate handoffs between agents when needed</step>
    <step>6. Track ownership changes and audit access</step>
  </thinking_pattern>
  
  <implementation>
    
    <phase name="ownership_analysis" order="1">
      <requirements>
        Agent type identified and ownership domains defined
        File patterns mapped to ownership rules
        Conflict detection mechanisms in place
      </requirements>
      <actions>
        Identify agent type from task assignment
        Load ownership patterns for agent type
        Map working files to ownership domains
        Detect potential conflicts early
      </actions>
      <validation>
        Agent ownership domains clearly defined
        File mappings unambiguous
        Conflict detection operational
      </validation>
    </phase>
    
    <phase name="access_control" order="2">
      <requirements>
        File access controlled by ownership rules
        Violations detected and prevented
        Exceptions handled appropriately
      </requirements>
      <actions>
        Enforce read/write permissions by ownership
        Block unauthorized modifications
        Log access attempts for audit
        Handle shared file coordination
      </actions>
      <validation>
        Access rules properly enforced
        No unauthorized modifications
        Audit trail complete
      </validation>
    </phase>
    
    <phase name="conflict_resolution" order="3">
      <requirements>
        Conflicts detected before they occur
        Resolution strategies applied automatically
        Handoffs coordinated smoothly
      </requirements>
      <actions>
        Detect concurrent access attempts
        Apply appropriate resolution strategy
        Coordinate ownership transfers
        Document conflict resolutions
      </actions>
      <validation>
        All conflicts resolved appropriately
        No data loss or corruption
        Coordination successful
      </validation>
    </phase>
    
  </implementation>
  
  <ownership_domains>
    <backend_agent domain="backend">
      <owned_paths>
        /api/**/*.{js,ts,py,java,go,rs}
        /backend/**/*
        /server/**/*
        /services/**/*
        /models/**/*
        /database/**/*
        /migrations/**/*
      </owned_paths>
      <shared_paths>
        /config/*.{json,yaml,toml}
        /docker-compose.yml
        /.env.example
      </shared_paths>
      <read_only>
        /frontend/**/*
        /docs/**/*
        /tests/e2e/**/*
      </read_only>
    </backend_agent>
    
    <frontend_agent domain="frontend">
      <owned_paths>
        /frontend/**/*.{js,jsx,ts,tsx}
        /src/**/*.{js,jsx,ts,tsx}
        /components/**/*
        /pages/**/*
        /styles/**/*
        /public/**/*
        /assets/**/*
      </owned_paths>
      <shared_paths>
        /package.json
        /tsconfig.json
        /.eslintrc.*
      </shared_paths>
      <read_only>
        /api/**/*
        /backend/**/*
        /docs/**/*
      </read_only>
    </frontend_agent>
    
    <devops_agent domain="infrastructure">
      <owned_paths>
        /.github/workflows/**/*
        /kubernetes/**/*
        /terraform/**/*
        /ansible/**/*
        /scripts/deploy/**/*
        /docker/**/*
        Dockerfile*
      </owned_paths>
      <shared_paths>
        /docker-compose.yml
        /.env.example
        /config/environments/**/*
      </shared_paths>
      <read_only>
        /src/**/*
        /api/**/*
        /frontend/**/*
      </read_only>
    </devops_agent>
    
    <test_agent domain="testing">
      <owned_paths>
        /tests/**/*
        /test/**/*
        /__tests__/**/*
        /spec/**/*
        /cypress/**/*
        /e2e/**/*
        /.jest/**/*
      </owned_paths>
      <shared_paths>
        /jest.config.*
        /cypress.config.*
        /playwright.config.*
      </shared_paths>
      <read_only>
        ALL - Test agents read all code
      </read_only>
    </test_agent>
    
    <docs_agent domain="documentation">
      <owned_paths>
        /docs/**/*
        /documentation/**/*
        README.md
        CONTRIBUTING.md
        CHANGELOG.md
        /examples/**/*
      </owned_paths>
      <shared_paths>
        /api/openapi.yaml
        /graphql/schema.graphql
      </shared_paths>
      <read_only>
        ALL - Docs agents read all code
      </read_only>
    </docs_agent>
  </ownership_domains>
  
  <conflict_detection>
    <pre_operation_checks>
      <ownership_verification>
        Check if file is owned by current agent
        Verify no other agent has lock
        Confirm operation is permitted
      </ownership_verification>
      
      <concurrent_access_detection>
        Check for active locks on files
        Detect ongoing modifications
        Identify potential race conditions
      </concurrent_access_detection>
      
      <dependency_analysis>
        Check if changes affect other domains
        Identify cross-domain dependencies
        Plan coordination if needed
      </dependency_analysis>
    </pre_operation_checks>
    
    <conflict_types>
      <ownership_violation>
        Agent attempting to modify non-owned file
        Resolution: Block and request handoff
      </ownership_violation>
      
      <concurrent_modification>
        Multiple agents modifying same file
        Resolution: Lock-based coordination
      </concurrent_modification>
      
      <dependency_conflict>
        Changes break other agent's domain
        Resolution: Coordinated update
      </dependency_conflict>
      
      <shared_file_conflict>
        Competing changes to shared file
        Resolution: Merge or sequence updates
      </shared_file_conflict>
    </conflict_types>
  </conflict_detection>
  
  <coordination_protocols>
    <ownership_transfer>
      <request_handoff>
        Agent requests ownership transfer
        Current owner approves/denies
        Transfer logged and tracked
      </request_handoff>
      
      <temporary_access>
        Agent requests temporary write access
        Time-limited permission granted
        Automatic reversion after timeout
      </temporary_access>
      
      <shared_editing>
        Multiple agents coordinate on shared file
        Changes queued and applied in order
        Merge conflicts resolved automatically
      </shared_editing>
    </ownership_transfer>
    
    <lock_management>
      <file_locks>
        Exclusive locks for owned files
        Shared locks for read operations
        Timeout-based lock release
      </file_locks>
      
      <directory_locks>
        Lock entire directories during bulk operations
        Prevent nested conflicts
        Recursive lock management
      </directory_locks>
      
      <global_locks>
        System-wide locks for critical operations
        Migration and deployment locks
        Maintenance mode enforcement
      </global_locks>
    </lock_management>
  </coordination_protocols>
  
  <permission_matrix>
    ```yaml
    # Permission Matrix Format
    # O: Owner (full control)
    # W: Write (modify allowed)
    # R: Read (view only)
    # X: Execute (run/deploy)
    # -: No access
    
    Domains:
      Backend:
        /api:          O
        /frontend:     R
        /tests:        W
        /docs:         R
        /devops:       R
        
      Frontend:
        /api:          R
        /frontend:     O
        /tests:        W
        /docs:         R
        /devops:       R
        
      DevOps:
        /api:          X
        /frontend:     X
        /tests:        X
        /docs:         R
        /devops:       O
        
      Testing:
        /api:          R
        /frontend:     R
        /tests:        O
        /docs:         R
        /devops:       R
        
      Documentation:
        /api:          R
        /frontend:     R
        /tests:        R
        /docs:         O
        /devops:       R
    ```
  </permission_matrix>
  
  <audit_and_compliance>
    <access_logging>
      <log_format>
        timestamp: ISO-8601
        agent: agent-type-id
        operation: read|write|execute
        file: /path/to/file
        result: success|denied|error
        reason: ownership|permission|lock
      </log_format>
      
      <retention>
        Keep logs for 30 days
        Archive for compliance
        Searchable by agent/file/time
      </retention>
    </access_logging>
    
    <violation_tracking>
      <violation_types>
        Unauthorized access attempts
        Ownership rule violations
        Lock timeout violations
        Conflict resolution failures
      </violation_types>
      
      <reporting>
        Real-time violation alerts
        Daily summary reports
        Pattern analysis for improvements
      </reporting>
    </violation_tracking>
  </audit_and_compliance>
  
  <integration_points>
    <depends_on>
      patterns/multi-agent.md for agent coordination
      quality/error-recovery.md for conflict recovery
    </depends_on>
    <provides_to>
      patterns/multi-agent.md for ownership rules
      patterns/session-management.md for conflict tracking
      quality/production-standards.md for access control
    </provides_to>
  </integration_points>
  
</module>
```