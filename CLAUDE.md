| version | last_updated | status |
|---------|--------------|--------|
| 3.0.0   | 2025-07-16   | stable |

# CLAUDE.md - Framework Control Document

# Overview

<purpose>Personal Claude Code workflow efficiency tool - NOT enterprise software</purpose>

# 🔗 Repository Information

```xml
<repository_config enforcement = "HARDCODED" version = "3.0.0">
  <github_details>
    <repository_url>https://github.com/swm-sink/claude-code-modular-prompts</repository_url>
    <repository_name>claude-code-modular-prompts</repository_name>
    <owner>swm-sink</owner>
    <default_branch>main</default_branch>
    <current_branch>framework-simplification-v3</current_branch>
    <clone_url>git@github.com:swm-sink/claude-code-modular-prompts.git</clone_url>
    <https_clone>https://github.com/swm-sink/claude-code-modular-prompts.git</https_clone>
  </github_details>
  
  <project_structure>
    <root_directory>/Users/smenssink/Documents/Github/claude-code-modular-prompts</root_directory>
    <framework_files>
      <claude_md>CLAUDE.md</claude_md>
      <project_config>PROJECT_CONFIG.xml</project_config>
      <framework_directory>.claude/</framework_directory>
      <getting_started>GETTING_STARTED.md</getting_started>
      <streamlit_dashboard>streamlit_dashboard/</streamlit_dashboard>
    </framework_files>
    <deployment_documentation>
      <railway_guide>streamlit_dashboard/RAILWAY_DEPLOYMENT_GUIDE.md</railway_guide>
      <dashboard_plan>STREAMLIT_DASHBOARD_PLAN.md</dashboard_plan>
      <agent_coordination>streamlit_dashboard/agent_comms/agent-coordination-tracker.json</agent_coordination>
    </deployment_documentation>
  </project_structure>
  
  <deployment_info>
    <last_deployment>2025-07-17</last_deployment>
    <deployment_commit>1bf59bb</deployment_commit>
    <deployment_status>Production Ready - Framework finalization complete</deployment_status>
    <branch_status>framework-simplification-v3 pushed successfully</branch_status>
  </deployment_info>
  
  <usage_urls>
    <issues>https://github.com/swm-sink/claude-code-modular-prompts/issues</issues>
    <pull_requests>https://github.com/swm-sink/claude-code-modular-prompts/pulls</pull_requests>
    <releases>https://github.com/swm-sink/claude-code-modular-prompts/releases</releases>
    <documentation>https://github.com/swm-sink/claude-code-modular-prompts/blob/main/README.md</documentation>
    <getting_started>https://github.com/swm-sink/claude-code-modular-prompts/blob/main/GETTING_STARTED.md</getting_started>
  </usage_urls>
  
  <quick_setup>
    <clone_command>git clone https://github.com/swm-sink/claude-code-modular-prompts.git</clone_command>
    <copy_framework>cp -r claude-code-modular-prompts/.claude your-project/ && cp claude-code-modular-prompts/CLAUDE.md your-project/ && cp claude-code-modular-prompts/PROJECT_CONFIG.xml your-project/</copy_framework>
    <test_command>/auto "analyze my project structure"</test_command>
  </quick_setup>
  
  <authentication>
    <github_cli>gh auth status</github_cli>
    <active_account>swm-sink</active_account>
    <required_permissions>repo, workflow, gist</required_permissions>
  </authentication>
</repository_config>
```

**Framework Status**: This repository contains a fully implemented modular prompt engineering framework with comprehensive `.claude/` architecture, advanced meta-prompting capabilities, and Claude 4 optimization.

**What's Included**:
- Complete `.claude/` modular framework with 64 specialized modules
- PROJECT_CONFIG.xml configuration system with dynamic templates
- Meta-prompting capabilities with self-improvement frameworks
- Comprehensive validation and optimization scripts
- Test infrastructure and performance monitoring
- Quality gates and TDD enforcement implementation

**Framework Architecture**:
- `.claude/modules/` - 64 specialized modules across domains
- `.claude/prompt_eng/` - Advanced prompt engineering patterns
- `.claude/system/` - Quality gates and infrastructure components
- `.claude/meta/` - Self-improving meta-framework capabilities


# 📚 2025 Research & Critical Analysis

**Important**: Comprehensive research has been conducted on this framework against 2025 best practices. The analysis includes 50+ sources covering Claude 4 optimization, meta-prompting, token efficiency, and industry standards.

## Research Documents

### 🔍 [Critical Analysis & Findings](./docs/2025-framework-critical-analysis.md)
- Deep architectural assessment identifying strengths and critical issues
- Comparison against 2025 industry best practices
- Strategic recommendations for framework evolution
- Implementation roadmap with success metrics

### 🚀 [Claude 4 Optimization Guide](./docs/claude-4-optimization-guide.md)
- Revolutionary Claude 4 features (adaptive thinking, persistent memory, parallel execution)
- Migration guide from Claude 3.5 patterns
- Performance benchmarks and cost optimization strategies
- Production-ready implementation patterns

### 🧠 [Meta-Prompting Research](./docs/meta-prompting-research.md)
- Self-improving prompt systems (DSPy, TEXTGRAD, Meta-Conductor)
- Automated optimization frameworks
- Production case studies from Uber, Anthropic, OpenAI
- Future directions in autonomous prompt evolution

