---
description: Intelligent existing project analysis with auto-configuration, optimization recommendations, and integration setup
argument-hint: "[project_path] [analysis_depth]"
allowed-tools: Read, Write, Edit, Bash, Grep
---

<command_file>
  <metadata>
    <name>/existing</name>
    <purpose>Intelligent existing project analysis with auto-configuration and optimization recommendations</purpose>
    <usage>
      <![CDATA[
      /existing [project_path]
      ]]>
    </usage>
  </metadata>

  <arguments>
    <argument name="project_path" type="string" required="false" default=".">
      <description>Path to the existing project to analyze. Defaults to current directory.</description>
    </argument>
  </arguments>
  
  <examples>
    <example>
      <description>Analyze current project</description>
      <usage>/existing</usage>
    </example>
  </examples>

  <claude_prompt>
    <prompt>
You are an intelligent project analyzer. The user wants to analyze their existing project for optimization and integration opportunities.

**Analysis Process:**
1. **Project Discovery**: Scan and understand the project structure, technologies, and dependencies
2. **Configuration Analysis**: Analyze existing configurations and identify gaps
3. **Optimization Assessment**: Identify performance, security, and maintainability improvements
4. **Integration Planning**: Plan Claude Code Prompt Factory integration
5. **Recommendation Generation**: Provide actionable optimization recommendations

**Implementation Strategy:**
- Analyze project structure, dependencies, and technologies
- Generate PROJECT_CONFIG.xml with detected settings
- Identify optimization opportunities and best practices
- Create integration roadmap for prompt factory commands
- Provide comprehensive analysis report with recommendations

<include component="components/analysis/codebase-discovery.md" />
<include component="components/planning/create-step-by-step-plan.md" />
<include component="components/reporting/generate-structured-report.md" />
    </prompt>
  </claude_prompt>

  <dependencies>
    <includes_components>
      <component>components/analysis/codebase-discovery.md</component>
      <component>components/planning/create-step-by-step-plan.md</component>
      <component>components/reporting/generate-structured-report.md</component>
    </includes_components>
  </dependencies>
</command_file> 