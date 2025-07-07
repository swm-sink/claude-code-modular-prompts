| version | last_updated | status |
|---------|--------------|--------|
| 1.0.0   | 2025-07-07   | stable |

# Git Operations Module

────────────────────────────────────────────────────────────────────────────────

```xml
<module name="git_operations" category="patterns">
  
  <purpose>
    Comprehensive git operation patterns for intelligent staging, conventional commits, release management, and automated workflows.
  </purpose>
  
  <trigger_conditions>
    <condition type="automatic">Commit creation, branch management, release operations, PR workflows</condition>
    <condition type="explicit">User requests git workflow patterns or repository operations</condition>
  </trigger_conditions>
  
  <implementation>
    
    <phase name="staging_intelligence" order="1">
      <requirements>
        Files intelligently selected based on commit type and content analysis
        Auto-exclude patterns enforced for temp files, cache, and build artifacts
        Staging coherence validated against commit description
      </requirements>
      <actions>
        Analyze git status and classify modified/untracked files by relevance
        Apply auto-include patterns for source files, configs, documentation, tests
        Exclude temporary files, cache directories, build artifacts, IDE files
        Validate staging makes logical sense for the intended commit type
      </actions>
      <validation>
        Staged files align with commit description and scope
        No temporary or inappropriate files included in staging
        Related files grouped together for atomic commits
      </validation>
    </phase>
    
    <phase name="conventional_commits" order="2">
      <requirements>
        Commit messages follow conventional commit format with proper classification
        Commit type automatically detected from description (feat, fix, docs, etc.)
        Scope detection based on affected components and keywords
      </requirements>
      <actions>
        Classify commit type using triggers: feat (add/implement), fix (resolve/correct), docs (document), refactor (restructure), etc.
        Auto-detect scope from keywords: api, auth, db, ui, test, docs, config
        Generate conventional commit with breaking change indicators if applicable
        Format header as type(scope): description with appropriate constraints
      </actions>
      <validation>
        Commit message follows conventional format with proper type classification
        Header under 50 characters using imperative mood without trailing period
        Breaking changes properly indicated with exclamation mark and footer
      </validation>
    </phase>
    
    <phase name="release_management" order="3">
      <requirements>
        Semantic versioning automation with changelog generation
        Version bumping based on conventional commit analysis
        Release workflow with tagging and deployment automation
      </requirements>
      <actions>
        Analyze commits since last version to determine bump type (major/minor/patch)
        Generate changelog entries grouped by type: features, fixes, breaking changes
        Update version files and create release commit with proper tagging
        Automate release workflow with push to remote and GitHub release creation
      </actions>
      <validation>
        Version correctly bumped based on conventional commit analysis
        Changelog accurately reflects changes with proper categorization
        Release commit and tag created with appropriate metadata
      </validation>
    </phase>
    
  </implementation>
  
  <commit_type_classification>
    <feat>
      <description>New feature for the user</description>
      <triggers>add, implement, create, introduce</triggers>
      <impact>minor_version_bump</impact>
    </feat>
    <fix>
      <description>Bug fix for the user</description>
      <triggers>fix, resolve, correct, repair</triggers>
      <impact>patch_version_bump</impact>
    </fix>
    <docs>
      <description>Documentation only changes</description>
      <triggers>document, update docs, add documentation</triggers>
      <impact>no_version_bump</impact>
    </docs>
    <refactor>
      <description>Code changes that neither fix a bug nor add a feature</description>
      <triggers>refactor, restructure, reorganize, clean up</triggers>
      <impact>patch_version_bump</impact>
    </refactor>
  </commit_type_classification>
  
  <branching_workflows>
    <feature_workflow>
      <naming_pattern>feature/{ticket-id}-{short-description}</naming_pattern>
      <source_branch>develop</source_branch>
      <target_branch>develop</target_branch>
      <requires_pr>true</requires_pr>
      <delete_after_merge>true</delete_after_merge>
    </feature_workflow>
    <hotfix_workflow>
      <naming_pattern>hotfix/{version}-{short-description}</naming_pattern>
      <source_branch>main</source_branch>
      <target_branch>main, develop</target_branch>
      <requires_pr>true</requires_pr>
      <immediate_deploy>true</immediate_deploy>
    </hotfix_workflow>
    <release_workflow>
      <naming_pattern>release/{version}</naming_pattern>
      <source_branch>develop</source_branch>
      <target_branch>main</target_branch>
      <requires_pr>true</requires_pr>
      <create_tag>true</create_tag>
    </release_workflow>
  </branching_workflows>
  
  <quality_integration>
    <pre_commit_checks>
      <linting>Language-specific linting: ruff/black for Python, eslint/prettier for JS/TS</linting>
      <type_checking>Type validation: mypy for Python, tsc for TypeScript</type_checking>
      <testing>Quick test execution: pytest -x for Python, npm test for Node.js</testing>
      <security>Security scanning: bandit for Python, npm audit for Node.js</security>
      <commit_validation>Conventional commit format and message length validation</commit_validation>
    </pre_commit_checks>
    <blocking_conditions>
      <condition>Linting errors present</condition>
      <condition>Type checking failures</condition>
      <condition>Test failures in affected areas</condition>
      <condition>Security vulnerabilities detected</condition>
      <condition>Commit message format invalid</condition>
    </blocking_conditions>
  </quality_integration>
  
  <pr_automation>
    <feature_template>
      <title_format>Feature: {description}</title_format>
      <sections>Summary, Type of Change, Testing, Checklist</sections>
      <labels>feature, needs-review</labels>
      <auto_reviewers>enabled</auto_reviewers>
    </feature_template>
    <bugfix_template>
      <title_format>Fix: {description}</title_format>
      <sections>Summary, Bug Description, Root Cause, Solution, Testing, Checklist</sections>
      <labels>bugfix, needs-review</labels>
      <auto_reviewers>enabled</auto_reviewers>
    </bugfix_template>
  </pr_automation>
  
  <session_integration>
    <complex_workflows>
      <triggers>Release management, major refactoring, multi-component changes</triggers>
      <documentation>Git strategy, branch management approach, release planning</documentation>
      <tracking>Git operation progress, quality gate results, release outcomes</tracking>
    </complex_workflows>
    <simple_operations>
      <scope>Single commits, straightforward PRs, minor fixes</scope>
      <approach>Direct execution without session overhead</approach>
    </simple_operations>
  </session_integration>
  
  <integration_points>
    <depends_on>
      patterns/tool-usage.md for efficient git command execution
      quality/production-standards.md for quality gate enforcement
    </depends_on>
    <provides_to>
      All commands for git workflow automation and repository management
      patterns/session-management.md for complex git workflow tracking
    </provides_to>
  </integration_points>
  
</module>
```