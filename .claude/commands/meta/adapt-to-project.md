---
name: /adapt-to-project
description: "Automated project adaptation - detects tech stack and replaces placeholders"
usage: /adapt-to-project
category: meta-commands
tools: Read, Write, Edit, MultiEdit, Glob
---

# Automated Project Adaptation

I'll automatically detect your project type and replace all placeholders in your Claude Code templates.

## Step 1: Detecting Project Type

Let me scan for project files to determine your tech stack:

**Checking for project files...**

I'll now scan your project directory to detect the technology stack and automatically adapt all templates.

First, let me check what project files exist to determine your tech stack:

**Scanning project directory...**

Looking for:
- `package.json` (React/Node.js projects)
- `requirements.txt`, `setup.py`, `pyproject.toml` (Python projects)  
- `pom.xml`, `build.gradle` (Java projects)
- `go.mod` (Go projects)
- `Cargo.toml` (Rust projects)

Based on what I find, I'll automatically:
1. **Extract project name** from configuration files or directory name
2. **Determine domain** (web-dev, data-science, backend, etc.)
3. **Identify tech stack** and primary language
4. **Set testing framework** based on dependencies
5. **Replace all placeholders** in your templates with detected values

## Executing Auto-Detection and Replacement

Let me start the automatic detection and replacement process:

I'll create a `project-config.yaml` with the detected values for future reference.

Let me start the automatic detection process now...

---

## 🔍 STEP 1: PROJECT DETECTION

First, let me scan the current directory to identify your project type:

### Scanning for Project Files...

I'll look for these key indicator files in your project:
- `package.json` (JavaScript/Node.js/React)
- `requirements.txt`, `setup.py`, `pyproject.toml` (Python)  
- `pom.xml`, `build.gradle` (Java)
- `go.mod` (Go)
- `Cargo.toml` (Rust)
- `composer.json` (PHP)

Let me check what files exist in your current directory to determine the project type.

### 📋 Project Detection Results

Based on the files I find, I'll determine:
1. **Primary Language**: JavaScript, Python, Java, etc.
2. **Framework**: React, Django, Spring Boot, etc.
3. **Domain**: web-dev, data-science, backend, etc.
4. **Testing Framework**: Jest, pytest, JUnit, etc.
5. **Project Name**: From config files or directory name

---

## 🔄 STEP 2: AUTOMATIC PLACEHOLDER REPLACEMENT

Once I identify your project type, I'll automatically update all Claude Code templates with the appropriate values:

### Core Replacements Made:
- `[INSERT_PROJECT_NAME]` → (detected project name)
- `[INSERT_DOMAIN]` → (web-dev/data-science/backend)  
- `[INSERT_TECH_STACK]` → (specific technologies detected)
- `[INSERT_PRIMARY_LANGUAGE]` → (JavaScript/Python/Java)
- `[INSERT_TESTING_FRAMEWORK]` → (Jest/pytest/JUnit)
- `[INSERT_CI_CD_PLATFORM]` → GitHub Actions

### Files Being Updated:
All command templates in `.claude/commands/` that contain placeholders will be automatically updated with your project-specific values.

---

## 📝 STEP 3: CONFIGURATION GENERATION

I'll create a `project-config.yaml` file with all detected values for future reference and manual adjustments if needed.

---

## ✅ STEP 4: VALIDATION & REPORT

Finally, I'll provide a summary of all changes made and verify the adaptation was successful.

**Ready to begin automatic adaptation? The system will:**
1. Scan your project directory
2. Detect tech stack automatically  
3. Replace all placeholders in templates
4. Generate configuration file
5. Provide completion report

No manual work required - everything will be done automatically!

---

## 🚀 EXECUTING AUTOMATIC ADAPTATION

Let me now perform the automatic detection and replacement:

### Phase 1: Project Detection
Running project detection scan...

I'll use the detection script to automatically identify your project type. Let me scan your current directory for project files like package.json, requirements.txt, pom.xml, etc.

### Phase 2: Automatic Placeholder Replacement
Once I detect your project type, I'll automatically replace all placeholders in the Claude Code templates with project-specific values.

### Phase 3: Configuration Generation  
I'll create a project-config.yaml file with all the detected values for future reference.

### Phase 4: Completion Report
Finally, I'll provide a summary of all the changes made and validate the adaptation was successful.

Let me execute each phase now...