### 💰 [Token Optimization Guide](./docs/token-optimization-guide.md)
- 30-60% token reduction techniques
- Context window management strategies
- Caching patterns for 90% cost savings
- Real-time optimization and monitoring

### 📖 [Comprehensive Sources](./docs/2025-prompt-engineering-sources.md)
- 53 authoritative sources with summaries
- Official documentation, academic papers, industry implementations
- Organized by category with usage recommendations

**Key Finding**: While this framework demonstrates sophisticated engineering (94.95% production readiness), research reveals opportunities for 40% token reduction, 60% complexity simplification, and alignment with 2025's context engineering paradigm.


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

# Command Status (Framework Remediation)

```xml
<command_status test_date = "2025-07-19" phase = "remediation" honesty = "RESTORED">
  <status_summary>
    <previous_issue>Phase 3 consolidation created false capability claims</previous_issue>
    <current_state>Documentation aligned with actual capabilities</current_state>
    <trust_status>Rebuilding through transparency</trust_status>
  </status_summary>
  
  <core_commands count = "20">
    <command name = "auto" status = "FULLY_FUNCTIONAL" actual = "Intelligent routing to other commands"/>
    <command name = "task" status = "FULLY_FUNCTIONAL" actual = "TDD single component development"/>
    <command name = "feature" status = "FULLY_FUNCTIONAL" actual = "PRD-driven feature development"/>
    <command name = "protocol" status = "FULLY_FUNCTIONAL" actual = "Production deployment with safety"/>
    <command name = "query" status = "FULLY_FUNCTIONAL" actual = "Read-only code analysis"/>
    <command name = "swarm" status = "FULLY_FUNCTIONAL" actual = "Multi-agent coordination"/>
    <command name = "session" status = "FULLY_FUNCTIONAL" actual = "Long-running context preservation"/>
    <command name = "init" status = "FULLY_FUNCTIONAL" actual = "Basic framework initialization"/>
    <command name = "init-new" status = "FULLY_FUNCTIONAL" actual = "New project setup"/>
    <command name = "init-custom" status = "FULLY_FUNCTIONAL" actual = "Custom configuration"/>
    <command name = "init-research" status = "FULLY_FUNCTIONAL" actual = "Research-focused setup"/>
    <command name = "init-validate" status = "FULLY_FUNCTIONAL" actual = "Framework validation"/>
    <command name = "meta" status = "FULLY_FUNCTIONAL" actual = "Unified meta operations"/>
    <command name = "docs" status = "FULLY_FUNCTIONAL" actual = "Documentation generation"/>
    <command name = "chain" status = "FULLY_FUNCTIONAL" actual = "Workflow orchestration"/>
    <command name = "context-prime" status = "FULLY_FUNCTIONAL" actual = "Project context analysis"/>
  </core_commands>
  
  <remediation_actions>
    <action>Removed false "auto-fix" claims from /task</action>
    <action>Removed false "meta-review" claims from /query</action>
    <action>Removed false "optimization/governance" claims from /protocol</action>
    <action>Restored init command variants for better UX</action>
    <action>Moved critical commands back from utilities</action>
    <action>Created truth audit report in .claude/truth/</action>
  </remediation_actions>
  
  <future_commitment>
    <principle>Documentation matches implementation</principle>
    <principle>No features without code</principle>
    <principle>User experience over metrics</principle>
    <principle>Transparency in all claims</principle>
  </future_commitment>
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
    <modules_found>64</modules_found>
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


# Quick Reference

## Essential Commands

```xml
<command_reference>
  <core_commands>
    <command name="/auto" purpose="Intelligent routing and framework selection">
      <usage>/auto "your request here"</usage>
      <best_for>Unclear requirements | Complex decisions | Route optimization</best_for>
    </command>
    
    <command name="/task" purpose="Single component TDD development">
      <usage>/task "implement specific functionality"</usage>
      <best_for>Single file changes | Bug fixes | <50 lines of code</best_for>
    </command>
    
    <command name="/feature" purpose="Complete feature lifecycle with PRD">
      <usage>/feature "develop new feature with requirements"</usage>
      <best_for>New features | Multi-component changes | System integration</best_for>
    </command>
    
    <command name="/query" purpose="Research and analysis">
      <usage>/query "analyze codebase or investigate issue"</usage>
      <best_for>Code research | Understanding systems | Read-only analysis</best_for>
    </command>
    
    <command name="/swarm" purpose="Multi-agent coordination for complex tasks">
      <usage>/swarm "coordinate multiple development tasks"</usage>
      <best_for>Complex projects | Parallel development | Team coordination</best_for>
    </command>
    
    <command name="/session" purpose="Long-running work with context preservation">
      <usage>/session "manage extended development session"</usage>
      <best_for>Extended work | Context preservation | Progress tracking</best_for>
    </command>
    
    <command name="/protocol" purpose="Production deployment with safety">
      <usage>/protocol "production deployment or critical changes"</usage>
      <best_for>Production deployments | Critical fixes | Safety validation</best_for>
    </command>
    
    <command name="/init" purpose="Framework initialization">
      <usage>/init "description"</usage>
      <best_for>Basic framework setup and configuration</best_for>
      <related>Use init-new, init-custom, init-research, or init-validate for specific needs</related>
    </command>
    
    <command name="/init-new" purpose="New project setup">
      <usage>/init-new "create new project with framework"</usage>
      <best_for>Starting fresh projects | Interactive setup | Full scaffolding</best_for>
    </command>
    
    <command name="/init-custom" purpose="Custom project configuration">
      <usage>/init-custom "configure for existing project"</usage>
      <best_for>Existing codebases | Custom requirements | Complex setups</best_for>
    </command>
    
    <command name="/init-research" purpose="Research project setup">
      <usage>/init-research "setup for code analysis"</usage>
      <best_for>Code analysis | Research workflows | Read-only exploration</best_for>
    </command>
    
    <command name="/init-validate" purpose="Framework validation">
      <usage>/init-validate "verify framework integrity"</usage>
      <best_for>Health checks | Configuration validation | Troubleshooting</best_for>
    </command>
    
    <command name="/meta" purpose="Unified meta-framework operations">
      <usage>/meta [operation] "target"</usage>
      <operations>review | optimize | evolve | govern | fix</operations>
      <best_for>Framework analysis | Performance tuning | Compliance | Evolution</best_for>
    </command>
    
    <command name="/docs" purpose="Documentation generation and management">
      <usage>/docs "generate or update documentation"</usage>
      <best_for>Documentation | README files | API docs | User guides</best_for>
    </command>
    
    <command name="/chain" purpose="Advanced workflow orchestration">
      <usage>/chain "execute multi-command workflows"</usage>
      <best_for>Complex workflows | Sequential operations | Conditional routing</best_for>
    </command>
    
    <command name="/context-prime" purpose="Project context establishment">
      <usage>/context-prime "establish project context"</usage>
      <best_for>Project initialization | Context analysis | Environment setup</best_for>
    </command>
  </core_commands>
