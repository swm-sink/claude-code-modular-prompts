| version | last_updated | status | readiness |
|---------|--------------|--------|----------|
| 3.0.0   | 2025-07-12   | stable | 95%      |

# Query Command - Research and Analysis Engine

────────────────────────────────────────────────────────────────────────────────


────────────────────────────────────────────────────────────────────────────────

```xml
<command name="query" category="research" enforcement="BLOCKING">
  
  <purpose>
    Execute comprehensive research and analysis for understanding codebases, requirements, patterns, and system architecture with Claude 4 optimized parallel operations and evidence-based findings.
  </purpose>
  
  <scope>
    <includes>Codebase analysis, pattern recognition, requirement research, architecture understanding, dependency mapping</includes>
    <excludes>Code modifications, implementation tasks, file creation, system changes</excludes>
    <boundaries>Read-only analysis and research without any modifications to existing systems or files</boundaries>
  </scope>
  
  <input_specification>
    <required_arguments>Research question or analysis target with specific information requirements</required_arguments>
    <context_requirements>Codebase access, relevant documentation, system context, research objectives</context_requirements>
    <preconditions>Target system available, research scope defined, analysis criteria established</preconditions>
  </input_specification>
  
  <output_specification>
    <deliverables>Comprehensive research findings, pattern analysis, actionable recommendations, evidence-based conclusions</deliverables>
    <success_criteria>Research questions answered, patterns identified, recommendations provided, findings validated</success_criteria>
    <artifacts>Research report, pattern documentation, dependency maps, analysis summaries, recommendation guides</artifacts>
  </output_specification>
</command>
```

Research and analysis command for understanding codebases and requirements.

## Thinking Pattern - Claude 4 Enhanced

