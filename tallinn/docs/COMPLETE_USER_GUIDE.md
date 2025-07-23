# Complete User Guide - Claude Code Modular Prompts Framework

## Welcome to Organized Development

This framework provides a structured approach to Claude Code development with 146+ organized commands in simplified markdown format, security tools, and performance monitoring. This guide covers the framework's actual capabilities and how to use them effectively for practical development tasks.

## 🚀 **Quick Start Guide**

### **First Steps**
```bash
# Start with the intelligent router
/auto "analyze the authentication system"

# Or query your codebase directly
/query "how does user authentication work?"

# Create focused improvements
/task "fix password validation bug"
```

### **Real Working Tools**
```bash
# Run security audit
python scripts/security_audit.py

# Manage API keys securely
python secure_api_key_manager.py encrypt --name "openai" --key "sk-..."

# Performance monitoring
python run_performance_benchmarks.py

# Start MCP server for Claude Code integration
python start_mcp_server.py
```

### **Basic Workflow Example**
```bash
# 1. Understand your system
/query "analyze the database connection logic"

# 2. Make focused improvements
/task "fix password validation bug"

# 3. Build complete features
/feature "user profile management system"
```

**Result**: Structured approach to development with real security and performance tools.

## 📚 **Core Commands Reference**

### **Intelligent Command Router**
```bash
/auto "your request in natural language"
```

**What it does**: Analyzes your request and routes to the most appropriate command from the 146+ available options.

**Examples**:
- `/auto "users can't log in after the last deployment"` → Routes to bug fix workflow
- `/auto "add dark mode to the application"` → Routes to feature development workflow

### **Codebase Query and Analysis**
```bash
/query "your question about the codebase"
```

**What it does**: Provides intelligent analysis and understanding of your codebase without making changes.

**Examples**:
- `/query "How does user authentication work in this app?"`
- `/query "What security measures are implemented?"`

### **Focused Development Tasks**
```bash
/task "specific task description"
```

**What it does**: Executes focused development tasks with a structured approach.

**Examples**:
- `/task "fix password validation bug in login form"`
- `/task "optimize database queries in user service"`

### **Complete Feature Development**
```bash
/feature "feature description"
```

**What it does**: Builds complete features from conception to implementation.

**Examples**:
- `/feature "user profile editing with avatar upload"`
- `/feature "email notification system"`

## 🗂️ **Command Categories**

### **Core Commands** (`.claude/commands/core/`)
- `/auto` - Intelligent command routing
- `/query` - Codebase analysis and understanding
- `/task` - Focused development tasks
- `/feature` - Complete feature development
- `/protocol` - Safe architectural changes
- `/research` - Research and investigation

### **Development Tools** (`.claude/commands/development/`)
- `/debug` - Debugging and troubleshooting
- `/dev-test` - Development testing workflows
- `/dev-refactor` - Code refactoring tasks
- `/dev-build` - Build and compilation tasks

### **Security Tools** (`.claude/commands/security/`)
- `/secure-audit` - Security auditing
- `/secure-scan` - Security scanning
- `/secure-fix` - Security issue fixing
- `/secure-config` - Security configuration

### **Performance Tools** (`.claude/commands/performance/`)
- `/perf-optimize` - Performance optimization
- `/perf-monitor` - Performance monitoring
- `/perf-benchmark` - Performance benchmarking
- `/perf-profile` - Performance profiling

### **Agent Commands** (`.claude/commands/agents/`)
- `/agent-spawn` - Spawn specialized agents
- `/swarm` - Multi-agent coordination
- `/researcher` - Research agent
- `/security-specialist` - Security specialist agent

### **Testing Tools** (`.claude/commands/testing/`)
- `/test-unit` - Unit testing
- `/test-integration` - Integration testing
- `/test-e2e` - End-to-end testing
- `/test-coverage` - Test coverage analysis

## 🛠️ **Python Scripts and Tools**

### **Security Auditing**
```bash
# Run comprehensive security audit
python scripts/security_audit.py

# Output: Detailed security analysis with recommendations
```

### **API Key Management**
```bash
# Encrypt and store API key
python secure_api_key_manager.py encrypt --name "openai" --key "sk-..."

# Rotate existing keys
python secure_api_key_manager.py rotate --name "openai"

# List stored keys
python secure_api_key_manager.py list
```

### **Performance Monitoring**
```bash
# Run performance benchmarks
python run_performance_benchmarks.py

# Output: Performance metrics and analysis
```

### **MCP Server Integration**
```bash
# Start MCP server for Claude Code integration
python start_mcp_server.py

# Setup MCP configuration
chmod +x setup_mcp.sh
./setup_mcp.sh
```

## 📊 **Command Structure**

All commands use the simplified markdown format with YAML frontmatter:

