<prompt_component>
  <step name="Dependency Analysis and Mapping">
    <description>
      Perform standardized dependency analysis across projects and programming languages.
      Map internal module dependencies, external library usage, and architectural relationships.
      Identify potential issues like circular dependencies, version conflicts, and security vulnerabilities.
    </description>
    <analysis_process>
      1. **Dependency File Discovery**:
         - package.json, package-lock.json (Node.js)
         - requirements.txt, Pipfile, pyproject.toml (Python)
         - Cargo.toml, Cargo.lock (Rust)
         - pom.xml, build.gradle (Java)
         - go.mod, go.sum (Go)
         - composer.json (PHP)

      2. **Internal Dependency Mapping**:
         - Analyze import/require statements
         - Map module-to-module relationships
         - Identify core vs peripheral modules
         - Detect circular dependencies

      3. **External Dependency Analysis**:
         - List direct vs transitive dependencies
         - Check for version conflicts
         - Identify outdated packages
         - Flag security vulnerabilities

      4. **Architecture Insights**:
         - Identify tightly coupled components
         - Suggest refactoring opportunities
         - Map data flow patterns
         - Detect architectural smells
    </analysis_process>
    <output>
      Provide structured dependency analysis:
      
      **Dependency Overview**:
      - **Total Dependencies**: [count direct/transitive]
      - **Dependency Managers**: [npm, pip, cargo, etc.]
      - **Major Frameworks**: [React, Django, Express, etc.]
      
      **Internal Dependencies**:
      - **Core Modules**: [main application modules]
      - **Shared Utilities**: [common utility modules]
      - **Circular Dependencies**: [if any found]
      
      **External Dependencies**:
      - **Production**: [critical runtime dependencies]
      - **Development**: [build tools, testing frameworks]
      - **Outdated**: [packages needing updates]
      - **Security Issues**: [vulnerable packages]
      
      **Recommendations**:
      - [Architecture improvements]
      - [Dependency cleanup suggestions]
      - [Security update priorities]
    </output>
  </step>
</prompt_component>