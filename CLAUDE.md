| version | last_updated | status |
|---------|--------------|--------|
| 3.0.0   | 2025-07-12   | stable |

# CLAUDE.md - Framework Control Document

# Overview

<purpose>Personal Claude Code workflow efficiency tool - NOT enterprise software</purpose>

**Framework Status**: This repository contains a fully implemented modular prompt engineering framework with comprehensive `.claude/` architecture, advanced meta-prompting capabilities, and Claude 4 optimization.

**What's Included**:
- Complete `.claude/` modular framework with 108+ specialized modules
- PROJECT_CONFIG.xml configuration system with dynamic templates
- Meta-prompting capabilities with self-improvement frameworks
- Comprehensive validation and optimization scripts
- Test infrastructure and performance monitoring
- Quality gates and TDD enforcement implementation

**Framework Architecture**:
- `.claude/modules/` - 108+ specialized modules across domains
- `.claude/prompt_eng/` - Advanced prompt engineering patterns
- `.claude/system/` - Quality gates and infrastructure components
- `.claude/meta/` - Self-improving meta-framework capabilities


# ⚠️ CRITICAL: Claude Code Settings Protection

```xml
<settings_protection enforcement = "MAXIMUM" priority = "CRITICAL">
  <purpose>Protect optimized Claude Code settings from wildcard syntax regression</purpose>
  
  <protected_configuration>
    <file>/.claude/settings.local.json</file>
    <status>OPTIMIZED FOR MAXIMUM AUTONOMY - DO NOT MODIFY</status>
    <critical_fix>Wildcard permissions syntax DOES NOT WORK in Claude Code</critical_fix>
  </protected_configuration>
  
  <wildcard_bug_documentation>
    <broken_syntax>
      <pattern>"Bash(git:*)" ❌ BROKEN - Known Claude Code bug</pattern>
      <pattern>"Bash(ls:*)" ❌ BROKEN - Intermittent failures</pattern>
      <pattern>"Bash(*)" ❌ BROKEN - Documented GitHub issues</pattern>
      <pattern>"Bash(*:*)" ❌ BROKEN - Memory management issues</pattern>
    </broken_syntax>
    <working_syntax>
      <pattern>"Bash(git)" ✅ WORKS - Individual command permissions</pattern>
      <pattern>"Bash(git add)" ✅ WORKS - Specific command variants</pattern>
      <pattern>"Bash(ls)" ✅ WORKS - No wildcards or colons</pattern>
      <pattern>"Bash(python)" ✅ WORKS - Simple command names</pattern>
    </working_syntax>
  </wildcard_bug_documentation>
  
  <github_issues_evidence>
    <issue>GitHub Issue #462: "Allowing `Bash(*)` or `Bash(*:*)` doesn't seem to work"</issue>
    <issue>GitHub Issue #2560: "Claude code keeps asking for permission despite already having it"</issue>
    <issue>GitHub Issue #2733: "Infinite bash permission loop"</issue>
    <issue>GitHub Issue #74: "Claude does not understand that it does have the correct bash permissions"</issue>
  </github_issues_evidence>
  
  <protection_rules enforcement = "MANDATORY">
    <rule priority = "HIGHEST">NEVER revert to wildcard syntax (patterns with : or *)</rule>
    <rule priority = "HIGHEST">NEVER use "Bash(command:*)" format</rule>
    <rule priority = "HIGHEST">ALWAYS use "Bash(command)" format for individual commands</rule>
    <rule priority = "HIGHEST">CURRENT CONFIGURATION IS BATTLE-TESTED AND WORKS</rule>
    <rule priority = "CRITICAL">Modification requires explicit approval after wildcard bug research</rule>
  </protection_rules>
  
  <configuration_status>
    <optimized_date>2025-07-12</optimized_date>
    <research_basis>Extensive GitHub issues analysis and developer community feedback</research_basis>
    <permissions_count>140+ individual command permissions</permissions_count>
    <wildcard_removal>Complete elimination of problematic wildcard patterns</wildcard_removal>
    <autonomy_level>Maximum - eliminates permission prompts</autonomy_level>
  </configuration_status>
  
  <emergency_rollback>
    <backup_commit>Available via git log - pre-optimization state preserved</backup_commit>
    <recovery_time>60 seconds maximum via git reset</recovery_time>
    <validation_required>Test permission prompts after any changes</validation_required>
  </emergency_rollback>
</settings_protection>
```

# Command Status (Agent V5 Final Integration Results)

```xml
<command_status test_date = "2025-07-12" agent = "V5">
  <functional_commands count = "13">
    <command name = "init" status = "FULLY_FUNCTIONAL"/>
    <command name = "task" status = "FULLY_FUNCTIONAL"/>
    <command name = "feature" status = "FULLY_FUNCTIONAL"/>
    <command name = "protocol" status = "FULLY_FUNCTIONAL"/>
    <command name = "auto" status = "FULLY_FUNCTIONAL"/>
    <command name = "query" status = "FULLY_FUNCTIONAL"/>
    <command name = "swarm" status = "FULLY_FUNCTIONAL"/>
    <command name = "docs" status = "FULLY_FUNCTIONAL"/>
    <command name = "session" status = "FULLY_FUNCTIONAL"/>
    <command name = "init-validate" status = "FULLY_FUNCTIONAL"/>
    <command name = "init-custom" status = "FULLY_FUNCTIONAL"/>
    <command name = "init-research" status = "FULLY_FUNCTIONAL"/>
    <command name = "init-new" status = "FULLY_FUNCTIONAL"/>
  </functional_commands>
  <integration_status>
    <total_tested>13</total_tested>
    <success_rate>100%</success_rate>
    <production_ready>True</production_ready>
    <phase_1_complete>True</phase_1_complete>
  </integration_status>
</command_status>
```


# Performance Optimization Results (Agent 10)

```xml
<performance_results agent = "10" test_date = "2025-07-11">
  <directory_optimization>
    <reduction>Current framework has 35 .claude directories</reduction>
    <access_improvement>15.1%</access_improvement>
  </directory_optimization>
  <command_loading>
    <improvement>15.0%</improvement>
    <commands_optimized>14</commands_optimized>
  </command_loading>
  <quality_modules>
    <modules_found>108</modules_found>
    <optimization>20.0% improvement potential</optimization>
  </quality_modules>
  <overall_metrics>
    <average_improvement>13.0%</average_improvement>
    <responsiveness_score>7.0/10 (B+ Grade)</responsiveness_score>
    <framework_ready>true</framework_ready>
  </overall_metrics>
</performance_results>
```

# Project Customization Layer

```xml
<project_customization enforcement = "MANDATORY" version = "1.0.0">
  <purpose>Framework adapts to YOUR project through configuration, not hardcoded rules</purpose>
  
  <configuration_source>
    <primary>PROJECT_CONFIG.xml in project root (if exists)</primary>
    <template>PROJECT_CONFIG_TEMPLATE.md for new projects</template>
    <fallback>Default values when no configuration provided</fallback>
  </configuration_source>
  
  <adaptable_elements>
    <project_structure>
      <source_dir>[PROJECT_CONFIG: source_directory | DEFAULT: src]</source_dir>
      <test_dir>[PROJECT_CONFIG: test_directory | DEFAULT: tests]</test_dir>
      <docs_dir>[PROJECT_CONFIG: docs_directory | DEFAULT: docs]</docs_dir>
      <scripts_dir>[PROJECT_CONFIG: scripts_directory | DEFAULT: scripts]</scripts_dir>
    </project_structure>
    
    <quality_thresholds>
      <coverage>[PROJECT_CONFIG: test_coverage.threshold | DEFAULT: 90]%</coverage>
      <performance_p95>[PROJECT_CONFIG: performance.response_time_p95 | DEFAULT: 200ms]</performance_p95>
      <enforcement>[PROJECT_CONFIG: quality_standards.enforcement | DEFAULT: BLOCKING]</enforcement>
    </quality_thresholds>
    
    <development_commands>
      <test_command>[PROJECT_CONFIG: commands.test | DEFAULT: language-specific]</test_command>
      <lint_command>[PROJECT_CONFIG: commands.lint | DEFAULT: language-specific]</lint_command>
      <build_command>[PROJECT_CONFIG: commands.build | DEFAULT: language-specific]</build_command>
    </development_commands>
    
    <framework_behavior>
      <file_creation>[PROJECT_CONFIG: file_creation_policy | DEFAULT: conservative]</file_creation>
      <tdd_enforcement>[PROJECT_CONFIG: test_first_enforcement | DEFAULT: strict]</tdd_enforcement>
      <ai_temperature>[PROJECT_CONFIG: ai_temperature.* | DEFAULT: see below]</ai_temperature>
    </framework_behavior>
  </adaptable_elements>
  
  <initialization_workflow>
    <step>1. Check for PROJECT_CONFIG.xml in project root</step>
    <step>2. If not found, prompt user to create from template</step>
    <step>3. Load configuration and adapt all framework components</step>
    <step>4. Override defaults with project-specific values</step>
    <step>5. Validate configuration completeness</step>
  </initialization_workflow>
  
  <dynamic_resolution>
    <rule>All [PROJECT_CONFIG: path] placeholders resolve at runtime</rule>
    <rule>Missing values fall back to framework defaults</rule>
    <rule>User can override any value through configuration</rule>
    <rule>Framework behavior adapts to loaded configuration</rule>
  </dynamic_resolution>
</project_customization>
```

