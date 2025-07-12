| version | last_updated | status |
|---------|--------------|--------|
| 3.0.0   | 2025-07-11   | stable |


# Command Selection Guide - Stop the Confusion!

> **TL;DR**: `/docs` = CREATE documentation | `/query` = RESEARCH without changes


# 🎯 The Key Difference

```xml
<critical_distinction>
  <docs_command>
    <purpose>Documentation creation, generation, and management</purpose>
    <actions>CREATE • GENERATE • VALIDATE • UPDATE documentation files</actions>
    <result>New or modified documentation files in /docs directory</result>
  </docs_command>
  
  <query_command>
    <purpose>Research, analysis, and information gathering</purpose>
    <actions>SEARCH • ANALYZE • INVESTIGATE • REPORT findings</actions>
    <result>Analysis report with NO file modifications</result>
  </query_command>
</critical_distinction>
```


# 🚨 When Users Get Confused


# ❌ Common Confusion Scenarios

**Scenario 1**: "I want to understand how authentication works"
- **Wrong**: `/docs "explain authentication"` 
- **Right**: `/query "how does authentication work?"`
- **Why**: You want research, not document creation

**Scenario 2**: "Create a setup guide for new developers"  
- **Wrong**: `/query "create setup guide"`
- **Right**: `/docs generate "Setup Guide"`
- **Why**: You want to CREATE documentation

**Scenario 3**: "Find existing documentation about testing"
- **Either works**:
  - `/docs search "testing"` (if you might update docs)
  - `/query "testing documentation"` (if just researching)


# 📊 Quick Decision Matrix

| I want to... | Use | Because |
|---------------|-----|---------|
| **Understand existing code** | `/query` | Research only, no new files |
| **Create new documentation** | `/docs` | Creates actual doc files |
| **Find security issues** | `/query` | Investigation without changes |
| **Write API documentation** | `/docs` | Creates structured docs |
| **Learn how X works** | `/query` | Analysis and explanation |
| **Update existing docs** | `/docs` | Documentation modification |
| **Research best practices** | `/query` | Information gathering |
| **Generate changelog** | `/docs` | Creates documentation file |


# 🎯 Command Selection Flowchart

```
Start: "I need information about..."
             │
             ▼
    ┌┐
    │   Do you want to        │
    │   CREATE/UPDATE         │
    │   documentation?        │
    └┬┘
              │
        ┌▼┐  
        │    YES    │ 
        └┬┘  
              │
              ▼
        ┌┐
        │   /docs     │ ← Creates files
        └┘
              
        ┌▼┐  
        │     NO    │ 
        └┬┘  
              │
              ▼
        ┌┐
        │   /query    │ ← Research only
        └┘
```


# 🔍 Detailed Use Cases


# `/docs` - Documentation Operations

```xml
<docs_use_cases>
  <case name = "Create New Docs">
    <example>/docs generate "API Reference"</example>
    <result>Creates structured API documentation file</result>
  </case>
  
  <case name = "Update Existing Docs">
    <example>/docs "update getting started guide"</example>
    <result>Modifies existing documentation</result>
  </case>
  
  <case name = "Validate Documentation">
    <example>/docs validate</example>
    <result>Checks all docs for consistency and completeness</result>
  </case>
  
  <case name = "Search for Doc Updates">
    <example>/docs search "authentication"</example>
    <result>Finds docs that may need updates</result>
  </case>
</docs_use_cases>
```


# `/query` - Research Operations

```xml
<query_use_cases>
  <case name = "Code Investigation">
    <example>/query "how does user authentication work?"</example>
    <result>Analysis of auth implementation with code examples</result>
  </case>
  
  <case name = "Pattern Discovery">
    <example>/query "find all repository pattern uses"</example>
    <result>Report of pattern usage across codebase</result>
  </case>
  
  <case name = "Security Analysis">
    <example>/query "identify potential security issues"</example>
    <result>Security assessment without modifying code</result>
  </case>
  
  <case name = "Architecture Understanding">
    <example>/query "explain the data flow"</example>
    <result>Comprehensive analysis of system architecture</result>
  </case>
</query_use_cases>
```


# ⚡ Quick Reference


# Need Documentation? → `/docs`
- Creating guides, references, or specs
- Updating existing documentation
- Generating structured content
- **Result**: New/modified files in `/docs`


# Need Understanding? → `/query`  
- Learning how code works
- Finding implementation details
- Investigating issues or patterns
- **Result**: Analysis report, no file changes


# Still Unsure? → `/auto`
- Let the framework decide for you
- Analyzes your request and routes correctly
- **Example**: `/auto "I need to understand the auth system"`


# 🛡️ Error Prevention


# Watch Out For These Mistakes

1. **Using `/docs` for research**
   - Creates unnecessary documentation files
   - Clutters the `/docs` directory
   - Use `/query` instead

2. **Using `/query` for documentation tasks**
   - Won't create the files you need
   - Generates reports instead of docs
   - Use `/docs` instead

3. **Mixing purposes**
   - "Create docs about how auth works" → Use `/docs`
   - "How does auth work?" → Use `/query`


# 📈 Success Indicators


# You're Using `/docs` Correctly When:
- ✅ New documentation files appear in `/docs`
- ✅ Existing docs get updated with new information
- ✅ Documentation follows framework standards
- ✅ Documentation index gets updated automatically


# You're Using `/query` Correctly When:
- ✅ You get detailed analysis without file creation
- ✅ Code examples are included in responses
- ✅ No new files are created
- ✅ You understand the codebase better


# 🎓 Pro Tips

1. **When in doubt**: Start with `/query` to understand, then use `/docs` if you need to document
2. **Research first**: Use `/query` to gather information, then `/docs` to create comprehensive documentation
3. **Use `/auto`**: When you're really unsure, let the intelligent routing decide
4. **Documentation workflow**: `/query` → analyze → `/docs` → create
5. **Read-only rule**: If you don't want ANY files modified, always use `/query`

**Remember**: Commands have single, clear purposes. Following this guide eliminates confusion and ensures you get exactly what you need!