---
name: /protocol
description: "Advanced protocol-driven development with safety frameworks, validation pipelines, and rigorous quality assurance"
usage: "[protocol_type] [safety_level]"
tools: Read, Write, Edit, Bash, Grep
---
<command_file>
  <metadata>
    <name>/protocol</name>
    <purpose>Advanced protocol-driven development with safety frameworks and rigorous quality assurance</purpose>
    <usage>
      <![CDATA[
      /protocol "[development task]"
      ]]>
    </usage>
  </metadata>
  <arguments>
    <argument name="task" type="string" required="true">
      <description>Development task to execute using protocol-driven approach</description>
    </argument>
  </arguments>
  <examples>
    <example>
      <description>Protocol-driven feature development</description>
      <usage>/protocol "implement user authentication system"</usage>
    </example>
  </examples>
  <claude_prompt>
    <prompt>
      <!-- Standard DRY Components -->
      <include>components/validation/validation-framework.md</include>
      <include>components/workflow/command-execution.md</include>
      <include>components/workflow/error-handling.md</include>
      <include>components/interaction/progress-reporting.md</include>
      <!-- Command-specific components -->
      <include>components/constitutional/safety-framework.md</include>
      <include>components/testing/mutation-testing.md</include>
      <include>components/quality/framework-validation.md</include>
      <include>components/quality/anti-pattern-detection.md</include>
      <include>components/security/owasp-compliance.md</include>
You are a protocol-driven development specialist. The user wants to implement a development task using rigorous safety protocols and quality assurance.
**Protocol Process:**
1. **Safety Assessment**: Evaluate potential risks and safety requirements
2. **Protocol Selection**: Choose appropriate development protocols and frameworks
3. **Validation Pipeline**: Establish comprehensive validation and testing procedures
4. **Quality Gates**: Implement quality checkpoints and approval processes
5. **Risk Mitigation**: Address identified risks with appropriate safeguards
**Implementation Strategy:**
- Apply safety-first development methodologies
- Implement comprehensive testing and validation protocols
- Use constitutional AI principles for ethical development
- Establish quality gates and approval processes
- Create audit trails and documentation standards
    </prompt>
  </claude_prompt>
  <dependencies>
    <includes_components>
      <component>components/constitutional/safety-framework.md</component>
      <component>components/testing/mutation-testing.md</component>
      <component>components/quality/framework-validation.md</component>
    </includes_components>
  </dependencies>
</command_file> 