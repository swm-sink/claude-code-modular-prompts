---
command: quick-help
description: Streamlined command guide for immediate productivity - zero setup required with v2.0 Progressive Disclosure System
category: core
parameters: 
  - name: COMMAND_NAME
    type: string
    required: false
    description: Specific command name for detailed quick help (optional)
usage_examples:
  - "/quick-help - Get essential commands overview"
  - "/quick-help task - Quick help for task command"
  - "/quick-help /quick-command - Learn about auto-generation layer"
prerequisites: 
  - "Claude Code environment active"
output_format: structured
tags: [quick-start, help, essential-commands, progressive-disclosure, v2-enhanced]
version: "2.0"
author: "lusaka-template-library"
last_updated: "2025-07-31"
allowed-tools:
- Read
- Grep
---

# 🚀 Quick Command Guide v2.0

<context type="project">
Streamlined help system for lusaka template library featuring 88 commands with v2.0 Progressive Disclosure System. Provides immediate productivity with zero setup through 3-layer complexity management: auto-generation, guided customization, and component assembly.
</context>

<instructions>
Provide quick start guidance for essential commands and Progressive Disclosure System navigation. Process $COMMAND_NAME for specific command help, or default to essential commands overview with immediate productivity focus.
</instructions>

## Usage Examples

<examples>
<example>
<input>/quick-help</input>
<expected_output>Essential commands overview with Progressive Disclosure System layers and immediate next steps</expected_output>
</example>
<example>
<input>/quick-help task</input>
<expected_output>Quick help for task command with v2.0 features and usage patterns</expected_output>
</example>
<example>
<input>/quick-help /quick-command</input>
<expected_output>Progressive Disclosure Layer 1 explanation with auto-generation capabilities</expected_output>
</example>
</examples>

## Quick Start Workflow

<workflow type="parallel">
<task priority="high">
**Progressive Disclosure Navigation**: Choose your complexity level
- **New Users**: Layer 1 - `/quick-command` for 30-second auto-generation
- **Intermediate**: Layer 2 - `/build-command` for 5-minute guided customization
- **Advanced**: Layer 3 - `/assemble-command` for professional 30-minute assembly
</task>

<task priority="high">
**Essential Commands**: Core functionality available immediately
- `/help` - Comprehensive guidance system with v2.0 features
- `/task` - Enhanced development task execution with XML workflow
- `/project` - Complete project management with 7 operational modes
- `/query` - Intelligent codebase analysis with pattern recognition
</task>

<task priority="medium">
**Command Discovery**: Navigate the full command library
- Use `/help --all` for complete 88-command overview
- Explore categories: Core (15), Quality (12), Meta (17), Specialized (11)
- Access Progressive Disclosure layers for appropriate complexity level
</task>
</workflow>

## 🎯 Progressive Disclosure System (v2.0)

### **Layer 1: Auto-Generation** (80% of users)
- **`/quick-command`** - 30-second command creation, zero learning curve
- **Perfect for**: Quick tasks, immediate results, newcomers
- **Success rate**: 30-second productivity

### **Layer 2: Guided Customization** (15% of users)  
- **`/build-command`** - 5-minute guided setup with smart options
- **Perfect for**: Specific needs, controlled complexity, targeted solutions
- **Success rate**: 5-minute customized results

### **Layer 3: Component Assembly** (5% of users)
- **`/assemble-command`** - Professional assembly with 91 components
- **Perfect for**: Complex workflows, enterprise needs, maximum control
- **Success rate**: 15-30 minute professional solutions

## 🚀 Essential Commands (Work Immediately)

### **Most Popular:**
- **`/help`** - Comprehensive guidance with v2.0 feature showcase
- **`/task`** - Enhanced task execution with XML workflow structure
- **`/welcome`** - Interactive onboarding with Progressive Disclosure navigation

### **Quick Development:**
- **`/quick-dev`** - Instant development assistance (already v2.0 enhanced)
- **`/query`** - Intelligent codebase analysis with architectural insights
- **`/project`** - Complete project management with 7 operational modes

### **Quality & Testing:**
- **`/quick-test`** - Streamlined testing guidance
- **`/quick-quality`** - Fast quality assessment

## 📊 Command Library Overview (88 Total)

**By Category:**
- **Core (15)**: Essential workflow and development commands
- **Quality (12)**: Testing, validation, and analysis tools
- **Meta (17)**: System management and adaptation commands
- **Specialized (11)**: Advanced orchestration and complex workflows
- **DevOps (5)**: Deployment, CI/CD, and infrastructure
- **Testing (5)**: Comprehensive testing framework commands
- **Database (4)**: Data management and migration tools
- **Development (6)**: Environment setup and API design
- **Others (13)**: Security, monitoring, examples, and utilities

<automation trigger="completion">
- Provide clear next steps based on user experience level
- Suggest appropriate Progressive Disclosure layer for user needs
- Offer related commands and workflow recommendations
- Track usage patterns for system optimization
</automation>