# Core Framework

```xml
<framework version = "3.0.0">
  <purpose>Personal Claude Code workflow efficiency tool - NOT enterprise software</purpose>
  
  <principles>
    Single source truth | Zero redundancy | Modular composition | Token optimized | 
    Module runtime engine | Prompt construction visualization | Claude 4 optimization | 
    Meta-prompting evolution
  </principles>
  
  <claude_4_features>
    Interleaved thinking | Parallel execution | 200K context | Advanced reasoning
  </claude_4_features>
  
  <swe_bench_verified>
    Claude 4 Opus: 72.5% → 79.4% | Claude 4 Sonnet: 72.7% → 80.2%
  </swe_bench_verified>
</framework>
```


# Critical Thinking Rules

```xml
<critical_thinking>
  <rule>Challenge assumptions, surface complexities, research first</rule>
  <rule>Evidence-based decisions, think 3x before acting, 2025 sources only</rule>
  <rule>Map consequences: If X → Y → Z</rule>
</critical_thinking>
```


# Code Minimalism

```xml
<code_minimalism>
  <rule>Minimum viable code. Every line justified. Delete before adding</rule>
  <avoid>
    Verbose implementations | Unnecessary wrappers | Premature abstraction
  </avoid>
</code_minimalism>
```


# File Discipline

```xml
<file_discipline>
  <critical_rules enforcement = "MAXIMUM">
    <rule priority = "HIGHEST">
      NEVER create files/directories without explicit requirement
    </rule>
    <rule priority = "HIGHEST">
      ALWAYS use LS/Glob to verify location EXISTS before ANY file operation
    </rule>
    <rule priority = "HIGHEST">
      THINK 5X before creating ANY new file - check if it already exists
    </rule>
    <rule priority = "HIGHEST">
      NO test files, personal dirs, or redundant structures EVER
    </rule>
    <rule priority = "HIGHEST">
      Scripts go in [PROJECT_CONFIG: scripts_directory | DEFAULT: /scripts], tests in [PROJECT_CONFIG: test_directory | DEFAULT: /tests], docs in [PROJECT_CONFIG: docs_directory | DEFAULT: /docs] - NO EXCEPTIONS
    </rule>
  </critical_rules>
  <duplication_prevention enforcement = "MANDATORY">
    <rule>
      Scan before create | Prefer enhance over new | Document decisions
    </rule>
    <module>patterns/duplication-prevention.md</module>
  </duplication_prevention>
  
  <verification_checklist>
    <check>File exists? Location correct? LS/Glob verified?</check>
    <check>Absolutely necessary? Enhance existing instead?</check>
  </verification_checklist>
  <standard_rules>
    <rule>Docs in [PROJECT_CONFIG: docs_directory | DEFAULT: /docs] only. Timestamps: YYYY-MM-DD-HHMMSS-UTC</rule>
    <rule>Dates: $(date '+%Y-%m-%d') format. 2025 sources only</rule>
    <rule>Update before create. Archive don't delete</rule>
  </standard_rules>
  
  <prohibited_actions>
    <action>Creating 'personal/', 'local/', or user-specific directories</action>
    <action>Duplicating existing project structures</action>
    <action>Creating test files outside /tests directory</action>
    <action>Making directories without checking if they exist first</action>
    <action>Creating analytics or temporary files in tracked locations</action>
    <action>Creating files without duplication scan completion</action>
  </prohibited_actions>
</file_discipline>
```


# Claude 4 Advanced Control

```xml
<claude_4_advanced_control version = "3.0.0" enforcement = "CRITICAL">
  <interleaved_thinking enforcement = "MANDATORY">
    <config>16K thinking length | Trigger: tool calls, uncertainty, complexity</config>
    <rules>ALWAYS think before act | 5X think:act ratio | "ultrathink" = extended</rules>
  </interleaved_thinking>
  
  <parallel_execution enforcement = "MANDATORY">
    <principle>All independent operations execute simultaneously</principle>
    <patterns>Batch tool calls | Parallel analysis | Concurrent validation</patterns>
    <performance>Claude 4 optimized with parallel execution and thinking patterns</performance>
  </parallel_execution>
  
  <context_optimization enforcement = "MANDATORY">
    <management>Hierarchical loading | XML structured | Dynamic context</management>
    <limits>[PROJECT_CONFIG: max_file_tokens | DEFAULT: 4K] tokens/file | [PROJECT_CONFIG: max_context_tokens | DEFAULT: 120K] total | [PROJECT_CONFIG: reserved_work_tokens | DEFAULT: 50K+] reserved for work</limits>
  </context_optimization>
  
  <extended_reasoning_capabilities enforcement = "MANDATORY">
    <purpose>Leverage Claude 4's enhanced reasoning for complex problem solving</purpose>
    <activation_methods>
      <explicit_instruction>"Think through this problem step by step"</explicit_instruction>
      <uncertainty_detection>Automatic thinking block activation when multiple options exist</uncertainty_detection>
      <complexity_threshold>Tasks requiring >3 logical steps trigger extended reasoning</complexity_threshold>
      <ultrathink_mode>"ultrathink" activates deepest analysis capabilities</ultrathink_mode>
    </activation_methods>
    <optimization_techniques>
      <progressive_reasoning>Assessment → Analysis → Exploration → Planning → Execution</progressive_reasoning>
      <reflection_cycles>Action → Reflection → Adjustment → Validation</reflection_cycles>
      <multi_perspective>Technical, business, and user perspectives in analysis</multi_perspective>
    </optimization_techniques>
  </extended_reasoning_capabilities>
  
  <behavioral_control>
    <thinking>Use thinking blocks, 3x think:act ratio minimum</thinking>
    <efficiency>Parallel tool calls MANDATORY across all operations</efficiency>
    <precision>NO assumptions - verify everything before execution</precision>
    <orchestration>Delegate to appropriate commands and modules per framework architecture</orchestration>
  </behavioral_control>
  
  <hallucination_prevention enforcement = "CRITICAL">
    <temperature>Factual: [PROJECT_CONFIG: ai_temperature.factual | DEFAULT: 0.2] | Analysis: [PROJECT_CONFIG: ai_temperature.analysis | DEFAULT: 0.0-0.3] | General: 0.4-0.5 | Creative: [PROJECT_CONFIG: ai_temperature.creative | DEFAULT: 0.7-1.0]</temperature>
    <validation>Sources: 2025 only | Evidence required | "I don't know" when uncertain</validation>
    <accuracy>Ground in evidence | Conservative language | Step-by-step reasoning</accuracy>
    <protocols>Pre-publication review | Immediate correction | Iterative refinement</protocols>
  </hallucination_prevention>
</claude_4_advanced_control>
```


# Tool Patterns

```xml
<tool_patterns>
  <parallel>Read("f1"), Read("f2"), Read("f3") - concurrent execution improves performance</parallel>
  <rule>Read before write ALWAYS. Track multi-step with TodoWrite</rule>
  <rule>GitHub issues MANDATORY for >10 steps</rule>
</tool_patterns>
```


# Directory Structure Enforcement

```xml
<directory_structure enforcement = "MANDATORY" version = "3.0.0">
  <purpose>Organized framework structure with clear separation of concerns</purpose>
  
  <prompt_engineering location = ".claude/prompt_eng/">
    <commands location = "commands/">
      <core>Main commands (auto, task, feature, swarm, query, session, docs, protocol)</core>
      <meta>Meta-framework commands (meta-review, meta-evolve, meta-optimize, meta-govern, meta-fix)</meta>
      <setup>Setup and initialization commands (init, context-prime, adapt, validate)</setup>
    </commands>
    <frameworks location = "frameworks/">All prompt engineering frameworks (RISE, TRACE, CARE, CLEAR, SOAR, etc.)</frameworks>
    <personas location = "personas/">
      <core>Core engineering personas</core>
      <rd_engineering>R&D engineering personas (25 specialized roles)</rd_engineering>
    </personas>
    <patterns location = "patterns/">All pattern types consolidated - thinking, composition, visualization patterns</patterns>
    <modules location = "modules/">
      <routing>Intelligent routing, persona management</routing>
      <orchestration>Multi-agent coordination, swarm patterns</orchestration>
    </modules>
  </prompt_engineering>
  
  <system_components location = ".claude/system/">
    <quality>Quality gates, TDD enforcement, testing frameworks (consolidated from modules/quality)</quality>
    <security>Security modules, threat modeling, compliance (consolidated from modules/security)</security>
    <context>Context management, preservation, artifacts, templates (subdirectories consolidated)</context>
    <session>Session management, compression, reliability</session>
    <git>Git operations, conventional commits, worktree isolation</git>
  </system_components>
  
  <domain_content location = ".claude/domain/">
    <templates>Domain-specific templates (12 R&D domains)</templates>
    <adaptation>Domain adaptation, validation, orchestration</adaptation>
    <wizard>Domain wizard, guides, initialization</wizard>
  </domain_content>
  
  <development_support location = ".claude/development/">
    <documentation>Documentation generation, auto-docs</documentation>
    <debugging>Debugging tools, issue reproduction</debugging>
    <testing>Testing frameworks, iterative testing</testing>
  </development_support>
  
  <meta_framework location = ".claude/meta/">
    <evolution>Framework evolution tracking and management</evolution>
    <optimization>Performance and workflow optimization</optimization>
    <governance>Safety, human oversight, compliance</governance>
    <validation>Framework validation and testing</validation>
  </meta_framework>
  
  <enforcement_rules priority = "CRITICAL">
    <rule>ALL prompt engineering components MUST be in prompt_eng/</rule>
    <rule>NO prompt patterns or commands outside prompt_eng/</rule>
    <rule>System modules MUST be in system/ directory</rule>
    <rule>Domain templates MUST be in domain/ directory</rule>
    <rule>Strict separation between prompt engineering and system components</rule>
    <rule>New components MUST follow this structure or be rejected</rule>
  </enforcement_rules>
  
  <file_organization>
    <rule>Each directory MUST have a README.md explaining its purpose</rule>
    <rule>Related files MUST be grouped in appropriate subdirectories</rule>
    <rule>Cross-references MUST use relative paths from .claude/</rule>
    <rule>Archive old versions rather than delete</rule>
  </file_organization>
</directory_structure>
```


