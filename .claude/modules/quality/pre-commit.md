| version | last_updated | status |
|---------|--------------|--------|
| 1.0.0   | 2025-07-11   | stable |

# Pre-commit Quality Gates Module

────────────────────────────────────────────────────────────────────────────────


────────────────────────────────────────────────────────────────────────────────

```xml
<module name="pre_commit" category="quality">
  
  <purpose>
    Prevent 95% of quality issues from reaching repository through automated pre-commit checks with auto-fix capabilities and blocking enforcement.
  </purpose>
  
  <trigger_conditions>
    <condition type="automatic">Before every git commit operation</condition>
    <condition type="explicit">Manual quality check request via commands</condition>
    <condition type="ci_integration">Automated pipeline quality gates</condition>
  </trigger_conditions>
  
  <implementation>
    
    <phase name="check_detection" order="1">
      <requirements>
        Language and framework detection from file extensions and config files
        Appropriate linting and checking tools identified for each language
        Project-specific configuration files located and validated
        Staged files analyzed for relevant check applicability
      </requirements>
      <actions>
        Detect languages from staged files: .js/.ts (ESLint), .py (Ruff/Black), .rs (Clippy), .go (golint)
        Locate configuration files: .eslintrc, pyproject.toml, rustfmt.toml, .golangci.yml
        Identify test frameworks: Jest, pytest, cargo test, go test
        Map staged files to applicable quality checks
      </actions>
      <validation>
        All relevant quality tools identified for staged files
        Configuration files found or default configs established
        Check applicability matrix created for each staged file
      </validation>
    </phase>
    
    <phase name="automated_checks" order="2">
      <requirements>
        All applicable quality checks executed on staged files
        Results captured with detailed error descriptions and locations
        Auto-fixable issues identified and fixed automatically
        Manual fixes required flagged with clear instructions
      </requirements>
      <actions>
        Execute linting checks with auto-fix where possible
        Run type checking for statically typed languages
        Execute relevant test suites for modified code areas
        Perform security scanning for vulnerability detection
        Validate code formatting and apply fixes automatically
      </actions>
      <validation>
        All checks completed with success/failure status
        Auto-fixes applied and staged for commit
        Manual fix requirements documented with specific locations
        Security issues identified and flagged appropriately
      </validation>
    </phase>
    
    <phase name="blocking_enforcement" order="3">
      <requirements>
        Critical failures block commit until resolved
        Auto-fixes applied and re-staged automatically
        Clear feedback provided for manual fixes required
        Bypass mechanisms available for emergency situations
      </requirements>
      <actions>
        Block commit if critical linting errors remain after auto-fix
        Block commit if type checking failures exist
        Block commit if security vulnerabilities detected
        Block commit if test failures in affected areas
        Provide detailed error report with fix instructions
      </actions>
      <validation>
        Commit blocked when quality standards not met
        Clear error messages provided for all blocking issues
        Auto-fixes properly applied and staged
        Emergency bypass available with justification requirement
      </validation>
    </phase>
    
  </implementation>
  
  <language_configurations>
    <javascript_typescript>
      <linting>
        <tool>ESLint with TypeScript support</tool>
        <config_files>.eslintrc.js, .eslintrc.json, eslint.config.js</config_files>
        <auto_fix>eslint --fix for fixable rules</auto_fix>
        <blocking_conditions>Error-level violations, security issues</blocking_conditions>
      </linting>
      <formatting>
        <tool>Prettier for code formatting</tool>
        <config_files>.prettierrc, prettier.config.js</config_files>
        <auto_fix>prettier --write for all formatting</auto_fix>
        <integration>ESLint-Prettier integration for consistency</integration>
      </formatting>
      <type_checking>
        <tool>TypeScript compiler (tsc)</tool>
        <config_files>tsconfig.json, jsconfig.json</config_files>
        <blocking_conditions>Type errors, missing declarations</blocking_conditions>
        <no_auto_fix>Manual type fixes required</no_auto_fix>
      </type_checking>
      <testing>
        <tool>Jest, Vitest, or detected test framework</tool>
        <scope>Tests for modified files and dependencies</scope>
        <blocking_conditions>Test failures in affected areas</blocking_conditions>
      </testing>
    </javascript_typescript>
    
    <python>
      <linting>
        <tool>Ruff for fast Python linting</tool>
        <config_files>pyproject.toml, ruff.toml, .ruff.toml</config_files>
        <auto_fix>ruff --fix for auto-fixable violations</auto_fix>
        <blocking_conditions>Error-level violations, security issues</blocking_conditions>
      </linting>
      <formatting>
        <tool>Black for code formatting</tool>
        <config_files>pyproject.toml, black.toml</config_files>
        <auto_fix>black --line-length 88 for all formatting</auto_fix>
        <integration>Ruff-Black integration for consistency</integration>
      </formatting>
      <type_checking>
        <tool>mypy for static type checking</tool>
        <config_files>mypy.ini, pyproject.toml</config_files>
        <blocking_conditions>Type errors, missing type annotations</blocking_conditions>
        <incremental>Focus on modified files for performance</incremental>
      </type_checking>
      <testing>
        <tool>pytest for test execution</tool>
        <scope>Tests for modified modules and dependencies</scope>
        <blocking_conditions>Test failures, assertion errors</blocking_conditions>
      </testing>
    </python>
    
    <rust>
      <linting>
        <tool>Clippy for Rust linting</tool>
        <config_files>clippy.toml, .clippy.toml</config_files>
        <auto_fix>cargo clippy --fix for auto-fixable issues</auto_fix>
        <blocking_conditions>Error-level lints, performance issues</blocking_conditions>
      </linting>
      <formatting>
        <tool>rustfmt for code formatting</tool>
        <config_files>rustfmt.toml, .rustfmt.toml</config_files>
        <auto_fix>cargo fmt for all formatting</auto_fix>
        <integration>Built into Rust toolchain</integration>
      </formatting>
      <type_checking>
        <tool>Rust compiler (rustc)</tool>
        <checking>Built into cargo check</checking>
        <blocking_conditions>Compilation errors, type mismatches</blocking_conditions>
        <no_auto_fix>Manual type fixes required</no_auto_fix>
      </type_checking>
      <testing>
        <tool>cargo test for Rust testing</tool>
        <scope>Tests for modified modules</scope>
        <blocking_conditions>Test failures, panic errors</blocking_conditions>
      </testing>
    </rust>
    
    <go>
      <linting>
        <tool>golangci-lint for comprehensive Go linting</tool>
        <config_files>.golangci.yml, .golangci.yaml</config_files>
        <auto_fix>golangci-lint run --fix for fixable issues</auto_fix>
        <blocking_conditions>Error-level violations, security issues</blocking_conditions>
      </linting>
      <formatting>
        <tool>gofmt and goimports for formatting</tool>
        <auto_fix>gofmt -w and goimports -w for all formatting</auto_fix>
        <integration>Built into Go toolchain</integration>
      </formatting>
      <type_checking>
        <tool>Go compiler (go build)</tool>
        <checking>Built into go build process</checking>
        <blocking_conditions>Compilation errors, type mismatches</blocking_conditions>
        <no_auto_fix>Manual type fixes required</no_auto_fix>
      </type_checking>
      <testing>
        <tool>go test for Go testing</tool>
        <scope>Tests for modified packages</scope>
        <blocking_conditions>Test failures, runtime panics</blocking_conditions>
      </testing>
    </go>
  </language_configurations>
  
  <security_scanning>
    <vulnerability_detection>
      <javascript>npm audit, yarn audit for dependency vulnerabilities</javascript>
      <python>bandit for security issues, safety for dependency checks</python>
      <rust>cargo audit for dependency vulnerabilities</rust>
      <go>gosec for security issues, govulncheck for vulnerabilities</go>
    </vulnerability_detection>
    <blocking_security_issues>
      <high_severity>Block commit for high/critical security vulnerabilities</high_severity>
      <medium_severity>Warn but allow commit with explicit acknowledgment</medium_severity>
      <low_severity>Report but do not block commit</low_severity>
    </blocking_security_issues>
    <auto_fix_security>
      <dependency_updates>Auto-update dependencies with security patches</dependency_updates>
      <safe_patterns>Apply secure coding pattern fixes automatically</safe_patterns>
      <manual_review>Flag complex security issues for manual review</manual_review>
    </auto_fix_security>
  </security_scanning>
  
  <test_execution>
    <scope_determination>
      <changed_files>Run tests for directly modified files</changed_files>
      <dependencies>Run tests for files that depend on modified code</dependencies>
      <integration>Run integration tests if multiple components affected</integration>
      <performance>Skip slow tests unless explicitly requested</performance>
    </scope_determination>
    <test_frameworks>
      <javascript>Jest, Vitest, Mocha, Cypress detection and execution</javascript>
      <python>pytest, unittest, nose2 detection and execution</python>
      <rust>cargo test with workspace support</rust>
      <go>go test with package-level execution</go>
    </test_frameworks>
    <failure_handling>
      <immediate_block>Block commit on any test failure</immediate_block>
      <detailed_output>Provide full test failure details and locations</detailed_output>
      <fix_suggestions>Suggest common fixes for typical test failures</fix_suggestions>
    </failure_handling>
  </test_execution>
  
  <auto_fix_capabilities>
    <formatting_fixes>
      <automatic>All code formatting issues fixed automatically</automatic>
      <staging>Auto-fixed files automatically re-staged</staging>
      <verification>Verify fixes don't introduce new issues</verification>
    </formatting_fixes>
    <linting_fixes>
      <safe_fixes>Apply safe linting fixes automatically (imports, spacing)</safe_fixes>
      <manual_fixes>Flag unsafe fixes for manual review (logic changes)</manual_fixes>
      <incremental>Apply fixes incrementally to avoid conflicts</incremental>
    </linting_fixes>
    <import_organization>
      <sorting>Automatically sort and organize imports</sorting>
      <removal>Remove unused imports automatically</removal>
      <addition>Add missing imports where deterministic</addition>
    </import_organization>
  </auto_fix_capabilities>
  
  <blocking_conditions>
    <critical_blocking>
      <condition>Linting errors marked as "error" level</condition>
      <condition>Type checking failures (compilation errors)</condition>
      <condition>High/critical security vulnerabilities</condition>
      <condition>Test failures in affected code areas</condition>
      <condition>Syntax errors or parsing failures</condition>
    </critical_blocking>
    <warning_conditions>
      <condition>Medium severity security issues (warn but allow)</condition>
      <condition>Linting warnings above configured threshold</condition>
      <condition>Missing test coverage below minimum threshold</condition>
      <condition>Code complexity above configured limits</condition>
    </warning_conditions>
    <bypass_mechanisms>
      <emergency>--force-commit flag for emergency situations</emergency>
      <justification>Required justification comment for bypass</justification>
      <audit_trail>Bypass usage logged for security audit</audit_trail>
    </bypass_mechanisms>
  </blocking_conditions>
  
  <performance_optimization>
    <incremental_checking>
      <changed_files>Focus checks on staged files only</changed_files>
      <cache_utilization>Use tool caches for faster subsequent runs</cache_utilization>
      <parallel_execution>Run compatible checks in parallel</parallel_execution>
    </incremental_checking>
    <tool_optimization>
      <fast_tools>Prefer faster tools where equivalent (ruff over pylint)</fast_tools>
      <selective_tests>Run only relevant tests based on change analysis</selective_tests>
      <result_caching>Cache check results for unchanged files</result_caching>
    </tool_optimization>
    <performance_targets>
      <small_commits>Under 10 files: <30 seconds total check time</small_commits>
      <medium_commits>10-50 files: <2 minutes total check time</medium_commits>
      <large_commits>50+ files: <5 minutes total check time</large_commits>
    </performance_targets>
  </performance_optimization>
  
  <integration_workflows>
    <git_hooks>
      <pre_commit>Primary integration point for automatic execution</pre_commit>
      <commit_msg>Validate commit message format via conventional-commits</commit_msg>
      <pre_push>Additional checks before pushing to remote</pre_push>
    </git_hooks>
    <ci_cd_integration>
      <github_actions>Pre-commit checks as GitHub Actions workflow</github_actions>
      <gitlab_ci>Integration with GitLab CI/CD pipelines</gitlab_ci>
      <local_development>Consistent checks between local and CI environments</local_development>
    </ci_cd_integration>
    <ide_integration>
      <real_time>Real-time linting and formatting in IDEs</real_time>
      <save_actions>Auto-fix on file save where supported</save_actions>
      <problem_highlighting>Inline error highlighting and quick fixes</problem_highlighting>
    </ide_integration>
  </integration_workflows>
  
  <reporting_output>
    <success_summary>
      <format>✅ All quality checks passed (X checks in Y seconds)</format>
      <details>Summary of checks run and auto-fixes applied</details>
      <performance>Timing breakdown for optimization insights</performance>
    </success_summary>
    <failure_reporting>
      <format>❌ Quality checks failed - commit blocked</format>
      <categorized_errors>Group errors by type: linting, typing, testing, security</categorized_errors>
      <fix_instructions>Specific commands to resolve each type of error</fix_instructions>
      <file_locations>Exact file paths and line numbers for all issues</file_locations>
    </failure_reporting>
    <auto_fix_summary>
      <applied_fixes>List of auto-fixes applied and files modified</applied_fixes>
      <remaining_issues>Manual fixes still required with instructions</remaining_issues>
      <next_steps>Clear guidance on how to proceed</next_steps>
    </auto_fix_summary>
  </reporting_output>
  
  <configuration_management>
    <project_detection>
      <automatic>Auto-detect project type and appropriate configurations</automatic>
      <inheritance>Support for shared configurations across projects</inheritance>
      <customization>Allow project-specific overrides and additions</customization>
    </project_detection>
    <configuration_hierarchy>
      <global>Framework-wide quality standards and tool preferences</global>
      <project>Project-specific configurations in repository root</project>
      <user>User-specific preferences and tool customizations</user>
    </configuration_hierarchy>
    <tool_configuration>
      <unified_config>Single configuration file for all quality tools where possible</unified_config>
      <tool_specific>Respect existing tool-specific configuration files</tool_specific>
      <defaults>Sensible defaults for projects without configuration</defaults>
    </tool_configuration>
  </configuration_management>
  
  <integration_points>
    <depends_on>
      git/conventional-commits.md for commit message validation
      quality/tdd.md for test execution standards
      patterns/tool-usage.md for parallel execution optimization
    </depends_on>
    <provides_to>
      All commands for automated quality enforcement
      patterns/git-operations.md for git workflow integration
      quality/production-standards.md for quality gate enforcement
    </provides_to>
  </integration_points>
  
  <pattern_usage>
    <uses_pattern from="patterns/pattern-library.md">automated_workflows</uses_pattern>
    <uses_pattern from="patterns/pattern-library.md">quality_gates</uses_pattern>
    <uses_pattern from="patterns/pattern-library.md">parallel_execution</uses_pattern>
    <implementation_notes>
      Automated execution follows automated_workflows pattern for consistency
      Blocking conditions implement quality_gates pattern for enforcement
      Multiple tools executed using parallel_execution for performance
      Integration with git hooks follows git-operations patterns
    </implementation_notes>
  </pattern_usage>
  
</module>
```