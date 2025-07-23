# Claude Code Modular Prompts Framework

## A Practical Extension Framework for Claude Code

**A modular prompt framework** that extends Claude Code with organized commands, simplified workflows, and practical development tools. This framework provides 146+ commands in simplified markdown format for common development tasks.

## 🚀 **What This Framework Provides**

### **Organized Command Structure**
A collection of 146+ organized commands in simplified markdown format covering common development workflows:

- **Core Commands**: Essential operations like `auto`, `query`, `task`, and `feature`
- **Development Tools**: Debugging, testing, and feature development workflows
- **Security Tools**: Security auditing scripts and API key management
- **Performance Monitoring**: Scripts for performance analysis and optimization
- **Simplified Format**: Commands converted from XML to human-readable markdown with YAML frontmatter

### **Real Capabilities**
- **📁 Modular Organization**: Commands organized by category in `.claude/commands/`
- **🔧 Practical Tools**: Real Python scripts for security auditing and API key management
- **📝 Human-Readable Commands**: Simplified markdown format with YAML frontmatter and $ARGUMENTS placeholders
- **🛡️ Security Features**: Encrypted API key storage and rotation system with actual implementation
- **📊 Performance Monitoring**: Basic monitoring and benchmarking capabilities (~19% test coverage)

## 🎯 **Quick Start**

### **Installation**
```bash
# Clone the repository
git clone https://github.com/user/claude-code-modular-prompts.git
cd claude-code-modular-prompts/tallinn

# Install dependencies (for Python scripts and MCP server)
pip install -r requirements.txt

# Set up MCP server (optional, for integration with Claude Code)
chmod +x setup_mcp.sh
./setup_mcp.sh
```

### **Basic Usage**
The framework provides commands you can use directly in Claude Code:

```bash
# Use the intelligent router to automatically select the best command
/auto "analyze the authentication system"

# Query the codebase for information
/query "how does user authentication work?"

# Create focused improvements
/task "fix password validation bug"

# Build complete features  
/feature "user profile management system"
```

All commands use the simplified markdown format with YAML frontmatter and are located in `.claude/commands/` directory.

### **Key Features**
- **Smart Routing**: The `/auto` command analyzes your request and picks the best tool
- **Organized Commands**: 146+ commands grouped by category (core, development, security, etc.)
- **Security Tools**: Encrypted API key management and security auditing scripts
- **Performance Monitoring**: Built-in performance analysis and optimization scripts

## 📊 **Project Status**

### **Current Implementation**
- **146+ Commands**: Organized command library in `.claude/commands/` covering common development tasks
- **Command Migration**: Successfully converted from XML to markdown format with YAML frontmatter
- **Security Features**: Encrypted API key manager with rotation capabilities
- **Performance Monitoring**: Basic benchmarking and analysis tools (~19% test coverage)
- **MCP Integration**: Model Context Protocol server for Claude Code integration

### **Recent Modernization**
- **Format Simplification**: Commands converted from XML to clean markdown format
- **Human-Readable Structure**: Clean markdown format with YAML frontmatter and $ARGUMENTS placeholders
- **Directory Organization**: Commands organized by category in `.claude/commands/`
- **Component Integration**: Component logic embedded directly in command files
- **Claude Code Ready**: Native integration with Claude Code slash command system

### **Available Tools**
1. **Command Simplifier**: Script to convert complex XML commands to markdown
2. **Security Auditing**: Tools for analyzing code security and compliance
3. **API Key Management**: Encrypted storage and rotation system
4. **Performance Monitoring**: Benchmarking and optimization scripts
5. **MCP Server**: Integration with Claude Code via Model Context Protocol

## 🛡️ **Security & Best Practices**

### **Security Features**
- **Encrypted API Keys**: Secure storage using industry-standard encryption
- **Key Rotation**: Automated rotation system for API key security
- **Security Auditing**: Built-in tools for analyzing code security
- **Input Validation**: Basic validation patterns for command arguments

### **Development Best Practices**
- **Modular Architecture**: Organized command and component structure
- **Clear Documentation**: Human-readable command format with examples
- **Error Handling**: Basic error handling patterns throughout framework
- **Performance Monitoring**: Tools for tracking and optimizing performance

## 🌟 **Framework Structure**

### **Command Categories (`.claude/commands/`)**
- **[Core Commands](.claude/commands/core/)**: Essential operations (`auto`, `query`, `task`, `feature`)
- **[Development Tools](.claude/commands/development/)**: Debugging, testing, and refactoring commands
- **[Security Tools](.claude/commands/security/)**: Security auditing and analysis commands
- **[Performance Tools](.claude/commands/performance/)**: Optimization and monitoring commands

### **AI & Reasoning Commands**
- **[Agentic Commands](.claude/commands/agentic/)**: Advanced reasoning and agent coordination
- **[Agent Commands](.claude/commands/agents/)**: Specialized agent roles and workflows
- **[Analysis Tools](.claude/commands/analysis/)**: Code analysis and quality tools

### **Infrastructure & Utilities**
- **[Session Management](.claude/commands/session/)**: Workspace and context management
- **[Utility Commands](.claude/commands/utilities/)**: Helper tools and monitoring
- **[Git Integration](.claude/commands/git/)**: Version control workflows
- **[Deployment Tools](.claude/commands/deployment/)**: Deployment and CI/CD automation

