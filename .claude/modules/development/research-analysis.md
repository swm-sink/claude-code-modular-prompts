| version | last_updated | status |
|---------|--------------|--------|
| 1.0.0   | 2025-07-07   | stable |

# Research Analysis Module

────────────────────────────────────────────────────────────────────────────────

```xml
<module name="research_analysis" category="development">
  
  <purpose>
    Execute comprehensive read-only codebase research and analysis without modifications.
  </purpose>
  
  <trigger_conditions>
    <condition type="automatic">Code understanding requests, architecture analysis, bug investigation</condition>
    <condition type="explicit">User requests /query command or read-only analysis</condition>
  </trigger_conditions>
  
  <implementation>
    
    <phase name="discovery" order="1">
      <requirements>
        System state captured before analysis begins
        Read-only guarantee enforced throughout process
        Broad overview analysis strategy defined
      </requirements>
      <actions>
        Capture initial system state for read-only verification
        Map overall codebase structure and organization
        Identify main modules, services, and architectural boundaries
        Document technology stack and frameworks used
      </actions>
      <validation>
        System state unchanged from initial capture
        Comprehensive structure mapping completed
        Technology stack documentation accurate
      </validation>
    </phase>
    
    <phase name="deep_analysis" order="2">
      <requirements>
        Progressive search refinement from broad to specific
        Efficient search patterns using batched operations
        Context building through layered analysis
      </requirements>
      <actions>
        Execute pattern-specific searches based on research focus
        Analyze implementation patterns and conventions
        Build dependency graph and trace data flows
        Examine integration points and external dependencies
      </actions>
      <validation>
        Search strategy optimized for research objectives
        Dependency relationships accurately mapped
        Integration patterns clearly documented
      </validation>
    </phase>
    
    <phase name="synthesis" order="3">
      <requirements>
        Comprehensive understanding synthesized from findings
        Actionable insights extracted and documented
        Knowledge documentation created for team sharing
      </requirements>
      <actions>
        Synthesize findings into comprehensive mental model
        Extract actionable insights and recommendations
        Generate appropriate report format (executive or technical)
        Document findings for future reference and team knowledge
      </actions>
      <validation>
        Mental model accurately reflects system reality
        Recommendations are specific and actionable
        Documentation format appropriate for intended audience
      </validation>
    </phase>
    
  </implementation>
  
  <quality_gates enforcement="strict">
    <gate name="read_only_compliance" requirement="Zero modifications to system state throughout analysis"/>
    <gate name="comprehensive_coverage" requirement="All relevant system aspects analyzed and documented"/>
    <gate name="actionable_insights" requirement="Findings lead to specific recommendations or understanding"/>
    <gate name="evidence_based" requirement="All conclusions backed by specific code examples or evidence"/>
  </quality_gates>
  
  <search_optimization>
    <progressive_refinement>Start broad, narrow down based on findings</progressive_refinement>
    <pattern_specific_searches>
      Architecture discovery: Glob services, controllers, models then Grep class patterns
      Security analysis: Grep authentication, authorization, encryption patterns
      Performance investigation: Grep query, cache, async patterns
    </pattern_specific_searches>
    <batched_execution>Group related searches for parallel execution efficiency</batched_execution>
  </search_optimization>
  
  <analysis_types>
    <code_understanding>
      Component identification and service boundary mapping
      Request lifecycle and data transformation flow analysis
      Pattern documentation and architectural decision capture
    </code_understanding>
    <security_audit>
      Vulnerability assessment against OWASP Top 10
      Authentication and authorization mechanism review
      Data exposure risk analysis and encryption verification
    </security_audit>
    <performance_investigation>
      Bottleneck identification in queries and algorithms
      Caching and optimization opportunity analysis
      Scalability assessment and resource constraint review
    </performance_investigation>
  </analysis_types>
  
  <session_integration>
    <mandatory_conditions>
      Architecture-level analysis requiring long-term documentation
      System-wide investigation affecting multiple components
      Complex security or performance analysis requiring tracking
    </mandatory_conditions>
    <optional_conditions>
      Simple code understanding for single components
      Quick bug investigation without broader implications
      Research for immediate development decisions
    </optional_conditions>
  </session_integration>
  
  <integration_points>
    <depends_on>
      patterns/tool-usage.md for efficient search strategies
      quality/critical-thinking.md for rigorous analysis methodology
    </depends_on>
    <provides_to>
      development/task-management.md for pre-development research
      security/audit.md for security analysis foundations
    </provides_to>
  </integration_points>
  
</module>
```