</command_reference>
```

## Configuration Quick Start

```xml
<configuration_reference>
  <essential_setup>
    <file name="CLAUDE.md">Must be in project root directory</file>
    <file name="PROJECT_CONFIG.xml">Project-specific configuration template</file>
    <directory name=".claude/">Framework modules and components</directory>
  </essential_setup>
  
  <project_config_essentials>
    <tech_stack>
      <primary_language>python | javascript | typescript | go | rust | java</primary_language>
      <framework>django | react | nextjs | gin | fastapi | spring</framework>
      <database>postgresql | mysql | mongodb | redis</database>
    </tech_stack>
    
    <commands>
      <test>pytest --cov=src | npm test | go test</test>
      <lint>flake8 | eslint | golangci-lint</lint>
      <build>python setup.py | npm run build | go build</build>
    </commands>
    
    <quality_standards>
      <test_coverage>
        <threshold>90</threshold>
        <enforcement>blocking</enforcement>
      </test_coverage>
      <performance>
        <response_time_p95>200</response_time_p95>
      </performance>
    </quality_standards>
  </project_config_essentials>
</configuration_reference>
```

## Common Workflows

```xml
<workflow_reference>
  <workflow name="New Feature Development">
    <steps>
      <step>1. /query "understand existing related functionality"</step>
      <step>2. /feature "implement new feature with requirements"</step>
      <step>3. /task "add specific components or fixes"</step>
      <step>4. /protocol "prepare for production deployment"</step>
    </steps>
  </workflow>
  
  <workflow name="Bug Investigation and Fix">
    <steps>
      <step>1. /query "analyze bug and understand root cause"</step>
      <step>2. /task "implement fix with comprehensive tests"</step>
      <step>3. /protocol "ensure fix meets production standards"</step>
    </steps>
  </workflow>
  
  <workflow name="Code Research and Documentation">
    <steps>
      <step>1. /query "analyze codebase and create documentation"</step>
      <step>2. /docs "generate comprehensive documentation"</step>
      <step>3. /task "add missing tests or improve coverage"</step>
    </steps>
  </workflow>
  
  <workflow name="Performance Optimization">
    <steps>
      <step>1. /meta-review "analyze current performance"</step>
      <step>2. /meta-optimize "implement optimizations"</step>
      <step>3. /task "apply specific performance improvements"</step>
      <step>4. /meta-evolve "learn from optimization patterns"</step>
    </steps>
  </workflow>
</workflow_reference>
```

## Troubleshooting Quick Fixes

```xml
<troubleshooting_reference>
  <issue name="Commands not working">
    <symptoms>Generic responses | Commands not recognized | No framework behavior</symptoms>
    <solutions>
      <solution>Check CLAUDE.md is in project root directory</solution>
      <solution>Verify .claude/ directory exists with modules</solution>
      <solution>Ensure PROJECT_CONFIG.xml is properly configured</solution>
    </solutions>
  </issue>
  
  <issue name="Quality gates not enforcing">
    <symptoms>No TDD enforcement | Coverage ignored | Tests skipped</symptoms>
    <solutions>
      <solution>Check quality_standards in PROJECT_CONFIG.xml</solution>
      <solution>Verify enforcement is set to "blocking"</solution>
      <solution>Ensure test commands are properly configured</solution>
    </solutions>
  </issue>
  
  <issue name="Poor performance">
    <symptoms>Slow responses | High token usage | Context timeouts</symptoms>
    <solutions>
      <solution>Run /meta-review to analyze performance</solution>
      <solution>Use /meta-optimize for automated improvements</solution>
      <solution>Check context_management settings in PROJECT_CONFIG.xml</solution>
    </solutions>
  </issue>
  
  <issue name="Generic AI responses">
    <symptoms>Not following framework patterns | Missing domain expertise</symptoms>
    <solutions>
      <solution>Customize PROJECT_CONFIG.xml for your tech stack</solution>
      <solution>Verify configuration is project-specific</solution>
      <solution>Use /meta-evolve to adapt to your patterns</solution>
    </solutions>
  </issue>