### **Supporting Infrastructure**
- **[Python Scripts](scripts/)**: Command simplification and security auditing tools
- **[MCP Server](mcp_server.py)**: Model Context Protocol integration for Claude Code
- **[Performance Monitoring](performance/)**: Benchmarking and optimization tools
- **[Original Commands](claude_prompt_factory/commands/)**: Original XML commands preserved for reference

## 📚 **Documentation**

### **Getting Started**
- **[Getting Started Guide](docs/GETTING_STARTED.md)**: Quick setup and basic usage
- **[Complete User Guide](docs/COMPLETE_USER_GUIDE.md)**: Comprehensive documentation
- **[Project Configuration](docs/PROJECT_CONFIG_SCHEMA.md)**: Configuration options and schema

### **Development**
- **[Developer Guide](docs/DEVELOPER_GUIDE.md)**: Framework architecture and development
- **[API Reference](docs/api-reference.md)**: Command and component documentation
- **[Contributing Guide](CONTRIBUTING.md)**: How to contribute to the project

### **Security & Performance**
- **[Security Audit Report](SECURITY_AUDIT_REPORT.md)**: Latest security assessment
- **[Performance Reports](PERFORMANCE_OPTIMIZATION_REPORT.md)**: Performance analysis and optimization
- **[Command Migration](COMMAND_MIGRATION_REPORT.md)**: Details on format modernization

## 🎯 **Usage Examples**

### **Code Analysis & Understanding**
```bash
# Understand how authentication works in your codebase
/query "how does user authentication work in this application?"

# Analyze performance bottlenecks
/auto "analyze the performance bottleneck in our API"

# Review security patterns
/query "what security measures are implemented?"
```

### **Development Workflows**
```bash
# Fix a specific bug with TDD approach
/task "fix password validation bug in login form"

# Build a complete feature
/feature "user profile editing with avatar upload"

# Safely refactor existing code
/protocol "refactor database connection logic"
```

### **Security & Performance**
```bash
# Run security audit
python scripts/security_audit.py

# Manage API keys securely  
python secure_api_key_manager.py encrypt --name "openai" --key "sk-..."

# Monitor performance
python run_performance_benchmarks.py
```

## 🏆 **Project Accomplishments**

### **Framework Modernization**
- **Command Migration**: Successfully converted 146+ commands from XML to simplified markdown format
- **Format Standardization**: All commands now use YAML frontmatter with consistent structure
- **Security Implementation**: Built encrypted API key management system with rotation capabilities
- **Performance Tooling**: Created monitoring and benchmarking infrastructure (~19% test coverage)
- **Documentation Cleanup**: Removed fabricated claims and provided accurate project status

### **Practical Tools Delivered**
- **Security Auditing**: Security analysis scripts with compliance checking
- **Command Simplifier**: Tool to convert XML commands to clean markdown (`scripts/simplify_commands.py`)
- **API Key Manager**: Encrypted key storage and rotation system (`secure_api_key_manager.py`)
- **Performance Monitor**: Basic benchmarking and optimization tools (`performance/`)
- **MCP Integration**: Model Context Protocol server for Claude Code integration (`mcp_server.py`)

## 🚀 **Getting Started**

### **Installation Steps**
```bash
# Clone the repository
git clone https://github.com/user/claude-code-modular-prompts.git
cd claude-code-modular-prompts/tallinn

# Install Python dependencies
pip install -r requirements.txt

# Optional: Set up MCP server for Claude Code integration
chmod +x setup_mcp.sh
./setup_mcp.sh
```

### **First Commands to Try**
1. **Smart Routing**: `/auto "analyze the authentication system"`
2. **Code Investigation**: `/query "how does user login work?"`
3. **Focused Tasks**: `/task "fix validation bug in signup form"`
4. **Feature Development**: `/feature "user profile management"`
5. **Security Audit**: `python scripts/security_audit.py`

## 🌟 **Community & Support**

### **Resources**
- **[Documentation](docs/)**: Guides, API reference, and troubleshooting
- **[Examples](examples/)**: Usage examples and workflow demonstrations
- **[Contributing](CONTRIBUTING.md)**: Guidelines for contributing to the project
- **[Security Reports](SECURITY_AUDIT_REPORT.md)**: Security analysis and recommendations

### **Getting Help**
- **Documentation**: Check the docs folder for comprehensive guides
- **Issues**: Report bugs or request features via GitHub issues
- **Contributing**: See CONTRIBUTING.md for development guidelines

---

## 📊 **Current Project Status**

| Component | Status | Description |
|-----------|--------|-------------|
| **Commands** | 146+ available | Organized command library in `.claude/commands/` |
| **Format Migration** | ✅ Complete | XML to markdown with YAML frontmatter |
| **Security Tools** | ✅ Implemented | API key encryption & auditing scripts |
| **Performance Tools** | ✅ Basic | Monitoring and benchmarking (~19% coverage) |
| **Documentation** | ✅ Updated | Accurate capability descriptions |
| **MCP Integration** | ✅ Available | Claude Code integration ready |

**Current Focus**: Transparency, accuracy, and practical utility for Claude Code users.

---

**A practical framework for extending Claude Code with organized commands and development tools.**  
**Focus on transparency, security, and real utility.**