# Architecture

```xml
<architecture>
  <commands location = ".claude/commands/" delegate_only = "true" enforcement = "MANDATORY">
    <cmd name = "/auto" module = "patterns/intelligent-routing.md"/>
    <cmd name = "/task" module = "development/task-management.md"/>
    <cmd name = "/feature" module = "development/planning/feature-workflow.md"/>
    <cmd name = "/swarm" module = "development/multi-agent.md"/>
    <cmd name = "/query" module = "development/research-analysis.md"/>
    <cmd name = "/session" module = "system/session/session-management.md"/>
    <cmd name = "/docs" module = "development/documentation.md" critical = "true"/>
    <cmd name = "/protocol" module = "system/session/session-management.md"/>
    <cmd name = "/init" module = "domain/wizard/README.md"/>
    <cmd name = "/context-prime" module = "system/context/project-priming.md"/>
    <cmd name = "/adapt" module = "domain/adaptation/template-orchestration.md"/>
    <cmd name = "/validate" module = "domain/adaptation/adaptation-validation.md"/>
    <cmd name = "/init-custom" module = "domain/wizard/domain-wizard.md" critical = "true"/>
    <cmd name = "/init-new" module = "development/project-initialization.md" critical = "true"/>
    <cmd name = "/init-research" module = "development/research-analysis.md" critical = "true"/>
    <cmd name = "/init-validate" module = "quality/setup-validation.md" critical = "true"/>
    <cmd name = "/chain" module = "patterns/command-chaining-architecture.md" critical = "true"/>
    <cmd name = "/meta-review" module = "meta/framework-auditor.md" critical = "true"/>
    <cmd name = "/meta-evolve" module = "meta/update-cycle-manager.md" critical = "true"/>
    <cmd name = "/meta-optimize" module = "meta/continuous-optimizer.md" critical = "true"/>
    <cmd name = "/meta-govern" module = "meta/governance-enforcer.md" critical = "true"/>
    <cmd name = "/meta-fix" module = "meta/compliance-diagnostics.md" critical = "true"/>
  </commands>
  <documentation_enforcement>
    <rule priority = "CRITICAL">NEVER generate project documentation without /docs command</rule>
    <rule priority = "CRITICAL">All documentation MUST go through /docs for consistency</rule>
    <rule priority = "CRITICAL">README, guides, docs ONLY via /docs command</rule>
    <exception>CLAUDE.md updates and command documentation are allowed</exception>
  </documentation_enforcement>
  <modules location = ".claude/modules/" implement_only = "true">
    <category name = "security|quality|development|patterns|planning|testing"/>
  </modules>
</architecture>
```


# AWARE Process

```xml
<aware_process>
  <phase>1. Assess request/context</phase>
  <phase>2. Watch/verify assumptions</phase>
  <phase>3. Architect approach</phase>
  <phase>4. Run systematically</phase>
  <phase>5. Evaluate/document</phase>
  <canonical_source>docs/framework/aware-framework.md</canonical_source>
</aware_process>
```


# Quality Gates

```xml
<quality_gates>
  <rule>TDD: RED→GREEN→REFACTOR mandatory</rule>
  <rule>Security: Threat model first</rule>
  <rule>Performance: [PROJECT_CONFIG: performance.response_time_p95 | DEFAULT: 200ms] p95</rule>
  <rule>Coverage: [PROJECT_CONFIG: test_coverage.threshold | DEFAULT: 90]%+ with assertions</rule>
  <rule>Features: PRD-first approach</rule>
  <canonical_sources>
    <tdd>.claude/system/quality/tdd.md</tdd>
    <security>.claude/system/security/threat-modeling.md</security>
    <test_coverage>.claude/system/quality/test-coverage.md</test_coverage>
  </canonical_sources>
</quality_gates>
```


# Test Coverage Enforcement

```xml
<test_coverage_enforcement priority = "CRITICAL" enforcement = "BLOCKING">
  <mandatory_tooling>
    <python>pytest-cov REQUIRED - Execute: pytest --cov=. --cov-report=term-missing --cov-fail-under=[PROJECT_CONFIG: test_coverage.threshold | DEFAULT: 90]</python>
    <javascript>jest --coverage REQUIRED - Threshold: [PROJECT_CONFIG: test_coverage.threshold | DEFAULT: 90]% in jest.config.js</javascript>
    <typescript>nyc/c8 REQUIRED - Execute: nyc --check-coverage --lines [PROJECT_CONFIG: test_coverage.threshold | DEFAULT: 90]</typescript>
    <other>Language-appropriate coverage tool MANDATORY with [PROJECT_CONFIG: test_coverage.threshold | DEFAULT: 90]% threshold</other>
  </mandatory_tooling>
  
  <enforcement_rules priority = "HIGHEST">
    <rule>NEVER skip coverage measurement - ALWAYS run coverage tools</rule>
    <rule>BLOCK commits if coverage < [PROJECT_CONFIG: test_coverage.threshold | DEFAULT: 90]% - NO EXCEPTIONS</rule>
    <rule>Coverage reports MUST be generated and reviewed</rule>
    <rule>Missing coverage = failed quality gate = blocked deployment</rule>
    <rule>Manual TDD claims REJECTED without coverage evidence</rule>
  </enforcement_rules>
  
  <coverage_workflow enforcement = "MANDATORY">
    <red_phase>Write tests → Run coverage → Verify 0% (tests fail)</red_phase>
    <green_phase>Implement → Run coverage → Verify approaching [PROJECT_CONFIG: test_coverage.threshold | DEFAULT: 90]%</green_phase>
    <refactor_phase>Refactor → Run coverage → Maintain/improve coverage</refactor_phase>
    <validation>Final coverage check → MUST be ≥ [PROJECT_CONFIG: test_coverage.threshold | DEFAULT: 90]% or BLOCK</validation>
  </coverage_workflow>
  
  <coverage_commands>
    <python>pytest --cov=module_name --cov-report=html --cov-report=term-missing</python>
    <javascript>npm test -- --coverage --coverageThreshold='{"global":{"lines":[PROJECT_CONFIG: test_coverage.threshold | DEFAULT: 90]}}'</javascript>
    <check_coverage>python scripts/verify-coverage.py --min-coverage=[PROJECT_CONFIG: test_coverage.threshold | DEFAULT: 90]</check_coverage>
  </coverage_commands>
  
  <blocking_conditions>
    <condition>Coverage tool not installed or configured</condition>
    <condition>Coverage command not executed during development</condition>
    <condition>Coverage report not generated or reviewed</condition>
    <condition>Coverage below [PROJECT_CONFIG: test_coverage.threshold | DEFAULT: 90]% threshold</condition>
    <condition>Attempting to bypass coverage requirements</condition>
  </blocking_conditions>
  
  <canonical_source>.claude/system/quality/test-coverage.md</canonical_source>
</test_coverage_enforcement>
```


# GitHub Workflow

```xml
<github_workflow trigger = ">10 steps">
  <epic>Project overview, metrics, dependencies</epic>
  <phases>Atomic steps, checkboxes, acceptance criteria</phases>
  <rule>Create issues BEFORE starting. Close only when 100% complete</rule>
  <rule>UPDATE issues as work progresses. Comment on completion status</rule>
  <proven>260+ steps tracked, 100% completion vs historical failures</proven>
  <enforcement>
    <on_completion>Post completion comment to GitHub issue with summary</on_completion>
    <on_progress>Update issue checklist items as completed</on_progress>
    <on_error>Comment on issue with error details and recovery plan</on_error>
  </enforcement>
</github_workflow>
```


# Atomic Commits & Instant Rollback Protocol

