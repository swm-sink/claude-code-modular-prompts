| version | last_updated | status |
|---------|--------------|--------|
| 1.0.0   | 2025-07-09   | stable |

# Research & Analysis Pattern Module

────────────────────────────────────────────────────────────────────────────────


────────────────────────────────────────────────────────────────────────────────

```xml
<module name="research_analysis_pattern" category="patterns">
  
  <purpose>
    Systematic information gathering and understanding before implementation, ensuring decisions are based on comprehensive analysis of existing patterns, constraints, and requirements.
  </purpose>
  
  <trigger_conditions>
    <condition type="automatic">Starting work on unfamiliar codebase</condition>
    <condition type="explicit">Understanding requirements for new features</condition>
    <condition type="explicit">Investigating bugs or performance issues</condition>
    <condition type="explicit">Learning about existing patterns and conventions</condition>
    <condition type="explicit">Making architectural decisions</condition>
  </trigger_conditions>
  
  <implementation>
    
    <phase name="define_research_goals" order="1">
      <requirements>
        Research objectives must be clearly defined
        Decision context must be established
        Resource constraints must be understood
      </requirements>
      <actions>
        Clarify what you need to understand
        Identify specific information required
        Define what decisions this research will inform
        Determine required level of detail
        Document constraints and timeline
      </actions>
      <validation>
        Research goals are specific and measurable
        Decision context is clearly established
        Resource constraints are documented
        Success criteria are defined
      </validation>
    </phase>
    
    <phase name="gather_information" order="2">
      <requirements>
        Research goals from phase 1 must be defined
        Information sources must be identified
        Search strategies must be planned
      </requirements>
      <actions>
        Collect relevant data from multiple sources
        Read existing documentation and code
        Search for similar implementations
        Analyze patterns and conventions
        Review related issues and discussions
        Use parallel searches for efficiency
      </actions>
      <validation>
        Multiple information sources consulted
        Parallel searches executed efficiently
        Relevant patterns and conventions identified
        Similar implementations found and analyzed
        Documentation and code reviewed systematically
      </validation>
    </phase>
    
    <phase name="analyze_findings" order="3">
      <requirements>
        Information from phase 2 must be available
        Analysis framework must be established
        Comparison criteria must be defined
      </requirements>
      <actions>
        Process and synthesize the information
        Identify patterns and themes
        Compare different approaches
        Evaluate pros and cons
        Note gaps and inconsistencies
        Document key insights
      </actions>
      <validation>
        Patterns and themes clearly identified
        Different approaches compared systematically
        Pros and cons evaluated objectively
        Gaps and inconsistencies documented
        Key insights captured and organized
      </validation>
    </phase>
    
    <phase name="validate_understanding" order="4">
      <requirements>
        Analysis from phase 3 must be completed
        Validation criteria must be established
        Cross-reference sources must be available
      </requirements>
      <actions>
        Confirm your analysis is accurate
        Cross-reference multiple sources
        Test assumptions with examples
        Verify findings with stakeholders if possible
        Check for contradictory evidence
      </actions>
      <validation>
        Analysis accuracy confirmed through cross-reference
        Assumptions tested with concrete examples
        Contradictory evidence identified and addressed
        Stakeholder validation obtained where possible
      </validation>
    </phase>
    
    <phase name="document_results" order="5">
      <requirements>
        Validated understanding from phase 4
        Documentation framework must be available
        Future reference needs must be considered
      </requirements>
      <actions>
        Capture findings for future reference
        Create summary of key findings
        Provide recommendations and next steps
        Document assumptions and limitations
        List references and sources
        Establish decision framework
      </actions>
      <validation>
        Key findings summarized clearly
        Recommendations are actionable
        Assumptions and limitations documented
        References and sources properly cited
        Decision framework established
      </validation>
    </phase>
    
  </implementation>
  
  <search_strategies>
    <strategy name="keyword_search">
      Use specific terms related to the domain
      Target technical terminology and concepts
      Include synonyms and related terms
    </strategy>
    <strategy name="pattern_search">
      Look for recurring implementations
      Identify common approaches and conventions
      Find established patterns and practices
    </strategy>
    <strategy name="example_search">
      Find working examples and use cases
      Locate implementation references
      Identify practical applications
    </strategy>
    <strategy name="dependency_search">
      Understand connections and relationships
      Map system interactions and dependencies
      Identify impact and integration points
    </strategy>
    <strategy name="historical_search">
      Review evolution and changes over time
      Understand decision history and context
      Learn from past issues and solutions
    </strategy>
  </search_strategies>
  
  <information_sources>
    <source type="code">Code repositories and file structures</source>
    <source type="documentation">Documentation and README files</source>
    <source type="discussion">Issue trackers and discussion forums</source>
    <source type="specification">API documentation and specifications</source>
    <source type="examples">Test files and examples</source>
    <source type="configuration">Configuration files and settings</source>
  </information_sources>
  
  <parallel_optimization>
    <optimization>Batch multiple file reads together</optimization>
    <optimization>Run concurrent searches for different aspects</optimization>
    <optimization>Combine related analysis tasks</optimization>
    <optimization>Use efficient search tools and techniques</optimization>
  </parallel_optimization>
  
  <quality_criteria>
    <criterion>Information is accurate and up-to-date</criterion>
    <criterion>Sources are credible and relevant</criterion>
    <criterion>Analysis is comprehensive and balanced</criterion>
    <criterion>Conclusions are well-supported by evidence</criterion>
    <criterion>Gaps and limitations are acknowledged</criterion>
  </quality_criteria>
  
  <integration_points>
    <provides_to>
      ../../prompt_eng/../../prompt_eng/patterns/thinking/critical-thinking-pattern.md for decision-making
      patterns/tdd-cycle-pattern.md with requirement understanding
      ../../patterns/implementation-pattern.md with informed approach
      development/documentation.md for knowledge sharing
    </provides_to>
    <depends_on>
      patterns/pattern-library.md for search and analysis patterns
      development/research-analysis.md for analysis frameworks
    </depends_on>
  </integration_points>
  
  <pattern_usage>
    <uses_pattern from="patterns/pattern-library.md">systematic_analysis</uses_pattern>
    <uses_pattern from="patterns/pattern-library.md">parallel_execution</uses_pattern>
    <implementation_notes>
      Enables informed decision-making through comprehensive research
      Supports parallel tool execution for efficient information gathering
      Integrates with critical thinking for evidence-based analysis
      Provides foundation for TDD with requirement understanding
    </implementation_notes>
  </pattern_usage>
  
  <configuration>
    <setting name="research_depth" default="comprehensive" required="true">
      Level of research depth (basic/standard/comprehensive)
    </setting>
    <setting name="parallel_searches" default="true" required="false">
      Enable parallel execution of search operations
    </setting>
    <setting name="source_validation" default="true" required="false">
      Require cross-validation of information sources
    </setting>
    <setting name="documentation_required" default="true" required="true">
      Require documentation of research findings
    </setting>
  </configuration>
  
  <error_handling>
    <error code="RAP001" severity="warning">
      Insufficient research depth - expand information gathering
    </error>
    <error code="RAP002" severity="warning">
      Single source reliance - require multiple sources
    </error>
    <error code="RAP003" severity="critical">
      Contradictory evidence unresolved - require resolution
    </error>
    <error code="RAP004" severity="warning">
      Missing documentation - require findings documentation
    </error>
  </error_handling>
  
  <examples>
    <example name="framework_understanding">
      <description>Understanding a new framework or library</description>
      <code>
        GOALS: Understand React hooks for state management
        GATHER: Read docs, find examples, analyze patterns
        ANALYZE: Compare hooks vs class components
        VALIDATE: Test understanding with examples
        DOCUMENT: Create summary with recommendations
      </code>
      <expected_output>
        Comprehensive understanding of React hooks
        Clear recommendations for implementation
        Documented patterns and best practices
      </expected_output>
    </example>
    
    <example name="performance_investigation">
      <description>Investigating performance bottlenecks</description>
      <code>
        GOALS: Identify cause of slow API responses
        GATHER: Review logs, profiling data, system metrics
        ANALYZE: Identify patterns in performance issues
        VALIDATE: Test hypotheses with measurements
        DOCUMENT: Performance analysis with solutions
      </code>
      <expected_output>
        Root cause identification for performance issues
        Evidence-based solutions and optimizations
        Performance improvement recommendations
      </expected_output>
    </example>
  </examples>
  
</module>
```

## Anti-patterns to Avoid
- Starting implementation without research
- Relying on single source of information
- Ignoring existing patterns and conventions
- Incomplete analysis leading to wrong decisions
- Not documenting findings for future reference

## Research & Analysis Validation Checklist
- [ ] Research goals clearly defined with success criteria
- [ ] Multiple information sources consulted and cross-referenced
- [ ] Parallel searches executed for efficiency
- [ ] Analysis is comprehensive and balanced
- [ ] Findings validated through examples and testing
- [ ] Results documented for future reference