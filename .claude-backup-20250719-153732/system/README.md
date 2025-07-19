| version | last_updated | status |
|---------|--------------|--------|
| 3.0.0   | 2025-07-12   | stable |

# System Directory - Framework Infrastructure

## Overview

This directory contains the **core infrastructure components** that support the Claude Code framework. These modules provide the foundational services that enable commands and modules to work together reliably and efficiently.

## System Components

```
system/
├── context/           # Context management and preservation
├── quality/           # Quality gates and validation infrastructure  
├── security/          # Security frameworks and threat modeling
├── git/               # Git operations and version control
└── session/           # Session management and artifact tracking
```

## Core Infrastructure

### Context Management (`/context/`)
**Purpose**: Context preservation, artifact management, and project state

**Key Components**:
- `project-priming.md` - Comprehensive codebase analysis and context building
- `decision-artifacts.md` - Decision tracking and audit trail management
- `restore-session.md` - Session restoration and continuity
- `template-resolution.md` - Dynamic template processing and configuration

**Services Provided**:
- Project context analysis and preservation
- Decision artifact creation and management
- Session state restoration and continuity
- Template resolution and configuration management

### Quality Infrastructure (`/quality/`)
**Purpose**: Universal quality gates, validation frameworks, and standards enforcement

**Key Components** (36 modules):
- `universal-quality-gates.md` - Comprehensive quality validation framework
- `tdd.md` - Test-driven development enforcement
- `production-standards.md` - Production readiness validation
- `performance-gates.md` - Performance benchmarking and monitoring
- `critical-thinking.md` - Cognitive quality and analysis standards

**Services Provided**:
- Quality gate enforcement across all operations
- TDD cycle validation and compliance
- Production readiness assessment
- Performance monitoring and optimization
- Security validation and threat assessment

### Security Infrastructure (`/security/`)
**Purpose**: Security frameworks, threat modeling, and compliance validation

**Key Components**:
- `threat-modeling.md` - Security analysis and vulnerability assessment
- `audit.md` - Security audit frameworks and monitoring
- `financial-compliance.md` - Financial and regulatory compliance

**Services Provided**:
- Threat modeling and vulnerability assessment
- Security audit and compliance monitoring
- Financial compliance validation
- Security documentation and standards

### Git Operations (`/git/`)
**Purpose**: Version control integration, workflow automation, and repository management

**Key Components**:
- `conventional-commits.md` - Standardized commit message formatting
- `git-operations.md` - Git workflow automation and best practices
- `worktree-isolation.md` - Development branch isolation and safety

**Services Provided**:
- Automated git operations and workflow management
- Conventional commit formatting and validation
- Branch isolation and development safety
- Repository management and optimization

### Session Management (`/session/`)
**Purpose**: Session tracking, compression, and reliability

**Key Components**:
- `session-management.md` - Core session tracking and coordination
- `session-compression.md` - Context compression and optimization
- `session-reliability.md` - Session recovery and fault tolerance
- `session-storage.md` - Session persistence and artifact storage

**Services Provided**:
- Session lifecycle management and tracking
- Context compression and memory optimization
- Session recovery and fault tolerance
- Artifact persistence and retrieval

## Infrastructure Architecture

### Service Integration
System components work together to provide:

```
User Request → Context Analysis → Quality Gates → Execution → Session Tracking
      ↓              ↓              ↓              ↓              ↓
  Project State → Standards → Security Check → Git Ops → Artifact Storage
```

### Quality Assurance Pipeline
Every operation flows through:

1. **Context Validation**: Project state and requirements analysis
2. **Security Assessment**: Threat modeling and vulnerability scanning
3. **Quality Gates**: TDD, coverage, performance, and compliance validation
4. **Execution Monitoring**: Real-time performance and error tracking
5. **Session Management**: State preservation and artifact creation

### Error Recovery Framework
Infrastructure provides comprehensive error recovery:

- **Context Recovery**: Project state restoration from artifacts
- **Quality Rollback**: Rollback to last passing quality state
- **Security Isolation**: Threat containment and system protection
- **Git Recovery**: Version control rollback and branch management
- **Session Recovery**: Session state restoration and continuity

## Key Principles

1. **Infrastructure Focus**: System-level functionality only
2. **Service Orientation**: Provides services to commands and modules
3. **Reliability**: Critical infrastructure for framework operation
4. **Integration**: Seamless integration with prompt engineering components

## Usage Guidelines

System components are used by commands and modules but do not contain prompt templates themselves.
They provide the infrastructure that enables reliable framework operation.

### For Framework Users
- System components work automatically in the background
- No direct interaction required - services are transparent
- Quality gates and security validation happen automatically
- Session management preserves context across interactions

### For Framework Developers
- Use system services through standardized interfaces
- Don't duplicate infrastructure functionality in modules
- Follow service contracts and error handling patterns
- Contribute infrastructure improvements through proper channels

## See Also

- `/commands/` - Commands that use these infrastructure services
- `/modules/` - Modules that integrate with infrastructure services
- `/prompt_eng/` - Advanced prompt engineering using infrastructure
- Main README.md - Complete framework overview