```xml
<thinking_pattern enforcement="MANDATORY">
  
  <checkpoint id="1" verify="true" enforcement="BLOCKING" thinking_mode="extended">
    <action>Pre-Research Atomic Commit: Create secure rollback point before research analysis (read-only safety)</action>
    <interleaved_thinking enforcement="MANDATORY">
      <pre_analysis>
        - What is the current state that should be preserved before research begins?
        - What context or findings might need to be rolled back if research direction changes?
        - How can we ensure clean state management for read-only research operations?
      </pre_analysis>
      <critical_thinking minimum_time="30_seconds">
        - [Safety Question: Is the current state safely preserved before research begins?]
        - [Research Question: What read-only research approach ensures comprehensive findings?]
        - [State Question: How can we maintain clean state management during analysis?]
      </critical_thinking>
    </interleaved_thinking>
    <atomic_commit enforcement="MANDATORY">
      <pre_operation>git add -A && git commit -m "PRE-OP: query - backup state before research analysis (read-only)"</pre_operation>
      <validation>Research baseline established for clean state management</validation>
      <rollback_capability>Available via: git reset --hard HEAD~1</rollback_capability>
    </atomic_commit>
  </checkpoint>
  
  <checkpoint id="2" verify="true" enforcement="BLOCKING" thinking_mode="extended">
    <action>Research Planning and Scope Definition: Comprehensive analysis of research objectives and systematic information gathering strategy</action>
    <interleaved_thinking enforcement="MANDATORY">
      <pre_analysis>
        - What specific information needs to be discovered and analyzed?
        - What research methodology will provide comprehensive and accurate findings?
        - How should research scope be structured for systematic investigation?
      </pre_analysis>
      <critical_thinking minimum_time="45_seconds">
        - [Objective Question: What are the precise research questions that need to be answered?]
        - [Scope Question: What boundaries define complete vs focused research for this investigation?]
        - [Methodology Question: What research approach ensures comprehensive and accurate findings?]
        - [Evidence Question: What types of evidence will validate research conclusions?]
        - [Priority Question: What information is most critical for achieving research objectives?]
        - [Context Question: How does existing system context inform research strategy and approach?]
      </critical_thinking>
      <decision_reasoning>
        - Why does this research approach ensure comprehensive information discovery?
        - What evidence supports the methodology for achieving accurate findings?
        - How does research scope optimization balance thoroughness with efficiency?
      </decision_reasoning>
    </interleaved_thinking>
    <parallel_execution_considerations>
      <tool_optimization>Batch research planning, scope analysis, and methodology design for comprehensive strategy development</tool_optimization>
      <context_efficiency>Load research targets, system documentation, and analysis criteria concurrently</context_efficiency>
      <dependency_analysis>Identify research planning steps that can be parallelized vs sequential strategy development</dependency_analysis>
    </parallel_execution_considerations>
    <output_format>RESEARCH_PLAN: [objectives] with [methodology] targeting [scope] using [evidence_criteria]</output_format>
    <validation>Research objectives clearly defined, methodology validated, scope appropriate, evidence criteria established</validation>
    <enforcement>BLOCK research execution until comprehensive planning validates systematic approach</enforcement>
    <context_transfer>Research objectives, systematic methodology, scope boundaries, evidence validation criteria</context_transfer>
  </checkpoint>
  
  <checkpoint id="2" verify="true" enforcement="BLOCKING" thinking_mode="interleaved">
    <action>Parallel Information Discovery: Execute systematic information gathering using optimized parallel operations</action>
    <interleaved_thinking enforcement="MANDATORY">
      <pre_analysis>
        - How can information discovery be optimized through parallel file operations?
        - What systematic approach ensures comprehensive coverage of research targets?
        - How can information quality and relevance be maintained during discovery?
      </pre_analysis>
      <critical_thinking minimum_time="30_seconds">
        - [Discovery Question: Is information gathering comprehensive across all relevant sources and contexts?]
        - [Efficiency Question: Are parallel operations optimized for maximum information discovery speed?]
        - [Quality Question: Does discovered information meet relevance and accuracy standards?]
        - [Coverage Question: Are all aspects of research objectives being systematically addressed?]
        - [Validation Question: How can information accuracy and completeness be verified during discovery?]
      </critical_thinking>
      <decision_reasoning>
        - Why does this discovery approach ensure comprehensive information gathering?
        - What evidence shows optimal use of parallel operations for research efficiency?
        - How does systematic coverage ensure no critical information is missed?
      </decision_reasoning>
    </interleaved_thinking>
    <parallel_execution_considerations>
      <tool_optimization>Execute parallel file reads, pattern searches, and information extraction for maximum efficiency</tool_optimization>
      <context_efficiency>Optimize concurrent information discovery across multiple sources and contexts</context_efficiency>
      <dependency_analysis>Identify information discovery that can be truly parallel vs sequential analysis requirements</dependency_analysis>
    </parallel_execution_considerations>
    <output_format>DISCOVERY: [sources_analyzed] with [information_gathered] covering [research_areas] at [quality_level]</output_format>
    <validation>Information discovery complete, quality validated, coverage comprehensive, parallel operations optimized</validation>
    <enforcement>BLOCK analysis until systematic information discovery validates comprehensive coverage</enforcement>
    <context_transfer>Discovered information, source validation, coverage assessment, quality confirmation</context_transfer>
  </checkpoint>
  
  <checkpoint id="3" verify="true" enforcement="BLOCKING" thinking_mode="interleaved">
    <action>Pattern Recognition and Analysis: Identify patterns, architectures, and relationships in discovered information</action>
    <interleaved_thinking enforcement="MANDATORY">
      <pre_analysis>
        - What patterns emerge from the discovered information and system analysis?
        - How do architectural decisions and design patterns inform understanding?
        - What relationships and dependencies are critical for comprehensive analysis?
      </pre_analysis>
      <critical_thinking minimum_time="30_seconds">
        - [Pattern Question: What significant patterns, architectures, and design decisions are evident?]
        - [Relationship Question: How do system components and concepts relate and interact?]
        - [Architecture Question: What architectural patterns and principles guide system organization?]
        - [Dependency Question: What critical dependencies and relationships affect system behavior?]
        - [Quality Question: How do discovered patterns align with best practices and standards?]
      </critical_thinking>
      <decision_reasoning>
        - Why do these patterns represent accurate understanding of system organization?
        - What evidence supports the architectural analysis and relationship mapping?
        - How does pattern recognition contribute to comprehensive system understanding?
      </decision_reasoning>
    </interleaved_thinking>
    <parallel_execution_considerations>
      <tool_optimization>Batch pattern analysis, relationship mapping, and architectural assessment for comprehensive understanding</tool_optimization>
      <context_efficiency>Analyze patterns and relationships concurrently across different system dimensions</context_efficiency>
      <dependency_analysis>Identify pattern analysis that can be parallelized vs sequential relationship validation</dependency_analysis>
    </parallel_execution_considerations>
    <output_format>PATTERNS: [identified_patterns] with [relationships] revealing [architecture] and [dependencies]</output_format>
    <validation>Patterns accurately identified, relationships mapped, architecture understood, dependencies clear</validation>
    <enforcement>BLOCK conclusion development until pattern analysis validates comprehensive understanding</enforcement>
    <context_transfer>Pattern identification, relationship maps, architectural understanding, dependency analysis</context_transfer>
  </checkpoint>
  
  <checkpoint id="4" verify="true" enforcement="BLOCKING" thinking_mode="interleaved">
    <action>Evidence-Based Conclusion Development: Synthesize findings into actionable insights and recommendations</action>
    <interleaved_thinking enforcement="MANDATORY">
      <pre_analysis>
        - How can research findings be synthesized into clear, actionable conclusions?
        - What evidence validates the accuracy and completeness of research conclusions?
        - How can recommendations be structured for maximum practical value?
      </pre_analysis>
      <critical_thinking minimum_time="30_seconds">
        - [Synthesis Question: Do conclusions accurately represent and synthesize all research findings?]
        - [Evidence Question: What evidence validates the accuracy and reliability of conclusions?]
        - [Actionability Question: Are recommendations specific, practical, and implementable?]
        - [Completeness Question: Do conclusions address all original research objectives comprehensively?]
        - [Value Question: How do findings and recommendations provide maximum practical value?]
      </critical_thinking>
      <decision_reasoning>
        - Why do these conclusions accurately represent comprehensive research findings?
        - What evidence demonstrates the practical value and accuracy of recommendations?
        - How does synthesis ensure all research objectives are thoroughly addressed?
      </decision_reasoning>
    </interleaved_thinking>
    <parallel_execution_considerations>
      <tool_optimization>Batch conclusion synthesis, evidence validation, and recommendation development</tool_optimization>
      <context_efficiency>Develop conclusions and recommendations concurrently with validation</context_efficiency>
      <dependency_analysis>Identify conclusion development that can be parallelized while maintaining logical coherence</dependency_analysis>
    </parallel_execution_considerations>
    <output_format>CONCLUSIONS: [findings] supported by [evidence] with [recommendations] addressing [objectives]</output_format>
    <validation>Conclusions evidence-based, recommendations actionable, research objectives fully addressed, findings validated</validation>
    <enforcement>BLOCK completion until evidence-based conclusions validate comprehensive research success</enforcement>
    <context_transfer>Evidence-based conclusions, actionable recommendations, research validation, objective completion</context_transfer>
  </checkpoint>
  
  <checkpoint id="5" verify="true" enforcement="CONDITIONAL" thinking_mode="standard">
    <action>Research Documentation and Knowledge Transfer: Document findings for future reference and knowledge sharing</action>
    <interleaved_thinking enforcement="MANDATORY">
      <pre_analysis>
        - How should research findings be documented for maximum future value?
        - What documentation format ensures effective knowledge transfer?
        - How can research insights be preserved for subsequent development work?
      </pre_analysis>
      <critical_thinking minimum_time="30_seconds">
        - [Documentation Question: Is research documentation comprehensive and well-organized for future reference?]
        - [Transfer Question: Does documentation enable effective knowledge transfer to development teams?]
        - [Accessibility Question: Are findings documented in accessible and actionable formats?]
        - [Preservation Question: Will research insights be available for future system development?]
        - [Quality Question: Does documentation meet professional standards for technical analysis?]
      </critical_thinking>
      <decision_reasoning>
        - Why does this documentation approach maximize future value of research findings?
        - What evidence shows effective knowledge transfer and accessibility?
        - How does documentation structure support ongoing development efforts?
      </decision_reasoning>
    </interleaved_thinking>
    <parallel_execution_considerations>
      <tool_optimization>Optimize documentation creation and knowledge transfer preparation</tool_optimization>
      <context_efficiency>Create documentation and validation concurrently where appropriate</context_efficiency>
      <dependency_analysis>Identify documentation steps that can be optimized while maintaining quality</dependency_analysis>
    </parallel_execution_considerations>
    <atomic_commit enforcement="MANDATORY">
      <post_operation>git add research-findings.md && git commit -m "POST-OP: query complete - research analysis documented with findings preservation"</post_operation>
      <validation>Research findings documented and preserved for future reference</validation>
      <rollback_trigger>Documentation failure triggers: git reset --hard HEAD~1 (return to research baseline)</rollback_trigger>
    </atomic_commit>
    <output_format>DOCUMENTATION: [research_report] with [knowledge_transfer] ensuring [future_accessibility]</output_format>
    <validation>Documentation comprehensive, knowledge transfer effective, accessibility confirmed, professional quality met</validation>
    <enforcement>CONDITIONAL - proceed if documentation adds value, skip if research complete</enforcement>
    <context_transfer>Research documentation, knowledge transfer materials, accessibility confirmation</context_transfer>
  </checkpoint>
  
</thinking_pattern>
```

