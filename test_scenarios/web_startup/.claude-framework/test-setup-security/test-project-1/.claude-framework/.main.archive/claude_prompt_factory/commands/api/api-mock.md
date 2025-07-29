---
description: API mocking and simulation with realistic data generation and behavior simulation
argument-hint: "[mock_type] [data_strategy]"
allowed-tools: Read, Write, Edit, Bash, Grep
---

# /api mock - API Mocking & Simulation

Advanced API mocking system with realistic data generation, behavior simulation, and comprehensive testing support.

## Usage
```bash
/api mock server                             # Create mock API server
/api mock endpoints                          # Mock specific endpoints
/api mock --realistic                        # Generate realistic mock data
/api mock --dynamic                          # Dynamic behavior simulation
```

## Arguments
- `spec_file` (required): Path to OpenAPI specification file (JSON or YAML)

## What It Does
1. **Parse Specification**: Reads OpenAPI spec to understand endpoints and schemas
2. **Generate Mock Data**: Creates realistic data matching defined schemas
3. **Set Up Server**: Provides code for mock server with configurable delays and errors

<command_file>
  <metadata>
    <name>/api mock</name>
    <purpose>Creates a mock API server from an OpenAPI specification or examples for parallel development and testing.</purpose>
    <usage>
      <![CDATA[
      /api mock <spec_file>
      ]]>
    </usage>
  </metadata>

  <arguments>
    <argument name="spec_file" type="string" required="true">
      <description>Path to the OpenAPI specification file (e.g., `openapi.json`).</description>
    </argument>
  </arguments>
  
  <examples>
    <example>
      <description>Create a mock server from a local OpenAPI file.</description>
      <usage>/api mock "docs/api/openapi.json"</usage>
    </example>
  </examples>

  <claude_prompt>
    <prompt>
      <!-- Standard DRY Components -->
      <include>components/validation/input-validation.md</include>
      <include>components/workflow/command-execution.md</include>
      <include>components/workflow/error-handling.md</include>
      <include>components/interaction/progress-reporting.md</include>
      
      <!-- Command-specific components -->
      <include>components/actions/apply-code-changes.md</include>
      <include>components/testing/test-integration.md</include>
      <include>components/reporting/generate-structured-report.md</include>
      
      <![CDATA[
You are a mock server generator. The user wants to create a mock API server from a specification file.

      1.  **Parse Specification**: Parse the provided OpenAPI specification to understand the endpoints, schemas, and responses.
      2.  **Generate Mock Data**: Generate realistic mock data for the API's responses that matches the defined schemas.
      3.  **Set Up & Run Server**: Provide the code for a simple mock server (e.g., using Express.js or FastAPI) that serves the generated mock data. The server should support configurable response delays and error rates.

      Your output should be the code for the mock server.
]]>
    </prompt>
  </claude_prompt>

  <dependencies>
    <!-- This command is self-contained -->
  </dependencies>
</command_file>