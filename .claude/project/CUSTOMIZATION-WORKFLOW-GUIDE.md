# Template Customization Workflow Guide
*User Experience Enhancement - Step 89*

## The 5-Step Customization Process

### Step 1: Choose Installation Method 📥
Based on your needs and experience level:

**Beginners**: Method 2 (Direct Integration)
```bash
git clone https://github.com/swm-sink/claude-code-modular-prompts
cd claude-code-modular-prompts && ./setup.sh ../your-project
```

**Experienced Users**: Method 1 (Git Submodule) 
```bash
git submodule add https://github.com/swm-sink/claude-code-modular-prompts .claude-framework
cd .claude-framework && ./setup.sh
```

**Selective Users**: Method 3 (Manual Copy)
- Copy specific commands/components you need
- Ideal for experienced users who want minimal setup

### Step 2: Get Customization Guidance 📋
```
/adapt-to-project
```
This command provides:
- Project-specific customization checklist
- List of all placeholders that need replacement
- Recommended commands for your project type
- Step-by-step customization instructions

### Step 3: Replace Placeholders ✏️
```
/replace-placeholders
```
This command shows you:
- All [INSERT_XXX] placeholders in your templates
- Recommended replacements based on your project
- Files that need manual editing
- Find & Replace commands for your editor

**Common Placeholders**:
- `[INSERT_PROJECT_NAME]` → Your project name
- `[INSERT_TECH_STACK]` → Your technology stack  
- `[INSERT_DOMAIN]` → Your domain (web-dev, data-science, etc.)
- `[INSERT_COMPANY_NAME]` → Your organization
- `[INSERT_TEAM_SIZE]` → Your team size

### Step 4: Customize Templates 🔧
**Manual Work Required** (typically 1-2 hours):
1. Open your editor with Find & Replace capability
2. Work through the placeholder list systematically
3. Remove commands you don't need
4. Modify commands for your specific workflows
5. Test commands as you customize them

### Step 5: Validate Customization ✅
```
/validate-adaptation
```
This command provides:
- Checklist to verify your customizations
- Common issues to check for
- Validation of file structure
- Confirmation of successful customization

## User Experience Tips

### For New Users 🌱
- **Start Small**: Don't try to customize all 82 commands at once
- **Focus on Core**: Begin with 5-10 essential commands for your workflow
- **Learn by Doing**: Customize one command completely before moving to the next
- **Use Examples**: Check the examples/ directory for real implementation patterns

### For Experienced Users ⚡
- **Batch Processing**: Use powerful Find & Replace tools for efficient placeholder replacement
- **Component Assembly**: Use atomic components to build custom commands
- **Automation**: Set up pre-commit hooks to validate customizations
- **Selective Integration**: Only install commands you actually need

### Common UX Improvements Applied

1. **Clear Expectations**: Documentation now clearly states this requires manual work
2. **Step-by-Step Guidance**: Each command provides detailed usage instructions
3. **Progressive Disclosure**: Information organized by user experience level
4. **Error Prevention**: Validation commands help catch common mistakes
5. **Recovery Options**: Backup and rollback procedures documented

## Troubleshooting Common Issues

### "Too Many Commands" Feeling
- Use `/find-commands [category]` to focus on relevant commands
- Start with core category only
- Remove commands you don't need

### "Placeholder Overwhelm"
- Use `/replace-placeholders` to get organized list
- Work through placeholders systematically
- Focus on one file at a time

### "Customization Confusion"  
- Use `/adapt-to-project` for step-by-step guidance
- Read the SECURITY-GUIDELINES.md for best practices
- Check examples/ directory for real usage patterns

## Time Investment Expectations

- **Setup**: 15-30 minutes
- **Initial Customization**: 1-3 hours  
- **Ongoing Maintenance**: 15 minutes per update
- **Advanced Customization**: 4-8 hours for full template library

## Success Metrics

You'll know customization is successful when:
- `/validate-adaptation` shows all checks passing
- Commands work without placeholder errors
- Templates match your project's terminology and structure
- Team members can use commands effectively

**Remember**: This is a one-time investment that saves months of prompt engineering trial-and-error.
