<command_file>
  <metadata>
    <name>/analyze dependencies</name>
    <purpose>Scans project dependencies for vulnerabilities, license issues, and optimization opportunities.</purpose>
    <usage>
      <![CDATA[
      /analyze dependencies
      ]]>
    </usage>
  </metadata>

  <arguments>
    <!-- This command takes no direct arguments; it reads from the config. -->
  </arguments>
  
  <examples>
    <example>
      <description>Run a full dependency analysis on the project.</description>
      <usage>/analyze dependencies</usage>
    </example>
  </examples>

  <claude_prompt>
    <prompt>
      You are a security and performance specialist. The user wants to analyze their project's dependencies.
      Your goal is to map the dependency tree, identify security and license issues, find circular dependencies, and suggest optimizations.

      First, identify the dependency manifest file (e.g., `${tech_stack.package_managers.manager#python.manifest}`).

      Then, perform the following analysis:
      1.  **Dependency Mapping**: Trace and list all direct and transitive dependencies.
      2.  **Security Analysis**: Scan for known vulnerabilities (CVEs) and check for license compliance issues.
      3.  **Circular Dependency Detection**: Analyze imports to find and report any circular dependencies.
      4.  **Optimization Opportunities**: Identify unused dependencies, duplicate packages, and opportunities to reduce bundle size.

      <include component="components/reporting/generate-structured-report.md" />
    </prompt>
  </claude_prompt>

  <dependencies>
    <includes_components>
      <component>components/reporting/generate-structured-report.md</component>
    </includes_components>
    <uses_config_values>
      <value>tech_stack.package_managers.manager#python.manifest</value>
      <value>tech_stack.package_managers.manager#javascript.manifest</value>
    </uses_config_values>
  </dependencies>
</command_file>