# Context Pattern Quick Reference Guide

## 🚀 Ready-to-Use Patterns

### File Processing Workflow
```
search-files → file-reader → content-sanitizer → data-transformer → output-formatter
```
**Use for**: Processing files with security checks and format conversion

### API Integration Workflow  
```
api-caller → response-validator → data-transformer → output-formatter
```
**Use for**: Making API calls with validation and formatting

### User Input Workflow
```
input-validation → parameter-parser → file-reader
```
**Use for**: Processing user commands with file access

### Complex Workflow Management
```
dependency-resolver → state-manager → workflow-coordinator → completion-tracker
```
**Use for**: Multi-step processes requiring coordination

## ⭐ Top Grade A Context Patterns (Production Ready)

### git-operations.md (100%)
```markdown
Execute git repository operations with validation:
- Parse git command specifications and validate syntax
- Verify repository access and branch permissions before execution
- Execute git commands using proper error handling and logging
- Monitor command output for conflicts and merge issues
- Generate detailed execution reports with commit hashes and status
- Handle authentication failures and permission errors gracefully
```

### file-reader.md (100%)
```markdown
Read file contents with error handling:
- Validate file path format and accessibility permissions
- Execute Read tool with absolute path and optional line limits
- Parse file content according to detected file type (text, binary, structured)
- Handle file not found errors with specific path recommendations
- Extract and return relevant content sections based on requirements
- Generate structured report of read operation results and metadata
```

### dependency-resolver.md (100%)
```markdown
Resolve component and resource dependencies:
- Parse dependency specifications from manifest files
- Verify dependency availability in specified locations
- Detect and resolve version conflicts using semantic versioning
- Execute dependency loading in topological order
- Report missing dependencies with specific installation commands
- Handle circular dependencies with clear error messages
```

### state-manager.md (100%)
```markdown
Coordinate command execution state management:
- Initialize state variables from parsed configuration file parameters
- Track workflow progress using timestamped checkpoint files
- Execute atomic state transitions with immediate rollback on errors
- Validate state consistency using checksum verification across operations
- Persist state changes to designated JSON/YAML storage files  
- Generate state reports with detailed error messages and recovery steps
```

## 🎯 Most Useful Grade B Components

### input-validation.md (83.3%)
```markdown
Validate user input with comprehensive error checking:
- Check input format matches expected patterns and data types
- Verify required fields are present and contain valid values
- Validate input ranges and constraints according to business rules
- Ensure data consistency across related input fields
- Generate specific error messages for validation failures with correction guidance
- Return validated data structure for further processing
```

### output-formatter.md (83.3%)
```markdown
Format output with structured presentation:
- Parse input data and detect current format (JSON, YAML, plain text)
- Apply consistent headers with hierarchical numbering for sections
- Generate bullet points with proper indentation for list structures
- Wrap technical content in appropriate code blocks with syntax highlighting
- Handle unsupported formats using markdown fallback with clear labels
- Create concise summaries with key metrics and actionable next steps
```

### task-summary.md (83.3%)
```markdown
Generate comprehensive task completion summary:
- Review input task list and completion status data
- Document specific tasks completed with measurable results
- Identify and categorize any issues or blockers encountered
- Handle missing or incomplete task information gracefully
- Provide clear, actionable next steps with priorities
- Validate summary completeness against original objectives  
- Format output as structured report with clear sections
```

## 🔧 Common Usage Patterns

### Start Any Workflow
- `input-validation` - For user input
- `search-files` - For file discovery
- `parameter-parser` - For command arguments

### Process Data
- `file-reader` → `content-sanitizer` → `data-transformer`
- `api-caller` → `response-validator` → `format-converter`

### Finish Any Workflow
- `output-formatter` - For display
- `file-writer` - For saving results  
- `task-summary` - For completion reports

### Add Throughout
- `progress-indicator` - Show progress
- `error-handler` - Handle failures
- `user-confirmation` - Before destructive actions

## 📊 Quality Distribution
- **Grade A (4)**: git-operations, file-reader, dependency-resolver, state-manager
- **Grade B (10)**: Most user interaction and processing components
- **Grade D (7)**: Functional but may need customization
- **Grade F (0)**: All failing components eliminated

*Quick reference guide for immediate component usage*