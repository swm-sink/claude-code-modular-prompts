# /git history - Git History Analyzer

**Purpose**: Analyze Git history to understand development patterns, identify key contributors, and track changes over time.

## Usage
```bash
/git history [path] [--since=<date>] [--author=<author>]
```

## Workflow

The `/git history` command follows a systematic process to analyze the Git history.

```xml
<git_history_workflow>
  <step name="Fetch & Parse Git Log">
    <description>Fetch the Git log for the specified path, applying any filters (e.g., date range, author). Parse the log to extract key information, such as commit messages, authors, dates, and file changes.</description>
    <tool_usage>
      <tool>Bash</tool>
      <description>Use `git log` with various formatting options to extract the necessary data.</description>
    </tool_usage>
  </step>
  
  <step name="Aggregate & Analyze Data">
    <description>Aggregate the parsed data to identify patterns and generate insights. This could include calculating commit frequency, identifying top contributors, or analyzing the types of changes made over time (e.g., features vs. fixes).</description>
    <tool_usage>
      <tool>Python/Pandas</tool>
      <description>Use a Python script with the Pandas library to perform data aggregation and analysis.</description>
    </tool_usage>
  </step>
  
  <step name="Generate & Display Report">
    <description>Generate a clear, concise report summarizing the findings. The report may include visualizations, such as charts or graphs, to make the data easier to understand.</description>
    <tool_usage>
      <tool>Markdown/Visualization Library</tool>
      <description>Generate a Markdown report, potentially embedding visualizations created with a library like Matplotlib or Seaborn.</description>
    </tool_usage>
  </step>
</git_history_workflow>
```

## Configuration

The `/git history` command can be configured through the `PROJECT_CONFIG.xml` file.

```xml
<command name="/git history">
  <setting name="default_since" value="30d" description="Default time range for history analysis (e.g., '30d' for 30 days)." />
  <setting name="output_format" value="markdown" description="The format for the output report (e.g., 'markdown', 'json')." />
</command>
```

## Use Cases

*   **Code Audits**: Understand who changed what and when in a critical part of the codebase.
*   **Performance Reviews**: Gather data on individual or team contributions over a specific period.
*   **Project Retrospectives**: Analyze development velocity and patterns to inform future planning.