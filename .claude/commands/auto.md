# Auto Command - Intelligent Routing and Framework Selection

────────────────────────────────────────────────────────────────────────────────

| version | last_updated | status | readiness |
|---------|--------------|--------|----------|
| 3.0.0   | 2025-07-12   | stable | 95%      |

────────────────────────────────────────────────────────────────────────────────

```xml
<command name="auto" category="routing" enforcement="BLOCKING">
  
  <purpose>
    Analyze requests using advanced reasoning and route to optimal commands with framework selection, complexity scoring, and TDD-aware routing decisions optimized for Claude 4 capabilities.
  </purpose>
  
  <scope>
    <includes>Request analysis, complexity assessment, framework selection, optimal command routing, delegation orchestration</includes>
    <excludes>Direct implementation, manual execution, bypass of established command patterns</excludes>
    <boundaries>Routes to appropriate commands, never executes implementation directly without proper command delegation</boundaries>
  </scope>
  
  <input_specification>
    <required_arguments>User request with varying complexity, context, and requirements</required_arguments>
    <context_requirements>Available commands, framework options, system capabilities, project context</context_requirements>
    <preconditions>Command framework available, routing logic validated, delegation mechanisms ready</preconditions>
  </input_specification>
  
  <output_specification>
    <deliverables>Optimal command selection, framework recommendation, routing justification, delegated execution</deliverables>
    <success_criteria>Correct command selected, appropriate framework chosen, successful delegation completed</success_criteria>
    <artifacts>Routing analysis, complexity assessment, framework selection rationale, delegation results</artifacts>
  </output_specification>
</command>
```

Intelligent routing with framework selection and optimal command routing.

## Thinking Pattern - Claude 4 Enhanced

