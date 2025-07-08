| version | last_updated | status |
|---------|--------------|--------|
| 2.6.0   | 2025-07-08   | stable |

# CLAUDE.md - Framework Control Document

────────────────────────────────────────────────────────────────────────────────

<purpose>Personal Claude Code workflow efficiency tool - NOT enterprise software</purpose>

## Core Framework

```xml
<framework version="2.6.0">
  <purpose>Personal Claude Code workflow efficiency tool - NOT enterprise software</purpose>
  <principles>Single source truth | Zero redundancy | Modular composition | Token optimized | Module runtime engine | Prompt construction visualization | Claude 4 optimization</principles>
  <claude_4_features>Interleaved thinking | Parallel execution | 200K context window (Claude 4 Opus/Sonnet verified) | Advanced reasoning | Extended thinking capabilities</claude_4_features>
  <official_sources>
    <anthropic_models>https://docs.anthropic.com/en/docs/about-claude/models/overview</anthropic_models>
    <claude_code_best_practices>https://www.anthropic.com/engineering/claude-code-best-practices</claude_code_best_practices>
    <hallucination_reduction>https://docs.anthropic.com/en/docs/test-and-evaluate/strengthen-guardrails/reduce-hallucinations</hallucination_reduction>
    <swe_bench_results>Claude 4 Opus: 72.5% → 79.4% parallel | Claude 4 Sonnet: 72.7% → 80.2% parallel</swe_bench_results>
  </official_sources>
</framework>
```

────────────────────────────────────────────────────────────────────────────────

## Critical Thinking Rules

```xml
<critical_thinking>
  <rule>Challenge assumptions, surface complexities, disagree constructively</rule>
  <rule>Research first, evidence-based, cross-reference, think 3x before acting - use 2025 sources only</rule>
  <rule>Map consequences: If X → Y → Z</rule>
</critical_thinking>
```

────────────────────────────────────────────────────────────────────────────────

## Code Minimalism

```xml
<code_minimalism>
  <rule>Minimum code that works correctly. Every line must justify existence</rule>
  <rule>No premature abstraction. Delete before adding. Inline simple logic</rule>
  <avoid>Verbose implementations | Unnecessary wrappers | Hypothetical edge cases</avoid>
</code_minimalism>
```

────────────────────────────────────────────────────────────────────────────────

## File Discipline

