# File Writer Component

**Purpose**: Write processed data to files safely with validation, error handling, and overwrite protection.

**Usage**: 
- Write new files using appropriate tool selection (Write vs Edit)
- Validate file paths and check permissions before writing
- Confirm before overwriting existing files
- Handle encoding, formatting, and path security issues
- Report successful writes and any errors encountered

**Compatibility**: 
- **Works with**: file-reader, output-formatter, error-handler, content-sanitizer
- **Requires**: Formatted data and valid file paths
- **Conflicts**: api-caller (different data flow patterns)

**Implementation**:
```pseudocode
data = receive_formatted_data()
path = validate_file_path(target_path)
if file_exists(path):
    confirm_overwrite()
result = write_file_safely(data, path)
return {written: true, path: path, size: file_size, errors: any_issues}
```

**Category**: atomic | **Complexity**: simple | **Time**: 5 minutes