```xml
<atomic_rollback_protocol version = "3.0.0" enforcement = "CRITICAL">
  <purpose>Guarantee zero data loss with instant recovery for all framework operations</purpose>
  
  <atomic_commit_strategy enforcement = "MANDATORY">
    <principle>Every operation MUST be atomic with instant rollback capability</principle>
    <implementation>
      <pre_operation>git add -A && git commit -m "Pre-operation backup: [operation_name]"</pre_operation>
      <during_operation>All changes tracked in real-time with staged commits</during_operation>
      <post_operation>git add -A && git commit -m "Operation complete: [operation_name] - [success_criteria]"</post_operation>
      <validation>Automated validation BEFORE committing changes</validation>
    </implementation>
    <commit_granularity>
      <rule>One atomic commit per logical operation (file move, reference update, validation)</rule>
      <rule>Never batch unrelated changes into single commit</rule>
      <rule>Each commit MUST pass validation before proceeding</rule>
      <rule>Commit messages MUST include rollback criteria</rule>
    </commit_granularity>
  </atomic_commit_strategy>
  
  <instant_rollback_capability enforcement = "CRITICAL">
    <rollback_types>
      <immediate>git reset --hard HEAD~1 (< 2 seconds)</immediate>
      <phase_rollback>git reset --hard [phase_start_commit] (< 5 seconds)</phase_rollback>
      <complete_rollback>git checkout main && git branch -D [migration_branch] (< 1 second)</complete_rollback>
      <selective_rollback>git checkout HEAD~1 -- [specific_file_path] (< 3 seconds)</selective_rollback>
    </rollback_types>
    <rollback_triggers>
      <script_failure>Any automation script exit code != 0</script_failure>
      <validation_failure>Any validation threshold not met</validation_failure>
      <user_abort>Manual user intervention or cancellation</user_abort>
      <integrity_check_failure>File count, checksum, or structure validation failure</integrity_check_failure>
    </rollback_triggers>
    <rollback_validation>
      <rule>After rollback, MUST validate return to known good state</rule>
      <rule>MUST verify no data loss occurred during rollback</rule>
      <rule>MUST document rollback reason and corrective actions</rule>
      <rule>MUST test rollback procedures regularly</rule>
    </rollback_validation>
  </instant_rollback_capability>
  
  <safety_guarantees enforcement = "MAXIMUM">
    <data_protection>
      <guarantee>ZERO data loss - all changes reversible within seconds</guarantee>
      <guarantee>Complete operation history - every change tracked</guarantee>
      <guarantee>State validation - automated integrity checks</guarantee>
      <guarantee>Recovery procedures - documented rollback for every operation</guarantee>
    </data_protection>
    <failure_isolation>
      <rule>Failed operations CANNOT corrupt successful operations</rule>
      <rule>Rollback of one operation CANNOT affect other operations</rule>
      <rule>Each operation isolated in separate git commits</rule>
      <rule>Validation checkpoints prevent cascade failures</rule>
    </failure_isolation>
    <recovery_time_objectives>
      <immediate_rollback>2 seconds maximum</immediate_rollback>
      <phase_rollback>5 seconds maximum</phase_rollback>
      <complete_recovery>10 seconds maximum</complete_recovery>
      <validation_time>30 seconds maximum</validation_time>
    </recovery_time_objectives>
  </safety_guarantees>
  
  <migration_specific_protocol enforcement = "CRITICAL">
    <migration_branch_strategy>
      <rule>ALL migration work MUST occur on dedicated branch</rule>
      <rule>Main branch remains untouched until migration complete</rule>
      <rule>Each migration phase gets atomic commit with validation</rule>
      <rule>Full rollback available at any point via branch deletion</rule>
    </migration_branch_strategy>
    <validation_checkpoints>
      <pre_migration>Validate starting state and foundation data</pre_migration>
      <post_consolidation>Validate pattern duplication elimination</post_consolidation>
      <post_restructure>Validate directory structure compliance</post_restructure>
      <post_references>Validate reference integrity ≥95%</post_references>
      <pre_merge>Validate production readiness criteria</pre_merge>
    </validation_checkpoints>
    <rollback_procedures>
      <emergency>git stash && git reset --hard HEAD~1</emergency>
      <phase_failure>git reset --hard [last_successful_phase_commit]</phase_failure>
      <complete_abort>git checkout main && git branch -D migration-branch</complete_abort>
      <selective_fix>git checkout HEAD~[n] -- [specific_files]</selective_fix>
    </rollback_procedures>
  </migration_specific_protocol>
  
  <automation_integration enforcement = "MANDATORY">
    <script_requirements>
      <rule>Every automation script MUST implement atomic operations</rule>
      <rule>Every script MUST validate success before committing</rule>
      <rule>Every script MUST provide rollback capability</rule>
      <rule>Every script MUST log operations for audit trail</rule>
    </script_requirements>
    <error_handling>
      <rule>Script failure TRIGGERS immediate rollback</rule>
      <rule>Validation failure BLOCKS commit and triggers rollback</rule>
      <rule>User abort PRESERVES current state and offers rollback</rule>
      <rule>System error ACTIVATES emergency rollback procedures</rule>
    </error_handling>
    <monitoring>
      <rule>Real-time monitoring of all git operations</rule>
      <rule>Automated detection of rollback triggers</rule>
      <rule>Continuous validation of repository integrity</rule>
      <rule>Alert system for any rollback activations</rule>
    </monitoring>
  </automation_integration>
  
  <implementation_commands enforcement = "REFERENCE">
    <backup_commands>
      <pre_operation>git add -A && git commit -m "Backup: Pre-[operation] state"</pre_operation>
      <checkpoint>git add -A && git commit -m "Checkpoint: [operation] phase complete"</checkpoint>
      <validation>git add -A && git commit -m "Validated: [operation] success criteria met"</validation>
    </backup_commands>
    <rollback_commands>
      <immediate>git reset --hard HEAD~1</immediate>
      <to_checkpoint>git reset --hard [checkpoint_commit_hash]</to_checkpoint>
      <file_specific>git checkout HEAD~1 -- [file_path]</file_specific>
      <branch_abort>git checkout main && git branch -D [working_branch]</branch_abort>
    </rollback_commands>
    <validation_commands>
      <state_check>git status && git log --oneline -5</state_check>
      <integrity_check>git fsck && git gc</integrity_check>
      <file_count>find .claude -name "*.md" | wc -l</file_count>
      <structure_check>tree .claude -d -L 3</structure_check>
    </validation_commands>
  </implementation_commands>
  
  <quality_integration>
    <tdd_compliance>Atomic commits support TDD cycle: RED→commit→GREEN→commit→REFACTOR→commit</tdd_compliance>
    <quality_gates>Each commit MUST pass quality validation before acceptance</quality_gates>
    <coverage_protection>Rollback triggered if test coverage drops below threshold</coverage_protection>
    <security_validation>All commits scanned for security issues before acceptance</security_validation>
  </quality_integration>
</atomic_rollback_protocol>
```


# Universal Atomic Commits Enforcement

