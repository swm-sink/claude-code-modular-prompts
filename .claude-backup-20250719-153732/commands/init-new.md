# Init-New Command - Create a new project with the framework

**Description**: Create a new project with the framework

────────────────────────────────────────────────────────────────────────────────

| version | last_updated | status | readiness |
|---------|--------------|--------|----------|
| 3.0.0   | 2025-07-12   | stable | 95%      |

────────────────────────────────────────────────────────────────────────────────


────────────────────────────────────────────────────────────────────────────────

```xml
<command name="init-new" category="initialization" enforcement="BLOCKING">
  
  <purpose>
    Interactive setup wizard for new projects with atomic commits safety, guided configuration creation, and comprehensive framework optimization with Claude 4 enhancement.
  </purpose>
  
  <scope>
    <includes>New project creation, interactive configuration, framework setup, best practices implementation</includes>
    <excludes>Existing project modification, automatic detection, legacy code handling</excludes>
    <boundaries>All setup must follow atomic commits pattern with instant rollback capability</boundaries>
  </scope>
  
  <input_specification>
    <required_arguments>Project type, domain, and basic configuration preferences via interactive prompts</required_arguments>
    <context_requirements>Empty or new project directory, development preferences, quality standards</context_requirements>
    <preconditions>Valid target directory, git repository initialized, user availability for interactive prompts</preconditions>
  </input_specification>
  
  <output_specification>
    <deliverables>Complete PROJECT_CONFIG.xml, optimized directory structure, framework integration, atomic commit trail</deliverables>
    <success_criteria>Interactive setup completed, configuration validated, rollback capability established</success_criteria>
    <artifacts>PROJECT_CONFIG.xml, setup documentation, interactive choices log, atomic commit history</artifacts>
  </output_specification>
</command>
```

Interactive setup wizard for new projects with atomic commits safety.

## Thinking Pattern - Claude 4 Enhanced

