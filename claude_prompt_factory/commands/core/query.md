---
description: Intelligent codebase query system with semantic search and context-aware analysis
argument-hint: "[question_or_search_term]"
allowed-tools: Read, Write, Edit, Bash, Grep
---

# /query - Intelligent Codebase Query

Advanced query system with semantic search, pattern recognition, and context-aware code analysis.

## Usage
```bash
/query "how does authentication work?"       # Semantic question about codebase
/query "find all database models"           # Search for specific patterns
/query "what are the API endpoints?"        # Functional queries
/query "security vulnerabilities"           # Risk assessment queries
```

<analysis_workflow>
  <step name="Intent Parsing">
    <description>Understand the core question being asked and extract key terms and concepts.</description>
  </step>
  
  <step name="Parallel Search">
    <description>Use multiple search strategies simultaneously to quickly locate relevant information.</description>
    <strategies>
      <strategy name="Keyword Search">Use grep for direct keywords from the user's query.</strategy>
      <strategy name="Pattern Search">Use grep with regular expressions for common patterns.</strategy>
      <strategy name="File Discovery">Use glob to find relevantly named files (e.g., `*auth*`, `*user*`).</strategy>
      <strategy name="Config Search">Search for keywords within configuration files in the root directory.</strategy>
    </strategies>
  </step>
  
  <step name="Context Gathering">
    <description>For each relevant file found, gather additional context to build a complete picture. This includes reading file contents, finding dependencies, and locating associated tests.</description>
  </step>
  
  <step name="Synthesis">
    <description>Analyze the gathered information to identify common patterns and synthesize a comprehensive answer.</description>
    <include component="components/context/find-relevant-code.md" />
    <include component="components/analysis/codebase-discovery.md" />
    <include component="components/context/adaptive-thinking.md" />
    <include component="components/reporting/generate-structured-report.md" />
  </step>
</analysis_workflow>

<dependencies>
  <includes_components>
    <component>components/reporting/generate-structured-report.md</component>
  </includes_components>
  <uses_config_values>
    <value>command_settings.command#query.max_results</value>
    <value>command_settings.command#query.semantic_search</value>
  </uses_config_values>
</dependencies> 