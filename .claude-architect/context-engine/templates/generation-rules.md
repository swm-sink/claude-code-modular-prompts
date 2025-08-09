# Claude Context Architect - Context Generation Rules
# Version: 1.0
# Created: 2025-08-07
# Purpose: Define conditional logic and generation decision-making

## Overview

This document defines the rules and logic that govern how consultation data is transformed into context files. The generation system uses sophisticated conditional logic to adapt content based on data quality, project characteristics, and confidence levels.

## Core Generation Principles

### 1. Quality Over Quantity
- **Principle**: Generate complete, high-quality context rather than sparse, low-confidence content
- **Implementation**: Skip sections with confidence < 5/10, add warnings for confidence < 7/10
- **Rationale**: Better to have accurate partial context than inaccurate complete context

### 2. Adaptive Depth
- **Principle**: Adjust content depth based on available information and project complexity
- **Implementation**: Use multi-tier content generation (minimal, standard, comprehensive)
- **Rationale**: Different projects need different levels of detail

### 3. Graceful Degradation
- **Principle**: Always generate valid context, even with incomplete data
- **Implementation**: Use sensible defaults, computed values, and fallback patterns
- **Rationale**: System should never fail completely due to missing data

### 4. Cross-Layer Consistency
- **Principle**: Ensure information consistency across all context layers
- **Implementation**: Validate cross-references and enforce inheritance rules
- **Rationale**: Inconsistent context leads to poor Claude responses

## Generation Decision Tree

### Stage 1: Data Quality Assessment

```
Input Data Quality Check:
├─ All Required Variables Present?
│  ├─ YES → Confidence Base Score = 8/10
│  └─ NO → Confidence Base Score = 5/10
│
├─ Optional Variable Coverage > 70%?
│  ├─ YES → Confidence +1
│  └─ NO → Confidence unchanged
│
├─ Data Passes Validation Rules?
│  ├─ YES → Confidence +0.5
│  └─ NO → Confidence -1, Add validation warnings
│
└─ Cross-Stage Consistency Check?
   ├─ CONSISTENT → Confidence unchanged
   └─ INCONSISTENT → Confidence -2, Flag conflicts
```

### Stage 2: Content Generation Strategy

```
Content Generation Decision:
├─ Confidence Score ≥ 8?
│  ├─ YES → Generate COMPREHENSIVE content
│  │      ├─ Include all optional sections
│  │      ├─ Add detailed examples
│  │      └─ Include cross-references
│  └─ NO → Continue to next check
│
├─ Confidence Score ≥ 6?
│  ├─ YES → Generate STANDARD content
│  │      ├─ Include core sections only
│  │      ├─ Add basic examples
│  │      └─ Limited cross-references
│  └─ NO → Continue to next check
│
└─ Confidence Score ≥ 4?
   ├─ YES → Generate MINIMAL content
   │      ├─ Essential sections only
   │      ├─ Basic information
   │      └─ Clear low-confidence warnings
   └─ NO → Generate ERROR content
          ├─ Template with placeholders
          ├─ Clear error messaging
          └─ Manual completion instructions
```

### Stage 3: Section-Level Decisions

```
For Each Template Section:
├─ Required Section?
│  ├─ YES → Always generate (use fallbacks if needed)
│  └─ NO → Continue to conditional check
│
├─ Has Required Data?
│  ├─ YES → Generate section
│  └─ NO → Continue to confidence check
│
├─ Computed Data Available?
│  ├─ YES → Generate with computed values
│  └─ NO → Continue to fallback check
│
└─ Fallback Data Available?
   ├─ YES → Generate with fallback + warning
   └─ NO → Skip section entirely
```

## Conditional Content Rules

### Foundation Context Rules

#### Project Identity Section
```yaml
conditions:
  always_include:
    - PROJECT_NAME (required)
    - PROJECT_DOMAIN (required)
    - PROJECT_TYPE (required)
  
  conditional_include:
    PROJECT_MISSION:
      condition: "confidence_score >= 6 AND primary_goals.length > 0"
      fallback: "Generate from project_name + domain + goals"
    
    PROJECT_VISION:
      condition: "aspirational_goals.exists AND confidence_score >= 7"
      fallback: "Skip section"
    
    VALUE_PROPOSITIONS:
      condition: "target_users.specific AND primary_goals.length >= 2"
      fallback: "Compute from target_users + goals"
```

#### Team Culture Section
```yaml
conditions:
  include_section:
    condition: "team_size.known AND (communication_style.known OR working_agreements.exists)"
    fallback_strategy: "generate_minimal_team_section"
  
  working_agreements:
    condition: "preference_learning.team_collaboration.exists"
    fallback: "Infer from team_size and project_type"
  
  communication_patterns:
    condition: "team_size > 1 AND communication_style.specified"
    fallback: "Skip if solo developer"
```

### Domain Context Rules

