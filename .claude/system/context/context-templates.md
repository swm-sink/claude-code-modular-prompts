| version | last_updated | status |
|---------|--------------|--------|
| 3.0.0   | $(date '+%Y-%m-%d') | stable |

# Context Templates Collection

## Overview

This document contains consolidated context templates for session management, decision logging, and project context tracking. These templates support the framework's context preservation and documentation capabilities.

## Session Context Template

### Session Metadata
- **Session ID**: [GENERATED]
- **Start Time**: [TIMESTAMP]
- **Framework Version**: 3.0.0
- **Active Branch**: [BRANCH_NAME]

### Session Objectives
[Define clear session goals and expected outcomes]

### Context Preservation
#### Key Decisions
- [Decision 1: Rationale and impact]
- [Decision 2: Rationale and impact]

#### Modified Files
- [File path: Nature of changes]
- [File path: Nature of changes]

#### Open Tasks
- [ ] [Task description and priority]
- [ ] [Task description and priority]

### Session State
#### Current Focus
[Active work area and immediate next steps]

#### Blockers/Issues
[Any impediments or concerns]

#### Progress Summary
[What has been accomplished in this session]

## Decision Log Template

### Decision Entry
**Date**: [TIMESTAMP]  
**Decision ID**: [DEC-XXX]  
**Status**: [PROPOSED | ACCEPTED | REJECTED | SUPERSEDED]

#### Context
[What is the issue or opportunity being addressed?]

#### Decision
[What was decided?]

#### Rationale
[Why was this decision made? What alternatives were considered?]

#### Consequences
##### Positive
- [Expected benefit 1]
- [Expected benefit 2]

##### Negative
- [Potential drawback 1]
- [Potential drawback 2]

##### Risks
- [Risk and mitigation strategy]

#### Implementation
- **Affected Components**: [List of files/modules]
- **Timeline**: [Expected implementation timeframe]
- **Dependencies**: [What must be completed first]

#### Review
- **Review Date**: [When to review this decision]
- **Success Metrics**: [How to measure success]
- **Rollback Plan**: [How to undo if needed]

## Project Context Template

### Project Overview
- **Project Name**: [PROJECT_NAME]
- **Framework Version**: 3.0.0
- **Configuration**: PROJECT_CONFIG.xml

### Architecture Context
#### Technology Stack
- **Primary Language**: [DETECTED_LANGUAGE]
- **Frameworks**: [LIST_OF_FRAMEWORKS]
- **Dependencies**: [KEY_DEPENDENCIES]

#### Project Structure
```
[PROJECT_ROOT]/
├── src/          # [Customizable via PROJECT_CONFIG]
├── tests/        # [Customizable via PROJECT_CONFIG]
├── docs/         # [Customizable via PROJECT_CONFIG]
└── .claude/      # Framework configuration
```

### Quality Standards
- **Test Coverage**: [PROJECT_CONFIG: test_coverage.threshold]%
- **Performance**: [PROJECT_CONFIG: performance.response_time_p95]ms
- **TDD Enforcement**: [PROJECT_CONFIG: test_first_enforcement]

### Development Patterns
#### Established Conventions
- [Pattern 1: Description and usage]
- [Pattern 2: Description and usage]

#### Code Standards
- [Standard 1: Description and examples]
- [Standard 2: Description and examples]

### Context Preservation
#### Key Architectural Decisions
- [Decision 1: Impact on system design]
- [Decision 2: Impact on system design]

#### Current Development Focus
- [Primary areas of active development]
- [Upcoming priorities]

#### Technical Debt
- [Identified debt items and remediation plans]

## Template Usage Guidelines

### Session Context
- Use at the start of each development session
- Update throughout session as context changes
- Archive completed sessions for reference

### Decision Log
- Create entry for all significant decisions
- Include alternative approaches considered
- Regular review of implemented decisions

### Project Context
- Update when project structure changes
- Review when onboarding new team members
- Keep synchronized with PROJECT_CONFIG.xml

## Integration Points

### Framework Integration
- Templates support context preservation patterns
- Integrate with session management modules
- Compatible with project configuration system

### Command Integration
- Session templates used by `/session` command
- Decision logs support architectural decisions
- Project context supports `/context-prime` command

### Quality Integration
- Templates support quality tracking
- Decision logs include quality implications
- Project context enforces quality standards

## Maintenance

### Template Updates
- Keep templates synchronized with framework version
- Update when new context requirements emerge
- Maintain backward compatibility when possible

### Usage Monitoring
- Track template usage patterns
- Collect feedback on template effectiveness
- Continuously improve based on usage data