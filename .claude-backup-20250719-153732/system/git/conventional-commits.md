| version | last_updated | status |
|---------|--------------|--------|
| 1.0.0   | 2025-07-11   | stable |

# Conventional Commits Module

────────────────────────────────────────────────────────────────────────────────


────────────────────────────────────────────────────────────────────────────────

```xml
<module name="conventional_commits" category="git">
  
  <purpose>
    Generate standardized conventional commit messages with emojis for improved history readability and automated changelog generation.
  </purpose>
  
  <trigger_conditions>
    <condition type="automatic">All task/feature/swarm completions trigger commit message generation</condition>
    <condition type="explicit">User requests conventional commit format or git workflow patterns</condition>
  </trigger_conditions>
  
  <implementation>
    
    <phase name="change_analysis" order="1">
      <requirements>
        Git diff analyzed to determine change type and scope
        Files categorized by functional area (frontend, backend, docs, tests)
        Breaking changes identified from code analysis
      </requirements>
      <actions>
        Analyze git diff to classify changes: new features, bug fixes, refactoring, etc.
        Detect affected components from file paths and content changes
        Identify breaking changes from API modifications and dependency updates
        Extract scope from modified directories and functional areas
      </actions>
      <validation>
        Change type correctly identified (feat, fix, docs, style, refactor, perf, test, chore)
        Scope accurately reflects affected components
        Breaking changes properly flagged with technical justification
      </validation>
    </phase>
    
    <phase name="message_generation" order="2">
      <requirements>
        Commit message follows conventional format with appropriate emoji
        Header under 50 characters using imperative mood
        Body provides context for complex changes
        Footer includes breaking change notices and issue references
      </requirements>
      <actions>
        Generate header: type(scope): emoji description
        Create detailed body explaining rationale for non-trivial changes
        Add footer with breaking change details and issue links
        Include co-authorship attribution when requested
      </actions>
      <validation>
        Header follows format: type(scope): emoji description
        Message uses imperative mood ("add" not "adds" or "added")
        Breaking changes documented in footer with BREAKING CHANGE: prefix
        Character limits respected (50 for header, 72 for body lines)
      </validation>
    </phase>
    
  </implementation>
  
  <commit_types>
    <feat>
      <description>New feature for the user</description>
      <emoji>✨</emoji>
      <triggers>add, implement, create, introduce, new</triggers>
      <scope_detection>api, ui, auth, db, config, cli</scope_detection>
      <examples>
        feat(auth): ✨ add JWT token refresh mechanism
        feat(ui): ✨ implement dark mode toggle
      </examples>
    </feat>
    <fix>
      <description>Bug fix for the user</description>
      <emoji>🐛</emoji>
      <triggers>fix, resolve, correct, repair, patch</triggers>
      <scope_detection>api, ui, auth, db, security, performance</scope_detection>
      <examples>
        fix(auth): 🐛 resolve token expiration edge case
        fix(ui): 🐛 correct responsive layout on mobile
      </examples>
    </fix>
    <docs>
      <description>Documentation only changes</description>
      <emoji>📚</emoji>
      <triggers>document, update docs, add documentation, readme</triggers>
      <scope_detection>readme, api, guide, tutorial</scope_detection>
      <examples>
        docs(api): 📚 update authentication endpoints
        docs(readme): 📚 add installation instructions
      </examples>
    </docs>
    <style>
      <description>Changes that do not affect code meaning</description>
      <emoji>💎</emoji>
      <triggers>format, lint, style, whitespace, semicolon</triggers>
      <scope_detection>eslint, prettier, black, rustfmt</scope_detection>
      <examples>
        style(frontend): 💎 apply prettier formatting
        style(backend): 💎 fix linting violations
      </examples>
    </style>
    <refactor>
      <description>Code change that neither fixes bug nor adds feature</description>
      <emoji>♻️</emoji>
      <triggers>refactor, restructure, reorganize, clean up</triggers>
      <scope_detection>components, services, utils, models</scope_detection>
      <examples>
        refactor(auth): ♻️ extract token validation logic
        refactor(ui): ♻️ consolidate component state logic
      </examples>
    </refactor>
    <perf>
      <description>Code change that improves performance</description>
      <emoji>🚀</emoji>
      <triggers>optimize, performance, speed, cache, lazy</triggers>
      <scope_detection>api, db, ui, cache, bundle</scope_detection>
      <examples>
        perf(api): 🚀 add response caching for user data
        perf(ui): 🚀 implement component lazy loading
      </examples>
    </perf>
    <test>
      <description>Adding missing or correcting existing tests</description>
      <emoji>🧪</emoji>
      <triggers>test, spec, unit test, integration test</triggers>
      <scope_detection>unit, integration, e2e, api, ui</scope_detection>
      <examples>
        test(auth): 🧪 add JWT validation unit tests
        test(api): 🧪 improve error handling coverage
      </examples>
    </test>
    <chore>
      <description>Changes to build process or auxiliary tools</description>
      <emoji>🔧</emoji>
      <triggers>build, deps, config, tools, workflow</triggers>
      <scope_detection>deps, build, ci, tools, config</scope_detection>
      <examples>
        chore(deps): 🔧 update React to v18.2.0
        chore(ci): 🔧 add automated security scanning
      </examples>
    </chore>
  </commit_types>
  
  <scope_detection>
    <automatic_detection>
      <frontend>Detect from: src/components/, src/pages/, *.tsx, *.jsx, *.vue</frontend>
      <backend>Detect from: src/api/, src/services/, *.py, *.java, *.go, *.rs</backend>
      <database>Detect from: migrations/, src/models/, *.sql, schema.*</database>
      <auth>Detect from: auth/, authentication/, login/, jwt/, oauth/</auth>
      <docs>Detect from: README.md, docs/, *.md, docstrings</docs>
      <tests>Detect from: test/, spec/, __tests__/, *.test.*, *.spec.*</tests>
      <config>Detect from: config/, .env, package.json, requirements.txt</config>
      <ci>Detect from: .github/, .gitlab-ci.yml, Dockerfile, docker-compose.yml</ci>
    </automatic_detection>
    <manual_override>
      <rule>User can specify scope with --scope flag</rule>
      <rule>Multiple scopes supported: feat(api,ui): description</rule>
      <rule>No scope allowed for global changes: feat: description</rule>
    </manual_override>
  </scope_detection>
  
  <breaking_changes>
    <detection_patterns>
      <api_changes>Modified function signatures, removed endpoints, changed response formats</api_changes>
      <dependency_updates>Major version bumps in package.json, requirements.txt, go.mod</dependency_updates>
      <config_changes>Required environment variables, configuration file format changes</config_changes>
      <database_schema>Non-backward-compatible migrations, dropped columns/tables</database_schema>
    </detection_patterns>
    <footer_format>
      <template>
        BREAKING CHANGE: Description of what changed and impact
        
        Migration guide:
        - Step 1: Action required
        - Step 2: Additional step
        
        Closes #123
      </template>
    </footer_format>
  </breaking_changes>
  
  <co_authorship>
    <default_behavior>
      <include>Include Claude co-authorship by default for all commits</include>
      <format>Co-Authored-By: Claude &lt;noreply@anthropic.com&gt;</format>
    </default_behavior>
    <skip_options>
      <flag>--no-claude-author to skip co-authorship</flag>
      <flag>--solo for user-only attribution</flag>
      <automatic>Skip for trivial changes like formatting or typo fixes</automatic>
    </skip_options>
    <additional_authors>
      <support>Support for multiple co-authors</support>
      <format>Co-Authored-By: Name &lt;email@domain.com&gt;</format>
      <flag>--co-author "Name &lt;email&gt;" for additional authors</flag>
    </additional_authors>
  </co_authorship>
  
  <message_templates>
    <simple_feature>
      <format>feat(scope): ✨ description</format>
      <example>feat(auth): ✨ add password reset functionality</example>
    </simple_feature>
    <breaking_change>
      <format>
        feat(scope)!: ✨ description
        
        Detailed explanation of the change and its impact.
        
        BREAKING CHANGE: What specifically breaks and why
        
        Migration guide for users to update their code.
        
        Co-Authored-By: Claude &lt;noreply@anthropic.com&gt;
      </format>
    </breaking_change>
    <bug_fix>
      <format>
        fix(scope): 🐛 description
        
        Explanation of the bug and how it was fixed.
        Root cause analysis if complex.
        
        Fixes #issue-number
        
        Co-Authored-By: Claude &lt;noreply@anthropic.com&gt;
      </format>
    </bug_fix>
    <refactor>
      <format>
        refactor(scope): ♻️ description
        
        Explanation of what was refactored and why.
        Performance or maintainability benefits.
        
        Co-Authored-By: Claude &lt;noreply@anthropic.com&gt;
      </format>
    </refactor>
  </message_templates>
  
  <automation_integration>
    <task_completion>
      <trigger>After successful task completion via /task command</trigger>
      <behavior>Generate conventional commit with task context</behavior>
      <scope>Auto-detect from modified files and task description</scope>
    </task_completion>
    <feature_completion>
      <trigger>After feature completion via /feature command</trigger>
      <behavior>Generate comprehensive commit with feature summary</behavior>
      <breaking_changes>Analyze feature for breaking changes and document</breaking_changes>
    </feature_completion>
    <swarm_completion>
      <trigger>After swarm coordination completion</trigger>
      <behavior>Generate coordinated commit reflecting all agent contributions</behavior>
      <multi_scope>Include all affected scopes from different agents</multi_scope>
    </swarm_completion>
  </automation_integration>
  
  <quality_checks>
    <message_validation>
      <header_length>Maximum 50 characters for commit header</header_length>
      <body_wrapping>Wrap body lines at 72 characters</body_wrapping>
      <imperative_mood>Use imperative mood: "add" not "adds" or "added"</imperative_mood>
      <no_period>No trailing period in header</no_period>
    </message_validation>
    <content_validation>
      <meaningful_description>Reject generic messages like "fix bug" or "update code"</meaningful_description>
      <scope_accuracy>Verify scope matches actual file changes</scope_accuracy>
      <type_accuracy>Ensure commit type matches actual changes made</type_accuracy>
    </content_validation>
  </quality_checks>
  
  <changelog_integration>
    <automated_generation>
      <feature_sections>Group feat commits under "Features" section</feature_sections>
      <bug_sections>Group fix commits under "Bug Fixes" section</bug_sections>
      <breaking_sections>Highlight breaking changes prominently</breaking_sections>
      <scope_grouping>Sub-group by scope within each section</scope_grouping>
    </automated_generation>
    <version_bumping>
      <major>Increment for breaking changes (BREAKING CHANGE in footer)</major>
      <minor>Increment for new features (feat type)</minor>
      <patch>Increment for bug fixes (fix type)</patch>
      <skip>No version bump for docs, style, test, chore</skip>
    </version_bumping>
  </changelog_integration>
  
  <integration_points>
    <depends_on>
      patterns/git-operations.md for git workflow automation
      quality/production-standards.md for commit quality standards
    </depends_on>
    <provides_to>
      development/task-management.md for automated commit generation
      patterns/multi-agent.md for coordinated commit messaging
      All commands for standardized commit workflow
    </provides_to>
  </integration_points>
  
  <pattern_usage>
    <uses_pattern from="patterns/pattern-library.md">automated_workflows</uses_pattern>
    <uses_pattern from="patterns/pattern-library.md">quality_gates</uses_pattern>
    <implementation_notes>
      Automated commit generation follows quality_gates pattern for validation
      Integration with all commands uses automated_workflows for consistency
      Breaking change detection follows consequence_mapping for impact analysis
    </implementation_notes>
  </pattern_usage>
  
</module>
```