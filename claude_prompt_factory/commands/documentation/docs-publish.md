# /docs publish - Documentation Deployment Command

**Purpose**: Deploy documentation to hosting platforms with automated building, versioning, and verification.

## Usage
```bash
/docs publish [target] [--version=v1.2.0] [--build=mkdocs]
```

## Workflow

The `/docs publish` command follows a systematic process to build and deploy documentation.

```xml
<docs_publish_workflow>
  <step name="Build Documentation">
    <description>Generate a static site from the documentation source using the specified build system (e.g., MkDocs, Sphinx, Docusaurus, GitBook).</description>
    <tool_usage>
      <tool>Bash</tool>
      <description>Run the build command for the selected system.</description>
    </tool_usage>
  </step>
  <step name="Version Management">
    <description>Tag and organize the documentation by version, if a version is specified.</description>
  </step>
  <step name="Asset Optimization">
    <description>Optimize assets (images, CSS, JS) for fast loading and SEO.</description>
  </step>
  <step name="Deploy">
    <description>Deploy the built documentation to the specified target platform (e.g., GitHub Pages, Netlify, Vercel, S3, local).</description>
    <tool_usage>
      <tool>Bash</tool>
      <description>Run the deployment command for the selected platform.</description>
    </tool_usage>
  </step>
  <step name="Verify Deployment">
    <description>Test the deployment and update links as needed.</description>
  </step>
</docs_publish_workflow>
```

## Features
- Automated CI/CD integration
- Multi-environment deployments
- SEO optimization
- Search indexing
- Analytics integration
- Custom domain configuration

Delegate to: @modules/documentation/deployment-orchestrator.md