```xml
<thinking_pattern enforcement="MANDATORY">
  
  <checkpoint id="1" verify="true" enforcement="BLOCKING" thinking_mode="interleaved">
    <action>Pre-Setup Atomic Commit: Create secure baseline before any project setup changes</action>
    <interleaved_thinking enforcement="MANDATORY">
      <pre_analysis>
        - What is the current state that must be preserved before setup begins?
        - What interactive choices will be made that need rollback capability?
        - How can we ensure instant recovery if setup needs to be restarted?
      </pre_analysis>
      <critical_thinking minimum_time="30_seconds">
        - [Safety Question: Is the current directory state safely preserved?]
        - [Setup Question: What interactive configuration steps need atomic safety?]
        - [Recovery Question: Can we rollback partial setup attempts instantly?]
      </critical_thinking>
    </interleaved_thinking>
    <atomic_commit enforcement="MANDATORY">
      <pre_operation>git add -A && git commit -m "PRE-OP: init-new - backup state before interactive project setup"</pre_operation>
      <validation>Baseline commit established for setup rollback</validation>
      <rollback_capability>Available via: git reset --hard HEAD~1</rollback_capability>
    </atomic_commit>
  </checkpoint>
  
  <checkpoint id="2" verify="true" enforcement="BLOCKING" thinking_mode="interactive">
    <action>Interactive Configuration Gathering: Guided collection of project preferences and requirements</action>
    <interleaved_thinking enforcement="MANDATORY">
      <interactive_scope>
        - What project type and domain should be configured?
        - What programming languages and frameworks are preferred?
        - What quality standards and development workflows are desired?
        - What directory structure and naming conventions are preferred?
      </interactive_scope>
      <critical_thinking minimum_time="30_seconds">
        - [Requirements Question: Are all necessary configuration elements gathered?]
        - [Preferences Question: Do the choices align with best practices?]
        - [Completeness Question: Is enough information collected for full setup?]
      </critical_thinking>
    </interleaved_thinking>
    <module_delegation enforcement="MANDATORY">
      <interactive_modules>
        <module>development/interactive-configuration-wizard.md</module>
        <module>patterns/project-type-selection.md</module>
        <module>patterns/quality-standards-setup.md</module>
      </interactive_modules>
    </module_delegation>
  </checkpoint>
  
  <checkpoint id="3" verify="true" enforcement="BLOCKING" thinking_mode="interleaved">
    <action>Optimized Configuration Generation: Create PROJECT_CONFIG.xml with interactive choices and best practices</action>
    <interleaved_thinking enforcement="MANDATORY">
      <configuration_optimization>
        - How should interactive choices be translated into optimal configuration?
        - What best practices should be automatically applied?
        - What domain-specific optimizations should be included?
        - How should quality gates be configured for the chosen project type?
      </configuration_optimization>
      <critical_thinking minimum_time="30_seconds">
        - [Optimization Question: Does the configuration reflect best practices for this project type?]
        - [Integration Question: Are all interactive choices properly reflected in configuration?]
        - [Standards Question: Are appropriate quality standards configured?]
      </critical_thinking>
    </interleaved_thinking>
    <atomic_commit enforcement="MANDATORY">
      <operation_execution>git add PROJECT_CONFIG.xml && git commit -m "OP-EXEC: init-new configuration - interactive setup with optimized PROJECT_CONFIG.xml"</operation_execution>
      <validation>Configuration generated successfully with interactive preferences</validation>
      <rollback_trigger>Configuration errors trigger: git reset --hard HEAD~1</rollback_trigger>
    </atomic_commit>
  </checkpoint>
  
  <checkpoint id="4" verify="true" enforcement="BLOCKING" thinking_mode="interleaved">
    <action>Complete Setup Validation: Comprehensive validation of new project setup and framework integration</action>
    <interleaved_thinking enforcement="MANDATORY">
      <validation_scope>
        - Is the complete project setup functional and ready for development?
        - Are all configuration elements valid and properly integrated?
        - Does the framework provide optimal support for this project type?
        - Is rollback capability tested and functional?
      </validation_scope>
      <critical_thinking minimum_time="30_seconds">
        - [Functionality Question: Is the new project setup fully functional?]
        - [Optimization Question: Does the setup provide optimal development experience?]
        - [Safety Question: Are all atomic commit safeguards in place?]
      </critical_thinking>
    </interleaved_thinking>
    <atomic_commit enforcement="MANDATORY">
      <post_operation>git add -A && git commit -m "POST-OP: init-new complete - new project setup validated with rollback capability"</post_operation>
      <validation>Complete setup validated and atomic commit trail established</validation>
      <rollback_trigger>Validation failure triggers: git reset --hard HEAD~2 (return to pre-setup)</rollback_trigger>
    </atomic_commit>
  </checkpoint>
  
</thinking_pattern>
```

## What It Does

This command provides an interactive setup wizard for new projects:

1. **Project Information Gathering**
   - Project name and description
   - Domain (web, mobile, data science, etc.)
   - Primary programming language
   - Framework and technology choices

2. **Configuration Customization**
   - Directory structure preferences
   - Quality standards and thresholds
   - Development workflow setup
   - Testing and deployment configuration

3. **Framework Optimization**
   - Domain-specific module selection
   - Custom persona configuration
   - Quality gate customization
   - Performance and security settings

## Interactive Questions

I'll ask you about:

**Project Basics**
- What type of project are you building?
- What domain/industry is this for?
- What's your primary programming language?
- What frameworks will you use?

**Quality Standards**
- What test coverage percentage do you target?
- How strict should quality enforcement be?
- What performance benchmarks matter?

**Development Workflow**
- What's your preferred directory structure?
- What build and test commands will you use?
- How do you manage deployments?

**Team Preferences**
- Coding style and conventions?
- Documentation standards?
- Git workflow preferences?

## Example Session

```
/init-new

> What type of project are you building?
"A React web application with TypeScript"

> What domain is this for?
"E-commerce platform"

> Target test coverage?
"90%"

[... more questions ...]

✅ Generated PROJECT_CONFIG.xml with your preferences!
```

## Benefits

- **Zero Manual Configuration** - Answer questions, get perfect setup
- **Best Practices Built-in** - Recommendations based on your domain
- **Customized Workflows** - Framework adapts to your preferences
- **Production Ready** - Quality gates and standards configured

## Related Commands

- `/init-custom` - For existing projects
- `/init-research` - Research-driven setup
- `/init-validate` - Validate configuration

$ARGUMENTS