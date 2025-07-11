| version | last_updated | status |
|---------|--------------|--------|
| 1.0.0   | 2025-07-09   | stable |

# Implementation Pattern Module

────────────────────────────────────────────────────────────────────────────────


────────────────────────────────────────────────────────────────────────────────

```xml
<module name="implementation_pattern" category="patterns">
  
  <purpose>
    Code development and creation with quality standards, ensuring systematic approach to building maintainable, secure, and performant software following established patterns.
  </purpose>
  
  <trigger_conditions>
    <condition type="automatic">Writing new code or features</condition>
    <condition type="explicit">Implementing solutions after research</condition>
    <condition type="explicit">Converting requirements into working code</condition>
    <condition type="explicit">Building on existing codebase</condition>
  </trigger_conditions>
  
  <implementation>
    
    <phase name="plan_implementation" order="1">
      <requirements>
        Requirements and constraints must be reviewed
        Research phase must be completed
        Design approach must be chosen
      </requirements>
      <actions>
        Design the approach based on research and requirements
        Review requirements and constraints
        Choose appropriate patterns and techniques
        Plan code structure and organization
        Identify dependencies and interfaces
      </actions>
      <validation>
        Implementation approach is well-defined
        Patterns and techniques are appropriate
        Code structure is planned and organized
        Dependencies and interfaces are identified
      </validation>
    </phase>
    
    <phase name="setup_environment" order="2">
      <requirements>
        Development environment must be available
        Testing framework must be configured
        Tools and dependencies must be ready
      </requirements>
      <actions>
        Prepare development environment and tools
        Configure development tools
        Set up testing framework
        Prepare debugging environment
        Ensure proper dependencies
      </actions>
      <validation>
        Development environment is configured
        Testing framework is operational
        Debugging tools are available
        All dependencies are properly installed
      </validation>
    </phase>
    
    <phase name="implement_core_logic" order="3">
      <requirements>
        Environment setup must be completed
        Core functionality must be defined
        Patterns and conventions must be established
      </requirements>
      <actions>
        Write the main functionality
        Follow established patterns and conventions
        Write clean, readable code
        Implement one feature at a time
        Test as you go
      </actions>
      <validation>
        Core functionality is implemented
        Code follows established patterns
        Implementation is clean and readable
        Features are implemented incrementally
        Tests are passing
      </validation>
    </phase>
    
    <phase name="handle_edge_cases" order="4">
      <requirements>
        Core logic must be implemented
        Edge cases must be identified
        Error handling strategy must be defined
      </requirements>
      <actions>
        Address boundary conditions and error scenarios
        Input validation and sanitization
        Error handling and recovery
        Performance under load
        Security considerations
      </actions>
      <validation>
        Edge cases are properly handled
        Input validation is comprehensive
        Error handling is robust
        Performance is acceptable under load
        Security considerations are addressed
      </validation>
    </phase>
    
    <phase name="optimize_and_refine" order="5">
      <requirements>
        Implementation must be functionally complete
        Quality standards must be defined
        Performance requirements must be known
      </requirements>
      <actions>
        Improve code quality and performance
        Refactor for clarity and maintainability
        Optimize critical paths
        Remove code duplication
        Improve documentation
      </actions>
      <validation>
        Code quality is improved
        Performance is optimized
        Code duplication is eliminated
        Documentation is clear and helpful
      </validation>
    </phase>
    
  </implementation>
  
  <quality_standards>
    <standard>Code follows established conventions</standard>
    <standard>Functions have single responsibility</standard>
    <standard>Error handling is comprehensive</standard>
    <standard>Performance is acceptable</standard>
    <standard>Security considerations are addressed</standard>
    <standard>Documentation is clear and helpful</standard>
  </quality_standards>
  
  <integration_points>
    <provides_to>
      patterns/quality-validation-pattern.md for verification
      patterns/error-recovery-pattern.md for robust code
    </provides_to>
    <depends_on>
      patterns/tdd-cycle-pattern.md for test-driven development
      patterns/research-analysis-pattern.md for informed decisions
      patterns/critical-thinking-pattern.md for design choices
    </depends_on>
  </integration_points>
  
  <examples>
    <example name="api_endpoint_development">
      <description>Building API endpoints with proper error handling</description>
      <code>
        PLAN: Design REST API with proper error handling
        SETUP: Configure Express.js with testing framework
        CORE: Implement CRUD operations with validation
        EDGES: Handle authentication, rate limiting, errors
        OPTIMIZE: Improve performance and add documentation
      </code>
      <expected_output>
        Robust API endpoint with comprehensive error handling
        Clean, maintainable code following REST conventions
        Proper authentication and security measures
      </expected_output>
    </example>
  </examples>
  
</module>
```