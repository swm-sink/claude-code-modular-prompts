| version | last_updated | status |
|---------|--------------|--------|
| 3.0.0   | 2025-01-08   | stable |

# Module Name

────────────────────────────────────────────────────────────────────────────────

```xml
<module name="module_name" category="category_name">
  
  <purpose>
    Comprehensive description of what this module does, why it exists, and what 
    problems it solves. Should be specific enough to understand when to use it.
  </purpose>
  
  <!-- Performance characteristics if relevant -->
  <performance_optimizations>
    <benchmarks>
      Operation X: <100ms p95
      Operation Y: <50ms p95
    </benchmarks>
    <caching_strategy>
      Cache type and eviction policy
    </caching_strategy>
  </performance_optimizations>
  
  <!-- When this module should be activated -->
  <trigger_conditions>
    <condition type="automatic">Automatically triggered when X happens</condition>
    <condition type="explicit">Explicitly triggered by Y command</condition>
    <condition type="implicit">Implicitly required when Z pattern detected</condition>
  </trigger_conditions>
  
  <!-- Main implementation logic -->
  <implementation>
    
    <phase name="phase_name" order="1">
      <requirements>
        Precondition 1 must be satisfied
        Resource X must be available
        State Y must be validated
      </requirements>
      <actions>
        Step 1: Specific action with clear outcome
        Step 2: Another action building on step 1
        Step 3: Final action in this phase
      </actions>
      <validation>
        Check that outcome X is achieved
        Verify state Y is consistent
        Ensure no side effects on Z
      </validation>
    </phase>
    
    <phase name="next_phase" order="2">
      <requirements>
        Previous phase completed successfully
        Additional requirements for this phase
      </requirements>
      <actions>
        Continue with next set of actions
        Build upon previous phase results
      </actions>
      <validation>
        Final state validations
        Success criteria checks
      </validation>
    </phase>
    
  </implementation>
  
  <!-- Integration with other modules -->
  <integration_points>
    <depends_on>
      patterns/pattern-library.md for execution patterns
      <!-- Add specific module dependencies here when implementing -->
    </depends_on>
    <provides_to>
      Commands or modules that consume this module's functionality
    </provides_to>
  </integration_points>
  
  <!-- Pattern usage from pattern library -->
  <pattern_usage>
    <uses_pattern from="pattern-library.md">pattern_name</uses_pattern>
    <uses_pattern from="pattern-library.md">another_pattern</uses_pattern>
    <implementation_notes>
      How patterns are specifically applied in this module
      Performance impact of pattern usage
      Any customizations or variations
    </implementation_notes>
  </pattern_usage>
  
  <!-- Configuration options -->
  <configuration>
    <setting name="setting_name" default="value" required="true">
      Description of what this setting controls
    </setting>
    <setting name="optional_setting" default="value" required="false">
      Optional configuration with sensible default
    </setting>
  </configuration>
  
  <!-- Error handling -->
  <error_handling>
    <error code="ERR001" severity="critical">
      Description and recovery strategy
    </error>
    <error code="ERR002" severity="warning">
      Non-critical error with fallback behavior
    </error>
  </error_handling>
  
  <!-- Usage examples -->
  <examples>
    <example name="basic_usage">
      <description>Simple use case demonstration</description>
      <code>
        Example code or command usage
      </code>
      <expected_output>
        What the user should expect to see
      </expected_output>
    </example>
  </examples>
  
</module>
```

<!-- 
Template Guidelines:
1. Module names use snake_case, categories are: security, quality, development, patterns, planning, testing
2. Version follows semantic versioning (major.minor.patch)
3. Status options: draft | active | deprecated | experimental | stable
4. Purpose should clearly explain when and why to use this module
5. Phases should be ordered and have clear dependencies
6. Performance metrics should be measurable and realistic
7. Pattern usage must reference actual patterns from pattern-library.md
8. Error codes should follow consistent naming (ERR###)
9. Remove sections not applicable to your module
10. Keep implementation phases focused and testable
11. Examples should be practical and demonstrate real usage
12. Integration points help with module composition
-->