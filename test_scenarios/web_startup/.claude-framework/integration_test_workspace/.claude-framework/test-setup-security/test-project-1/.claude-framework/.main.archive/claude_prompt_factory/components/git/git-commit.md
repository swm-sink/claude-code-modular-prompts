<prompt_component>
  <step name="Intelligent Git Commit Management">
    <description>
Advanced git commit workflow with intelligent message generation, change analysis, and commit organization. Automatically analyzes code changes, generates meaningful commit messages, and ensures proper commit hygiene following conventional commit standards.
    </description>
  </step>

  <git_commit>
    <change_analysis>
      <semantic_analysis>
        <!-- Analyze the nature and scope of changes -->
        <change_classification>
          - Feature additions and new functionality
          - Bug fixes and issue resolutions
          - Refactoring and code improvements
          - Documentation updates and corrections
          - Configuration and build system changes
          - Test additions and improvements
        </change_classification>
        
        <impact_assessment>
          - Breaking changes detection and documentation
          - Scope of affected components and modules
          - Dependencies and integration impact analysis
          - Performance and security implications
        </impact_assessment>
      </semantic_analysis>
      
      <staging_optimization>
        <!-- Intelligent staging of related changes -->
        <logical_grouping>
          Group related changes into coherent commits:
          - Atomic commits for single logical changes
          - Separate commits for different concerns
          - Proper separation of refactoring and features
          - Documentation commits when substantial
        </logical_grouping>
        
        <staging_recommendations>
          - Suggest optimal file groupings for commits
          - Identify changes that should be separate commits
          - Recommend commit splitting strategies
          - Detect accidental inclusions or exclusions
        </staging_recommendations>
      </staging_optimization>
    </change_analysis>
    
    <message_generation>
      <conventional_commits>
        <!-- Generate conventional commit messages -->
        <format_structure>
          type(scope): description
          
          [optional body]
          
          [optional footer(s)]
        </format_structure>
        
        <type_detection>
          Automatically detect commit type:
          - feat: new features
          - fix: bug fixes
          - docs: documentation changes
          - style: formatting, missing semicolons, etc.
          - refactor: code refactoring
          - test: adding missing tests
          - chore: maintenance tasks
        </type_detection>
        
        <scope_identification>
          Identify affected scope:
          - Component or module names
          - Feature areas or subsystems
          - Configuration or build targets
          - Documentation sections
        </scope_identification>
      </conventional_commits>
      
      <message_quality>
        <!-- Ensure high-quality commit messages -->
        <description_guidelines>
          - Use imperative mood ("add" not "added")
          - Be concise but descriptive
          - Explain what and why, not how
          - Reference issues or tickets when applicable
        </description_guidelines>
        
        <body_content>
          Include additional context when needed:
          - Motivation for the change
          - Contrast with previous behavior
          - Side effects or implications
          - Links to relevant documentation
        </body_content>
      </message_quality>
    </message_generation>
    
    <commit_validation>
      <pre_commit_checks>
        <!-- Validate commit quality before committing -->
        <code_quality>
          - Linting and code style validation
          - Test execution and coverage checks
          - Security vulnerability scanning
          - Documentation completeness verification
        </code_quality>
        
        <commit_hygiene>
          - No merge conflict markers
          - No debug code or console logs
          - No sensitive information exposure
          - Proper file permissions and line endings
        </commit_hygiene>
      </pre_commit_checks>
    </commit_validation>
  </git_commit>

  <o>
Git commit completed with intelligent analysis and conventional message generation:

**Commit Type:** [type] detected based on change analysis
**Scope:** [scope] identified from affected components
**Message Quality:** [0-100] conventional commit compliance score
**Files Staged:** [count] files logically grouped for atomic commit
**Pre-commit Checks:** All validation checks passed
**Commit Hash:** [hash] successfully created
  </o>
</prompt_component> 