---
name: assemble-command
description: Layer 3 Interactive Consultation - Advanced component assembly for professional workflows with 96 components and enterprise capabilities
category: core
parameters: 
  - name: WORKFLOW_TYPE
    type: string
    required: false
    description: Workflow type (data-processing, security-analysis, code-migration, custom)
  - name: MODE
    type: string
    required: false
    description: Assembly mode (--interactive, --from-template, --components, --browse)
  - name: TEMPLATE_NAME
    type: string
    required: false
    description: Template name for template-based assembly (security-audit, data-pipeline, code-transformation)
  - name: COMPONENT_LIST
    type: string
    required: false
    description: Comma-separated list of specific components to assemble
usage_examples:
  - "/assemble-command --interactive"
  - "/assemble-command --from-template security-audit"
  - "/assemble-command data-processing"
  - "/assemble-command --components 'file-reader,data-transformer,output-formatter'"
prerequisites: 
  - "Advanced understanding of component architecture"
  - "Comfort with 15-30 minute assembly process"
  - "Need for complex, reusable workflows"
output_format: structured
tags: [professional-assembly, interactive-consultation, layer-3, enterprise-grade, component-library, v2-enhanced]
version: "1.0"
author: "template-library"
last_updated: "2025-07-31"
allowed-tools:
- Write
- Read
- Grep
- Glob
- Edit
- MultiEdit
---

<!-- AI_METADATA_START -->
<ai_document_metadata>
  <document_type>command</document_type>
  <ai_consumption_priority>critical</ai_consumption_priority>
  <content_structure>yaml_frontmatter</content_structure>
  <file_path>/path/to/your/project/.claude/commands/core/assemble-command.md</file_path>
  <last_modified>2025-07-31T12:00:00Z</last_modified>
  <ai_index_version>1.0</ai_index_version>
</ai_document_metadata>

<command_metadata>
  <command_id>assemble-command</command_id>
  <command_count>88</command_count>
  <progressive_disclosure_layer>3</progressive_disclosure_layer>
  
  <component_dependencies>
    <required_components>
      <component ref="component-loader" role="component_discovery"/>
      <component ref="dependency-resolver" role="compatibility_analysis"/>
      <component ref="workflow-coordinator" role="assembly_orchestration"/>
      <component ref="validation-framework" role="professional_validation"/>
    </required_components>
    <optional_components>
      <component ref="performance-analysis" benefit="optimization_suggestions"/>
      <component ref="security-validation" benefit="enterprise_compliance"/>
      <component ref="documentation-generator" benefit="professional_documentation"/>
    </optional_components>
  </component_dependencies>
  
  <orchestration_capability>
    <can_invoke_commands>true</can_invoke_commands>
    <invokable_commands>
      <command ref="build-command" context="layer_2_fallback"/>
      <command ref="quick-command" context="layer_1_fallback"/>
      <command ref="validate-component" context="component_validation"/>
      <command ref="analyze-system" context="performance_analysis"/>
    </invokable_commands>
    <orchestration_patterns>interactive|template_based|component_driven|workflow_patterns</orchestration_patterns>
  </orchestration_capability>
  
  <v2_features>
    <task_description>Professional component assembly with 96 components, enterprise validation, and advanced workflow orchestration</task_description>
    <implementation_strategy>component_discovery|compatibility_analysis|workflow_design|assembly_execution|professional_validation|documentation_generation</implementation_strategy>
    <command_chaining_enabled>true</command_chaining_enabled>
  </v2_features>
</command_metadata>

