| version | last_updated | status |
|---------|--------------|--------|
| 3.0.0   | 2025-07-11   | stable |

# Research Analysis Module

────────────────────────────────────────────────────────────────────────────────

────────────────────────────────────────────────────────────────────────────────

```xml
<module name="research_analysis" category="development">
  
  <purpose>
    Comprehensive research and analysis capabilities for the /query command, enabling deep understanding of codebases, requirements, and technical domains.
  </purpose>
  
  <interface_contract>
    <inputs>
      <required>research_query, context_scope, analysis_objectives</required>
      <optional>domain_constraints, time_limits, depth_requirements</optional>
    </inputs>
    <outputs>
      <success>research_findings, analysis_summary, recommendations, knowledge_artifacts</success>
      <failure>research_limitations, analysis_gaps, partial_findings</failure>
    </outputs>
  </interface_contract>
  
  <execution_pattern>
    <claude_4_behavior>
      WHEN invoked:
      1. Define research scope and establish clear objectives
      2. Execute comprehensive information gathering with parallel searches
      3. Analyze findings systematically with critical thinking
      4. Synthesize insights and generate actionable recommendations
      5. Document knowledge artifacts for future reference
    </claude_4_behavior>
  </execution_pattern>
  
  <trigger_conditions>
    <condition type="automatic">/query command invoked requiring research</condition>
    <condition type="explicit">Understanding unfamiliar codebase or domain</condition>
    <condition type="explicit">Investigating issues or performance problems</condition>
    <condition type="explicit">Analyzing patterns and architectural decisions</condition>
  </trigger_conditions>
  
  <implementation>
    
    <phase name="research_planning" order="1">
      <requirements>
        Research objectives must be clearly defined
        Scope and boundaries must be established
        Success criteria must be determined
        MANDATORY: Use critical thinking to frame research questions
      </requirements>
      <actions>
        Define specific research questions and hypotheses
        Establish scope boundaries and time constraints
        Identify key information sources and search strategies
        Plan parallel research execution for efficiency
        Set success criteria and validation approaches
        MANDATORY: Apply 30s critical thinking for complex research
        ENFORCEMENT: Use ../../system/../../system/quality/critical-thinking.md for research framing
      </actions>
      <validation>
        Research objectives clearly defined and measurable
        Scope boundaries prevent research scope creep
        Success criteria enable validation of findings
        Parallel execution plan optimizes efficiency
        VERIFICATION: Research plan documented with clear methodology
      </validation>
      <blocking_conditions>
        <condition>Research objectives unclear or too broad</condition>
        <condition>Scope boundaries insufficient for focused research</condition>
        <condition>Success criteria undefined or unmeasurable</condition>
      </blocking_conditions>
    </phase>
    
    <phase name="information_gathering" order="2">
      <requirements>
        Research planning from phase 1 must be completed
        Information sources must be accessible
        Search strategies must be executed systematically
        MANDATORY: Parallel execution for efficiency optimization
      </requirements>
      <actions>
        Execute systematic codebase exploration and analysis
        Perform parallel searches across multiple information sources
        Analyze existing documentation and architectural artifacts
        Investigate patterns, conventions, and established practices
        Gather performance data and system metrics where relevant
        MANDATORY: Use parallel tool execution for efficiency
        ENFORCEMENT: Use patterns/tool-usage.md for parallel optimization
      </actions>
      <validation>
        Information gathering covers all planned sources
        Parallel execution maximizes research efficiency
        Systematic approach ensures comprehensive coverage
        Data quality validated through multiple sources
        VERIFICATION: Information inventory documented with sources
      </validation>
      <blocking_conditions>
        <condition>Information sources incomplete or inaccessible</condition>
        <condition>Parallel execution not optimized for efficiency</condition>
        <condition>Systematic approach not followed</condition>
      </blocking_conditions>
    </phase>
    
    <phase name="analysis_synthesis" order="3">
      <requirements>
        Information gathering from phase 2 must be completed
        Analysis framework must be established
        Critical thinking must be applied systematically
        MANDATORY: Evidence-based analysis with consequence mapping
      </requirements>
      <actions>
        Analyze gathered information for patterns and insights
        Identify key findings and their implications
        Map consequences and dependencies systematically
        Synthesize insights into actionable recommendations
        Validate findings against original research objectives
        MANDATORY: Apply critical thinking patterns for analysis depth
        ENFORCEMENT: Use ../../system/../../system/quality/critical-thinking.md for systematic analysis
      </actions>
      <validation>
        Analysis identifies clear patterns and insights
        Findings directly address research objectives
        Consequences mapped with supporting evidence
        Recommendations are actionable and specific
        VERIFICATION: Analysis reasoning documented with evidence chain
      </validation>
      <blocking_conditions>
        <condition>Analysis lacks systematic approach or depth</condition>
        <condition>Findings don't address research objectives</condition>
        <condition>Consequences not mapped with sufficient evidence</condition>
      </blocking_conditions>
    </phase>
    
    <phase name="knowledge_documentation" order="4">
      <requirements>
        Analysis synthesis from phase 3 must be completed
        Documentation framework must be established
        Knowledge artifacts must be created for future reference
        MANDATORY: Comprehensive documentation for knowledge preservation
      </requirements>
      <actions>
        Document research findings in structured format
        Create knowledge artifacts for future reference
        Generate executive summary with key insights
        Provide detailed recommendations with implementation guidance
        Establish decision framework for future similar research
        MANDATORY: Use documentation patterns for consistency
        ENFORCEMENT: Use patterns/documentation-pattern.md for structure
      </actions>
      <validation>
        Documentation captures all key findings and insights
        Knowledge artifacts enable future reference and reuse
        Recommendations include implementation guidance
        Decision framework supports future research decisions
        VERIFICATION: Documentation reviewed for completeness and clarity
      </validation>
      <blocking_conditions>
        <condition>Documentation incomplete or lacks structure</condition>
        <condition>Knowledge artifacts insufficient for future reference</condition>
        <condition>Recommendations lack implementation guidance</condition>
      </blocking_conditions>
    </phase>
    
  </implementation>
  
  <research_methodologies>
    <methodology name="codebase_exploration">
      <purpose>Understanding existing codebase structure and patterns</purpose>
      <techniques>
        Systematic file structure analysis
        Pattern recognition and convention identification
        Dependency mapping and relationship analysis
        Performance characteristic evaluation
        Architecture and design pattern identification
      </techniques>
      <tools>
        Parallel file reading and analysis
        Grep-based pattern searching
        Dependency visualization
        Performance profiling integration
      </tools>
    </methodology>
    <methodology name="domain_research">
      <purpose>Learning about unfamiliar technical domains</purpose>
      <techniques>
        Authoritative source identification
        Best practice research and analysis
        Technology comparison and evaluation
        Implementation pattern research
        Community knowledge gathering
      </techniques>
      <tools>
        Web search with domain filtering
        Documentation analysis
        Example code examination
        Community resource evaluation
      </tools>
    </methodology>
    <methodology name="problem_investigation">
      <purpose>Root cause analysis and issue investigation</purpose>
      <techniques>
        Systematic problem reproduction
        Log analysis and error pattern identification
        Performance bottleneck identification
        Dependency and integration analysis
        Historical change impact analysis
      </techniques>
      <tools>
        Log aggregation and analysis
        Performance monitoring integration
        Version control history analysis
        System metrics correlation
      </tools>
    </methodology>
    <methodology name="requirements_analysis">
      <purpose>Understanding and clarifying requirements</purpose>
      <techniques>
        Stakeholder need identification
        Constraint and limitation analysis
        Success criteria definition
        Risk and impact assessment
        Alternative solution evaluation
      </techniques>
      <tools>
        Requirements documentation analysis
        Stakeholder interview simulation
        Constraint mapping
        Solution comparison matrices
      </tools>
    </methodology>
  </research_methodologies>
  
  <analysis_frameworks>
    <framework name="systematic_analysis">
      <components>
        <component name="data_collection">Gather comprehensive information</component>
        <component name="pattern_recognition">Identify recurring themes</component>
        <component name="root_cause_analysis">Determine underlying causes</component>
        <component name="impact_assessment">Evaluate consequences and implications</component>
        <component name="solution_evaluation">Assess potential approaches</component>
      </components>
    </framework>
    <framework name="critical_thinking">
      <components>
        <component name="assumption_challenge">Question underlying assumptions</component>
        <component name="evidence_evaluation">Assess quality and relevance of evidence</component>
        <component name="alternative_consideration">Explore multiple perspectives</component>
        <component name="bias_recognition">Identify potential biases</component>
        <component name="logical_reasoning">Apply systematic logical analysis</component>
      </components>
    </framework>
  </analysis_frameworks>
  
  <parallel_execution_optimization>
    <strategy name="concurrent_searches">
      Execute multiple search operations simultaneously
      Batch file reading operations for efficiency
      Parallel pattern matching across different domains
      Concurrent analysis of multiple hypotheses
    </strategy>
    <strategy name="information_aggregation">
      Collect related information in parallel streams
      Aggregate findings from multiple sources concurrently
      Synthesize insights from parallel analysis tracks
      Optimize context window usage through batching
    </strategy>
  </parallel_execution_optimization>
  
  <quality_validation>
    <validation_criteria>
      <criterion name="completeness">Research covers all relevant aspects</criterion>
      <criterion name="accuracy">Findings are factually correct and verified</criterion>
      <criterion name="relevance">Information directly addresses research objectives</criterion>
      <criterion name="actionability">Recommendations are specific and implementable</criterion>
      <criterion name="evidence_quality">Claims supported by credible evidence</criterion>
    </validation_criteria>
    <validation_process>
      Cross-reference findings from multiple sources
      Validate conclusions against original objectives
      Test recommendations for feasibility
      Review evidence quality and credibility
      Ensure documentation completeness
    </validation_process>
  </quality_validation>
  
  <knowledge_artifacts>
    <artifact name="research_summary">
      <purpose>Executive summary of key findings</purpose>
      <content>Objectives, methodology, key findings, recommendations</content>
      <format>Structured document with clear sections</format>
    </artifact>
    <artifact name="detailed_analysis">
      <purpose>Comprehensive analysis with supporting evidence</purpose>
      <content>Full analysis, evidence, reasoning, implications</content>
      <format>Detailed report with references and appendices</format>
    </artifact>
    <artifact name="decision_framework">
      <purpose>Framework for future similar decisions</purpose>
      <content>Decision criteria, evaluation process, lessons learned</content>
      <format>Reusable template for similar research</format>
    </artifact>
    <artifact name="implementation_guide">
      <purpose>Practical guidance for implementing recommendations</purpose>
      <content>Step-by-step implementation, risks, success criteria</content>
      <format>Actionable checklist with detailed guidance</format>
    </artifact>
  </knowledge_artifacts>
  
  <integration_points>
    <depends_on>
      ../../system/../../system/quality/critical-thinking.md for systematic analysis
      patterns/tool-usage.md for parallel execution optimization
      patterns/documentation-pattern.md for knowledge documentation
      patterns/research-analysis-pattern.md for methodology guidance
    </depends_on>
    <provides_to>
      /query command for comprehensive research capabilities
      development/task-management.md for research-informed implementation
      patterns/intelligent-routing.md for research complexity assessment
      All commands for domain knowledge and understanding
    </provides_to>
  </integration_points>
  
  <quality_gates enforcement="strict">
    <gate name="research_completeness" requirement="Research covers all planned objectives and scope"/>
    <gate name="analysis_depth" requirement="Analysis applies critical thinking with evidence validation"/>
    <gate name="finding_validation" requirement="Findings validated through multiple sources"/>
    <gate name="documentation_quality" requirement="Knowledge artifacts comprehensive and actionable"/>
  </quality_gates>
  
</module>
```

