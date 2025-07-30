---
name: /adapt-to-project
description: "Interactive automated project customization with real-time detection"
usage: /adapt-to-project
category: meta-commands
tools: Bash, Read, Write, Edit, MultiEdit, Glob, LS
---

# 🚀 Interactive Automated Project Customization

**I'll automatically detect your project and customize all templates. No manual work required!**

## How This Actually Works

1. **🔍 Auto-detect** your project type by scanning files
2. **💬 Ask** interactive questions for missing details  
3. **🔄 Replace** all placeholders automatically
4. **✅ Validate** that everything works

**Timeline: 2-5 minutes total**

---

## 🔍 Phase 1: Project Detection  

I'll scan your current working directory to detect your project automatically.

Let me check what project files exist in your current directory:

### Scanning for Project Indicators...

I'm looking for these key files to determine your tech stack:
- `package.json` (JavaScript/TypeScript/React/Node.js)
- `requirements.txt`, `setup.py`, `pyproject.toml` (Python)
- `pom.xml`, `build.gradle` (Java/Kotlin)
- `go.mod` (Go)
- `Cargo.toml` (Rust)
- `composer.json` (PHP)
- `Gemfile` (Ruby)
- `.csproj` files (C#/.NET)

Let me start by scanning your directory structure and analyzing the project files I find.

Based on what I discover, I'll automatically determine:
- **Project Name**: From package files or directory name
- **Primary Language**: JavaScript, Python, Java, etc.
- **Framework/Stack**: React, Django, Spring Boot, etc.
- **Domain**: web-dev, data-science, backend, etc.
- **Testing Framework**: Jest, pytest, JUnit, etc.

---

## 💬 Phase 2: Interactive Questions

For any details I can't auto-detect, I'll ask quick questions:

**Example interaction:**
```
🤖 I detected a React + Node.js project called "MyApp"
🤖 Is this a web application? (y/n)
👤 y
🤖 What's your team size? (solo/small/medium/large)  
👤 small
🤖 Perfect! Customizing templates for small team web development...
```

---

## 🔄 Phase 3: Automatic Replacement

I'll automatically update **all** templates with your project details:

### Files I'll Update:
- `.claude/commands/**/*.md` - All command templates
- `.claude/components/**/*.md` - Component templates  
- `.claude/context/*.md` - Context files
- `CLAUDE.md` - Project memory

### Replacements Made:
- `[INSERT_PROJECT_NAME]` → Your actual project name
- `[INSERT_DOMAIN]` → web-dev, data-science, etc.
- `[INSERT_TECH_STACK]` → Your specific technologies
- `[INSERT_PRIMARY_LANGUAGE]` → JavaScript, Python, etc.
- `[INSERT_TESTING_FRAMEWORK]` → Jest, pytest, etc.
- `[INSERT_CI_CD_PLATFORM]` → GitHub Actions (default)

---

## ✅ Phase 4: Validation & Report

I'll verify all customizations worked and provide a summary:

**What you'll get:**
- 📊 Summary of all replacements made
- 📋 List of customized commands ready to use
- 🎯 5 recommended commands to try first
- ⚠️ Any issues that need attention

---

## 🚀 Ready to Start?

Just say **"yes"** or **"start"** and I'll begin the automated customization process!

The entire process takes 2-5 minutes and requires no manual editing from you.

**Example session:**
```
👤 /adapt-to-project
🤖 Starting automated project detection...
🤖 Found package.json - React + TypeScript project detected!
🤖 Project name: "awesome-todo-app" 
🤖 Is this a web application? (y/n)
👤 y
🤖 Customizing 64 templates for web development...
🤖 ✅ All templates customized! Try /help to see your commands.
```

Ready to customize your Claude Code templates automatically?