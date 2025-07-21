---
description: Standard codebase analysis for context priming with comprehensive project overview
argument-hint: "[analysis_depth] [focus_areas]"
allowed-tools: Read, Write, Edit, Bash, Grep
---

# /context prime - Codebase Context Priming

Comprehensive codebase analysis system for generating high-level project overview and context priming summary.

## Usage
```bash
/context prime                               # Standard comprehensive analysis
/context prime --quick                       # Quick overview for rapid understanding
/context prime --deep                        # Deep analysis with detailed insights
/context prime --focus security             # Focus on specific aspects
```

  <claude_prompt>
    <prompt>
      You are a codebase analysis tool. Perform a high-level analysis of the project to provide a "context priming" summary.

      1.  **Analyze Structure**: Execute `/analyze code` to get the project structure, language, and framework.
      2.  **Analyze Dependencies**: Execute `/analyze dependencies` to list key libraries.
      3.  **Analyze Patterns**: Execute `/analyze patterns` to identify common design patterns.
      4.  **Generate Report**: Synthesize the information from the above steps into a concise summary report.

      <include component="components/reporting/generate-structured-report.md" />
    </prompt>
  </claude_prompt>

  <dependencies>
    <chain>
      <command>/analyze code</command>
      <command>/analyze dependencies</command>
      <command>/analyze patterns</command>
    </chain>
    <includes_components>
      <component>components/reporting/generate-structured-report.md</component>
    </includes_components>
  </dependencies>
</command_file> 