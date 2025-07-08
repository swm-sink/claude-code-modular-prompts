| version | last_updated | status |
|---------|--------------|--------|
| 1.0.0   | 2025-01-08   | stable |

# PR Review Automation Module

────────────────────────────────────────────────────────────────────────────────

```xml
<module name="code_review" category="development">
  
  <purpose>
    Automate PR review process with 50% faster reviews and 90% issue detection through automated checks, intelligent review templates, and comprehensive quality validation.
  </purpose>
  
  <trigger_conditions>
    <condition type="automatic">After feature/swarm completion when creating pull requests</condition>
    <condition type="explicit">User requests code review automation or PR quality checks</condition>
    <condition type="ci_integration">Automated PR creation triggers review workflow</condition>
  </trigger_conditions>
  
  <implementation>
    
    <phase name="automated_check_execution" order="1">
      <requirements>
        All quality checks executed automatically on PR creation
        Results captured with detailed error descriptions and fix suggestions
        Check status clearly communicated with pass/fail indicators
        Integration with existing CI/CD pipeline for consistency
      </requirements>
      <actions>
        Execute code style compliance checks using language-specific linters
        Run type checking for statically typed languages (TypeScript, Python, Rust)
        Perform security vulnerability scanning for code and dependencies
        Validate test coverage and ensure new code meets coverage requirements
        Check performance regression against baseline benchmarks
        Verify documentation completeness for public APIs and significant changes
      </actions>
      <validation>
        All automated checks completed with clear pass/fail status
        Detailed results available with specific file locations and fix suggestions
        Security scan results categorized by severity with remediation guidance
        Coverage reports show impact of changes on overall project coverage
      </validation>
    </phase>
    
    <phase name="review_template_generation" order="2">
      <requirements>
        Intelligent PR template generated based on change analysis
        Template includes relevant sections for type of changes made
        Automated checklist items populated based on modified files
        Links to relevant documentation and design decisions included
      </requirements>
      <actions>
        Analyze changed files to determine PR category (feature, fix, refactor, docs)
        Generate appropriate template sections based on change type
        Populate checklist with relevant items for modified components
        Include links to related issues, documentation, and design decisions
        Add testing guidance specific to the changes made
      </actions>
      <validation>
        Template accurately reflects the type and scope of changes
        All relevant checklist items included for comprehensive review
        Links and references are valid and helpful for reviewers
        Template encourages thorough review without being overly verbose
      </validation>
    </phase>
    
    <phase name="quality_validation" order="3">
      <requirements>
        Comprehensive validation of code quality standards
        Performance impact assessment with benchmarking
        Security review with threat analysis for changes
        Architecture compliance validation against project standards
      </requirements>
      <actions>
        Validate code follows established patterns and conventions
        Assess performance impact using automated benchmarking
        Review security implications of changes with threat modeling
        Check architectural compliance and design principle adherence
        Verify error handling and edge case coverage
      </actions>
      <validation>
        Code quality meets or exceeds project standards
        Performance impact documented and within acceptable limits
        Security review completed with no high-severity issues
        Architecture compliance verified against established patterns
      </validation>
    </phase>
    
    <phase name="review_guidance" order="4">
      <requirements>
        Clear guidance provided for human reviewers
        Focus areas highlighted based on change analysis
        Risk assessment included with mitigation strategies
        Estimated review time provided based on change complexity
      </requirements>
      <actions>
        Generate review focus areas based on change impact analysis
        Highlight high-risk changes requiring special attention
        Provide context on business logic changes and their implications
        Estimate review time based on change complexity and type
        Include suggestions for testing and validation approaches
      </actions>
      <validation>
        Review guidance is relevant and actionable
        Risk areas clearly identified with appropriate context
        Review time estimates are realistic and helpful for planning
        Testing suggestions are practical and comprehensive
      </validation>
    </phase>
    
  </implementation>
  
  <automated_checks>
    <code_quality>
      <linting>
        <javascript_typescript>ESLint with TypeScript rules, Prettier formatting</javascript_typescript>
        <python>Ruff for linting, Black for formatting, isort for imports</python>
        <rust>Clippy for linting, rustfmt for formatting</rust>
        <go>golangci-lint for comprehensive linting, gofmt for formatting</go>
        <blocking_conditions>Error-level lint violations, security rule violations</blocking_conditions>
      </linting>
      
      <complexity_analysis>
        <cyclomatic_complexity>Flag functions with complexity > 10</cyclomatic_complexity>
        <cognitive_complexity>Flag functions with cognitive load > 15</cognitive_complexity>
        <file_size>Flag files > 300 lines for potential refactoring</file_size>
        <function_length>Flag functions > 50 lines for review</function_length>
      </complexity_analysis>
      
      <code_patterns>
        <anti_patterns>Detect and flag common anti-patterns for the language</anti_patterns>
        <best_practices>Verify adherence to established team coding standards</best_practices>
        <consistency>Check consistency with existing codebase patterns</consistency>
        <maintainability>Assess code maintainability and technical debt</maintainability>
      </code_patterns>
    </code_quality>
    
    <security_validation>
      <vulnerability_scanning>
        <dependency_audit>Scan for known vulnerabilities in dependencies</dependency_audit>
        <code_analysis>Static analysis for security vulnerabilities</code_analysis>
        <secret_detection>Scan for accidentally committed secrets or keys</secret_detection>
        <injection_vulnerabilities>Check for SQL injection, XSS, and similar issues</injection_vulnerabilities>
      </vulnerability_scanning>
      
      <security_patterns>
        <authentication>Verify proper authentication and authorization patterns</authentication>
        <data_validation>Check input validation and sanitization</data_validation>
        <encryption>Verify proper encryption and hashing usage</encryption>
        <access_control>Review access control implementation</access_control>
      </security_patterns>
      
      <compliance_checks>
        <data_privacy>Check for GDPR, CCPA compliance requirements</data_privacy>
        <audit_trails>Verify audit logging for sensitive operations</audit_trails>
        <secure_defaults>Ensure secure configuration defaults</secure_defaults>
        <principle_least_privilege>Verify minimal permission assignments</principle_least_privilege>
      </compliance_checks>
    </security_validation>
    
    <performance_analysis>
      <benchmark_comparison>
        <response_times>Compare API response times against baseline</response_times>
        <memory_usage>Monitor memory consumption patterns</memory_usage>
        <cpu_utilization>Track CPU usage for algorithmic changes</cpu_utilization>
        <database_queries>Analyze query performance and N+1 patterns</database_queries>
      </benchmark_comparison>
      
      <scalability_assessment>
        <load_testing>Automated load testing for performance-critical changes</load_testing>
        <concurrency>Test concurrent access patterns</concurrency>
        <resource_limits>Verify resource usage stays within limits</resource_limits>
        <caching_efficiency>Assess caching strategy effectiveness</caching_efficiency>
      </scalability_assessment>
      
      <optimization_opportunities>
        <algorithm_efficiency>Identify potential algorithm improvements</algorithm_efficiency>
        <data_structure_usage>Review data structure choices for efficiency</data_structure_usage>
        <network_calls>Optimize external API calls and reduce round trips</network_calls>
        <bundling_optimization>For frontend: bundle size and loading performance</bundling_optimization>
      </optimization_opportunities>
    </performance_analysis>
    
    <test_validation>
      <coverage_analysis>
        <line_coverage>Ensure new code has >90% line coverage</line_coverage>
        <branch_coverage>Verify >85% branch coverage for new code</branch_coverage>
        <critical_path_coverage>100% coverage for business-critical functionality</critical_path_coverage>
        <regression_protection>Ensure adequate tests prevent regression</regression_protection>
      </coverage_analysis>
      
      <test_quality>
        <test_independence>Verify tests don't depend on each other</test_independence>
        <assertion_quality>Check for meaningful assertions vs simple existence checks</assertion_quality>
        <edge_case_coverage>Verify edge cases and error conditions are tested</edge_case_coverage>
        <mock_usage>Review mock usage for appropriate isolation</mock_usage>
      </test_quality>
      
      <integration_testing>
        <api_testing>Verify API contract testing for changed endpoints</api_testing>
        <database_testing>Check database interaction testing</database_testing>
        <external_service_testing>Mock external services appropriately</external_service_testing>
        <end_to_end_testing>Ensure critical user flows are tested</end_to_end_testing>
      </integration_testing>
    </test_validation>
  </automated_checks>
  
  <review_templates>
    <feature_pr_template>
      <title_format>feat(scope): Brief description of the feature</title_format>
      <template>
        ## 🎯 Feature Summary
        
        ### What's New
        [Brief description of the feature and its business value]
        
        ### Changes Made
        - [ ] **Frontend**: [Specific UI/UX changes]
        - [ ] **Backend**: [API endpoints, business logic changes]
        - [ ] **Database**: [Schema changes, migrations]
        - [ ] **Infrastructure**: [Deployment, configuration changes]
        
        ## 🧪 Testing Strategy
        
        ### Test Coverage
        - [ ] Unit tests added/updated (coverage: X%)
        - [ ] Integration tests cover new functionality
        - [ ] E2E tests validate user workflows
        - [ ] Performance tests verify scalability
        
        ### Manual Testing
        - [ ] Feature tested in development environment
        - [ ] Edge cases and error scenarios validated
        - [ ] Cross-browser/device testing completed
        - [ ] Accessibility requirements verified
        
        ## 🔒 Security & Performance
        
        ### Security Review
        - [ ] No sensitive data exposed in logs/responses
        - [ ] Authentication/authorization properly implemented
        - [ ] Input validation and sanitization in place
        - [ ] Dependencies scanned for vulnerabilities
        
        ### Performance Impact
        - [ ] Response times within acceptable limits (&lt;200ms p95)
        - [ ] Memory usage optimized and monitored
        - [ ] Database queries optimized (no N+1 issues)
        - [ ] Frontend bundle size impact assessed
        
        ## 📋 Review Checklist
        
        ### Code Quality
        - [ ] Code follows project conventions and patterns
        - [ ] Functions are small, focused, and well-named
        - [ ] Complex logic is documented and explained
        - [ ] Error handling is comprehensive and appropriate
        
        ### Documentation
        - [ ] README updated if installation/setup changed
        - [ ] API documentation updated for new endpoints
        - [ ] Architecture decisions documented
        - [ ] Migration guide provided if breaking changes
        
        ### Deployment
        - [ ] Feature flags configured if needed
        - [ ] Environment variables documented
        - [ ] Backward compatibility maintained
        - [ ] Rollback plan documented
        
        ## 🔗 Related Links
        
        - **Issue**: #[issue-number]
        - **Design Doc**: [link if applicable]
        - **Figma/Mockups**: [link if applicable]
        - **Dependencies**: [related PRs]
        
        ## 🎬 Demo
        
        [Screenshots, GIFs, or video demonstrating the feature]
        
        ---
        
        **Estimated Review Time**: [X] minutes
        **Risk Level**: [Low/Medium/High]
        **Breaking Changes**: [Yes/No]
      </template>
    </feature_pr_template>
    
    <bugfix_pr_template>
      <title_format>fix(scope): Brief description of the bug fix</title_format>
      <template>
        ## 🐛 Bug Fix Summary
        
        ### Issue Description
        **Problem**: [What was broken or not working correctly]
        **Impact**: [Who was affected and how]
        **Severity**: [Critical/High/Medium/Low]
        
        ### Root Cause Analysis
        **Cause**: [Technical explanation of why the bug occurred]
        **Location**: [File and line number where issue existed]
        **How it manifested**: [Symptoms users experienced]
        
        ## 🔧 Solution Implemented
        
        ### Changes Made
        - [ ] **Core Fix**: [Primary change that resolves the issue]
        - [ ] **Additional Changes**: [Supporting changes, refactoring]
        - [ ] **Prevention**: [Changes to prevent similar issues]
        
        ### Fix Strategy
        [Explanation of the approach taken and why]
        
        ## 🧪 Testing & Verification
        
        ### Reproduction Test
        - [ ] Added test that reproduces the original bug
        - [ ] Verified test fails before fix and passes after fix
        - [ ] Test covers edge cases and boundary conditions
        
        ### Regression Testing
        - [ ] All existing tests continue to pass
        - [ ] No new functionality broken by the fix
        - [ ] Performance impact assessed and acceptable
        
        ### Manual Verification
        - [ ] Bug reproduction steps no longer produce error
        - [ ] Fix tested in development environment
        - [ ] Edge cases manually validated
        
        ## 📋 Review Checklist
        
        ### Fix Quality
        - [ ] Fix addresses root cause, not just symptoms
        - [ ] Solution is minimal and surgical
        - [ ] No over-engineering or unnecessary changes
        - [ ] Error handling improved if relevant
        
        ### Risk Assessment
        - [ ] Change scope is minimal and well-contained
        - [ ] No impact on unrelated functionality
        - [ ] Backward compatibility maintained
        - [ ] Safe to deploy with current rollback plan
        
        ## 🔗 Related Information
        
        - **Original Issue**: #[issue-number]
        - **Bug Report**: [link to bug report]
        - **Related PRs**: [any dependent/related changes]
        - **Documentation Updates**: [if any]
        
        ---
        
        **Estimated Review Time**: [X] minutes
        **Risk Level**: [Low/Medium/High] 
        **Hotfix Candidate**: [Yes/No]
      </template>
    </bugfix_pr_template>
    
    <refactor_pr_template>
      <title_format>refactor(scope): Brief description of refactoring</title_format>
      <template>
        ## ♻️ Refactoring Summary
        
        ### Motivation
        **Why**: [Reason for refactoring - technical debt, performance, maintainability]
        **Benefits**: [Expected improvements from this refactoring]
        **Scope**: [What parts of the system are affected]
        
        ### Changes Made
        - [ ] **Code Structure**: [Architectural or organizational changes]
        - [ ] **Performance**: [Optimizations and efficiency improvements]
        - [ ] **Maintainability**: [Code clarity and design improvements]
        - [ ] **Technical Debt**: [Debt reduction and pattern improvements]
        
        ## 🎯 Refactoring Objectives
        
        ### Primary Goals
        - [ ] [Specific objective 1 with measurable outcome]
        - [ ] [Specific objective 2 with measurable outcome]
        - [ ] [Specific objective 3 with measurable outcome]
        
        ### Success Metrics
        - **Performance**: [Specific improvements expected]
        - **Maintainability**: [Code quality metrics]
        - **Technical Debt**: [Debt reduction measurements]
        
        ## 🧪 Validation Strategy
        
        ### Behavior Preservation
        - [ ] All existing tests pass without modification
        - [ ] No changes to public APIs or interfaces
        - [ ] Identical input/output behavior verified
        - [ ] Performance benchmarks show improvement/no regression
        
        ### Quality Verification
        - [ ] Code complexity metrics improved
        - [ ] Test coverage maintained or improved
        - [ ] Documentation updated for significant changes
        - [ ] Architecture consistency verified
        
        ## 📋 Review Focus Areas
        
        ### Code Quality
        - [ ] Design patterns properly implemented
        - [ ] SOLID principles better adhered to
        - [ ] Code duplication eliminated
        - [ ] Naming and structure improved
        
        ### Risk Assessment
        - [ ] No behavioral changes introduced
        - [ ] Refactoring scope is appropriate and manageable
        - [ ] Safe to deploy with minimal risk
        - [ ] Rollback plan available if needed
        
        ## 📊 Impact Analysis
        
        ### Before/After Comparison
        [Metrics showing improvement: complexity, performance, etc.]
        
        ### Technical Debt Reduction
        [Specific debt items addressed and resolved]
        
        ---
        
        **Estimated Review Time**: [X] minutes
        **Risk Level**: [Low/Medium/High]
        **Performance Impact**: [Positive/Neutral/Monitored]
      </template>
    </refactor_pr_template>
  </review_templates>
  
  <review_guidance>
    <focus_area_generation>
      <change_impact_analysis>
        <high_risk_changes>Database schema, security logic, performance-critical code</high_risk_changes>
        <integration_points>API changes, external service integrations, data flow modifications</integration_points>
        <business_logic>Core business rules, calculation logic, workflow changes</business_logic>
        <user_interface>User experience flows, accessibility, responsive design</user_interface>
      </change_impact_analysis>
      
      <reviewer_guidance>
        <focus_areas>
          [Generated based on changed files and risk analysis]
          - Pay special attention to [specific area] due to [reason]
          - Verify [specific functionality] works as expected
          - Check for potential [specific risk] in [file/function]
        </focus_areas>
        
        <testing_suggestions>
          [Generated based on change type and scope]
          - Test [specific scenario] to verify [expected behavior]
          - Validate edge case: [specific condition]
          - Performance test: [specific metric] under [conditions]
        </testing_suggestions>
        
        <review_priorities>
          [Ordered by impact and risk]
          1. **High Priority**: [Critical areas requiring thorough review]
          2. **Medium Priority**: [Important areas needing attention]
          3. **Low Priority**: [Areas that can be reviewed quickly]
        </review_priorities>
      </reviewer_guidance>
    </focus_area_generation>
    
    <time_estimation>
      <complexity_factors>
        <change_size>Lines of code added/modified/deleted</change_size>
        <file_count>Number of files affected</file_count>
        <component_diversity>Frontend, backend, database, infrastructure changes</component_diversity>
        <business_logic_complexity>Complexity of business rules and logic</business_logic_complexity>
      </complexity_factors>
      
      <estimation_algorithm>
        <base_time>5 minutes for basic PR setup and overview</base_time>
        <code_review_time>2 minutes per changed file + 0.5 minutes per 10 lines</code_review_time>
        <testing_review_time>3 minutes per test file + complexity multiplier</testing_review_time>
        <documentation_time>2 minutes per documentation file</documentation_time>
        <complexity_multiplier>1.5x for high complexity, 1.2x for medium complexity</complexity_multiplier>
      </estimation_algorithm>
      
      <time_categories>
        <quick_review>Under 15 minutes - Simple changes, clear context</quick_review>
        <standard_review>15-45 minutes - Typical feature or bug fix</standard_review>
        <thorough_review>45-90 minutes - Complex changes, multiple components</thorough_review>
        <comprehensive_review>90+ minutes - Major features, architecture changes</comprehensive_review>
      </time_categories>
    </time_estimation>
  </review_guidance>
  
  <quality_gates>
    <blocking_conditions>
      <critical_failures>
        <condition>Security vulnerabilities rated High or Critical</condition>
        <condition>Test coverage below 90% for new code</condition>
        <condition>Performance regression > 20% in critical paths</condition>
        <condition>Linting errors or compilation failures</condition>
        <condition>Breaking changes without migration plan</condition>
      </critical_failures>
      
      <warning_conditions>
        <condition>Medium security vulnerabilities (review required)</condition>
        <condition>Test coverage below 95% (encourage improvement)</condition>
        <condition>Performance regression 10-20% (investigate)</condition>
        <condition>High complexity functions (suggest refactoring)</condition>
        <condition>Missing documentation for public APIs</condition>
      </warning_conditions>
    </blocking_conditions>
    
    <approval_requirements>
      <automatic_approval>
        <condition>Documentation-only changes with no code impact</condition>
        <condition>Minor formatting or style fixes with no logic changes</condition>
        <condition>Dependency updates with clean security scans</condition>
        <condition>Test additions without production code changes</condition>
      </automatic_approval>
      
      <single_approval>
        <condition>Bug fixes with comprehensive tests and low risk</condition>
        <condition>Feature changes isolated to single component</condition>
        <condition>Refactoring with behavior preservation verified</condition>
        <condition>Configuration changes with rollback capability</condition>
      </single_approval>
      
      <multiple_approvals>
        <condition>Database schema changes or migrations</condition>
        <condition>Security-related modifications</condition>
        <condition>Performance-critical algorithm changes</condition>
        <condition>Breaking API changes</condition>
        <condition>Architecture or design pattern changes</condition>
      </multiple_approvals>
    </approval_requirements>
  </quality_gates>
  
  <integration_workflows>
    <ci_cd_integration>
      <automated_triggers>
        <on_pr_creation>Execute full automated check suite</on_pr_creation>
        <on_code_push>Re-run checks for updated code</on_code_push>
        <on_approval>Final validation before merge eligibility</on_approval>
        <pre_merge>Last-minute checks before actual merge</pre_merge>
      </automated_triggers>
      
      <status_reporting>
        <check_status>Real-time status updates for each automated check</check_status>
        <quality_metrics>Coverage, complexity, and performance metrics</quality_metrics>
        <security_status>Vulnerability scan results and remediation status</security_status>
        <review_readiness>Overall readiness score for human review</review_readiness>
      </status_reporting>
    </ci_cd_integration>
    
    <notification_system>
      <reviewer_assignment>
        <automatic_assignment>Assign reviewers based on code ownership and expertise</automatic_assignment>
        <workload_balancing>Distribute review workload across team members</workload_balancing>
        <escalation_rules>Escalate to senior reviewers for high-risk changes</escalation_rules>
      </reviewer_assignment>
      
      <status_notifications>
        <review_ready>Notify when PR is ready for human review</review_ready>
        <review_complete>Notify when review is complete and PR can be merged</review_complete>
        <blocking_issues>Immediate notification for critical blocking issues</blocking_issues>
        <merge_conflicts>Alert when merge conflicts need resolution</merge_conflicts>
      </status_notifications>
    </notification_system>
  </integration_workflows>
  
  <performance_metrics>
    <review_efficiency>
      <target>Average review time reduced by 50% compared to manual process</target>
      <measurement>Time from PR creation to approval</measurement>
      <tracking>Review time by PR type, size, and complexity</tracking>
    </review_efficiency>
    
    <issue_detection>
      <target>90% of potential issues caught by automated checks</target>
      <measurement>Issues found in automated review vs post-merge issues</measurement>
      <tracking>Issue type, severity, and detection source</tracking>
    </issue_detection>
    
    <quality_improvement>
      <target>Improved code quality metrics and reduced technical debt</target>
      <measurement>Code complexity, coverage, and maintainability scores</measurement>
      <tracking>Quality trends over time and correlation with automated review usage</tracking>
    </quality_improvement>
  </performance_metrics>
  
  <integration_points>
    <depends_on>
      quality/pre-commit.md for automated quality checking infrastructure
      git/conventional-commits.md for PR title and description generation
      quality/tdd.md for test coverage and quality standards
      patterns/git-operations.md for git workflow integration
    </depends_on>
    <provides_to>
      patterns/git-operations.md for enhanced PR workflow automation
      quality/production-standards.md for comprehensive quality validation
      development/task-management.md for review process integration
      All commands for automated review workflow
    </provides_to>
  </integration_points>
  
  <pattern_usage>
    <uses_pattern from="patterns/pattern-library.md">automated_workflows</uses_pattern>
    <uses_pattern from="patterns/pattern-library.md">quality_gates</uses_pattern>
    <uses_pattern from="patterns/pattern-library.md">template_generation</uses_pattern>
    <implementation_notes>
      Automated check execution follows automated_workflows pattern for consistency
      Quality validation implements quality_gates pattern for comprehensive checking
      Review template generation uses template_generation for intelligent customization
      Integration with CI/CD follows established automation patterns
    </implementation_notes>
  </pattern_usage>
  
</module>
```