```xml
<file_discipline>
  <critical_rules enforcement="MAXIMUM">
    <rule priority="HIGHEST">NEVER create files/directories without explicit requirement</rule>
    <rule priority="HIGHEST">ALWAYS use LS/Glob to verify location EXISTS before ANY file operation</rule>
    <rule priority="HIGHEST">THINK 5X before creating ANY new file - check if it already exists</rule>
    <rule priority="HIGHEST">NO test files, personal dirs, or redundant structures EVER</rule>
    <rule priority="HIGHEST">Scripts go in /scripts, tests in /tests, docs in /docs - NO EXCEPTIONS</rule>
  </critical_rules>
  <duplication_prevention enforcement="MANDATORY">
    <rule priority="CRITICAL">Run duplication scan BEFORE any file creation</rule>
    <rule priority="CRITICAL">Display scan results showing similar existing files</rule>
    <rule priority="CRITICAL">Prefer enhancing existing files over creating new ones</rule>
    <rule priority="CRITICAL">Document duplication decision in registry</rule>
    <module>patterns/duplication-prevention.md</module>
  </duplication_prevention>
  <verification_checklist mandatory="true">
    <before_create>Does this file/directory already exist somewhere?</before_create>
    <before_create>Is there an existing location where this belongs?</before_create>
    <before_create>Have I checked with LS/Glob to verify the path?</before_create>
    <before_create>Is this ABSOLUTELY necessary for the user's request?</before_create>
    <before_create>Am I creating clutter or organizing properly?</before_create>
    <before_create>Have I run the duplication prevention scan?</before_create>
    <before_create>Can I enhance existing code instead of creating new?</before_create>
  </verification_checklist>
  <standard_rules>
    <rule>Docs in /docs only. One location per file. Clear naming</rule>
    <rule>Timestamps: filename-YYYY-MM-DD-HHMMSS-UTC</rule>
    <rule>Temporal Standards: All dates MUST use system-generated current dates $(date '+%Y-%m-%d') in UTC format</rule>
    <rule>Version Table Format: | version | last_updated | status | with YYYY-MM-DD format</rule>
    <rule>Compliance: Use $(date '+%Y-%m-%d') for current date, increment manually for sequencing when needed</rule>
    <rule>CRITICAL: Current date is July 2025 - ALL research MUST use 2025 sources and context</rule>
    <rule>Update existing files before creating. Archive don't delete</rule>
  </standard_rules>
  <limits patterns="8" quality="5" planning="5" development="4" security="3" testing="2" reports="5" docs_per_dir="20"/>
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

────────────────────────────────────────────────────────────────────────────────

## Claude 4 Advanced Control

```xml
<claude_4_advanced_control version="2.6.0" enforcement="CRITICAL">
  <interleaved_thinking enforcement="MANDATORY">
    <purpose>Leverage Claude 4's revolutionary thinking capabilities for complex reasoning</purpose>
    <configuration>
      <thinking_mode>interleaved</thinking_mode>
      <max_thinking_length>16000</max_thinking_length>
      <trigger_conditions>After tool calls, when uncertain, for complex multi-step tasks</trigger_conditions>
    </configuration>
    <mandatory_usage>
      <rule priority="CRITICAL">ALWAYS use &lt;antml:thinking&gt; blocks before EVERY action</rule>
      <rule priority="CRITICAL">Think 5X longer than acting - NO EXCEPTIONS</rule>
      <rule priority="CRITICAL">Use thinking blocks at every major decision point</rule>
      <rule priority="CRITICAL">Activate extended reasoning for "ultrathink" requests</rule>
    </mandatory_usage>
  </interleaved_thinking>
  
  <parallel_execution_mastery enforcement="MANDATORY">
    <purpose>Significant performance improvement through optimized tool orchestration based on SWE-bench verified results</purpose>
    <core_principle>All independent operations MUST execute simultaneously</core_principle>
    <mandatory_patterns>
      <pattern>Batch tool calls: Read("f1"), Read("f2"), Read("f3") in single message</pattern>
      <pattern>Parallel analysis: Multiple code sections analyzed concurrently</pattern>
      <pattern>Concurrent validation: Run multiple quality checks simultaneously</pattern>
    </mandatory_patterns>
    <performance_targets>
      <target>SWE-bench verified: Claude 4 Opus 72.5% → 79.4% with parallel compute (6.9% improvement)</target>
      <target>SWE-bench verified: Claude 4 Sonnet 72.7% → 80.2% with parallel compute (7.5% improvement)</target>
      <target>Intelligent batching for independent operations reduces latency</target>
      <target>Context optimization through parallel loading</target>
    </performance_targets>
    <official_source>Anthropic SWE-bench performance data, July 2025</official_source>
  </parallel_execution_mastery>
  
  <context_window_optimization enforcement="MANDATORY">
    <purpose>Maximize efficiency within 200K token capacity</purpose>
    <token_management>
      <hierarchical_context>Critical instructions → Context → Examples → References</hierarchical_context>
      <xml_efficiency>XML tags provide structured reasoning and improved accuracy (Anthropic 2025)</xml_efficiency>
      <dynamic_loading>Load context as needed rather than upfront</dynamic_loading>
    </token_management>
    <performance_targets>
      <framework_limit>Stay within 4000 token limits per file</framework_limit>
      <total_framework>Maintain under 120K tokens for headroom</total_framework>
      <session_efficiency>Reserve 50K+ tokens for active work</session_efficiency>
    </performance_targets>
  </context_window_optimization>
  
  <extended_reasoning_capabilities enforcement="MANDATORY">
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
  
  <hallucination_prevention enforcement="CRITICAL">
    <purpose>Prevent fabricated claims and ensure factual accuracy through systematic validation</purpose>
    <temperature_optimization>
      <factual_content>Use temperature 0.2 for business-critical and factual applications (PerfectApps 2025 recommendation)</factual_content>
      <analytical_tasks>Use temperature 0.0-0.3 for analytical, multiple choice, and verification tasks (Anthropic 2025)</analytical_tasks>
      <general_work>Use temperature 0.4-0.5 for balanced general-purpose tasks (community best practice 2025)</general_work>
      <creative_work>Use temperature 0.7-1.0 only for creative and generative tasks (Anthropic official range)</creative_work>
      <parameter_isolation>NEVER adjust both temperature and top_p simultaneously - focus on temperature only (Anthropic API docs)</parameter_isolation>
    </temperature_optimization>
    <detection_protocols>
      <validation_checkpoints>Validate ALL claims against reliable sources before inclusion</validation_checkpoints>
      <source_verification>Cross-reference multiple authoritative sources for technical claims</source_verification>
      <percentage_claim_blocking>Block ANY percentage improvement claims without verified sources</percentage_claim_blocking>
      <extraordinary_claim_validation>Require extraordinary evidence for extraordinary claims</extraordinary_claim_validation>
      <uncertainty_acknowledgment>Explicitly state "I don't know" when information is uncertain (drastically reduces false information - Anthropic 2025)</uncertainty_acknowledgment>
      <current_source_mandate>ALL sources MUST be from 2025 - July 2025 context is MANDATORY</current_source_mandate>
      <outdated_source_blocking>BLOCK references to 2024 or earlier without current verification</outdated_source_blocking>
    </detection_protocols>
    <accuracy_enforcement>
      <grounding_requirement>All technical claims MUST be grounded in documented evidence</grounding_requirement>
      <direct_quotes>Extract word-for-word quotes from sources for grounding (Anthropic hallucination reduction guide)</direct_quotes>
      <citation_verification>Require citations and supporting evidence for all statements</citation_verification>
      <conservative_language>Use conservative language avoiding absolute statements without proof</conservative_language>
      <chain_of_thought>Explain reasoning step-by-step to reveal potential faulty logic (chain-of-thought verification, Anthropic 2025)</chain_of_thought>
    </accuracy_enforcement>
    <systematic_validation>
      <pre_publication_review>All content MUST undergo systematic fact-checking before finalization</pre_publication_review>
      <source_reliability_assessment>Evaluate source credibility using established criteria</source_reliability_assessment>
      <claim_substantiation>Document evidence trail for all technical assertions</claim_substantiation>
      <peer_review_simulation>Challenge own assumptions through adversarial thinking</peer_review_simulation>
      <iterative_refinement>Use previous outputs as follow-up prompts to catch inconsistencies (Anthropic iterative refinement method)</iterative_refinement>
    </systematic_validation>
    <error_correction_protocols>
      <immediate_correction>Correct identified errors immediately upon detection</immediate_correction>
      <systematic_review>Conduct comprehensive review when patterns of error detected</systematic_review>
      <transparency_requirement>Document corrections and methodology for future reference</transparency_requirement>
      <learning_integration>Update validation protocols based on error patterns</learning_integration>
    </error_correction_protocols>
    <trustworthiness_scoring>
      <self_evaluation>Rate own output trustworthiness in additional requests</self_evaluation>
      <uncertainty_quantification>Provide confidence levels for factual claims</uncertainty_quantification>
      <external_validation>Use external knowledge restrictions when appropriate (restrict to provided documents only - Anthropic technique)</external_validation>
      <best_of_n_verification>Run same prompts multiple times to compare outputs for inconsistencies (best-of-N verification, Anthropic 2025)</best_of_n_verification>
    </trustworthiness_scoring>
  </hallucination_prevention>
