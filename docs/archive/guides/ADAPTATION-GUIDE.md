# Adaptation Guide

## Template Customization Patterns

### Manual Customization Process

1. **Get Customization Checklist**
   ```bash
   /adapt-to-project     # Get project-specific customization guide
   ```

2. **Identify Placeholders to Replace**
   ```bash
   /replace-placeholders # Get list of all [INSERT_XXX] markers
   ```

3. **Manual Find & Replace Work**
   - Open files in your editor
   - Replace `[INSERT_PROJECT_NAME]` with your project name
   - Replace `[INSERT_DOMAIN]` with your domain (web-dev, data-science, etc.)
   - Replace `[INSERT_TECH_STACK]` with your technology stack
   - Replace `[INSERT_COMPANY_NAME]` with your organization
   - Replace `[INSERT_TEAM_SIZE]` with your team size

4. **Validate Adaptations**
   ```bash
   /validate-adaptation  # Get verification checklist
   ```

## Common Adaptation Patterns

### Web Development Projects
- Domain: "web-dev"
- Tech Stack: "React/Node.js" or "Vue/Express" etc.
- Common commands: /task, /review, /debug, /test

### Data Science Projects  
- Domain: "data-science"
- Tech Stack: "Python/Pandas" or "R/Tidyverse" etc.
- Common commands: /analyze, /task, /docs

### API Development
- Domain: "api-dev" 
- Tech Stack: "FastAPI/Python" or "Express/Node.js" etc.
- Common commands: /task, /test, /debug

## Customization Templates

### project-config.yaml (Manual Template)
```yaml
project_config:
  metadata:
    name: "[INSERT_PROJECT_NAME]"
    domain: "[INSERT_DOMAIN]"
  placeholders:
    TECH_STACK: "[INSERT_TECH_STACK]"
    WORKFLOW_TYPE: "[INSERT_WORKFLOW_TYPE]"
```

*Note: This is just a template - Claude Code commands cannot read or use this file.*

## Update Process

### Future Updates from Context Engineering System
```bash
/sync-from-reference  # Get manual update instructions
```

### Sharing Your Adaptations
```bash
/share-adaptation    # Create shareable pattern document
```

*See USAGE.md for command examples and CLAUDE.md for complete project context.*