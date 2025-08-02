# Find Relevant Code

**Purpose**: Comprehensive codebase analysis to identify relevant files, classes, functions, and snippets based on user requests.

**Usage**: 
- Performs file searching and code analysis
- Traces dependencies to find related code
- Prioritizes source and test directories
- Provides justification for relevance
- Ensures high confidence before proceeding

**Compatibility**: 
- **Works with**: codebase-discovery, search-files, dependency-mapping
- **Requires**: search_query, file_paths, dependency_graph
- **Conflicts**: None (universal search component)

**Implementation**:
```yaml
find_relevant:
  methods: [file_search, code_analysis, dependency_trace]
  priority: [source_dir, tests_dir]
  output: files_with_justification
  confidence: high_required
```

**Category**: context | **Complexity**: simple | **Time**: 10 minutes