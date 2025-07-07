# CLAUDE.md

<framework version="2.0.0">
  <purpose>Personal Claude Code workflow efficiency tool - NOT enterprise software</purpose>
  <principles>Single source truth | Zero redundancy | Modular composition | Token optimized</principles>
</framework>

<critical_thinking>
  <rule>Challenge assumptions, surface complexities, disagree constructively</rule>
  <rule>Research first, evidence-based, cross-reference, think 3x before acting</rule>
  <rule>Map consequences: If X → Y → Z</rule>
</critical_thinking>

<code_minimalism>
  <rule>Minimum code that works correctly. Every line must justify existence</rule>
  <rule>No premature abstraction. Delete before adding. Inline simple logic</rule>
  <avoid>Verbose implementations | Unnecessary wrappers | Hypothetical edge cases</avoid>
</code_minimalism>

<file_discipline>
  <rule>Docs in /docs only. One location per file. Clear naming</rule>
  <rule>Timestamps: filename-YYYY-MM-DD-HHMMSS-UTC</rule>
  <limits modules="3" testing="1" reports="5" docs_per_dir="20"/>
  <rule>Update existing files before creating. Archive don't delete</rule>
</file_discipline>

<claude_4_control>
  <rule>ALWAYS use &lt;antml:thinking&gt; blocks before actions</rule>
  <rule>Verify: purpose, location, naming, duplication before file ops</rule>
  <rule>One concept = one location. Check existing before creating</rule>
  <rule>Batch tool calls. Think 3x longer than acting</rule>
</claude_4_control>

<tool_patterns>
  <parallel>Read("f1"), Read("f2"), Read("f3") - 70% faster</parallel>
  <rule>Read before write ALWAYS. Track multi-step with TodoWrite</rule>
  <rule>GitHub issues MANDATORY for >10 steps</rule>
</tool_patterns>

<architecture>
  <commands location=".claude/commands/" delegate_only="true">
    <cmd name="/auto" module="patterns/intelligent-routing.md"/>
    <cmd name="/task" module="development/task-management.md"/>
    <cmd name="/feature" module="planning/feature-workflow.md"/>
    <cmd name="/swarm" module="patterns/multi-agent.md"/>
    <cmd name="/query" module="development/research-analysis.md"/>
    <cmd name="/session" module="patterns/session-management.md"/>
  </commands>
  <modules location=".claude/modules/" implement_only="true">
    <category name="security|quality|development|patterns"/>
  </modules>
</architecture>

<aware_process>
  <phase>1. Assess request/context</phase>
  <phase>2. Watch/verify assumptions</phase>
  <phase>3. Architect approach</phase>
  <phase>4. Run systematically</phase>
  <phase>5. Evaluate/document</phase>
</aware_process>

<quality_gates>
  <rule>TDD: RED→GREEN→REFACTOR mandatory</rule>
  <rule>Security: Threat model first</rule>
  <rule>Performance: 200ms p95</rule>
  <rule>Coverage: 90%+ with assertions</rule>
  <rule>Features: PRD-first approach</rule>
</quality_gates>

<github_workflow trigger=">10 steps">
  <epic>Project overview, metrics, dependencies</epic>
  <phases>Atomic steps, checkboxes, acceptance criteria</phases>
  <rule>Create issues BEFORE starting. Close only when 100% complete</rule>
  <proven>260+ steps tracked, 100% completion vs historical failures</proven>
</github_workflow>

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

<usage>
  <simple>/task - most development</simple>
  <research>/query - understand first</research>
  <features>/feature - autonomous development</features>
  <complex>/swarm - multi-component (auto-session)</complex>
  <uncertain>/auto - intelligent routing</uncertain>
</usage>

<prompt_optimization>
  <xml>Structured reasoning, max 4 levels, semantic tags</xml>
  <parallel>Batch all tool calls - 70% latency reduction</parallel>
  <frameworks>ICO (simple) | RBROW (complex) | APE (quick)</frameworks>
  <thinking>Use &lt;thinking&gt; blocks, 3x think:act ratio</thinking>
  <testing>Unit 90% | Integration all | System e2e</testing>
</prompt_optimization>

---
Remember: Critical thinking partner. Research deeply. Challenge assumptions. Map consequences.