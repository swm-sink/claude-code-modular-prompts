<command_file>
  <metadata>
    <name>/secure audit</name>
    <purpose>Performs a comprehensive security compliance audit across code, configuration, and access controls.</purpose>
    <usage>
      <![CDATA[
      /secure audit <standard="owasp">
      ]]>
    </usage>
  </metadata>

  <arguments>
    <argument name="standard" type="string" required="false" default="owasp">
      <description>The compliance standard to audit against (e.g., 'owasp', 'iso27001', 'nist').</description>
    </argument>
  </arguments>
  
  <examples>
    <example>
      <description>Run a security audit against the OWASP Top 10 standard.</description>
      <usage>/secure audit</usage>
    </example>
    <example>
      <description>Run a security audit against the NIST framework.</description>
      <usage>/secure audit standard="nist"</usage>
    </example>
  </examples>

  <claude_prompt>
    <prompt>
      You are a security auditor. The user wants to perform a compliance audit.

      1.  **Define Scope**: Based on the chosen `standard`, define the full scope of the audit. This includes checking access control, code security, and configuration.
      2.  **Execute Audit Checks**:
          *   Scan the codebase and configuration files for compliance gaps related to the standard.
          *   For example, for OWASP, this would involve looking for potential injection flaws, broken authentication, sensitive data exposure, etc.
          *   <include component="components/context/find-relevant-code.md" />
      3.  **Generate Audit Report**:
          *   Create a comprehensive audit report that includes:
              *   A risk assessment matrix.
              *   A detailed list of all identified compliance gaps with severity levels.
              *   A prioritized remediation roadmap.
          *   <include component="components/reporting/generate-structured-report.md" />
    </prompt>
  </claude_prompt>

  <dependencies>
    <includes_components>
      <component>components/context/find-relevant-code.md</component>
      <component>components/reporting/generate-structured-report.md</component>
    </includes_components>
  </dependencies>
</command_file>