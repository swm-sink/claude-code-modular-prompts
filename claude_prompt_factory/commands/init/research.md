# /init research - Initialize for a Research Project

**Purpose**: Initialize the Prompt Factory for a research-focused project, with a focus on setting up a structured environment for experimentation, data analysis, and knowledge management.

## Usage
```bash
/init research "[research topic]"
```

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