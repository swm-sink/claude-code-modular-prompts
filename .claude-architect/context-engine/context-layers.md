# Claude Context Architect - Context Layers Guide

## Overview

The Claude Context Architect employs a sophisticated 5-layer hierarchical context system that transforms consultation insights into deep project understanding. Each layer serves a specific purpose and builds upon the layers below it, creating a comprehensive knowledge architecture.

## Layer Architecture

### Layer 1: Project Foundation Context

**Purpose**: Establishes the fundamental project identity and overarching patterns that define the project's core essence.

**Key Responsibilities**:
- Project mission, vision, and identity
- Fundamental architectural decisions and philosophy
- Team culture and working agreements
- Historical evolution and key milestones
- Core constraints and principles

**Primary Files**:
- `CLAUDE.md` - Master project context and memory
- `.claude/project-dna.md` - Core project characteristics
- `.claude/project-evolution.md` - Historical development patterns
- `.claude/decision-log.md` - Key architectural and strategic decisions

**Content Structure**:
```markdown
## Project Identity
- Project name, domain, and mission
- Core value propositions
- Target users and use cases

## Architectural Philosophy  
- Design principles and patterns
- Technology choices rationale
- Scalability and performance priorities

## Team Culture
- Working agreements and communication patterns
- Decision-making processes
- Knowledge sharing approaches

## Historical Context
- Project evolution timeline
- Key milestones and pivots
- Lessons learned from major decisions
```

**Token Budget**: 2000 tokens (highest priority)
**Dependencies**: None (root layer)
**Provides**: Foundational context to all other layers

---

### Layer 2: Domain Intelligence Context

**Purpose**: Captures deep business domain expertise, terminology, and the specific knowledge required to understand the problem space.

**Key Responsibilities**:
- Domain-specific terminology and glossaries
- Business rules and logic patterns
- User personas and journey mapping
- Data model relationships and flows
- Integration requirements and external touchpoints

**Primary Files**:
- `.claude/domain-context.md` - Core domain knowledge
- `.claude/domain-glossary.md` - Terminology definitions
- `.claude/business-rules.md` - Domain logic and constraints
- `.claude/user-journeys.md` - User workflow patterns
- `.claude/data-models.md` - Data relationships and structures

**Content Structure**:
```markdown
## Domain Overview
- Business context and industry background
- Core domain concepts and relationships
- Key stakeholders and their needs

## Terminology & Glossary
- Domain-specific terms and definitions
- Acronyms and technical vocabulary
- Conceptual models and frameworks

## Business Logic
- Core business rules and constraints
- Workflow patterns and processes
- Decision trees and logic flows

## User Understanding
- Primary user personas and goals
- User journey mapping and touchpoints
- Pain points and success criteria

## Data Architecture
- Core data entities and relationships
- Data flow patterns and transformations
- Integration points and external dependencies
```

**Token Budget**: 1500 tokens
**Dependencies**: Project Foundation Context
**Provides**: Domain expertise to technical and workflow layers

---

### Layer 3: Technical Architecture Context

**Purpose**: Defines technical implementation patterns, framework conventions, and the specific technical approach used in the project.

**Key Responsibilities**:
- Framework usage patterns and conventions
- Architectural decisions and rationale
- Code organization and structure principles
- Testing strategies and quality approaches
- Deployment and infrastructure patterns

**Primary Files**:
- `.claude/technical-context.md` - Core technical architecture
- `.claude/architecture-patterns.md` - Design patterns and approaches
- `.claude/framework-conventions.md` - Framework-specific patterns
- `.claude/testing-strategy.md` - Testing approaches and standards
- `.claude/deployment-patterns.md` - Deployment and infrastructure

**Content Structure**:
```markdown
## Technical Stack
- Primary frameworks and libraries
- Language choices and versions
- Development tools and dependencies

## Architecture Patterns
- Overall system architecture approach
- Design patterns and principles
- Component organization strategies

## Code Conventions
- Naming conventions and standards
- File organization patterns
- Code style and formatting rules

## Testing Strategy
- Testing pyramid and approach
- Test types and coverage requirements
- Quality gates and validation

## Deployment & Infrastructure
- Deployment pipeline and processes
- Infrastructure patterns and choices
- Monitoring and observability approaches
```

**Token Budget**: 2000 tokens
**Dependencies**: Project Foundation, Domain Intelligence
**Provides**: Technical patterns to workflow and integration layers

---

### Layer 4: Workflow Orchestration Context

**Purpose**: Captures team processes, development workflows, and operational procedures that govern how work gets done.

**Key Responsibilities**:
- Development workflows and processes
- Code review standards and procedures
- Deployment workflows and release processes
- Troubleshooting guides and operational knowledge
- Team collaboration patterns and tools