<ai_navigation>
  <discovery_metadata>
    <primary_discovery_path>progressive_disclosure_layer_3</primary_discovery_path>
    <alternative_paths>
      <path>professional_assembly_entry_point</path>
      <path>enterprise_component_composition</path>
      <path>advanced_workflow_creation</path>
    </alternative_paths>
  </discovery_metadata>
  
  <relationship_map>
    <upstream_dependencies>
      <file type="command" ref="build-command" relation="layer_2_escalation_source"/>
      <file type="component" ref=".claude/components/COMPONENT-LIBRARY-INDEX.md" relation="component_catalog"/>
      <file type="context" ref=".claude/context/component-assembly-patterns.md" relation="assembly_guidance"/>
    </upstream_dependencies>
    <downstream_consumers>
      <file type="workflow" ref="professional_workflows" relation="generates"/>
      <file type="validation" ref="enterprise_validation_reports" relation="produces"/>
    </downstream_consumers>
    <peer_alternatives>
      <file type="command" ref="build-command" similarity="0.70"/>
      <file type="command" ref="quick-command" similarity="0.40"/>
      <file type="command" ref="component-gen" similarity="0.60"/>
    </peer_alternatives>
  </relationship_map>
  
  <usage_context>
    <when_to_use>
      <scenario>enterprise_workflow_requirements</scenario>
      <scenario>complex_multi_component_assembly</scenario>
      <scenario>professional_quality_standards_needed</scenario>
      <scenario>maximum_customization_and_control</scenario>
    </when_to_use>
    <when_not_to_use>
      <scenario>simple_standard_use_cases</scenario>
      <scenario>time_critical_30_second_needs</scenario>
      <scenario>beginner_users_without_component_knowledge</scenario>
    </when_not_to_use>
  </usage_context>
  
  <ai_search_optimization>
    <keywords>assemble command component assembly professional enterprise layer 3 workflow advanced</keywords>
    <semantic_tags>professional_assembly enterprise_grade maximum_control component_orchestration</semantic_tags>
    <functionality_vectors>[0.3, 0.5, 1.0, 0.9, 0.7]</functionality_vectors>
  </ai_search_optimization>
</ai_navigation>

<context_engineering>
  <ai_understanding_scope>
    <scope_level>project</scope_level>
    <context_retention>session</context_retention>
    <memory_priority>9</memory_priority>
  </ai_understanding_scope>
  
  <knowledge_dependencies>
    <required_context>
      <context_file ref=".claude/context/interactive-consultation-guide.md" importance="critical"/>
      <context_file ref=".claude/components/COMPONENT-LIBRARY-INDEX.md" importance="critical"/>
      <context_file ref=".claude/context/component-assembly-patterns.md" importance="high"/>
    </required_context>
    <helpful_context>
      <context_file ref=".claude/context/enterprise-patterns.md" importance="medium"/>
      <context_file ref=".claude/context/performance-optimization.md" importance="medium"/>
    </helpful_context>
  </knowledge_dependencies>
  
  <workflow_integration>
    <workflow_stage>professional_assembly</workflow_stage>
    <integration_patterns>
      <pattern>component_discovery_and_selection</pattern>
      <pattern>compatibility_validation</pattern>
      <pattern>workflow_design_and_optimization</pattern>
      <pattern>enterprise_quality_assurance</pattern>
    </integration_patterns>
  </workflow_integration>
  
  <ai_learning_markers>
    <concept_introduction>professional_component_assembly</concept_introduction>
    <skill_progression>advanced</skill_progression>
    <mastery_indicators>
      <indicator>successful_complex_workflow_assembly</indicator>
      <indicator>enterprise_validation_compliance</indicator>
      <indicator>performance_optimized_output</indicator>
    </mastery_indicators>
  </ai_learning_markers>
</context_engineering>
<!-- AI_METADATA_END -->

# 🔧 Layer 3: Professional Assembly v1.0

<context type="project">
Interactive Consultation System Layer 3 for context engineering system providing enterprise-grade component assembly with 96 components across 6 professional categories. Designed for power users (5% of users) requiring maximum flexibility, complex workflow orchestration, and 15-30 minute professional assembly processes.
</context>

<instructions>
Execute advanced component assembly using $WORKFLOW_TYPE, $MODE, $TEMPLATE_NAME, and $COMPONENT_LIST parameters. Provide interactive component browser, dependency visualization, performance analysis, and professional validation. Support multiple assembly patterns and enterprise-grade quality assurance.
</instructions>

## Usage Examples

