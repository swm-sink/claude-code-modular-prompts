---
command: help
description: Comprehensive guide to 88 available commands and v2.0 enhanced features for lusaka template library
category: core
parameters: 
  - name: COMMAND_NAME
    type: string
    required: false
    description: Specific command name to get detailed help for (optional)
  - name: HELP_TYPE
    type: string
    required: false
    description: Type of help requested (--all, --best-practices, --v2-features)
usage_examples:
  - "/help - Get general help and command overview"
  - "/help task - Get detailed help for the task command"
  - "/help --all - Comprehensive list of all 88 commands"
  - "/help --v2-features - Learn about v2.0 enhancements"
prerequisites: 
  - "Claude Code environment configured"
  - "Template library installed"
output_format: structured
tags: [help, documentation, guidance, commands, v2-enhanced]
version: "2.0"
author: "lusaka-template-library"
last_updated: "2025-07-31"
allowed-tools:
- Read
- Grep
---

# /help - Comprehensive Command Guide v2.0

<context type="project">
Lusaka template library with 88 Claude Code commands featuring v2.0 enhancements: enhanced metadata, XML semantic structure, parameter validation, Progressive Disclosure System, and team collaboration features.
</context>

<instructions>
Provide comprehensive help and guidance for the template library. Process $COMMAND_NAME for specific command help, or use $HELP_TYPE for specialized help categories. Default to general overview with quick start guidance.
</instructions>

## Usage Examples

<examples>
<example>
<input>/help</input>
<expected_output>General overview with quick start guide and most popular commands</expected_output>
</example>
<example>
<input>/help task</input>
<expected_output>Detailed help for the task command including v2.0 features and usage examples</expected_output>
</example>
<example>
<input>/help --v2-features</input>
<expected_output>Comprehensive guide to v2.0 enhancements: metadata, XML structure, team features</expected_output>
</example>
</examples>

## Help System Workflow

<workflow type="sequential">
<task priority="high">
**Request Analysis**: Determine help type and scope
- Parse $COMMAND_NAME for specific command help
- Process $HELP_TYPE for specialized categories
- Default to general overview if no parameters provided
</task>

<task priority="high">
**Content Delivery**: Provide targeted help information
- Command-specific help with v2.0 features explanation
- Category overviews with command listings
- Best practices and usage patterns
</task>

<task priority="medium">
**Guidance Enhancement**: Offer next steps and learning paths
- Suggest related commands and workflows
- Provide Progressive Disclosure System navigation
- Link to advanced features and team collaboration
</task>
</workflow>

## 🚀 Quick Start Guide

### **Most Popular Commands:**
- **`/help`** - This command - comprehensive guidance system
- **`/task`** - Enhanced development task execution with v2.0 features
- **`/quick-command`** - 30-second auto-generation (Layer 1 Progressive Disclosure)
- **`/welcome`** - Interactive onboarding and project setup

### **Progressive Disclosure System (v2.0):**
1. **Layer 1**: `/quick-command` - Instant generation, zero learning curve
2. **Layer 2**: `/build-command` - Guided customization with smart options  
3. **Layer 3**: `/assemble-command` - Professional assembly with 94 components

### **Command Categories (88 Total):**
- **Core (15)**: Essential commands for daily development
- **Quality (12)**: Testing, validation, and analysis tools
- **Meta (17)**: Adaptation, memory management, and system commands
- **Specialized (11)**: Advanced orchestration and complex workflows
- **DevOps (5)**: Deployment, CI/CD, and infrastructure
- **Testing (5)**: Unit, integration, e2e testing frameworks
- **Database (4)**: Migration, backup, and data management
- **Development (6)**: Environment setup and API design
- **Others (13)**: Security, monitoring, examples, and utilities

## 🆕 v2.0 Enhanced Features

### **Enhanced Metadata System:**
- Parameter validation with type checking
- Usage examples with expected outputs
- Prerequisites and dependency tracking
- Version control and team attribution

### **XML Semantic Structure:**
- `<context>` - Project-specific information
- `<instructions>` - Procedural guidance with parameters
- `<examples>` - Structured input/output demonstrations
- `<workflow>` - Implementation phases and task organization

### **Team Collaboration:**
- Hierarchical memory management (Project/Personal/Global)
- MCP integration for external tools
- Advanced command discovery and knowledge sharing

<automation trigger="completion">
- Log help request for usage analytics
- Suggest related commands based on request pattern
- Update user journey tracking for Progressive Disclosure navigation
</automation>