#### Business Concepts Section
```yaml
conditions:
  core_concepts:
    minimum_required: 2
    condition: "domain_concepts.length >= minimum_required"
    fallback_strategy: "generate_generic_concepts_from_domain"
  
  domain_terminology:
    minimum_required: 3
    condition: "terminology.length >= minimum_required"
    fallback_strategy: "extract_terms_from_descriptions"
  
  stakeholders:
    condition: "business_domain != 'technical' AND stakeholder_info.exists"
    fallback: "Generate generic stakeholders for domain type"
```

#### User Understanding Section
```yaml
conditions:
  user_personas:
    condition: "user_journeys.exists OR user_types.detailed"
    confidence_threshold: 6
    fallback_strategy: "generate_basic_persona_from_target_users"
  
  user_journeys:
    condition: "personas.exists AND workflows.documented"
    min_confidence: 7
    fallback: "Skip section, note in missing info"
  
  common_operations:
    condition: "user_workflows.specific OR business_processes.documented"
    fallback_strategy: "infer_from_domain_type"
```

### Technical Context Rules

#### Architecture Patterns Section
```yaml
conditions:
  architecture_decisions:
    condition: "architectural_choices.documented OR framework_rationale.exists"
    confidence_threshold: 6
    fallback_strategy: "generate_generic_decisions_for_stack"
  
  design_patterns:
    condition: "coding_patterns.documented OR framework_conventions.specific"
    fallback: "Extract common patterns for framework type"
  
  component_organization:
    condition: "project_structure.understood OR organization_strategy.specified"
    fallback_strategy: "use_framework_defaults"
```

#### Testing Strategy Section
```yaml
conditions:
  testing_pyramid:
    condition: "testing_approach.detailed OR test_types.specified"
    min_confidence: 5
    fallback_strategy: "generate_standard_pyramid_for_framework"
  
  quality_gates:
    condition: "quality_requirements.specified OR review_process.documented"
    fallback: "Generate basic quality gates"
  
  test_patterns:
    condition: "testing_examples.exist OR testing_conventions.specified"
    confidence_threshold: 7
    fallback: "Skip detailed patterns, include framework basics"
```

### Workflow Context Rules

#### Development Process Section
```yaml
conditions:
  feature_development_stages:
    condition: "development_process.documented OR methodology.specific"
    fallback_strategy: "generate_stages_for_methodology"
  
  code_review_process:
    condition: "review_requirements.specified OR team_size > 1"
    fallback: "Generate basic peer review process"
  
  quality_gates:
    condition: "quality_requirements.exist OR deployment_process.gated"
    fallback_strategy: "infer_from_project_complexity"
```

#### Team Collaboration Section
```yaml
conditions:
  communication_protocols:
    condition: "team_size > 3 OR remote_team.true"
    fallback: "Skip for small co-located teams"
  
  meeting_cadence:
    condition: "methodology.agile OR team_size > 5"
    fallback_strategy: "generate_basic_cadence_for_team_size"
  
  decision_making:
    condition: "team_structure.hierarchical OR decision_process.documented"
    fallback: "Skip for small teams"
```

### Integration Context Rules

#### Cross-Cutting Concerns Section
```yaml
conditions:
  security_patterns:
    condition: "security_requirements.exist OR external_integrations.exist OR compliance_needed.true"
    fallback_strategy: "generate_basic_security_for_project_type"
  
  logging_architecture:
    condition: "monitoring_requirements.exist OR system_complexity.high"
    fallback: "Generate basic logging strategy"
  
  error_handling:
    condition: "error_scenarios.documented OR resilience_requirements.exist"
    fallback_strategy: "infer_from_architecture_style"
```

## Content Depth Adaptation Rules

### Comprehensive Content (Confidence ≥ 8)

#### Foundation Layer
- **Include**: Full historical context, detailed team culture, comprehensive constraints
- **Examples**: Specific decision rationales, detailed lessons learned
- **Cross-References**: Link to all related context layers
- **Tone**: Detailed, authoritative, confident

#### Domain Layer  
- **Include**: Complete business rules, detailed user journeys, comprehensive data models
- **Examples**: Specific business scenarios, detailed workflow examples
- **Cross-References**: Link business concepts to technical implementations
- **Tone**: Domain-expert level, assumes business knowledge

#### Technical Layer
- **Include**: Detailed architecture decisions, comprehensive patterns, full testing strategy
- **Examples**: Code examples, specific configuration details
- **Cross-References**: Link to domain requirements and workflow processes
- **Tone**: Technical expert level, implementation-focused

### Standard Content (Confidence 6-7)

#### All Layers
- **Include**: Core sections with essential details
- **Examples**: Generic examples adapted to project
- **Cross-References**: Basic linking between layers
- **Tone**: Professional but accessible
- **Warnings**: Note areas with lower confidence

### Minimal Content (Confidence 4-5)

