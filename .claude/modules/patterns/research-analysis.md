<module name="research_analysis" category="patterns">

<purpose>
  Conduct research-only operations without making code changes - for understanding before acting.
</purpose>

<trigger_conditions>
  <condition type="explicit">User requests research or analysis without implementation</condition>
  <condition type="intelligence_gathering">Need to understand codebase, requirements, or context before changes</condition>
</trigger_conditions>

<implementation>
  
  <phase name="research_scope" order="1">
    <requirements>
      Define clear research questions and scope boundaries
      Identify information sources and search strategies
      Establish what decisions depend on research findings
    </requirements>
    <actions>
      Use WebSearch for current best practices and standards
      Use Glob and Grep for targeted codebase exploration
      Use Read for understanding existing implementations
      Document research questions and success criteria
    </actions>
    <validation>
      Research scope clearly defined with specific questions
      Information sources identified and accessible
      Decision criteria established for research outcomes
    </validation>
  </phase>
  
  <phase name="information_gathering" order="2">
    <requirements>
      Systematic exploration of identified information sources
      Evidence-based analysis with source attribution
      Cross-referencing multiple sources for validation
    </requirements>
    <actions>
      Execute parallel searches across multiple sources
      Document findings with source links and context
      Identify patterns, gaps, and conflicting information
      Validate findings through triangulation
    </actions>
    <validation>
      Comprehensive information gathered from multiple sources
      All findings documented with proper attribution
      Conflicting information identified and analyzed
    </validation>
  </phase>
  
  <phase name="analysis_synthesis" order="3">
    <requirements>
      Synthesize findings into actionable insights
      Identify implications and recommendations
      Document assumptions and limitations
    </requirements>
    <actions>
      Analyze patterns and trends in gathered information
      Synthesize insights relevant to original questions
      Generate recommendations with supporting evidence
      Document limitations and areas needing further research
    </actions>
    <validation>
      Clear insights derived from research findings
      Recommendations supported by evidence
      Limitations and assumptions clearly documented
    </validation>
  </phase>
  
</implementation>

<research_patterns>
  <pattern name="codebase_exploration" usage="understanding_existing_code">
    <tools>Glob, Grep, Read in parallel for comprehensive coverage</tools>
    <approach>Start broad, then narrow focus based on findings</approach>
    <documentation>Architecture overview, key patterns, integration points</documentation>
  </pattern>
  
  <pattern name="technology_research" usage="evaluating_options">
    <tools>WebSearch for current standards and best practices</tools>
    <approach>Compare multiple sources, look for consensus and conflicts</approach>
    <documentation>Option comparison, pros/cons, recommendation rationale</documentation>
  </pattern>
  
  <pattern name="requirement_analysis" usage="understanding_needs">
    <tools>Read for existing requirements, WebSearch for standards</tools>
    <approach>Gap analysis between current state and requirements</approach>
    <documentation>Requirement gaps, implementation complexity, risk assessment</documentation>
  </pattern>
</research_patterns>

<quality_standards>
  <standard name="evidence_based">All findings supported by credible sources</standard>
  <standard name="comprehensive">Multiple sources consulted and cross-referenced</standard>
  <standard name="actionable">Research leads to clear recommendations</standard>
  <standard name="documented">Findings and sources properly documented</standard>
</quality_standards>

<integration_points>
  <depends_on>
    Native Claude Code tools (WebSearch, Glob, Grep, Read)
    Critical thinking frameworks for analysis
  </depends_on>
  <provides_to>
    development/task-management.md for informed implementation
    patterns/intelligent-routing.md for decision making
    All commands requiring research before action
  </provides_to>
</integration_points>

</module>