```xml
<thinking_pattern enforcement="MANDATORY">
  
  <checkpoint id="1" verify="true" enforcement="BLOCKING" thinking_mode="extended">
    <action>Comprehensive Request Analysis: Deep analysis of request intent, scope, complexity, and technical requirements</action>
    <interleaved_thinking enforcement="MANDATORY">
      <pre_analysis>
        - What is the exact intent and scope of this request?
        - How complex is this request across multiple dimensions?
        - What technical and contextual requirements must be considered?
      </pre_analysis>
      <critical_thinking minimum_time="45_seconds">
        - [Intent Question: What exactly does the user want to accomplish?]
        - [Scope Question: How many components, files, or systems are involved?]
        - [Complexity Question: What is the technical complexity across architecture, integration, and implementation?]
        - [Context Question: What existing system context and constraints apply?]
        - [Requirements Question: What quality, performance, and security requirements are implied?]
        - [Timeline Question: What urgency and timeline constraints affect the approach?]
      </critical_thinking>
      <decision_reasoning>
        - Why does this analysis accurately capture the request requirements?
        - What evidence supports the complexity and scope assessment?
        - How do contextual factors influence the optimal routing decision?
      </decision_reasoning>
    </interleaved_thinking>
    <parallel_execution_considerations>
      <tool_optimization>Batch request parsing, complexity analysis, and context evaluation for comprehensive assessment</tool_optimization>
      <context_efficiency>Load system context, available commands, and framework options concurrently</context_efficiency>
      <dependency_analysis>Identify analysis components that can be parallelized vs sequential reasoning requirements</dependency_analysis>
    </parallel_execution_considerations>
    <output_format>REQUEST_ANALYSIS: [intent] with [scope] requiring [complexity_level] and [technical_requirements]</output_format>
    <validation>Request intent clearly understood, scope properly assessed, complexity accurately evaluated, requirements identified</validation>
    <enforcement>BLOCK routing decision until comprehensive request analysis validates understanding</enforcement>
    <context_transfer>Request intent, scope assessment, complexity evaluation, technical requirements</context_transfer>
  </checkpoint>
  
  <checkpoint id="2" verify="true" enforcement="BLOCKING" thinking_mode="interleaved">
    <action>Advanced Framework Selection: Choose optimal prompting framework (RISE, TRACE, CARE) based on complexity and domain</action>
    <interleaved_thinking enforcement="MANDATORY">
      <pre_analysis>
        - Which 2025 prompting framework best matches this request complexity?
        - How do framework characteristics align with request requirements?
        - What framework combination or hybrid approach might be optimal?
      </pre_analysis>
      <critical_thinking minimum_time="30_seconds">
        - [Framework Question: Which framework (RISE/TRACE/CARE/CLEAR/SOAR) best fits the complexity profile?]
        - [Capability Question: How do framework capabilities align with request requirements?]
        - [Integration Question: Can frameworks be combined for enhanced effectiveness?]
        - [Performance Question: Which framework approach optimizes execution efficiency?]
        - [Quality Question: How does framework selection ensure quality outcomes?]
      </critical_thinking>
      <decision_reasoning>
        - Why is this framework selection optimal for the request characteristics?
        - What evidence shows framework alignment with complexity and requirements?
        - How does framework choice optimize execution quality and efficiency?
      </decision_reasoning>
    </interleaved_thinking>
    <parallel_execution_considerations>
      <tool_optimization>Batch framework analysis, capability matching, and optimization assessment</tool_optimization>
      <context_efficiency>Evaluate framework options and integration possibilities concurrently</context_efficiency>
      <dependency_analysis>Identify framework evaluation steps that can be parallelized</dependency_analysis>
    </parallel_execution_considerations>
    <output_format>FRAMEWORK_SELECTED: [framework] optimized for [complexity] with [capabilities] supporting [requirements]</output_format>
    <validation>Framework selected based on complexity analysis, capabilities aligned with requirements, optimization confirmed</validation>
    <enforcement>BLOCK command routing until optimal framework selection validated and justified</enforcement>
    <context_transfer>Selected framework, capability alignment, optimization rationale</context_transfer>
  </checkpoint>
  
  <checkpoint id="3" verify="true" enforcement="BLOCKING" thinking_mode="interleaved">
    <action>Intelligent Command Routing: Select optimal command based on TDD-aware complexity scoring and capability matching</action>
    <interleaved_thinking enforcement="MANDATORY">
      <pre_analysis>
        - Which command best matches the request scope and complexity?
        - How do TDD requirements influence command selection?
        - What command capabilities align with framework and requirements?
      </pre_analysis>
      <critical_thinking minimum_time="30_seconds">
        - [Command Question: Which command (/task, /feature, /swarm, /query, /session, /protocol) best fits the scope?]
        - [TDD Question: How do TDD requirements influence command selection for code changes?]
        - [Capability Question: Do command capabilities match framework and complexity requirements?]
        - [Efficiency Question: Which command provides the most efficient execution path?]
        - [Quality Question: How does command selection ensure quality standards and TDD compliance?]
      </critical_thinking>
      <decision_reasoning>
        - Why is this command selection optimal for the analyzed requirements?
        - What evidence supports the capability matching and efficiency assessment?
        - How does command choice ensure TDD compliance and quality outcomes?
      </decision_reasoning>
    </interleaved_thinking>
    <parallel_execution_considerations>
      <tool_optimization>Batch command capability analysis, TDD assessment, and routing optimization</tool_optimization>
      <context_efficiency>Evaluate command options and capability matching concurrently</context_efficiency>
      <dependency_analysis>Identify routing analysis steps that can be parallelized while maintaining decision integrity</dependency_analysis>
    </parallel_execution_considerations>
    <output_format>COMMAND_ROUTING: [selected_command] for [scope] with [framework] ensuring [tdd_compliance] and [quality_standards]</output_format>
    <validation>Command selected based on scope analysis, framework integration confirmed, TDD compliance ensured, quality standards met</validation>
    <enforcement>BLOCK execution until command routing validated with comprehensive justification</enforcement>
    <context_transfer>Selected command, routing justification, framework integration, TDD compliance plan</context_transfer>
  </checkpoint>
  
  <checkpoint id="4" verify="true" enforcement="BLOCKING" thinking_mode="standard">
    <action>Validated Delegation: Execute selected command with framework integration and quality monitoring</action>
    <interleaved_thinking enforcement="MANDATORY">
      <pre_analysis>
        - How should delegation be executed with framework integration?
        - What monitoring and validation ensure successful execution?
        - How can delegation maintain quality standards and TDD compliance?
      </pre_analysis>
      <critical_thinking minimum_time="30_seconds">
        - [Delegation Question: Is the selected command properly configured with framework and context?]
        - [Integration Question: How does framework integration enhance command execution?]
        - [Monitoring Question: What monitoring ensures successful delegation and quality outcomes?]
        - [Validation Question: How will delegation success be measured and validated?]
        - [Quality Question: Does delegation maintain TDD compliance and quality standards?]
      </critical_thinking>
      <decision_reasoning>
        - Why does this delegation approach ensure optimal execution?
        - What evidence shows proper framework integration and quality monitoring?
        - How does delegation maintain the established quality and TDD standards?
      </decision_reasoning>
    </interleaved_thinking>
    <parallel_execution_considerations>
      <tool_optimization>Execute delegation with framework integration and concurrent quality monitoring</tool_optimization>
      <context_efficiency>Optimize delegation execution and result validation</context_efficiency>
      <dependency_analysis>Identify delegation steps that can be optimized while maintaining execution integrity</dependency_analysis>
    </parallel_execution_considerations>
    <output_format>DELEGATION_EXECUTED: [command] with [framework] achieving [outcomes] maintaining [quality_standards]</output_format>
    <validation>Delegation executed successfully, framework integrated effectively, quality standards maintained, outcomes achieved</validation>
    <enforcement>BLOCK completion until delegation validates successful execution with quality confirmation</enforcement>
    <context_transfer>Delegation results, execution outcomes, quality validation, framework effectiveness</context_transfer>
  </checkpoint>
  
</thinking_pattern>
```