#### All Layers
- **Include**: Essential information only
- **Examples**: Framework defaults and generic patterns
- **Cross-References**: Minimal, avoid assumptions
- **Tone**: Cautious, clearly mark uncertainties
- **Warnings**: Prominent low-confidence warnings

## Error Handling and Recovery Rules

### Missing Critical Data
```yaml
recovery_strategies:
  missing_project_name:
    action: "prompt_for_input"
    message: "Project name is required for context generation"
    fallback: "Generate template with [PROJECT_NAME] placeholder"
  
  missing_technology_stack:
    action: "infer_from_project_type"
    confidence_penalty: -2
    fallback: "Use generic technology stack"
  
  missing_domain_context:
    action: "infer_from_project_description"
    include_uncertainty_note: true
    fallback: "Use 'General Business' domain"
```

### Validation Failures
```yaml
validation_recovery:
  invalid_team_size:
    action: "use_reasonable_default"
    default: 3
    log_warning: true
  
  invalid_framework_name:
    action: "normalize_and_validate"
    fallback: "Use generic framework category"
  
  circular_dependencies:
    action: "break_circular_references"
    strategy: "remove_weakest_link"
```

### Confidence Below Threshold
```yaml
low_confidence_handling:
  confidence_below_4:
    action: "generate_template_with_placeholders"
    include_manual_completion_guide: true
    
  confidence_4_to_6:
    action: "generate_with_warnings"
    warning_placement: "section_headers"
    
  confidence_6_to_8:
    action: "generate_with_notes"
    note_placement: "section_footers"
```

## Cross-Layer Consistency Rules

### Inheritance Validation
```yaml
inheritance_checks:
  foundation_to_all:
    required_exports: ["project_name", "domain_context", "technology_stack"]
    validation: "ensure_consistent_across_layers"
    
  domain_to_technical:
    consistency_checks:
      - "domain_vocabulary referenced in technical_patterns"
      - "business_logic_patterns align with architectural_decisions"
    
  technical_to_workflow:
    consistency_checks:
      - "testing_requirements match testing_strategy"
      - "deployment_procedures align with architecture"
```

### Conflict Resolution
```yaml
conflict_resolution:
  strategy: "child_overrides_parent"
  exceptions:
    - "project_name: must be consistent across all layers"
    - "technology_stack: child can extend but not replace"
  
  conflict_logging:
    level: "WARNING"
    include_resolution_rationale: true
    suggest_manual_review: true
```

## Token Budget Management Rules

### Budget Allocation Strategy
```yaml
token_allocation:
  foundation: 2000  # 25% of total
  domain: 1500      # 18.75%
  technical: 2000   # 25%
  workflow: 1200    # 15%
  integration: 800  # 10%
  buffer: 500       # 6.25% buffer
  total: 8000
```

### Overflow Handling
```yaml
overflow_strategy:
  priority_trimming:
    1: "Remove optional examples"
    2: "Shorten section descriptions"  
    3: "Remove lowest-confidence sections"
    4: "Truncate integration layer first"
    5: "Compress all content to essential"
  
  section_priority:
    foundation:
      high: ["Project Identity", "Core Constraints"]
      medium: ["Team Culture", "Historical Context"]
      low: ["Aspirational Goals"]
    
    domain:
      high: ["Core Concepts", "Terminology"]
      medium: ["Business Rules", "User Understanding"]
      low: ["Integration Requirements"]
```

## Quality Assurance Rules

### Pre-Generation Validation
```yaml
pre_generation:
  data_quality_checks:
    - "required_variables_present"
    - "data_type_validation"
    - "cross_stage_consistency"
    - "confidence_threshold_met"
  
  template_validation:
    - "template_syntax_valid"
    - "variable_placeholders_resolvable"
    - "inheritance_chain_valid"
```

### Post-Generation Validation
```yaml
post_generation:
  content_quality_checks:
    - "minimum_section_lengths_met"
    - "no_placeholder_content_remains"
    - "cross_references_valid"
    - "token_budgets_respected"
  
  consistency_validation:
    - "inheritance_variables_propagated"
    - "no_conflicting_information"
    - "terminology_consistent"
```

### Quality Gates
```yaml
quality_gates:
  gate_1_data_validation:
    criteria: "All required data passes validation"
    action_on_fail: "Fix data or use fallbacks"
  
  gate_2_template_processing:
    criteria: "All templates process without errors"
    action_on_fail: "Use error recovery strategies"
  
  gate_3_content_quality:
    criteria: "Generated content meets quality thresholds"
    action_on_fail: "Apply content improvements"
  
  gate_4_consistency:
    criteria: "Cross-layer consistency validated"
    action_on_fail: "Resolve conflicts automatically or flag for manual review"
```

This comprehensive rule system ensures that context generation adapts intelligently to the quality and completeness of consultation data while maintaining consistency and usefulness across all scenarios.