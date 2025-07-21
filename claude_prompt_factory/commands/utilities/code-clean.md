---
description: Advanced code cleaning with intelligent refactoring, automated optimization, and comprehensive quality enhancement
argument-hint: "[cleaning_scope] [optimization_level]"
allowed-tools: Read, Write, Edit, Bash, Grep
---

# /code clean - Advanced Code Cleaning

Sophisticated code cleaning system with intelligent refactoring, automated optimization, and comprehensive quality enhancement.

## Usage
```bash
/code clean quality                          # Quality-focused code cleaning
/code clean --comprehensive                  # Comprehensive cleaning and optimization
/code clean --automated                      # Fully automated cleaning process
/code clean --performance                    # Performance-optimized cleaning
```

<command_file>
  <metadata>
    <n>/code clean</n>
    <purpose>Advanced code cleaning with intelligent refactoring, automated optimization, and comprehensive quality enhancement</purpose>
    <usage>
      <![CDATA[
      /code clean [cleaning_scope]
      ]]>
    </usage>
  </metadata>

  <arguments>
    <argument name="cleaning_scope" type="string" required="false" default="quality">
      <description>Scope of code cleaning to perform</description>
    </argument>
    <argument name="optimization_level" type="string" required="false" default="comprehensive">
      <description>Level of optimization and enhancement</description>
    </argument>
  </arguments>
  
  <examples>
    <example>
      <description>Quality-focused code cleaning</description>
      <usage>/code clean quality</usage>
    </example>
    <example>
      <description>Comprehensive cleaning and optimization</description>
      <usage>/code clean --comprehensive</usage>
    </example>
  </examples>

  <claude_prompt>
    <prompt>
You are an advanced code cleaning specialist. The user wants to implement intelligent refactoring with automated optimization and comprehensive quality enhancement.

**Cleaning Process:**
1. **Code Analysis**: Analyze codebase for cleaning opportunities and quality issues
2. **Refactoring Planning**: Plan intelligent refactoring and optimization strategies
3. **Automated Cleaning**: Execute automated cleaning with safety validations
4. **Quality Enhancement**: Apply comprehensive quality improvements and standards
5. **Validation & Testing**: Validate cleaned code and ensure functionality preservation

**Implementation Strategy:**
- Analyze code quality using static analysis and pattern detection
- Implement intelligent refactoring with automated dead code removal
- Apply comprehensive formatting, linting, and style optimization
- Create quality enhancement with best practices enforcement
- Establish validation testing to ensure functionality preservation

<include component="components/quality/anti-pattern-detection.md" />
<include component="components/analysis/codebase-discovery.md" />
<include component="components/testing/framework-validation.md" />
    </prompt>
  </claude_prompt>

  <dependencies>
    <includes_components>
      <component>components/quality/anti-pattern-detection.md</component>
      <component>components/analysis/codebase-discovery.md</component>
      <component>components/testing/framework-validation.md</component>
    </includes_components>
    <uses_config_values>
      <value>code_cleaning.automated.enabled</value>
      <value>quality.standards.enforcement_level</value>
    </uses_config_values>
  </dependencies>
</command_file>

## Workflow

The `/code clean` command follows a systematic process to safely clean the codebase.

```xml
<code_cleaning_workflow>
  <step name="Analyze Codebase">
    <description>Analyze the codebase to identify dead code (unused functions, variables, and classes), unused imports, debug statements, and build artifacts.</description>
    <tool_usage>
      <tool>Parallel Grep/Glob/Read</tool>
      <description>Scan the codebase for cleaning opportunities.</description>
    </tool_usage>
  </step>
  
  <step name="Preview & Confirm Changes">
    <description>Present a preview of the proposed changes to the user and request confirmation before applying them. If the `--preview` flag is used, the command will exit after this step.</description>
  </step>
  
  <step name="Apply Cleaning Operations">
    <description>Apply the confirmed cleaning operations, including removing dead code, optimizing imports, eliminating debug statements, and cleaning build artifacts.</description>
    <tool_usage>
      <tool>Edit</tool>
      <description>Apply the cleaning changes to the code.</description>
      <tool>Bash</tool>
      <description>Remove build artifacts.</description>
    </tool_usage>
  </step>
  
  <step name="Verify & Report">
    <description>Verify that the cleaning operations were applied correctly and did not introduce any regressions. Generate a report summarizing the changes made.</description>
    <tool_usage>
      <tool>Bash</tool>
      <description>Run the test suite to verify the changes.</description>
    </tool_usage>
    <output>A summary of the cleaning changes.</output>
  </step>
</code_cleaning_workflow>

### Language-Specific Cleaning
- **Python**: Removes unused imports, cleans `__pycache__`, and optimizes with `black`