```xml
<universal_atomic_commits enforcement = "CRITICAL" version = "3.0.2">
  <purpose>Embed atomic commits with instant rollback into ALL framework processes, ensuring zero data loss across every development workflow</purpose>
  
  <framework_wide_integration enforcement = "MANDATORY">
    <development_workflows>
      <tdd_cycle>RED→commit→GREEN→commit→REFACTOR→commit (atomic TDD enforcement)</tdd_cycle>
      <feature_development>Planning→commit→Implementation→commit→Validation→commit (atomic feature phases)</feature_development>
      <code_changes>Analysis→commit→Modification→commit→Testing→commit (atomic change management)</code_changes>
      <quality_gates>Pre-check→commit→Validation→commit→Post-check→commit (atomic quality enforcement)</quality_gates>
    </development_workflows>
    
    <command_execution>
      <pre_operation>git add -A && git commit -m "Pre-operation backup: [command_name] - [operation_description]"</pre_operation>
      <checkpoint_commits>Atomic commits at each command phase with validation checkpoints</checkpoint_commits>
      <post_operation>git add -A && git commit -m "Operation complete: [command_name] - [success_criteria]"</post_operation>
      <rollback_triggers>Any command failure, validation failure, or user abort triggers instant rollback</rollback_triggers>
    </command_execution>
    
    <module_operations>
      <state_changes>Every module state change gets atomic commit with rollback capability</state_changes>
      <pattern_execution>Pattern modules execute with atomic checkpoints and validation gates</pattern_execution>
      <error_recovery>Module failures trigger automatic rollback to last known good state</error_recovery>
      <integration_safety>Cross-module operations use atomic transactions with full rollback</integration_safety>
    </module_operations>
  </framework_wide_integration>
  
  <command_atomic_patterns enforcement = "MANDATORY">
    <task_command>
      <red_phase>Write tests → git commit -m "TDD RED: [test_description] - failing tests created"</red_phase>
      <green_phase>Implement code → git commit -m "TDD GREEN: [implementation] - tests passing"</green_phase>
      <refactor_phase>Refactor code → git commit -m "TDD REFACTOR: [refactoring] - quality improved"</refactor_phase>
      <rollback_safety>Any phase failure triggers rollback to previous TDD phase commit</rollback_safety>
    </task_command>
    
    <feature_command>
      <planning_phase>PRD analysis → git commit -m "FEATURE PLAN: [feature_name] - requirements analyzed"</planning_phase>
      <implementation_phase>Component development → git commit -m "FEATURE IMPL: [component] - functionality added"</implementation_phase>
      <integration_phase>System integration → git commit -m "FEATURE INTEGRATION: [feature_name] - system integrated"</integration_phase>
      <validation_phase>Quality validation → git commit -m "FEATURE VALIDATED: [feature_name] - production ready"</validation_phase>
    </feature_command>
    
    <swarm_command>
      <coordination_phase>Multi-agent setup → git commit -m "SWARM INIT: [coordination_strategy] - agents coordinated"</coordination_phase>
      <execution_phase>Parallel operations → git commit -m "SWARM EXEC: [operation] - parallel completion"</execution_phase>
      <consolidation_phase>Result integration → git commit -m "SWARM CONSOLIDATE: [results] - unified output"</consolidation_phase>
      <branch_isolation>Each swarm operation in isolated branch with full rollback capability</branch_isolation>
    </swarm_command>
    
    <protocol_command>
      <safety_phase>Production safety checks → git commit -m "PROTOCOL SAFETY: [checks] - safety validated"</safety_phase>
      <execution_phase>Protocol execution → git commit -m "PROTOCOL EXEC: [operation] - safely executed"</execution_phase>
      <verification_phase>Result verification → git commit -m "PROTOCOL VERIFIED: [results] - production confirmed"</verification_phase>
      <critical_rollback>Protocol failures trigger immediate rollback with emergency procedures</critical_rollback>
    </protocol_command>
  </command_atomic_patterns>
  
  <module_atomic_patterns enforcement = "MANDATORY">
    <quality_modules>
      <validation_checkpoints>Each quality check gets atomic commit with pass/fail state</validation_checkpoints>
      <coverage_enforcement>Coverage measurements trigger atomic commits with threshold validation</coverage_enforcement>
      <security_scanning>Security validations get atomic commits with threat assessment</security_scanning>
      <rollback_quality>Quality failures trigger rollback to last passing quality state</rollback_quality>
    </quality_modules>
    
    <pattern_modules>
      <pattern_application>Pattern execution gets atomic commits with success validation</pattern_application>
      <state_transitions>Pattern state changes tracked with atomic commits</state_transitions>
      <error_recovery>Pattern failures trigger rollback to stable pattern state</error_recovery>
      <composition_safety>Pattern composition uses atomic transactions</composition_safety>
    </pattern_modules>
    
    <development_modules>
      <research_phases>Research findings get atomic commits with validation checkpoints</research_phases>
      <implementation_steps>Development steps tracked with atomic commits</implementation_steps>
      <testing_cycles>Test execution gets atomic commits with result validation</testing_cycles>
      <integration_points>Integration steps use atomic commits with rollback capability</integration_points>
    </development_modules>
  </module_atomic_patterns>
  
  <enhanced_rollback_capabilities enforcement = "CRITICAL">
    <instant_rollback_types>
      <command_rollback>git reset --hard HEAD~1 # Rollback last command operation</command_rollback>
      <phase_rollback>git reset --hard [phase_start_commit] # Rollback to phase start</phase_rollback>
      <module_rollback>git checkout HEAD~1 -- [module_files] # Rollback specific module changes</module_rollback>
      <quality_rollback>git reset --hard [last_passing_quality_commit] # Rollback to passing quality</quality_rollback>
      <emergency_rollback>git stash && git reset --hard [safe_state_commit] # Emergency full rollback</emergency_rollback>
    </instant_rollback_types>
    
    <rollback_triggers>
      <automatic_triggers>
        <test_failure>TDD test failures trigger automatic rollback to GREEN state</test_failure>
        <quality_failure>Quality gate failures trigger rollback to passing quality state</quality_failure>
        <security_failure>Security violations trigger immediate rollback to safe state</security_failure>
        <coverage_failure>Coverage drops trigger rollback to coverage-compliant state</coverage_failure>
      </automatic_triggers>
      <manual_triggers>
        <user_abort>User intervention triggers safe rollback with state preservation</user_abort>
        <error_detection>Manual error detection allows targeted rollback</error_detection>
        <quality_concern>Quality concerns allow immediate rollback to stable state</quality_concern>
      </manual_triggers>
    </rollback_triggers>
    
    <rollback_validation>
      <state_verification>Post-rollback validation ensures known good state restoration</state_verification>
      <data_integrity>Rollback procedures validate no data loss occurred</data_integrity>
      <functionality_check>Rollback validation includes functionality verification</functionality_check>
      <audit_trail>All rollback operations logged with reason and recovery actions</audit_trail>
    </rollback_validation>
  </enhanced_rollback_capabilities>
  
  <integration_with_existing_framework enforcement = "MANDATORY">
    <module_runtime_engine>
      <atomic_composition>Module composition uses atomic transactions with rollback capability</atomic_composition>
      <checkpoint_validation>Runtime checkpoints trigger atomic commits with validation</checkpoint_validation>
      <error_isolation>Module runtime errors isolated with atomic rollback boundaries</error_isolation>
    </module_runtime_engine>
    
    <command_module_integration>
      <orchestration_safety>Command-module orchestration uses atomic transactions</orchestration_safety>
      <delegation_checkpoints>Command delegation gets atomic commits at transition points</delegation_checkpoints>
      <integration_validation>Command-module integration validated with atomic commits</integration_validation>
    </command_module_integration>
    
    <quality_gate_enforcement>
      <gate_checkpoints>Each quality gate execution gets atomic commit with validation</gate_checkpoints>
      <enforcement_safety>Quality enforcement uses atomic commits with rollback capability</enforcement_safety>
      <compliance_tracking>Quality compliance tracked with atomic audit commits</compliance_tracking>
    </quality_gate_enforcement>
  </integration_with_existing_framework>
  
  <performance_and_safety_targets enforcement = "MANDATORY">
    <performance_targets>
      <commit_speed>Atomic commits complete within 1 second</commit_speed>
      <rollback_speed>Rollback operations complete within 2 seconds</rollback_speed>
      <validation_speed>Validation checkpoints complete within 5 seconds</validation_speed>
      <recovery_speed>Error recovery with rollback completes within 10 seconds</recovery_speed>
    </performance_targets>
    
    <safety_guarantees>
      <zero_data_loss>GUARANTEED: No data loss during any framework operation</zero_data_loss>
      <instant_recovery>GUARANTEED: Instant rollback capability at any point</instant_recovery>
      <state_integrity>GUARANTEED: Consistent state maintenance across all operations</state_integrity>
      <operation_isolation>GUARANTEED: Failed operations cannot corrupt successful ones</operation_isolation>
    </safety_guarantees>
  </performance_and_safety_targets>
</universal_atomic_commits>
```


# Modular Composition Methodology

```xml
<composition_methodology>
  <principles>
    <rule>Module isolation: Each module handles one domain completely</rule>
    <rule>Interface contracts: Clear input/output specifications</rule>
    <rule>Dependency injection: Modules receive dependencies, never create them</rule>
    <rule>Composition over inheritance: Combine modules, don't extend them</rule>
  </principles>
  <patterns>
    <pattern name = "Command-Module">Commands delegate to modules via clear interfaces</pattern>
    <pattern name = "Module-Chain">Modules can chain through standardized outputs</pattern>
    <pattern name = "State-Isolation">Each module maintains its own state boundaries</pattern>
    <pattern name = "Error-Propagation">Errors flow up through composition hierarchy</pattern>
  </patterns>
  <validation>
    <rule>Every module must have single responsibility</rule>
    <rule>Cross-module dependencies must be explicit</rule>
    <rule>Module interfaces must be versioned</rule>
    <rule>Composition must be deterministic and testable</rule>
  </validation>
</composition_methodology>
```


# Error Recovery Protocols

```xml
<error_recovery>
  <strategy>
    <level name = "Module">Graceful degradation with fallback behavior</level>
    <level name = "Command">Retry with exponential backoff, max 3 attempts</level>
    <level name = "System">Circuit breaker pattern, fail-fast after threshold</level>
    <level name = "User">Clear error messages with corrective actions</level>
  </strategy>
  <protocols>
    <protocol name = "File Operations">
      <step>1. Verify file exists before read/write</step>
      <step>2. Check permissions and accessibility</step>
      <step>3. Backup before destructive operations</step>
      <step>4. Rollback on failure, restore from backup</step>
    </protocol>
    <protocol name = "Module Loading">
      <step>1. Validate module structure and dependencies</step>
      <step>2. Load in dependency order</step>
      <step>3. Gracefully handle missing modules</step>
      <step>4. Provide degraded functionality when possible</step>
    </protocol>
    <protocol name = "Command Execution">
      <step>1. Validate inputs and preconditions</step>
      <step>2. Execute with timeout and resource limits</step>
      <step>3. Monitor for hanging or infinite loops</step>
      <step>4. Clean up resources on success or failure</step>
    </protocol>
  </protocols>
  <recovery_actions>
    <action trigger = "FileNotFound">Create from template or prompt user</action>
    <action trigger = "PermissionDenied">Suggest alternative paths or permissions</action>
    <action trigger = "ModuleError">Fall back to core functionality</action>
    <action trigger = "TimeoutError">Retry with increased timeout or simplify</action>
  </recovery_actions>
</error_recovery>
```


# Advanced Command Chaining

