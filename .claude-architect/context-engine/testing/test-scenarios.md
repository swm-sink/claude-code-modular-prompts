# Context Testing Scenarios
## Comprehensive Test Cases for Context Effectiveness Validation

### Overview
This document defines detailed test scenarios that validate how effectively generated context improves Claude's understanding and responses. Each scenario includes specific prompts, expected behaviors, and measurable success criteria.

---

## Category 1: Code Generation Tests
*Validates that Claude generates project-appropriate code that follows project conventions*

### Scenario 1.1: Component Generation with Project Patterns
**Context Requirements**: Technical architecture, coding conventions, component patterns

**Test Prompt**: "Create a new user authentication component following the project's established patterns."

**Without Enhanced Context**:
- Generic component structure
- Standard naming conventions
- Common authentication patterns
- No project-specific integrations

**With Enhanced Context Expected**:
- Uses project's specific component architecture
- Follows established naming conventions
- Integrates with project's auth system
- Includes project-specific error handling
- Uses configured state management pattern

**Success Metrics**:
- Convention adherence: 90%+ matching project patterns
- Integration accuracy: All dependencies correctly identified
- Code quality: Passes project linting/formatting rules
- Completeness: Includes all standard component features

### Scenario 1.2: API Endpoint Creation
**Context Requirements**: API architecture, routing patterns, database schemas

**Test Prompt**: "Add a new endpoint to retrieve user preferences with proper validation and error handling."

**Expected Improvements**:
- Uses correct routing patterns
- Implements project's validation strategy
- Follows established error response format
- Integrates with existing middleware
- Uses correct database access patterns

**Validation Criteria**:
- Endpoint structure matches project patterns
- Validation rules align with existing endpoints
- Error handling follows project standards
- Database queries use established patterns

### Scenario 1.3: Test Generation
**Context Requirements**: Testing frameworks, test patterns, coverage standards

**Test Prompt**: "Write comprehensive tests for the user authentication component."

**Expected Improvements**:
- Uses project's testing framework correctly
- Follows established test organization
- Includes project-specific test utilities
- Covers edge cases relevant to the project
- Matches existing test naming conventions

---

## Category 2: Architecture Advice Tests
*Validates that Claude provides recommendations aligned with project architecture*

### Scenario 2.1: Scalability Recommendations
**Context Requirements**: Current architecture, performance constraints, scaling history

**Test Prompt**: "Our user registration is slowing down. What architectural changes would you recommend?"

**Without Enhanced Context**:
- Generic scaling advice
- Common performance patterns
- Standard caching solutions
- Generic database optimization

**With Enhanced Context Expected**:
- Considers existing architecture constraints
- Aligns with project's scaling strategy
- Recommends compatible technologies
- Addresses project-specific bottlenecks
- Considers team expertise and preferences

**Success Metrics**:
- Recommendation feasibility: 95%+ implementable
- Architecture alignment: Compatible with existing systems
- Technology fit: Uses approved/preferred technologies
- Problem targeting: Addresses actual bottlenecks

### Scenario 2.2: Integration Architecture
**Context Requirements**: Current integrations, API patterns, security requirements

**Test Prompt**: "How should we integrate with the new payment provider while maintaining our security standards?"

**Expected Improvements**:
- Uses project's integration patterns
- Follows established security practices
- Considers existing payment flows
- Aligns with current API design
- Addresses project-specific compliance needs

### Scenario 2.3: Database Schema Evolution
**Context Requirements**: Database schema, migration patterns, data relationships

**Test Prompt**: "Design a schema change to support user roles and permissions."

**Expected Improvements**:
- Compatible with existing schema
- Uses established migration patterns
- Considers current data relationships
- Follows project's naming conventions
- Addresses existing permission patterns

---

## Category 3: Domain Language Tests
*Validates that Claude uses correct project-specific terminology and concepts*

### Scenario 3.1: Business Logic Implementation
**Context Requirements**: Domain model, business rules, terminology

**Test Prompt**: "Implement the order processing workflow according to our business rules."

**Without Enhanced Context**:
- Generic e-commerce patterns
- Standard order states
- Common validation rules
- General business logic

**With Enhanced Context Expected**:
- Uses project-specific order states
- Implements actual business rules
- Uses correct domain terminology
- Considers project-specific workflows
- Integrates with existing business services

**Success Metrics**:
- Terminology accuracy: 100% correct domain terms
- Rule implementation: All business rules correctly applied
- Workflow alignment: Matches established processes
- Integration correctness: Uses existing services properly

### Scenario 3.2: Data Model Discussion
**Context Requirements**: Data model, relationships, business concepts

**Test Prompt**: "Explain how customer segmentation affects our pricing model."

**Expected Improvements**:
- Uses project's customer segmentation approach
- References actual pricing rules
- Mentions specific business metrics
- Considers existing customer data
- Addresses real business constraints

### Scenario 3.3: Feature Specification
**Context Requirements**: Feature requirements, user flows, business objectives

**Test Prompt**: "Specify the requirements for the loyalty program feature."

**Expected Improvements**:
- Aligns with existing loyalty concepts
- Uses established user journey patterns
- References current reward systems
- Considers integration with existing features
- Addresses real business objectives

---

## Category 4: Workflow Understanding Tests
*Validates that Claude respects and enhances team processes*

### Scenario 4.1: Development Workflow
**Context Requirements**: Git workflow, CI/CD pipeline, code review process

**Test Prompt**: "Walk me through the process for deploying this feature to production."

**Without Enhanced Context**:
- Generic git workflow
- Standard deployment steps
- Common review practices
- General CI/CD patterns