</claude_4_advanced_control>
```

────────────────────────────────────────────────────────────────────────────────

## Tool Patterns

```xml
<tool_patterns>
  <parallel>Read("f1"), Read("f2"), Read("f3") - concurrent execution improves performance</parallel>
  <rule>Read before write ALWAYS. Track multi-step with TodoWrite</rule>
  <rule>GitHub issues MANDATORY for >10 steps</rule>
</tool_patterns>
```

────────────────────────────────────────────────────────────────────────────────

## Architecture

```xml
<architecture>
  <commands location=".claude/commands/" delegate_only="true" enforcement="MANDATORY">
    <cmd name="/auto" module="patterns/intelligent-routing.md"/>
    <cmd name="/task" module="development/task-management.md"/>
    <cmd name="/feature" module="planning/feature-workflow.md"/>
    <cmd name="/swarm" module="patterns/multi-agent.md"/>
    <cmd name="/query" module="development/research-analysis.md"/>
    <cmd name="/session" module="patterns/session-management.md"/>
    <cmd name="/docs" module="development/documentation.md" critical="true"/>
    <cmd name="/protocol" module="patterns/session-management.md"/>
  </commands>
  <documentation_enforcement>
    <rule priority="CRITICAL">NEVER generate project documentation without /docs command</rule>
    <rule priority="CRITICAL">All documentation MUST go through /docs for consistency</rule>
    <rule priority="CRITICAL">README, guides, docs ONLY via /docs command</rule>
    <exception>CLAUDE.md updates and command documentation are allowed</exception>
  </documentation_enforcement>
  <modules location=".claude/modules/" implement_only="true">
    <category name="security|quality|development|patterns|planning|testing"/>
  </modules>
</architecture>
```

────────────────────────────────────────────────────────────────────────────────

## AWARE Process

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

────────────────────────────────────────────────────────────────────────────────

## Quality Gates

```xml
<quality_gates>
  <rule>TDD: RED→GREEN→REFACTOR mandatory</rule>
  <rule>Security: Threat model first</rule>
  <rule>Performance: 200ms p95</rule>
  <rule>Coverage: 90%+ with assertions</rule>
  <rule>Features: PRD-first approach</rule>
  <canonical_sources>
    <tdd>.claude/modules/quality/tdd.md</tdd>
    <security>.claude/modules/security/threat-modeling.md</security>
  </canonical_sources>
</quality_gates>
```

────────────────────────────────────────────────────────────────────────────────

## GitHub Workflow

```xml
<github_workflow trigger=">10 steps">
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

────────────────────────────────────────────────────────────────────────────────


## Modular Composition Methodology

```xml
<composition_methodology>
  <principles>
    <rule>Module isolation: Each module handles one domain completely</rule>
    <rule>Interface contracts: Clear input/output specifications</rule>
    <rule>Dependency injection: Modules receive dependencies, never create them</rule>
    <rule>Composition over inheritance: Combine modules, don't extend them</rule>
  </principles>
  <patterns>
    <pattern name="Command-Module">Commands delegate to modules via clear interfaces</pattern>
    <pattern name="Module-Chain">Modules can chain through standardized outputs</pattern>
    <pattern name="State-Isolation">Each module maintains its own state boundaries</pattern>
    <pattern name="Error-Propagation">Errors flow up through composition hierarchy</pattern>
  </patterns>
  <validation>
    <rule>Every module must have single responsibility</rule>
    <rule>Cross-module dependencies must be explicit</rule>
    <rule>Module interfaces must be versioned</rule>
    <rule>Composition must be deterministic and testable</rule>
  </validation>
</composition_methodology>
```

────────────────────────────────────────────────────────────────────────────────

## Error Recovery Protocols