</troubleshooting_reference>
```

## Setup Checklist

```xml
<setup_checklist>
  <prerequisites>
    <item>✓ Claude Code CLI installed and authenticated</item>
    <item>✓ Project directory with existing codebase</item>
    <item>✓ Git repository initialized</item>
    <item>✓ Development environment configured</item>
  </prerequisites>
  
  <framework_setup>
    <item>✓ Copy CLAUDE.md to project root</item>
    <item>✓ Copy PROJECT_CONFIG.xml to project root</item>
    <item>✓ Create .claude/ directory structure</item>
    <item>✓ Customize PROJECT_CONFIG.xml for your stack</item>
  </framework_setup>
  
  <validation>
    <item>✓ Run /auto "test framework setup" to verify</item>
    <item>✓ Try /task "simple test task" to confirm TDD</item>
    <item>✓ Check /meta-review for any issues</item>
    <item>✓ Verify quality gates are enforcing</item>
  </validation>
  
  <optimization>
    <item>✓ Run /meta-optimize after first week of usage</item>
    <item>✓ Use /meta-evolve to adapt to team patterns</item>
    <item>✓ Regular /meta-review for performance monitoring</item>
    <item>✓ Update PROJECT_CONFIG.xml as project evolves</item>
  </optimization>
</setup_checklist>
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
    <module>modules/patterns/</module>
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
  <purpose>Comprehensive Claude 4 optimization with advanced reasoning, prompt construction, and execution transparency</purpose>
  
  <core_capabilities>
    <interleaved_thinking enforcement = "MANDATORY">
      <config>16K thinking length | Trigger: tool calls, uncertainty, complexity</config>
      <rules>ALWAYS think before act | 5X think:act ratio | "ultrathink" = extended</rules>
      <critical_thinking>30-second minimum analysis with consequence mapping</critical_thinking>
    </interleaved_thinking>
    
    <parallel_execution enforcement = "MANDATORY">
      <principle>All independent operations execute simultaneously</principle>
      <patterns>Batch tool calls | Parallel analysis | Concurrent validation</patterns>
      <performance>Claude 4 optimized with parallel execution and thinking patterns</performance>
      <tool_optimization>Intelligent batching | Cascaded memory 5 hops | Token efficiency</tool_optimization>
    </parallel_execution>
    
    <context_optimization enforcement = "MANDATORY">
      <management>Hierarchical loading | XML structured | Dynamic context</management>
      <limits>[PROJECT_CONFIG: max_file_tokens | DEFAULT: 4K] tokens/file | [PROJECT_CONFIG: max_context_tokens | DEFAULT: 120K] total | [PROJECT_CONFIG: reserved_work_tokens | DEFAULT: 50K+] reserved for work</limits>
      <structure>XML structure 4 levels | 200K context window | Token budget tracking</structure>
    </context_optimization>
  </core_capabilities>
  
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
  
  <prompt_construction_methodology>
    <execution_model>
      <step order = "1">Parse command structure and extract thinking pattern checkpoints</step>
      <step order = "2">Load required modules and validate interface contracts</step>
      <step order = "3">Construct execution workflow with dependency resolution</step>
      <step order = "4">Optimize context window usage through parallel execution</step>
      <step order = "5">Execute with real-time progress tracking and error handling</step>
    </execution_model>
    
    <transparency_features>
      <workflow_preview>Visual representation of execution flow before starting</workflow_preview>
      <progress_indicators>Real-time checkpoint completion with time estimates</progress_indicators>
      <context_visualization>Token usage tracking with optimization suggestions</context_visualization>
      <debug_information>Module state and decision reasoning visibility</debug_information>
    </transparency_features>
    
    <lego_block_assembly>
      <command_role>Blueprint that selects and orders execution blocks with clear dependency chains</command_role>
      <module_role>Self-contained execution units with standardized interfaces and predictable outputs</module_role>
      <runtime_role>Assembly engine that constructs final prompt with optimization and validation</runtime_role>
      <integration_role>Composition coordinator that manages module interactions and state transitions</integration_role>
    </lego_block_assembly>
  </prompt_construction_methodology>
  
  <behavioral_control>
    <thinking>Use thinking blocks, 3x think:act ratio minimum</thinking>
    <efficiency>Parallel tool calls MANDATORY across all operations</efficiency>
    <precision>NO assumptions - verify everything before execution</precision>
    <orchestration>Delegate to appropriate commands and modules per framework architecture</orchestration>
    <frameworks>RISE/TRACE/CARE (foundational) | APE/CLEAR/SOAR/CRISP/SPARK (specialized)</frameworks>
  </behavioral_control>
  
  <performance_targets>
    <assembly_time>Prompt construction within 5 seconds for complex workflows</assembly_time>
    <execution_visibility>Real-time progress updates every 10 seconds</execution_visibility>
    <context_efficiency>Significant improvement through optimized tool batching</context_efficiency>
    <error_recovery>Sub-second failure detection with immediate recovery options</error_recovery>
    <session_optimization>40min sessions | Strategic /compact | Cost monitoring</session_optimization>
  </performance_targets>
  
  <hallucination_prevention enforcement = "CRITICAL">
    <temperature>Factual: [PROJECT_CONFIG: ai_temperature.factual | DEFAULT: 0.2] | Analysis: [PROJECT_CONFIG: ai_temperature.analysis | DEFAULT: 0.0-0.3] | General: 0.4-0.5 | Creative: [PROJECT_CONFIG: ai_temperature.creative | DEFAULT: 0.7-1.0]</temperature>
    <validation>Sources: 2025 only | Evidence required | "I don't know" when uncertain</validation>
    <accuracy>Ground in evidence | Conservative language | Step-by-step reasoning</accuracy>
    <protocols>Pre-publication review | Immediate correction | Iterative refinement</protocols>
    <quality_enforcement>Evidence validation | Consequence mapping | TDD mandatory</quality_enforcement>
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
  
  <actual_structure location = ".claude/">
    <commands location = "commands/">
      <core>Main commands (auto, task, feature, swarm, query, session, docs, protocol)</core>
      <meta>Meta-framework commands (meta-review, meta-evolve, meta-optimize, meta-govern, meta-fix)</meta>
      <setup>Setup and initialization commands (init, context-prime, chain)</setup>
    </commands>
    <modules location = "modules/">
      <patterns>Advanced patterns - thinking, composition, routing, orchestration</patterns>
      <development>Development support modules</development>
      <meta>Meta-framework modules</meta>
    </modules>
    <system location = "system/">
      <quality>Quality gates, TDD enforcement, testing frameworks</quality>
      <security>Security modules, threat modeling, compliance</security>
      <context>Context management, preservation, artifacts, templates</context>
      <session>Session management, compression, reliability</session>
      <git>Git operations, conventional commits, worktree isolation</git>
    </system>
    <prompt_eng location = "prompt_eng/">
      <frameworks>Prompt engineering frameworks</frameworks>
    </prompt_eng>
    <domain location = "domain/">
      <templates>Domain-specific templates</templates>
      <wizard>Domain wizard, guides, initialization</wizard>
    </domain>
    <meta location = "meta/">
      <meta_prompting>Meta-prompting orchestration</meta_prompting>
    </meta>
    <sessions location = "sessions/">
      <session_data>Session data and artifacts</session_data>
    </sessions>
    <templates location = "templates/">
      <framework_templates>Framework templates</framework_templates>
    </templates>
  </actual_structure>
  
  <enforcement_rules priority = "CRITICAL">
    <rule>Commands MUST be in commands/ directory</rule>
    <rule>Modules MUST be in modules/ with patterns, development, meta subdirectories</rule>
    <rule>System components MUST be in system/ directory</rule>
    <rule>Domain templates MUST be in domain/ directory</rule>
    <rule>Strict separation between different component types</rule>
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
    <cmd name = "/auto" module = "modules/patterns/intelligent-routing.md"/>
    <cmd name = "/task" module = "modules/patterns/tdd-cycle-pattern.md"/>
    <cmd name = "/feature" module = "modules/patterns/workflow-orchestration-engine.md"/>
    <cmd name = "/swarm" module = "modules/patterns/multi-agent.md"/>
    <cmd name = "/query" module = "modules/patterns/research-analysis-pattern.md"/>
    <cmd name = "/session" module = "modules/patterns/session-management-pattern.md"/>
    <cmd name = "/protocol" module = "modules/patterns/workflow-orchestration-engine.md"/>
    <cmd name = "/init" module = "domain/wizard/README.md"/>
    <cmd name = "/init-new" module = "modules/development/"/>
    <cmd name = "/init-custom" module = "domain/wizard/"/>
    <cmd name = "/init-research" module = "modules/patterns/research-analysis-pattern.md"/>
    <cmd name = "/init-validate" module = "system/quality/comprehensive-validation.md"/>
    <cmd name = "/meta" module = "modules/meta/"/>
    <cmd name = "/docs" module = "modules/patterns/documentation-pattern.md" critical = "true"/>
    <cmd name = "/chain" module = "modules/patterns/command-chaining-architecture.md" critical = "true"/>
    <cmd name = "/context-prime" module = "system/context/project-priming.md"/>
  </commands>
  <documentation_enforcement>
    <rule priority = "CRITICAL">NEVER generate project documentation without /docs command</rule>
    <rule priority = "CRITICAL">All documentation MUST go through /docs for consistency</rule>
    <rule priority = "CRITICAL">README, guides, docs ONLY via /docs command</rule>
    <exception>CLAUDE.md updates and command documentation are allowed</exception>
  </documentation_enforcement>
  <modules location = ".claude/modules/" implement_only = "true">
    <category name = "patterns|development|meta"/>
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
  <canonical_source>.claude/modules/patterns/</canonical_source>
