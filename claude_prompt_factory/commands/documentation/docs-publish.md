<command_file>
  <metadata>
    <name>/docs publish</name>
    <purpose>Deploys documentation to a hosting platform with automated building and versioning.</purpose>
    <usage>
      <![CDATA[
      /docs publish <target="github-pages">
      ]]>
    </usage>
  </metadata>

  <arguments>
    <argument name="target" type="string" required="false" default="github-pages">
      <description>The deployment platform to publish to (e.g., 'github-pages', 'netlify', 's3').</description>
    </argument>
  </arguments>
  
  <examples>
    <example>
      <description>Build and publish the documentation to GitHub Pages.</description>
      <usage>/docs publish</usage>
    </example>
    <example>
      <description>Publish the documentation to Netlify.</description>
      <usage>/docs publish target="netlify"</usage>
    </example>
  </examples>

  <claude_prompt>
    <prompt>
      You are a documentation deployment pipeline. The user wants to publish the project's documentation.

      1.  **Read Configuration**: Read `PROJECT_CONFIG.xml` to get the documentation build tool (e.g., MkDocs, Docusaurus) and the deployment configuration for the specified `target`.
      2.  **Generate Plan**: Create a step-by-step plan:
          *   Run the command to build the static documentation site.
          *   Run the command to deploy the built site to the target platform.
          *   Run a final verification step to check that the site is live.
      3.  **Propose Script**: Present the full script to the user for confirmation.
      4.  **Execute**: Upon approval, execute the script and report on the outcome.

      <include component="components/reporting/generate-structured-report.md" />
    </prompt>
  </claude_prompt>

  <dependencies>
    <uses_config_values>
      <value>documentation.build_tool</value>
      <value>documentation.deployment.target</value>
    </uses_config_values>
    <includes_components>
      <component>components/reporting/generate-structured-report.md</component>
    </includes_components>
  </dependencies>
</command_file>