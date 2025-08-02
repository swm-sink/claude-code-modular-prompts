# File Reader Component

**Purpose**: Read file contents with proper path validation, error handling, and content parsing

**Usage**: 
Validate file path format and check accessibility permissions
Execute Read tool with absolute paths and optional line limits for large files
Parse file content based on detected file type (text, binary, structured data)
Handle file not found errors with specific path recommendations
Extract and return relevant content sections based on user requirements

**Compatibility**: 
- **Works with**: error-handler, content-sanitizer, data-transformer, parameter-parser
- **Requires**: file_path (string), read_options (optional object)
- **Conflicts**: file-writer (use sequentially, not simultaneously)

**Implementation**:
```javascript
// Read file with error handling and content parsing
const read_config = {
  file_path: "/absolute/path/to/file.txt",
  line_limit: 1000,  // Optional for large files
  offset: 0,          // Optional starting line
  parse_type: "auto"  // auto, text, json, csv
};

const result = await read_file(read_config);
if (!result.success) {
  return handle_error("file_access", `Cannot read ${file_path}: ${result.error}`);
}

// Process file content based on detected type
return parse_content(result.content, result.file_type);
```

**Category**: atomic | **Complexity**: simple | **Time**: 15 minutes