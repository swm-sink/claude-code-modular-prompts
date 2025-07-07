| version | last_updated | status |
|---------|--------------|--------|
| 1.0.0   | 2025-07-07   | stable |

# /commit - Intelligent git operations

────────────────────────────────────────────────────────────────────────────────

```xml
<command purpose="Intelligent git operations with automatic staging and conventional commits">
  
  <delegation target="modules/patterns/git-operations.md">
    This command delegates ALL implementation to the git operations module which provides comprehensive git workflow automation including conventional commits, intelligent staging, release management, and PR creation.
  </delegation>
  
  <module_integration>
    <primary_module>modules/patterns/git-operations.md</primary_module>
    <supporting_modules>
      <module>modules/quality/production-standards.md</module>
      <module>modules/patterns/session-management.md</module>
    </supporting_modules>
  </module_integration>
  
  <usage_examples>
    <example type="basic">/commit "Add user authentication"</example>
    <example type="scoped">/commit "Update user model" --scope api</example>
    <example type="breaking">/commit "Change API response format" --breaking</example>
    <example type="release">/commit --release minor --changelog</example>
    <example type="pr">/commit --pr "Feature: Add OAuth support"</example>
  </usage_examples>
  
  <reference>
    See modules/patterns/git-operations.md for complete implementation details including conventional commit patterns, automated staging, release workflows, and PR integration.
  </reference>
  
</command>
```