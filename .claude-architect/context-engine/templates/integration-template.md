# {{PROJECT_NAME}} - Integration Mesh Context
# Layer 5: Cross-Cutting Concerns and System Interconnections
# Generated: {{GENERATION_TIMESTAMP}}
# Confidence: {{INTEGRATION_CONFIDENCE_SCORE}}

<!--
CONTEXT LAYER: Integration Mesh (Priority: 6, Token Budget: 800)
PURPOSE: Manages cross-cutting concerns and system interconnections
DEPENDENCIES: All previous layers (Project Foundation, Domain Intelligence, Technical Architecture, Workflow Orchestration)
PROVIDES: System-wide integration knowledge
INHERITS: project_name, domain_vocabulary, coding_patterns, workflow_procedures
-->

## Cross-Cutting Concerns

### Security Architecture
{{#if SECURITY_APPROACH}}
**Security Model**: {{SECURITY_APPROACH}}
{{#if security_frameworks}}
**Security Frameworks**: {{security_frameworks}}
{{/if}}
{{/if}}

**Security Patterns**:
{{#each SECURITY_PATTERNS}}
#### {{pattern_name}}
**Purpose**: {{purpose}}
**Implementation**: {{implementation}}
{{#if threat_mitigation}}
**Threats Mitigated**: {{threat_mitigation}}
{{/if}}

**Application Points**:
{{#each application_points}}
- {{this}}
{{/each}}

{{#if configuration}}
**Configuration**:
```{{config_format}}
{{configuration}}
```
{{/if}}

{{/each}}

**Security Requirements**:
{{#each SECURITY_REQUIREMENTS}}
- **{{requirement_category}}**: {{requirement_description}}
{{#if compliance_standards}}
  - *Standards*: {{compliance_standards}}
{{/if}}
{{#if validation_method}}
  - *Validation*: {{validation_method}}
{{/if}}
{{/each}}

### Logging & Observability Strategy
**Logging Architecture**: {{LOGGING_ARCHITECTURE}}
{{#if logging_centralization}}
**Centralization Approach**: {{logging_centralization}}
{{/if}}

**Log Categories & Levels**:
{{#each LOG_CATEGORIES}}
#### {{category_name}}
**Purpose**: {{purpose}}
**Log Level**: {{log_level}}
**Retention**: {{retention_policy}}

**Information Captured**:
{{#each captured_info}}
- {{this}}
{{/each}}

{{#if sensitive_data_handling}}
**Sensitive Data Handling**: {{sensitive_data_handling}}
{{/if}}

{{/each}}

**Structured Logging Format**:
{{#if STRUCTURED_LOGGING}}
**Format**: {{STRUCTURED_LOGGING.format}}
**Schema**:
```{{schema_format}}
{{STRUCTURED_LOGGING.schema}}
```

**Standard Fields**:
{{#each STRUCTURED_LOGGING.standard_fields}}
- **{{field_name}}**: {{field_description}}
{{/each}}
{{/if}}

### Monitoring & Metrics
**Monitoring Strategy**: {{MONITORING_STRATEGY}}
{{#if monitoring_tools}}
**Primary Tools**: {{monitoring_tools}}
{{/if}}

**Key Metrics Categories**:
{{#each METRICS_CATEGORIES}}
#### {{category_name}}
**Purpose**: {{purpose}}
**Collection Method**: {{collection_method}}

**Key Metrics**:
{{#each metrics}}
- **{{metric_name}}**: {{metric_description}}
{{#if threshold_values}}
  - *Thresholds*: {{threshold_values}}
{{/if}}
{{#if alert_conditions}}
  - *Alerts*: {{alert_conditions}}
{{/if}}
{{/each}}

{{/each}}

**Distributed Tracing**:
{{#if DISTRIBUTED_TRACING}}
**Tracing Strategy**: {{DISTRIBUTED_TRACING.strategy}}
{{#if tracing_tools}}
**Tools**: {{tracing_tools}}
{{/if}}

**Trace Correlation**:
{{#each DISTRIBUTED_TRACING.correlation_patterns}}
- **{{pattern_name}}**: {{pattern_description}}
{{/each}}
{{/if}}

## System Integration Architecture

### API Design & Interface Patterns
**API Architecture Style**: {{API_ARCHITECTURE_STYLE}}
{{#if api_standards}}
**Standards Compliance**: {{api_standards}}
{{/if}}

**Interface Patterns**:
{{#each INTERFACE_PATTERNS}}
#### {{pattern_name}}
**Use Cases**: {{use_cases}}
**Implementation**: {{implementation}}

**Contract Definition**:
```{{contract_format}}
{{contract_example}}
```

**Versioning Strategy**: {{versioning_strategy}}
{{#if backward_compatibility}}
**Backward Compatibility**: {{backward_compatibility}}
{{/if}}

{{/each}}

**API Quality Standards**:
{{#each API_QUALITY_STANDARDS}}
- **{{standard_category}}**: {{standard_description}}
{{#if validation_criteria}}
  - *Validation*: {{validation_criteria}}
{{/if}}
{{/each}}

### Message Passing & Event Handling
{{#if MESSAGING_ARCHITECTURE}}
**Messaging Architecture**: {{MESSAGING_ARCHITECTURE}}
{{#if messaging_tools}}
**Messaging Tools**: {{messaging_tools}}
{{/if}}

**Message Patterns**:
{{#each MESSAGE_PATTERNS}}
#### {{pattern_name}}
**Purpose**: {{purpose}}
**Message Flow**: {{message_flow}}

**Message Structure**:
```{{message_format}}
{{message_schema}}
```

**Delivery Guarantees**: {{delivery_guarantees}}
{{#if error_handling}}
**Error Handling**: {{error_handling}}
{{/if}}

{{/each}}
{{/if}}

**Event-Driven Patterns**:
{{#if EVENT_PATTERNS}}
{{#each EVENT_PATTERNS}}
#### {{event_type}}
**Trigger Conditions**: {{trigger_conditions}}
**Event Payload**: {{event_payload}}

**Consumers**:
{{#each consumers}}
- **{{consumer_name}}**: {{consumer_action}}
{{/each}}

**Processing Guarantees**: {{processing_guarantees}}

{{/each}}
{{/if}}

### Data Synchronization & Consistency
**Consistency Model**: {{CONSISTENCY_MODEL}}
{{#if consistency_tools}}
**Supporting Tools**: {{consistency_tools}}
{{/if}}

**Synchronization Patterns**:
{{#each SYNCHRONIZATION_PATTERNS}}
#### {{pattern_name}}
**Scope**: {{scope}}
**Synchronization Method**: {{sync_method}}
**Conflict Resolution**: {{conflict_resolution}}

**Implementation**:
{{implementation_details}}

{{#if performance_impact}}
**Performance Impact**: {{performance_impact}}
{{/if}}

{{/each}}

**Data Consistency Rules**:
{{#each DATA_CONSISTENCY_RULES}}
- **{{rule_category}}**: {{rule_description}}
{{#if validation_method}}
  - *Validation*: {{validation_method}}
{{/if}}
{{#if violation_handling}}
  - *Violation Handling*: {{violation_handling}}
{{/if}}
{{/each}}

## External Dependencies & Integration Points

### Third-Party Service Integrations
{{#each EXTERNAL_INTEGRATIONS}}
#### {{service_name}}
**Purpose**: {{integration_purpose}}
**Integration Type**: {{integration_type}}
**Criticality**: {{criticality_level}}

**Connection Details**:
- **Protocol**: {{protocol}}
- **Authentication**: {{authentication_method}}
{{#if rate_limits}}
- **Rate Limits**: {{rate_limits}}
{{/if}}
{{#if sla_requirements}}
- **SLA Requirements**: {{sla_requirements}}
{{/if}}

**Data Exchange**:
{{#if outbound_data}}
- **Outbound**: {{outbound_data}}
{{/if}}
{{#if inbound_data}}
- **Inbound**: {{inbound_data}}
{{/if}}

**Error Handling Strategy**:
{{#each error_scenarios}}
- **{{scenario}}**: {{handling_approach}}
{{/each}}

**Monitoring & Health Checks**:
{{#each health_checks}}
- {{this}}
{{/each}}

{{/each}}

### External API Usage Patterns
**API Client Architecture**: {{API_CLIENT_ARCHITECTURE}}
{{#if client_libraries}}
**Client Libraries**: {{client_libraries}}
{{/if}}

**Usage Patterns**:
{{#each API_USAGE_PATTERNS}}
#### {{pattern_name}}
**Use Cases**: {{use_cases}}
**Implementation Approach**: {{implementation}}

**Retry Logic**:
{{#if retry_strategy}}
- **Strategy**: {{retry_strategy}}
- **Max Attempts**: {{max_attempts}}
- **Backoff**: {{backoff_strategy}}
{{/if}}

**Caching Strategy**:
{{#if caching_approach}}
- **Approach**: {{caching_approach}}
- **TTL**: {{cache_ttl}}
- **Invalidation**: {{cache_invalidation}}
{{/if}}

{{/each}}

### Dependency Management Strategy
**Dependency Philosophy**: {{DEPENDENCY_PHILOSOPHY}}

**Dependency Categories**:
{{#each DEPENDENCY_CATEGORIES}}
- **{{category_name}}**: {{management_approach}}
{{#if update_strategy}}
  - *Update Strategy*: {{update_strategy}}
{{/if}}
{{#if risk_mitigation}}
  - *Risk Mitigation*: {{risk_mitigation}}
{{/if}}
{{/each}}

**Vendor Lock-in Mitigation**:
{{#if VENDOR_LOCKIN_MITIGATION}}
{{#each VENDOR_LOCKIN_MITIGATION}}
- **{{service_category}}**: {{mitigation_strategy}}
{{/each}}
{{/if}}

## Resilience & Recovery Patterns

### Error Handling Strategies
**Global Error Handling**: {{GLOBAL_ERROR_HANDLING}}

**Error Classification & Response**:
{{#each ERROR_CLASSIFICATIONS}}
#### {{error_class}}
**Examples**: {{error_examples}}
**Response Strategy**: {{response_strategy}}
**User Impact**: {{user_impact}}

**Handling Approach**:
{{#each handling_steps}}
{{step_number}}. {{step_description}}
{{/each}}

{{#if escalation_criteria}}
**Escalation Criteria**: {{escalation_criteria}}
{{/if}}

{{/each}}

### Circuit Breaker & Retry Patterns
{{#if CIRCUIT_BREAKER_PATTERNS}}
**Circuit Breaker Implementation**: {{CIRCUIT_BREAKER_PATTERNS.implementation}}

**Circuit Breaker Configurations**:
{{#each CIRCUIT_BREAKER_PATTERNS.configurations}}
#### {{service_name}}
- **Failure Threshold**: {{failure_threshold}}
- **Recovery Time**: {{recovery_time}}
- **Half-Open Trial**: {{half_open_trial}}

**Fallback Strategy**: {{fallback_strategy}}

{{/each}}
{{/if}}

**Retry Strategies**:
{{#each RETRY_STRATEGIES}}
#### {{strategy_name}}
**Applicable Scenarios**: {{applicable_scenarios}}
**Retry Logic**:
- **Max Attempts**: {{max_attempts}}
- **Backoff Strategy**: {{backoff_strategy}}
- **Jitter**: {{jitter_approach}}

**Success Criteria**: {{success_criteria}}
**Abort Conditions**: {{abort_conditions}}

{{/each}}

### Disaster Recovery Procedures
**Recovery Strategy**: {{DISASTER_RECOVERY_STRATEGY}}
{{#if recovery_tools}}
**Recovery Tools**: {{recovery_tools}}
{{/if}}

**Recovery Scenarios**:
{{#each RECOVERY_SCENARIOS}}
#### {{scenario_name}}
**Scenario Description**: {{scenario_description}}
**Impact Assessment**: {{impact_assessment}}

**Recovery Steps**:
{{#each recovery_steps}}
{{step_number}}. **{{step_name}}**: {{step_description}}
{{#if estimated_time}}
   - *Estimated Time*: {{estimated_time}}
{{/if}}
{{#if responsible_role}}
   - *Responsible*: {{responsible_role}}
{{/if}}
{{#if validation}}
   - *Validation*: {{validation}}
{{/if}}
{{/each}}

**Recovery Time Objective**: {{rto}}
**Recovery Point Objective**: {{rpo}}

{{/each}}

---

## Context Inheritance Exports

This integration context provides the following variables to child contexts:

**Integration Pattern Variables**:
{{#each INTEGRATION_PATTERN_EXPORTS}}
- `{{pattern_name}}`: {{pattern_description}}
{{/each}}

**Security Requirement Variables**:
{{#each SECURITY_REQUIREMENT_EXPORTS}}
- `{{requirement_type}}`: {{requirement_detail}}
{{/each}}

**Monitoring Standard Variables**:
{{#each MONITORING_STANDARD_EXPORTS}}
- `{{standard_name}}`: {{standard_detail}}
{{/each}}

**Error Handling Approach Variables**:
{{#each ERROR_HANDLING_EXPORTS}}
- `{{approach_name}}`: {{approach_description}}
{{/each}}

---

*This context was generated from cross-cutting concerns analysis across all consultation stages and provides system-wide integration understanding for comprehensive project context.*

<!-- VALIDATION CHECKPOINTS -->
<!-- ✓ Cross-cutting concerns documented -->
<!-- ✓ System integration patterns defined -->
<!-- ✓ External dependencies mapped -->
<!-- ✓ Resilience strategies established -->
<!-- ✓ Recovery procedures documented -->

<!-- TOKEN BUDGET USAGE: Estimated {{ESTIMATED_TOKEN_COUNT}} tokens -->
<!-- CONFIDENCE SCORE: {{INTEGRATION_CONFIDENCE_SCORE}}/10 -->
<!-- LAST UPDATED: {{GENERATION_TIMESTAMP}} -->