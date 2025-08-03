# Simple Component Assembly Guide

## What Are Atomic Components?

Atomic components are small, reusable prompt snippets (5-10 lines each) that handle one specific task. Think of them as LEGO blocks for building slash commands.

## Available Components

| Component | Purpose |
|-----------|---------|  
| `input-validation.md` | Validate user input |
| `output-formatter.md` | Format response output |
| `error-handler.md` | Handle errors gracefully |
| `progress-indicator.md` | Show task progress |
| `file-reader.md` | Read file contents |
| `file-writer.md` | Write/update files |
| `search-files.md` | Search for patterns |
| `user-confirmation.md` | Confirm before actions |
| `task-summary.md` | Summarize completed work |
| `parameter-parser.md` | Parse command arguments |

## How to Assemble Components

1. **Pick components** based on what your command needs
2. **Copy their content** into your command file
3. **Arrange in order**: Input → Process → Output
4. **Add transitions** between components if needed

## Quick Example

To build a "rename files" command:

```markdown
---
name: /rename-files
description: "Rename files matching a pattern"
usage: "[old-pattern] [new-pattern]"
tools: Glob, Edit
---

# Rename Files Command

[Copy parameter-parser.md here]
[Copy input-validation.md here]
[Copy search-files.md here]
[Copy user-confirmation.md here]
[Copy progress-indicator.md here]
[Copy file-writer.md here]
[Copy task-summary.md here]
```

## Best Practices

✅ **DO:**
- Use only the components you need
- Keep commands focused on one task
- Test with real inputs

❌ **DON'T:**
- Over-complicate with too many components
- Create components larger than 10 lines
- Nest components within components

## That's It!

No complex frameworks. No orchestration. Just copy, paste, and customize.