<examples>
<example>  
<input>/assemble-command --interactive</input>
<expected_output>Step-by-step guided assembly with component browser, dependency visualization, and real-time validation</expected_output>
</example>
<example>
<input>/assemble-command --from-template security-audit</input>
<expected_output>Professional security analysis workflow assembled from proven template with enterprise validation</expected_output>
</example>
<example>
<input>/assemble-command data-processing</input>
<expected_output>Intelligent data processing pipeline with workflow pattern matching and performance optimization</expected_output>
</example>
<example>
<input>/assemble-command --components "file-reader,data-transformer,output-formatter"</input>
<expected_output>Direct component assembly with compatibility analysis and dependency resolution</expected_output>
</example>
</examples>

## Professional Assembly Workflow

<workflow type="sequential">
<task priority="high">
**Discovery & Component Exploration**: Navigate 96-component library
- **Interactive Component Browser**: Search, filter, and explore 6 professional categories
- **Dependency Mapping**: Understand component relationships and integration patterns
- **Preview Functionality**: Examine component capabilities and requirements
- **Category Navigation**: Atomic (21), Analysis (15+), Orchestration (10+), Security (12+), Performance (8+), Intelligence (10+)
</task>

<task priority="high">
**Assembly Planning & Pattern Recognition**: Design workflow architecture
- **Workflow Pattern Matching**: Linear Pipeline, Fan-out/Fan-in, State Machine, Event-Driven patterns
- **Template Selection**: Security-audit, data-pipeline, code-transformation proven workflows
- **Component Compatibility Analysis**: Validate integration feasibility and data flow
- **Performance Estimation**: Memory usage, execution time, CPU intensity, I/O operations
</task>

<task priority="high">
**Interactive Assembly & Integration**: Build professional workflow
- **Visual Workflow Builder**: Text-based workflow construction with real-time feedback  
- **Real-time Validation**: Component compatibility, dependency resolution, data flow validation
- **Dependency Resolution**: Automatic ordering, circular dependency detection, optimization suggestions
- **Preview & Testing**: Step-by-step validation with performance analysis
</task>

<task priority="medium">
**Quality Assurance & Professional Validation**: Enterprise-grade verification
- **Automated Testing**: Unit tests, integration tests, end-to-end tests, performance benchmarks
- **Security Review**: OWASP compliance, credential protection, input validation frameworks
- **Documentation Generation**: Professional command documentation with usage examples
- **Performance Analysis**: Bottleneck identification, optimization opportunities, scaling considerations
</task>
</workflow>

## 🏗️ Professional Assembly Modes

### **Interactive Mode** (Recommended - Full Guidance)
**Perfect for**: First-time professional assembly, complex workflow exploration
- **Step-by-step guidance** with explanations and previews
- **Component browser** with search and filtering capabilities
- **Real-time validation** and dependency resolution
- **Performance analysis** and optimization suggestions

### **Template-Based Assembly** (Proven Workflows)
**Perfect for**: Starting with validated enterprise patterns
- **Security-audit template**: Comprehensive security analysis with OWASP compliance
- **Data-pipeline template**: Robust data processing with validation and monitoring
- **Code-transformation template**: Complex code migration and modernization workflows
- **Custom template creation** for reusable organizational patterns

### **Component List Assembly** (Direct Integration)
**Perfect for**: Known component requirements and experienced users
- **Direct component specification** with comma-separated lists
- **Automatic dependency resolution** and compatibility validation
- **Performance optimization** suggestions based on component combinations
- **Quality assurance** with enterprise-grade testing frameworks

### **Workflow Type Assembly** (Intelligent Suggestions)
**Perfect for**: Category-based assembly with intelligent recommendations
- **Data-processing workflows** with intelligent pipeline construction
- **Security-analysis workflows** with compliance and validation frameworks
- **Code-migration workflows** with transformation and validation patterns
- **Custom workflow types** with pattern recognition and suggestion engines

## 🧩 Professional Specialized Agent System (96 Components)

### **Atomic Components** (21 components) - Building Blocks
**Single-purpose, highly reliable components:**
- **I/O Operations**: file-reader, file-writer, parameter-parser, output-formatter, search-files
- **Data Processing**: data-transformer, format-converter, content-sanitizer, response-validator
- **Workflow Control**: state-manager, workflow-coordinator, dependency-resolver, completion-tracker
- **System Operations**: git-operations, api-caller, test-runner
- **User Interface**: progress-indicator, user-confirmation, task-summary, error-handler
- **Validation**: input-validation