**Primary Files**:
- `.claude/workflow-context.md` - Core workflow patterns
- `.claude/development-process.md` - Development lifecycle
- `.claude/code-review-standards.md` - Review processes
- `.claude/deployment-workflow.md` - Release procedures
- `.claude/troubleshooting-guides.md` - Operational knowledge

**Content Structure**:
```markdown
## Development Workflow
- Feature development process
- Branch management and git workflow
- Task tracking and project management

## Quality Assurance
- Code review process and standards
- Testing workflows and automation
- Quality gates and acceptance criteria

## Deployment Process
- Release preparation and validation
- Deployment procedures and rollback
- Environment management and promotion

## Team Collaboration
- Communication patterns and tools
- Meeting cadences and decision processes
- Knowledge sharing and documentation

## Operational Procedures
- Troubleshooting guides and runbooks
- Monitoring and alerting responses
- Maintenance and support procedures
```

**Token Budget**: 1200 tokens
**Dependencies**: Project Foundation, Domain Intelligence, Technical Architecture
**Provides**: Process knowledge to integration layer

---

### Layer 5: Integration Mesh Context

**Purpose**: Manages cross-cutting concerns and system interconnections that span multiple layers and components.

**Key Responsibilities**:
- Cross-cutting concerns (security, logging, monitoring)
- System integration patterns and boundaries
- External dependency management
- Error handling and resilience strategies
- Performance and observability patterns

**Primary Files**:
- `.claude/integration-context.md` - Integration patterns
- `.claude/cross-cutting-concerns.md` - System-wide concerns
- `.claude/system-boundaries.md` - Interface definitions
- `.claude/external-dependencies.md` - Third-party integrations

**Content Structure**:
```markdown
## Cross-Cutting Concerns
- Security patterns and requirements
- Logging and monitoring strategies
- Error handling and resilience patterns

## System Integration
- API design and interface patterns
- Message passing and event handling
- Data synchronization and consistency

## External Dependencies
- Third-party service integrations
- External API usage patterns
- Dependency management strategies

## Observability
- Metrics collection and analysis
- Distributed tracing approaches
- Performance monitoring patterns

## Resilience & Recovery
- Error handling strategies
- Circuit breaker and retry patterns
- Disaster recovery procedures
```

**Token Budget**: 800 tokens
**Dependencies**: All previous layers
**Provides**: System-wide integration knowledge

## Layer Interaction Patterns

### Inheritance Flow
Context information flows down the hierarchy:
1. **Project Foundation** provides fundamental identity to all layers
2. **Domain Intelligence** adds business context to technical layers
3. **Technical Architecture** informs workflow and integration approaches
4. **Workflow Orchestration** guides integration implementations
5. **Integration Mesh** synthesizes all concerns into system-wide patterns

### Cross-References
Layers can reference each other through:
- **Upward References**: Child layers referencing parent context
- **Lateral References**: Peer layers sharing related information
- **Downward References**: Parent layers providing guidance to children

### Conflict Resolution
When contexts conflict:
1. Higher priority layers override lower priority
2. More recent modifications take precedence
3. Explicit context directives can override inheritance
4. Child contexts can override inherited parent values

## Token Management Strategy

### Budget Allocation
- **Total Budget**: 8000 tokens maximum
- **Priority Weighting**: Higher layers get guaranteed minimums
- **Overflow Handling**: Lowest priority content trimmed first
- **Dynamic Adjustment**: Budget reallocated based on context relevance

### Loading Strategies
- **Minimal**: Project Foundation only (startup performance)
- **Standard**: Foundation + Domain + Technical (most common)
- **Comprehensive**: All layers except Integration (deep understanding)
- **Full**: All layers (complete project context)

## Quality Assurance

### Validation Gates
- **Structural**: Required files exist and are well-formed
- **Content**: No placeholder content, minimum quality thresholds
- **Integration**: Cross-references resolve, no circular dependencies
- **Performance**: Token budgets respected, loading times acceptable

### Maintenance Procedures
- **Monthly Reviews**: Content freshness and accuracy
- **Quarterly Optimization**: Performance tuning and pruning
- **Yearly Revision**: Major architectural updates
- **Automatic Cleanup**: Deprecated content and broken references

## Evolution and Adaptation

### Adaptation Triggers
- **Project Growth**: Team size or scope changes
- **Technical Evolution**: Framework or architecture updates
- **Domain Expansion**: New business requirements or domains
- **Process Maturation**: Workflow and quality improvements

### Migration Support
- **Backward Compatibility**: Older context versions still readable
- **Guided Updates**: Semi-automated migration assistance
- **Validation Support**: Integrity checking during transitions
- **Rollback Capability**: Revert to previous context versions

This layered approach ensures that Claude receives progressively richer context about your project, building from foundational understanding to deep operational knowledge. Each layer contributes its specialized expertise while building upon the insights from the layers below it.