| version | last_updated | status |
|---------|--------------|--------|
| 1.1.0   | 2025-07-07   | stable |

# Git Operations Module

────────────────────────────────────────────────────────────────────────────────


────────────────────────────────────────────────────────────────────────────────

```xml
<module name="git_operations" category="patterns">
  
  <purpose>
    Comprehensive git operation patterns for intelligent staging, conventional commits, release management, git worktree workflows, and automated workflows.
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
    
    <phase name="worktree_management" order="4">
      <requirements>
        Efficient multi-branch management using git worktrees
        Automated worktree creation for feature/hotfix branches
        Context isolation between different work streams
        Automatic cleanup of completed worktrees
      </requirements>
      <actions>
        Create worktree for new feature/hotfix branches automatically
        Maintain separate working directories for concurrent development
        Synchronize worktree state with main repository
        Clean up worktrees after branch merge or abandonment
      </actions>
      <validation>
        Worktree created in appropriate directory structure
        No conflicts between concurrent worktree operations
        Proper cleanup after worktree lifecycle completion
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
  
  <git_worktree_patterns>
    <worktree_creation>
      <description>Automated worktree creation for parallel development</description>
      <implementation>
        ```bash
        # AUTOMATED WORKTREE CREATION PATTERN
        create_feature_worktree() {
          local branch_name="$1"
          local ticket_id="$2"
          local base_branch="${3:-develop}"
          
          # Standardized worktree directory structure
          local worktree_dir="../worktrees/${branch_name}"
          
          # Create worktree from base branch
          git worktree add -b "$branch_name" "$worktree_dir" "origin/$base_branch"
          
          # Initialize worktree environment
          cd "$worktree_dir"
          
          # Install dependencies if needed
          if [ -f "package.json" ]; then
            npm install
          elif [ -f "requirements.txt" ]; then
            python -m venv .venv
            source .venv/bin/activate
            pip install -r requirements.txt
          fi
          
          # Create initial commit for tracking
          git commit --allow-empty -m "feat: initialize $branch_name for $ticket_id"
          
          echo "✅ Worktree created: $worktree_dir"
          echo "📝 Branch: $branch_name"
          echo "🎯 Ticket: $ticket_id"
        }
        ```
      </implementation>
      <benefits>
        - Parallel development without stashing or context switching
        - Isolated environments for each feature/fix
        - Faster branch switching with pre-built dependencies
      </benefits>
    </worktree_creation>
    
    <worktree_management>
      <description>Intelligent worktree lifecycle management</description>
      <implementation>
        ```bash
        # WORKTREE LIFECYCLE MANAGEMENT
        manage_worktrees() {
          local action="$1"
          
          case "$action" in
            "list")
              # List all active worktrees with status
              git worktree list --porcelain | while read -r line; do
                if [[ $line =~ ^worktree ]]; then
                  local path="${line#worktree }"
                  local branch=$(cd "$path" 2>/dev/null && git branch --show-current)
                  local status=$(cd "$path" 2>/dev/null && git status --porcelain | wc -l)
                  echo "📁 $path"
                  echo "   Branch: $branch"
                  echo "   Uncommitted changes: $status"
                fi
              done
              ;;
              
            "clean")
              # Remove completed worktrees
              git worktree list --porcelain | while read -r line; do
                if [[ $line =~ ^worktree ]]; then
                  local path="${line#worktree }"
                  local branch=$(cd "$path" 2>/dev/null && git branch --show-current)
                  
                  # Check if branch is merged
                  if git branch -r --merged | grep -q "origin/$branch"; then
                    echo "🧹 Removing merged worktree: $path"
                    git worktree remove "$path"
                  fi
                fi
              done
              ;;
              
            "sync")
              # Sync all worktrees with remote
              git worktree list --porcelain | while read -r line; do
                if [[ $line =~ ^worktree ]]; then
                  local path="${line#worktree }"
                  echo "🔄 Syncing worktree: $path"
                  (cd "$path" && git fetch origin && git pull --rebase)
                fi
              done
              ;;
          esac
        }
        ```
      </implementation>
      <automation>
        - Automatic cleanup of merged worktrees
        - Sync all worktrees with remote changes
        - Status monitoring across all active worktrees
      </automation>
    </worktree_management>
    
    <worktree_workflows>
      <concurrent_development>
        <description>Efficient concurrent feature development using worktrees</description>
        <pattern>
          ```bash
          # CONCURRENT FEATURE DEVELOPMENT
          develop_features_concurrently() {
            local features=("$@")
            
            for feature in "${features[@]}"; do
              local branch_name="feature/$feature"
              local worktree_dir="../worktrees/$feature"
              
              # Create worktree for each feature
              git worktree add -b "$branch_name" "$worktree_dir" origin/develop
              
              # Open in separate terminal/IDE instance
              echo "🚀 Feature worktree ready: $worktree_dir"
              echo "   Run: cd $worktree_dir && code ."
            done
          }
          ```
        </pattern>
        <use_cases>
          - Developing multiple features simultaneously
          - Quick context switching between tasks
          - Isolated testing environments
        </use_cases>
      </concurrent_development>
      
      <hotfix_isolation>
        <description>Emergency hotfix development without disrupting current work</description>
        <pattern>
          ```bash
          # HOTFIX WORKTREE PATTERN
          create_hotfix_worktree() {
            local version="$1"
            local description="$2"
            local branch_name="hotfix/$version-$description"
            local worktree_dir="../worktrees/hotfix-$version"
            
            # Create hotfix worktree from main
            git worktree add -b "$branch_name" "$worktree_dir" origin/main
            
            cd "$worktree_dir"
            
            # Apply hotfix
            echo "🚨 Hotfix worktree created: $worktree_dir"
            echo "📌 Branch: $branch_name"
            echo "⚡ Ready for emergency fix"
            
            # After fix is complete and tested
            git push -u origin "$branch_name"
            gh pr create --base main --title "Hotfix: $description" --label "hotfix,urgent"
          }
          ```
        </pattern>
        <benefits>
          - No need to stash current work
          - Immediate hotfix capability
          - Clean separation from feature development
        </benefits>
      </hotfix_isolation>
      
      <review_worktrees>
        <description>Dedicated worktrees for code review</description>
        <pattern>
          ```bash
          # CODE REVIEW WORKTREE
          create_review_worktree() {
            local pr_number="$1"
            local pr_info=$(gh pr view "$pr_number" --json headRefName,baseRefName)
            local branch=$(echo "$pr_info" | jq -r .headRefName)
            local base=$(echo "$pr_info" | jq -r .baseRefName)
            local worktree_dir="../worktrees/review-pr-$pr_number"
            
            # Create review worktree
            git fetch origin "pull/$pr_number/head:pr-$pr_number"
            git worktree add "$worktree_dir" "pr-$pr_number"
            
            cd "$worktree_dir"
            
            # Set up for review
            echo "👀 Review worktree created: $worktree_dir"
            echo "🔍 PR #$pr_number: $branch → $base"
            echo "📋 Run tests and review changes"
          }
          ```
        </pattern>
        <advantages>
          - Review PRs without affecting current work
          - Run full test suites on PR code
          - Easy comparison with base branch
        </advantages>
      </review_worktrees>
    </worktree_workflows>
    
    <worktree_best_practices>
      <directory_structure>
        ```
        project/
        ├── main/                    # Main repository
        └── worktrees/              # All worktrees
            ├── feature-auth/       # Feature worktree
            ├── feature-api/        # Another feature
            ├── hotfix-2.1.1/      # Hotfix worktree
            └── review-pr-123/     # PR review worktree
        ```
      </directory_structure>
      <naming_conventions>
        <feature>../worktrees/feature-{description}</feature>
        <hotfix>../worktrees/hotfix-{version}</hotfix>
        <release>../worktrees/release-{version}</release>
        <review>../worktrees/review-pr-{number}</review>
      </naming_conventions>
      <cleanup_policy>
        <merged_branches>Remove worktree within 24 hours of merge</merged_branches>
        <abandoned_branches>Clean up after 7 days of inactivity</abandoned_branches>
        <review_worktrees>Remove after PR is closed</review_worktrees>
      </cleanup_policy>
    </worktree_best_practices>
    
    <worktree_automation>
      <hooks_integration>
        ```bash
        # POST-MERGE HOOK FOR WORKTREE CLEANUP
        #!/bin/bash
        # .git/hooks/post-merge
        
        # Clean up merged worktrees automatically
        current_branch=$(git branch --show-current)
        
        git worktree list --porcelain | while read -r line; do
          if [[ $line =~ ^worktree ]]; then
            path="${line#worktree }"
            branch=$(cd "$path" 2>/dev/null && git branch --show-current)
            
            if [ "$branch" = "$current_branch" ] && [ "$path" != "$(pwd)" ]; then
              echo "🧹 Cleaning up merged worktree: $path"
              git worktree remove "$path"
            fi
          fi
        done
        ```
      </hooks_integration>
      <ci_integration>
        <parallel_testing>Run tests in multiple worktrees simultaneously</parallel_testing>
        <build_isolation>Separate build artifacts per worktree</build_isolation>
        <deployment_staging>Use worktrees for deployment staging</deployment_staging>
      </ci_integration>
    </worktree_automation>
  </git_worktree_patterns>
  
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