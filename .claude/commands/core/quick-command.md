---
command: quick-command
description: Layer 1 Progressive Disclosure - Auto-generate complete commands from simple descriptions with 30-second success guarantee
category: core
parameters: 
  - name: TYPE
    type: string
    required: true
    description: Command type (search, analyze, transform, validate, report)
  - name: DESCRIPTION
    type: string
    required: true
    description: Clear description of what you want to accomplish
usage_examples:
  - "/quick-command search 'find TODO comments in JavaScript'"
  - "/quick-command analyze 'check Python code quality'"
  - "/quick-command transform 'convert JSON files to YAML'"
  - "/quick-command validate 'check all API responses'"
prerequisites: 
  - "Clear understanding of desired command functionality"
  - "Basic description of target files or operations"
output_format: structured
tags: [auto-generation, progressive-disclosure, layer-1, zero-setup, v2-enhanced]
version: "2.0"
author: "lusaka-template-library"
last_updated: "2025-07-31"
allowed-tools:
- Write
- Read
- Grep
- Glob
- Edit
---

# 🚀 Layer 1: Auto-Generation v2.0 

<context type="project">
Progressive Disclosure System Layer 1 for lusaka template library providing 30-second command auto-generation with zero learning curve. Supports 5 command types (search, analyze, transform, validate, report) with intelligent template selection and automatic component assembly.
</context>

<instructions>
Auto-generate complete, working commands from $TYPE and $DESCRIPTION using intelligent template selection, automatic component assembly, and quality assurance. Deliver ready-to-use commands with proper YAML frontmatter, error handling, and usage examples within 30 seconds.
</instructions>

## Usage Examples

<examples>
<example>
<input>/quick-command search "find TODO comments in JavaScript"</input>
<expected_output>Complete /find-js-todos command with Grep pattern matching, file filtering, and result formatting</expected_output>
</example>
<example>
<input>/quick-command analyze "check Python code quality"</input>
<expected_output>Complete /analyze-python-quality command with code examination, quality metrics, and report generation</expected_output>
</example>
<example>
<input>/quick-command transform "convert JSON files to YAML"</input>
<expected_output>Complete /convert-json-yaml command with file discovery, format conversion, and backup creation</expected_output>
</example>
<example>
<input>/quick-command validate "check all API responses"</input>
<expected_output>Complete /validate-api-responses command with input checking, validation logic, and error reporting</expected_output>
</example>
</examples>

## Auto-Generation Workflow

<workflow type="sequential">
<task priority="high">
**Intent Analysis & Type Detection**: Parse command requirements
- Analyze $DESCRIPTION to understand desired functionality
- Validate $TYPE against supported categories (search, analyze, transform, validate, report)
- Identify key patterns, file types, and operations
- Determine optimal implementation approach automatically
</task>

<task priority="high">
**Template Selection & Component Assembly**: Intelligent automation
- **Search commands**: Pattern matching with file filtering using Grep/Glob
- **Analyze commands**: Code examination with quality metrics using Read/Grep
- **Transform commands**: Data conversion with validation using Read/Write/Edit
- **Validate commands**: Input checking with error reporting using validation patterns
- **Report commands**: Data aggregation with formatting using analysis and output tools
</task>

<task priority="high">
**Auto-Component Integration**: Quality assurance inclusion
- Input validation (required for all command types)
- Core processing logic (type-specific implementation)
- Error handling (comprehensive scenarios coverage)
- Output formatting (consistent, actionable results)
- Progress tracking (for operations requiring time)
</task>

<task priority="medium">
**Command Generation & Validation**: Production-ready output
- Generate complete YAML frontmatter with v2.0 metadata
- Implement functional command logic with best practices
- Include comprehensive error handling and edge cases
- Add usage examples and documentation
- Validate generated command for immediate usability
</task>
</workflow>

## 🧠 Intelligent Auto-Generation System

### **Command Type Intelligence Matrix:**

#### **Search Commands** (`search`)
- **Detection Pattern**: Pattern search + file filtering requirements
- **Generated Components**: Grep patterns, file globbing, result formatting
- **Automatic Inclusions**: Input validation, search logic, output structuring
- **Example Output**: `/find-js-todos` command ready for immediate execution

#### **Analysis Commands** (`analyze`)
- **Detection Pattern**: Code analysis + language-specific examination
- **Generated Components**: File discovery, analysis patterns, report generation
- **Automatic Inclusions**: Quality metrics, pattern recognition, recommendation engine
- **Example Output**: `/analyze-python-quality` command with comprehensive reporting

#### **Transform Commands** (`transform`)
- **Detection Pattern**: Format conversion + batch processing requirements
- **Generated Components**: File discovery, transformation logic, backup systems
- **Automatic Inclusions**: Data validation, conversion algorithms, safety mechanisms
- **Example Output**: `/convert-json-yaml` command with backup and validation

#### **Validation Commands** (`validate`)
- **Detection Pattern**: Input checking + integrity verification needs
- **Generated Components**: Validation rules, error detection, reporting systems
- **Automatic Inclusions**: Rule engines, compliance checking, detailed error output
- **Example Output**: `/validate-api-responses` command with comprehensive validation

#### **Report Commands** (`report`)
- **Detection Pattern**: Data aggregation + summary generation requirements
- **Generated Components**: Data collection, analysis engines, formatting systems
- **Automatic Inclusions**: Statistics calculation, visualization, executive summaries
- **Example Output**: `/summarize-test-results` command with actionable insights

## 🎯 Layer 1 Success Metrics

### **30-Second Success Guarantee:**
- **Zero Learning Curve**: No documentation reading required
- **Instant Productivity**: Working command in 30 seconds or less
- **High Success Rate**: >95% user satisfaction with generated commands
- **Quality Results**: Production-ready commands with comprehensive error handling

### **Quality Assurance Features:**
- **Automatic Error Handling**: File not found, permissions, invalid inputs, format issues
- **Input Validation**: Parameter checking, path sanitization, type verification, safety checks
- **Output Quality**: Consistent formatting, clear indicators, actionable messages, progress tracking
- **Best Practices**: Claude Code conventions, security considerations, performance optimization

## 🔄 Progressive Disclosure Navigation

### **Current Layer (Layer 1):**
**Perfect for**: Newcomers, quick tasks, immediate results, zero complexity

### **Next Level Options:**

#### **Layer 2: Guided Customization**
```
/build-command [type] [description] --customize
```
- **When to use**: Generated command is close but needs specific adjustments
- **Time investment**: 5 minutes guided customization
- **User experience**: 3-5 relevant options, no overwhelming complexity

#### **Layer 3: Professional Assembly**
```
/assemble-command --interactive
```
- **When to use**: Complex workflows, enterprise requirements, maximum control
- **Time investment**: 15-30 minutes professional assembly
- **User experience**: Full component library access with organized tools

<automation trigger="completion">
- Generate complete, functional command with proper YAML frontmatter and v2.0 enhancements
- Validate command syntax and logic for immediate usability
- Provide clear usage instructions and escalation paths to Layer 2/3
- Update auto-generation intelligence based on successful command patterns
</automation>