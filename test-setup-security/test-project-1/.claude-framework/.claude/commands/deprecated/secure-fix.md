---
name: /secure-fix
description: "Automated security issue remediation with validation and rollback capabilities"
argument-hint: "[issue_type] [fix_level]"
allowed-tools: Read, Write, Edit, Bash, Grep
deprecated: true
deprecation-date: 2025-07-25
removal-date: 2025-08-25
replacement: "/secure-manage fix"
---
# /secure fix - Automated Security Remediation

⚠️ **DEPRECATED COMMAND** ⚠️

**This command is deprecated as of 2025-07-25 and will be removed on 2025-08-25.**

**Use instead:** `/secure-manage fix`

This command has been consolidated into the new `/secure-manage` command with `fix` mode for better organization and consistency.

---

Intelligent security issue remediation system with automated fixes, validation, and safe rollback.
## Usage
```bash
/secure fix vulnerabilities         # Fix known vulnerabilities
/secure fix permissions            # Fix file/directory permissions
/secure fix dependencies --safe    # Safe dependency updates
```
<command_file>
  <metadata>
    <name>/secure fix</name>
    <purpose>Automatically fixes security vulnerabilities in code and dependencies, with verification and reporting.</purpose>
    <usage>
      <![CDATA[
      /secure fix "[vulnerability_id_or_description]"
      ]]>
    </usage>
  </metadata>
  <arguments>
    <argument name="vulnerability" type="string" required="true">
      <description>The specific vulnerability to fix, identified by an ID from a scan or a clear description.</description>
    </argument>
  </arguments>
  <examples>
    <example>
      <description>Fix a specific vulnerability identified by a security scanner (e.g., CVE-2023-12345).</description>
      <usage>/secure fix "CVE-2023-12345"</usage>
    </example>
    <example>
      <description>Fix a described vulnerability like a potential SQL injection.</description>
      <usage>/secure fix "Potential SQL injection in user search API endpoint"</usage>
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
      <include>components/context/find-relevant-code.md</include>
      <include>components/interaction/request-user-confirmation.md</include>
      <include>components/actions/apply-code-changes.md</include>
      You are a security remediation specialist. The user wants you to fix a specific security vulnerability.
      1.  **Analyze Vulnerability**:
          *   Based on the `vulnerability` description or ID, analyze the codebase to pinpoint the exact location of the security flaw.
      2.  **Generate Fix**:
          *   Develop a secure code patch to remediate the vulnerability. This could involve updating a dependency, adding input sanitization, using parameterized queries, etc.
      3.  **Ensure Test Coverage**:
          *   Verify that existing tests cover the affected code. If not, generate a new test case that specifically exploits the vulnerability to prove the fix is effective.
      4.  **Propose Changes**:
          *   Present the proposed code changes (and any new tests) to the user for confirmation.
      5.  **Apply and Verify**:
          *   On confirmation, apply the changes.
          *   Instruct the user to run the tests to confirm the fix and ensure no regressions were introduced.
    </prompt>
  </claude_prompt>
  <dependencies>
    <chain>
      <command>/test unit</command>
    </chain>
    <includes_components>
      <component>components/context/find-relevant-code.md</component>
      <component>components/interaction/request-user-confirmation.md</component>
      <component>components/actions/apply-code-changes.md</component>
    </includes_components>
  </dependencies>
</command_file>