# /query - Intelligent Analysis Command

**Purpose**: Perform parallel search and analysis across the codebase to answer questions and provide context-aware results without making any modifications.

## Usage
```bash
/query "how is authentication handled"
/query "find all API endpoints"
/query "what databases are used"
/query "show error handling patterns"
```

## Workflow

The `/query` command performs intelligent, multi-dimensional analysis:

1. **Parse Intent** - Understand what you're looking for
2. **Parallel Search** - Use multiple search strategies simultaneously
3. **Context Gathering** - Collect surrounding code for understanding
4. **Pattern Analysis** - Identify common patterns and practices
5. **Synthesize Results** - Present findings with actionable insights

## Implementation

When you use `/query`, I will follow this structured analysis process:

```xml
<analysis_workflow>
  <step name="Intent Parsing">
    <description>Understand the core question being asked and extract key terms and concepts.</description>
  </step>
  
  <step name="Parallel Search">
    <description>Use multiple search strategies simultaneously to quickly locate relevant information.</description>
    <strategies>
      <strategy name="Direct Keyword Search">Use Grep for direct keywords (e.g., "auth", "authentication").</strategy>
      <strategy name="Pattern-Based Search">Use Grep with regular expressions for patterns (e.g., "middleware.*auth").</strategy>
      <strategy name="File Discovery">Use Glob to find relevantly named files and directories (e.g., "**/auth/**").</strategy>
      <strategy name="Configuration Search">Use Grep to search for keywords within configuration files.</strategy>
    </strategies>
  </step>
  
  <step name="Context Gathering">
    <description>For each relevant file found, gather additional context to build a complete picture.</description>
    <actions>
      <action>Read the full content of the most relevant files.</action>
      <action>Find all imports and dependencies within those files.</action>
      <action>Locate any associated test files to understand expected behavior.</action>
    </actions>
  </step>
  
  <step name="Pattern Analysis & Synthesis">
    <description>Analyze the gathered information to identify common patterns and synthesize a comprehensive answer.</description>
    <actions>
      <action>Identify common architectural patterns (e.g., middleware, decorators).</action>
      <action>Detect the specific frameworks and libraries being used.</action>
      <action>Map the relationships between different components.</action>
      <action>Synthesize all findings into a clear, structured report.</action>
    </actions>
  </step>
</analysis_workflow>
```

## Advanced Techniques

To provide the most accurate and comprehensive results, the `/query` command employs several advanced techniques.

```xml
<advanced_techniques>
  <technique name="Efficient Search Cascade">
    <description>A multi-level search strategy to quickly narrow down the most relevant information.</description>
    <steps>
      <step level="1" name="Broad Search">
        <description>Perform a broad, case-insensitive search for the user's query terms to identify a set of potentially relevant files.</description>
        <tool_usage>
          <tool>Parallel Grep/Glob</tool>
        </tool_usage>
      </step>
      <step level="2" name="Deep Dive">
        <description>Read the full contents of the most promising files from the broad search to gain a deeper understanding of their context.</description>
        <tool_usage>
          <tool>Parallel Read</tool>
        </tool_usage>
      </step>
      <step level="3" name="Related File Discovery">
        <description>Analyze the files from the deep dive to discover related files, such as imports, dependencies, and tests.</description>
        <tool_usage>
          <tool>Parallel Grep/Glob</tool>
        </tool_usage>
      </step>
    </steps>
  </technique>
  
  <technique name="Semantic Search">
    <description>Go beyond simple keyword matching to understand the user's intent at a deeper level.</description>
    <capabilities>
      <capability>Understand synonyms (e.g., auth -> authentication, login).</capability>
      <capability>Recognize architectural patterns (e.g., middleware, decorators).</capability>
      <capability>Identify framework-specific conventions.</capability>
    </capabilities>
  </technique>
  
  <technique name="Dependency Tracking">
    <description>Map the relationships between different components to provide a clear picture of how the system works together.</description>
    <output>A dependency graph showing how components connect.</output>
  </technique>
  
  <technique name="Code Quality Insights">
    <description>Proactively identify potential issues and suggest improvements.</description>
    <capabilities>
      <capability>Identify potential performance bottlenecks.</capability>
      <capability>Suggest refactoring opportunities.</capability>
      <capability>Highlight best practices.</capability>
      <capability>Flag potential security concerns.</capability>
    </capabilities>
  </technique>
</advanced_techniques>
```

## Configuration

Customize behavior via `PROJECT_CONFIG.xml`:
```xml
<project_config>
  <commands>
    <query>
      <max_results>50</max_results>
      <context_lines>10</context_lines>
      <include_tests>true</include_tests>
      <parallel_searches>5</parallel_searches>
      <semantic_search>true</semantic_search>
    </query>
  </commands>
</project_config>
```

## Example Queries

### Example 1: API Discovery
```bash
/query "find all API endpoints"
```
Results:
- Route definitions in Express/FastAPI/Gin
- REST endpoints with methods
- GraphQL schema definitions
- WebSocket handlers
- API documentation

### Example 2: Error Handling
```bash
/query "how are errors handled"
```
Results:
- Global error handlers
- Try-catch patterns
- Error middleware
- Logging strategies
- User-facing error messages

### Example 3: Database Usage
```bash
/query "what databases are used"
```
Results:
- Database drivers and ORMs
- Connection configurations
- Migration files
- Schema definitions
- Query patterns

## Best Practices

1.  **Be Specific** - More specific queries yield better results.
2.  **Use Context** - "auth in user service" vs just "auth".
3.  **Iterate** - Refine queries based on initial results.
4.  **Combine Queries** - Chain queries for deeper analysis.
5.  **Verify Findings** - Cross-reference with documentation.

---
*Smart analysis through parallel search and pattern recognition*