# /api design - API Design & Specification Command

**Purpose**: Design RESTful or GraphQL APIs and generate comprehensive specifications and documentation.

## Usage
```bash
/api design "[description of API]" [--type=rest|graphql]
```

## Workflow

The `/api design` command follows a systematic process to design and specify APIs.

```xml
<api_design_workflow>
  <step name="Analyze Requirements">
    <description>Analyze the user's description of the desired API to understand the business needs, data models, and core functionality.</description>
  </step>
  
  <step name="Design Endpoints & Schema">
    <description>Design the RESTful resource endpoints or GraphQL schema, including the operations, parameters, and request/response models.</description>
  </step>
  
  <step name="Generate API Specification">
    <description>Generate a complete API specification in the OpenAPI or GraphQL schema format, including data models, authentication patterns, error handling, and versioning strategies.</description>
    <tool_usage>
      <tool>Write</tool>
      <description>Create the API specification file.</description>
    </tool_usage>
  </step>
</api_design_workflow>
```

## Key Features
- **Specification Generation**: Creates OpenAPI 3.0/3.1 or GraphQL schema specifications.
- **JSON Schema Validation**: Defines request/response models with JSON Schema.
- **Authentication & Authorization**: Includes patterns for authentication and authorization.
- **Error Handling**: Defines standardized error response formats.
- **Versioning**: Supports various versioning strategies.
- **Rate Limiting**: Includes definitions for rate limiting.