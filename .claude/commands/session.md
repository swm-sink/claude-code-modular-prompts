| version | last_updated | status |
|---------|--------------|--------|
| 2.3.1   | 2025-07-08   | stable |

# /session - AI session management via GitHub Issues

────────────────────────────────────────────────────────────────────────────────

```xml
<command purpose="AI session management via GitHub Issues with context preservation">
  
  <delegation target="modules/patterns/session-management.md">
    Create issue → Track progress → Update status → Link artifacts → Complete with summary
  </delegation>
  
  <thinking_pattern enforcement="MANDATORY">
    <step>1. Determine session type (start/update/complete/view)</step>
    <step>2. For start: Create GitHub issue with AI template</step>
    <step>3. For update: Add progress comment with context</step>
    <step>4. For complete: Summarize outcomes and lessons learned</step>
    <step>5. Auto-link commits, PRs, and related issues</step>
    <step>6. Preserve context for /protocol resumption</step>
    <step>7. Apply labels (ai-session, active, completed)</step>
  </thinking_pattern>
  
  <module_integration>
    <primary_module>modules/patterns/session-management.md</primary_module>
    <supporting_modules>
      <module>modules/patterns/git-operations.md for commit linking</module>
      <module>modules/quality/production-standards.md for compliance tracking</module>
      <module>modules/patterns/multi-agent.md for swarm coordination</module>
    </supporting_modules>
  </module_integration>
  
  <usage_examples>
    <example type="start">/session start "Implement OAuth2 authentication" # Creates #124</example>
    <example type="update">/session update "Completed user model, TDD tests passing"</example>
    <example type="link">/session link PR-456 # Links PR to current session</example>
    <example type="complete">/session complete "OAuth2 fully implemented with 95% coverage"</example>
    <example type="view">/session view 123 # Shows full session history</example>
  </usage_examples>
  
  <github_integration>
    <feature>Creates GitHub issues with AI session template</feature>
    <feature>Manages labels programmatically (ai-session, active, completed)</feature>
    <feature>Links commits and PRs automatically</feature>
    <feature>Provides searchable session history</feature>
    <feature>Zero external dependencies - pure GitHub CLI</feature>
  </github_integration>
  
  <strict_enforcement target="session_tracking">
    <primary_rule>Multi-agent work MUST use session tracking for coordination</primary_rule>
    <verification>Complex tasks automatically prompt for session creation</verification>
    <consequence>Session-less multi-agent work creates coordination failures</consequence>
  </strict_enforcement>
  
  <reference>
    See modules/patterns/session-management.md for complete implementation details including GitHub CLI operations, session templates, workflow integration, and team coordination patterns.
  </reference>
  
  <pattern_usage>
    • Implements issue_tracking pattern from pattern-library.md
    • Uses explicit_validation for session operations
    • Applies single_responsibility pattern
    • Leverages graceful_degradation for error handling
    
    See modules/patterns/pattern-library.md for pattern details
    See modules/patterns/session-management.md for full implementation
  </pattern_usage>
  
</command>
```