**With Enhanced Context Expected**:
- Uses actual branching strategy
- References specific deployment pipeline
- Mentions required approvals/checks
- Considers environment-specific steps
- Addresses project's rollback procedures

**Success Metrics**:
- Process accuracy: 100% alignment with actual workflow
- Step completeness: All required steps included
- Tool accuracy: Correct tools and commands referenced
- Context awareness: Considers project-specific constraints

### Scenario 4.2: Code Review Guidelines
**Context Requirements**: Review standards, quality gates, team preferences

**Test Prompt**: "Review this pull request and provide feedback according to our standards."

**Expected Improvements**:
- Applies project's coding standards
- Checks against established quality gates
- Uses team's preferred feedback style
- Considers architectural guidelines
- References relevant documentation

### Scenario 4.3: Issue Triage Process
**Context Requirements**: Bug classification, priority matrix, assignment rules

**Test Prompt**: "How should we prioritize and assign these reported issues?"

**Expected Improvements**:
- Uses project's priority classification
- Applies established severity levels
- Considers team capacity and expertise
- References historical similar issues
- Follows established escalation paths

---

## Category 5: Integration Awareness Tests
*Validates that Claude understands system boundaries and connections*

### Scenario 5.1: API Integration Impact
**Context Requirements**: Service dependencies, API contracts, integration patterns

**Test Prompt**: "What will be impacted if we change the user service API?"

**Without Enhanced Context**:
- General API impact considerations
- Common dependency patterns
- Standard breaking change risks
- Generic rollback advice

**With Enhanced Context Expected**:
- Identifies actual dependent services
- References specific API consumers
- Considers contract versioning strategy
- Addresses project-specific migration needs
- Mentions relevant integration tests

**Success Metrics**:
- Dependency accuracy: 100% correct service identification
- Impact completeness: All affected systems mentioned
- Migration strategy: Aligned with project approach
- Risk assessment: Addresses actual project risks

### Scenario 5.2: Database Migration Impact
**Context Requirements**: Data relationships, migration strategy, downstream systems

**Test Prompt**: "Plan the migration for splitting the user table into separate profile tables."

**Expected Improvements**:
- Considers actual data relationships
- Uses established migration patterns
- Addresses specific downstream impacts
- Plans for project's data consistency needs
- Includes relevant backup/rollback steps

### Scenario 5.3: Third-Party Integration Changes
**Context Requirements**: External service dependencies, integration patterns, fallback strategies

**Test Prompt**: "The analytics service is changing their API. How should we adapt?"

**Expected Improvements**:
- References current integration implementation
- Uses established adapter patterns
- Considers fallback mechanisms
- Addresses data migration needs
- Plans for gradual transition

---

## Category 6: Performance and Optimization Tests
*Validates context-aware performance optimization recommendations*

### Scenario 6.1: Query Optimization
**Context Requirements**: Database schema, query patterns, performance constraints

**Test Prompt**: "Optimize the user dashboard query that's running slowly."

**Expected Improvements**:
- Analyzes actual schema structure
- Considers existing indexes
- Uses project's optimization patterns
- Addresses specific performance constraints
- References existing query performance data

### Scenario 6.2: Caching Strategy
**Context Requirements**: Caching infrastructure, data access patterns, invalidation strategies

**Test Prompt**: "Design a caching strategy for the product catalog."

**Expected Improvements**:
- Uses existing caching infrastructure
- Considers actual data access patterns
- Implements established cache patterns
- Addresses project-specific invalidation needs
- Integrates with existing cache layers

---

## Test Execution Protocol

### Pre-Test Setup
1. **Context Loading**: Load minimal baseline context vs. full generated context
2. **Environment Preparation**: Set up isolated test environment
3. **Baseline Collection**: Record responses with minimal context
4. **Metric Initialization**: Prepare measurement tools and criteria

### During Test Execution
1. **Scenario Execution**: Run identical prompts with both context levels
2. **Response Collection**: Capture complete responses and metadata
3. **Real-time Metrics**: Measure response time and token usage
4. **Quality Assessment**: Apply immediate quality scoring

### Post-Test Analysis
1. **Comparative Analysis**: Compare baseline vs. enhanced responses
2. **Metric Calculation**: Compute all effectiveness metrics
3. **Gap Analysis**: Identify areas where context didn't improve outcomes
4. **Recommendation Generation**: Suggest context improvements

### Success Criteria per Scenario
- **Measurable Improvement**: At least 40% improvement in response quality
- **Accuracy Increase**: 25% or greater increase in technical accuracy
- **Relevance Score**: 80%+ project-specific relevance
- **User Satisfaction**: 4.0+ rating on response usefulness
- **Token Efficiency**: Improvement per additional token >= 5.0

### Test Result Documentation
Each test scenario must document:
- **Baseline Response Quality Score**: 0-100 scale
- **Enhanced Response Quality Score**: 0-100 scale
- **Improvement Percentage**: (Enhanced - Baseline) / Baseline * 100
- **Context Utilization**: Percentage of context actually referenced
- **Token Impact**: Additional tokens used vs. quality improvement
- **Failure Modes**: Ways context failed to improve responses
- **Optimization Opportunities**: Specific context improvements identified

### Continuous Improvement Integration
- **Failed Tests**: Immediately generate context improvement tasks
- **Low-Impact Areas**: Identify context sections with minimal utilization
- **High-Value Patterns**: Recognize context patterns with maximum impact
- **User Feedback**: Incorporate real user satisfaction data
- **Performance Trends**: Track metric improvements over time