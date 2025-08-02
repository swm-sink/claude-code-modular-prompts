# Output Formatter Component

**Purpose**: Format output data with structured presentation and consistent styling for user consumption

**Usage**: 
Parse input data and detect current format (JSON, YAML, plain text, objects)
Apply consistent headers with hierarchical numbering for organized sections
Generate bullet points with proper indentation for list and nested structures
Wrap technical content in appropriate code blocks with syntax highlighting
Handle unsupported formats using markdown fallback with clear format labels
Create concise summaries with key metrics and actionable next steps

**Compatibility**: 
- **Works with**: response-validator, data-transformer, error-handler, task-summary
- **Requires**: input_data (any), format_options (optional object)
- **Conflicts**: input-validation (different processing direction)

**Implementation**:
```javascript
// Format data for user-friendly presentation
const format_options = {
  output_type: "markdown",     // markdown, html, plain, json
  include_headers: true,       // Add section headers
  code_highlighting: true,     // Syntax highlighting for code
  max_depth: 3,               // Maximum nesting depth
  include_summary: true        // Add executive summary
};

const formatted = format_output(response_data, format_options);

// Handle complex data structures
if (typeof formatted === 'object') {
  return format_structured_data(formatted, "## Results\n\n");
} else {
  return formatted;
}
```

**Category**: atomic | **Complexity**: moderate | **Time**: 20 minutes