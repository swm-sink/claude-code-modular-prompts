---
description: Creates a mock API server from OpenAPI specification for parallel development and testing
argument-hint: "[spec_file]"
allowed-tools: Read, Write, Bash
---

# /api mock - Mock API Server Generator

Creates a mock API server from an OpenAPI specification or examples for parallel development and testing.

## Usage
```bash
/api mock "docs/api/openapi.json"     # Generate mock server from OpenAPI spec
/api mock "swagger.yaml"              # Generate from YAML specification
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