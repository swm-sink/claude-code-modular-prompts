# /init new - Initialize for a New Project

**Purpose**: Initialize the Prompt Factory for a new, empty project, with a focus on setting up a solid foundation for future development.

## Usage
```bash
/init new "[project description]"
```

## Workflow

The `/init new` command follows a systematic process to set up the Prompt Factory in a new project.

```xml
<init_new_workflow>
  <step name="Project Scaffolding">
    <description>Create a basic project scaffold, including a directory structure, a README.md file, a .gitignore file, and a license file.</description>
    <tool_usage>
      <tool>File System</tool>
      <description>Create the basic project scaffold.</description>
    </tool_usage>
  </step>
  
  <step name="Technology Stack Selection">
    <description>Based on your project description, I will recommend a technology stack (e.g., language, framework, database) and ask for your confirmation before proceeding.</description>
  </step>
  
  <step name="Configuration & Setup">
    <description>I will create a `PROJECT_CONFIG.xml` file tailored to the selected technology stack and set up a basic CI/CD pipeline for the project.</description>
    <tool_usage>
      <tool>File System & CI/CD</tool>
      <description>Create the configuration file and set up the CI/CD pipeline.</description>
    </tool_usage>
  </step>
  
  <step name="Boilerplate Generation">
    <description>I will generate boilerplate code for the core components of the application, including a basic application server, a sample API endpoint, and a simple test suite.</description>
    <tool_usage>
      <tool>Code Generation</tool>
      <description>Generate the boilerplate code.</description>
    </tool_usage>
  </step>
</init_new_workflow>
```

## Use Cases

*   **Greenfield Projects**: Quickly bootstrap a new project with a solid foundation.
*   **Prototyping**: Rapidly create a working prototype of a new application.
*   **Learning**: Explore a new technology stack by creating a simple, working project. 