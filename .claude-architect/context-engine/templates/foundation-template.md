# {{PROJECT_NAME}} - Project Foundation Context
# Layer 1: Core Project Identity and Architectural Philosophy
# Generated: {{GENERATION_TIMESTAMP}}
# Confidence: {{FOUNDATION_CONFIDENCE_SCORE}}

<!--
CONTEXT LAYER: Project Foundation (Priority: 10, Token Budget: 2000)
PURPOSE: Establishes fundamental project identity and overarching patterns
DEPENDENCIES: None (root layer)
PROVIDES: Foundational context to all other layers
-->

## Project Identity

### Core Project Information
**Project Name**: {{PROJECT_NAME}}
**Domain**: {{PROJECT_DOMAIN}}
**Project Type**: {{PROJECT_TYPE}}
**Development Stage**: {{PROJECT_STAGE}}

### Mission & Vision
{{#if PROJECT_MISSION}}
**Mission**: {{PROJECT_MISSION}}
{{/if}}

{{#if PROJECT_VISION}}
**Vision**: {{PROJECT_VISION}}
{{/if}}

**Primary Goals**:
{{#each PRIMARY_GOALS}}
- {{this}}
{{/each}}

**Target Users**: {{TARGET_USERS}}

{{#if VALUE_PROPOSITIONS}}
### Value Propositions
{{#each VALUE_PROPOSITIONS}}
- {{this}}
{{/each}}
{{/if}}

## Architectural Philosophy

### Design Principles
{{#each DESIGN_PRINCIPLES}}
- **{{name}}**: {{description}}
{{/each}}

### Technology Philosophy
**Core Technology Stack**: {{TECHNOLOGY_STACK}}

{{#if TECH_DECISION_RATIONALE}}
**Technology Rationale**:
{{TECH_DECISION_RATIONALE}}
{{/if}}

### Scalability & Performance Priorities
{{#if SCALABILITY_APPROACH}}
**Scalability Approach**: {{SCALABILITY_APPROACH}}
{{/if}}

{{#if PERFORMANCE_PRIORITIES}}
**Performance Priorities**:
{{#each PERFORMANCE_PRIORITIES}}
- {{this}}
{{/each}}
{{/if}}

{{#if QUALITY_FOCUS}}
**Quality Focus Areas**:
{{#each QUALITY_FOCUS}}
- {{this}}
{{/each}}
{{/if}}

## Team Culture & Working Agreements

### Team Structure
**Team Size**: {{TEAM_SIZE}}
**Team Composition**: {{TEAM_COMPOSITION}}
{{#if TEAM_EXPERTISE_LEVEL}}
**Expertise Level**: {{TEAM_EXPERTISE_LEVEL}}
{{/if}}

### Communication Patterns
{{#if COMMUNICATION_STYLE}}
**Communication Style**: {{COMMUNICATION_STYLE}}
{{/if}}

{{#if MEETING_CADENCE}}
**Meeting Cadence**: {{MEETING_CADENCE}}
{{/if}}

{{#if DECISION_MAKING_PROCESS}}
**Decision-Making Process**: {{DECISION_MAKING_PROCESS}}
{{/if}}

### Working Agreements
{{#if WORKING_AGREEMENTS}}
{{#each WORKING_AGREEMENTS}}
- {{this}}
{{/each}}
{{/if}}

{{#if KNOWLEDGE_SHARING_APPROACH}}
**Knowledge Sharing**: {{KNOWLEDGE_SHARING_APPROACH}}
{{/if}}

## Historical Context & Evolution

### Project Timeline
{{#if PROJECT_START_DATE}}
**Project Started**: {{PROJECT_START_DATE}}
{{/if}}

{{#if KEY_MILESTONES}}
**Key Milestones**:
{{#each KEY_MILESTONES}}
- **{{date}}**: {{milestone}}
{{/each}}
{{/if}}

### Major Decisions & Pivots
{{#if MAJOR_DECISIONS}}
{{#each MAJOR_DECISIONS}}
#### {{decision_title}}
**Date**: {{date}}
**Context**: {{context}}
**Decision**: {{decision}}
{{#if rationale}}
**Rationale**: {{rationale}}
{{/if}}
{{#if impact}}
**Impact**: {{impact}}
{{/if}}

{{/each}}
{{/if}}

### Lessons Learned
{{#if LESSONS_LEARNED}}
{{#each LESSONS_LEARNED}}
- **{{category}}**: {{lesson}}
{{/each}}
{{/if}}

## Core Constraints & Principles

### Technical Constraints
{{#if TECHNICAL_CONSTRAINTS}}
{{#each TECHNICAL_CONSTRAINTS}}
- **{{constraint_type}}**: {{description}}
{{/each}}
{{/if}}

### Business Constraints
{{#if BUSINESS_CONSTRAINTS}}
{{#each BUSINESS_CONSTRAINTS}}
- **{{constraint_type}}**: {{description}}
{{/each}}
{{/if}}

### Non-Functional Requirements
{{#if NON_FUNCTIONAL_REQUIREMENTS}}
{{#each NON_FUNCTIONAL_REQUIREMENTS}}
- **{{requirement_type}}**: {{description}}
{{/each}}
{{/if}}

## Current Challenges & Aspirations

### Primary Pain Points
{{#if CURRENT_PAIN_POINTS}}
{{#each CURRENT_PAIN_POINTS}}
- **{{category}}**: {{description}}
{{#if impact}}
  - *Impact*: {{impact}}
{{/if}}
{{/each}}
{{/if}}

### Success Criteria (6-month outlook)
{{#if SUCCESS_CRITERIA}}
{{#each SUCCESS_CRITERIA}}
- {{this}}
{{/each}}
{{/if}}

{{#if ASPIRATIONAL_GOALS}}
### Aspirational Goals
{{#each ASPIRATIONAL_GOALS}}
- {{this}}
{{/each}}
{{/if}}

---

## Context Inheritance Exports

This foundation context provides the following variables to child contexts:

**Project Identity Variables**:
- `project_name`: {{PROJECT_NAME}}
- `domain_context`: {{PROJECT_DOMAIN}}
- `technology_stack`: {{TECHNOLOGY_STACK}}
- `team_size`: {{TEAM_SIZE}}

**Cultural Pattern Variables**:
{{#if CULTURAL_PATTERNS}}
{{#each CULTURAL_PATTERNS}}
- `{{key}}`: {{value}}
{{/each}}
{{/if}}

**Core Constraint Variables**:
{{#if CORE_CONSTRAINTS}}
{{#each CORE_CONSTRAINTS}}
- `{{constraint_key}}`: {{constraint_value}}
{{/each}}
{{/if}}

---

*This context was generated from consultation stages 1-4 and provides the foundational understanding for all subsequent context layers.*

<!-- VALIDATION CHECKPOINTS -->
<!-- ✓ Project identity clearly established -->
<!-- ✓ Architectural philosophy documented -->
<!-- ✓ Team culture captured -->
<!-- ✓ Historical context preserved -->
<!-- ✓ Inheritance variables defined -->

<!-- TOKEN BUDGET USAGE: Estimated {{ESTIMATED_TOKEN_COUNT}} tokens -->
<!-- CONFIDENCE SCORE: {{FOUNDATION_CONFIDENCE_SCORE}}/10 -->
<!-- LAST UPDATED: {{GENERATION_TIMESTAMP}} -->