```xml
<error_recovery>
  <strategy>
    <level name="Module">Graceful degradation with fallback behavior</level>
    <level name="Command">Retry with exponential backoff, max 3 attempts</level>
    <level name="System">Circuit breaker pattern, fail-fast after threshold</level>
    <level name="User">Clear error messages with corrective actions</level>
  </strategy>
  <protocols>
    <protocol name="File Operations">
      <step>1. Verify file exists before read/write</step>
      <step>2. Check permissions and accessibility</step>
      <step>3. Backup before destructive operations</step>
      <step>4. Rollback on failure, restore from backup</step>
    </protocol>
    <protocol name="Module Loading">
      <step>1. Validate module structure and dependencies</step>
      <step>2. Load in dependency order</step>
      <step>3. Gracefully handle missing modules</step>
      <step>4. Provide degraded functionality when possible</step>
    </protocol>
    <protocol name="Command Execution">
      <step>1. Validate inputs and preconditions</step>
      <step>2. Execute with timeout and resource limits</step>
      <step>3. Monitor for hanging or infinite loops</step>
      <step>4. Clean up resources on success or failure</step>
    </protocol>
  </protocols>
  <recovery_actions>
    <action trigger="FileNotFound">Create from template or prompt user</action>
    <action trigger="PermissionDenied">Suggest alternative paths or permissions</action>
    <action trigger="ModuleError">Fall back to core functionality</action>
    <action trigger="TimeoutError">Retry with increased timeout or simplify</action>
  </recovery_actions>
</error_recovery>
```

────────────────────────────────────────────────────────────────────────────────

## Command Selection Decision Trees

```xml
<command_selection>
  <decision_tree>
    <node name="Task Complexity">
      <condition>Simple single-step task</condition>
      <action>/task - Direct execution</action>
    </node>
    <node name="Task Complexity">
      <condition>Multi-step development task</condition>
      <branch>
        <condition>Requires research/understanding</condition>
        <action>/query - Research first, then /task</action>
      </branch>
      <branch>
        <condition>Clear requirements</condition>
        <action>/task - Direct implementation</action>
      </branch>
    </node>
    <node name="Feature Development">
      <condition>New feature with specifications</condition>
      <action>/feature - Autonomous development cycle</action>
    </node>
    <node name="Complex Integration">
      <condition>Multi-component system changes</condition>
      <action>/swarm - Multi-agent coordination</action>
    </node>
    <node name="Uncertainty">
      <condition>Unclear requirements or approach</condition>
      <action>/auto - Intelligent routing and planning</action>
    </node>
    <node name="Documentation vs Research">
      <condition>Need to understand how code works</condition>
      <action>/query - Research and analysis without modifications</action>
    </node>
    <node name="Documentation vs Research">
      <condition>Need to create or update documentation</condition>
      <action>/docs - Generate or modify documentation files</action>
    </node>
    <node name="Session Management">
      <condition>Long-running or multi-session work</condition>
      <action>/session - Context preservation</action>
    </node>
  </decision_tree>
  <selection_criteria>
    <criterion name="Scope">Lines of code affected, files modified</criterion>
    <criterion name="Complexity">Algorithmic complexity, integration points</criterion>
    <criterion name="Risk">Production impact, reversibility</criterion>
    <criterion name="Knowledge">Domain expertise required, research needed</criterion>
    <criterion name="Time">Estimated duration, session boundaries</criterion>
  </selection_criteria>
  <routing_logic>
    <rule>Single file + &lt;50 lines → /task</rule>
    <rule>Multiple files + clear spec → /feature</rule>
    <rule>Research required → /query then reassess</rule>
    <rule>Understanding code → /query (read-only analysis)</rule>
    <rule>Creating documentation → /docs (file generation)</rule>
    <rule>System-wide changes → /swarm</rule>
    <rule>Ambiguous requirements → /auto</rule>
    <rule>Session continuity needed → /session</rule>
  </routing_logic>
</command_selection>
```

────────────────────────────────────────────────────────────────────────────────

## Quality Gate Enforcement

```xml
<quality_gate_enforcement>
  <canonical_source>quality/universal-quality-gates.md</canonical_source>
  <master_mandate>ALL commands MUST validate through quality gates with BLOCKING enforcement</master_mandate>
  <critical_gates>
    <gate>TDD Compliance: RED→GREEN→REFACTOR mandatory</gate>
    <gate>Security Standards: Zero high-severity issues</gate>
    <gate>Performance Benchmarks: 200ms p95 required</gate>
    <gate>Code Quality: 90%+ coverage required</gate>
  </critical_gates>
  <orchestration>Commands delegate to quality modules for detailed validation and enforcement procedures</orchestration>
</quality_gate_enforcement>
```

────────────────────────────────────────────────────────────────────────────────

## Archive Management

```xml
<archive_management>
  <canonical_source>patterns/duplication-prevention.md</canonical_source>
  <master_rule>Check dependencies BEFORE archiving. Test AFTER archiving</master_rule>
  <archive_structure>/archive/[modules|commands|reports|experiments|documentation]/</archive_structure>
  <enforcement_context>Archive operations MUST follow dependency checking and validation procedures from duplication prevention module</enforcement_context>
  <orchestration>Delegate detailed procedures, lifecycle management, and monitoring to duplication prevention patterns</orchestration>
</archive_management>
```

