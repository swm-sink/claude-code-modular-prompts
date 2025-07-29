---
description: Comprehensive API design with OpenAPI specification, best practices, and validation
argument-hint: "[api_type] [design_approach]"
allowed-tools: Read, Write, Edit, Bash, Grep
---

# /api design - API Design & Architecture

Advanced API design system with OpenAPI specification generation, RESTful best practices, and comprehensive validation.

## Usage
```bash
/api design rest                             # Design RESTful API architecture
/api design graphql                          # Design GraphQL API schema
/api design --openapi                        # Generate OpenAPI specification
/api design --validate                       # Validate API design patterns
```

## Arguments
- `description` (required): Natural language description of the API to design
- `type` (optional): API type - "rest" or "graphql" (default: "rest")

<command_file>
  <metadata>
    <name>/api design</name>
    <purpose>Designs RESTful or GraphQL APIs and generates comprehensive specifications and documentation.</purpose>
    <usage>
      <![CDATA[
      /api design "[description]" <type="rest">
      ]]>
    </usage>
  </metadata>

  <arguments>
    <argument name="description" type="string" required="true">
      <description>A natural language description of the API to be designed.</description>
    </argument>
    <argument name="type" type="string" required="false" default="rest">
      <description>The type of API to design ('rest' or 'graphql').</description>
    </argument>
  </arguments>
  
  <examples>
    <example>
      <description>Design a REST API for a simple user management system.</description>
      <usage>/api design "a user service with create, read, update, delete endpoints"</usage>
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
      <include>components/planning/create-step-by-step-plan.md</include>
      <include>components/reporting/generate-structured-report.md</include>
      <include>components/security/owasp-compliance.md</include>
      <include>components/validation/xml-structure.md</include>
      
      <![CDATA[
You are an expert API architect. The user wants you to design an API based on their description.

      1.  **Analyze Requirements**: Analyze the user's description to understand the business needs, data models, and core functionality.
      2.  **Design Endpoints & Schema**: Design the RESTful resource endpoints or GraphQL schema, including operations, parameters, and models.
      3.  **Generate API Specification**: Generate a complete API specification in OpenAPI 3.0 (for REST) or GraphQL schema format. Include data models, authentication patterns, and error handling.

      Your output should be the raw specification file content.
]]>
    </prompt>
  </claude_prompt>

  <dependencies>
    <!-- This command is self-contained -->
  </dependencies>
</command_file>