| version | last_updated | status |
|---------|--------------|--------|
| 3.0.0   | 2025-07-07   | stable |


# Prompt Naming Conventions


# Overview
This document defines the naming conventions for prompts in the Claude Code Modular Prompts framework to ensure consistency, discoverability, and maintainability.


# File Naming Convention


# Format
```
<category>-<subcategory>-<descriptive-name>-v<version>.json
```


# Rules
1. **All lowercase**: Use only lowercase letters
2. **Hyphen separation**: Use hyphens (-) to separate words
3. **No spaces or underscores**: Replace with hyphens
4. **Version suffix**: Always include version (e.g., v1.0.0)
5. **JSON extension**: All prompt files use .json extension


# Examples
- ✅ `queries-code-analysis-v1.0.0.json`
- ✅ `features-api-endpoint-implementation-v2.1.0.json`
- ✅ `patterns-multi-agent-coordination-v1.5.2.json`
- ❌ `Queries_Code_Analysis_v1.json` (wrong case, underscores)
- ❌ `features-api-endpoint.json` (missing version)


# Prompt ID Convention


# Format
```
<category>-<subcategory>-<unique-identifier>
```


# Rules
1. **Unique within framework**: Must be globally unique
2. **Descriptive**: Should indicate prompt purpose
3. **No version in ID**: Version tracked separately
4. **Alphanumeric with hyphens**: Only a-z, 0-9, and hyphens


# Examples
- ✅ `code-analysis-comprehensive`
- ✅ `api-endpoint-rest-implementation`
- ✅ `security-audit-owasp-full`
- ❌ `code_analysis_v1` (underscores, version in ID)


# Category Naming


# Primary Categories
- `queries` - Information retrieval and analysis
- `features` - Feature development and implementation
- `reviews` - Code review and quality assurance
- `patterns` - Reusable patterns and architectures
- `templates` - Meta-templates for creating prompts


# Subcategories
Common subcategories by primary category:


# Queries
- `code-analysis` - Code quality and structure analysis
- `architecture-review` - System architecture analysis
- `dependency-scan` - Dependency analysis
- `performance-profile` - Performance analysis


# Features
- `api-endpoint` - API endpoint implementations
- `ui-component` - UI component development
- `database-schema` - Database design
- `integration` - Service integrations


# Reviews
- `security-audit` - Security reviews
- `code-review` - Code quality reviews
- `performance-review` - Performance optimization
- `accessibility-audit` - Accessibility reviews


# Patterns
- `multi-agent` - Multi-agent patterns
- `error-handling` - Error handling patterns
- `authentication` - Auth patterns
- `data-flow` - Data flow patterns


# Version Naming


# Semantic Versioning
Follow semantic versioning (MAJOR.MINOR.PATCH):

- **MAJOR**: Breaking changes to template structure
- **MINOR**: New features or non-breaking changes
- **PATCH**: Bug fixes or minor improvements


# Examples
- `1.0.0` - Initial release
- `1.1.0` - Added new variables
- `1.1.1` - Fixed typo in template
- `2.0.0` - Changed template structure


# Tag Naming


# Format
- All lowercase
- Hyphen separated
- Descriptive and specific


# Common Tags
- **By Function**: `analysis`, `implementation`, `review`, `audit`
- **By Domain**: `security`, `performance`, `api`, `database`
- **By Language**: `python`, `javascript`, `go`, `rust`
- **By Pattern**: `multi-agent`, `async`, `distributed`
- **By Quality**: `testing`, `documentation`, `refactoring`


# Archive Naming

When archiving old versions:


# Directory Structure
```
archived/
  v1/
    <original-filename>
  v2/
    <original-filename>
```


# Naming Format
Archived files keep original names but are organized by major version.


# Special Naming Cases


# Experimental Prompts
Prefix with `experimental-`:
```
experimental-<category>-<name>-v0.1.0.json
```


# Deprecated Prompts
Add `-deprecated` suffix before version:
```
<category>-<name>-deprecated-v1.0.0.json
```


# Template Prompts
For meta-templates that generate other prompts:
```
templates-prompt-generator-<type>-v1.0.0.json
```


# Best Practices

1. **Be Descriptive**: Names should clearly indicate purpose
2. **Keep It Concise**: Avoid overly long names
3. **Use Common Terms**: Stick to widely understood terminology
4. **Version Everything**: Always include version numbers
5. **Document Changes**: Update changelog for each version
6. **Avoid Abbreviations**: Use full words for clarity
7. **Test Names**: Ensure names work across different filesystems


# Examples of Good vs Bad Names


# Good Names ✅
- `queries-code-complexity-analysis-v1.0.0.json`
- `features-rest-api-crud-generator-v2.1.0.json`
- `reviews-security-penetration-test-v1.5.0.json`
- `patterns-event-driven-architecture-v3.0.0.json`


# Bad Names ❌
- `CodeAnalysis.json` (wrong case, no version)
- `api_endpoint_impl_v1.json` (underscores, abbreviation)
- `security-review-final-final-v2.json` (redundant words)
- `pattern1.json` (not descriptive)