---
name: /adapt-to-project
description: "Intelligent project adaptation with express or guided modes"
usage: /adapt-to-project [--express|--guided] [--dry-run]
category: meta-commands
tools: Read, Write, Edit, MultiEdit
---

# Adapt Framework to Your Project - Manual Guide

## 🎯 What This Command Actually Does

**I'm a guide, not an automation engine.** I'll help you manually customize this Claude Code framework by:
- 📋 Providing step-by-step checklists
- 📝 Generating copy-paste ready configurations
- 🔍 Listing all files that need manual updates
- ✅ Creating validation checklists to verify your work

## ⚠️ What I Cannot Do
- ❌ Automatically detect your tech stack (you'll tell me)
- ❌ Replace placeholders in files (I'll show you what to replace)
- ❌ Create configuration files (I'll give you the content to paste)
- ❌ Calculate scores programmatically (I'll provide a checklist)

## Choose Your Adaptation Mode

### Express Mode (15-20 minutes of manual work)
I'll guide you through 50 quick questions, then provide:
- Complete list of all replacements needed
- Copy-paste ready configurations
- File-by-file update instructions

### Guided Mode (30-45 minutes of manual work)
We'll go through each customization step with:
- Detailed explanations for each choice
- Examples of common patterns
- Best practices for your domain

Which mode would you prefer?
1. Express checklist mode
2. Detailed guided mode
3. Just show me what needs changing

## What I'll Customize

**Project Information**:
- [INSERT_PROJECT_NAME] → Your actual project name
- [INSERT_DOMAIN] → Your domain (web-dev, data-science, devops, etc.)
- [INSERT_TECH_STACK] → Your technology stack

**Team & Workflow**:
- [INSERT_TEAM_SIZE] → Your team size
- [INSERT_WORKFLOW_TYPE] → Your development workflow
- [INSERT_COMPANY_NAME] → Your organization

**Technical Choices**:
- [INSERT_PRIMARY_LANGUAGE] → Your main programming language
- [INSERT_TESTING_FRAMEWORK] → Your testing tools
- [INSERT_CI_CD_PLATFORM] → Your deployment pipeline

## Manual Tech Stack Identification

Since I cannot automatically scan your files, please tell me about your project:

**Common tech stacks I can help you adapt for:**
- **JavaScript/Node.js**: Look for package.json
- **Python**: Look for requirements.txt, Pipfile, or setup.py
- **Go**: Look for go.mod
- **Rust**: Look for Cargo.toml
- **Java**: Look for pom.xml or build.gradle
- **PHP**: Look for composer.json
- **Ruby**: Look for Gemfile

**Quick check**: What files do you see in your project root? I'll help you identify the right adaptations based on what you tell me.

## Express Mode Questions

If you choose express mode, here are the 50 yes/no questions I'll ask:

**Project Type (10 questions)**:
1. Is this a web development project?
2. Does it involve data science or ML?
3. Is it a DevOps/infrastructure project?
4. Do you build mobile applications?
5. Is it an API-first project?
6. Do you work with microservices?
7. Is this an enterprise application?
8. Do you need real-time features?
9. Is it a CLI tool or library?
10. Do you work with embedded systems?

**Team & Process (10 questions)**:
11. Are you working solo?
12. Is your team smaller than 5 people?
13. Do you follow agile methodology?
14. Do you use GitFlow?
15. Is code review mandatory?
16. Do you pair program regularly?
17. Is documentation a priority?
18. Do you have dedicated QA?
19. Are you in a regulated industry?
20. Do you work with external contractors?

**Technology Preferences (10 questions)**:
21. Do you prefer functional programming?
22. Is TypeScript mandatory?
23. Do you use a monorepo?
24. Are you cloud-native?
25. Do you use containers?
26. Is Kubernetes in your stack?
27. Do you need multi-region deployment?
28. Is offline functionality required?
29. Do you process sensitive data?
30. Is performance critical?

**Tools & Integration (10 questions)**:
31. Do you use VS Code primarily?
32. Is GitHub your version control?
33. Do you need Jira integration?
34. Is Slack your main communication?
35. Do you use feature flags?
36. Is A/B testing important?
37. Do you need analytics integration?
38. Is error tracking automated?
39. Do you use a CDN?
40. Is caching strategy critical?

**Security & Compliance (10 questions)**:
41. Do you handle payment data?
42. Is GDPR compliance required?
43. Do you need SOC2 compliance?
44. Is penetration testing regular?
45. Do you use secret management?
46. Is audit logging required?
47. Do you need data encryption?
48. Is 2FA mandatory?
49. Do you have security review process?
50. Is zero-trust architecture used?

## After the Questions - What You'll Get

Based on your answers, I'll provide:

### 1. Customized Replacement Guide
```markdown
File: .claude/commands/core/task.md
- Line 12: Replace "[INSERT_PROJECT_NAME]" with "YourProjectName"
- Line 28: Replace "[INSERT_TESTING_FRAMEWORK]" with "Jest"

File: .claude/commands/core/query.md
- Line 8: Replace "[INSERT_DOMAIN]" with "web-dev"
[... complete list for all files ...]
```

### 2. Copy-Paste project-config.yaml
```yaml
# Copy this entire block to .claude/config/project-config.yaml
project_config:
  metadata:
    name: "YourProjectName"
    domain: "web-dev"
  placeholders:
    TECH_STACK: "React, Node.js, PostgreSQL"
    # ...
```

### 3. Validation Checklist
```markdown
□ All placeholders replaced in core commands
□ project-config.yaml created and saved
□ Unused commands removed from .claude/commands/
□ Domain-specific commands added
□ Settings reviewed and updated
```

### 4. Manual Next Steps
1. Open each file listed in the replacement guide
2. Use Find & Replace for the placeholders
3. Save the project-config.yaml content
4. Remove commands you don't need
5. Run the validation checklist

## Ready to Begin?

Remember: This is a **manual process** that I'll guide you through. I cannot make the changes for you, but I'll make it as easy as possible with clear instructions.

Choose your mode:
1. **Express**: Answer 50 questions → Get complete replacement list
2. **Guided**: Step-by-step with explanations
3. **Preview**: See example output without answering questions