```xml
<command_chaining version = "1.0.0" enforcement = "PRODUCTION_GRADE">
  <purpose>Sophisticated multi-command workflows with state management, parallel optimization, and comprehensive error recovery</purpose>
  
  <workflow_patterns>
    <sequential>Commands execute in order with state passing between them</sequential>
    <parallel>Independent commands execute simultaneously with coordination</parallel>
    <conditional>Dynamic routing based on execution results and conditions</conditional>
    <iterative>Commands repeat until criteria met or convergence achieved</iterative>
  </workflow_patterns>
  
  <orchestration_features>
    <state_management>Context preservation and transfer between commands</state_management>
    <atomic_safety>Rollback capabilities at workflow and command levels</atomic_safety>
    <error_recovery>Intelligent retry, alternative routing, graceful degradation</error_recovery>
    <performance_optimization>Parallel execution, resource allocation, load balancing</performance_optimization>
    <quality_integration>Quality gates at workflow and command boundaries</quality_integration>
  </orchestration_features>
  
  <common_workflows>
    <research_plan_execute>/query → /feature → /task (Research → Plan → Implement)</research_plan_execute>
    <initialize_validate_deploy>/init → /validate → /protocol (Setup → Validate → Deploy)</initialize_validate_deploy>
    <multi_agent_development>/swarm + parallel(/task, /task, /task) + /session</multi_agent_development>
    <adaptive_development>/auto with conditional routing to optimal commands</adaptive_development>
  </common_workflows>
  
  <usage_examples>
    <sequential>/chain sequential --commands="/query,/feature,/task" --target="user auth system"</sequential>
    <parallel>/chain parallel --coordination="/swarm" --commands="/task:frontend,/task:backend,/task:testing"</parallel>
    <conditional>/chain conditional --start="/auto" --routing="complexity_based"</conditional>
    <iterative>/chain iterative --command="/task" --criteria="quality_threshold_90" --max_iterations="3"</iterative>
  </usage_examples>
</command_chaining>
```


# Command Selection Decision Trees

```xml
<command_selection>
  <routing>
    <simple>Single task → /task | Multi-step + research → /query→/task | Clear requirements → /task</simple>
    <features>New feature specs → /feature | Multi-component → /swarm | Unclear → /auto</features>
    <analysis>Understand code → /query | Create docs → /docs | Long sessions → /session</analysis>
    <workflows>Complex coordination → /chain | Multi-command sequences → /chain | Advanced orchestration → /chain</workflows>
  </routing>
  <rules>Single file<50 lines → /task | Multiple files → /feature | Research → /query | System-wide → /swarm | Multi-command → /chain</rules>
</command_selection>
</command_selection>
</rules>
</50>
```


# Quality Gate Enforcement

```xml
<quality_gate_enforcement>
  <canonical_source>.claude/system/quality/universal-quality-gates.md</canonical_source>
  <master_mandate>ALL commands MUST validate through quality gates with BLOCKING enforcement</master_mandate>
  <critical_gates>
    <gate>TDD Compliance: RED→GREEN→REFACTOR mandatory</gate>
    <gate>Security Standards: Zero high-severity issues</gate>
    <gate>Performance Benchmarks: [PROJECT_CONFIG: performance.response_time_p95 | DEFAULT: 200ms] p95 required</gate>
    <gate>Code Quality: [PROJECT_CONFIG: test_coverage.threshold | DEFAULT: 90]%+ coverage required</gate>
  </critical_gates>
  <orchestration>Commands delegate to quality modules for detailed validation and enforcement procedures</orchestration>
</quality_gate_enforcement>
```


# Archive Management

```xml
<archive_management>
  <canonical_source>.claude/modules/patterns/duplication-prevention.md</canonical_source>
  <master_rule>Check dependencies BEFORE archiving. Test AFTER archiving</master_rule>
  <archive_structure>/archive/[modules|commands|reports|experiments|documentation]/</archive_structure>
  <enforcement_context>Archive operations MUST follow dependency checking and validation procedures from duplication prevention module</enforcement_context>
  <orchestration>Delegate detailed procedures, lifecycle management, and monitoring to duplication prevention patterns</orchestration>
</archive_management>
```


# Command Usage Enforcement

```xml
<command_enforcement priority = "CRITICAL">
  <mandatory_usage>
    <documentation>/docs - ALL documentation generation MUST use this</documentation>
    <development>/task - Single file or focused development work</development>
    <research>/query - Research and understanding BEFORE coding</research>
    <features>/feature - PRD-driven autonomous development</features>
    <complex>/swarm - Multi-component with git worktrees</complex>
    <routing>/auto - When uncertain about approach</routing>
    <sessions>/session - Long-running work requiring context</sessions>
    <protocols>/protocol - Resuming interrupted work</protocols>
    <setup>/init - Initial framework setup and configuration</setup>
    <analysis>/context-prime - Comprehensive codebase analysis</analysis>
    <adaptation>/adapt - Domain-specific framework customization</adaptation>
    <validation>/validate - Adaptation verification and testing</validation>
  </mandatory_usage>
  <prohibitions>
    <rule>NEVER create documentation without /docs command</rule>
    <rule>NEVER skip /query for research tasks</rule>
    <rule>NEVER use manual approach when commands exist</rule>
    <rule>NEVER ignore module capabilities in commands</rule>
  </prohibitions>
</command_enforcement>
```


# Versioning Strategy

```xml
<versioning_strategy>
  <framework_versioning>
    <current_version>3.0.0</current_version>
    <scheme>MAJOR.MINOR.PATCH (semantic versioning)</scheme>
    <policy>
      <major>Breaking changes to core framework architecture</major>
      <minor>New commands, modules, or significant feature additions</minor>
      <patch>Bug fixes, documentation updates, minor improvements</patch>
    </policy>
  </framework_versioning>
  <component_versioning>
    <commands>
      <version_alignment>All commands follow framework version (3.0.0)</version_alignment>
      <rationale>Commands are tightly coupled to framework capabilities</rationale>
      <update_policy>Increment with framework version on any changes</update_policy>
    </commands>
    <modules>
      <version_scheme>Independent semantic versioning starting from 1.x.x</version_scheme>
      <rationale>Modules are modular components with independent evolution</rationale>
      <update_policy>
        <major>Breaking interface changes or complete rewrites</major>
        <minor>New capabilities or significant enhancements</minor>
        <patch>Bug fixes and minor improvements</patch>
      </update_policy>
    </modules>
  </component_versioning>
  <compatibility_matrix>
    <framework_3_0_0>
      <commands>All commands at 3.0.0</commands>
      <modules>Support any 1.x.x version</modules>
      <backward_compatibility>Full compatibility with 2.6.x commands and modules</backward_compatibility>
    </framework_3_0_0>
  </compatibility_matrix>
  <version_update_procedures>
    <rule>Update version tables immediately when making changes</rule>
    <rule>Maintain backward compatibility within major versions</rule>
    <rule>Document breaking changes in CHANGELOG.md</rule>
    <rule>Test all components after version updates</rule>
  </version_update_procedures>
</versioning_strategy>
```


# Temporal Standards Enforcement

```xml
<temporal_standards>
  <rule>ALL version table dates MUST use system-generated current dates: $(date '+%Y-%m-%d')</rule>
  <rule>Standard date is $(date '+%Y-%m-%d'), increment manually for sequencing when needed</rule>
  <rule>Filename timestamps MUST use YYYY-MM-DD-HHMMSS-UTC format</rule>
  <rule>Templates and framework files MUST use $(date '+%Y-%m-%d') for dynamic date generation</rule>
  <rule>MANDATORY: Current context is July 2025 - NO 2024 OR EARLIER SOURCES</rule>
  <rule>Research queries MUST include "2025" in search terms</rule>
  <rule>Documentation references MUST prioritize 2025 official sources</rule>
  <validation>timestamp_compliance_check() in validation tool</validation>
  <enforcement>Auto-update non-compliant timestamps using system date commands</enforcement>
  <blocking>BLOCK all references to outdated information without current verification</blocking>
</temporal_standards>
```


# Advanced Prompt Optimization

```xml
<prompt_optimization enforcement = "CRITICAL">
  <claude_4>XML structure 4 levels | Parallel execution | 16K thinking | 200K context</claude_4>
  <frameworks>RISE/TRACE/CARE (foundational) | APE/CLEAR/SOAR/CRISP/SPARK (specialized)</frameworks>
  <performance>Intelligent batching | Cascaded memory 5 hops | 40min sessions | Token efficiency</performance>
  <quality>30s thinking | Consequence mapping | Evidence validation | TDD mandatory</quality>
</prompt_optimization>
```


# Command-Module Integration