## Instructions

Execute comprehensive research and analysis workflow for: $ARGUMENTS

1. **Research Planning**: Define objectives and systematic methodology.
   - **Planning Checkpoint**: Document research scope, methodology, and evidence criteria

2. **Information Discovery**: Execute parallel operations for comprehensive coverage.
   - **Discovery Checkpoint**: Parallel file analysis with optimized information gathering

3. **Pattern Analysis**: Identify architectures, relationships, and design decisions.
   - **Analysis Checkpoint**: Pattern recognition with architectural understanding

4. **Conclusion Synthesis**: Develop evidence-based findings and recommendations.
   - **Synthesis Checkpoint**: Actionable conclusions with validation evidence

5. **Documentation**: Create knowledge transfer materials (if valuable).
   - **Documentation Checkpoint**: Professional research documentation for future reference

## Critical Rules

- ALWAYS use parallel file operations for maximum efficiency
- NEVER make modifications during research - read-only analysis only
- Ensure comprehensive coverage of research objectives
- Provide evidence-based conclusions with actionable recommendations
- **RESEARCH SAFETY**: Maintain read-only operations with no system changes
- **EVIDENCE VALIDATION**: All conclusions must be supported by discovered evidence

## Research Techniques

```xml
<research_optimization>
  <parallel_operations>Concurrent file reading, pattern searching, information extraction</parallel_operations>
  <systematic_coverage>Structured analysis ensuring comprehensive research scope</systematic_coverage>
  <evidence_validation>Rigorous validation of findings with supporting evidence</evidence_validation>
  <actionable_insights>Practical recommendations based on research conclusions</actionable_insights>
</research_optimization>
```

