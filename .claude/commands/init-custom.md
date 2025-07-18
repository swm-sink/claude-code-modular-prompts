# Init-Custom Command - Set up framework with custom settings

**Description**: Set up framework with custom settings

────────────────────────────────────────────────────────────────────────────────

| version | last_updated | status | readiness |
|---------|--------------|--------|----------|
| 3.0.0   | 2025-07-12   | stable | 95%      |

────────────────────────────────────────────────────────────────────────────────


────────────────────────────────────────────────────────────────────────────────

```xml
<command name="init-custom" category="initialization" enforcement="BLOCKING">
  
  <purpose>
    Auto-configure framework for existing projects with atomic commits safety, comprehensive codebase analysis, and intelligent module selection with Claude 4 optimization.
  </purpose>
  
  <scope>
    <includes>Existing project analysis, automatic configuration generation, framework adaptation</includes>
    <excludes>New project creation, manual configuration, destructive changes</excludes>
    <boundaries>Configuration must preserve existing project structure and conventions</boundaries>
  </scope>
  
  <input_specification>
    <required_arguments>Project root directory with existing codebase</required_arguments>
    <context_requirements>Existing code files, project structure, development patterns</context_requirements>
    <preconditions>Valid project directory, readable code files, git repository available</preconditions>
  </input_specification>
  
  <output_specification>
    <deliverables>PROJECT_CONFIG.xml with project-specific settings, framework integration report, atomic commit trail</deliverables>
    <success_criteria>Configuration generated successfully, framework integrated, rollback capability available</success_criteria>
    <artifacts>PROJECT_CONFIG.xml, configuration analysis report, atomic commit history</artifacts>
  </output_specification>
</command>
```

Auto-configure framework for existing projects with atomic commits safety.

## Thinking Pattern - Claude 4 Enhanced

```xml
<thinking_pattern enforcement="MANDATORY">
  
  <checkpoint id="1" verify="true" enforcement="BLOCKING" thinking_mode="interleaved">
    <action>Pre-Operation Atomic Commit: Create secure rollback point before any configuration changes</action>
    <interleaved_thinking enforcement="MANDATORY">
      <pre_analysis>
        - What is the current state of the project that must be preserved?
        - What configuration changes will be made that need rollback capability?
        - How can we ensure zero data loss during framework integration?
      </pre_analysis>
      <critical_thinking minimum_time="30_seconds">
        - [Safety Question: Are all existing project files and configurations safely preserved?]
        - [Impact Question: What changes will framework integration make to the project?]
        - [Recovery Question: Can we instantly rollback if anything goes wrong?]
      </critical_thinking>
    </interleaved_thinking>
    <atomic_commit enforcement="MANDATORY">
      <pre_operation>git add -A && git commit -m "PRE-OP: init-custom - backup state before framework configuration"</pre_operation>
      <validation>Commit successful and rollback point established</validation>
      <rollback_capability>Available via: git reset --hard HEAD~1</rollback_capability>
    </atomic_commit>
  </checkpoint>
  
  <checkpoint id="2" verify="true" enforcement="BLOCKING" thinking_mode="interleaved">
    <action>Comprehensive Codebase Analysis: Deep analysis of project structure, technology stack, and conventions</action>
    <interleaved_thinking enforcement="MANDATORY">
      <analysis_scope>
        - What programming languages and frameworks are used?
        - What is the project structure and organization pattern?
        - What quality standards and testing approaches exist?
        - What architectural patterns are implemented?
      </analysis_scope>
      <critical_thinking minimum_time="45_seconds">
        - [Architecture Question: What patterns and conventions should the framework respect?]
        - [Technology Question: How should framework modules be selected for this tech stack?]
        - [Quality Question: What existing quality standards should be preserved and enhanced?]
      </critical_thinking>
    </interleaved_thinking>
    <module_delegation enforcement="MANDATORY">
      <analysis_modules>
        <module>development/codebase-analyzer.md</module>
        <module>patterns/technology-stack-detection.md</module>
        <module>patterns/project-structure-analysis.md</module>
      </analysis_modules>
    </module_delegation>
  </checkpoint>
  
  <checkpoint id="3" verify="true" enforcement="BLOCKING" thinking_mode="interleaved">
    <action>Intelligent Configuration Generation: Generate PROJECT_CONFIG.xml with project-specific settings</action>
    <interleaved_thinking enforcement="MANDATORY">
      <configuration_logic>
        - How should quality thresholds be set based on existing standards?
        - What directory structure should be configured?
        - What development commands and workflows should be established?
        - How should domain-specific modules be selected?
      </configuration_logic>
      <critical_thinking minimum_time="30_seconds">
        - [Adaptation Question: Does the configuration match project conventions?]
        - [Integration Question: Will the framework enhance rather than disrupt workflows?]
        - [Completeness Question: Are all necessary configuration elements specified?]
      </critical_thinking>
    </interleaved_thinking>
    <atomic_commit enforcement="MANDATORY">
      <operation_execution>git add PROJECT_CONFIG.xml && git commit -m "OP-EXEC: init-custom configuration - PROJECT_CONFIG.xml generated with project-specific settings"</operation_execution>
      <validation>Configuration file created and project-specific settings applied</validation>
      <rollback_trigger>Configuration errors trigger: git reset --hard HEAD~1</rollback_trigger>
    </atomic_commit>
  </checkpoint>
  
  <checkpoint id="4" verify="true" enforcement="BLOCKING" thinking_mode="interleaved">
    <action>Framework Integration Validation: Comprehensive validation of framework integration and configuration completeness</action>
    <interleaved_thinking enforcement="MANDATORY">
      <validation_scope>
        - Does the framework integrate seamlessly with existing project?
        - Are all configuration paths and settings valid?
        - Do framework modules work correctly with project structure?
        - Is rollback capability fully functional?
      </validation_scope>
      <critical_thinking minimum_time="30_seconds">
        - [Integration Question: Does the framework enhance the project without disruption?]
        - [Functionality Question: Are all framework features working correctly?]
        - [Safety Question: Is rollback capability tested and functional?]
      </critical_thinking>
    </interleaved_thinking>
    <atomic_commit enforcement="MANDATORY">
      <post_operation>git add -A && git commit -m "POST-OP: init-custom complete - framework integrated successfully with rollback capability"</post_operation>
      <validation>Integration validated and atomic commit trail established</validation>
      <rollback_trigger>Validation failure triggers: git reset --hard HEAD~2 (return to pre-operation)</rollback_trigger>
    </atomic_commit>
  </checkpoint>
  
</thinking_pattern>
```

