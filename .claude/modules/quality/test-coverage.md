| version | last_updated | status |
|---------|--------------|--------|
| 1.0.0   | 2025-07-11   | stable |

# Test Coverage Module

────────────────────────────────────────────────────────────────────────────────


────────────────────────────────────────────────────────────────────────────────

```xml
<module name="test_coverage" category="quality">
  
  <purpose>
    Enforce mandatory test coverage measurement and reporting with automated tooling integration, blocking enforcement, and comprehensive validation across all development workflows.
  </purpose>
  
  <interface_contract>
    <inputs>
      <required>project_language, source_directory, test_directory, coverage_threshold</required>
      <optional>coverage_config_path, report_formats, exclusion_patterns, branch_coverage</optional>
    </inputs>
    <outputs>
      <success>coverage_report, coverage_percentage, uncovered_lines, quality_gate_status</success>
      <failure>coverage_tool_missing, threshold_not_met, configuration_error, execution_failure</failure>
    </outputs>
  </interface_contract>
  
  <execution_pattern>
    <claude_4_behavior>
      WHEN invoked:
      1. Detect project language and appropriate coverage tool
      2. Verify coverage tool installation and configuration
      3. Execute coverage measurement with proper parameters
      4. Parse coverage results and validate against thresholds
      5. Generate detailed reports and block if requirements not met
    </claude_4_behavior>
  </execution_pattern>
  
  <trigger_conditions>
    <condition type="automatic">Any code changes during TDD RED-GREEN-REFACTOR cycle</condition>
    <condition type="automatic">Pre-commit validation and quality gate checks</condition>
    <condition type="explicit">User requests coverage report or validation</condition>
    <condition type="mandatory">All /task, /feature, /swarm command executions</condition>
  </trigger_conditions>
  
  <implementation>
    
    <coverage_tool_configuration>
      <python_coverage>
        <tool>pytest-cov</tool>
        <installation>pip install pytest-cov coverage[toml]</installation>
        <basic_command>pytest --cov={source_dir} --cov-report=term-missing --cov-fail-under=90</basic_command>
        <detailed_command>
          pytest --cov={source_dir} \
                 --cov-report=html \
                 --cov-report=term-missing \
                 --cov-report=xml \
                 --cov-branch \
                 --cov-fail-under=90 \
                 tests/
        </detailed_command>
        <config_file>.coveragerc or pyproject.toml [tool.coverage]</config_file>
        <exclusions>
          <pattern>*/tests/*</pattern>
          <pattern>*/migrations/*</pattern>
          <pattern>*/__pycache__/*</pattern>
          <pattern>*/venv/*</pattern>
          <pattern>setup.py</pattern>
        </exclusions>
      </python_coverage>
      
      <javascript_coverage>
        <tool>jest</tool>
        <installation>npm install --save-dev jest</installation>
        <basic_command>jest --coverage --coverageThreshold='{"global":{"lines":90,"branches":85}}'</basic_command>
        <config_file>jest.config.js or package.json "jest" section</config_file>
        <coverage_config>
          {
            "collectCoverage": true,
            "coverageDirectory": "coverage",
            "coverageReporters": ["text", "lcov", "html"],
            "coverageThreshold": {
              "global": {
                "branches": 85,
                "functions": 90,
                "lines": 90,
                "statements": 90
              }
            }
          }
        </coverage_config>
      </javascript_coverage>
      
      <typescript_coverage>
        <tool>nyc with ts-node</tool>
        <installation>npm install --save-dev nyc @istanbuljs/nyc-config-typescript</installation>
        <basic_command>nyc --check-coverage --lines 90 --branches 85 npm test</basic_command>
        <config_file>.nycrc.json</config_file>
        <coverage_config>
          {
            "extends": "@istanbuljs/nyc-config-typescript",
            "check-coverage": true,
            "lines": 90,
            "branches": 85,
            "functions": 90,
            "statements": 90,
            "reporter": ["text", "lcov", "html"]
          }
        </coverage_config>
      </typescript_coverage>
      
      <go_coverage>
        <tool>go test -cover</tool>
        <installation>Built into Go toolchain</installation>
        <basic_command>go test -cover -coverprofile=coverage.out ./...</basic_command>
        <html_report>go tool cover -html=coverage.out -o coverage.html</html_report>
        <threshold_check>Custom script required for threshold enforcement</threshold_check>
      </go_coverage>
    </coverage_tool_configuration>
    
    <coverage_enforcement_rules enforcement="MANDATORY">
      <phase name="tdd_red_phase_coverage">
        <requirement>Execute coverage tool to establish baseline (expect 0% for new code)</requirement>
        <command>Run coverage tool with test files only to verify test infrastructure</command>
        <validation>Tests exist and coverage tool executes successfully</validation>
        <blocking_condition>Coverage tool not installed or configured</blocking_condition>
      </phase>
      
      <phase name="tdd_green_phase_coverage">
        <requirement>Run coverage after implementation to measure coverage percentage</requirement>
        <command>Execute full coverage suite with all tests against implementation</command>
        <validation>Coverage approaching or exceeding 90% threshold</validation>
        <blocking_condition>Coverage below 90% after implementation</blocking_condition>
        <output_example>
          ======= Coverage report =======
          Module            Lines    Miss  Cover
          ----------------------------------------
          my_module.py        45       3    93%
          utils.py            28       0   100%
          ----------------------------------------
          TOTAL               73       3    96%
          
          ✅ Coverage threshold (90%) met!
        </output_example>
      </phase>
      
      <phase name="tdd_refactor_phase_coverage">
        <requirement>Maintain or improve coverage during refactoring</requirement>
        <command>Run coverage after each refactor step to ensure no regression</command>
        <validation>Coverage percentage must not decrease from GREEN phase</validation>
        <blocking_condition>Any decrease in coverage percentage</blocking_condition>
      </phase>
      
      <phase name="final_validation_coverage">
        <requirement>Final coverage check with detailed reporting</requirement>
        <commands>
          <html_report>Generate HTML coverage report for detailed analysis</html_report>
          <missing_lines>Show specific uncovered lines requiring attention</missing_lines>
          <branch_coverage>Verify branch coverage meets standards (85%+)</branch_coverage>
        </commands>
        <validation>All coverage metrics meet or exceed thresholds</validation>
        <blocking_condition>Any metric below required threshold</blocking_condition>
      </phase>
    </coverage_enforcement_rules>
    
    <blocking_enforcement priority="CRITICAL">
      <rule name="no_coverage_no_commit">
        <description>BLOCK all commits without coverage evidence</description>
        <enforcement>Pre-commit hook must verify coverage execution</enforcement>
        <error_message>❌ BLOCKED: No coverage report found. Run coverage tools first!</error_message>
      </rule>
      
      <rule name="threshold_not_met">
        <description>BLOCK if coverage below 90% threshold</description>
        <enforcement>Quality gates must check coverage percentage</enforcement>
        <error_message>❌ BLOCKED: Coverage {current}% is below 90% threshold!</error_message>
      </rule>
      
      <rule name="coverage_regression">
        <description>BLOCK if coverage decreases from previous run</description>
        <enforcement>Compare with baseline and reject regressions</enforcement>
        <error_message>❌ BLOCKED: Coverage decreased from {previous}% to {current}%!</error_message>
      </rule>
      
      <rule name="missing_critical_coverage">
        <description>BLOCK if critical paths have <100% coverage</description>
        <enforcement>Identify and enforce 100% coverage for critical code</enforcement>
        <error_message>❌ BLOCKED: Critical path {path} has only {coverage}% coverage!</error_message>
      </rule>
    </blocking_enforcement>
    
    <coverage_reporting>
      <report_formats>
        <terminal>Always display coverage summary in terminal output</terminal>
        <html>Generate HTML report for detailed line-by-line analysis</html>
        <xml>Create XML report for CI/CD integration (Cobertura format)</xml>
        <json>Generate JSON report for programmatic analysis</json>
      </report_formats>
      
      <report_location>
        <html_report>./htmlcov/index.html or ./coverage/lcov-report/index.html</html_report>
        <xml_report>./coverage.xml or ./coverage/cobertura-coverage.xml</xml_report>
        <badge_generation>Generate coverage badge for README display</badge_generation>
      </report_location>
      
      <uncovered_analysis>
        <show_missing>Display specific line numbers that lack coverage</show_missing>
        <context_lines>Show surrounding code context for uncovered sections</context_lines>
        <prioritization>Highlight critical uncovered code requiring immediate attention</prioritization>
      </uncovered_analysis>
    </coverage_reporting>
    
    <quality_gate_integration>
      <gate name="test_coverage_verification" enforcement="BLOCKING">
        <description>Verify test coverage meets all requirements using actual tools</description>
        <criteria>
          <requirement>Coverage tool installed and configured correctly</requirement>
          <requirement>Coverage command executed successfully</requirement>
          <requirement>Line coverage ≥ 90% verified by tool output</requirement>
          <requirement>Branch coverage ≥ 85% where applicable</requirement>
          <requirement>Critical paths have 100% coverage</requirement>
          <requirement>Coverage report generated and accessible</requirement>
        </criteria>
        <validation_method>
          <check>Parse coverage tool output for percentage</check>
          <check>Verify report files exist and contain data</check>
          <check>Analyze uncovered lines for critical code</check>
          <check>Compare with previous baseline if available</check>
        </validation_method>
        <failure_response>BLOCK with specific coverage gaps and remediation steps</failure_response>
      </gate>
    </quality_gate_integration>
    
  </implementation>
  
  <integration_points>
    <depends_on>
      quality/tdd.md for TDD cycle integration and test-first methodology
      quality/universal-quality-gates.md for quality gate framework and enforcement
      quality/production-standards.md for production readiness criteria
      patterns/tool-usage.md for coverage tool execution patterns
    </depends_on>
    <provides_to>
      quality/tdd.md for coverage measurement during RED-GREEN-REFACTOR cycle
      quality/universal-quality-gates.md for coverage verification gate implementation
      quality/production-standards.md for coverage reporting requirements
      All commands for mandatory coverage tool execution and validation
      development/task-management.md for coverage checks in task workflow
      patterns/multi-agent.md for aggregated coverage across agents
    </provides_to>
  </integration_points>
  
  <pattern_usage>
    <uses_pattern from="patterns/pattern-library.md">tool_execution</uses_pattern>
    <uses_pattern from="patterns/pattern-library.md">quality_gates</uses_pattern>
    <uses_pattern from="patterns/pattern-library.md">blocking_enforcement</uses_pattern>
    <implementation_notes>
      Coverage tools follow tool_execution pattern for consistent invocation
      Coverage verification implements quality_gates pattern for validation
      Threshold enforcement uses blocking_enforcement pattern for compliance
      Reports follow standardized output patterns for parsing and analysis
    </implementation_notes>
  </pattern_usage>
  
  <session_integration>
    <coverage_tracking>
      <baseline_recording>Record initial coverage percentage at session start</baseline_recording>
      <progress_monitoring>Track coverage improvements throughout development</progress_monitoring>
      <regression_detection>Alert on any coverage decreases during session</regression_detection>
      <final_validation>Ensure coverage meets targets before session completion</final_validation>
    </coverage_tracking>
    <documentation_requirements>
      <coverage_evidence>Include coverage reports in session artifacts</coverage_evidence>
      <improvement_tracking>Document coverage progression from RED to GREEN</improvement_tracking>
      <gap_analysis>Identify and document remaining coverage gaps</gap_analysis>
      <remediation_plan>Create action items for uncovered critical code</remediation_plan>
    </documentation_requirements>
  </session_integration>
  
  <command_integration_requirements>
    <task_command>
      <red_phase>Execute coverage baseline check after writing tests</red_phase>
      <green_phase>Run coverage verification after implementation</green_phase>
      <refactor_phase>Ensure coverage maintained during refactoring</refactor_phase>
      <final_check>Validate 90%+ coverage before task completion</final_check>
    </task_command>
    <feature_command>
      <mvp_coverage>Verify MVP implementation meets coverage standards</mvp_coverage>
      <integration_coverage>Check coverage for integration points</integration_coverage>
      <system_coverage>Aggregate coverage across all feature components</system_coverage>
    </feature_command>
    <swarm_command>
      <agent_coverage>Each agent must achieve coverage targets independently</agent_coverage>
      <aggregate_coverage>Combine coverage reports from all agents</aggregate_coverage>
      <gap_coordination>Coordinate coverage gap remediation across agents</gap_coordination>
    </swarm_command>
  </command_integration_requirements>
  
</module>
```