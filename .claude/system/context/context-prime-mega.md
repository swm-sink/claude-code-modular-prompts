| version | last_updated | status |
|---------|--------------|--------|
| 1.0.0   | 2025-07-19   | stable |

# Context Prime Mega Module

────────────────────────────────────────────────────────────────────────────────

────────────────────────────────────────────────────────────────────────────────

```xml
<module name="context_prime_mega" category="context">
  
  <purpose>
    Comprehensive codebase analysis using sequential multi-agent coordination with detailed findings documentation and critical analysis for enterprise-grade project assessment.
  </purpose>
  
  <interface_contract>
    <inputs>
      <required>project_directory, analysis_scope</required>
      <optional>agent_count_override, time_constraints, specific_focus_areas</optional>
    </inputs>
    <outputs>
      <success>master_analysis_report, agent_findings_collection, improvement_roadmap, critical_issues_summary</success>
      <failure>analysis_failures, agent_coordination_errors, insufficient_data_warnings</failure>
    </outputs>
  </interface_contract>
  
  <execution_pattern>
    <claude_4_behavior>
      WHEN invoked:
      1. Assess codebase size and complexity to determine agent allocation
      2. Get user confirmation on analysis scope and agent count
      3. Initialize agent coordination workspace and tracking system
      4. Execute sequential specialized agents with findings documentation
      5. Compile comprehensive master analysis report with critical recommendations
    </claude_4_behavior>
  </execution_pattern>
  
  <trigger_conditions>
    <condition type="explicit">/context-prime-mega command invoked for comprehensive analysis</condition>
    <condition type="explicit">Enterprise codebase requiring multi-agent assessment</condition>
    <condition type="explicit">Complex project needing detailed findings documentation</condition>
    <condition type="explicit">Critical analysis required for strategic decision making</condition>
  </trigger_conditions>
  
  <implementation>
    
    <phase name="codebase_assessment" order="1">
      <requirements>
        Project directory must be accessible and readable
        Codebase metrics must be calculated for size determination
        Agent allocation strategy must be determined
        User confirmation required for analysis scope
      </requirements>
      <actions>
        Scan project directory structure and calculate complexity metrics
        Count files, directories, lines of code, and technology diversity
        Determine codebase size category (small/medium/large/enterprise)
        Calculate optimal agent allocation based on complexity assessment
        Present analysis plan to user with estimated timeframe
        Get user confirmation or allow custom agent allocation
        Initialize agent coordination workspace in agent_comms/context-analysis-[timestamp]/
        Create findings tracking system and progress monitoring
      </actions>
      <validation>
        Codebase metrics successfully calculated and categorized
        Agent allocation strategy confirmed by user
        Coordination workspace initialized and accessible
        Progress tracking system operational and ready
      </validation>
    </phase>
    
    <phase name="agent_coordination_initialization" order="2">
      <requirements>
        Codebase assessment completed with confirmed agent allocation
        Coordination workspace initialized and operational
        Agent specialization assignments must be defined
        Sequential execution order must be established
      </requirements>
      <actions>
        Create agent coordination tracker with progress monitoring
        Define agent specializations based on codebase size and user preferences
        Establish sequential execution order with state passing between agents
        Initialize findings documentation structure for each agent
        Set up integration points and cross-agent communication protocols
        Create master analysis report template with compilation framework
        Establish checkpoints and user intervention points
        Configure timeout and safety controls for agent execution
      </actions>
      <validation>
        Agent coordination system fully initialized and operational
        Agent specializations clearly defined with execution order
        Findings documentation structure created and accessible
        Safety controls and checkpoints configured and tested
      </validation>
    </phase>
    
    <phase name="sequential_agent_execution" order="3">
      <requirements>
        Agent coordination system operational with defined specializations
        Sequential execution order established with state passing
        Findings documentation framework ready for agent reports
        Progress monitoring and checkpoint system active
      </requirements>
      <actions>
        Execute specialized agents in sequential order with coordination
        Each agent performs detailed analysis in their specialization domain
        Document findings in structured agent-specific reports with evidence
        Pass analysis state and context to subsequent agents
        Monitor progress with checkpoint validation and user intervention points
        Validate agent findings for quality and completeness before proceeding
        Handle agent execution errors with graceful recovery and continuation
        Compile integration notes and cross-agent insights throughout execution
      </actions>
      <agent_execution_workflow>
        <agent_template>
          <initialization>Load previous agent findings and analysis state</initialization>
          <analysis>Perform specialized deep analysis in assigned domain</analysis>
          <documentation>Create comprehensive findings report with evidence</documentation>
          <validation>Validate findings quality and completeness</validation>
          <state_transfer>Pass analysis state and insights to next agent</state_transfer>
        </agent_template>
        
        <specialization_matrix>
          <small_codebase agents="2">
            <agent id="1" specialization="structure" focus="architecture and organization"/>
            <agent id="2" specialization="issues" focus="problems and recommendations"/>
          </small_codebase>
          <medium_codebase agents="4">
            <agent id="1" specialization="structure" focus="architecture and directory organization"/>
            <agent id="2" specialization="dependencies" focus="external/internal dependencies"/>
            <agent id="3" specialization="patterns" focus="coding patterns and conventions"/>
            <agent id="4" specialization="issues" focus="technical debt and recommendations"/>
          </medium_codebase>
          <large_codebase agents="6">
            <agent id="1" specialization="architecture" focus="system design and structure"/>
            <agent id="2" specialization="dependencies" focus="package management and integrations"/>
            <agent id="3" specialization="security" focus="vulnerabilities and compliance"/>
            <agent id="4" specialization="performance" focus="bottlenecks and optimization"/>
            <agent id="5" specialization="patterns" focus="design patterns and quality"/>
            <agent id="6" specialization="issues" focus="critical issues and roadmap"/>
          </large_codebase>
          <enterprise_codebase agents="8">
            <agent id="1" specialization="architecture" focus="system architecture and services"/>
            <agent id="2" specialization="services" focus="microservices and APIs"/>
            <agent id="3" specialization="data" focus="data flow and architecture"/>
            <agent id="4" specialization="security" focus="security posture assessment"/>
            <agent id="5" specialization="performance" focus="performance and scalability"/>
            <agent id="6" specialization="quality" focus="code quality and testing"/>
            <agent id="7" specialization="patterns" focus="design patterns and practices"/>
            <agent id="8" specialization="issues" focus="strategic recommendations"/>
          </enterprise_codebase>
        </specialization_matrix>
      </agent_execution_workflow>
      <validation>
        All specialized agents executed successfully with documented findings
        Agent findings documented in structured reports with evidence
        Cross-agent state transfer completed successfully
        Progress checkpoints passed with user intervention points respected
      </validation>
    </phase>
    
    <phase name="findings_compilation" order="4">
      <requirements>
        All agent executions completed with documented findings
        Agent findings available in structured format for compilation
        Cross-agent analysis framework ready for integration
        Master report template prepared for comprehensive compilation
      </requirements>
      <actions>
        Aggregate all agent findings into unified analysis structure
        Perform cross-agent analysis to identify conflicting and reinforcing findings
        Categorize and prioritize issues by severity, impact, and implementation effort
        Generate executive summary with critical issues requiring immediate attention
        Create detailed findings compilation with evidence and agent attribution
        Develop actionable improvement roadmap with timelines and resource requirements
        Compile comprehensive master analysis report with strategic recommendations
        Validate report completeness and quality before finalization
      </actions>
      <compilation_framework>
        <aggregation>
          <findings_integration>Combine all agent reports into unified structure</findings_integration>
          <cross_validation>Identify conflicts and reinforcing patterns across agents</cross_validation>
          <evidence_compilation>Aggregate supporting evidence and examples</evidence_compilation>
          <insight_synthesis>Synthesize high-level insights from detailed findings</insight_synthesis>
        </aggregation>
        
        <prioritization>
          <severity_assessment>Categorize issues by critical, high, medium, low severity</severity_assessment>
          <impact_analysis>Assess business and technical impact of identified issues</impact_analysis>
          <effort_estimation>Estimate implementation effort for recommended improvements</effort_estimation>
          <roi_calculation>Calculate return on investment for major improvements</roi_calculation>
        </prioritization>
        
        <roadmap_generation>
          <immediate_actions>Issues requiring urgent attention (next 30 days)</immediate_actions>
          <short_term_goals>Improvements for next 3 months with resource allocation</short_term_goals>
          <long_term_strategy>Strategic improvements for 6-12 months</long_term_strategy>
          <success_metrics>Measurable goals and key performance indicators</success_metrics>
        </roadmap_generation>
      </compilation_framework>
      <validation>
        Comprehensive master analysis report generated with all agent findings
        Cross-agent analysis completed with conflict resolution
        Issue prioritization completed with actionable improvement roadmap
        Report quality validated and ready for user review and approval
      </validation>
    </phase>
    
  </implementation>
  
  <codebase_size_detection>
    <assessment_criteria>
      <metrics>
        <file_count>Total number of source files in project</file_count>
        <line_count>Total lines of code excluding comments and blanks</line_count>
        <directory_depth>Maximum directory nesting level</directory_depth>
        <technology_diversity>Number of different languages and frameworks</technology_diversity>
        <dependency_complexity>External and internal dependency count</dependency_complexity>
      </metrics>
      
      <size_categories>
        <small threshold="low_complexity">
          <criteria>Files < 50, LOC < 10k, Directories < 5, Technologies < 3</criteria>
          <agents>2 (Structure + Issues)</agents>
          <timeframe>15-30 minutes</timeframe>
          <focus>Basic architecture and immediate improvements</focus>
        </small>
        <medium threshold="moderate_complexity">
          <criteria>Files 50-500, LOC 10k-100k, Directories 5-20, Technologies 3-6</criteria>
          <agents>4 (Structure + Dependencies + Patterns + Issues)</agents>
          <timeframe>45-60 minutes</timeframe>
          <focus>Comprehensive analysis with dependency mapping</focus>
        </medium>
        <large threshold="high_complexity">
          <criteria>Files 500-2000, LOC 100k-500k, Directories 20-50, Technologies 6-10</criteria>
          <agents>6 (Architecture + Dependencies + Security + Performance + Patterns + Issues)</agents>
          <timeframe>90-120 minutes</timeframe>
          <focus>Enterprise analysis with security and performance focus</focus>
        </large>
        <enterprise threshold="maximum_complexity">
          <criteria>Files > 2000, LOC > 500k, Directories > 50, Technologies > 10</criteria>
          <agents>8 (Architecture + Services + Data + Security + Performance + Quality + Patterns + Issues)</agents>
          <timeframe>2-3 hours with checkpoints</timeframe>
          <focus>Strategic enterprise assessment with comprehensive coverage</focus>
        </enterprise>
      </size_categories>
      
      <user_interaction>
        <assessment_presentation>
          <detected_metrics>Present calculated metrics with size determination</detected_metrics>
          <recommended_approach>Show recommended agent count and timeframe</recommended_approach>
          <customization_options>Allow user to override agent count (1-12) or focus areas</customization_options>
          <confirmation_required>Get explicit user approval before proceeding</confirmation_required>
        </assessment_presentation>
      </user_interaction>
    </assessment_criteria>
  </codebase_size_detection>
  
  <document_generation>
    <findings_structure>
      <workspace_organization>
        <base_directory>agent_comms/context-analysis-[timestamp]/</base_directory>
        <assessment_report>00-codebase-assessment.md</assessment_report>
        <agent_reports>01-agent-[specialization]-[timestamp].md to XX-agent-[specialization]-[timestamp].md</agent_reports>
        <master_report>99-master-analysis-report.md</master_report>
        <coordination_tracker>coordination-tracker.json</coordination_tracker>
      </workspace_organization>
      
      <agent_report_template>
        <header>
          <agent_metadata>Agent ID, specialization, analysis timestamp, duration</agent_metadata>
          <codebase_context>Analyzed components and scope coverage</codebase_context>
          <previous_agents>Summary of previous agent findings relevant to this analysis</previous_agents>
        </header>
        <executive_summary>
          <key_findings>Top 3-5 most important discoveries in this specialization</key_findings>
          <critical_issues>Urgent problems requiring immediate attention</critical_issues>
          <impact_assessment>Business and technical impact of findings</impact_assessment>
        </executive_summary>
        <detailed_analysis>
          <methodology>Analysis approach and tools/techniques used</methodology>
          <comprehensive_findings>Detailed findings with supporting evidence and examples</comprehensive_findings>
          <evidence_documentation>Code examples, metrics, and supporting data</evidence_documentation>
          <pattern_recognition>Identified patterns, anti-patterns, and architectural insights</pattern_recognition>
        </detailed_analysis>
        <issues_identified>
          <critical_severity>Issues requiring immediate action with high impact</critical_severity>
          <high_severity>Important issues for short-term resolution</high_severity>
          <medium_severity>Issues for medium-term planning and resolution</medium_severity>
          <low_severity>Minor improvements and optimizations</low_severity>
        </issues_identified>
        <recommendations>
          <immediate_actions>Specific steps for urgent issue resolution</immediate_actions>
          <short_term_improvements>Recommended changes for next 3 months</short_term_improvements>
          <long_term_strategy>Strategic improvements for 6-12 month timeline</long_term_strategy>
          <resource_requirements>Team, time, and technology needs for implementation</resource_requirements>
        </recommendations>
        <integration_notes>
          <next_agent_context>Information and insights for subsequent agents</next_agent_context>
          <cross_domain_issues>Issues spanning multiple specialization domains</cross_domain_issues>
          <coordination_insights>Recommendations for overall coordination and integration</coordination_insights>
        </integration_notes>
      </agent_report_template>
      
      <master_report_template>
        <executive_summary>
          <codebase_overview>Size, complexity, technology stack, and overall assessment</codebase_overview>
          <health_score>Overall codebase health rating with key metrics</health_score>
          <critical_issues>Top 5-10 most serious problems requiring immediate action</critical_issues>
          <strategic_assessment>High-level evaluation and strategic recommendations</strategic_assessment>
        </executive_summary>
        <methodology>
          <analysis_approach>Multi-agent sequential analysis methodology</analysis_approach>
          <agent_specializations>Summary of agent assignments and coverage areas</agent_specializations>
          <limitations>Analysis scope limitations and areas not covered</limitations>
        </methodology>
        <comprehensive_findings>
          <architecture_analysis>System design, structure, and architectural quality</architecture_analysis>
          <technical_debt>Code quality issues, maintenance burden, and technical debt</technical_debt>
          <security_assessment>Security vulnerabilities, compliance, and risk factors</security_assessment>
          <performance_analysis>Performance bottlenecks, scalability, and optimization opportunities</performance_analysis>
          <dependency_analysis>External dependencies, integration risks, and version management</dependency_analysis>
          <quality_metrics>Code quality scores, test coverage, and maintainability indicators</quality_metrics>
        </comprehensive_findings>
        <issue_prioritization>
          <critical_issues>Immediate attention required with high business impact</critical_issues>
          <high_priority>Important issues for short-term resolution</high_priority>
          <medium_priority>Issues for medium-term planning</medium_priority>
          <low_priority>Minor improvements and optimizations</low_priority>
        </issue_prioritization>
        <improvement_roadmap>
          <immediate_actions>Urgent fixes and improvements (next 30 days)</immediate_actions>
          <short_term_goals>Planned improvements for next 3 months</short_term_goals>
          <long_term_strategy>Strategic improvements for 6-12 months</long_term_strategy>
          <success_metrics>Measurable goals and key performance indicators</success_metrics>
          <resource_planning>Team, budget, and technology requirements</resource_planning>
        </improvement_roadmap>
        <appendices>
          <agent_reports>Links and references to detailed agent findings</agent_reports>
          <metrics_summary>Quantitative analysis results and benchmarks</metrics_summary>
          <tool_recommendations>Suggested tools, frameworks, and technologies</tool_recommendations>
          <reference_materials>Additional resources and documentation</reference_materials>
        </appendices>
      </master_report_template>
    </findings_structure>
  </document_generation>
  
  <safety_controls>
    <execution_safety>
      <timeout_controls>
        <total_analysis>Maximum 3 hours with mandatory checkpoints</total_analysis>
        <individual_agent>Maximum 30 minutes per agent with progress monitoring</individual_agent>
        <user_intervention>User can pause, resume, or abort at any checkpoint</user_intervention>
      </timeout_controls>
      
      <progress_monitoring>
        <real_time_tracking>Live progress updates with estimated completion times</real_time_tracking>
        <checkpoint_validation>Mandatory validation points between agent executions</checkpoint_validation>
        <quality_gates>Quality validation before proceeding to next phase</quality_gates>
      </progress_monitoring>
      
      <error_recovery>
        <agent_failure_handling>Graceful recovery from individual agent failures</agent_failure_handling>
        <partial_results>Ability to generate reports with partial agent completion</partial_results>
        <resume_capability>Resume analysis from last successful checkpoint</resume_capability>
      </error_recovery>
    </execution_safety>
    
    <data_protection>
      <workspace_isolation>Analysis workspace isolated from main project files</workspace_isolation>
      <read_only_access>All analysis operations are read-only on source code</read_only_access>
      <temporary_artifacts>Analysis artifacts automatically cleaned up after completion</temporary_artifacts>
      <sensitive_data_handling>Automatic detection and protection of sensitive information</sensitive_data_handling>
    </data_protection>
  </safety_controls>
  
  <performance_optimization>
    <parallel_execution>
      <file_system_operations>Concurrent file reading and directory traversal</file_system_operations>
      <analysis_operations>Parallel analysis within each agent specialization</analysis_operations>
      <report_generation>Concurrent document generation and compilation</report_generation>
    </parallel_execution>
    
    <memory_management>
      <streaming_analysis>Process large codebases in chunks to manage memory</streaming_analysis>
      <selective_loading>Load only relevant files for each agent specialization</selective_loading>
      <garbage_collection>Regular cleanup of temporary analysis data</garbage_collection>
    </memory_management>
    
    <caching_strategy>
      <analysis_cache>Cache analysis results for repeated operations</analysis_cache>
      <metadata_cache>Cache file system metadata for faster subsequent access</metadata_cache>
      <pattern_cache>Cache recognized patterns for faster pattern matching</pattern_cache>
    </caching_strategy>
  </performance_optimization>
  
  <configuration>
    <user_customization>
      <agent_count_override>Allow 1-12 agents regardless of size detection</agent_count_override>
      <specialization_focus>User can specify focus areas for analysis</specialization_focus>
      <time_constraints>User can set maximum analysis time limits</time_constraints>
      <depth_preferences>User can choose analysis depth (surface/standard/deep)</depth_preferences>
    </user_customization>
    
    <analysis_parameters>
      <include_patterns>File patterns to include in analysis</include_patterns>
      <exclude_patterns>File patterns to exclude from analysis</exclude_patterns>
      <language_focus>Focus on specific programming languages</language_focus>
      <framework_focus>Focus on specific frameworks or technologies</framework_focus>
    </analysis_parameters>
  </configuration>
  
</module>
```

## Integration with Existing Framework

This module integrates with the following framework components:
- **Task Tool**: For spawning specialized analysis agents
- **File Operations**: For read-only codebase scanning and analysis
- **Document Generation**: For structured findings and report creation
- **Progress Tracking**: For user feedback and checkpoint management
- **Quality Gates**: For validation of analysis quality and completeness

## Usage Examples

### Basic Enterprise Analysis
```bash
/context-prime-mega "Analyze this enterprise application for architectural issues and improvements"
```

### Custom Agent Configuration
```bash
/context-prime-mega "Perform security-focused analysis with 6 agents specializing in vulnerabilities"
```

### Targeted Analysis
```bash
/context-prime-mega "Focus on performance and scalability issues in this microservices architecture"
```