────────────────────────────────────────────────────────────────────────────────

## Command Usage Enforcement

```xml
<command_enforcement priority="CRITICAL">
  <mandatory_usage>
    <documentation>/docs - ALL documentation generation MUST use this</documentation>
    <development>/task - Single file or focused development work</development>
    <research>/query - Research and understanding BEFORE coding</research>
    <features>/feature - PRD-driven autonomous development</features>
    <complex>/swarm - Multi-component with git worktrees</complex>
    <routing>/auto - When uncertain about approach</routing>
    <sessions>/session - Long-running work requiring context</sessions>
    <protocols>/protocol - Resuming interrupted work</protocols>
  </mandatory_usage>
  <prohibitions>
    <rule>NEVER create documentation without /docs command</rule>
    <rule>NEVER skip /query for research tasks</rule>
    <rule>NEVER use manual approach when commands exist</rule>
    <rule>NEVER ignore module capabilities in commands</rule>
  </prohibitions>
</command_enforcement>
```


## Versioning Strategy

```xml
<versioning_strategy>
  <framework_versioning>
    <current_version>2.6.0</current_version>
    <scheme>MAJOR.MINOR.PATCH (semantic versioning)</scheme>
    <policy>
      <major>Breaking changes to core framework architecture</major>
      <minor>New commands, modules, or significant feature additions</minor>
      <patch>Bug fixes, documentation updates, minor improvements</patch>
    </policy>
  </framework_versioning>
  <component_versioning>
    <commands>
      <version_alignment>All commands follow framework version (2.6.0)</version_alignment>
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
    <framework_2_6_0>
      <commands>All commands at 2.6.0</commands>
      <modules>Support any 1.x.x version</modules>
      <backward_compatibility>Full compatibility with 2.5.x commands</backward_compatibility>
    </framework_2_6_0>
  </compatibility_matrix>
  <version_update_procedures>
    <rule>Update version tables immediately when making changes</rule>
    <rule>Maintain backward compatibility within major versions</rule>
    <rule>Document breaking changes in CHANGELOG.md</rule>
    <rule>Test all components after version updates</rule>
  </version_update_procedures>
</versioning_strategy>
```

────────────────────────────────────────────────────────────────────────────────

## Temporal Standards Enforcement

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

────────────────────────────────────────────────────────────────────────────────

## Advanced Prompt Optimization

```xml
<advanced_prompt_optimization version="2.6.0" enforcement="CRITICAL">
  <claude_4_optimization>
    <xml_structure>Structured reasoning, max 4 levels, semantic tags for improved accuracy and clarity</xml_structure>
    <parallel_execution>Batch all tool calls - concurrent operations improve development workflow efficiency</parallel_execution>
    <thinking_integration>Interleaved thinking blocks with 16K token capacity for complex reasoning</thinking_integration>
    <context_management>200K token window optimization with hierarchical loading (Claude 4 verified)</context_management>
  </claude_4_optimization>
  
  <advanced_frameworks_2025>
    <foundational>RISE (Role, Input, Steps, Expectation) | TRACE (Task, Request, Action, Context, Expectation) | CARE (Context, Action, Result, Evaluation)</foundational>
    <specialized>APE (quick) | CLEAR (comprehensive) | SOAR (strategic) | CRISP (detailed) | SPARK (problem-solving)</specialized>
    <framework_selection>
      <simple_tasks>APE, CARE for rapid execution</simple_tasks>
      <moderate_tasks>RISE, TRACE, SOAR for structured workflows</moderate_tasks>
      <complex_tasks>CLEAR, CRISP, BRIDGE for comprehensive analysis</complex_tasks>
    </framework_selection>
  </advanced_frameworks_2025>
  
  <performance_patterns>
    <tool_orchestration>Intelligent batching for improved development workflow performance</tool_orchestration>
    <memory_optimization>Cascaded memory system with recursive imports up to 5 hops</memory_optimization>
    <session_management>40-minute session limits for optimal Claude Sonnet performance</session_management>
    <cost_optimization>Token-efficient prompts with structured XML for maximum value</cost_optimization>
  </performance_patterns>
  
  <quality_enforcement>
    <thinking_validation>Minimum 30-second critical thinking analysis before action</thinking_validation>
    <consequence_mapping>Map decision consequences: If X → Y → Z</consequence_mapping>
    <evidence_validation>Research-first methodology with cross-referencing using verified 2025 sources only</evidence_validation>
    <testing_standards>Unit 90% | Integration all | System e2e | TDD mandatory</testing_standards>
  </quality_enforcement>
</advanced_prompt_optimization>
```

────────────────────────────────────────────────────────────────────────────────

## Command-Module Integration

