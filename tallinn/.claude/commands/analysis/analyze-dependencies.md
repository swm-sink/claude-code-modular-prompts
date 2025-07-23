---
name: /analyze-dependencies
description: Advanced dependency analysis with intelligent mapping, vulnerability scanning, and optimization recommendations
usage: /analyze-dependencies [analysis_type] [scan_depth]
tools: Read, Write, Edit, Bash, Grep
---

# Advanced dependency analysis with intelligent mapping, vulnerability scanning, and optimization recommendations

**Usage**: `/analyze-dependencies $ANALYSIS_TYPE $SCAN_DEPTH`

## Key Arguments

- **$ANALYSIS_TYPE** (optional): Type of dependency analysis to perform
- **$SCAN_DEPTH** (optional): Depth of dependency scanning

## Examples

```bash
/analyze dependencies security
```
*Security vulnerability analysis*

```bash
/analyze dependencies --outdated
```
*Outdated package detection*

## Core Logic

components/validation/input-validation.md
 components/workflow/command-execution.md
 components/workflow/error-handling.md
 components/interaction/progress-reporting.md
 components/analysis/codebase-discovery.md
 components/analysis/dependency-mapping.md
 components/workflow/report-generation.md

You are an advanced dependency analysis specialist. The user wants to perform comprehensive dependency analysis with intelligent mapping and vulnerability scanning.

**Analysis Process:**
1. **Dependency Mapping**: Create comprehensive dependency graphs and relationships
2. **Vulnerability Scanning**: Scan for known security vulnerabilities and CVEs
3. **Version Analysis**: Analyze version compatibility and update requirements
4. **Conflict Detection**: Identify dependency conflicts and resolution strategies
5. **Optimization Assessment**: Recommend optimization and cleanup opportunities

**Implementation Strategy:**
- Generate detailed dependency trees and impact analysis
- Perform security vulnerability scanning with CVE databases
- Analyze license compatibility and compliance issues
- Identify circular dependencies and resolution strategies
- Create prioritized update and optimization roadmaps

## Essential Component Logic

### Input Validation
**Input Validation**: Comprehensive input validation for command arguments, ensuring type safety, format correctness, and security before execution. 1. **Type Validation**: - String: Non-empty, length limits, character res...

**Key Criteria**: 1. **Type Validation**: - String: Non-empty, length limits, character restrictions - Number: Range validation, integer vs float - Boolean: True/false ...

*[Additional logic optimized for execution...]*

## Execution Pattern

1. **Input Processing**: Validate and process $ARGUMENTS
2. **Core Execution**: Execute main command logic
3. **Output Generation**: Generate structured results

