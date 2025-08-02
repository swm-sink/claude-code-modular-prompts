# Search Files Component

**Purpose**: Find files and search content using pattern matching with Grep and Glob tools for code discovery.

**Usage**: 
- Use Glob tool for file pattern matching (*.js, **/*.md, specific directories)
- Use Grep tool for content search within files (regex patterns, keywords)
- Combine both tools for targeted searches (find files then search content)
- Parse search patterns and parameters with validation
- Report findings clearly with file paths and match contexts

**Compatibility**: 
- **Works with**: file-reader, input-validation, output-formatter, error-handler
- **Requires**: Search patterns and file criteria
- **Conflicts**: None (universal search utility)

**Implementation**:
```pseudocode
pattern = parse_search_parameters()
if searching_by_filename:
    files = use_glob_tool(pattern)
if searching_by_content:
    matches = use_grep_tool(pattern, target_files)
combined_results = combine_file_and_content_matches()
return {files_found: count, content_matches: list, search_summary: report}
```

**Category**: atomic | **Complexity**: low | **Time**: 2 hours