# Installation Guide

> **Quick Setup**: Most users should start with [Quick Start](quick-start.md) for immediate productivity.

This guide covers complete installation options for different scenarios.

## 🎯 Choose Your Installation Method

### 🚀 Automatic Setup (Recommended)
Best for most users - framework analyzes and configures automatically.

#### New Projects
```bash
# Copy framework files
cp -r claude-code-modular-prompts/.claude your-new-project/
cp claude-code-modular-prompts/CLAUDE.md your-new-project/
cd your-new-project/

# Interactive setup wizard
/init-new
# → Asks about tech stack, domain, quality standards
# → Generates optimized PROJECT_CONFIG.xml
# → Framework instantly adapts to your choices
```

#### Existing Projects
```bash
# Copy framework files
cp -r claude-code-modular-prompts/.claude your-project/
cp claude-code-modular-prompts/CLAUDE.md your-project/
cd your-project/

# Automatic codebase analysis
/init-custom
# → Analyzes existing code and patterns
# → Detects tech stack and conventions
# → Generates PROJECT_CONFIG.xml automatically
```

#### Research-Driven Setup
```bash
# Copy framework files
cp -r claude-code-modular-prompts/.claude your-project/
cp claude-code-modular-prompts/CLAUDE.md your-project/
cd your-project/

# Evidence-based configuration
/init-research
# → Researches 2025 best practices for your domain
# → Applies latest patterns and standards
# → Creates optimized configuration
```

### ⚙️ Manual Setup
For users who need full control over configuration.

#### Step 1: Copy Core Files
```bash
# Clone framework repository
git clone https://github.com/swm-sink/claude-code-modular-prompts.git

# Copy framework to your project
cp -r claude-code-modular-prompts/.claude your-project/
cp claude-code-modular-prompts/CLAUDE.md your-project/
cp claude-code-modular-prompts/PROJECT_CONFIG.xml your-project/

cd your-project/
```

#### Step 2: Choose Configuration Template
```bash
# Option A: Use generic template (comes by default)
# PROJECT_CONFIG.xml is ready to use with sensible defaults

# Option B: Use domain-specific template
cp examples/project-configs/web-react-typescript.xml PROJECT_CONFIG.xml
cp examples/project-configs/data-science-python.xml PROJECT_CONFIG.xml
cp examples/project-configs/mobile-react-native.xml PROJECT_CONFIG.xml
cp examples/project-configs/api-microservices.xml PROJECT_CONFIG.xml
```

#### Step 3: Customize Configuration
Edit `PROJECT_CONFIG.xml` to match your project:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project_configuration version="1.0.0">
  <project_info>
    <name>My Project</name>
    <domain>web-development</domain>  <!-- Choose: web-development, mobile-development, data-science, devops-platform -->
    <primary_language>typescript</primary_language>
    <framework_stack>react+nextjs+tailwind</framework_stack>
  </project_info>
  
  <project_structure>
    <source_directory>src</source_directory>
    <test_directory>tests</test_directory>
    <docs_directory>docs</docs_directory>
  </project_structure>
  
  <quality_standards>
    <test_coverage>
      <threshold>90</threshold>
      <enforcement>BLOCKING</enforcement>
    </test_coverage>
  </quality_standards>
</project_configuration>
```

## 🔍 Verification Steps

### 1. Test Basic Functionality
```bash
# Verify framework recognizes your project
/query "what type of project is this?"

# Should return analysis based on your PROJECT_CONFIG.xml settings
```

### 2. Test Command Routing
```bash
# Test intelligent routing
/auto "analyze the codebase structure"

# Should route appropriately and provide project-specific analysis
```

### 3. Test Domain Adaptation
```bash
# Test domain-specific behavior
/task "add a simple helper function"

# Should create code using patterns appropriate for your tech stack
```

### 4. Validate Configuration
```bash
# Run configuration validator (optional)
python scripts/framework/config_validator.py

# Check template resolution (optional)
python scripts/framework/template_resolver.py --text "Tests go in [PROJECT_CONFIG: test_directory | DEFAULT: tests]"
```

## 🛠️ Advanced Installation Options

### Team Installation
For teams wanting shared configuration:

```bash
# 1. Setup framework as above
# 2. Create team configuration
cp PROJECT_CONFIG.xml PROJECT_CONFIG_TEAM.xml