## Instructions

Analyze the request and route to the optimal command for: $ARGUMENTS

1. **Request Analysis**: Understand the intent, scope, and complexity of the request.
   - **Atomic Checkpoint**: `git add -A && git commit -m "AUTO ANALYSIS: [request] - intent and complexity analyzed"`

2. **Framework Selection**: Choose the most appropriate framework (RISE, TRACE, CARE, etc.).
   - **Atomic Checkpoint**: `git add -A && git commit -m "AUTO FRAMEWORK: [selected_framework] - framework selection optimized"`

3. **Command Routing**: Route to the optimal command based on analysis:
   - Simple tasks → /task
   - Multi-component → /swarm  
   - Research needed → /query
   - Documentation → /docs
   - Sessions → /session
   - **Atomic Checkpoint**: `git add -A && git commit -m "AUTO ROUTING: [selected_command] - intelligent routing decision made"`

4. **Execution**: Execute the selected command with framework integration.
   - **Delegated Atomic Safety**: Selected command inherits atomic commit capabilities
   - **Final Checkpoint**: `git add -A && git commit -m "AUTO COMPLETE: [operation] - intelligent routing and execution successful"`

## Routing Logic

- **Single file/component + clear requirements** → /task
- **Multiple files/components** → /swarm
- **Need to understand codebase first** → /query
- **Generate documentation** → /docs
- **Long-running complex work** → /session

## Routing Decision Tree

```xml
<routing_logic>
  <complexity_scoring>
    <simple_tasks score="1-3">
      <criteria>Single file modification, clear requirements, existing patterns</criteria>
      <route>/task</route>
      <framework>RISE for structured execution</framework>
    </simple_tasks>
    
    <moderate_features score="4-6">
      <criteria>Multi-component, defined scope, standard architecture</criteria>
      <route>/feature</route>
      <framework>TRACE for comprehensive planning</framework>
    </moderate_features>
    
    <complex_systems score="7-8">
      <criteria>Multi-agent coordination, complex integration, distributed components</criteria>
      <route>/swarm</route>
      <framework>CARE for coordination and evaluation</framework>
    </complex_systems>
    
    <production_critical score="9-10">
      <criteria>Security sensitive, compliance required, zero-downtime deployment</criteria>
      <route>/protocol</route>
      <framework>CRISP for detailed execution</framework>
    </production_critical>
  </complexity_scoring>
  
  <special_routing>
    <research_needed>
      <criteria>Understanding required before implementation</criteria>
      <route>/query</route>
      <framework>CLEAR for comprehensive analysis</framework>
    </research_needed>
    
    <long_duration>
      <criteria>>10 steps, extended development, progress tracking needed</criteria>
      <route>/session</route>
      <framework>SOAR for sustained execution</framework>
    </long_duration>
    
    <documentation_only>
      <criteria>Documentation generation, no code changes</criteria>
      <route>/docs</route>
      <framework>FOCUS for user-centered design</framework>
    </documentation_only>
  </special_routing>
</routing_logic>
```

