---
description: Enforces code quality standards using configurable quality gates
argument-hint: ""
allowed-tools: Bash, Read, Grep, Glob
---

# /quality enforce - Quality Gate Enforcement

Enforces code quality standards by applying configurable quality gates from the project configuration.

## Usage
```bash
/quality enforce  # Run quality gate enforcement
```

## What It Does
1. **Load Quality Gates**: Reads quality standards from PROJECT_CONFIG.xml
2. **Analyze Codebase**: Measures test coverage, complexity, and security metrics
3. **Evaluate Gates**: Compares metrics against configured thresholds
4. **Generate Report**: Creates detailed report and blocks pipeline if gates fail

<command_file>
  <metadata>
    <name>/quality enforce</name>
    <purpose>Enforces code quality standards by applying a set of configurable quality gates from the project config.</purpose>
    <usage>
      <![CDATA[
      /quality enforce
      ]]>
    </usage>
  </metadata>

  <arguments>
    <!-- This command takes no direct arguments; it reads from the config. -->
  </arguments>
  
  <examples>
    <example>
      <description>Run the quality gate enforcement on the project.</description>
      <usage>/quality enforce</usage>
    </example>
  </examples>

  <claude_prompt>
    <prompt>
      <![CDATA[
You are a CI/CD quality engineer. Your task is to enforce the project's quality gates.

      1.  **Load Quality Gates**: Read the `<quality_standards>` section of `PROJECT_CONFIG.xml`.
      2.  **Analyze Codebase**: Perform a comprehensive analysis to measure metrics for test coverage, complexity, and security.
      3.  **Evaluate Quality Gates**: Compare the measured metrics against the configured thresholds.
      4.  **Generate Report & Enforce**: Generate a detailed report. If any gates fail, state that you would exit with a non-zero status code to block a pipeline.

      
]]>
      <include component="components/reporting/generate-structured-report.md" />
    </prompt>
  </claude_prompt>

  <dependencies>
    <includes_components>
      <!-- <component>components/reporting/generate-structured-report.md</component> -->
    </includes_components>
    <uses_config_values>
      <value>quality_standards.test_coverage.threshold</value>
      <value>quality_standards.performance.response_time_p95</value>
      <value>quality_standards.code_quality.max_complexity</value>
    </uses_config_values>
  </dependencies>
</command_file>