<command_file>
  <metadata>
    <name>/ci setup</name>
    <purpose>Initializes a CI/CD pipeline for the project, with support for multiple platforms and automated testing.</purpose>
    <usage>
      <![CDATA[
      /ci setup <platform>
      ]]>
    </usage>
  </metadata>

  <arguments>
    <argument name="platform" type="string" required="true">
      <description>The CI/CD platform to set up (e.g., 'github', 'gitlab').</description>
    </argument>
  </arguments>
  
  <examples>
    <example>
      <description>Set up a standard CI pipeline for GitHub Actions.</description>
      <usage>/ci setup "github"</usage>
    </example>
  </examples>

  <claude_prompt>
    <prompt>
      You are a CI/CD engineer. The user wants to set up a new CI pipeline for their project.

      1.  **Detect Project Type**: Analyze the project to determine the language and framework.
      2.  **Generate Pipeline Configuration**: Based on the project type and the specified `platform`, generate a complete, best-practice pipeline configuration file (e.g., `.github/workflows/main.yml`). The pipeline should include standard stages:
          *   Checkout code
          *   Install dependencies (with caching)
          *   Lint and format check
          *   Run unit and integration tests
          *   Build the application
          *   (Optional) A placeholder for deployment.
      3.  **Present Configuration**: Output the full configuration file content for the user to review and save.
    </prompt>
  </claude_prompt>

  <dependencies>
    <!-- This command is self-contained but analyzes the project structure -->
  </dependencies>
</command_file>