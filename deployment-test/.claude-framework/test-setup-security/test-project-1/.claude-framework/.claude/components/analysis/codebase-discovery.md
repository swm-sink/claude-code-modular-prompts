<prompt_component>
  <step name="Comprehensive Codebase Discovery">
    <description>
      Perform systematic codebase discovery and analysis using standardized patterns.
      This extends find-relevant-code.md with deeper project structure analysis.
      Analyze project architecture, identify key directories, understand technology stack,
      and map component relationships for comprehensive understanding.
    </description>
    <discovery_process>
      1. **Project Structure Analysis**:
         - Scan root directory for configuration files (package.json, pom.xml, Cargo.toml, etc.)
         - Identify source directories (src/, app/, lib/, components/, etc.)
         - Locate test directories (tests/, test/, __tests__, spec/, etc.)
         - Find build/deployment configs (Dockerfile, .github/, .gitlab-ci.yml, etc.)

      2. **Technology Stack Detection**:
         - Analyze package managers and dependency files
         - Identify frameworks and libraries in use
         - Determine language versions and tooling
         - Detect architectural patterns (MVC, microservices, monorepo, etc.)

      3. **Code Organization Mapping**:
         - Map module/component hierarchies
         - Identify entry points and main files
         - Locate configuration and environment files
         - Find documentation and README files

      4. **Dependency Analysis**:
         - Map internal module dependencies
         - Identify external library usage
         - Detect circular dependencies or architectural issues
         - Understand data flow and component interactions
    </discovery_process>
    <output>
      Provide structured analysis:
      - **Project Type**: [web app/API/library/CLI tool/etc.]
      - **Technology Stack**: [languages, frameworks, tools]
      - **Architecture**: [monolith/microservices/serverless/etc.]
      - **Key Directories**: [src paths, test paths, config paths]
      - **Entry Points**: [main files, API endpoints, CLI commands]
      - **Important Files**: [configs, schemas, core components]
      
      Always prioritize understanding over exhaustive listing.
      Focus on files most relevant to the user's current task.
    </output>
  </step>
</prompt_component>