```markdown
---
name: /command-name
description: Brief description of what the command does
usage: /command-name [arguments]
tools: Read, Write, Edit, Grep, Glob, Bash
---

# Command implementation

**Usage**: `/command-name $ARGUMENTS`

## Key Arguments
- **$ARGUMENT1** (required): Description
- **$ARGUMENT2** (optional): Description

## Examples
```bash
/command-name "example usage"
```

## Core Logic
[Command implementation logic with embedded components]
```

## 🔧 **Configuration and Setup**

### **Directory Structure**
```
tallinn/
├── .claude/
│   └── commands/          # 146+ simplified markdown commands
├── scripts/               # Utility scripts
├── performance/          # Performance monitoring tools
├── security/            # Security tools and reports
├── mcp_server.py        # MCP server for Claude Code
└── docs/               # Documentation
```

### **MCP Integration**
The Model Context Protocol server enables Claude Code to access framework commands:

1. **Setup**: Run `./setup_mcp.sh`
2. **Start**: Run `python start_mcp_server.py`
3. **Use**: Commands become available as slash commands in Claude Code

### **Configuration Files**
- `mcp_config.json` - MCP server configuration
- `settings.local.json` - Local development settings
- `requirements.txt` - Python dependencies

## 🛡️ **Security Features**

### **Encrypted API Key Storage**
- Industry-standard encryption for API keys
- Secure rotation system
- Multiple provider support

### **Security Auditing**
- Automated security analysis
- OWASP compliance checking
- Vulnerability detection

### **Best Practices**
- Input validation patterns
- Secure coding guidelines
- Error handling standards

## 📈 **Performance Monitoring**

### **Current Status**
- **Test Coverage**: ~19% (realistic measurement)
- **Command Count**: 146+ organized commands
- **Format Migration**: 100% complete (XML to markdown)

### **Benchmarking Tools**
- Performance analysis scripts
- Resource usage monitoring
- Optimization recommendations

### **Metrics**
All metrics are based on actual measurements, not fabricated numbers.

## 🎯 **Best Practices**

### **Command Usage**
1. **Start Simple**: Begin with `/auto` for intelligent routing
2. **Be Specific**: Provide clear, detailed requests
3. **Iterate**: Use feedback to refine your approach
4. **Security First**: Run security audits regularly

### **Development Workflow**
1. **Understand**: Use `/query` to understand existing code
2. **Plan**: Use `/task` for focused improvements
3. **Build**: Use `/feature` for complete features
4. **Secure**: Use security tools throughout

### **Performance Optimization**
1. **Measure**: Use benchmarking tools
2. **Analyze**: Identify bottlenecks
3. **Optimize**: Apply targeted improvements
4. **Verify**: Measure improvements

## 🚨 **Troubleshooting**

### **Common Issues**

**Command Not Found**
- Ensure commands are in `.claude/commands/`
- Check YAML frontmatter format
- Verify MCP server is running

**Permission Errors**
- Run `chmod +x setup_mcp.sh`
- Check file permissions
- Verify Python environment

**Performance Issues**
- Check system resources
- Review test coverage (~19% currently)
- Run performance benchmarks

### **Getting Help**
- Check documentation in `/docs/`
- Review security reports
- Run diagnostic scripts

## 📚 **Advanced Usage**

### **Custom Commands**
Create new commands following the established pattern:
```markdown
---
name: /your-command
description: Your command description
usage: /your-command [arguments]
tools: Read, Write, Edit
---

# Your command implementation
```

### **Agent Coordination**
Use specialized agents for complex tasks:
```bash
/swarm "coordinate multiple agents for complex project"
/security-specialist "focus on security aspects"
/researcher "investigate and analyze"
```

### **Integration Patterns**
Combine commands for complex workflows:
```bash
# Research → Plan → Implement → Test → Secure
/query "understand current architecture"
/task "implement specific improvement"
/test-coverage "verify implementation"
/secure-audit "ensure security compliance"
```

## 🎓 **Learning Resources**

### **Documentation**
- [Getting Started Guide](GETTING_STARTED.md)
- [API Reference](api-reference.md)
- [Contributing Guide](../CONTRIBUTING.md)

### **Examples**
- Browse `.claude/commands/` for command examples
- Check `examples/` directory for workflows
- Review security reports for best practices

### **Community**
- Contribute improvements
- Report issues
- Share usage patterns

## 📊 **Project Status**

### **Current Implementation**
| Component | Status | Coverage |
|-----------|--------|----------|
| Commands | 146+ available | 100% converted |
| Format | Simplified markdown | Complete |
| Security | Tools implemented | Active |
| Performance | Basic monitoring | ~19% tested |
| MCP Integration | Available | Ready |

### **Future Development**
- Improved test coverage
- Enhanced security features
- Performance optimizations
- Community contributions

---

**A practical framework for extending Claude Code with organized commands and development tools.**

*Focus on transparency, security, and real utility for developers.*