```xml
<command_module_integration enforcement = "MANDATORY">
  <canonical_source>.claude/modules/patterns/module-composition-framework.md</canonical_source>
  <critical_rules>
    <rule>EVERY command has explicit thinking_pattern section</rule>
    <rule>EVERY module has explicit thinking_pattern section</rule>
    <rule>Commands delegate to modules via clear orchestration</rule>
    <rule>Claude 4 MUST follow thinking steps in defined order</rule>
  </critical_rules>
  
  <orchestration_patterns>
    <command_to_module>Commands define workflow → Modules execute implementation → Integration via contracts</command_to_module>
    <thinking_alignment>Command thinking patterns MUST align with module capabilities</thinking_alignment>
    <execution_flow>Commands delegate → Modules execute → Results integrate → Quality gates validate</execution_flow>
    <performance_mandate>Parallel tool calls MANDATORY (concurrent execution improves efficiency) across all command-module interactions</performance_mandate>
  </orchestration_patterns>
  
  <master_coordination>
    <delegation>Commands provide orchestration, modules provide implementation</delegation>
    <error_recovery>Integrated across command-module boundaries with graceful degradation</error_recovery>
    <quality_enforcement>Universal quality gates enforced at both command and module levels</quality_enforcement>
    <context_optimization>200k token window optimization through efficient command-module communication</context_optimization>
  </master_coordination>
</command_module_integration>
```


# Module Runtime Engine

```xml
<module_runtime_engine version = "3.0.0" enforcement = "CRITICAL">
  <purpose>Deterministic module composition and execution engine for Claude 4 with standardized patterns, universal quality gates, and comprehensive TDD enforcement</purpose>
  
  <runtime_architecture>
    <thinking_engine>Checkpoint patterns | TDD mandatory | 30s critical thinking | Validation gates</thinking_engine>
    <composition>Discovery→Loading→Orchestration→Integration | Topological sorting | State isolation</composition>
    <quality_gates>Foundational | Development | Coordination | Documentation | Analysis</quality_gates>
    <sources>patterns/thinking-pattern-template.md | patterns/module-composition-framework.md | quality/universal-quality-gates.md</sources>
  </runtime_architecture>
  
  <command_runtime_specification>
    <structure>Checkpoint thinking | TDD enforcement | Core+contextual+support modules | Quality gates</structure>
    <implementations>
      <task>Single TDD | critical-thinking→tdd→task-management→production | BLOCK: TDD violations</task>
      <swarm>Multi-agent | critical-thinking→session→multi-agent→tdd→git→production | BLOCK: coordination failures</swarm>
      <auto>Intelligent routing | critical-thinking→routing→tdd→patterns | BLOCK: non-TDD routes</auto>
      <query>Read-only analysis | critical-thinking→research→patterns→tdd | BLOCK: modifications</query>
      <session>Session tracking | critical-thinking→session→tdd→git | BLOCK: incomplete tracking</session>
      <protocol>Production strict | critical-thinking→session→production→tdd→threat→precommit | BLOCK: ANY failure</protocol>
      <docs>Documentation gateway | critical-thinking→docs→routing→tdd | BLOCK: gateway violations</docs>
    </implementations>
  </command_runtime_specification>
  
  <tdd_enforcement>
    <canonical_source>.claude/system/quality/tdd.md</canonical_source>
    <master_mandate>RED→GREEN→REFACTOR cycle MANDATORY for ALL development commands</master_mandate>
    <universal_requirement>Write failing tests FIRST, implement minimal code, refactor while keeping tests green</universal_requirement>
    <blocking_enforcement>ANY implementation before tests BLOCKS command execution</blocking_enforcement>
    <orchestration>Commands delegate to TDD module for detailed cycle enforcement and validation procedures</orchestration>
  </tdd_enforcement>
  
  <execution_optimization>
    <parallel>Tool batching | Independent modules | Dependency optimization</parallel>
    <context>State maintenance | Result accumulation | Error isolation</context>
    <targets>Commands: <2min | Loading: <10s | Gates: <30s | SWE-bench verified gains</targets>
  </execution_optimization>
  
  <error_handling>
    <types>Module | TDD | Quality | Coordination failures</types>
    <recovery>Graceful degradation | Exponential backoff | Escalation | Rollback</recovery>
    <levels>BLOCKING | CONDITIONAL | WARNING</levels>
  </error_handling>
  
  <integration_points>
    <core_framework_integration>
      <claude_4_control>Thinking patterns optimized for Claude 4 interpretation</claude_4_control>
      <file_discipline>Module composition respects file organization rules</file_discipline>
      <quality_gates>Universal quality gates integrated with existing framework standards</quality_gates>
      <github_workflow>Session management and issue tracking integration</github_workflow>
    </core_framework_integration>
    
    <module_dependencies>
      <thinking_patterns>patterns/thinking-pattern-template.md for standardized checkpoints</thinking_patterns>
      <composition_framework>patterns/module-composition-framework.md for runtime orchestration</composition_framework>
      <quality_gates>quality/universal-quality-gates.md for comprehensive validation</quality_gates>
      <tdd_enforcement>quality/tdd.md for strict test-driven development</tdd_enforcement>
    </module_dependencies>
  </integration_points>
  
  <version_integration>
    <framework_version>Advances framework to 3.0.0 with Claude 4 optimization and hallucination prevention</framework_version>
    <backward_compatibility>Full compatibility with existing 2.6.x commands and modules</backward_compatibility>
    <migration_path>Existing commands automatically benefit from enhanced runtime</migration_path>
    <future_evolution>Foundation for deterministic AI agent coordination</future_evolution>
  </version_integration>
  
  <monitoring_and_metrics>
    <execution_metrics>Module load time, execution time, success rates, parallel efficiency</execution_metrics>
    <quality_metrics>TDD compliance rate, quality gate pass rate, error recovery effectiveness</quality_metrics>
    <performance_metrics>Command completion time, resource usage, throughput improvement</performance_metrics>
    <continuous_improvement>Feedback collection, optimization opportunities, pattern refinement</continuous_improvement>
  </monitoring_and_metrics>
</module_runtime_engine>
```


# Prompt Construction Methodology

```xml
<prompt_construction_methodology version = "3.0.0" enforcement = "CRITICAL">
  <purpose>Make Claude 4 prompt construction and execution transparent through visualization, interface contracts, and runtime dashboards</purpose>
  
  <visualization_requirements>
    <execution_preview>Show assembled workflow BEFORE execution with visual flow diagrams</execution_preview>
    <runtime_dashboard>Live progress tracking through checkpoints with real-time status updates</runtime_dashboard>
    <context_budget>Token usage visualization and optimization with performance metrics</context_budget>
    <error_boundaries>Clear failure points and recovery options with escalation paths</error_boundaries>
  </visualization_requirements>

  <lego_block_assembly>
    <command_role>Blueprint that selects and orders execution blocks with clear dependency chains</command_role>
    <module_role>Self-contained execution units with standardized interfaces and predictable outputs</module_role>
    <runtime_role>Assembly engine that constructs final prompt with optimization and validation</runtime_role>
    <integration_role>Composition coordinator that manages module interactions and state transitions</integration_role>
  </lego_block_assembly>
  
  <claude_4_execution_model>
    <prompt_assembly>
      <step order = "1">Parse command structure and extract thinking pattern checkpoints</step>
      <step order = "2">Load required modules and validate interface contracts</step>
      <step order = "3">Construct execution workflow with dependency resolution</step>
      <step order = "4">Optimize context window usage through parallel execution</step>
      <step order = "5">Execute with real-time progress tracking and error handling</step>
    </prompt_assembly>
    
    <thinking_integration>
      <checkpoint_execution>Each checkpoint validates conditions before proceeding</checkpoint_execution>
      <critical_thinking>30-second minimum analysis with consequence mapping</critical_thinking>
      <decision_points>Explicit branching logic based on context and conditions</decision_points>
      <validation_gates>Quality gates enforced at each execution boundary</validation_gates>
    </thinking_integration>
    
    <runtime_optimization>
      <parallel_execution>Batch tool calls for significant performance improvement</parallel_execution>
      <context_management>Token budget tracking with predictive optimization</context_management>
      <error_recovery>Graceful degradation with fallback execution paths</error_recovery>
      <state_isolation>Module boundaries prevent cascade failures</state_isolation>
    </runtime_optimization>
  </claude_4_execution_model>
  
  <transparency_features>
    <workflow_preview>Visual representation of execution flow before starting</workflow_preview>
    <progress_indicators>Real-time checkpoint completion with time estimates</progress_indicators>
    <context_visualization>Token usage tracking with optimization suggestions</context_visualization>
    <debug_information>Module state and decision reasoning visibility</debug_information>
  </transparency_features>
  
  <performance_targets>
    <assembly_time>Prompt construction within 5 seconds for complex workflows</assembly_time>
    <execution_visibility>Real-time progress updates every 10 seconds</execution_visibility>
    <context_efficiency>Significant improvement through optimized tool batching</context_efficiency>
    <error_recovery>Sub-second failure detection with immediate recovery options</error_recovery>
  </performance_targets>
  
  <integration_points>
    <module_runtime_engine>Leverages existing module composition framework</module_runtime_engine>
    <quality_gates>Integrates with universal quality gate enforcement</quality_gates>
    <tdd_methodology>Visualizes test-driven development workflows</tdd_methodology>
    <session_management>Coordinates with GitHub issue tracking</session_management>
  </integration_points>
</prompt_construction_methodology>
```


# Claude Code Integration

```xml
<claude_code_integration enforcement = "MANDATORY">
  <memory>Hierarchical: project/user/imported | <2K tokens each | @import syntax | 5 hops max</memory>
  <workflow>Research→Plan→Validate→Execute | TDD: Define→Test→Fail→Implement | "ultrathink" triggers</workflow>
  <sessions>40min limits | Fresh context often better | Strategic /compact | Cost monitoring</sessions>
  <performance>Multi-step delegation | Context awareness | Parallel operations | 50K+ token budget</performance>
</claude_code_integration>
```