```xml
<command_module_integration enforcement="MANDATORY">
  <canonical_source>patterns/module-composition-framework.md</canonical_source>
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

────────────────────────────────────────────────────────────────────────────────

## Module Runtime Engine

```xml
<module_runtime_engine version="2.6.0" enforcement="CRITICAL">
  <purpose>Deterministic module composition and execution engine for Claude 4 with standardized patterns, universal quality gates, and comprehensive TDD enforcement</purpose>
  
  <runtime_architecture>
    <thinking_pattern_engine>
      <standardized_checkpoints>Every command uses checkpoint-based thinking patterns from patterns/thinking-pattern-template.md</standardized_checkpoints>
      <tdd_integration>TDD enforcement mandatory across all development commands with strict RED-GREEN-REFACTOR cycles</tdd_integration>
      <critical_thinking>30-second minimum analysis before any action with consequence mapping</critical_thinking>
      <validation_gates>Each checkpoint has verifiable validation criteria and blocking enforcement</validation_gates>
    </thinking_pattern_engine>
    
    <module_composition_framework>
      <lifecycle_management>Discovery → Loading → Orchestration → Integration with state management</lifecycle_management>
      <dependency_resolution>Topological sorting with hard/soft/conditional dependency types</dependency_resolution>
      <execution_patterns>Sequential for core stack, parallel for support modules, conditional for context-specific</execution_patterns>
      <state_isolation>Modules communicate through contracts, no direct state modification</state_isolation>
      <canonical_source>patterns/module-composition-framework.md</canonical_source>
    </module_composition_framework>
    
    <universal_quality_gates>
      <foundational_gates>Critical thinking, requirement clarity, module integration, error handling</foundational_gates>
      <development_gates>TDD compliance, code quality, security requirements, performance validation</development_gates>
      <coordination_gates>Multi-agent synchronization, session tracking, integration validation</coordination_gates>
      <documentation_gates>Standards compliance, TDD methodology documentation</documentation_gates>
      <analysis_gates>Research comprehensiveness, routing decision quality</analysis_gates>
      <canonical_source>quality/universal-quality-gates.md</canonical_source>
    </universal_quality_gates>
  </runtime_architecture>
  
  <command_runtime_specification>
    <standard_command_structure>
      <thinking_pattern enforcement="MANDATORY">Checkpoint-based with critical thinking and TDD integration</thinking_pattern>
      <tdd_integration enforcement="MANDATORY">Command-specific TDD requirements with blocking conditions</tdd_integration>
      <module_execution enforcement="MANDATORY">Core stack + contextual + support modules</module_execution>
      <universal_quality_gates enforcement="MANDATORY">Command-appropriate gate sets with validation</universal_quality_gates>
    </standard_command_structure>
    
    <command_implementations>
      <task_command>
        <runtime>Single-component TDD with foundational + development gates</runtime>
        <modules>critical-thinking → tdd → task-management → production-standards</modules>
        <gates>BLOCKING on TDD violations, quality failures</gates>
      </task_command>
      
      <swarm_command>
        <runtime>Multi-agent coordination with full gate enforcement</runtime>
        <modules>critical-thinking → session-management → multi-agent → tdd → git-operations → production-standards</modules>
        <gates>BLOCKING on coordination failures, TDD violations, integration issues</gates>
      </swarm_command>
      
      <auto_command>
        <runtime>TDD-aware intelligent routing with analysis gates</runtime>
        <modules>critical-thinking → intelligent-routing → tdd → pattern-library</modules>
        <gates>BLOCKING on routing to non-TDD commands for code changes</gates>
      </auto_command>
      
      <query_command>
        <runtime>Read-only analysis with test-aware research</runtime>
        <modules>critical-thinking → research-analysis → pattern-library → tdd</modules>
        <gates>BLOCKING on modification attempts, CONDITIONAL on analysis depth</gates>
      </query_command>
      
      <session_command>
        <runtime>Session management with TDD progress tracking</runtime>
        <modules>critical-thinking → session-management → tdd → git-operations</modules>
        <gates>BLOCKING on incomplete TDD tracking, missing artifacts</gates>
      </session_command>
      
      <protocol_command>
        <runtime>Production standards with strictest TDD enforcement</runtime>
        <modules>critical-thinking → session-management → production-standards → tdd → threat-modeling → pre-commit</modules>
        <gates>BLOCKING on ANY quality gate failure - strictest enforcement</gates>
      </protocol_command>
      
      <docs_command>
        <runtime>Documentation gateway with TDD methodology integration</runtime>
        <modules>critical-thinking → documentation → intelligent-routing → tdd</modules>
        <gates>BLOCKING on gateway violations, missing TDD references</gates>
      </docs_command>
    </command_implementations>
  </command_runtime_specification>
  
  <tdd_enforcement>
    <canonical_source>quality/tdd.md</canonical_source>
    <master_mandate>RED→GREEN→REFACTOR cycle MANDATORY for ALL development commands</master_mandate>
    <universal_requirement>Write failing tests FIRST, implement minimal code, refactor while keeping tests green</universal_requirement>
    <blocking_enforcement>ANY implementation before tests BLOCKS command execution</blocking_enforcement>
    <orchestration>Commands delegate to TDD module for detailed cycle enforcement and validation procedures</orchestration>
  </tdd_enforcement>
  
  <execution_optimization>
    <parallel_execution>
      <tool_batching>Significant performance improvement through parallel tool calls (SWE-bench verified gains)</tool_batching>
      <module_parallelization>Independent modules execute simultaneously</module_parallelization>
      <dependency_optimization>Topological sorting minimizes execution time</dependency_optimization>
    </parallel_execution>
    
    <context_preservation>
      <state_management>Execution context maintained across module boundaries</state_management>
      <result_accumulation>Module outputs accumulated for integration</result_accumulation>
      <error_isolation>Module failures contained without cascade effects</error_isolation>
    </context_preservation>
    
    <performance_targets>
      <command_execution>Commands complete within 2-minute typical case</command_execution>
      <module_loading>Module dependency resolution within 10 seconds</module_loading>
      <quality_gates>Quality gate validation within 30 seconds</quality_gates>
      <parallel_speedup>Performance improvement through batched operations (verified by SWE-bench results)</parallel_speedup>
    </performance_targets>
  </execution_optimization>
  
  <error_handling_and_recovery>
    <error_classification>
      <module_errors>Loading failures, execution errors, integration failures</module_errors>
      <tdd_violations>Implementation before tests, coverage failures, cycle violations</tdd_violations>
      <quality_gate_failures>Security issues, performance problems, compliance violations</quality_gate_failures>
      <coordination_failures>Agent conflicts, session issues, communication breakdowns</coordination_failures>
    </error_classification>
    
    <recovery_protocols>
      <graceful_degradation>Continue with reduced functionality for non-critical failures</graceful_degradation>
      <retry_mechanisms>Exponential backoff for transient failures</retry_mechanisms>
      <escalation_paths>Route to appropriate recovery modules or user intervention</escalation_paths>
      <rollback_capabilities>State rollback for critical failures</rollback_capabilities>
    </recovery_protocols>
    
    <enforcement_levels>
      <blocking>HALT execution until issue resolved</blocking>
      <conditional>Alternative paths or degraded functionality</conditional>
      <warning>Log issue but continue execution</warning>
    </enforcement_levels>
  </error_handling_and_recovery>
  
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
    <framework_version>Advances framework to 2.6.0 with Claude 4 optimization and hallucination prevention</framework_version>
    <backward_compatibility>Full compatibility with existing 2.3.x commands and modules</backward_compatibility>
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

