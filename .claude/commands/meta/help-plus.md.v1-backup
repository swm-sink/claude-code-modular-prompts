---
name: /help-plus
description: Enhanced help system with error handling, troubleshooting, and user guidance
usage: '[command] [error] [troubleshoot]'
allowed-tools:
- Read
- LS
- Grep
category: meta
---

# /help-plus - Enhanced Help & Troubleshooting

Enhanced help system with error handling, troubleshooting guides, and user guidance for the template library.

## Usage Patterns

### Get Help for Specific Command
```
/help-plus /task              # Get detailed help for /task command
/help-plus /adapt-to-project  # Get help for adaptation command
```

### Troubleshoot Common Errors
```
/help-plus error placeholder   # Help with placeholder-related errors
/help-plus error permission    # Help with permission errors
/help-plus error validation    # Help with validation failures
```

### General Troubleshooting
```
/help-plus troubleshoot       # Show common issues and solutions
```

## Common Error Categories & Solutions

### 1. Placeholder Errors ⚠️
**Symptoms**: Commands fail with [INSERT_XXX] references
**Solution**:
1. Run `/replace-placeholders` to see all placeholders
2. Use Find & Replace in your editor to replace them
3. Run `/validate-adaptation` to verify fixes

### 2. Permission Errors 🔒
**Symptoms**: "Permission denied" or file access errors
**Solution**:
1. Check `.claude/settings.json` allowedPaths configuration
2. Ensure files are in allowed directories
3. Verify file permissions (readable/writable)

### 3. Validation Failures ❌
**Symptoms**: `/validate-adaptation` shows failures
**Solution**:
1. Check specific validation error messages
2. Fix issues one at a time
3. Re-run validation after each fix
4. Use `/help-plus error validation` for specific guidance

### 4. Setup Issues 🔧
**Symptoms**: Commands not found, setup script failures
**Solution**:
1. Verify installation method was completed
2. Check `.claude/commands/` directory exists
3. Verify setup script ran without errors
4. Use `/welcome` to restart onboarding process

### 5. Customization Confusion 🤔
**Symptoms**: Unsure how to customize templates
**Solution**:
1. Start with `/welcome` for experience-level guidance
2. Use `/adapt-to-project` for step-by-step help
3. Check `CUSTOMIZATION-WORKFLOW-GUIDE.md`
4. Start with fewer commands, expand gradually

## Troubleshooting Workflow

### Step 1: Identify Error Type
- **Template Error**: Contains [INSERT_XXX] placeholders
- **File Error**: Permission or path issues
- **Validation Error**: Command structure or content issues
- **Usage Error**: Incorrect command usage or expectations

### Step 2: Apply Specific Solution
- Use the relevant section above
- Follow step-by-step instructions
- Test after each fix

### Step 3: Verify Resolution
- Re-run the failing command
- Use validation commands to confirm fix
- Document what worked for future reference

## Quick Reference: Essential Commands

### For New Users
- `/welcome` - Start here for onboarding
- `/adapt-to-project` - Get customization guidance
- `/help-plus troubleshoot` - When things go wrong

### For Customization
- `/replace-placeholders` - See what needs replacement
- `/validate-adaptation` - Check your work
- `/find-commands [category]` - Discover relevant templates

### For Advanced Users  
- `/sync-from-reference` - Update templates
- `/share-adaptation` - Document your customization patterns

## When to Get Additional Help

If you're still stuck after following troubleshooting steps:
1. Check the SECURITY-GUIDELINES.md for security-related issues
2. Review the DOCUMENTATION-ACCURACY-REPORT.md for current project stats
3. Look at examples/ directory for working implementation patterns
4. Consider if your use case requires custom command development

## Pro Tips for Better UX

1. **Start Simple**: Begin with 3-5 core commands, expand gradually
2. **Document Changes**: Keep notes on your customizations
3. **Test Early**: Validate commands as you customize them
4. **Use Categories**: Focus on one command category at a time
5. **Backup Work**: Create backups before major customization sessions

**Remember**: This template library is designed for customization. The initial setup work pays off with months of saved prompt engineering time.
