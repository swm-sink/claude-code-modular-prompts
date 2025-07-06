<command purpose="Test-driven development with strict RED-GREEN-REFACTOR discipline and coverage enforcement">
  
  <delegation target="modules/quality/tdd.md">
    This command delegates ALL implementation to the TDD module which provides comprehensive test-driven development workflows including strict RED-GREEN-REFACTOR cycle enforcement, coverage standards, and quality gate validation.
  </delegation>
  
  <module_integration>
    <primary_module>modules/quality/tdd.md</primary_module>
    <supporting_modules>
      <module>modules/quality/production-standards.md</module>
      <module>modules/patterns/session-management.md</module>
      <module>modules/development/task-management.md</module>
    </supporting_modules>
  </module_integration>
  
  <usage_examples>
    <example type="feature">/test "Add password reset functionality"</example>
    <example type="bug_fix">/test "Fix user logout not clearing session"</example>
    <example type="refactor">/test "Refactor payment processing for clarity"</example>
    <example type="coverage">/test "Add test coverage for user service"</example>
  </usage_examples>
  
  <strict_enforcement target="tdd_discipline">
    <primary_rule>MUST follow RED-GREEN-REFACTOR cycle - no exceptions</primary_rule>
    <verification>Test fails first (RED) + minimal implementation (GREEN) + safe refactor</verification>
    <consequence>Skipping TDD phases violates test-first development contract</consequence>
  </strict_enforcement>
  
  <reference>
    See modules/quality/tdd.md for complete implementation details including TDD cycle enforcement, coverage standards, test patterns, and quality gate requirements.
  </reference>
  
</command>
