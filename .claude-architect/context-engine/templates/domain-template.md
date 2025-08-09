# {{PROJECT_NAME}} - Domain Intelligence Context
# Layer 2: Business Domain Expertise and Terminology
# Generated: {{GENERATION_TIMESTAMP}}
# Confidence: {{DOMAIN_CONFIDENCE_SCORE}}

<!--
CONTEXT LAYER: Domain Intelligence (Priority: 9, Token Budget: 1500)
PURPOSE: Captures business domain expertise and terminology
DEPENDENCIES: Project Foundation Context
PROVIDES: Domain expertise to technical and workflow layers
INHERITS: project_name, domain_context, core_constraints
-->

## Domain Overview

### Business Context
**Industry/Domain**: {{BUSINESS_DOMAIN}}
**Market Segment**: {{MARKET_SEGMENT}}
{{#if INDUSTRY_BACKGROUND}}
**Industry Background**: {{INDUSTRY_BACKGROUND}}
{{/if}}

### Core Domain Concepts
{{#each CORE_DOMAIN_CONCEPTS}}
#### {{concept_name}}
{{concept_description}}
{{#if concept_relationships}}
**Related Concepts**: {{concept_relationships}}
{{/if}}
{{#if concept_importance}}
**Business Importance**: {{concept_importance}}
{{/if}}

{{/each}}

### Key Stakeholders
{{#each KEY_STAKEHOLDERS}}
- **{{stakeholder_type}}**: {{description}}
{{#if needs}}
  - *Primary Needs*: {{needs}}
{{/if}}
{{#if pain_points}}
  - *Pain Points*: {{pain_points}}
{{/if}}
{{/each}}

## Domain Terminology & Glossary

### Business Vocabulary
{{#each DOMAIN_TERMINOLOGY}}
**{{term}}**: {{definition}}
{{#if context}}
  - *Context*: {{context}}
{{/if}}
{{#if synonyms}}
  - *Synonyms*: {{synonyms}}
{{/if}}
{{#if related_terms}}
  - *Related*: {{related_terms}}
{{/if}}

{{/each}}

### Acronyms & Technical Terms
{{#if ACRONYMS}}
{{#each ACRONYMS}}
**{{acronym}}**: {{expansion}}
{{#if usage_context}}
  - *Used in*: {{usage_context}}
{{/if}}
{{/each}}
{{/if}}

### Conceptual Models & Frameworks
{{#if CONCEPTUAL_MODELS}}
{{#each CONCEPTUAL_MODELS}}
#### {{model_name}}
{{model_description}}
{{#if model_components}}
**Components**: {{model_components}}
{{/if}}
{{#if model_applications}}
**Applications**: {{model_applications}}
{{/if}}

{{/each}}
{{/if}}

## Business Logic & Rules

### Core Business Rules
{{#each BUSINESS_RULES}}
#### {{rule_category}}
{{#each rules}}
- **{{rule_name}}**: {{rule_description}}
{{#if conditions}}
  - *Conditions*: {{conditions}}
{{/if}}
{{#if exceptions}}
  - *Exceptions*: {{exceptions}}
{{/if}}
{{#if business_impact}}
  - *Impact*: {{business_impact}}
{{/if}}
{{/each}}

{{/each}}

### Workflow Patterns & Processes
{{#each BUSINESS_WORKFLOWS}}
#### {{workflow_name}}
**Purpose**: {{purpose}}
{{#if trigger_conditions}}
**Triggered by**: {{trigger_conditions}}
{{/if}}

**Steps**:
{{#each steps}}
{{step_number}}. {{step_description}}
{{#if step_validation}}
   - *Validation*: {{step_validation}}
{{/if}}
{{/each}}

{{#if success_criteria}}
**Success Criteria**: {{success_criteria}}
{{/if}}
{{#if failure_scenarios}}
**Failure Scenarios**: {{failure_scenarios}}
{{/if}}

{{/each}}

### Decision Trees & Logic Flows
{{#if DECISION_TREES}}
{{#each DECISION_TREES}}
#### {{decision_context}}
{{decision_description}}

**Decision Points**:
{{#each decision_points}}
- **{{condition}}** → {{outcome}}
{{/each}}

{{/each}}
{{/if}}

## User Understanding

### Primary User Personas
{{#each USER_PERSONAS}}
#### {{persona_name}}
**Role**: {{role}}
{{#if demographics}}
**Demographics**: {{demographics}}
{{/if}}

**Goals & Motivations**:
{{#each goals}}
- {{this}}
{{/each}}

**Pain Points**:
{{#each pain_points}}
- {{this}}
{{/each}}

{{#if behavior_patterns}}
**Behavior Patterns**: {{behavior_patterns}}
{{/if}}

{{#if technology_comfort}}
**Technology Comfort**: {{technology_comfort}}
{{/if}}

{{/each}}

### User Journey Mapping
{{#each USER_JOURNEYS}}
#### {{journey_name}}
**Persona**: {{persona}}
**Goal**: {{goal}}

**Journey Steps**:
{{#each steps}}
{{step_number}}. **{{stage}}**: {{description}}
{{#if touchpoints}}
   - *Touchpoints*: {{touchpoints}}
{{/if}}
{{#if emotions}}
   - *Emotions*: {{emotions}}
{{/if}}
{{#if pain_points}}
   - *Pain Points*: {{pain_points}}
{{/if}}
{{#if opportunities}}
   - *Opportunities*: {{opportunities}}
{{/if}}
{{/each}}

**Success Metrics**: {{success_metrics}}

{{/each}}

### Common Tasks & Operations
{{#if COMMON_OPERATIONS}}
{{#each COMMON_OPERATIONS}}
#### {{operation_name}}
**Frequency**: {{frequency}}
**Complexity**: {{complexity}}
**User Types**: {{user_types}}

**Typical Flow**:
{{operation_description}}

{{#if variations}}
**Common Variations**:
{{#each variations}}
- {{this}}
{{/each}}
{{/if}}

{{#if error_scenarios}}
**Error Scenarios**:
{{#each error_scenarios}}
- {{scenario}}: {{handling}}
{{/each}}
{{/if}}

{{/each}}
{{/if}}

## Data Architecture & Relationships

### Core Data Entities
{{#each DATA_ENTITIES}}
#### {{entity_name}}
{{entity_description}}

**Key Attributes**:
{{#each attributes}}
- **{{attribute_name}}** ({{data_type}}): {{description}}
{{#if constraints}}
  - *Constraints*: {{constraints}}
{{/if}}
{{/each}}

**Relationships**:
{{#each relationships}}
- {{relationship_type}} {{related_entity}} ({{cardinality}})
{{#if relationship_description}}
  - {{relationship_description}}
{{/if}}
{{/each}}

{{#if business_rules}}
**Business Rules**:
{{#each business_rules}}
- {{this}}
{{/each}}
{{/if}}

{{/each}}

### Data Flow Patterns
{{#if DATA_FLOWS}}
{{#each DATA_FLOWS}}
#### {{flow_name}}
**Purpose**: {{purpose}}
**Source**: {{source}} → **Destination**: {{destination}}

**Transformation Rules**:
{{#each transformations}}
- {{this}}
{{/each}}

{{#if validation_rules}}
**Validation Rules**:
{{#each validation_rules}}
- {{this}}
{{/each}}
{{/if}}

{{#if error_handling}}
**Error Handling**: {{error_handling}}
{{/if}}

{{/each}}
{{/if}}

### Data Quality & Validation
{{#if DATA_QUALITY_RULES}}
{{#each DATA_QUALITY_RULES}}
#### {{rule_category}}
{{#each rules}}
- **{{rule_name}}**: {{rule_description}}
{{#if validation_method}}
  - *Validation*: {{validation_method}}
{{/if}}
{{#if error_action}}
  - *On Error*: {{error_action}}
{{/if}}
{{/each}}

{{/each}}
{{/if}}

## Integration Requirements

### External System Touchpoints
{{#if EXTERNAL_INTEGRATIONS}}
{{#each EXTERNAL_INTEGRATIONS}}
#### {{system_name}}
**Purpose**: {{purpose}}
**Type**: {{integration_type}}
**Criticality**: {{criticality}}

**Data Exchange**:
{{#if data_sent}}
- **Outbound**: {{data_sent}}
{{/if}}
{{#if data_received}}
- **Inbound**: {{data_received}}
{{/if}}

**Business Dependencies**:
{{#each business_dependencies}}
- {{this}}
{{/each}}

{{#if sla_requirements}}
**SLA Requirements**: {{sla_requirements}}
{{/if}}

{{/each}}
{{/if}}

### Internal System Dependencies
{{#if INTERNAL_DEPENDENCIES}}
{{#each INTERNAL_DEPENDENCIES}}
#### {{dependency_name}}
**Type**: {{dependency_type}}
**Purpose**: {{purpose}}
**Impact**: {{impact}}

{{#if dependency_details}}
**Details**: {{dependency_details}}
{{/if}}

{{/each}}
{{/if}}

---

## Context Inheritance Exports

This domain context provides the following variables to child contexts:

**Domain Vocabulary Variables**:
{{#each DOMAIN_VOCABULARY_EXPORTS}}
- `{{key}}`: {{value}}
{{/each}}

**Business Logic Pattern Variables**:
{{#each BUSINESS_LOGIC_EXPORTS}}
- `{{pattern_name}}`: {{pattern_description}}
{{/each}}

**User Interaction Model Variables**:
{{#each USER_INTERACTION_EXPORTS}}
- `{{interaction_type}}`: {{interaction_pattern}}
{{/each}}

**Data Flow Pattern Variables**:
{{#each DATA_FLOW_EXPORTS}}
- `{{flow_name}}`: {{flow_pattern}}
{{/each}}

---

*This context was generated from consultation stage 3 (Domain Extraction) and provides business domain understanding for technical and workflow implementation.*

<!-- VALIDATION CHECKPOINTS -->
<!-- ✓ Core business concepts identified -->
<!-- ✓ Domain terminology captured -->
<!-- ✓ User journeys mapped -->
<!-- ✓ Data relationships documented -->
<!-- ✓ Integration requirements specified -->

<!-- TOKEN BUDGET USAGE: Estimated {{ESTIMATED_TOKEN_COUNT}} tokens -->
<!-- CONFIDENCE SCORE: {{DOMAIN_CONFIDENCE_SCORE}}/10 -->
<!-- LAST UPDATED: {{GENERATION_TIMESTAMP}} -->