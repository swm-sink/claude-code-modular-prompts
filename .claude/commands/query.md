| version | last_updated | status |
|---------|--------------|--------|
| 2.3.1   | 2025-07-08   | stable |

# /query - Research & Analysis ONLY (Zero Modifications)

────────────────────────────────────────────────────────────────────────────────

> **⚡ Clear Purpose**: Researches and explains code WITHOUT creating any files. Want to CREATE documentation? Use `/docs` instead!

────────────────────────────────────────────────────────────────────────────────

```xml
<command purpose="Read-only investigation with deep analysis patterns">
  
  <delegation target="modules/development/research-analysis.md">
    Parallel search → Deep analysis → Pattern mapping → Comprehensive report
  </delegation>
  
  <thinking_pattern enforcement="MANDATORY">
    <checkpoint id="1" verify="true" enforcement="BLOCKING">
      <action>Parse query and identify key search terms with TDD awareness</action>
      <critical_thinking>
        - What specifically is being asked about?
        - Is this a request for code analysis or code creation?
        - Should I analyze existing tests or testing patterns?
        - Am I being asked to understand vs modify?
      </critical_thinking>
      <output_format>QUERY_ANALYSIS: [research_type] seeking [information_type] (TDD relevance: [none/analysis_only])</output_format>
      <validation>Query clearly identified as research-only with no modification intent</validation>
      <enforcement>BLOCK if query requests code modifications - route to appropriate command</enforcement>
    </checkpoint>
    <checkpoint id="2" verify="true" enforcement="BLOCKING">
      <action>Execute parallel search operations for maximum efficiency</action>
      <critical_thinking>
        - Which files/patterns should I search simultaneously?
        - Should I include test files in my search for comprehensive understanding?
        - Can I batch Grep/Glob operations for 70% performance improvement?
        - What search terms will give the most relevant results?
      </critical_thinking>
      <output_format>PARALLEL_SEARCH: Grep([patterns]) + Glob([files]) + Read([priority_files])</output_format>
      <validation>Multiple search operations executed in parallel for efficiency</validation>
      <enforcement>VERIFY parallel execution used - sequential searches are inefficient</enforcement>
    </checkpoint>
    <checkpoint id="3" verify="true" enforcement="BLOCKING">
      <action>Read and analyze relevant files with smart prioritization</action>
      <critical_thinking>
        - Which files contain the most relevant information?
        - Should I analyze both implementation and test files for complete understanding?
        - Are there architectural patterns I should understand first?
        - What dependencies and relationships should I map?
      </critical_thinking>
      <output_format>ANALYSIS_PRIORITY: [high_priority_files] → [supporting_files] → [context_files]</output_format>
      <validation>Files read in logical priority order for efficient understanding</validation>
      <enforcement>ENSURE comprehensive analysis without overwhelming detail</enforcement>
    </checkpoint>
    <checkpoint id="4" verify="true" enforcement="BLOCKING">
      <action>Analyze patterns, dependencies, and architectural relationships</action>
      <critical_thinking>
        - What patterns emerge from the code structure?
        - How do components relate and depend on each other?
        - Are there test patterns that reveal implementation intent?
        - What architectural decisions can I infer?
      </critical_thinking>
      <output_format>PATTERN_ANALYSIS: [identified_patterns] with [relationships] and [dependencies]</output_format>
      <validation>Comprehensive analysis revealing structure and design decisions</validation>
      <enforcement>ENSURE analysis depth matches query complexity</enforcement>
    </checkpoint>
    <checkpoint id="5" verify="true" enforcement="BLOCKING">
      <action>Generate comprehensive report with concrete examples</action>
      <critical_thinking>
        - How can I best explain the findings clearly?
        - What specific code examples illustrate the patterns?
        - Should I include test examples to show expected behavior?
        - How can I structure the report for maximum usefulness?
      </critical_thinking>
      <output_format>RESEARCH_REPORT: Comprehensive analysis with examples and explanations</output_format>
      <validation>Report provides clear, actionable insights with concrete examples</validation>
      <enforcement>CRITICAL: ZERO modifications made - analysis and reporting ONLY</enforcement>
    </checkpoint>
  </thinking_pattern>
  
  <examples>
    /query "How does authentication work?"  # Researches auth patterns, explains code
    /query "Find Repository pattern uses"   # Analyzes pattern usage across codebase
    /query "Identify security issues"       # Security analysis with NO modifications
    /query "Performance bottlenecks"        # Code analysis for optimization opportunities
    /query "Explain the data flow"          # Investigates and explains architecture
  </examples>
  
  <anti_examples>
    ❌ /query "create API documentation"         # Use /docs instead!
    ❌ /query "generate setup guide"             # Use /docs instead!
    ❌ /query "write security guidelines"        # Use /docs instead!
    ✅ /query "how does the security system work?" # Perfect for research!
  </anti_examples>
  
  <rules enforcement="STRICT">
    <rule priority="CRITICAL">ZERO modifications - read-only analysis ONLY</rule>
    <rule priority="CRITICAL">Use parallel tool calls for search efficiency</rule>
    <rule priority="HIGH">Comprehensive analysis with code examples</rule>
    <rule priority="HIGH">Cross-reference with documentation</rule>
  </rules>
  
  <tdd_integration enforcement="MANDATORY">
    <read_only_analysis>No TDD enforcement needed - analysis and research ONLY</read_only_analysis>
    <test_pattern_analysis>Include existing test files in analysis for comprehensive understanding</test_pattern_analysis>
    <tdd_awareness>Understand and explain existing TDD patterns when analyzing code structure</tdd_awareness>
    <validation>Reference quality/tdd.md#analysis_patterns for test-aware research</validation>
    <blocking_conditions>
      <condition>Any attempt to modify files or create new code</condition>
      <condition>Query requesting code generation rather than analysis</condition>
      <condition>Analysis bypassing existing test files that would provide insight</condition>
      <condition>Research conclusions that would require code changes to verify</condition>
    </blocking_conditions>
  </tdd_integration>
  
  <module_execution enforcement="MANDATORY">
    <core_stack order="sequential">
      <module>quality/critical-thinking.md - 30-second analysis before research approach</module>
      <module>development/research-analysis.md - Comprehensive analysis workflow</module>
      <module>patterns/pattern-library.md - Pattern recognition and search strategies</module>
      <module>quality/tdd.md - Test-aware analysis for complete understanding</module>
    </core_stack>
    <contextual_modules>
      <conditional module="patterns/intelligent-routing.md" condition="query_scope_unclear"/>
      <conditional module="security/threat-modeling.md" condition="security_analysis"/>
      <conditional module="development/documentation.md" condition="documentation_analysis"/>
    </contextual_modules>
  </module_execution>
  
  <pattern_usage>
    • Uses parallel_execution for Grep/Glob operations (70% faster)
    • Implements smart_memoization for repeated queries
    • Applies three_x_rule for thorough analysis
    • Leverages consequence_mapping for impact assessment
    • Uses pattern-library.md search patterns
    
    See modules/patterns/pattern-library.md for pattern details
    See modules/development/research-analysis.md for full implementation
  </pattern_usage>
  
</command>
```