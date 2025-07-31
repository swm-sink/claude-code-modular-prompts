---
name: /find-duplicates
description: Find duplicate files in your project
usage: '[file-pattern] [--type extension]'
allowed-tools:
- Glob
- Read
- Grep
category: find-duplicates.md
---

# Find Duplicate Files

I'll help you find duplicate files in your project based on the pattern: $ARGUMENTS

## Parse Arguments
Parse command arguments:
- Extract named parameters (--flag value)
- Handle positional arguments
- Set defaults for missing values
- Validate parameter combinations

## Validate Input
Validate the provided input:
- Check for required parameters
- Verify data types match expectations  
- Return clear error messages if validation fails
- Continue only with valid inputs

## Show Progress
Show progress throughout the task:
- "Starting duplicate file search..."
- "Scanning project files..."
- "Analyzing file contents..."
- "Search completed successfully"

## Search for Files
To search for content:
- Use Glob for file patterns
- Read file contents for comparison
- Track files with identical content
- Group duplicates together

## Handle Errors
If an error occurs:
- Identify the error type (file access, invalid pattern)
- Provide a clear, actionable error message
- Suggest next steps to resolve
- Continue with remaining files if possible

## Format Results
Format the output as follows:
- Use clear headers for duplicate groups
- List file paths under each group
- Show file sizes for context
- Highlight the most recent version

## Summarize Findings
After completing work:
- Report total duplicates found
- Calculate space that could be saved
- Suggest which files might be safe to remove
- Keep summary concise (3-5 bullets)