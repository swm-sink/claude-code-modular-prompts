| version | last_updated | status |
|---------|--------------|--------|
| 2.3.0   | 2025-07-07   | stable |

# CLAUDE.md - Framework Control Document

────────────────────────────────────────────────────────────────────────────────

<purpose>Personal Claude Code workflow efficiency tool - NOT enterprise software</purpose>

## Core Framework

```xml
<framework version="2.3.0">
  <purpose>Personal Claude Code workflow efficiency tool - NOT enterprise software</purpose>
  <principles>Single source truth | Zero redundancy | Modular composition | Token optimized</principles>
</framework>
```

────────────────────────────────────────────────────────────────────────────────

## Critical Thinking Rules

```xml
<critical_thinking>
  <rule>Challenge assumptions, surface complexities, disagree constructively</rule>
  <rule>Research first, evidence-based, cross-reference, think 3x before acting</rule>
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
  <verification_checklist mandatory="true">
    <before_create>Does this file/directory already exist somewhere?</before_create>
    <before_create>Is there an existing location where this belongs?</before_create>
    <before_create>Have I checked with LS/Glob to verify the path?</before_create>
    <before_create>Is this ABSOLUTELY necessary for the user's request?</before_create>
    <before_create>Am I creating clutter or organizing properly?</before_create>
  </verification_checklist>
  <standard_rules>
    <rule>Docs in /docs only. One location per file. Clear naming</rule>
    <rule>Timestamps: filename-YYYY-MM-DD-HHMMSS-UTC</rule>
    <rule>Temporal Standards: All dates MUST be July 2025 (2025-07-XX) in UTC format</rule>
    <rule>Version Table Format: | version | last_updated | status | with YYYY-MM-DD format</rule>
    <rule>Compliance: Use 2025-07-07 as standard date, increment days for sequencing</rule>
    <rule>Update existing files before creating. Archive don't delete</rule>
  </standard_rules>
  <limits patterns="6" quality="4" planning="5" development="4" security="3" testing="2" reports="5" docs_per_dir="20"/>
  <prohibited_actions>
    <action>Creating 'personal/', 'local/', or user-specific directories</action>
    <action>Duplicating existing project structures</action>
    <action>Creating test files outside /tests directory</action>
    <action>Making directories without checking if they exist first</action>
    <action>Creating analytics or temporary files in tracked locations</action>
  </prohibited_actions>
</file_discipline>
```

────────────────────────────────────────────────────────────────────────────────

## Claude 4 Control

```xml
<claude_4_control>
  <mandatory_verification enforcement="ABSOLUTE">
    <rule priority="CRITICAL">ALWAYS use &lt;antml:thinking&gt; blocks before EVERY action</rule>
    <rule priority="CRITICAL">Think 5X longer than acting - NO EXCEPTIONS</rule>
    <rule priority="CRITICAL">Verify location EXISTS with LS/Glob BEFORE any file operation</rule>
    <rule priority="CRITICAL">Check for duplicates/existing files BEFORE creating anything</rule>
  </mandatory_verification>
  <file_operation_protocol>
    <step order="1">THINK: What am I about to do and why?</step>
    <step order="2">CHECK: Does this file/directory already exist? (USE LS/Glob)</step>
    <step order="3">VERIFY: Is this the correct location per framework rules?</step>
    <step order="4">VALIDATE: Is this absolutely necessary?</step>
    <step order="5">EXECUTE: Only if all checks pass</step>
  </file_operation_protocol>
  <attention_to_detail>
    <rule>One concept = one location. NEVER duplicate</rule>
    <rule>Batch tool calls for efficiency</rule>
    <rule>Read file organization rules BEFORE creating</rule>
    <rule>Double-check paths and naming conventions</rule>
    <rule>NO assumptions - verify everything</rule>
  </attention_to_detail>
</claude_4_control>
```

────────────────────────────────────────────────────────────────────────────────

## Tool Patterns

