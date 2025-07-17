# Getting Started with Claude Code Framework

Welcome! This guide will help you install, configure, and run your first commands with the Claude Code Framework.

## 🎯 What You'll Accomplish

By the end of this guide, you will:
- Have the framework installed and working
- Understand the core concepts and terminology
- Successfully execute your first framework command
- Be ready to explore individual command examples

**Estimated Time**: 15-30 minutes

## 📋 Prerequisites

Before starting, ensure you have:
- **Programming Experience**: Basic familiarity with any programming language
- **Command Line**: Comfortable using terminal/command prompt
- **Text Editor**: Any text editor or IDE for configuration files
- **Git**: Installed and configured (for project management)

## 🚀 Installation

### Step 1: Install Claude Code

Choose your platform:

#### macOS
```bash
# Using Homebrew (recommended)
brew install claude-code

# Or download from releases
curl -sSL https://get.claude.ai/code | bash
```

#### Linux
```bash
# Using package manager
sudo apt install claude-code  # Ubuntu/Debian
sudo yum install claude-code  # CentOS/RHEL

# Or using install script
curl -sSL https://get.claude.ai/code | bash
```

#### Windows
```powershell
# Using winget
winget install AnthropicAI.ClaudeCode

# Or download installer from releases page
```

### Step 2: Verify Installation

Test that the installation worked:

```bash
# Check version
claude-code --version

# Expected output:
# Claude Code v3.0.0
```

If you see version information, installation was successful! 🎉

### Step 3: Initial Setup

Configure your environment:

```bash
# Set up authentication (follow prompts)
claude-code auth login

# Initialize framework in a test directory
mkdir test-project
cd test-project
claude-code init
```

## 🧠 Core Concepts

Before diving into commands, understand these fundamental concepts:

### Framework Commands
The framework provides several commands, each for different purposes:

- **`/auto`** - Intelligent routing that decides the best approach
- **`/task`** - Focused development for single components or functions  
- **`/query`** - Research and analysis of existing code
- **`/feature`** - Complete feature development from planning to implementation
- **`/session`** - Extended work sessions with context preservation

### PROJECT_CONFIG.xml
This file tells the framework about your project:
- Programming language and framework
- Directory structure and conventions  
- Quality standards and preferences
- Tool integrations and workflows

### Quality Gates
Automatic checks that ensure code quality:
- Test-driven development (TDD) enforcement
- Code coverage requirements
- Performance standards
- Security validations

### CLAUDE.md
The framework control document that:
- Enables framework features in your project
- Provides project-specific guidance
- Integrates with your development workflow

## 🎮 Your First Command

Let's run your first framework command to make sure everything works.

### Step 1: Create a Test Project

```bash
# Create and enter a new directory
mkdir my-first-framework-test
cd my-first-framework-test

# Initialize as a git repository
git init

# Create a simple file to work with
echo "print('Hello, Framework!')" > hello.py
```

### Step 2: Run Your First Command

```bash
# Use auto command to analyze and improve the file
/auto "analyze the hello.py file and suggest improvements"
```

### Expected Response

The framework should respond with something like:

```
🔍 ANALYZING PROJECT CONTEXT...
- Language: Python detected
- File: hello.py (simple script)
- Framework: Not configured yet

📋 ANALYSIS RESULTS:
✅ Valid Python syntax
✅ Functional code structure
⚠️  Missing PROJECT_CONFIG.xml configuration
⚠️  No testing framework detected

💡 SUGGESTED IMPROVEMENTS:
1. Add PROJECT_CONFIG.xml for better framework integration
2. Consider adding a main() function for better structure
3. Add docstring for documentation
4. Set up testing framework (pytest recommended)

🎯 NEXT STEPS:
- Run: /task "add main function and docstring to hello.py"
- Create: PROJECT_CONFIG.xml configuration file
- Setup: Testing framework for quality assurance
```

If you see a similar response, congratulations! The framework is working correctly. 🎉