────────────────────────────────────────────────────────────────────────────────

## Prompt Construction Methodology

```xml
<prompt_construction_methodology version="1.0.0" enforcement="CRITICAL">
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
      <step order="1">Parse command structure and extract thinking pattern checkpoints</step>
      <step order="2">Load required modules and validate interface contracts</step>
      <step order="3">Construct execution workflow with dependency resolution</step>
      <step order="4">Optimize context window usage through parallel execution</step>
      <step order="5">Execute with real-time progress tracking and error handling</step>
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

────────────────────────────────────────────────────────────────────────────────

## Claude Code Integration

```xml
<claude_code_integration version="2.6.0" enforcement="MANDATORY">
  <purpose>Advanced Claude Code terminal optimization for maximum productivity and efficiency</purpose>
  
  <memory_management_mastery>
    <cascaded_memory_system>
      <purpose>Hierarchical context loading for optimal token usage</purpose>
      <memory_hierarchy>
        <level name="project_memory">./CLAUDE.md - Project-specific guidelines and conventions</level>
        <level name="user_memory">~/.claude/CLAUDE.md - Personal preferences across all projects</level>
        <level name="imported_memory">@path/to/import - Conditional context via import syntax</level>
      </memory_hierarchy>
      <optimization_strategies>
        <lean_memory>Keep memory files under 2000 tokens each with bullet points</lean_memory>
        <conditional_loading>Use @import for context that's only sometimes needed</conditional_loading>
        <recursive_imports>Up to 5 hops for complex project structures</recursive_imports>
      </optimization_strategies>
    </cascaded_memory_system>
    
    <claude_md_best_practices>
      <essential_sections>
        <project_overview>Architecture, main technologies, key dependencies</project_overview>
        <development_conventions>Code style, naming conventions, file organization</development_conventions>
        <workflow_patterns>Testing strategy, deployment process, common tasks</workflow_patterns>
        <environment_setup>Local development setup, tool configuration, dependencies</environment_setup>
      </essential_sections>
    </claude_md_best_practices>
  </memory_management_mastery>
  
  <workflow_optimization_patterns>
    <research_first_methodology>
      <purpose>Significantly improve Claude Code performance through structured analysis</purpose>
      <core_principle>Research and planning BEFORE coding prevents costly iterations</core_principle>
      <implementation_steps>
        <context_gathering>Analyze project structure and understand requirements</context_gathering>
        <planning_phase>Detailed implementation plan with trade-off analysis</planning_phase>
        <validation_phase>Review plan against project conventions and constraints</validation_phase>
        <execution_phase>Implement solution with continuous validation</execution_phase>
      </implementation_steps>
    </research_first_methodology>
    
    <tdd_enhanced_workflows>
      <purpose>Leverage agentic coding for powerful test-driven development</purpose>
      <patterns>
        <test_specification>Define behavior → Write comprehensive tests → Verify failures → Block implementation</test_specification>
        <iterative_implementation>Minimal code for single test → Confirm pass → Refactor → Repeat</iterative_implementation>
        <quality_enforcement>No implementation until tests written and failing</quality_enforcement>
      </patterns>
    </tdd_enhanced_workflows>
    
    <extended_thinking_triggers>
      <thinking_levels>
        <standard>Normal reasoning and problem solving</standard>
        <enhanced>"think more", "think harder", "think longer"</enhanced>
        <maximum>"ultrathink" - Activates deepest analysis capabilities</maximum>
      </thinking_levels>
    </extended_thinking_triggers>
  </workflow_optimization_patterns>
  
  <session_management_strategies>
    <context_preservation>
      <session_optimization>
        <compact_sessions>40-minute session limits for optimal Claude Sonnet performance</compact_sessions>
        <state_reconstruction>Fresh context loading often more efficient than continuation</state_reconstruction>
        <strategic_compaction>Use /compact only when approaching message limits</strategic_compaction>
      </session_optimization>
    </context_preservation>
    
    <cost_optimization>
      <monitoring_strategies>
        <token_awareness>Monitor consumption and estimate costs in real-time</token_awareness>
        <session_efficiency>Optimize prompts to reduce back-and-forth iterations</session_efficiency>
        <clear_instructions>Use specific instructions to minimize clarification requests</clear_instructions>
      </monitoring_strategies>
    </cost_optimization>
  </session_management_strategies>
  
  <advanced_claude_code_techniques>
    <autonomous_workflow_patterns>
      <multi_step_delegation>Complete workflows from requirements to testing</multi_step_delegation>
      <context_awareness>Intelligent decisions across file system, Git history, runtime logs</context_awareness>
      <intelligent_error_recovery>Self-healing workflows with minimal intervention</intelligent_error_recovery>
    </autonomous_workflow_patterns>
    
    <performance_enhancement>
      <parallel_file_operations>Significant improvement through concurrent Read() operations</parallel_file_operations>
      <context_budget_management>Reserve 50K+ tokens for active development work</context_budget_management>
      <tool_selection_optimization>Choose optimal tools for each task type</tool_selection_optimization>
    </performance_enhancement>
  </advanced_claude_code_techniques>
