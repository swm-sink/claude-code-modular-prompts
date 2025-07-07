| version | last_updated | status |
|---------|--------------|--------|
| 1.0.0   | 2025-07-07   | stable |

# /session - AI session management via GitHub Issues

────────────────────────────────────────────────────────────────────────────────

```xml
<command purpose="AI session management via GitHub Issues for development tracking and coordination">
  
  <delegation target="modules/patterns/session-management.md">
    This command delegates ALL implementation to the session management module which provides comprehensive GitHub Issues integration for AI coding session tracking, progress updates, and team coordination.
  </delegation>
  
  <module_integration>
    <primary_module>modules/patterns/session-management.md</primary_module>
    <supporting_modules>
      <module>modules/patterns/git-operations.md</module>
      <module>modules/quality/production-standards.md</module>
    </supporting_modules>
  </module_integration>
  
  <usage_examples>
    <example type="start">/session start "Implement OAuth2 authentication"</example>
    <example type="update">/session update "Completed user model, starting auth middleware"</example>
    <example type="link">/session link 123</example>
    <example type="complete">/session complete successful</example>
    <example type="list">/session list active</example>
    <example type="view">/session view 123</example>
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