# 3. Share team config
git add PROJECT_CONFIG_TEAM.xml CLAUDE.md .claude/
git commit -m "Add Claude Code Framework configuration"

# 4. Team members can use:
cp PROJECT_CONFIG_TEAM.xml PROJECT_CONFIG.xml
```

### Multi-Project Installation
For working across multiple projects:

```bash
# Create shared framework location
git clone https://github.com/swm-sink/claude-code-modular-prompts.git ~/claude-framework

# Link to projects (symlinks for easy updates)
ln -s ~/claude-framework/.claude your-project1/.claude
ln -s ~/claude-framework/CLAUDE.md your-project1/CLAUDE.md

# Copy project-specific config
cp ~/claude-framework/PROJECT_CONFIG.xml your-project1/PROJECT_CONFIG.xml
# Customize your-project1/PROJECT_CONFIG.xml as needed
```

### Container Installation
For containerized development:

```bash
# Add to your Dockerfile
COPY .claude/ /app/.claude/
COPY CLAUDE.md /app/
COPY PROJECT_CONFIG.xml /app/

# Or mount as volume for development
docker run -v $(pwd)/.claude:/app/.claude -v $(pwd)/CLAUDE.md:/app/CLAUDE.md your-image
```

## 🚧 Troubleshooting

### Common Issues

#### "Permission denied" errors
```bash
# Fix permissions (macOS/Linux)
chmod +x .claude/commands/*
chmod -R u+r .claude/

# Alternative: Copy files with correct permissions
cp -a claude-code-modular-prompts/.claude your-project/
```

#### "Framework not detected" errors
```bash
# Ensure files are in correct location
ls -la CLAUDE.md PROJECT_CONFIG.xml .claude/

# Framework must detect CLAUDE.md in project root
pwd  # Should be your project directory
```

#### "Configuration invalid" errors
```bash
# Validate XML syntax
python scripts/framework/config_validator.py

# Check for required fields
grep -E '<name>|<domain>|<primary_language>' PROJECT_CONFIG.xml
```

#### "Commands not working" errors
```bash
# Test basic framework loading
/query "framework status"

# Check command files exist
ls .claude/commands/

# Verify directory structure
tree .claude/ -L 2
```

### Performance Issues

#### Slow command responses
```bash
# Optimize configuration
/meta-optimize "improve response time"

# Check for large files in project
find . -size +10M -not -path "./.git/*"

# Simplify PROJECT_CONFIG.xml if overly complex
```

#### High memory usage
```bash
# Check context optimization
/meta-review "analyze memory usage"

# Exclude large directories from analysis
echo "node_modules/" >> .gitignore
echo "build/" >> .gitignore
```

### Domain-Specific Issues

#### Web Development
```bash
# Ensure Node.js tools are available
npm --version
npx --version

# Configure for your specific stack
<framework_stack>react+typescript+vite</framework_stack>
```

#### Data Science
```bash
# Ensure Python environment is active
python --version
pip --version

# Configure for your environment
<framework_stack>pandas+scikit-learn+jupyter</framework_stack>
```

#### Mobile Development
```bash
# Configure for your platform
<framework_stack>react-native+expo</framework_stack>  # React Native
<framework_stack>flutter+dart</framework_stack>      # Flutter
<framework_stack>swiftui+combine</framework_stack>   # iOS Native
```

## ✅ Installation Verification Checklist

- [ ] Framework files copied to project directory
- [ ] `CLAUDE.md` exists in project root
- [ ] `PROJECT_CONFIG.xml` configured for your project
- [ ] `/query` command returns project analysis
- [ ] `/auto` command routes intelligently
- [ ] Framework produces code appropriate for your tech stack
- [ ] No permission or access errors
- [ ] Configuration validates successfully

## 🎯 Next Steps

### Immediate (Today)
- **Learn core commands**: [First Commands](first-commands.md)
- **Try basic workflows**: [Common Patterns](../user-guide/workflows/common-patterns.md)

### This Week
- **Master command selection**: [Command Guide](../user-guide/commands/)
- **Customize for your team**: Team Configuration

### Ongoing
- **Optimize performance**: Performance Guide
- **Extend functionality**: [Custom Modules](../advanced/extending-framework.md)

---

**Installation complete?** Continue to [First Commands](first-commands.md) to learn essential framework usage.

**Still having issues?** Check [detailed troubleshooting](../reference/troubleshooting.md) or start over with [Quick Start](quick-start.md).