</aware_process>
```


# Quality Gates

```xml
<quality_gates version = "3.0.0" enforcement = "CRITICAL">
  <purpose>Universal quality enforcement across all commands and modules with comprehensive validation and blocking controls</purpose>
  
  <master_mandate>ALL commands MUST validate through quality gates with BLOCKING enforcement</master_mandate>
  
  <critical_gates>
    <gate name = "TDD_Compliance">
      <cycle>RED→GREEN→REFACTOR mandatory cycle enforcement</cycle>
      <universal_requirement>Write failing tests FIRST, implement minimal code, refactor while keeping tests green</universal_requirement>
      <blocking_enforcement>ANY implementation before tests BLOCKS command execution</blocking_enforcement>
      <atomic_integration>Atomic commits at each TDD phase with validation checkpoints</atomic_integration>
    </gate>
    <gate name = "Security_Standards">Threat model first | Zero high-severity issues</gate>
    <gate name = "Performance_Benchmarks">[PROJECT_CONFIG: performance.response_time_p95 | DEFAULT: 200ms] p95 required</gate>
    <gate name = "Code_Quality">[PROJECT_CONFIG: test_coverage.threshold | DEFAULT: 90]%+ coverage with assertions</gate>
    <gate name = "Features_Approach">PRD-first development approach mandatory</gate>
  </critical_gates>
  
  <canonical_sources>
    <tdd>.claude/modules/patterns/tdd-cycle-pattern.md</tdd>
    <security>.claude/system/security/</security>
    <test_coverage>.claude/system/quality/test-coverage.md</test_coverage>
    <universal_gates>.claude/system/quality/universal-quality-gates.md</universal_gates>
  </canonical_sources>
  
  <orchestration>
    <delegation>Commands delegate to quality modules for detailed validation and enforcement procedures</delegation>
    <integration>Quality gates enforced at both command and module levels</integration>
    <validation>Each quality gate execution gets atomic commit with validation</validation>
  </orchestration>
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
<github_workflow trigger = ">10 steps" repository = "swm-sink/claude-code-modular-prompts">
  <repository_info>
    <url>https://github.com/swm-sink/claude-code-modular-prompts</url>
    <issues_url>https://github.com/swm-sink/claude-code-modular-prompts/issues</issues_url>
    <cli_command>gh issue create --repo swm-sink/claude-code-modular-prompts</cli_command>
    <authentication>Use GitHub CLI with swm-sink account</authentication>
  </repository_info>
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
  <commands>
    <create_issue>gh issue create --title "Epic: [title]" --body "[description]" --repo swm-sink/claude-code-modular-prompts</create_issue>
    <update_issue>gh issue comment [issue_number] --body "[update]" --repo swm-sink/claude-code-modular-prompts</update_issue>
    <close_issue>gh issue close [issue_number] --comment "[completion_summary]" --repo swm-sink/claude-code-modular-prompts</close_issue>
  </commands>