```xml
<tool_patterns>
  <parallel>Read("f1"), Read("f2"), Read("f3") - 70% faster</parallel>
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

## Archival Policy

```xml
<archival_policy>
  <scope>
    This policy applies to all files and directories that are no longer in active use but are kept for historical reference. This includes, but is not limited to:
    - Deprecated modules and commands
    - Outdated reports and analysis documents
    - Completed experimental code
  </scope>
  <procedure>
    <step order="1" name="Dependency Check">Before archiving any file, perform a full workspace search to identify all files that reference it. Update or remove all references before proceeding.</step>
    <step order="2" name="Relocation">Move the file or directory to the appropriate subdirectory within the `/archive` directory, following the structure defined below.</step>
    <step order="3" name="Verification">After moving the file, run all project tests and re-emulate key command prompts to ensure the archival has not introduced any regressions or broken dependencies.</step>
  </procedure>
  <structure>
    <path>/archive/modules/</path>
    <path>/archive/commands/</path>
    <path>/archive/reports/</path>
    <path>/archive/experiments/</path>
    <path>/archive/documentation/</path>
  </structure>
</archival_policy>
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
    <rule>System-wide changes → /swarm</rule>
    <rule>Ambiguous requirements → /auto</rule>
    <rule>Session continuity needed → /session</rule>
  </routing_logic>
</command_selection>
```

────────────────────────────────────────────────────────────────────────────────

## Quality Gate Enforcement Integration

```xml
<quality_gate_enforcement>
  <enforcement_points>
    <point name="Pre-Development">
      <gate>Requirements validation</gate>
      <gate>Architecture review</gate>
      <gate>Security threat modeling</gate>
      <action>Block until all gates pass</action>
    </point>
    <point name="Development">
      <gate>Code quality standards</gate>
      <gate>Test coverage minimum</gate>
      <gate>Performance benchmarks</gate>
      <action>Continuous validation during development</action>
    </point>
    <point name="Pre-Commit">
      <gate>All tests passing</gate>
      <gate>Security scan clean</gate>
      <gate>Documentation updated</gate>
      <action>Prevent commit until resolved</action>
    </point>
    <point name="Post-Development">
      <gate>Integration testing</gate>
      <gate>Performance regression check</gate>
      <gate>User acceptance criteria</gate>
      <action>Mark complete only when all gates pass</action>
    </point>
  </enforcement_points>
  <gate_definitions>
    <gate name="TDD Compliance">
      <check>RED test written first</check>
      <check>GREEN implementation passes</check>
      <check>REFACTOR improves design</check>
      <threshold>100% compliance required</threshold>
    </gate>
    <gate name="Security Standards">
      <check>Threat model completed</check>
      <check>Security scan passed</check>
      <check>Authentication/authorization verified</check>
      <threshold>Zero high-severity issues</threshold>
    </gate>
    <gate name="Performance Benchmarks">
      <check>Response time &lt; 200ms p95</check>
      <check>Memory usage within limits</check>
      <check>CPU utilization acceptable</check>
      <threshold>All benchmarks met</threshold>
    </gate>
    <gate name="Code Quality">
      <check>Test coverage ≥ 90%</check>
      <check>Cyclomatic complexity &lt; 10</check>
      <check>Code review approved</check>
      <threshold>All quality metrics met</threshold>
    </gate>
  </gate_definitions>
  <escalation_policy>
    <level name="Warning">Gate failure logged, development continues</level>
    <level name="Block">Gate failure prevents next phase</level>
    <level name="Abort">Gate failure terminates process</level>
    <override>Manual override requires explicit justification</override>
  </escalation_policy>
