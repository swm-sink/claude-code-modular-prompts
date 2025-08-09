# {{PROJECT_NAME}} - Technical Architecture Context
# Layer 3: Technical Implementation Patterns and Standards
# Generated: {{GENERATION_TIMESTAMP}}
# Confidence: {{TECHNICAL_CONFIDENCE_SCORE}}

<!--
CONTEXT LAYER: Technical Architecture (Priority: 8, Token Budget: 2000)
PURPOSE: Defines technical patterns, frameworks, and implementation standards
DEPENDENCIES: Project Foundation, Domain Intelligence
PROVIDES: Technical patterns to workflow and integration layers
INHERITS: project_name, technology_stack, core_constraints, domain_vocabulary
-->

## Technical Stack Overview

### Primary Technologies
**Core Framework**: {{PRIMARY_FRAMEWORK}}
**Programming Language**: {{PROGRAMMING_LANGUAGE}}
{{#if LANGUAGE_VERSION}}
**Language Version**: {{LANGUAGE_VERSION}}
{{/if}}

**Key Libraries & Dependencies**:
{{#each KEY_LIBRARIES}}
- **{{library_name}}** ({{version}}): {{purpose}}
{{#if why_chosen}}
  - *Rationale*: {{why_chosen}}
{{/if}}
{{/each}}

### Development Environment
**Package Manager**: {{PACKAGE_MANAGER}}
**Build Tool**: {{BUILD_TOOL}}
{{#if DEVELOPMENT_SERVER}}
**Development Server**: {{DEVELOPMENT_SERVER}}
{{/if}}

**Development Tools**:
{{#each DEV_TOOLS}}
- **{{tool_name}}**: {{tool_purpose}}
{{/each}}

## Architecture Patterns & Approaches

### System Architecture
**Architecture Style**: {{ARCHITECTURE_STYLE}}
{{#if ARCHITECTURE_DESCRIPTION}}
**Description**: {{ARCHITECTURE_DESCRIPTION}}
{{/if}}

**Key Architectural Decisions**:
{{#each ARCHITECTURAL_DECISIONS}}
#### {{decision_title}}
**Decision**: {{decision}}
**Context**: {{context}}
**Rationale**: {{rationale}}
{{#if consequences}}
**Consequences**: {{consequences}}
{{/if}}
{{#if alternatives_considered}}
**Alternatives Considered**: {{alternatives_considered}}
{{/if}}

{{/each}}

### Design Patterns
{{#each DESIGN_PATTERNS}}
#### {{pattern_name}}
**Usage Context**: {{usage_context}}
**Implementation**: {{implementation_notes}}
{{#if benefits}}
**Benefits**: {{benefits}}
{{/if}}
{{#if trade_offs}}
**Trade-offs**: {{trade_offs}}
{{/if}}

**Example Usage**:
```{{code_language}}
{{code_example}}
```

{{/each}}

### Component Organization Strategy
**Organization Approach**: {{COMPONENT_ORGANIZATION}}
{{#if FOLDER_STRUCTURE}}
**Folder Structure**:
```
{{FOLDER_STRUCTURE}}
```
{{/if}}

**Component Categories**:
{{#each COMPONENT_CATEGORIES}}
- **{{category_name}}**: {{category_description}}
{{#if location}}
  - *Location*: {{location}}
{{/if}}
{{#if naming_convention}}
  - *Naming*: {{naming_convention}}
{{/if}}
{{/each}}

## Code Conventions & Standards

### Naming Conventions
{{#each NAMING_CONVENTIONS}}
#### {{convention_type}}
**Pattern**: {{pattern}}
**Examples**: {{examples}}
{{#if rationale}}
**Rationale**: {{rationale}}
{{/if}}
{{#if exceptions}}
**Exceptions**: {{exceptions}}
{{/if}}

{{/each}}

### File Organization Standards
**File Naming**: {{FILE_NAMING_STANDARD}}
{{#if FILE_STRUCTURE_RULES}}
**Structure Rules**:
{{#each FILE_STRUCTURE_RULES}}
- {{this}}
{{/each}}
{{/if}}

**Import/Export Conventions**:
{{#if IMPORT_CONVENTIONS}}
{{#each IMPORT_CONVENTIONS}}
- **{{import_type}}**: {{convention}}
{{/each}}
{{/if}}

### Code Style Guidelines
{{#if CODE_STYLE_TOOL}}
**Style Tool**: {{CODE_STYLE_TOOL}}
{{#if style_config}}
**Configuration**: {{style_config}}
{{/if}}
{{/if}}

**Key Style Rules**:
{{#each CODE_STYLE_RULES}}
- **{{rule_category}}**: {{rule_description}}
{{#if examples}}
  - *Examples*: {{examples}}
{{/if}}
{{/each}}

**Documentation Standards**:
{{#each DOCUMENTATION_STANDARDS}}
- **{{doc_type}}**: {{standard}}
{{/each}}

## Testing Strategy & Quality Assurance

### Testing Pyramid
{{#if TESTING_PYRAMID}}
**Testing Approach**: {{TESTING_PYRAMID.approach}}

**Test Types by Level**:
{{#each TESTING_PYRAMID.levels}}
#### {{level_name}} ({{percentage}}%)
**Purpose**: {{purpose}}
**Tools**: {{tools}}
**Coverage Target**: {{coverage_target}}

{{#if characteristics}}
**Characteristics**:
{{#each characteristics}}
- {{this}}
{{/each}}
{{/if}}

{{#if example_scenarios}}
**Example Scenarios**:
{{#each example_scenarios}}
- {{this}}
{{/each}}
{{/if}}

{{/each}}
{{/if}}

### Testing Framework & Tools
**Primary Testing Framework**: {{PRIMARY_TEST_FRAMEWORK}}
**Test Runner**: {{TEST_RUNNER}}
{{#if ASSERTION_LIBRARY}}
**Assertion Library**: {{ASSERTION_LIBRARY}}
{{/if}}

**Specialized Testing Tools**:
{{#each TESTING_TOOLS}}
- **{{tool_name}}**: {{tool_purpose}}
{{#if usage_notes}}
  - *Usage*: {{usage_notes}}
{{/if}}
{{/each}}

### Quality Gates & Coverage
{{#if COVERAGE_REQUIREMENTS}}
**Coverage Requirements**:
{{#each COVERAGE_REQUIREMENTS}}
- **{{coverage_type}}**: {{requirement}}
{{/each}}
{{/if}}

**Quality Gates**:
{{#each QUALITY_GATES}}
- **{{gate_name}}**: {{gate_criteria}}
{{#if enforcement}}
  - *Enforcement*: {{enforcement}}
{{/if}}
{{/each}}

### Test Organization & Patterns
**Test Structure**: {{TEST_ORGANIZATION}}
{{#if TEST_PATTERNS}}
**Common Test Patterns**:
{{#each TEST_PATTERNS}}
#### {{pattern_name}}
{{pattern_description}}

**Example**:
```{{code_language}}
{{code_example}}
```

{{/each}}
{{/if}}

## Data Persistence & State Management

### Data Storage Strategy
{{#if DATABASE_TYPE}}
**Primary Database**: {{DATABASE_TYPE}}
{{#if database_rationale}}
**Rationale**: {{database_rationale}}
{{/if}}
{{/if}}

{{#if DATA_PERSISTENCE_PATTERNS}}
**Persistence Patterns**:
{{#each DATA_PERSISTENCE_PATTERNS}}
- **{{pattern_name}}**: {{pattern_description}}
{{#if use_cases}}
  - *Use Cases*: {{use_cases}}
{{/if}}
{{/each}}
{{/if}}

### State Management
{{#if STATE_MANAGEMENT_APPROACH}}
**State Management**: {{STATE_MANAGEMENT_APPROACH}}
{{#if state_tools}}
**Tools/Libraries**: {{state_tools}}
{{/if}}

**State Organization**:
{{#each STATE_ORGANIZATION}}
- **{{state_type}}**: {{organization_pattern}}
{{/each}}
{{/if}}

### Data Access Patterns
{{#if DATA_ACCESS_PATTERNS}}
{{#each DATA_ACCESS_PATTERNS}}
#### {{pattern_name}}
**Purpose**: {{purpose}}
**Implementation**: {{implementation}}
{{#if benefits}}
**Benefits**: {{benefits}}
{{/if}}

**Example**:
```{{code_language}}
{{code_example}}
```

{{/each}}
{{/if}}

## Performance & Optimization

### Performance Requirements
{{#if PERFORMANCE_REQUIREMENTS}}
{{#each PERFORMANCE_REQUIREMENTS}}
- **{{metric}}**: {{target}} ({{measurement_method}})
{{#if context}}
  - *Context*: {{context}}
{{/if}}
{{/each}}
{{/if}}

### Performance Patterns
{{#if PERFORMANCE_PATTERNS}}
{{#each PERFORMANCE_PATTERNS}}
#### {{pattern_name}}
**Problem Addressed**: {{problem}}
**Solution**: {{solution}}
{{#if implementation_notes}}
**Implementation**: {{implementation_notes}}
{{/if}}
{{#if trade_offs}}
**Trade-offs**: {{trade_offs}}
{{/if}}

{{/each}}
{{/if}}

### Optimization Strategies
{{#if OPTIMIZATION_STRATEGIES}}
{{#each OPTIMIZATION_STRATEGIES}}
- **{{strategy_name}}**: {{strategy_description}}
{{#if measurement}}
  - *Measurement*: {{measurement}}
{{/if}}
{{/each}}
{{/if}}

## Deployment & Infrastructure Patterns

### Build & Deployment Pipeline
{{#if BUILD_PROCESS}}
**Build Process**: {{BUILD_PROCESS}}
{{#if build_tools}}
**Build Tools**: {{build_tools}}
{{/if}}
{{/if}}

{{#if DEPLOYMENT_STRATEGY}}
**Deployment Strategy**: {{DEPLOYMENT_STRATEGY}}
{{#if deployment_tools}}
**Deployment Tools**: {{deployment_tools}}
{{/if}}
{{/if}}

**Pipeline Stages**:
{{#each PIPELINE_STAGES}}
{{stage_number}}. **{{stage_name}}**: {{stage_description}}
{{#if stage_tools}}
   - *Tools*: {{stage_tools}}
{{/if}}
{{#if success_criteria}}
   - *Success Criteria*: {{success_criteria}}
{{/if}}
{{/each}}

### Environment Configuration
{{#if ENVIRONMENT_STRATEGY}}
**Environment Strategy**: {{ENVIRONMENT_STRATEGY}}

**Environment Types**:
{{#each ENVIRONMENTS}}
- **{{env_name}}**: {{env_purpose}}
{{#if env_config}}
  - *Configuration*: {{env_config}}
{{/if}}
{{#if env_differences}}
  - *Key Differences*: {{env_differences}}
{{/if}}
{{/each}}
{{/if}}

### Infrastructure Patterns
{{#if INFRASTRUCTURE_PATTERNS}}
{{#each INFRASTRUCTURE_PATTERNS}}
#### {{pattern_name}}
**Purpose**: {{purpose}}
**Implementation**: {{implementation}}
{{#if benefits}}
**Benefits**: {{benefits}}
{{/if}}
{{#if considerations}}
**Considerations**: {{considerations}}
{{/if}}

{{/each}}
{{/if}}

## Error Handling & Resilience

### Error Handling Strategy
{{#if ERROR_HANDLING_APPROACH}}
**Overall Approach**: {{ERROR_HANDLING_APPROACH}}

**Error Categories**:
{{#each ERROR_CATEGORIES}}
- **{{category_name}}**: {{handling_strategy}}
{{#if examples}}
  - *Examples*: {{examples}}
{{/if}}
{{/each}}
{{/if}}

### Logging & Monitoring
{{#if LOGGING_STRATEGY}}
**Logging Strategy**: {{LOGGING_STRATEGY}}
{{#if logging_tools}}
**Logging Tools**: {{logging_tools}}
{{/if}}

**Log Levels & Usage**:
{{#each LOG_LEVELS}}
- **{{level}}**: {{usage_description}}
{{/each}}
{{/if}}

{{#if MONITORING_APPROACH}}
**Monitoring Approach**: {{MONITORING_APPROACH}}
{{#if monitoring_tools}}
**Monitoring Tools**: {{monitoring_tools}}
{{/if}}
{{/if}}

---

## Context Inheritance Exports

This technical context provides the following variables to child contexts:

**Coding Pattern Variables**:
{{#each CODING_PATTERN_EXPORTS}}
- `{{pattern_name}}`: {{pattern_description}}
{{/each}}

**Framework Convention Variables**:
{{#each FRAMEWORK_CONVENTION_EXPORTS}}
- `{{convention_type}}`: {{convention_detail}}
{{/each}}

**Testing Requirement Variables**:
{{#each TESTING_REQUIREMENT_EXPORTS}}
- `{{requirement_type}}`: {{requirement_detail}}
{{/each}}

**Deployment Procedure Variables**:
{{#each DEPLOYMENT_PROCEDURE_EXPORTS}}
- `{{procedure_name}}`: {{procedure_detail}}
{{/each}}

---

*This context was generated from consultation stage 2 (Technical Deep Dive) and provides technical architecture understanding for workflow and integration implementation.*

<!-- VALIDATION CHECKPOINTS -->
<!-- ✓ Technical stack documented -->
<!-- ✓ Architecture patterns defined -->
<!-- ✓ Code conventions established -->
<!-- ✓ Testing strategy outlined -->
<!-- ✓ Performance requirements captured -->

<!-- TOKEN BUDGET USAGE: Estimated {{ESTIMATED_TOKEN_COUNT}} tokens -->
<!-- CONFIDENCE SCORE: {{TECHNICAL_CONFIDENCE_SCORE}}/10 -->
<!-- LAST UPDATED: {{GENERATION_TIMESTAMP}} -->