</github_workflow>
```


# Agent Coordination Protocol

```xml
<agent_coordination_protocol version = "1.0.0" enforcement = "CRITICAL">
  <purpose>Structured coordination for parallel agent execution with comprehensive tracking and quality enforcement</purpose>
  
  <communication_requirements enforcement = "MANDATORY">
    <agent_comms_location>agent_comms/ - ALL agent communications MUST go in this root directory</agent_comms_location>
    <coordination_tracking>agent_comms/agent-coordination-tracker.json - Simple JSON tracker for all agent coordination</coordination_tracking>
    <output_consolidation>framework-transformation/batch{N}-results/ - Organized results per batch</output_consolidation>
    <atomic_documentation>Each agent produces comprehensive deliverable documentation</atomic_documentation>
  </communication_requirements>
  
  <coordination_structure enforcement = "MANDATORY">
    <batch_execution>Maximum 4 agents per batch for optimal parallel performance</batch_execution>
    <agent_tracking>Real-time status updates in coordination tracker JSON</agent_tracking>
    <quality_gates>All agents must pass TDD and quality validation before completion</quality_gates>
    <interruption_handling>Resume from last checkpoint with full state preservation</interruption_handling>
    <atomic_commits>Per agent completion with rollback capability</atomic_commits>
  </coordination_structure>
  
  <brutal_quality_standards enforcement = "CRITICAL" version = "2.0.0">
    <purpose>ELIMINATE VAGUE BULLSHIT - DEMAND ACTIONABLE PROMPT ENGINEERING</purpose>
    
    <prompt_engineering_deliverable_requirements enforcement = "BLOCKING">
      <working_prompts>ALL agents MUST deliver FUNCTIONAL .md prompts that can be immediately used</working_prompts>
      <tested_prompt_patterns>Every deliverable MUST include tested prompt patterns with demonstrated results</tested_prompt_patterns>
      <measurable_improvements>ALL performance claims MUST be backed by ACTUAL before/after prompt effectiveness</measurable_improvements>
      <usable_modules>Agents deliver FUNCTIONAL prompt modules, not theoretical frameworks</usable_modules>
      <validation_evidence>ALL claims MUST be supported by prompt testing and effectiveness validation</validation_evidence>
    </prompt_engineering_deliverable_requirements>
    
    <prohibited_bullshit enforcement = "BLOCKING">
      <vague_concepts>BANNED: Abstract frameworks without concrete prompt implementations</vague_concepts>
      <unvalidated_claims>BANNED: Prompt improvements without testing evidence</unvalidated_claims>
      <future_implementations>BANNED: "Will create prompts" - deliver WORKING prompts NOW</future_implementations>
      <aspirational_metrics>BANNED: "Target 90% improvement" - show ACTUAL prompt testing results</aspirational_metrics>
      <theoretical_patterns>BANNED: Prompt patterns without working examples and test results</theoretical_patterns>
    </prohibited_bullshit>
    
    <prompt_quality_validation_gates enforcement = "BLOCKING">
      <prompt_execution>Every deliverable prompt MUST be tested and produce expected outputs</prompt_execution>
      <effectiveness_measurement>All optimization claims MUST be backed by before/after prompt performance</effectiveness_measurement>
      <integration_testing>All prompt modules MUST integrate successfully with existing framework</integration_testing>
      <user_effectiveness>All UX improvements MUST be validated with actual prompt usage testing</user_effectiveness>
      <production_readiness>All deliverables MUST be ready for immediate framework deployment</production_readiness>
    </prompt_quality_validation_gates>
    
    <agent_failure_criteria enforcement = "IMMEDIATE">
      <theory_without_prompts>Agent fails if deliverables are concepts without working prompt implementations</theory_without_prompts>
      <untested_prompts>Agent fails if prompts cannot be validated and tested</untested_prompts>
      <unsubstantiated_claims>Agent fails if prompt effectiveness claims lack testing evidence</unsubstantiated_claims>
      <incomplete_implementation>Agent fails if prompt modules are partial or require "future work"</incomplete_implementation>
      <missing_validation>Agent fails if prompt testing and validation results are not provided</missing_validation>
    </agent_failure_criteria>
    
    <acceptable_prompt_standards enforcement = "MANDATORY">
      <functional_prompts>Working .md files that can be immediately used in the framework</functional_prompts>
      <comprehensive_testing>Prompt testing with clear before/after results and effectiveness metrics</comprehensive_testing>
      <performance_benchmarks>Before/after measurements proving prompt optimization claims</performance_benchmarks>
      <integration_examples>Working examples showing prompt integration with existing framework</integration_examples>
      <deployment_instructions>Clear, tested instructions for implementing prompts in production</deployment_instructions>
    </acceptable_prompt_standards>
    
    <enforcement_protocol enforcement = "IMMEDIATE">
      <agent_review>Every agent deliverable undergoes brutal quality review for prompt effectiveness</agent_review>
      <prompt_testing>All prompts must be tested and validated in controlled environment</prompt_testing>
      <claim_validation>All prompt effectiveness and improvement claims must be empirically verified</claim_validation>
      <rejection_criteria>Agents delivering theoretical prompt concepts are immediately rejected and restarted</rejection_criteria>
      <standards_escalation>Prompt quality standards increase with each batch - no regression tolerance</standards_escalation>
    </enforcement_protocol>
  </brutal_quality_standards>
  
  <tracker_schema enforcement = "MANDATORY">
    <coordination_meta>Session metadata, version, batch planning</coordination_meta>
    <active_batch>Current batch status, agent progress, deliverables tracking</active_batch>
    <batch_queue>Planned batch execution with missions and status</batch_queue>
    <epic_progress>High-level progress tracking across all epics</epic_progress>
    <coordination_rules>Enforcement rules and execution protocols</coordination_rules>
  </tracker_schema>
  
  <execution_workflow enforcement = "MANDATORY">
    <pre_batch>Update tracker with batch initialization and agent assignments</pre_batch>
    <during_execution>Real-time status updates as agents complete tasks</during_execution>
    <post_completion>Consolidate results, validate quality, commit atomically</post_completion>
    <between_batches>Compile results, update epic progress, prepare next batch</between_batches>
  </execution_workflow>
  
  <integration_with_existing_framework enforcement = "MANDATORY">
    <file_discipline>Agent communications respect file organization rules</file_discipline>
    <quality_gates>Agent coordination must pass universal quality gates</quality_gates>
    <atomic_commits>Integration with existing atomic rollback protocol</atomic_commits>
    <tdd_enforcement>All agent outputs subject to TDD validation</tdd_enforcement>
    <github_workflow>Large multi-agent operations create GitHub issues for tracking</github_workflow>
  </integration_with_existing_framework>
  
  <parallel_optimization enforcement = "MANDATORY">
    <task_batching>Use Task() calls for parallel agent execution</task_batching>
    <resource_allocation>Balanced workload distribution across agents</resource_allocation>
    <coordination_efficiency>Minimal overhead coordination protocol</coordination_efficiency>
    <quality_preservation>Parallel execution maintains quality standards</quality_preservation>
  </parallel_optimization>