</quality_gate_enforcement>
```

────────────────────────────────────────────────────────────────────────────────

## Enhanced Archive Management Protocols

```xml
<enhanced_archive_management>
  <lifecycle_management>
    <phase name="Active">Files in primary workspace, regular updates</phase>
    <phase name="Deprecated">Files marked for archival, read-only</phase>
    <phase name="Archived">Files moved to /archive, historical reference</phase>
    <phase name="Purged">Files removed permanently after retention period</phase>
  </lifecycle_management>
  <archival_triggers>
    <trigger name="Time-based">Files unused for 90+ days</trigger>
    <trigger name="Version-based">Superseded by newer versions</trigger>
    <trigger name="Dependency-based">No active references found</trigger>
    <trigger name="Manual">Explicit archival request</trigger>
  </archival_triggers>
  <enhanced_procedures>
    <procedure name="Smart Dependency Analysis">
      <step>1. Recursive dependency scanning across all file types</step>
      <step>2. Cross-reference analysis including comments and documentation</step>
      <step>3. Import/export relationship mapping</step>
      <step>4. Dynamic reference detection (eval, require, etc.)</step>
    </procedure>
    <procedure name="Graduated Archival">
      <step>1. Mark as deprecated with warning notices</step>
      <step>2. Update dependent files to use alternatives</step>
      <step>3. Move to staging area for validation period</step>
      <step>4. Final archival with complete audit trail</step>
    </procedure>
    <procedure name="Archive Validation">
      <step>1. Full test suite execution</step>
      <step>2. Command validation across all modules</step>
      <step>3. Documentation link verification</step>
      <step>4. Performance regression testing</step>
    </procedure>
  </enhanced_procedures>
  <retention_policies>
    <policy name="Code Modules">5 years minimum retention</policy>
    <policy name="Documentation">3 years minimum retention</policy>
    <policy name="Reports">1 year minimum retention</policy>
    <policy name="Experiments">6 months minimum retention</policy>
  </retention_policies>
  <recovery_mechanisms>
    <mechanism name="Rollback">Quick restoration from archive</mechanism>
    <mechanism name="Partial Recovery">Selective file restoration</mechanism>
    <mechanism name="Reference Repair">Automatic dependency fixing</mechanism>
    <mechanism name="Version Bridging">Compatibility layer creation</mechanism>
  </recovery_mechanisms>
  <monitoring>
    <metric name="Archive Size">Track growth patterns</metric>
    <metric name="Access Frequency">Monitor archived file usage</metric>
    <metric name="Recovery Events">Track restoration requests</metric>
    <metric name="Dependency Breaks">Monitor reference failures</metric>
  </monitoring>
</enhanced_archive_management>
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

## Usage Patterns

```xml
<usage>
  <simple>/task - most development</simple>
  <research>/query - understand first</research>
  <features>/feature - autonomous development</features>
  <complex>/swarm - multi-component (auto-session)</complex>
  <uncertain>/auto - intelligent routing</uncertain>
  <documentation>/docs - ALL documentation tasks</documentation>
</usage>
```

────────────────────────────────────────────────────────────────────────────────

## Temporal Standards Enforcement

```xml
<temporal_standards>
  <rule>ALL version table dates MUST use July 2025 format: 2025-07-XX</rule>
  <rule>Standard date is 2025-07-07, increment for sequencing if needed</rule>
  <rule>Filename timestamps MUST use YYYY-MM-DD-HHMMSS-UTC format</rule>
  <rule>NO dates from January 2025 or other months allowed</rule>
  <validation>timestamp_compliance_check() in validation tool</validation>
  <enforcement>Auto-update non-compliant timestamps to 2025-07-07</enforcement>
</temporal_standards>
```

────────────────────────────────────────────────────────────────────────────────

## Prompt Optimization

```xml
<prompt_optimization>
  <xml>Structured reasoning, max 4 levels, semantic tags</xml>
  <parallel>Batch all tool calls - 70% latency reduction</parallel>
  <frameworks>ICO (simple) | RBROW (complex) | APE (quick)</frameworks>
  <thinking>Use &lt;thinking&gt; blocks, 3x think:act ratio</thinking>
  <testing>Unit 90% | Integration all | System e2e</testing>
</prompt_optimization>
```

────────────────────────────────────────────────────────────────────────────────

## Command Thinking Patterns

```xml
<command_thinking enforcement="MANDATORY">
  <critical_rule>EVERY command has explicit thinking_pattern section</critical_rule>
  <critical_rule>Claude 4 MUST follow thinking steps in order</critical_rule>
  <critical_rule>Commands EXPLICITLY guide module usage</critical_rule>
  
  <command_patterns>
    <auto>Calculate complexity score → Research → Route intelligently</auto>
    <task>Understand → Write FAILING test → Implement → Pass → Refactor</task>
    <feature>Generate PRD → Create session → Calculate complexity → Execute</feature>
    <swarm>Create session → Setup worktrees → Parallel Task() → Merge</swarm>
    <query>Parse → Parallel search → Analyze → Report (NO modifications)</query>
    <session>Create issue → Track progress → Link artifacts → Complete</session>
    <docs>BLOCK external docs → Apply standards → Update index</docs>
    <protocol>Validate → TDD → Security → Performance → Compliance</protocol>
  </command_patterns>
  
  <module_integration>
    <rule>Commands MUST explicitly reference module workflows</rule>
    <rule>Thinking patterns MUST align with module capabilities</rule>
    <rule>Error recovery MUST be integrated in all commands</rule>
    <rule>Performance patterns MUST use parallel execution</rule>
  </module_integration>
</command_thinking>
```

**Remember**: Critical thinking partner. Research deeply. Challenge assumptions. Map consequences.