| version | last_updated | status |
|---------|--------------|--------|
| 1.0.0   | 2025-07-11   | stable |

# Decision Artifacts Module

────────────────────────────────────────────────────────────────────────────────


────────────────────────────────────────────────────────────────────────────────

```xml
<module name="decision_artifacts" category="context">
  
  <purpose>
    Define structured schemas and formats for capturing, storing, and validating architectural and implementation decisions in multi-agent workflows.
  </purpose>
  
  <thinking_pattern enforcement="MANDATORY">
    <step>1. Determine decision type and categorization</step>
    <step>2. Apply appropriate schema template</step>
    <step>3. Validate required fields and dependencies</step>
    <step>4. Store with immutability and audit trail</step>
    <step>5. Enable decision acknowledgment workflows</step>
    <step>6. Verify decision consistency across agents</step>
  </thinking_pattern>
  
  <implementation>
    
    <phase name="decision_schema_definition" order="1">
      <requirements>
        Standardized JSON schema for all decision types
        Immutability markers for critical architectural decisions
        Version tracking and change history for evolving decisions
        Cross-reference capabilities for decision dependencies
      </requirements>
      <actions>
        Define core decision artifact schema with required fields
        Create category-specific schemas for different decision types
        Establish immutability rules and change approval workflows
        Implement decision dependency tracking and validation
      </actions>
      <validation>
        Schema validates all decision artifacts correctly
        Immutability constraints properly enforced
        Version history maintains complete audit trail
        Dependencies accurately tracked and verified
      </validation>
    </phase>
    
    <phase name="decision_storage_management" order="2">
      <requirements>
        Centralized decision registry accessible to all agents
        Atomic operations for decision creation and updates
        Conflict detection and resolution mechanisms
        Backup and recovery capabilities for decision data
      </requirements>
      <actions>
        Create centralized registry at .claude/swarm-decisions/
        Implement atomic operations for decision management
        Build conflict detection algorithms for competing decisions
        Establish backup procedures and recovery protocols
      </actions>
      <validation>
        Registry accessible and operational for all agents
        Decision operations complete atomically without corruption
        Conflicts detected and flagged for manual resolution
        Backup procedures tested and recovery verified
      </validation>
    </phase>
    
    <phase name="acknowledgment_workflow" order="3">
      <requirements>
        Agent acknowledgment tracking for decision compliance
        Notification system for decision updates and conflicts
        Validation workflows for decision implementation
        Audit trails for compliance and governance requirements
      </requirements>
      <actions>
        Build acknowledgment tracking system for agent compliance
        Create notification mechanisms for decision changes
        Implement validation workflows for implementation verification
        Generate audit reports for compliance documentation
      </actions>
      <validation>
        Acknowledgments properly tracked and verified
        Notifications sent and received by affected agents
        Implementation validation confirms decision adherence
        Audit trails complete and compliant with requirements
      </validation>
    </phase>
    
  </implementation>
  
  <decision_artifact_schema>
    <core_schema>
</module>
</decision_artifact_schema>
</core_schema>
      ```json
      {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "type": "object",
        "required": [
          "decision_id",
          "decision_summary",
          "owner_agent",
          "category",
          "rationale",
          "impacts",
          "immutable",
          "timestamp",
          "status"
        ],
        "properties": {
          "decision_id": {
            "type": "string",
            "pattern": "^[A-Z]+_[0-9]{3}$",
            "description": "Unique identifier (e.g., AUTH_001, DB_003)"
          },
          "decision_summary": {
            "type": "string",
            "maxLength": 100,
            "description": "One-line summary of the decision"
          },
          "owner_agent": {
            "type": "string",
            "enum": ["security_expert", "backend_developer", "frontend_developer", "devops_engineer", "system_architect", "performance_engineer"],
            "description": "Agent responsible for this decision"
          },
          "category": {
            "type": "string",
            "enum": ["authentication", "authorization", "data_models", "api_contracts", "security_policies", "performance_specs", "deployment", "infrastructure"],
            "description": "Decision category for organization"
          },
          "rationale": {
            "type": "string",
            "description": "Detailed explanation of why this decision was made"
          },
          "alternatives_considered": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "alternative": {"type": "string"},
                "pros": {"type": "array", "items": {"type": "string"}},
                "cons": {"type": "array", "items": {"type": "string"}},
                "rejection_reason": {"type": "string"}
              }
            },
            "description": "Alternative approaches considered and why they were rejected"
          },
          "impacts": {
            "type": "array",
            "items": {"type": "string"},
            "description": "List of agents or components affected by this decision"
          },
          "technical_constraints": {
            "type": "array",
            "items": {"type": "string"},
            "description": "Technical limitations or requirements imposed by this decision"
          },
          "dependencies": {
            "type": "array",
            "items": {"type": "string"},
            "description": "Other decisions this depends on"
          },
          "dependents": {
            "type": "array",
            "items": {"type": "string"},
            "description": "Decisions that depend on this one"
          },
          "immutable": {
            "type": "boolean",
            "description": "Whether this decision can be changed after implementation"
          },
          "timestamp": {
            "type": "string",
            "format": "date-time",
            "description": "When this decision was made"
          },
          "status": {
            "type": "string",
            "enum": ["proposed", "approved", "implemented", "superseded"],
            "description": "Current status of the decision"
          },
          "acknowledgments": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "agent": {"type": "string"},
                "timestamp": {"type": "string", "format": "date-time"},
                "notes": {"type": "string"}
              }
            },
            "description": "Agents who have acknowledged this decision"
          },
          "implementation_notes": {
            "type": "string",
            "description": "Notes about how this decision was implemented"
          },
          "validation_criteria": {
            "type": "array",
            "items": {"type": "string"},
            "description": "How to verify this decision was implemented correctly"
          },
          "change_history": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "timestamp": {"type": "string", "format": "date-time"},
                "agent": {"type": "string"},
                "change_type": {"type": "string", "enum": ["created", "modified", "acknowledged", "implemented", "superseded"]},
                "description": {"type": "string"},
                "previous_value": {"type": "string"}
              }
            },
            "description": "Complete history of changes to this decision"
          }
        }
      }
      ```
    </core_schema>
    
    <category_schemas>
      <authentication_schema>
        ```json
        {
          "allOf": [
            {"$ref": "#/definitions/core_decision"},
            {
              "properties": {
                "category": {"const": "authentication"},
                "auth_method": {
                  "type": "string",
                  "enum": ["jwt", "oauth2", "saml", "basic", "api_key", "mutual_tls"]
                },
                "token_expiry": {"type": "string"},
                "refresh_strategy": {"type": "string"},
                "session_management": {"type": "string"},
                "multi_factor": {"type": "boolean"},
                "identity_providers": {"type": "array", "items": {"type": "string"}}
              }
            }
          ]
        }
        ```
      </authentication_schema>
      
      <database_schema>
        ```json
        {
          "allOf": [
            {"$ref": "#/definitions/core_decision"},
            {
              "properties": {
                "category": {"const": "data_models"},
                "database_type": {
                  "type": "string",
                  "enum": ["postgresql", "mysql", "mongodb", "redis", "elasticsearch"]
                },
                "schema_changes": {"type": "array", "items": {"type": "string"}},
                "migration_strategy": {"type": "string"},
                "indexing_strategy": {"type": "array", "items": {"type": "string"}},
                "data_retention": {"type": "string"},
                "backup_strategy": {"type": "string"}
              }
            }
          ]
        }
        ```
      </database_schema>
      
      <api_schema>
        ```json
        {
          "allOf": [
            {"$ref": "#/definitions/core_decision"},
            {
              "properties": {
                "category": {"const": "api_contracts"},
                "api_style": {
                  "type": "string",
                  "enum": ["rest", "graphql", "grpc", "websocket"]
                },
                "versioning_strategy": {"type": "string"},
                "request_format": {"type": "string"},
                "response_format": {"type": "string"},
                "error_handling": {"type": "string"},
                "rate_limiting": {"type": "object"},
                "documentation_format": {"type": "string"}
              }
            }
          ]
        }
        ```
      </api_schema>
    </category_schemas>
  </decision_artifact_schema>
  
  <decision_categories>
    <authentication>
      <prefix>AUTH_</prefix>
      <description>Login methods, session management, token handling</description>
      <immutable_by_default>true</immutable_by_default>
      <required_acknowledgments>["backend_developer", "frontend_developer", "devops_engineer"]</required_acknowledgments>
    </authentication>
    
    <authorization>
      <prefix>AUTHZ_</prefix>
      <description>Permissions, RBAC, access control policies</description>
      <immutable_by_default>true</immutable_by_default>
      <required_acknowledgments>["backend_developer", "frontend_developer"]</required_acknowledgments>
    </authorization>
    
    <data_models>
      <prefix>DB_</prefix>
      <description>Database schema, relationships, migrations</description>
      <immutable_by_default>false</immutable_by_default>
      <required_acknowledgments>["backend_developer"]</required_acknowledgments>
    </data_models>
    
    <api_contracts>
      <prefix>API_</prefix>
      <description>Endpoint design, request/response formats</description>
      <immutable_by_default>false</immutable_by_default>
      <required_acknowledgments>["frontend_developer", "backend_developer"]</required_acknowledgments>
    </api_contracts>
    
    <security_policies>
      <prefix>SEC_</prefix>
      <description>Security requirements, threat mitigations</description>
      <immutable_by_default>true</immutable_by_default>
      <required_acknowledgments>["backend_developer", "frontend_developer", "devops_engineer"]</required_acknowledgments>
    </security_policies>
    
    <performance_specs>
      <prefix>PERF_</prefix>
      <description>Response times, scalability requirements</description>
      <immutable_by_default>false</immutable_by_default>
      <required_acknowledgments>["backend_developer", "frontend_developer"]</required_acknowledgments>
    </performance_specs>
    
    <deployment>
      <prefix>DEPLOY_</prefix>
      <description>Infrastructure, CI/CD, monitoring</description>
      <immutable_by_default>false</immutable_by_default>
      <required_acknowledgments>["devops_engineer"]</required_acknowledgments>
    </deployment>
  </decision_categories>
  
  <decision_precedence_rules>
    <security_first>
      All AUTH_, AUTHZ_, and SEC_ decisions must be finalized before implementation begins
    </security_first>
    <dependency_ordering>
      Decisions with dependencies must acknowledge all prerequisite decisions
    </dependency_ordering>
    <immutable_protection>
      Immutable decisions require unanimous consent from all impacted agents to change
    </immutable_protection>
    <conflict_escalation>
      Conflicting decisions automatically escalate to session for resolution
    </conflict_escalation>
  </decision_precedence_rules>
  
  <registry_operations>
    <create_decision>
      ```bash
      # Create new decision with validation
      create_decision() {
        local decision_data="$1"
        local session_id="$2"
        
        # Validate against schema
        echo "$decision_data" | jq -e . > /dev/null || {
          echo "ERROR: Invalid JSON format"
          return 1
        }
        
        # Extract decision ID and check for duplicates
        local decision_id=$(echo "$decision_data" | jq -r '.decision_id')
        local registry_file=".claude/swarm-decisions/session-${session_id}.json"
        
        if [[ -f "$registry_file" ]] && jq -e ".decisions[] | select(.decision_id == \"$decision_id\")" "$registry_file" > /dev/null; then
          echo "ERROR: Decision $decision_id already exists"
          return 1
        fi
        
        # Add timestamp and initial change history
        local timestamped_decision=$(echo "$decision_data" | jq ". + {
          timestamp: now | strftime(\"%Y-%m-%dT%H:%M:%SZ\"),
          change_history: [{
            timestamp: now | strftime(\"%Y-%m-%dT%H:%M:%SZ\"),
            agent: .owner_agent,
            change_type: \"created\",
            description: \"Initial decision creation\"
          }]
        }")
        
        # Append to registry
        if [[ -f "$registry_file" ]]; then
          jq ".decisions += [$timestamped_decision]" "$registry_file" > "${registry_file}.tmp" && mv "${registry_file}.tmp" "$registry_file"
        else
          mkdir -p "$(dirname "$registry_file")"
          jq -n "{decisions: [$timestamped_decision]}" > "$registry_file"
        fi
        
        echo "Decision $decision_id created successfully"
      }
      ```
    </create_decision>
    
    <acknowledge_decision>
      ```bash
      # Acknowledge existing decision
      acknowledge_decision() {
        local decision_id="$1"
        local agent="$2"
        local notes="$3"
        local session_id="$4"
        
        local registry_file=".claude/swarm-decisions/session-${session_id}.json"
        
        # Check if decision exists
        if ! jq -e ".decisions[] | select(.decision_id == \"$decision_id\")" "$registry_file" > /dev/null; then
          echo "ERROR: Decision $decision_id not found"
          return 1
        fi
        
        # Add acknowledgment
        local acknowledgment=$(jq -n "{
          agent: \"$agent\",
          timestamp: now | strftime(\"%Y-%m-%dT%H:%M:%SZ\"),
          notes: \"$notes\"
        }")
        
        jq "(.decisions[] | select(.decision_id == \"$decision_id\") | .acknowledgments) += [$acknowledgment] |
            (.decisions[] | select(.decision_id == \"$decision_id\") | .change_history) += [{
              timestamp: now | strftime(\"%Y-%m-%dT%H:%M:%SZ\"),
              agent: \"$agent\",
              change_type: \"acknowledged\",
              description: \"Decision acknowledged by $agent\"
            }]" "$registry_file" > "${registry_file}.tmp" && mv "${registry_file}.tmp" "$registry_file"
        
        echo "Decision $decision_id acknowledged by $agent"
      }
      ```
    </acknowledge_decision>
    
    <validate_decision_consistency>
      ```bash
      # Validate all decisions are consistent
      validate_decision_consistency() {
        local session_id="$1"
        local registry_file=".claude/swarm-decisions/session-${session_id}.json"
        
        if [[ ! -f "$registry_file" ]]; then
          echo "ERROR: No decision registry found"
          return 1
        fi
        
        # Check for conflicting decisions
        local conflicts=$(jq -r '
          .decisions as $decisions |
          [
            $decisions[] as $d1 |
            $decisions[] as $d2 |
            if ($d1.decision_id < $d2.decision_id) and 
               ($d1.category == $d2.category) and
               ($d1 | .technical_constraints | intersect($d2.technical_constraints) | length > 0)
            then "CONFLICT: \($d1.decision_id) and \($d2.decision_id) have conflicting constraints"
            else empty
            end
          ] | unique[]
        ' "$registry_file")
        
        if [[ -n "$conflicts" ]]; then
          echo "Decision conflicts detected:"
          echo "$conflicts"
          return 1
        fi
        
        # Check for missing acknowledgments
        local missing_acks=$(jq -r '
          .decisions[] |
          select(.status == "approved" or .status == "implemented") |
          . as $decision |
          (
            if .category == "authentication" or .category == "authorization" or .category == "security_policies"
            then ["backend_developer", "frontend_developer", "devops_engineer"]
            elif .category == "api_contracts"
            then ["frontend_developer", "backend_developer"]
            elif .category == "data_models"
            then ["backend_developer"]
            elif .category == "deployment"
            then ["devops_engineer"]
            else []
            end
          ) as $required |
          $required[] as $agent |
          if ($decision.acknowledgments | map(.agent) | contains([$agent]) | not)
          then "MISSING: \($decision.decision_id) requires acknowledgment from \($agent)"
          else empty
          end
        ' "$registry_file")
        
        if [[ -n "$missing_acks" ]]; then
          echo "Missing acknowledgments detected:"
          echo "$missing_acks"
          return 1
        fi
        
        echo "All decisions are consistent and properly acknowledged"
        return 0
      }
      ```
    </validate_decision_consistency>
  </registry_operations>
  
  <integration_points>
    <depends_on>
      patterns/session-management.md for session context
      patterns/multi-agent.md for agent coordination
    </depends_on>
    <provides_to>
      patterns/multi-agent.md for decision coordination
      patterns/session-storage.md for decision persistence
      patterns/conflict-resolution.md for decision conflicts
    </provides_to>
  </integration_points>
  
</module>
```