</agent_coordination_protocol>
```


# Atomic Commits & Instant Rollback Protocol

```xml
<atomic_rollback_reference enforcement = "CRITICAL">
  <purpose>Zero data loss with instant recovery for all framework operations</purpose>
  <canonical_source>@.claude/system/git/atomic-rollback-protocol.md</canonical_source>
  <core_guarantees>
    <zero_data_loss>All changes reversible within seconds with complete operation history</zero_data_loss>
    <performance_targets>Commit <1s, Rollback <2s, Validation <5s, Recovery <10s</performance_targets>
    <framework_integration>Embedded into ALL framework processes and commands</framework_integration>
  </core_guarantees>
  <quick_reference>
    <immediate_rollback>git reset --hard HEAD~1</immediate_rollback>
    <emergency_rollback>git stash && git reset --hard [safe_state_commit]</emergency_rollback>
    <branch_abort>git checkout main && git branch -D [working_branch]</branch_abort>
  </quick_reference>
</atomic_rollback_reference>
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
<module_runtime_reference enforcement = "CRITICAL">
  <purpose>Deterministic module composition and execution engine for Claude 4</purpose>
  <canonical_source>@.claude/modules/patterns/module-runtime-engine.md</canonical_source>
  <core_features>
    <runtime_architecture>Checkpoint patterns | TDD mandatory | Validation gates</runtime_architecture>
    <command_specifications>Task | Swarm | Auto | Query | Session | Protocol | Docs</command_specifications>
    <performance_targets>Commands: <2min | Loading: <10s | Gates: <30s</performance_targets>
  </core_features>
  <integration_dependencies>
    <thinking_patterns>@.claude/modules/patterns/thinking-pattern-template.md</thinking_patterns>
    <composition_framework>@.claude/modules/patterns/module-composition-framework.md</composition_framework>
    <quality_gates>@.claude/system/quality/universal-quality-gates.md</quality_gates>
    <tdd_enforcement>@.claude/modules/patterns/tdd-cycle-pattern.md</tdd_enforcement>
  </integration_dependencies>