### **Analysis Components** (15+ components) - Intelligence & Discovery  
**Advanced analysis and pattern recognition:**
- **Code Analysis**: codebase-discovery, dependency-mapping, quality-metrics, anti-pattern-detection
- **Framework Analysis**: framework-validation, pattern-extraction, architectural-analysis
- **Intelligence**: tree-of-thoughts-reasoning, cognitive-analysis, complexity-assessment

### **Orchestration Components** (10+ components) - Workflow Management
**Complex workflow orchestration and coordination:**
- **Coordination**: agent-orchestration, dag-orchestrator, task-planning, multi-agent-coordination
- **Execution**: dependency-analysis, progress-tracking, task-execution, workflow-optimization
- **Management**: resource-allocation, state-synchronization

### **Security Components** (12+ components) - Enterprise Security
**Professional security and compliance frameworks:**
- **Protection**: credential-protection, input-validation-framework, prompt-injection-prevention
- **Validation**: path-validation, command-security-wrapper, security-audit-framework
- **Compliance**: owasp-compliance, security-policy-enforcement, vulnerability-assessment

### **Performance Components** (8+ components) - Optimization & Efficiency
**Performance optimization and resource management:**
- **Optimization**: context-compression, component-cache, prompt-optimization, framework-optimization
- **Automation**: autoprompt-framework, search-ranking, performance-monitoring
- **Scaling**: resource-optimization

### **Intelligence Components** (10+ components) - Advanced AI Capabilities
**Sophisticated AI and reasoning systems:**
- **Architecture**: cognitive-architecture, adaptive-thinking, meta-learning, reasoning-engine
- **Coordination**: multi-agent-coordination, distributed-intelligence, collaborative-reasoning
- **Advanced Reasoning**: react-reasoning, tree-of-thoughts-framework, strategic-planning

## 🔄 Interactive Consultation Navigation

### **Current Layer (Layer 3):**
**Perfect for**: Power users, enterprise requirements, complex workflows, maximum control

### **Layer Transitions:**

#### **From Layer 2** (Guided Customization Escalation):
```
/build-command complex-analysis --customize
→ "Need maximum control? Try: /assemble-command --from-template analysis-framework"  
```

#### **To Layer 2** (Complexity Reduction):
```
/assemble-command --interactive
→ "Want something simpler? Try: /build-command [workflow-type] --customize"
```

## 🎯 Layer 3 Success Metrics

### **Professional Assembly Targets:**
- **5% of users** require this level of control and complexity  
- **15-30 minute assembly time** acceptable for professional workflows
- **Unlimited customization** with full 96-component library access
- **Enterprise-grade validation** with comprehensive quality assurance
- **High reusability** of assembled professional commands

### **Quality Assurance Standards:**
- **Automated Testing Framework**: Unit, integration, end-to-end, performance benchmarks
- **Security Review Process**: OWASP compliance, vulnerability assessment, security policy enforcement  
- **Performance Analysis**: Bottleneck identification, optimization opportunities, scaling analysis
- **Professional Documentation**: Complete usage examples, integration guides, maintenance procedures

## 🚀 Assembly Pattern Examples

### **Linear Pipeline**: `Input → Process → Validate → Output` (Data transformation, file processing)
### **Fan-out/Fan-in**: `Input → [Process A, B, C] → Merge → Output` (Parallel analysis, multi-format output)  
### **State Machine**: `Input → Decision → [Path A|B|C] → Output` (Conditional workflows, error handling)
### **Event-Driven**: `Trigger → [Handler A, B] → Aggregator → Output` (Reactive systems, monitoring)

<automation trigger="completion">
- Execute professional component assembly with full quality assurance and enterprise validation
- Generate comprehensive workflow documentation with usage examples and integration guidance
- Provide performance analysis with bottleneck identification and optimization recommendations
- Establish professional maintenance procedures and update enterprise component intelligence patterns
</automation>
