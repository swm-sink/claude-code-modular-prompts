# Component Assembly Example

## Building a File Processing Command from Atomic Components

This example demonstrates how to assemble atomic components into a working `/process-files` slash command using the proven workflow pattern:

`search-files → file-reader → content-sanitizer → data-transformer → output-formatter`

### Step 1: Start with Command Template

```yaml
---
name: "process-files"
description: "Search, read, sanitize, transform and format files"
usage: "process-files <search-pattern> <target-format>"
allowed-tools: ["Glob", "Read", "Edit", "Write"]
category: "file-processing"
---

# Process Files Command

Process files by searching, reading, sanitizing, transforming and formatting them.

## Usage
/process-files "*.json" yaml

## Implementation
```

### Step 2: Assemble Components in Sequence

```markdown
## Implementation

### 1. Search for Files
```
Search for files and content patterns:
- Accept and parse input data or parameters
- Process search patterns and directory specifications using glob/regex
- Execute comprehensive file and content searches with proper recursion
- Filter results based on file type, size, and modification criteria
- Handle errors and edge cases according to defined criteria
- Generate structured search results with relevance ranking
```

### 2. Read File Contents
```
Read file contents with error handling:
- Validate file path format and accessibility permissions
- Execute Read tool with absolute path and optional line limits
- Parse file content according to detected file type (text, binary, structured)
- Handle file not found errors with specific path recommendations
- Extract and return relevant content sections based on requirements
- Generate structured report of read operation results and metadata
```

### 3. Sanitize Content
```
Sanitize input content for security:
- Remove potentially harmful code or scripts
- Escape special characters and markup
- Validate against whitelist patterns
- Strip unnecessary metadata and formatting
- Handle unsupported formats with appropriate fallbacks
- Ensure content meets safety standards
```

### 4. Transform Data
```
Transform data between different formats:
- Identify source and target data formats
- Apply appropriate transformation rules
- Preserve data integrity during conversion
- Process nested structures and arrays
- Handle transformation failures gracefully
- Validate transformation completeness
```

### 5. Format Output
```
Format output with structured presentation:
- Parse input data and detect current format (JSON, YAML, plain text)
- Apply consistent headers with hierarchical numbering for sections
- Generate bullet points with proper indentation for list structures
- Wrap technical content in appropriate code blocks with syntax highlighting
- Handle unsupported formats using markdown fallback with clear labels
- Create concise summaries with key metrics and actionable next steps
```
```

### Step 3: Complete Command File

```yaml
---
name: "process-files"
description: "Search, read, sanitize, transform and format files"
usage: "process-files <search-pattern> <target-format>"
allowed-tools: ["Glob", "Read", "Edit", "Write"]
category: "file-processing"
---

# Process Files Command

Process files by searching, reading, sanitizing, transforming and formatting them.

## Usage
/process-files "*.json" yaml

## Implementation

### 1. Search for Files
```
Search for files and content patterns:
- Accept and parse input data or parameters
- Process search patterns and directory specifications using glob/regex
- Execute comprehensive file and content searches with proper recursion
- Filter results based on file type, size, and modification criteria
- Handle errors and edge cases according to defined criteria
- Generate structured search results with relevance ranking
```

### 2. Read File Contents
```
Read file contents with error handling:
- Validate file path format and accessibility permissions
- Execute Read tool with absolute path and optional line limits
- Parse file content according to detected file type (text, binary, structured)
- Handle file not found errors with specific path recommendations
- Extract and return relevant content sections based on requirements
- Generate structured report of read operation results and metadata
```

### 3. Sanitize Content
```
Sanitize input content for security:
- Remove potentially harmful code or scripts
- Escape special characters and markup
- Validate against whitelist patterns
- Strip unnecessary metadata and formatting
- Handle unsupported formats with appropriate fallbacks
- Ensure content meets safety standards
```

### 4. Transform Data
```
Transform data between different formats:
- Identify source and target data formats
- Apply appropriate transformation rules
- Preserve data integrity during conversion
- Process nested structures and arrays
- Handle transformation failures gracefully
- Validate transformation completeness
```

### 5. Format Output
```
Format output with structured presentation:
- Parse input data and detect current format (JSON, YAML, plain text)
- Apply consistent headers with hierarchical numbering for sections
- Generate bullet points with proper indentation for list structures
- Wrap technical content in appropriate code blocks with syntax highlighting
- Handle unsupported formats using markdown fallback with clear labels
- Create concise summaries with key metrics and actionable next steps
```

## Error Handling
This command incorporates error handling from each component to provide comprehensive failure management throughout the file processing pipeline.

## Expected Output
- Structured file search results
- Sanitized and transformed file contents
- Formatted output in specified target format
- Comprehensive operation summary
```

## Key Assembly Principles

### 1. Sequential Flow
Components are arranged in logical order where each component's output feeds into the next component's expected input.

### 2. Error Propagation
Each component includes error handling that allows graceful failure without breaking the entire workflow.

### 3. Interface Compatibility
Components are selected based on compatible interfaces - file paths, content data, formatted output.

### 4. Tool Requirements
The `allowed-tools` field includes all tools required by the assembled components (Glob for search, Read for file access, etc.).

## Alternative Assembly Patterns

### Minimal Version (3 components)
```
file-reader → data-transformer → output-formatter
```

### Enhanced Version (with monitoring)
```
input-validation → search-files → file-reader → content-sanitizer → 
data-transformer → output-formatter → task-summary
```

### API Integration Version
```
input-validation → api-caller → response-validator → 
data-transformer → output-formatter
```

## Testing Your Assembly

1. **Validate Components**: Ensure all referenced components exist and are Grade B or higher
2. **Check Tool Requirements**: Verify allowed-tools includes all component requirements
3. **Test Workflow**: Use integration testing to validate component sequence
4. **Edge Case Testing**: Ensure error handling works across component boundaries

*Example demonstrates practical component assembly for real-world slash command creation*