</module_runtime_reference>
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


# Meta-Framework Control

```xml
<meta_framework_reference enforcement = "CRITICAL">
  <purpose>Unified meta-framework operations with intelligent routing and safety boundaries</purpose>
  <unified_command>@.claude/commands/meta.md</unified_command>
  <framework_control>@.claude/meta/meta-framework-control.md</framework_control>
  
  <operations>
    <review>/meta review "audit framework compliance"</review>
    <optimize>/meta optimize "improve performance and efficiency"</optimize>
    <evolve>/meta evolve "adapt framework to new patterns"</evolve>
    <govern>/meta govern "enforce quality and compliance standards"</govern>
    <fix>/meta fix "diagnose and correct compliance issues"</fix>
  </operations>
  
  <safety_framework>
    <boundaries>5% weekly limit | Human approval | 60s rollback | 99.9% stability</boundaries>
    <oversight>Ultimate human authority | Emergency override | Full transparency</oversight>
    <capabilities>Framework evolution | Compliance enforcement | Performance optimization</capabilities>
  </safety_framework>
  
  <integration_points>
    <meta_modules>@.claude/modules/meta/</meta_modules>
    <quality_gates>@.claude/system/quality/universal-quality-gates.md</quality_gates>
    <atomic_rollback>@.claude/system/git/atomic-rollback-protocol.md</atomic_rollback>
    <module_runtime>@.claude/modules/patterns/module-runtime-engine.md</module_runtime>
  </integration_points>
</meta_framework_reference>
```


# Intelligent Framework Control

```xml
<intelligent_framework_control version = "4.0" enforcement = "ACTIVE">
  <purpose>Active intelligence layer preventing framework degradation through validation and monitoring</purpose>
  
  <state_awareness>
    <current_state>@.claude/state/current-system-state.json</current_state>
    <change_history>@.claude/state/change-history.log</change_history>
    <health_monitor>@.claude/monitors/system-health-monitor.md</health_monitor>
  </state_awareness>
  
  <change_protection enforcement = "BLOCKING">
    <before_any_change>
      <must_run>@.claude/guards/change-impact-analyzer.md</must_run>
      <must_pass>@.claude/truth/claim-validator.md</must_pass>
      <must_verify>All functionality preserved</must_verify>
    </before_any_change>
    
    <blocking_conditions>
      <condition>Any functionality loss without superior replacement</condition>
      <condition>Any false capability claims in documentation</condition>
      <condition>User experience degradation for <20% token benefit</condition>
      <condition>Introduction of unimplemented features</condition>
    </blocking_conditions>
  </change_protection>
  
  <truth_enforcement enforcement = "CRITICAL">
    <no_features_without_code>Every claimed feature must have implementation</no_features_without_code>
    <no_enhancements_without_proof>Every enhancement must show measurable improvement</no_enhancements_without_proof>
    <no_optimization_without_metrics>Every optimization must have benchmarks</no_optimization_without_metrics>
    <user_experience_over_tokens>Never sacrifice UX for minor token savings</user_experience_over_tokens>
  </truth_enforcement>
  
  <continuous_monitoring>
    <health_checks>@.claude/monitors/system-health-monitor.md</health_checks>
    <truth_audits>@.claude/truth/claim-validator.md</truth_audits>
    <change_tracking>@.claude/state/change-history.log</change_tracking>
    <alert_thresholds>
      <critical>Health score < 60 | Any false claims</critical>
      <warning>Health score < 70 | Token usage > 150K</warning>
    </alert_thresholds>
  </continuous_monitoring>
  
  <remediation_protocol>
    <detect>Continuous validation of all claims</detect>
    <document>Record violations in truth tracking</document>
    <correct>Remove false claims immediately</correct>
    <prevent>Update guards to prevent recurrence</prevent>
    <learn>Document lessons in change history</learn>
  </remediation_protocol>
</intelligent_framework_control>
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