## Module Integration

```xml
<module_orchestration>
  <core_modules>
    <module>patterns/critical-thinking-pattern.md</module>
    <module>patterns/intelligent-routing.md</module>
    <module>development/deterministic-routing.md</module>
    <module>prompt_eng/frameworks/framework-selector.md</module>
  </core_modules>
  
  <contextual_modules>
    <module condition="complex_analysis">patterns/research-analysis-pattern.md</module>
    <module condition="multi_component">patterns/multi-agent.md</module>
    <module condition="production_routing">quality/production-standards.md</module>
  </contextual_modules>
  
  <support_modules>
    <module>patterns/comprehensive-error-handling.md</module>
    <module>patterns/error-recovery.md</module>
    <module>patterns/context-management-pattern.md</module>
    <module>quality/universal-quality-gates.md</module>
  </support_modules>
</module_orchestration>
```

## Intelligent Routing Error Handling

```xml
<error_handling framework="intelligent_routing" enforcement="ADAPTIVE">
  <error_classification_integration>
    <module>patterns/comprehensive-error-handling.md</module>
    <routing_specific_patterns>Command selection failures, context analysis errors, routing decision conflicts</routing_specific_patterns>
  </error_classification_integration>
  
  <graceful_degradation>
    <routing_analysis_failures>Fall back to conservative command selection, provide multiple options</routing_analysis_failures>
    <context_analysis_failures>Use simplified analysis, request user clarification</context_analysis_failures>
    <decision_conflicts>Present alternative approaches, escalate to human decision</decision_conflicts>
  </graceful_degradation>
  
  <adaptive_learning>
    <routing_optimization>Learn from successful routing decisions, improve pattern recognition</routing_optimization>
    <failure_analysis>Analyze routing failures, enhance decision algorithms</failure_analysis>
  </adaptive_learning>
</error_handling>

## Original Error Handling

```xml
<error_handling>
  <routing_failures>
    <ambiguous_request>Request clarification, provide routing options with rationale</ambiguous_request>
    <scope_unclear>Route to /query for requirements clarification before implementation</scope_unclear>
    <command_unavailable>Provide alternative routing with capability explanation</command_unavailable>
    <framework_mismatch>Re-analyze complexity, adjust framework selection, retry routing</framework_mismatch>
  </routing_failures>
  
  <delegation_failures>
    <command_execution_failure>Analyze failure root cause, suggest alternative command or approach</command_execution_failure>
    <framework_integration_failure>Fallback to simpler framework, retry delegation with adjusted parameters</framework_integration_failure>
    <quality_standard_failure>Route to appropriate command with enhanced quality enforcement</quality_standard_failure>
  </delegation_failures>
  
  <recovery_procedures>
    <incorrect_routing>Re-analyze request with enhanced complexity assessment, route to correct command</incorrect_routing>
    <execution_timeout>Break down request into smaller components, route to appropriate commands sequentially</execution_timeout>
    <quality_escalation>Route to /protocol for maximum quality enforcement when standards are critical</quality_escalation>
  </recovery_procedures>
</error_handling>
```

## Examples

- `/auto "Add user login"` - Analyzes scope, likely routes to /swarm
- `/auto "Fix this bug"` - Analyzes context, likely routes to /task
- `/auto "Understand the auth system"` - Routes to /query