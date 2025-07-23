# Getting Started with Claude Code Modular Prompts Framework

Welcome to the Claude Code modular prompts framework! This guide will help you set up and start using the framework's organized command library and development tools.

## 🎯 What You'll Learn

By the end of this guide, you'll be able to:
- ✅ Set up the framework in your project
- ✅ Use organized commands in simplified markdown format
- ✅ Leverage the 146+ commands for common development tasks
- ✅ Utilize security and performance monitoring tools

## 🚀 Quick Setup

### Prerequisites
- [Claude Code desktop application](https://claude.ai/code) 
- Python 3.8+ (for optional tools and MCP server)
- A project directory (existing or new)
- Basic command line familiarity

### Step 1: Get the Framework
```bash
# Clone the repository
git clone https://github.com/user/claude-code-modular-prompts.git
cd claude-code-modular-prompts/tallinn

# Install Python dependencies (for scripts and MCP server)
pip install -r requirements.txt
```

### Step 2: Understand the Structure
The framework provides:
- **146+ Commands**: Organized in `.claude/commands/` (simplified markdown format)
- **Security Tools**: Python scripts for auditing and API key management
- **Performance Tools**: Monitoring and benchmarking utilities (~19% test coverage)
- **MCP Server**: Claude Code integration via Model Context Protocol

### Step 3: Try Basic Commands
Start with these core commands (now in simplified markdown format):

**Intelligent routing:**
```bash
/auto "analyze the authentication system"
```

**Direct code analysis:**
```bash
/query "how does user authentication work?"
```

**Focused development tasks:**
```bash
/task "fix password validation bug"
```

All commands are now in simplified markdown format with YAML frontmatter, located in `.claude/commands/`.

## ⚡ Available Tools & Commands

### Python Scripts (Ready to Use)
```bash
# Run security audit
python scripts/security_audit.py

# Manage API keys securely
python secure_api_key_manager.py encrypt --name "openai" --key "sk-..."

# Performance benchmarking
python run_performance_benchmarks.py

# MCP server for Claude Code integration
python start_mcp_server.py
```

### Framework Commands (Simplified Markdown Format)
The framework provides 146+ organized commands in simplified markdown format:

**Core Commands** (`.claude/commands/core/`):
- `/auto` - Intelligent command routing
- `/query` - Code analysis and understanding 
- `/task` - Focused development tasks
- `/feature` - Complete feature development

**Other Categories** (`.claude/commands/`):
- `agentic/` - AI reasoning and coordination
- `development/` - Feature development workflows
- `security/` - Security analysis tools
- `performance/` - Performance optimization
- `agents/` - Specialized agent roles
- `utilities/` - Helper tools and monitoring

### Getting Real Value
1. **Use Python Scripts**: These provide immediate, practical value
2. **Try Core Commands**: All commands now use simplified format
3. **Explore Structure**: Browse `.claude/commands/` to see command organization
4. **Security First**: Use the API key manager and security auditing tools

## 🏗️ Real-World Example

### Scenario: Security Audit & API Key Management
Let's use the framework's real capabilities:

```bash
# Step 1: Run a security audit
python scripts/security_audit.py

# Step 2: Set up secure API key storage
python secure_api_key_manager.py encrypt --name "openai" --key "your-api-key"

# Step 3: Try framework command routing
/auto "analyze the authentication system in this codebase"

# Step 4: Run performance benchmarks
python run_performance_benchmarks.py
```

**What you get:** 
- Real security analysis with specific recommendations
- Encrypted API key storage with rotation capabilities
- Structured command routing (though many commands still need modernization)
- Basic performance monitoring and insights

## 📊 Framework Structure

The framework organizes 146+ commands into logical categories in `.claude/commands/`:

### 🧠 **AI & Reasoning** (Simplified markdown format)
- **`agentic/`**: Advanced reasoning patterns (ReAct, Tree of Thoughts)
- **`agents/`**: Specialized agent roles and coordination

### 🛠️ **Development Tools** (Simplified markdown format)
- **`core/`**: Essential commands like `/auto`, `/query`, `/task`
- **`development/`**: Feature development and debugging workflows
- **`testing/`**: Quality assurance and testing tools

### 🔍 **Analysis & Security** (Simplified markdown format + Python scripts)
- **`analysis/`**: Code analysis commands
- **`security/`**: Security auditing commands (plus Python scripts in `/scripts/`)
- **`performance/`**: Performance monitoring and optimization

### 🤝 **Utilities & Infrastructure**
- **`utilities/`**: Helper commands and monitoring tools
- **`session/`**: Session and context management
- **`git/`**: Version control integration
- **`deployment/`**: Deployment and CI/CD tools

**Current Status**: All 146+ commands converted to simplified markdown format with YAML frontmatter.

## ⚙️ Configuration & Setup

### Optional MCP Server Setup
For deeper Claude Code integration:

```bash
# Set up MCP server (optional)
chmod +x setup_mcp.sh
./setup_mcp.sh

# Start MCP server manually
python start_mcp_server.py
```

The MCP server enables Claude Code to access the framework commands directly through the Model Context Protocol.

### Project Configuration
The framework includes configuration files for MCP integration and command processing. All commands are ready to use with Claude Code.

## 🎯 Recommended Approach

### Getting Started
1. **Start with Python scripts** - these provide immediate value
2. **Try core commands** - `/auto`, `/query`, `/task` are most useful
3. **Explore the structure** - browse `.claude/commands/` to understand organization
4. **Use security tools** - practical and ready to use

### For Development Teams
1. **Security First**: Use the auditing and API key management tools
2. **Gradual Adoption**: Start with a few core commands
3. **Structured Development**: Use the organized command categories
4. **Monitor**: Use performance benchmarking tools (~19% test coverage currently)

## 🚀 Next Steps

### Immediate Actions
- [ ] **Run the security audit**: `python scripts/security_audit.py`
- [ ] **Set up API key management**: `python secure_api_key_manager.py`
- [ ] **Try basic commands**: `/auto`, `/query`, `/task` in Claude Code
- [ ] **Explore the structure**: Browse `.claude/commands/` directory

### Available Resources
- **[Complete User Guide](COMPLETE_USER_GUIDE.md)**: Comprehensive documentation
- **[API Reference](api-reference.md)**: Command documentation
- **[Security Reports](../SECURITY_AUDIT_REPORT.md)**: Latest security analysis
- **[Performance Reports](../PERFORMANCE_OPTIMIZATION_REPORT.md)**: Performance insights

### Getting Support
- **[Contributing Guide](../CONTRIBUTING.md)**: Help improve the framework
- **Documentation**: Check docs folder for guides and troubleshooting
- **Security**: Review security reports for best practices

## 💡 Practical Tips

**🔧 Start with Scripts**: The Python scripts provide immediate, practical value for security and performance monitoring.

**🛡️ Security First**: Use the API key manager and security auditing tools for real security benefits.

**📊 Monitor Performance**: Run benchmarks to understand your current performance baseline (~19% test coverage).

---

## 🎯 Framework Goals

This framework aims to provide:
- **Organized Structure**: Clear categorization of 146+ development commands
- **Security Tools**: Practical security auditing and key management
- **Performance Monitoring**: Basic benchmarking and optimization tools
- **Claude Code Integration**: Native slash command support with MCP server

**Current Status**: All 146+ commands converted to simplified markdown format with YAML frontmatter, ready for Claude Code integration.

---

*A practical framework focused on transparency, security, and real utility for Claude Code users.* 