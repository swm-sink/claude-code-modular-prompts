<command_file>
  <metadata>
    <name>/api test</name>
    <purpose>Performs comprehensive testing of API endpoints, including functional and performance validation.</purpose>
    <usage>
      <![CDATA[
      /api test "[endpoint]" <method="GET">
      ]]>
    </usage>
  </metadata>

  <arguments>
    <argument name="endpoint" type="string" required="true">
      <description>The full URL of the API endpoint to test.</description>
    </argument>
    <argument name="method" type="string" required="false" default="GET">
      <description>The HTTP method to use (GET, POST, PUT, DELETE, etc.).</description>
    </argument>
  </arguments>
  
  <examples>
    <example>
      <description>Perform a GET request to a user endpoint.</description>
      <usage>/api test "https://api.example.com/users/123"</usage>
    </example>
    <example>
      <description>Perform a POST request to create a user.</description>
      <usage>/api test "https://api.example.com/users" method="POST"</usage>
    </example>
  </examples>

  <claude_prompt>
    <prompt>
      You are an API testing tool. The user wants to test an API endpoint.

      1.  **Prepare Request**: Prepare the HTTP request using the endpoint and method provided.
      2.  **Execute Request**: Use `curl` to send the request. Monitor the response time, status code, and any errors.
      3.  **Analyze Response**: Validate the response schema and data integrity.
      4.  **Generate Report**: Generate a detailed test report.

      <include component="components/reporting/generate-structured-report.md" />
    </prompt>
  </claude_prompt>

  <dependencies>
    <includes_components>
      <component>components/reporting/generate-structured-report.md</component>
    </includes_components>
    <uses_config_values>
      <value>deployment.environments.environment#production.url</value>
    </uses_config_values>
  </dependencies>
</command_file>