### Step 3: Try a Simple Task

Let's make an improvement:

```bash
# Use task command to improve the file
/task "add a main function and docstring to hello.py following Python best practices"
```

The framework will:
1. Create tests first (TDD approach)
2. Implement the improvements
3. Verify tests pass
4. Provide the enhanced code

## 📁 Project Structure

After running commands, your project structure might look like:

```
my-first-framework-test/
├── hello.py              # Your original file (now improved)
├── test_hello.py         # Tests created by framework
├── PROJECT_CONFIG.xml    # Auto-generated configuration
└── .claude/              # Framework data (auto-created)
    ├── session.json      # Session information
    └── context/          # Project context cache
```

## ⚙️ Basic Configuration

The framework works better with a PROJECT_CONFIG.xml file. Here's a minimal example:

### Create PROJECT_CONFIG.xml

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project_configuration version="1.0.0">
  <project_info>
    <name>my-first-framework-test</name>
    <domain>general-development</domain>
    <primary_language>python</primary_language>
  </project_info>
  
  <project_structure>
    <source_directory>src</source_directory>
    <test_directory>tests</test_directory>
    <docs_directory>docs</docs_directory>
  </project_structure>
  
  <development_workflow>
    <commands>
      <test>python -m pytest</test>
      <lint>python -m flake8</lint>
      <format>python -m black</format>
    </commands>
  </development_workflow>
</project_configuration>
```

### Add CLAUDE.md (Optional but Recommended)

Create a CLAUDE.md file in your project root:

```markdown
# CLAUDE.md - Framework Control Document

| version | last_updated | status |
|---------|--------------|--------|
| 3.0.0   | 2025-07-15   | active |

This project uses the Claude Code Framework for enhanced development workflows.

## Quick Commands

- `/auto "describe what you want"` - Intelligent task routing
- `/task "specific development task"` - Single component development  
- `/query "research question"` - Code analysis and research

## Configuration

Project settings are in PROJECT_CONFIG.xml. Customize for your needs.
```

## ✅ Verification Checklist

Confirm everything is working:

- [ ] Framework version displays correctly
- [ ] Authentication completed successfully
- [ ] Test project created and commands run
- [ ] First `/auto` command executed successfully
- [ ] First `/task` command completed with tests
- [ ] PROJECT_CONFIG.xml created (auto or manual)
- [ ] Understanding of core concepts

## 🛟 Troubleshooting

### Common Issues

**"Command not found: claude-code"**
- Installation may have failed or PATH not updated
- Try restarting terminal or checking installation instructions

**"Authentication failed"**
- Check internet connection
- Verify Claude Code account and credentials
- Try `claude-code auth logout` then `claude-code auth login`

**"Framework not responding"**
- Ensure you're in a directory with code files
- Check that the directory has git initialized
- Try starting with `/auto "help me get started"`

**"No such file or directory"**
- Ensure you're in the correct project directory
- Check that files exist before referencing them
- Use absolute paths if relative paths don't work

### Getting More Help

If you encounter issues:
1. Use `/help` command for context-specific assistance
2. Review installation documentation  
3. Check framework community forums
4. Try the basic command examples to verify your setup

## 🎯 Next Steps

Now that you have the framework working:

1. **Explore Basic Commands**: Start with [basic-commands/task-command.md](basic-commands/task-command.md)
2. **Learn Workflows**: Master [workflow patterns](../02-intermediate/) for complex problems
3. **Understand Configuration**: Study PROJECT_CONFIG.xml options
4. **Practice Regularly**: Use the framework for real development tasks

## 💡 Quick Tips for Success

- **Start Simple**: Begin with small, single-file projects
- **Read Output Carefully**: The framework provides detailed guidance
- **Follow TDD**: Let the framework write tests first, then implementation
- **Experiment**: Try different commands to see what works best
- **Ask for Help**: Use `/auto "help me with..."` when uncertain

Ready to continue? Head to [basic-commands/](basic-commands/) to master the core framework commands!