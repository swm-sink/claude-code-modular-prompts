---
description: Intelligent git history analysis with pattern detection, contributor insights, and code evolution tracking
argument-hint: "[analysis_type] [scope]"
allowed-tools: Read, Write, Edit, Bash, Grep
---

# /git history - Intelligent History Analysis

Advanced git history analysis with pattern detection, contributor insights, code evolution tracking, and intelligent reporting.

## Usage
```bash
/git history analyze                         # Comprehensive history analysis
/git history contributors                    # Contributor insights and patterns
/git history evolution                       # Code evolution and trend analysis
/git history --pattern                       # Pattern detection in commit history
```

<command_file>
  <metadata>
    <name>/git history</name>
    <purpose>Analyzes Git history to understand development patterns and track changes.</purpose>
    <usage>
      <![CDATA[
      /git history <path="all"> <since="30d"> <author="all">
      ]]>
    </usage>
  </metadata>

  <arguments>
    <argument name="path" type="string" required="false" default="all">
      <description>The file or directory path to analyze. Defaults to the entire repository.</description>
    </argument>
    <argument name="since" type="string" required="false" default="30d">
      <description>The time window to analyze (e.g., '7d', '30d', '3m').</description>
    </argument>
     <argument name="author" type="string" required="false" default="all">
      <description>Filter the history by a specific author's email.</description>
    </argument>
  </arguments>
  
  <examples>
    <example>
      <description>Analyze the commit history for the entire repository over the last 30 days.</description>
      <usage>/git history</usage>
    </example>
    <example>
      <description>Analyze the history for the 'src/core' directory over the last 3 months.</description>
      <usage>/git history path="src/core" since="3m"</usage>
    </example>
  </examples>

  <claude_prompt>
    <prompt>
      You are a git history analyst. The user wants to understand the development history of the project.

      1.  **Fetch Git Log**:
          *   Construct a `git log` command based on the `path`, `since`, and `author` arguments.
          *   Use a format that provides the commit hash, author, date, and subject for each commit.
      2.  **Analyze Data**:
          *   Parse the git log output.
          *   Aggregate the data to identify key metrics:
              *   Total number of commits.
              *   Top contributors.
              *   Commit frequency over time.
      3.  **Generate Report**:
          *   Create a report summarizing the findings.
          *   Include simple visualizations (e.g., a bar chart for commit frequency) if possible.
          *   <include component="components/reporting/generate-structured-report.md" />
    </prompt>
  </claude_prompt>

  <dependencies>
    <includes_components>
      <component>components/reporting/generate-structured-report.md</component>
    </includes_components>
  </dependencies>
</command_file>