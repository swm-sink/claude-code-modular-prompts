---
description: Advanced research framework with intelligent information gathering, analysis synthesis, and knowledge discovery
argument-hint: "[research_domain] [depth_level]"
allowed-tools: Read, Write, Edit, Bash, Grep
---

# /research - Advanced Research Framework

Sophisticated research system with intelligent information gathering, comprehensive analysis synthesis, and automated knowledge discovery.

## Usage
```bash
/research technology                         # Technology research and analysis
/research --academic                         # Academic research methodology
/research --market                           # Market research and trends
/research --comprehensive                    # Comprehensive multi-domain research
```

<command_file>
  <metadata>
    <n>/research</n>
    <purpose>Advanced research framework with intelligent information gathering, analysis synthesis, and knowledge discovery</purpose>
    <usage>
      <![CDATA[
      /research [research_domain]
      ]]>
    </usage>
  </metadata>

  <arguments>
    <argument name="research_domain" type="string" required="false" default="technology">
      <description>Domain of research to conduct</description>
    </argument>
    <argument name="depth_level" type="string" required="false" default="comprehensive">
      <description>Depth level of research analysis</description>
    </argument>
  </arguments>
  
  <examples>
    <example>
      <description>Technology research and analysis</description>
      <usage>/research technology</usage>
    </example>
    <example>
      <description>Academic research methodology</description>
      <usage>/research --academic</usage>
    </example>
  </examples>

  <claude_prompt>
    <prompt>
You are an advanced research specialist. The user wants to conduct comprehensive research with intelligent information gathering and analysis synthesis.

**Research Process:**
1. **Domain Analysis**: Analyze the research domain and define scope
2. **Information Gathering**: Systematic collection of relevant information and sources
3. **Analysis Synthesis**: Synthesize findings into coherent insights
4. **Knowledge Discovery**: Identify patterns, trends, and breakthrough insights
5. **Report Generation**: Create comprehensive research reports and recommendations

**Implementation Strategy:**
- Conduct systematic literature reviews and source analysis
- Apply advanced research methodologies and frameworks
- Synthesize information from multiple sources and perspectives
- Generate actionable insights and recommendations
- Create comprehensive documentation and knowledge bases

<include component="components/analytics/business-intelligence.md" />
<include component="components/reasoning/tree-of-thoughts.md" />
<include component="components/reporting/generate-structured-report.md" />
    </prompt>
  </claude_prompt>

  <dependencies>
    <includes_components>
      <component>components/analytics/business-intelligence.md</component>
      <component>components/reasoning/tree-of-thoughts.md</component>
      <component>components/reporting/generate-structured-report.md</component>
    </includes_components>
    <uses_config_values>
      <value>research.domains.preferred</value>
      <value>analysis.depth.default</value>
    </uses_config_values>
  </dependencies>
</command_file>

## Workflow

The `/init research` command follows a systematic process to set up the Prompt Factory for a research project.

```xml
<init_research_workflow>
  <step name="Research Scaffolding">
    <description>Create a structured directory for the research project, including folders for data, notebooks, papers, and presentations. I will also create a `README.md` file with a template for documenting the research project.</description>
    <tool_usage>
      <tool>File System</tool>
      <description>Create the research project scaffold.</description>
    </tool_usage>
  </step>
  
  <step name="Tooling & Environment Setup">
    <description>Based on the research topic, I will recommend and set up the appropriate tools and environment for the project. This may include setting up a virtual environment with the necessary libraries, configuring a Jupyter notebook server, or setting up a data visualization dashboard.</description>
    <tool_usage>
      <tool>Environment Setup</tool>
      <description>Set up the research environment.</description>
    </tool_usage>
  </step>
  
  <step name="Knowledge Management Setup">
    <description>I will set up a knowledge management system for the project, including a Zotero library for managing references, an Obsidian vault for taking notes, and a private GitHub repository for sharing the research with collaborators.</description>
    <tool_usage>
      <tool>Knowledge Management Setup</tool>
      <description>Set up the knowledge management system.</description>
    </tool_usage>
  </step>
</init_research_workflow>
```

## Use Cases

*   **Academic Research**: Set up a structured environment for a new academic research project.
*   **Data Science Projects**: Create a reproducible environment for a data science project, with a focus on data analysis and visualization.
*   **Personal Knowledge Management**: Use the Prompt Factory to create a structured system for managing your personal knowledge and research. 