<command purpose="General development execution for single-component work with automatic quality enforcement">
  
  <delegation target="modules/development/task-management.md">
    This command delegates ALL implementation to the task management module which provides comprehensive single-component development workflows including TDD enforcement, quality gates, and intelligent escalation patterns.
  </delegation>
  
  <module_integration>
    <primary_module>modules/development/task-management.md</primary_module>
    <supporting_modules>
      <module>modules/quality/tdd.md</module>
      <module>modules/quality/production-standards.md</module>
      <module>modules/patterns/session-management.md</module>
      <module>modules/patterns/git-operations.md</module>
    </supporting_modules>
  </module_integration>
  
  <usage_examples>
    <example type="basic">/task "Add email validation to user registration"</example>
    <example type="bug_fix">/task "Fix memory leak in image processor" --fix</example>
    <example type="refactor">/task "Refactor user service to SOLID principles" --refactor</example>
    <example type="docs">/task "Document the authentication API" --docs</example>
    <example type="issue_linked">/task "Add OAuth2 support" --issue #89</example>
    <example type="ci_setup">/task "Setup automated testing pipeline" --ci</example>
  </usage_examples>
  
  <escalation_triggers>
    <trigger condition="multi_component">Multiple components affected - escalates to /swarm</trigger>
    <trigger condition="system_wide">System-wide changes needed - escalates to /swarm</trigger>
    <trigger condition="complex_integration">Complex integration required - escalates to /swarm</trigger>
  </escalation_triggers>
  
  <strict_enforcement target="quality_standards">
    <primary_rule>ALL tasks MUST satisfy mandatory quality gates before completion</primary_rule>
    <verification>Tests pass + linting clean + coverage >90% + types valid</verification>
    <consequence>Incomplete quality gates prevent task completion and deployment</consequence>
  </strict_enforcement>
  
  <reference>
    See modules/development/task-management.md for complete implementation details including TDD workflows, quality enforcement, session integration, and escalation patterns.
  </reference>
  
</command>