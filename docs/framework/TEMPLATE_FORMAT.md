# Prompt Template Format Specification


# Overview
This document defines the standard format for creating and storing prompts in the Claude Code Modular Agents framework.


# Template Format


# 1. Variable Syntax
Variables in prompts use double curly braces: `{{variable_name}}`

```
Example: "Analyze the {{language}} code in {{file_path}} for {{analysis_type}}"
```


# 2. Conditional Sections
Use conditional blocks for optional content:
```
{{#if include_tests}}
Also generate comprehensive test cases for the implementation.
{{/if}}
```


# 3. Loops
For repeating sections with arrays:
```
{{#each requirements}}
- {{this.name}}: {{this.description}}
{{/each}}
```


# 4. Default Values
Specify defaults in the template:
```
{{timeout|default:120}} seconds timeout
```


# File Naming Convention


# Standard Format
`<category>-<subcategory>-<name>-v<version>.json`

Examples:
- `queries-code-analysis-v1.0.0.json`
- `features-api-endpoint-v2.1.0.json`
- `patterns-multi-agent-v1.5.2.json`


# Categories
- **queries**: Information retrieval and analysis prompts
- **features**: Feature development and implementation prompts
- **reviews**: Code review and quality assurance prompts
- **patterns**: Reusable pattern and architecture prompts
- **templates**: Meta-templates for creating other prompts


# Prompt Structure


# Basic Structure
```json
{
  "id": "unique-prompt-id",
  "version": "1.0.0",
  "category": "features",
  "name": "Human Readable Name",
  "description": "What this prompt does",
  "prompt": {
    "template": "The actual prompt text with {{variables}}",
    "variables": [
      {
        "name": "variable_name",
        "description": "What this variable represents",
        "type": "string",
        "required": true,
        "examples": ["example1", "example2"]
      }
    ]
  },
  "metadata": {
    "created": "2025-07-07T00:00:00Z",
    "updated": "2025-07-07T00:00:00Z",
    "author": "system",
    "tags": ["development", "automation"]
  }
}
```


# Best Practices


# 1. Clarity
- Use clear, descriptive variable names
- Provide comprehensive descriptions
- Include examples for complex prompts


# 2. Modularity
- Keep prompts focused on a single task
- Use dependencies for complex workflows
- Avoid prompt duplication


# 3. Versioning
- Follow semantic versioning (MAJOR.MINOR.PATCH)
- Document all changes in changelog
- Maintain backward compatibility when possible


# 4. Performance
- Estimate token usage accurately
- Optimize prompt length without sacrificing clarity
- Consider computational complexity


# 5. Validation
- Define clear success criteria
- Specify expected output format
- Include validation schemas for structured outputs


# Template Types


# 1. Simple Templates
Direct text replacement:
```
"Implement a {{component_type}} component named {{component_name}}"
```


# 2. Complex Templates
Multi-part prompts with conditions:
```
"Analyze {{target}} for:
{{#each analysis_types}}
- {{this}}
{{/each}}
{{#if include_recommendations}}
Provide specific recommendations for improvement.
{{/if}}"
```


# 3. Structured Output Templates
Templates expecting specific output formats:
```json
{
  "template": "Generate a REST API endpoint specification",
  "outputFormat": "json",
  "outputSchema": {
    "type": "object",
    "properties": {
      "endpoint": {"type": "string"},
      "method": {"type": "string"},
      "parameters": {"type": "array"}
    }
  }
}
```


# Integration with Framework


# 1. Command Integration
Prompts can be referenced by commands:
```markdown
/task --prompt=features-api-endpoint-v1.0.0
```


# 2. Multi-Agent Coordination
Prompts support agent specialization:
```json
{
  "metadata": {
    "agentType": "backend-specialist",
    "coordinationLevel": "high"
  }
}
```


# 3. Session Management
Prompts can define session requirements:
```json
{
  "metadata": {
    "requiresSession": true,
    "estimatedDuration": 300
  }
}
```