# Claude 4 Optimization Guide

<guide_metadata>
  <purpose>Claude 4 optimization patterns for framework files</purpose>
  <enforcement>MANDATORY consultation before editing .claude files</enforcement>
  <version>2.0.0</version>
</guide_metadata>

<optimization_principles>
  
  <xml_structure enforcement="mandatory">
    <rule>ALL framework files MUST use XML structure for critical components</rule>
    <purpose>Leverage Claude 4's enhanced XML parsing accuracy</purpose>
  </xml_structure>
  
  <token_targets>
    <foundation_files max="3000"/>
    <core_commands max="4000"/>
    <modules max="2000"/>
    <total_framework max="120000"/>
  </token_targets>
  
</optimization_principles>

<claude_4_techniques>
  
  <explicit_instructions>
    <principle>Claude 4 requires MORE explicit instructions than previous versions</principle>
    <pattern>
      <correct_format>
        <instruction enforcement="strict">
          <requirement>MUST create GitHub session for all multi-agent work</requirement>
          <validation>Verify session creation before proceeding</validation>
        </instruction>
      </correct_format>
    </pattern>
  </explicit_instructions>
  
  <deterministic_execution>
    <purpose>Ensure consistent behavior through strict enforcement</purpose>
    <pattern>
      <execution_control type="deterministic">
        <pre_conditions mandatory="true">
          <condition>All required files must exist</condition>
        </pre_conditions>
        <quality_gates mandatory="true">
          <gate name="tests_pass" command="pytest"/>
        </quality_gates>
      </execution_control>
    </pattern>
  </deterministic_execution>
  
  <multiple_emphasis>
    <purpose>Layer emphasis for critical rules</purpose>
    <pattern>
      <critical_requirement enforcement="MANDATORY">
        <rule priority="HIGHEST">ALL commands MUST delegate to modules</rule>
        <validation>Commands contain ONLY delegation instructions</validation>
        <failure_consequence>Violating delegation breaks modularity</failure_consequence>
      </critical_requirement>
    </pattern>
  </multiple_emphasis>
  
  <context_motivation>
    <purpose>Explain WHY for better Claude 4 performance</purpose>
    <pattern>
      <instruction context="performance_optimization">
        <motivation>Parallel execution reduces latency by 70%</motivation>
        <requirement>Use ALL tool calls in single message</requirement>
      </instruction>
    </pattern>
  </context_motivation>
  
</claude_4_techniques>

<framework_standards enforcement="mandatory">
  
  <command_structure>
    <template>
      <command name="[command_name]" purpose="[brief_description]">
        <delegation target="modules/[category]/[module_name].md">
          This command delegates ALL implementation to the specified module
        </delegation>
        <module_integration>
          <primary_module>modules/[category]/[module_name].md</primary_module>
        </module_integration>
        <usage_examples>
          <example type="basic">[simple usage]</example>
        </usage_examples>
        <reference>See modules/[category]/[module_name].md for implementation</reference>
      </command>
    </template>
  </command_structure>
  
  <module_structure>
    <template>
      <module name="[module_name]" category="[development|patterns|quality|security]">
        <purpose>[Concise 1-2 sentence description]</purpose>
        <trigger_conditions>
          <condition type="automatic">[When auto-activates]</condition>
        </trigger_conditions>
        <implementation>
          <phase name="[phase_1]" order="1">
            <requirements>[What must be true]</requirements>
            <actions>[Specific steps]</actions>
            <validation>[Verify success]</validation>
          </phase>
        </implementation>
        <quality_gates enforcement="strict">
          <gate name="[gate_name]" requirement="[requirement]"/>
        </quality_gates>
      </module>
    </template>
  </module_structure>
  
</framework_standards>

