# {{PROJECT_NAME}} - Workflow Orchestration Context
# Layer 4: Team Processes and Development Workflows
# Generated: {{GENERATION_TIMESTAMP}}
# Confidence: {{WORKFLOW_CONFIDENCE_SCORE}}

<!--
CONTEXT LAYER: Workflow Orchestration (Priority: 7, Token Budget: 1200)
PURPOSE: Captures team processes, development workflows, and operational procedures
DEPENDENCIES: Project Foundation, Domain Intelligence, Technical Architecture
PROVIDES: Process knowledge to integration layer
INHERITS: project_name, team_size, cultural_patterns, coding_patterns, testing_requirements
-->

## Development Workflow Overview

### Development Lifecycle
**Development Methodology**: {{DEVELOPMENT_METHODOLOGY}}
{{#if methodology_details}}
**Methodology Details**: {{methodology_details}}
{{/if}}

**Sprint/Iteration Cycle**: {{ITERATION_CYCLE}}
{{#if cycle_length}}
**Cycle Length**: {{cycle_length}}
{{/if}}

### Feature Development Process
{{#each FEATURE_DEVELOPMENT_STAGES}}
#### {{stage_number}}. {{stage_name}}
**Purpose**: {{stage_purpose}}
**Duration**: {{estimated_duration}}
**Responsible Role**: {{responsible_role}}

**Activities**:
{{#each activities}}
- {{this}}
{{/each}}

**Deliverables**:
{{#each deliverables}}
- {{this}}
{{/each}}

{{#if entry_criteria}}
**Entry Criteria**:
{{#each entry_criteria}}
- {{this}}
{{/each}}
{{/if}}

{{#if exit_criteria}}
**Exit Criteria**:
{{#each exit_criteria}}
- {{this}}
{{/each}}
{{/if}}

{{/each}}

### Branch Management & Git Workflow
**Git Workflow**: {{GIT_WORKFLOW}}
{{#if workflow_description}}
**Workflow Description**: {{workflow_description}}
{{/if}}

**Branch Types**:
{{#each BRANCH_TYPES}}
- **{{branch_type}}**: {{purpose}}
{{#if naming_convention}}
  - *Naming*: {{naming_convention}}
{{/if}}
{{#if merge_strategy}}
  - *Merge Strategy*: {{merge_strategy}}
{{/if}}
{{#if lifetime}}
  - *Lifetime*: {{lifetime}}
{{/if}}
{{/each}}

**Commit Standards**:
{{#if COMMIT_MESSAGE_FORMAT}}
**Message Format**: {{COMMIT_MESSAGE_FORMAT}}
{{#if commit_examples}}
**Examples**:
{{#each commit_examples}}
- {{this}}
{{/each}}
{{/if}}
{{/if}}

{{#if COMMIT_GUIDELINES}}
**Commit Guidelines**:
{{#each COMMIT_GUIDELINES}}
- {{this}}
{{/each}}
{{/if}}

### Task Tracking & Project Management
{{#if PROJECT_MANAGEMENT_TOOL}}
**Project Management Tool**: {{PROJECT_MANAGEMENT_TOOL}}
{{#if tool_configuration}}
**Configuration**: {{tool_configuration}}
{{/if}}
{{/if}}

**Task Categories**:
{{#each TASK_CATEGORIES}}
- **{{category_name}}**: {{category_description}}
{{#if priority_levels}}
  - *Priority Levels*: {{priority_levels}}
{{/if}}
{{#if estimation_approach}}
  - *Estimation*: {{estimation_approach}}
{{/if}}
{{/each}}

**Workflow States**:
{{#each WORKFLOW_STATES}}
{{state_number}}. **{{state_name}}**: {{state_description}}
{{#if state_criteria}}
   - *Criteria*: {{state_criteria}}
{{/if}}
{{#if responsible_role}}
   - *Owner*: {{responsible_role}}
{{/if}}
{{/each}}

## Quality Assurance Workflows

### Code Review Process
**Review Requirements**: {{CODE_REVIEW_REQUIREMENTS}}
{{#if review_tool}}
**Review Tool**: {{review_tool}}
{{/if}}

**Review Stages**:
{{#each CODE_REVIEW_STAGES}}
#### {{stage_name}}
**Reviewer Role**: {{reviewer_role}}
**Focus Areas**:
{{#each focus_areas}}
- {{this}}
{{/each}}

**Approval Criteria**:
{{#each approval_criteria}}
- {{this}}
{{/each}}

{{#if checklist}}
**Review Checklist**:
{{#each checklist}}
- [ ] {{this}}
{{/each}}
{{/if}}

{{/each}}

**Review Standards**:
{{#each REVIEW_STANDARDS}}
- **{{standard_category}}**: {{standard_description}}
{{#if examples}}
  - *Examples*: {{examples}}
{{/if}}
{{/each}}

### Testing Workflows & Automation
**Testing Strategy Integration**: {{TESTING_WORKFLOW_INTEGRATION}}

**Test Automation Pipeline**:
{{#each TEST_AUTOMATION_STAGES}}
{{stage_number}}. **{{stage_name}}**: {{stage_description}}
{{#if trigger_condition}}
   - *Triggered by*: {{trigger_condition}}
{{/if}}
{{#if tools}}
   - *Tools*: {{tools}}
{{/if}}
{{#if success_criteria}}
   - *Success Criteria*: {{success_criteria}}
{{/if}}
{{#if failure_action}}
   - *On Failure*: {{failure_action}}
{{/if}}
{{/each}}

**Manual Testing Procedures**:
{{#if MANUAL_TESTING_PROCEDURES}}
{{#each MANUAL_TESTING_PROCEDURES}}
#### {{procedure_name}}
**Frequency**: {{frequency}}
**Responsible Role**: {{responsible_role}}

**Steps**:
{{#each steps}}
{{step_number}}. {{step_description}}
{{#if expected_outcome}}
   - *Expected*: {{expected_outcome}}
{{/if}}
{{/each}}

{{/each}}
{{/if}}

### Quality Gates & Acceptance Criteria
**Quality Gates**:
{{#each QUALITY_GATES}}
#### {{gate_name}}
**Trigger Point**: {{trigger_point}}
**Criteria**:
{{#each criteria}}
- {{criterion}}
{{#if measurement}}
  - *Measurement*: {{measurement}}
{{/if}}
{{/each}}

**Approval Authority**: {{approval_authority}}
{{#if escalation_process}}
**Escalation**: {{escalation_process}}
{{/if}}

{{/each}}

## Deployment & Release Workflows

### Release Process
**Release Cadence**: {{RELEASE_CADENCE}}
{{#if release_planning}}
**Release Planning**: {{release_planning}}
{{/if}}

**Release Preparation**:
{{#each RELEASE_PREPARATION_STEPS}}
{{step_number}}. **{{step_name}}**: {{step_description}}
{{#if responsible_role}}
   - *Responsible*: {{responsible_role}}
{{/if}}
{{#if dependencies}}
   - *Dependencies*: {{dependencies}}
{{/if}}
{{#if validation}}
   - *Validation*: {{validation}}
{{/if}}
{{/each}}

### Deployment Procedures
**Deployment Strategy**: {{DEPLOYMENT_STRATEGY}}
{{#if deployment_windows}}
**Deployment Windows**: {{deployment_windows}}
{{/if}}

**Deployment Steps**:
{{#each DEPLOYMENT_STEPS}}
#### {{step_category}}
{{#each steps}}
{{step_number}}. {{step_description}}
{{#if verification}}
   - *Verification*: {{verification}}
{{/if}}
{{#if rollback_procedure}}
   - *Rollback*: {{rollback_procedure}}
{{/if}}
{{/each}}

{{/each}}

### Environment Management
**Environment Promotion**: {{ENVIRONMENT_PROMOTION_STRATEGY}}

**Environment Workflows**:
{{#each ENVIRONMENT_WORKFLOWS}}
#### {{environment_name}}
**Purpose**: {{purpose}}
**Access Control**: {{access_control}}

**Deployment Process**:
{{#each deployment_process}}
- {{this}}
{{/each}}

**Validation Requirements**:
{{#each validation_requirements}}
- {{this}}
{{/each}}

{{#if special_considerations}}
**Special Considerations**: {{special_considerations}}
{{/if}}

{{/each}}

## Team Collaboration Patterns

### Communication Standards
{{#if COMMUNICATION_TOOLS}}
**Primary Tools**:
{{#each COMMUNICATION_TOOLS}}
- **{{tool_name}}**: {{tool_usage}}
{{#if usage_guidelines}}
  - *Guidelines*: {{usage_guidelines}}
{{/if}}
{{/each}}
{{/if}}

**Communication Protocols**:
{{#each COMMUNICATION_PROTOCOLS}}
- **{{protocol_name}}**: {{protocol_description}}
{{#if usage_scenarios}}
  - *Used for*: {{usage_scenarios}}
{{/if}}
{{/each}}

### Meeting Cadence & Decision Processes
**Regular Meetings**:
{{#each REGULAR_MEETINGS}}
#### {{meeting_name}}
**Frequency**: {{frequency}}
**Duration**: {{duration}}
**Participants**: {{participants}}

**Agenda Structure**:
{{#each agenda_items}}
- {{this}}
{{/each}}

**Decision Process**: {{decision_process}}

{{/each}}

**Decision-Making Framework**:
{{#if DECISION_FRAMEWORK}}
{{#each DECISION_FRAMEWORK}}
#### {{decision_type}}
**Authority**: {{decision_authority}}
**Process**: {{decision_process}}
{{#if consultation_required}}
**Consultation Required**: {{consultation_required}}
{{/if}}
{{#if documentation_required}}
**Documentation**: {{documentation_required}}
{{/if}}

{{/each}}
{{/if}}

### Knowledge Sharing & Documentation
**Documentation Strategy**: {{DOCUMENTATION_STRATEGY}}
{{#if documentation_tools}}
**Documentation Tools**: {{documentation_tools}}
{{/if}}

**Knowledge Sharing Practices**:
{{#each KNOWLEDGE_SHARING_PRACTICES}}
- **{{practice_name}}**: {{practice_description}}
{{#if frequency}}
  - *Frequency*: {{frequency}}
{{/if}}
{{#if participants}}
  - *Participants*: {{participants}}
{{/if}}
{{/each}}

**Documentation Standards**:
{{#each DOCUMENTATION_STANDARDS}}
- **{{doc_type}}**: {{standard}}
{{#if update_frequency}}
  - *Update Frequency*: {{update_frequency}}
{{/if}}
{{#if owner}}
  - *Owner*: {{owner}}
{{/if}}
{{/each}}

## Operational Procedures

### Troubleshooting & Support Workflows
**Support Tiers**:
{{#each SUPPORT_TIERS}}
#### Tier {{tier_level}}: {{tier_name}}
**Responsibilities**:
{{#each responsibilities}}
- {{this}}
{{/each}}

**Escalation Criteria**:
{{#each escalation_criteria}}
- {{this}}
{{/each}}

{{#if response_time}}
**Response Time**: {{response_time}}
{{/if}}

{{/each}}

**Incident Response Process**:
{{#each INCIDENT_RESPONSE_STEPS}}
{{step_number}}. **{{step_name}}**: {{step_description}}
{{#if responsible_role}}
   - *Responsible*: {{responsible_role}}
{{/if}}
{{#if time_target}}
   - *Target Time*: {{time_target}}
{{/if}}
{{#if escalation_trigger}}
   - *Escalate if*: {{escalation_trigger}}
{{/if}}
{{/each}}

### Monitoring & Alerting Workflows
{{#if MONITORING_WORKFLOWS}}
**Monitoring Responsibilities**:
{{#each MONITORING_WORKFLOWS}}
#### {{monitoring_area}}
**Primary Monitor**: {{primary_monitor}}
**Backup Monitor**: {{backup_monitor}}

**Alert Conditions**:
{{#each alert_conditions}}
- **{{condition_name}}**: {{condition_criteria}}
  - *Action*: {{required_action}}
{{#if escalation_time}}
  - *Escalate after*: {{escalation_time}}
{{/if}}
{{/each}}

{{/each}}
{{/if}}

### Maintenance & Housekeeping
**Regular Maintenance Tasks**:
{{#each MAINTENANCE_TASKS}}
#### {{task_name}}
**Frequency**: {{frequency}}
**Responsible Role**: {{responsible_role}}

**Procedure**:
{{#each procedure}}
{{step_number}}. {{step_description}}
{{/each}}

{{#if validation_criteria}}
**Validation**: {{validation_criteria}}
{{/if}}

{{/each}}

---

## Context Inheritance Exports

This workflow context provides the following variables to child contexts:

**Workflow Procedure Variables**:
{{#each WORKFLOW_PROCEDURE_EXPORTS}}
- `{{procedure_name}}`: {{procedure_description}}
{{/each}}

**Quality Standard Variables**:
{{#each QUALITY_STANDARD_EXPORTS}}
- `{{standard_name}}`: {{standard_detail}}
{{/each}}

**Collaboration Pattern Variables**:
{{#each COLLABORATION_PATTERN_EXPORTS}}
- `{{pattern_name}}`: {{pattern_description}}
{{/each}}

**Operational Knowledge Variables**:
{{#each OPERATIONAL_KNOWLEDGE_EXPORTS}}
- `{{knowledge_area}}`: {{knowledge_detail}}
{{/each}}

---

*This context was generated from consultation stage 4 (Preference Learning) and team process analysis, providing workflow understanding for integration and operational implementation.*

<!-- VALIDATION CHECKPOINTS -->
<!-- ✓ Development workflow documented -->
<!-- ✓ Quality assurance processes defined -->
<!-- ✓ Deployment procedures established -->
<!-- ✓ Team collaboration patterns captured -->
<!-- ✓ Operational procedures documented -->

<!-- TOKEN BUDGET USAGE: Estimated {{ESTIMATED_TOKEN_COUNT}} tokens -->
<!-- CONFIDENCE SCORE: {{WORKFLOW_CONFIDENCE_SCORE}}/10 -->
<!-- LAST UPDATED: {{GENERATION_TIMESTAMP}} -->