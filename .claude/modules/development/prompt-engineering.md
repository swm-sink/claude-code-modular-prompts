| version | last_updated | status |
|---------|--------------|--------|
| 1.0.0   | 2025-07-07   | stable |

# Prompt Engineering Module

────────────────────────────────────────────────────────────────────────────────

```xml
<module name="prompt_engineering" category="development">
  
  <purpose>
    Advanced prompt engineering patterns for Claude Code including modular composition, parameter systems, and optimization strategies.
  </purpose>
  
  <modular_composition>
    
    <delegation_pattern>
      <description>Commands delegate ALL implementation to specialized modules</description>
      <structure>
        ```xml
        <command purpose="...">
          <delegation target="modules/category/module-name.md">
            Brief description of what module provides
          </delegation>
        </command>
        ```
      </structure>
      <benefits>Single source of truth, consistent behavior, maintainable</benefits>
    </delegation_pattern>
    
    <module_integration>
      <description>Modules reference and compose with other modules</description>
      <structure>
        ```xml
        <module_integration>
          <primary_module>modules/category/main-module.md</primary_module>
          <supporting_modules>
            <module>modules/category/support-module.md</module>
          </supporting_modules>
        </module_integration>
        ```
      </structure>
      <benefits>Clear dependency mapping, predictable composition</benefits>
    </module_integration>
    
  </modular_composition>
  
  <parameter_systems>
    
    <structured_parameters>
      <description>Use XML-structured parameters for clarity and validation</description>
      <pattern>
        ```xml
        <parameters>
          <parameter name="--type" values="system|user|assistant" default="system">
            <purpose>Specify the type of prompt being created</purpose>
          </parameter>
        </parameters>
        ```
      </pattern>
    </structured_parameters>
    
    <subcommand_organization>
      <description>Break complex commands into focused subcommands</description>
      <pattern>
        ```xml
        <subcommands>
          <subcommand name="create">
            <purpose>Create new prompts with best practices</purpose>
            <example>/command create "feature" --type system</example>
          </subcommand>
        </subcommands>
        ```
      </pattern>
    </subcommand_organization>
    
  </parameter_systems>
  
  <optimization_strategies>
    
    <token_efficiency>
      <description>Minimize token usage while maintaining clarity</description>
      <techniques>
        - Use XML blocks for structure (more efficient than markdown)
        - Reference modules instead of duplicating content
        - Batch operations for parallel execution
        - Use semantic tags for better parsing
      </techniques>
    </token_efficiency>
    
    <context_management>
      <description>Manage context size and relevance</description>
      <techniques>
        - Lazy load module content only when needed
        - Use summaries for large modules
        - Clear dependency chains
        - Avoid circular references
      </techniques>
    </context_management>
    
  </optimization_strategies>
  
  <quality_enforcement>
    
    <escalation_triggers>
      <description>Define when to escalate to more powerful patterns</description>
      <pattern>
        ```xml
        <escalation_triggers>
          <trigger condition="complex_multi_component">Escalates to /swarm</trigger>
          <trigger condition="production_deployment">Requires /protocol validation</trigger>
        </escalation_triggers>
        ```
      </pattern>
    </escalation_triggers>
    
    <validation_hooks>
      <description>Built-in validation and quality checks</description>
      <pattern>
        ```xml
        <integration_hooks>
          <hook type="pre_execute">Validates parameters and dependencies</hook>
          <hook type="post_execute">Analyzes results and suggests improvements</hook>
        </integration_hooks>
        ```
      </pattern>
    </validation_hooks>
    
  </quality_enforcement>
  
  <integration_points>
    <multi_agent>Agent coordination and prompt specialization</multi_agent>
    <production_standards>Quality gates and compliance integration</production_standards>
    <session_management>Context preservation across sessions</session_management>
    <tdd>Test-driven prompt development</tdd>
  </integration_points>
  
</module>
```

────────────────────────────────────────────────────────────────────────────────

## Prompt Engineering Principles

```xml
<prompt_engineering_principles>
  <principle>Modular composition over monolithic prompts</principle>
  <principle>XML structure for semantic clarity and efficiency</principle>
  <principle>Delegation patterns for single source of truth</principle>
  <principle>Parameter validation and type safety</principle>
  <principle>Escalation triggers for complexity management</principle>
  <principle>Quality hooks for continuous improvement</principle>
</prompt_engineering_principles>
```

────────────────────────────────────────────────────────────────────────────────

## Advanced Patterns

```xml
<advanced_patterns>
  
  <command_composition>
    <description>Commands compose multiple modules for complex workflows</description>
    <example>
      /feature delegates to:
      - planning/feature-workflow.md (main orchestration)
      - development/task-management.md (implementation)
      - quality/tdd.md (testing standards)
      - security/audit.md (security validation)
    </example>
  </command_composition>
  
  <dynamic_routing>
    <description>Intelligent routing based on request analysis</description>
    <implementation>patterns/intelligent-routing.md</implementation>
  </dynamic_routing>
  
  <quality_enforcement>
    <description>Mandatory quality enforcement through specialized modules</description>
    <implementation>quality/production-standards.md</implementation>
  </quality_enforcement>
  
</advanced_patterns>
```

────────────────────────────────────────────────────────────────────────────────

**Reference**: Used by multi-agent.md, production-standards.md, tdd.md, session-management.md for advanced prompt engineering capabilities.