<strict_enforcement_patterns>
  <pattern name="zero_redundancy">
    <primary_rule>Every concept exists in exactly ONE place</primary_rule>
    <verification>Commands delegate - modules implement</verification>
    <consequence>Violation breaks single source of truth</consequence>
    <validation_checklist>
      <check>Commands contain only delegation</check>
      <check>Modules contain all implementation</check>
      <check>No content duplication</check>
    </validation_checklist>
  </pattern>
</strict_enforcement_patterns>

<xml_best_practices>
  
  <naming_standards>
    <rule>Use lowercase with underscores: execution_requirements</rule>
    <rule>Be descriptive: trigger_conditions not conditions</rule>
    <rule>Match references: "Using <requirements>"</rule>
  </naming_standards>
  
  <framework_vocabulary>
    <core_tags>
      <tag name="command">Root tag for command files</tag>
      <tag name="module">Root tag for module files</tag>
      <tag name="delegation">Command→Module relationship</tag>
    </core_tags>
    <control_tags>
      <tag name="strict_enforcement">Non-negotiable requirements</tag>
      <tag name="quality_gates">Mandatory checkpoints</tag>
      <tag name="execution_requirements">Pre-conditions</tag>
    </control_tags>
  </framework_vocabulary>
  
</xml_best_practices>

<quality_validation mandatory="true">
  
  <structural_checks>
    <check>XML tags properly opened/closed</check>
    <check>Consistent tag naming</check>
    <check>Proper nesting hierarchy</check>
  </structural_checks>
  
  <content_checks>
    <check>Commands ONLY delegate</check>
    <check>Modules contain ALL implementation</check>
    <check>No redundant content</check>
    <check>References point to correct modules</check>
  </content_checks>
  
  <optimization_checks>
    <check>Token count within limits</check>
    <check>Strict enforcement for critical rules</check>
    <check>Claude 4 techniques implemented</check>
  </optimization_checks>
  
</quality_validation>

<common_pitfalls>
  <pitfall name="verbose_explanations">
    <problem>Claude 4 prefers concise, structured instructions</problem>
    <solution>Use XML structure instead of long prose</solution>
  </pitfall>
  <pitfall name="ambiguous_instructions">
    <problem>Claude 4 needs MORE explicit instructions</problem>
    <solution>Specify exact behaviors and validation</solution>
  </pitfall>
  <pitfall name="missing_context">
    <problem>Not explaining WHY behaviors matter</problem>
    <solution>Add motivation tags</solution>
  </pitfall>
</common_pitfalls>

<performance_optimization>
  
  <token_management>
    <strategies>
      <strategy>Replace prose with XML structure</strategy>
      <strategy>Move implementation to modules</strategy>
      <strategy>Use reference links vs duplication</strategy>
    </strategies>
    <tools>
      <tool>Token counter (tiktoken)</tool>
      <tool>XML validator</tool>
      <tool>Redundancy checker</tool>
    </tools>
  </token_management>
  
  <claude_4_features>
    <parallel_execution>All tool calls in single message</parallel_execution>
    <thinking_capabilities>Complex reasoning with thinking tags</thinking_capabilities>
    <extended_context>200k token window with XML structure</extended_context>
  </claude_4_features>
  
</performance_optimization>

<quick_reference>
  
  <pre_edit_checklist>
    <step>Read this guide completely</step>
    <step>Identify file type (command vs module)</step>
    <step>Apply XML structure</step>
    <step>Use strict enforcement for critical rules</step>
    <step>Validate token count within limits</step>
    <step>Ensure zero redundancy principle</step>
  </pre_edit_checklist>
  
  <emergency_rules enforcement="ABSOLUTE">
    <rule>Commands ONLY delegate - modules ONLY implement</rule>
    <rule>Every concept exists in exactly ONE place</rule>
    <rule>Use XML structure for ALL framework components</rule>
    <rule>Stay within token budgets</rule>
    <rule>Apply strict enforcement to critical requirements</rule>
  </emergency_rules>
  
</quick_reference>

<guide_conclusion>
  This optimized guide ensures Claude 4 compatibility while maintaining framework modularity and efficiency.
</guide_conclusion>