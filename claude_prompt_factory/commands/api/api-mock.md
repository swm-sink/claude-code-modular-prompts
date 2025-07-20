# /api mock - Mock API Server Command

**Purpose**: Create a mock API server from an OpenAPI specification or a set of examples, enabling parallel development and testing.

## Usage
```bash
/api mock [spec_file] [--port=3001] [--delay=100]
```

## Workflow

The `/api mock` command follows a systematic process to create and run a mock API server.

```xml
<mock_api_workflow>
  <step name="Parse Specification">
    <description>Parse the provided OpenAPI specification or set of examples to understand the API's endpoints, schemas, and responses.</description>
    <tool_usage>
      <tool>Read</tool>
      <description>Read the API specification file.</description>
    </tool_usage>
  </step>
  
  <step name="Generate Mock Data">
    <description>Generate realistic mock data for the API's responses using faker libraries and other techniques to match the defined schemas.</description>
  </step>
  
  <step name="Set Up & Run Server">
    <description>Set up and run a mock API server (e.g., using Express or Fastify) that serves the generated mock data. The server will support configurable response delays, error rates, and authentication simulation.</description>
    <tool_usage>
      <tool>Bash</tool>
      <description>Run the mock API server.</description>
    </tool_usage>
  </step>
</mock_api_workflow>
```

## Features
- **Dynamic Data**: Uses Faker.js for realistic mock data.
- **Response Simulation**: Supports configurable delays and error rates.
- **RESTful Routes**: Simulates full CRUD operations with proper status codes.
- **Authentication**: Simulates JWT token-based authentication.
- **Pagination**: Supports page/limit parameters with metadata.
- **Filtering**: Supports basic query parameter filtering.
- **Rate Limiting**: Simulates API throttling.