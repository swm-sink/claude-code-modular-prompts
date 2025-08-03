# Example: Building a Slash Command from Atomic Components

This example shows how to combine atomic components to create a file search command.

## Step 1: Create the Command File

Create `.claude/commands/search-project.md`:

```markdown
---
name: /search-project
description: "Search for patterns in project files"
usage: "[search term] [--type file-extension]"
tools: Grep, Glob, Read
---

# Search Project Files

I'll search for "$ARGUMENTS" in your project files.

<!-- Component: parameter-parser.md -->
Parse command arguments:
- Extract named parameters (--flag value)
- Handle positional arguments
- Set defaults for missing values
- Validate parameter combinations

<!-- Component: input-validation.md -->
Validate the provided input:
- Check for required parameters
- Verify data types match expectations  
- Return clear error messages if validation fails
- Continue only with valid inputs

<!-- Component: progress-indicator.md -->
Show progress throughout the task:
- "Starting [task name]..."
- "Completed step X of Y"
- "Processing [current item]..."
- "Task completed successfully"

<!-- Component: search-files.md -->
To search for content:
- Use Grep for text patterns
- Use Glob for file patterns
- Combine both for targeted searches
- Report findings clearly

<!-- Component: error-handler.md -->
If an error occurs:
- Identify the error type (user input, system, logic)
- Provide a clear, actionable error message
- Suggest next steps to resolve
- Log the error for debugging

<!-- Component: output-formatter.md -->
Format the output as follows:
- Use clear headers for sections
- Bullet points for lists
- Code blocks for technical content
- Concise summaries at the end

<!-- Component: task-summary.md -->
After completing work:
- List what was accomplished
- Note any issues encountered
- Suggest next steps if relevant
- Keep it concise (3-5 bullets)
```

## Step 2: How It Works

1. **Copy the component content** directly into your command
2. **Arrange components** in logical order (parse → validate → execute → output)
3. **Add connecting text** between components as needed
4. **Test the command** with various inputs

## Step 3: Using the Command

```bash
# Search for a term
/search-project TODO

# Search with file type filter
/search-project "handleError" --type js
```

## Benefits of This Approach

✅ **Reusable**: Each component can be used in multiple commands
✅ **Simple**: Just copy and paste the components you need
✅ **Maintainable**: Update a component once, benefit everywhere
✅ **Clear**: Each component has a single responsibility

## Tips

- Start with essential components (validation, error handling)
- Add optional components based on command complexity
- Keep component order consistent across commands
- Test with edge cases (missing arguments, invalid input)