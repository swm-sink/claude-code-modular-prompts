# /cache clear - Cache Clearing Command

**Purpose**: Clear various cache types across the project and development environment to improve performance, fix issues, and free storage space.

## Usage
```bash
/cache clear [type]
```

## Workflow

The `/cache clear` command follows a systematic process to safely clear caches.

```xml
<cache_clear_workflow>
  <step name="Analyze Caches">
    <description>Analyze all relevant cache types (memory, file, build, dependency, and application) to determine their size and contents. This includes language-specific caches for Python, Node.js, Java, Go, and Docker.</description>
    <tool_usage>
      <tool>Parallel Bash</tool>
      <description>Run commands to analyze the size of various cache directories.</description>
    </tool_usage>
  </step>
  
  <step name="Clear Caches">
    <description>Clear the specified cache types. By default, it will clear all identified caches. The user can specify a type (e.g., `build`, `deps`) to clear only a specific cache.</description>
    <tool_usage>
      <tool>Parallel Bash</tool>
      <description>Run commands to delete the contents of various cache directories.</description>
    </tool_usage>
  </step>
  
  <step name="Verify & Report">
    <description>Verify that the caches have been cleared successfully and generate a report detailing the cleared caches and the amount of space freed.</description>
    <output>A summary report of the cache clearing operation.</output>
  </step>
</cache_clear_workflow>
```

### Language-Specific Caches
- **Python**: pip cache, __pycache__, .pyc files, pytest cache
- **Node.js**: npm/yarn cache, node_modules/.cache, .next cache
- **Java**: Maven/Gradle cache, target directories, .class files
- **Go**: Module cache, build cache, test cache
- **Docker**: Image cache, build cache, volume cache