<module name="api_development" category="patterns">
  
  <purpose>
    Enterprise API development patterns with performance optimization, security integration, and microservice architecture.
  </purpose>
  
  <trigger_conditions>
    <condition type="automatic">REST API development, microservice creation, API gateway implementation, GraphQL services</condition>
    <condition type="explicit">User requests API patterns, enterprise API development, or microservice architecture</condition>
  </trigger_conditions>
  
  <implementation>
    
    <phase name="architecture_design" order="1">
      <requirements>
        Layered architecture designed based on complexity requirements
        API patterns selected appropriate for use case and scale
        Security patterns integrated from design phase
      </requirements>
      <actions>
        Design layered architecture: presentation, application, domain, infrastructure
        Select appropriate patterns: RESTful design, GraphQL, microservice communication
        Integrate security patterns: authentication, authorization, rate limiting
        Plan performance optimization: caching, async processing, load balancing
      </actions>
      <validation>
        Architecture layers properly separated with clear responsibilities
        API design follows RESTful principles and industry standards
        Security considerations addressed at architectural level
      </validation>
    </phase>
    
    <phase name="implementation_standards" order="2">
      <requirements>
        Production-ready implementation with comprehensive error handling
        Performance optimizations applied based on requirements
        Security standards enforced throughout implementation
      </requirements>
      <actions>
        Implement layered architecture with proper dependency injection
        Apply async patterns for concurrent processing and external API calls
        Implement comprehensive error handling with structured responses
        Add rate limiting, authentication, and authorization mechanisms
      </actions>
      <validation>
        Implementation meets performance SLAs and security requirements
        Error handling provides appropriate responses without data leakage
        API endpoints properly documented with OpenAPI specification
      </validation>
    </phase>
    
    <phase name="testing_documentation" order="3">
      <requirements>
        Comprehensive test coverage including unit, integration, and contract tests
        Complete API documentation with examples and error scenarios
        Performance testing validates SLA requirements
      </requirements>
      <actions>
        Implement unit tests for business logic with proper mocking
        Create integration tests for full request/response cycles
        Generate contract tests for API specification compliance
        Produce comprehensive OpenAPI documentation with examples
      </actions>
      <validation>
        Test coverage meets quality standards with meaningful assertions
        API documentation complete with request/response examples
        Performance testing confirms SLA compliance under load
      </validation>
    </phase>
    
  </implementation>
  
  <architecture_patterns>
    <layered_architecture>
      <presentation>HTTP request/response handling, serialization, validation, middleware</presentation>
      <application>Business logic orchestration, use case implementation, service layer</application>
      <domain>Core business logic, domain rules, entities, value objects</domain>
      <infrastructure>Data persistence, external services, cross-cutting concerns</infrastructure>
    </layered_architecture>
    <microservice_patterns>
      <synchronous_communication>HTTP REST for real-time, GraphQL for flexible data, gRPC for performance</synchronous_communication>
      <asynchronous_communication>Message queues for reliability, event streams for real-time, pub/sub for events</asynchronous_communication>
      <resilience_patterns>Circuit breaker, retry with backoff, timeout handling, bulkhead isolation</resilience_patterns>
    </microservice_patterns>
  </architecture_patterns>
  
  <restful_design>
    <resource_naming>
      <collections>Plural nouns: users, orders, products</collections>
      <instances>Collection + identifier: /users/123</instances>
      <subcollections>Nested resources: /users/123/orders</subcollections>
      <actions>Verbs for non-CRUD: /users/123/activate</actions>
    </resource_naming>
    <http_methods>
      <get>Retrieve resources (idempotent, safe)</get>
      <post>Create resources (non-idempotent)</post>
      <put>Update/replace resources (idempotent)</put>
      <patch>Partial updates (idempotent)</patch>
      <delete>Remove resources (idempotent)</delete>
    </http_methods>
    <status_codes>
      <success>200 OK, 201 Created, 202 Accepted, 204 No Content</success>
      <client_errors>400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 409 Conflict, 422 Validation</client_errors>
      <server_errors>500 Internal Error, 502 Bad Gateway, 503 Service Unavailable</server_errors>
    </status_codes>
  </restful_design>
  
  <performance_optimization>
    <async_patterns>
      <concurrent_processing>Parallel external API calls, batch database operations</concurrent_processing>
      <background_tasks>Email sending, file processing, analytics, cleanup operations</background_tasks>
      <streaming>Large datasets, real-time data, file uploads, CSV exports</streaming>
    </async_patterns>
    <caching_strategies>
      <application_cache>In-memory for frequently accessed data (minutes TTL)</application_cache>
      <distributed_cache>Redis/Memcached for shared data (hours TTL)</distributed_cache>
      <cdn_cache>Content delivery for static assets (days TTL)</cdn_cache>
      <database_cache>Query result caching for expensive operations</database_cache>
    </caching_strategies>
  </performance_optimization>
  
  <security_integration>
    <authentication_methods>
      <jwt_tokens>Stateless authentication for APIs and microservice communication</jwt_tokens>
      <oauth2>Authorization code flow for third-party integrations and social login</oauth2>
      <api_keys>Simple server-to-server authentication for basic integrations</api_keys>
    </authentication_methods>
    <authorization_models>
      <rbac>Role-Based Access Control for standard business applications</rbac>
      <abac>Attribute-Based Access Control for complex authorization requirements</abac>
      <resource_based>Resource-Based Access Control for document and file management</resource_based>
    </authorization_models>
    <rate_limiting>
      <algorithms>Token bucket for burst handling, sliding window for precision, fixed window for simplicity</algorithms>
      <granularity>Global, per-user, per-endpoint, per-IP, per-API-key levels</granularity>
      <responses>Reject with 429, queue for later, degrade service, redirect to alternative</responses>
    </rate_limiting>
  </security_integration>
  
  <testing_patterns>
    <unit_tests>Individual endpoint logic with mocked dependencies</unit_tests>
    <integration_tests>Full request/response cycle with test database</integration_tests>
    <contract_tests>API specification compliance and schema validation</contract_tests>
    <performance_tests>Load and stress testing with response time metrics</performance_tests>
  </testing_patterns>
  
  <documentation_standards>
    <openapi_specification>
      <endpoint_docs>Summary, description, tags, operation ID for each endpoint</endpoint_docs>
      <parameter_docs>Path, query, header parameters with validation rules</parameter_docs>
      <response_docs>Success and error responses with examples and status codes</response_docs>
      <schema_design>Reusable data models with validation constraints and composition</schema_design>
    </openapi_specification>
    <code_generation>Client SDKs, server stubs, mock servers, interactive documentation</code_generation>
  </documentation_standards>
  
  <session_integration>
    <complex_apis>
      <triggers>Microservice architecture, enterprise API, complex integration requirements</triggers>
      <documentation>API design decisions, architecture patterns, performance requirements</documentation>
      <tracking>Development progress, quality gates, performance benchmarks</tracking>
    </complex_apis>
    <simple_apis>
      <scope>Single endpoint implementation, straightforward CRUD operations</scope>
      <approach>Direct implementation without session overhead</approach>
    </simple_apis>
  </session_integration>
  
  <integration_points>
    <depends_on>
      quality/production-standards.md for enterprise quality gates
      security/financial-compliance.md for security pattern integration
      patterns/session-management.md for complex API project tracking
    </depends_on>
    <provides_to>
      development/task-management.md for API implementation standards
      All commands for enterprise API development patterns
    </provides_to>
  </integration_points>
  
</module>