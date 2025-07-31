# Advanced User Quick Start Example
*For experienced Claude Code users who want efficient template integration*

## Scenario: Senior Developer, Multiple Projects, Selective Integration

### Step 1: Selective Installation (10 minutes)
```bash
# Use git submodule for easy updates
git submodule add https://github.com/swm-sink/claude-code-modular-prompts .claude-framework

# Create custom selection script
cat > selective-setup.sh << 'EOF'
#!/bin/bash
mkdir -p .claude/commands/{core,quality,specialized}
mkdir -p .claude/components/atomic

# Copy only needed commands
cp .claude-framework/.claude/commands/core/{task,analyze,review}.md .claude/commands/core/
cp .claude-framework/.claude/commands/quality/{test,validate}.md .claude/commands/quality/
cp .claude-framework/.claude/commands/specialized/api-design.md .claude/commands/specialized/

# Copy atomic components for custom building
cp .claude-framework/.claude/components/atomic/*.md .claude/components/atomic/

# Copy security and performance configs
cp .claude-framework/.claude/{security_config.json,command_cache.json} .claude/
EOF
chmod +x selective-setup.sh && ./selective-setup.sh
```

### Step 2: Batch Placeholder Replacement (15 minutes)
```bash
# Create project config
cat > project-config.json << 'EOF'
{
  "project_name": "Enterprise API Platform",
  "tech_stack": "Node.js, TypeScript, PostgreSQL, Docker, Kubernetes",
  "domain": "backend-api",
  "company_name": "TechCorp",
  "team_size": "12"
}
EOF

# Batch replace with sed/awk
find .claude/commands -name "*.md" -exec sed -i ''   -e 's/\[INSERT_PROJECT_NAME\]/Enterprise API Platform/g'   -e 's/\[INSERT_TECH_STACK\]/Node.js, TypeScript, PostgreSQL, Docker, K8s/g'   -e 's/\[INSERT_DOMAIN\]/backend-api/g'   -e 's/\[INSERT_COMPANY_NAME\]/TechCorp/g'   -e 's/\[INSERT_TEAM_SIZE\]/12/g' {} \;
```

### Step 3: Custom Command Assembly (20 minutes)
```bash
# Build custom deployment command from atomic components
cat > .claude/commands/specialized/deploy.md << 'EOF'
---
name: /deploy
description: Custom deployment workflow for Enterprise API Platform
usage: '[environment] [version]'
allowed-tools: [Bash, Read, Write]
category: specialized
---

# /deploy - Enterprise API Deployment

$(cat .claude/components/atomic/input-validation.md | tail -n +6)
$(cat .claude/components/atomic/file-reader.md | tail -n +6)
$(cat .claude/components/atomic/progress-indicator.md | tail -n +6)

## Deployment Process for TechCorp Enterprise API Platform

[Custom deployment logic specific to your infrastructure]
EOF
```

### Step 4: Automation Setup (10 minutes)
```bash
# Set up pre-commit validation
cat > .git/hooks/pre-commit << 'EOF'
#!/bin/bash
python3 .claude-framework/enhanced-validation-framework.py
if [ $? -ne 0 ]; then
  echo "❌ Template validation failed"
  exit 1
fi
EOF
chmod +x .git/hooks/pre-commit

# Set up periodic updates
echo "0 9 * * 1 cd $(pwd) && git submodule update --remote" | crontab -
```

### Step 5: Team Integration (5 minutes)
```bash
# Document your customization pattern
cat > TEAM-TEMPLATE-GUIDE.md << 'EOF'
# Team Template Usage Guide
- Use /task for development workflows
- Use /analyze for code review prep
- Use /test for comprehensive testing
- Use /deploy for production deployments

## Custom Commands Built:
- /deploy: Kubernetes deployment workflow
- /api-design: TechCorp API standards compliance
EOF

# Commit customized templates
git add .claude/ TEAM-TEMPLATE-GUIDE.md
git commit -m "Add customized Claude Code templates for Enterprise API Platform"
```

## Total Time Investment: ~1 hour
## Result: 
- 6 highly customized commands
- 1 custom-built command using atomic components  
- Automated validation and updates
- Team documentation and integration

## Advanced Benefits Achieved
- **Efficiency**: Batch processing saved manual work
- **Customization**: Built custom commands using atomic components
- **Automation**: Pre-commit hooks and update scheduling
- **Team Integration**: Documented patterns for team adoption
- **Maintenance**: Automated updates from template library
