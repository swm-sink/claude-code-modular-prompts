<prompt_component>
  <step name="Intelligent Git Merge Management">
    <description>
Advanced git merge workflow with conflict resolution, merge strategy optimization, and integration validation. Automatically analyzes branch differences, selects optimal merge strategies, and provides intelligent conflict resolution assistance.
    </description>
  </step>

  <git_merge>
    <merge_analysis>
      <branch_comparison>
        <!-- Analyze branches before merging -->
        <divergence_analysis>
          - Number of commits ahead/behind
          - Files modified in each branch
          - Potential conflict identification
          - Semantic change overlap detection
        </divergence_analysis>
        
        <compatibility_assessment>
          - Breaking change detection
          - API compatibility validation
          - Dependency conflict identification
          - Test compatibility verification
        </compatibility_assessment>
      </branch_comparison>
      
      <strategy_selection>
        <!-- Choose optimal merge strategy -->
        <merge_strategies>
          - Fast-forward: When possible for clean history
          - No-fast-forward: For feature integration tracking
          - Squash: For cleaning up feature branch history
          - Rebase: For linear history maintenance
        </merge_strategies>
        
        <strategy_recommendations>
          Based on branch analysis:
          - Project workflow preferences
          - Change complexity and scope
          - Team collaboration patterns
          - Release and versioning strategy
        </strategy_recommendations>
      </strategy_selection>
    </merge_analysis>
    
    <conflict_resolution>
      <conflict_detection>
        <!-- Identify and categorize merge conflicts -->
        <conflict_types>
          - Content conflicts in source files
          - Binary file conflicts
          - Rename and move conflicts
          - Deletion vs modification conflicts
        </conflict_types>
        
        <conflict_complexity>
          - Simple text conflicts (easily resolvable)
          - Complex logical conflicts (requiring review)
          - Structural conflicts (file organization)
          - Semantic conflicts (code behavior changes)
        </conflict_complexity>
      </conflict_detection>
      
      <resolution_assistance>
        <!-- Provide intelligent conflict resolution help -->
        <automated_resolution>
          - Auto-resolve simple formatting conflicts
          - Apply consistent style preferences
          - Resolve trivial import/include ordering
          - Handle whitespace and newline conflicts
        </automated_resolution>
        
        <manual_guidance>
          - Highlight conflicting sections with context
          - Suggest resolution strategies
          - Provide side-by-side comparison
          - Recommend testing after resolution
        </manual_guidance>
      </resolution_assistance>
    </conflict_resolution>
    
    <integration_validation>
      <post_merge_verification>
        <!-- Validate successful integration -->
        <automated_testing>
          - Run full test suite after merge
          - Verify build and compilation success
          - Check for integration test failures
          - Validate deployment compatibility
        </automated_testing>
        
        <quality_checks>
          - Code quality metric verification
          - Security vulnerability scanning
          - Performance regression detection
          - Documentation consistency validation
        </quality_checks>
      </post_merge_verification>
    </integration_validation>
  </git_merge>

  <o>
Git merge completed with intelligent conflict resolution and validation:

**Merge Strategy:** [strategy] selected based on branch analysis
**Conflicts Resolved:** [count] conflicts automatically and manually resolved
**Integration Status:** [success/warning/failure] with detailed validation results
**Test Results:** [count] tests passed, [count] failed (if any)
**Quality Score:** [0-100] post-merge code quality rating
**Merge Commit:** [hash] successfully created with proper merge message
  </o>
</prompt_component> 