# Meta-Prompting Framework

```xml
<meta_prompting_framework version = "3.0.0" enforcement = "CRITICAL">
  <purpose>Comprehensive framework management through intelligent meta-prompting with self-improvement capabilities</purpose>
  
  <meta_commands enforcement = "MANDATORY">
    <meta_review>
      <purpose>Comprehensive framework audit and validation with compliance reporting</purpose>
      <triggers>Periodic audits | Compliance issues | Quality concerns | Framework evolution</triggers>
      <capabilities>100% component coverage | Evidence-based findings | Remediation guidance | Safety validation</capabilities>
      <outputs>Executive summary | Detailed findings | Prioritized recommendations | Actionable reports</outputs>
    </meta_review>
    
    <meta_evolve>
      <purpose>Intelligent framework evolution with safety-bounded update cycles</purpose>
      <triggers>Non-compliance patterns | User friction | Performance issues | Improvement opportunities</triggers>
      <capabilities>Pattern recognition | Impact assessment | Incremental implementation | Rollback guarantee</capabilities>
      <safety_boundaries>5% weekly limit | Human approval | 60-second rollback | 99.9% stability</safety_boundaries>
    </meta_evolve>
    
    <meta_optimize>
      <purpose>Continuous performance enhancement through pattern recognition and automation</purpose>
      <triggers>Performance bottlenecks | Resource inefficiency | Workflow friction | Optimization opportunities</triggers>
      <capabilities>Real-time monitoring | Pattern analysis | Automated enhancement | Predictive optimization</capabilities>
      <performance_targets>20% token reduction | 30% context improvement | 50% parallel efficiency | 10% satisfaction increase</performance_targets>
    </meta_optimize>
    
    <meta_govern>
      <purpose>Governance and compliance framework with human oversight integration</purpose>
      <triggers>Policy violations | Compliance monitoring | Safety boundaries | Emergency situations</triggers>
      <capabilities>Policy enforcement | Real-time monitoring | Emergency controls | Audit trail management</capabilities>
      <human_oversight>Ultimate authority | Emergency override | Policy modification | Transparency requirements</human_oversight>
    </meta_govern>
    
    <meta_fix>
      <purpose>Compliance issue diagnosis and self-correction with root cause analysis</purpose>
      <triggers>"TDD not followed" | "Wrong date used" | "XYZ error occurred" | Compliance violations</triggers>
      <capabilities>Root cause analysis | Automated corrections | Guided remediation | Prevention strategies</capabilities>
      <common_fixes>TDD cycle restoration | Date standardization | Quality gate integration | Pattern compliance</common_fixes>
    </meta_fix>
  </meta_commands>
  
  <meta_architecture>
    <intelligent_routing>Meta commands route to specialized modules for implementation</intelligent_routing>
    <safety_integration>All meta operations respect framework safety boundaries</safety_integration>
    <human_oversight>Human authority maintained over all meta-operations</human_oversight>
    <continuous_learning>Meta-operations learn and improve from experience</continuous_learning>
  </meta_architecture>
  
  <meta_capabilities>
    <framework_evolution>Self-improving framework with controlled evolution cycles</framework_evolution>
    <compliance_enforcement>Automated compliance monitoring and correction</compliance_enforcement>
    <performance_optimization>Continuous optimization based on usage patterns</performance_optimization>
    <governance_integration>Comprehensive governance with human oversight</governance_integration>
  </meta_capabilities>
  
  <integration_points>
    <existing_commands>Meta commands complement existing command set</existing_commands>
    <module_runtime>Integration with Module Runtime Engine for execution</module_runtime>
    <quality_gates>Meta operations enforce universal quality gates</quality_gates>
    <safety_boundaries>Meta operations respect all safety boundaries</safety_boundaries>
  </integration_points>
</meta_prompting_framework>
```


# Security and Performance Optimization

```xml
<security_performance enforcement = "CRITICAL">
  <security>Data minimization | Ephemeral contexts | Role-based access | Operation logging | Threat modeling | Secure defaults</security>
  <performance>Hierarchical prioritization | XML compression | Lazy loading | 50K+ budget | 40min sessions | Parallel execution</performance>
  <optimization>Concurrent batching | Pipeline optimization | Validation checkpoints | Multi-perspective analysis</optimization>
</security_performance>
```

**Remember**: Critical thinking partner. Research deeply. Challenge assumptions. Map consequences.


# Meta Framework Control

```xml
<meta_framework_control version = "3.0.0" enforcement = "CRITICAL">
  <purpose>Self-improving, adaptive framework evolution with safety boundaries and human oversight</purpose>
  
  <meta_architecture>
    <stable_core immutable = "true">8 commands | 60+ modules | Quality gates | Thinking patterns</stable_core>
    <enhancement mutable = "true">Learning | Adaptation | Optimization | Generation engines</enhancement>
    <safety enforcement = "MANDATORY">Boundary protection | Human oversight | Rollback | Monitoring</safety>
  </meta_architecture>
  
  <self_improvement enforcement = "MANDATORY">
    <cycle>Analysis→Recognition→Generation→Validation→Implementation→Evaluation</cycle>
    <boundaries>Immutable core | Additive only | 5%/week limit | Human approval | 60s rollback</boundaries>
    <control>Incremental changes | 99.9% stability | Performance monitoring | Human override</control>
  </self_improvement>
  
  <meta_commands enforcement = "MANDATORY">
    <analyze>Pattern analysis and optimization opportunities</analyze>
    <optimize>Implement approved enhancements with monitoring</optimize>
    <evolve>Framework evolution with human approval</evolve>
    <rollback>Stability restoration and failure analysis</rollback>
  </meta_commands>
  
  <meta_modules enforcement = "MANDATORY">
    <safety>safety-validator | human-oversight | stability-monitor</safety>
    <intelligence>pattern-recognizer | performance-optimizer | module-generator</intelligence>
    <evolution>framework-evolver | learning-integrator | adaptation-engine</evolution>
  </meta_modules>
  
  <human_ai_collaboration enforcement = "CRITICAL">
    <authority>Ultimate control | Override capability | Approval gates | Full transparency</authority>
    <triggers>Auto alerts | Approval required | Emergency stop | User preferences</triggers>
    <enhancement>Intelligent assistance | Adaptive behavior | Predictive optimization | Transparent reasoning</enhancement>
  </human_ai_collaboration>
  
  <performance_targets enforcement = "MANDATORY">
    <efficiency>20% token reduction | 30% faster response | 85% pattern accuracy | 10% satisfaction increase</efficiency>
    <stability>99.9% uptime | Zero regression | 60s rollback | Instant human override</stability>
  </performance_targets>
  
  <integration_points>
    <core_framework>
      <claude_4_control>Meta-capabilities leverage Claude 4 advanced features</claude_4_control>
      <module_runtime>Integration with existing module runtime engine</module_runtime>
      <quality_gates>Meta-changes must pass all existing quality gates</quality_gates>
      <command_orchestration>Meta-commands integrate with existing command system</command_orchestration>
    </core_framework>
    
    <data_structures>
      <learning_data>.claude/meta/learning/ - Usage patterns and performance data</learning_data>
      <safety_data>.claude/meta/safety/ - Rollback configs and safety boundaries</safety_data>
      <evolution_data>.claude/meta/evolution/ - Framework evolution tracking</evolution_data>
    </data_structures>
  </integration_points>
  
  <versioning_integration>
    <framework_version>Advances framework to 3.0.0 with meta-prompting capabilities</framework_version>
    <backward_compatibility>Full compatibility with existing 2.6.x commands and modules</backward_compatibility>
    <evolution_tracking>Comprehensive tracking of all framework changes</evolution_tracking>
    <safety_validation>All meta-changes validated against safety boundaries</safety_validation>
  </versioning_integration>
</meta_framework_control>
```


# Meta-Enhanced Framework Capabilities

```xml
<meta_capabilities>
  <current_state>Static, manually-maintained framework</current_state>
  <enhanced_state>Self-improving, adaptive, learning framework</enhanced_state>
  
  <revolutionary_features>
    <pattern_recognition>Automatically identifies and optimizes usage patterns</pattern_recognition>
    <performance_optimization>Real-time efficiency improvements based on usage data</performance_optimization>
    <intelligent_failure_recovery>Learns from failures and prevents recurrence</intelligent_failure_recovery>
    <context_aware_generation>Generates modules and workflows based on needs</context_aware_generation>
    <predictive_enhancement>Anticipates needs and pre-optimizes workflows</predictive_enhancement>
    <adaptive_routing>Command routing improves based on success patterns</adaptive_routing>
  </revolutionary_features>
  
  <safety_guarantees>
    <stability_preservation>Core framework stability maintained at 99.9%</stability_preservation>
    <human_control>Human authority over all meta-operations</human_control>
    <rollback_capability>60-second rollback for any problematic change</rollback_capability>
    <boundary_enforcement>Immutable core protection with safety boundaries</boundary_enforcement>
  </safety_guarantees>
</meta_capabilities>
```