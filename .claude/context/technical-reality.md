# Claude Code Technical Reality
# Single Source of Truth for Claude Code capabilities and constraints
# Last Updated: 2025-01-09

## 🎯 What Claude Code Actually Is
- **CLI Tool**: Terminal-based assistant with built-in tools
- **System Prompt**: ~17,000 words defining behavior
- **Stateless**: No memory between sessions, full reload each time
- **Token Window**: 200k tokens (~150k words) maximum

## ✅ Claude Code Native Tools (USE THESE)
- **Read**: Read files from filesystem
- **Write**: Write complete files
- **Edit**: Make string replacements
- **MultiEdit**: Multiple edits in one operation
- **Bash**: Execute shell commands
- **Glob**: Find files by pattern
- **Grep**: Search file contents
- **LS**: List directory contents (fails on hidden dirs)
- **TodoWrite/TodoRead**: Task management
- **WebSearch**: Search internet for current information
- **WebFetch**: Retrieve and analyze web content

## ❌ What Claude Code CANNOT Do
- Save state between conversations
- Access memory from previous sessions
- Dynamically load new capabilities
- Execute Python/JavaScript directly (must use Bash)
- See hidden directories reliably with LS tool

## 📝 Correct YAML Frontmatter Format
```yaml
---
name: command-name
description: Brief description  
usage: "command [args]"
allowed-tools: [Read, Write, Edit, Bash]  # NOT 'tools'
category: core
---
```

## 🔒 Security Model
- Read-only by default
- Requires approval for modifications
- Bash commands verified before execution
- No access to sensitive system areas

## 💡 Session Management Reality
- Each session starts fresh
- CLAUDE.md loads as primary context
- Commands load their own context
- No persistence without explicit file writes

## ⚠️ Common Misconceptions
- **WRONG**: Claude Code can remember previous conversations
- **RIGHT**: Each session is completely new

- **WRONG**: YAML files execute logic
- **RIGHT**: YAMLs are just data, commands must read and implement

- **WRONG**: Backend orchestrates automatically
- **RIGHT**: Commands must explicitly wire to backend

- **WRONG**: LS tool works on hidden directories
- **RIGHT**: Use Bash `ls -la` for hidden directories

## 🎯 Best Practices
1. Use native tools, don't shell out unnecessarily
2. Write state to files for persistence
3. Load context efficiently (token management)
4. Validate with WebSearch for current information
5. Use CLAUDE.md for project memory

## 📊 Performance Constraints
- **Context Window**: Manage carefully, use /compact at 50%
- **Response Time**: Keep operations under 30 seconds
- **File Size**: Large files may truncate
- **Search Depth**: Grep/Glob have practical limits

---
*This file is the ONLY source for Claude Code technical capabilities. 
Reference, don't duplicate.*