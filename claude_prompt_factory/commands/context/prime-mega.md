# /context prime-mega - Deep Multi-Agent Codebase Analysis

**Purpose**: Perform a comprehensive, deep codebase analysis using a sequence of specialized AI agents, compiling their findings into a master report with actionable insights.

## Usage
```bash
/context prime-mega
```

## Workflow

The `/context prime-mega` command follows a sophisticated, multi-phase process to conduct a deep analysis of the codebase.

```xml
<context_prime_mega_workflow>
  <step name="Phase 1: Assess & Plan">
    <description>First, I will assess the codebase size and complexity (small, medium, large, enterprise) by scanning the directory structure and counting files/lines of code. Based on this, I will determine the optimal number of specialized analysis agents required and present this plan to you for confirmation before proceeding.</description>
    <tool_usage>
      <tool>File System Analysis</tool>
      <description>Scan the project to determine its scale.</description>
    </tool_usage>
  </step>
  
  <step name="Phase 2: Sequential Agent Analysis">
    <description>I will execute a sequence of specialized AI agents, each building upon the findings of the previous one. Each agent will perform a deep analysis in its specific domain (e.g., Architecture, Dependencies, Security, Performance), documenting its findings in a detailed report before passing its conclusions to the next agent in the chain.</description>
    <agent_specializations>
      <small_codebase>Structure, Issues</small_codebase>
      <medium_codebase>Structure, Dependencies, Patterns, Issues</medium_codebase>
      <large_codebase>Architecture, Dependencies, Security, Performance, Patterns, Issues</large_codebase>
      <enterprise_codebase>Architecture, Services, Data, Security, Performance, Quality, Patterns, Issues</enterprise_codebase>
    </agent_specializations>
  </step>
  
  <step name="Phase 3: Compile Master Report">
    <description>After all agents have completed their analysis, I will aggregate all individual findings into a single, unified structure. I will perform a cross-agent analysis to identify reinforcing or conflicting findings, prioritize all identified issues by severity and impact, and generate a final, comprehensive master analysis report.</description>
    <output>A master analysis report including an executive summary, detailed findings, and an actionable improvement roadmap.</output>
  </step>
</context_prime_mega_workflow>
```

## Use Cases

*   **Deep Architectural Review**: Get a comprehensive, multi-faceted understanding of a project's architecture before a major redesign.
*   **Pre-Release Audit**: Perform a full audit of a project's security, performance, and quality before a major release.
*   **Strategic Technical Planning**: Generate a detailed technical debt assessment and an actionable roadmap for long-term improvements. 