## Module Integration

```xml
<module_orchestration>
  <core_modules>
    <module>patterns/thinking/critical-thinking-pattern.md</module>
    <module>development/research-analysis.md</module>
    <module>patterns/research-analysis-pattern.md</module>
    <module>patterns/context-management-pattern.md</module>
  </core_modules>
  
  <contextual_modules>
    <module condition="architecture_analysis">patterns/architecture-analysis.md</module>
    <module condition="security_research">security/security-analysis.md</module>
    <module condition="performance_analysis">patterns/performance-analysis.md</module>
    <module condition="integration_research">patterns/integration-analysis.md</module>
  </contextual_modules>
  
  <support_modules>
    <module>patterns/comprehensive-error-handling.md</module>
    <module>patterns/validation-pattern.md</module>
    <module>patterns/documentation-pattern.md</module>
    <module>patterns/evidence-validation.md</module>
  </support_modules>
</module_orchestration>
```

## Research Analysis Error Handling

```xml
<error_handling framework="research_analysis" enforcement="COMPREHENSIVE">
  <error_classification_integration>
    <module>patterns/comprehensive-error-handling.md</module>
    <research_specific_patterns>Information gathering failures, analysis incomplete, source validation errors</research_specific_patterns>
  </error_classification_integration>
  
  <graceful_degradation>
    <information_gathering_failures>Use available sources, document gaps, provide partial analysis</information_gathering_failures>
    <analysis_incomplete>Provide preliminary findings, flag areas needing investigation</analysis_incomplete>
    <source_validation_failures>Cross-reference multiple sources, indicate confidence levels</source_validation_failures>
  </graceful_degradation>
  
  <quality_preservation>
    <research_integrity>Maintain source attribution, document methodology, preserve evidence</research_integrity>
    <analysis_quality>Provide structured findings, clear recommendations, next steps</analysis_quality>
  </quality_preservation>
</error_handling>

## Original Error Handling

```xml
<error_handling>
  <research_failures>
    <insufficient_information>Expand research scope, identify additional sources, adjust methodology</insufficient_information>
    <unclear_objectives>Clarify research questions, refine scope, establish clear success criteria</unclear_objectives>
    <access_limitations>Document limitations, work within available information, note research constraints</access_limitations>
    <pattern_complexity>Break down analysis, focus on key patterns, provide incremental insights</pattern_complexity>
  </research_failures>
  
  <escalation_paths>
    <implementation_needed>Route to /task for focused implementation after research</implementation_needed>
    <complex_development>Route to /feature for comprehensive development planning</complex_development>
    <multi_component_work>Route to /swarm for coordinated multi-component development</multi_component_work>
    <long_term_projects>Route to /session for extended development with GitHub tracking</long_term_projects>
  </escalation_paths>
  
  <quality_assurance>
    <evidence_validation>Verify all findings with concrete evidence from research</evidence_validation>
    <completeness_check>Ensure all research objectives are thoroughly addressed</completeness_check>
    <actionability_review>Confirm recommendations are specific and implementable</actionability_review>
    <knowledge_transfer>Validate effective communication of research insights</knowledge_transfer>
  </quality_assurance>
</error_handling>
```

## Examples

- `/query "How does authentication work in this system?"` - Analyzes auth patterns and implementation
- `/query "What testing frameworks are being used?"` - Identifies test infrastructure and patterns
- `/query "How is error handling implemented?"` - Studies error patterns and recovery mechanisms
- `/query "What are the performance bottlenecks?"` - Analyzes system performance characteristics
- `/query "How does the payment system integrate?"` - Researches integration patterns and dependencies