## Research Analysis Workflow Examples

### Example 1: Codebase Understanding
**Objective**: Understand authentication system architecture
**Planning**: Map authentication flow, identify components, analyze security patterns
**Gathering**: Parallel file analysis, pattern searching, dependency mapping
**Analysis**: Architecture documentation, security assessment, improvement opportunities
**Documentation**: Architecture guide, security recommendations, refactoring roadmap

### Example 2: Performance Investigation
**Objective**: Identify database query performance bottlenecks
**Planning**: Performance metrics analysis, query pattern identification, optimization research
**Gathering**: Log analysis, performance profiling, query execution analysis
**Analysis**: Bottleneck identification, optimization strategies, impact assessment
**Documentation**: Performance report, optimization recommendations, implementation plan

### Example 3: Technology Evaluation
**Objective**: Evaluate frontend framework options for new project
**Planning**: Requirements analysis, framework comparison criteria, evaluation methodology
**Gathering**: Framework documentation, community research, example analysis
**Analysis**: Feature comparison, trade-off analysis, recommendation generation
**Documentation**: Technology comparison, decision rationale, implementation roadmap

### Example 4: Domain Learning
**Objective**: Understand machine learning model deployment patterns
**Planning**: ML deployment research, pattern identification, best practice analysis
**Gathering**: Documentation research, example code analysis, community best practices
**Analysis**: Pattern synthesis, implementation strategies, tooling recommendations
**Documentation**: Deployment guide, pattern library, implementation templates

## Anti-patterns to Avoid
- Starting research without clear objectives
- Relying on single information sources
- Skipping systematic analysis for quick answers
- Not documenting findings for future reference
- Ignoring parallel execution opportunities
- Insufficient validation of research findings

## Research Quality Checklist
- [ ] Research objectives clearly defined and measurable
- [ ] Information gathering executed with parallel optimization
- [ ] Analysis applies critical thinking with evidence validation
- [ ] Findings address original research objectives
- [ ] Recommendations are actionable and specific
- [ ] Knowledge artifacts created for future reference
- [ ] Documentation reviewed for completeness and clarity