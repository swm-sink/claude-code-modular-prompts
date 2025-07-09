# /context-prime - Project Context Establishment

**Version**: 1.0.0 | **Status**: Basic | **Last Updated**: 2025-07-09

---

## Purpose

Establish comprehensive project context by analyzing project structure, recent activity, and development patterns to prime Claude for optimal development workflow efficiency.

**Note**: This is a simplified version that focuses on core functionality without the full framework complexity.

---

## How It Works

### 1. Project Analysis
- **File Structure**: Analyze project organization and architecture
- **Recent Activity**: Review recent commits, branches, and changes
- **Development Patterns**: Identify coding conventions and patterns in use
- **Dependencies**: Understand key dependencies and integrations

### 2. Context Establishment
- **Current State**: Establish what the project currently does
- **Active Development**: Identify what's being worked on
- **Key Patterns**: Document architectural and coding patterns
- **Development Environment**: Understand build, test, and deployment setup

### 3. Context Priming
- **Summary Generation**: Create concise project overview
- **Pattern Recognition**: Identify and document key patterns
- **Development Context**: Establish optimal development workflow
- **Quick Reference**: Create accessible context for future sessions

---

## Usage Examples

```bash
# Basic context establishment
/context-prime

# Focus on specific areas
/context-prime --focus architecture
/context-prime --focus recent-changes
/context-prime --focus patterns
/context-prime --focus dependencies
```

---

## What It Does

### Project Structure Analysis
- Scans project directories and files
- Identifies architectural patterns
- Documents key components and modules
- Maps dependencies and relationships

### Recent Activity Review
- Analyzes recent commits (last 10-20)
- Reviews active branches
- Identifies current development focus
- Documents recent changes and decisions

### Pattern Recognition
- Identifies coding conventions
- Documents architectural patterns
- Recognizes development workflows
- Maps testing and quality patterns

### Context Summary
- Creates project overview
- Documents key insights
- Establishes development context
- Provides quick reference guide

---

## Output Format

### Project Overview
```
PROJECT: [project-name]
TYPE: [project-type]
TECH_STACK: [main-technologies]
ARCHITECTURE: [architectural-pattern]
```

### Recent Activity
```
RECENT_COMMITS: [summary-of-recent-changes]
ACTIVE_BRANCHES: [current-development-branches]
DEVELOPMENT_FOCUS: [current-priorities]
```

### Development Patterns
```
CODING_CONVENTIONS: [identified-patterns]
ARCHITECTURE_PATTERNS: [design-patterns-in-use]
TESTING_APPROACH: [testing-strategy]
QUALITY_STANDARDS: [quality-practices]
```

### Context Summary
```
CONTEXT_ESTABLISHED: [timestamp]
KEY_INSIGHTS: [important-findings]
DEVELOPMENT_READY: [context-status]
QUICK_REFERENCE: [essential-info]
```

---

## Key Features

### ✅ Self-Contained
- No external module dependencies
- Direct analysis and processing
- Built-in error handling
- Standalone functionality

### ✅ Fast & Efficient
- Quick project scanning
- Focused analysis
- Minimal overhead
- Rapid context establishment

### ✅ Comprehensive
- Project structure analysis
- Recent activity review
- Pattern recognition
- Context summarization

### ✅ Practical
- Clear, actionable output
- Development-focused insights
- Quick reference generation
- Session context establishment

---

## Error Handling

### Common Issues
- **Large Projects**: Focuses on key directories and files
- **No Git History**: Uses file analysis instead
- **Complex Architecture**: Provides high-level overview
- **Missing Dependencies**: Documents what's available

### Graceful Degradation
- Provides partial context if full analysis fails
- Uses available information sources
- Focuses on accessible data
- Maintains useful output even with limitations

---

## Best Practices

### When to Use
- **New Project**: Understanding unfamiliar codebase
- **Session Start**: Establishing context for development
- **Team Onboarding**: Getting up to speed quickly
- **Context Loss**: Re-establishing project understanding

### Optimization Tips
- Use `--focus` flags for targeted analysis
- Run regularly to maintain context
- Combine with other research commands
- Update context after major changes

---

## Differences from Full Framework

### Simplified Approach
- **No Complex XML**: Simple workflow steps
- **No Module Dependencies**: Self-contained logic
- **No Advanced Frameworks**: Basic analysis patterns
- **No Mandatory Enforcement**: Supportive workflow

### Core Focus
- **Essential Functionality**: Core context establishment
- **Practical Output**: Development-ready insights
- **Fast Execution**: Minimal overhead
- **Clear Results**: Actionable information

---

## Integration

### Works Well With
- `/research` - For deeper analysis
- `/task` - For focused development
- `/feature` - For feature development
- `/review` - For code review context

### Typical Workflow
1. **Start**: `/context-prime` to establish project context
2. **Research**: `/research` for deeper investigation
3. **Development**: `/task` or `/feature` for implementation
4. **Review**: `/review` for quality assurance

---

**Note**: This simplified command provides core context establishment functionality without the complexity of the full framework. For advanced features like CARE framework integration, complex module orchestration, or meta-capabilities, use the full framework commands.