</claude_code_integration>
```

────────────────────────────────────────────────────────────────────────────────

## Security and Performance Optimization

```xml
<security_performance_optimization version="2.6.0" enforcement="CRITICAL">
  <purpose>Advanced security and performance patterns for Claude 4 and Claude Code</purpose>
  
  <security_optimization_patterns>
    <data_protection_strategies>
      <privacy_enforcement>
        <data_minimization>Only include necessary data in prompts and context</data_minimization>
        <secure_context_handling>Use ephemeral contexts for sensitive operations</secure_context_handling>
        <access_control>Role-based access to sensitive Claude Code operations</access_control>
      </privacy_enforcement>
      
      <audit_and_monitoring>
        <operation_logging>Log all Claude Code operations for security auditing</operation_logging>
        <anomaly_detection>Monitor unusual usage patterns and policy violations</anomaly_detection>
        <compliance_validation>Regular validation against security policies and regulations</compliance_validation>
      </audit_and_monitoring>
    </data_protection_strategies>
    
    <secure_coding_patterns>
      <threat_modeling_integration>
        <security_first_design>Include threat modeling in architectural planning</security_first_design>
        <vulnerability_scanning>Integrate security scanning into workflows</vulnerability_scanning>
        <secure_defaults>Apply security best practices by default</secure_defaults>
      </threat_modeling_integration>
    </secure_coding_patterns>
  </security_optimization_patterns>
  
  <performance_optimization_mastery>
    <context_window_efficiency>
      <token_management_strategies>
        <hierarchical_prioritization>Critical first, supporting details last</hierarchical_prioritization>
        <compression_techniques>XML structure for improved token efficiency and accuracy</compression_techniques>
        <lazy_loading_patterns>Load context incrementally as needed</lazy_loading_patterns>
      </token_management_strategies>
      
      <session_optimization>
        <context_budget_monitoring>Track usage, reserve 50K+ for active work</context_budget_monitoring>
        <strategic_session_management>40 minutes intensive = new session</strategic_session_management>
        <context_inheritance>Efficient transfer through memory files</context_inheritance>
      </session_optimization>
    </context_window_efficiency>
    
    <execution_performance_patterns>
      <parallel_processing_optimization>
        <concurrent_operation_batching>Latency reduction through parallel execution based on SWE-bench results</concurrent_operation_batching>
        <pipeline_optimization>Parallel gathering → Sequential analysis → Parallel implementation</pipeline_optimization>
        <resource_utilization>Complex reasoning during parallel tool execution</resource_utilization>
      </parallel_processing_optimization>
      
      <accuracy_optimization>
        <validation_checkpoints>Intermediate result verification and error correction</validation_checkpoints>
        <iterative_refinement>Initial solution → Reflection → Refinement → Validation</iterative_refinement>
        <multi_perspective_analysis>Technical, business, and user perspectives</multi_perspective_analysis>
      </accuracy_optimization>
    </execution_performance_patterns>
  </performance_optimization_mastery>
</security_performance_optimization>
```

────────────────────────────────────────────────────────────────────────────────

**Remember**: Critical thinking partner. Research deeply. Challenge assumptions. Map consequences.