---
description: Performs a comprehensive, deep codebase analysis using specialized agents
argument-hint: ""
allowed-tools: Bash, Read, Grep, Glob, Task
---

# /context prime-mega - Master Project Auditor

Performs a comprehensive, deep codebase analysis using a sequence of specialized analysis agents.

## Usage
```bash
/context prime-mega  # Run complete multi-agent analysis
```

## What It Does
1. **Assess & Plan**: Analyzes project scale and creates analysis plan
2. **Request Confirmation**: Presents plan for user approval
3. **Execute Analysis**: Runs specialized commands in sequence
4. **Synthesize Report**: Creates comprehensive master analysis report

<command_file>
  <metadata>
    <name>/context prime-mega</name>
    <purpose>Performs a comprehensive, deep codebase analysis using a sequence of specialized agents.</purpose>
    <usage>
      <![CDATA[
      /context prime-mega
      ]]>
    </usage>
  </metadata>

  <arguments>
    <!-- No arguments -->
  </arguments>
  
  <examples>
    <example>
      <description>Run a deep, multi-agent analysis on the current project.</description>
      <usage>/context prime-mega</usage>
    </example>
  </examples>

  <claude_prompt>
    <prompt>
      <!-- Standard DRY Components -->
      <include>components/validation/input-validation.md</include>
      <include>components/workflow/command-execution.md</include>
      <include>components/workflow/error-handling.md</include>
      <include>components/interaction/progress-reporting.md</include>
      
      <!-- Command-specific components -->
      <include>components/interaction/request-user-confirmation.md</include>
      <include>components/reporting/generate-structured-report.md</include>
      <include>components/orchestration/agent-orchestration.md</include>
      <include>components/analysis/codebase-discovery.md</include>
      <include>components/planning/create-step-by-step-plan.md</include>
      
      <![CDATA[
      You are a master project auditor. Your task is to perform a deep, multi-faceted analysis of the entire codebase by orchestrating a team of specialized analysis agents (commands).

      1.  **Assess & Plan**:
          *   First, get a sense of the project's scale (e.g., small, medium, large, enterprise) by analyzing the file count and directory structure.
          *   Based on the scale, propose a multi-phase analysis plan listing the specialized commands you will run (e.g., for a large project, you might propose running `/analyze code`, `/analyze dependencies`, `/security scan`, and `/analyze performance`).

      2.  **Request Confirmation**:
          *   Present this plan to the user for approval before proceeding.

      3.  **Execute Analysis Chain**:
          *   Upon confirmation, execute the planned sequence of analysis commands, capturing the output from each.

      4.  **Synthesize Master Report**:
          *   Aggregate all findings from the individual command reports.
          *   Perform a cross-analysis to identify reinforcing or conflicting findings.
          *   Prioritize all identified issues by severity and impact.
          *   Generate a final, comprehensive master analysis report with an executive summary and an actionable improvement roadmap.
      ]]>
    </prompt>
  </claude_prompt>

  <dependencies>
    <invokes_commands>
      <command>/analyze code</command>
      <command>/analyze dependencies</command>
      <command>/analyze patterns</command>
      <command>/analyze performance</command>
      <command>/security scan</command>
      <command>/quality report</command>
    </invokes_commands>
    <includes_components>
      <!-- <component>components/interaction/request-user-confirmation.md</component> -->
      <!-- <component>components/reporting/generate-structured-report.md</component> -->
    </includes_components>
  </dependencies>
</command_file> 