## What It Does

This command helps you integrate the framework into an existing project by:

1. **Analyzing Your Codebase**
   - Detects programming languages, frameworks, and libraries
   - Identifies project structure and conventions
   - Discovers existing quality standards and testing approaches
   - Maps architectural patterns and domain characteristics

2. **Auto-Generating Configuration**
   - Creates PROJECT_CONFIG.xml with detected settings
   - Selects appropriate framework modules for your tech stack
   - Configures quality gates based on existing standards
   - Sets up development workflows matching your patterns

3. **Framework Customization**
   - Adapts all framework modules to your project specifics
   - Configures domain-specific features and standards
   - Optimizes for your development workflow
   - Ensures zero manual configuration required

## Process

I'll analyze your project using these steps:

1. **Comprehensive Codebase Analysis**
   - Scale and complexity assessment
   - Technology stack detection
   - Architecture pattern recognition
   - Domain identification
   - Convention discovery

2. **Intelligent Module Selection**
   - Choose relevant framework modules
   - Apply domain-specific templates
   - Match quality standards to your needs
   - Optimize workflow configurations

3. **Configuration Generation**
   - Generate complete PROJECT_CONFIG.xml
   - Validate all settings and paths
   - Test framework integration
   - Provide customization report

## Example Workflow

When you run `/init-custom`, I will:
- Scan your project structure
- Analyze code patterns and conventions
- Detect your tech stack (React, Python, Go, etc.)
- Identify testing frameworks and coverage
- Generate PROJECT_CONFIG.xml automatically
- Configure framework for your specific needs

The result is a fully configured framework that adapts to YOUR project, not the other way around!

## Requirements

- Existing codebase with some structure
- At least basic project organization
- Some code files to analyze

## Related Commands

- `/init-new` - For brand new projects
- `/init-research` - Research-driven configuration
- `/init-validate` - Validate framework setup

$ARGUMENTS