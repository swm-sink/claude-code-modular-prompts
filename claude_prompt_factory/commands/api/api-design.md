---
description: Designs RESTful or GraphQL APIs and generates comprehensive specifications
argument-hint: "[description] [type]"
allowed-tools: Write, Read
---

# /api design - API Design & Specification

Designs RESTful or GraphQL APIs and generates comprehensive specifications and documentation.

## Usage
```bash
/api design "user management with CRUD endpoints"     # REST API (default)
/api design "social media API" type="graphql"         # GraphQL API
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
      You are an expert API architect. The user wants you to design an API based on their description.

      1.  **Analyze Requirements**: Analyze the user's description to understand the business needs, data models, and core functionality.
      2.  **Design Endpoints & Schema**: Design the RESTful resource endpoints or GraphQL schema, including operations, parameters, and models.
      3.  **Generate API Specification**: Generate a complete API specification in OpenAPI 3.0 (for REST) or GraphQL schema format. Include data models, authentication patterns, and error handling.

      Your output should be the raw specification file content.
    </prompt>
  </claude_prompt>

  <dependencies>
    <!-- This command is self-contained -->
  </dependencies>
</command_file>