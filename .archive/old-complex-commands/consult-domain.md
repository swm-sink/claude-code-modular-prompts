---
name: /consult-domain
description: Business domain and workflow exploration consultation focusing on terminology, user journeys, and domain intelligence
usage: "/consult-domain [quick|standard|comprehensive] [resume]"
allowed-tools: [Read, Write, Edit, Bash, Grep, Glob, LS, TodoWrite]
category: consultation
version: "1.0"
---

# Domain Intelligence Consultation: Business Context & Workflow Discovery

## Purpose
This command provides focused business domain consultation (7-10 minutes) that extracts deep understanding of your project's business domain, terminology, user workflows, and domain-specific patterns. Designed as both a standalone consultation and Stage 3 of the full consultation flow.

## 🎯 What This Consultation Discovers

**Business Domain Intelligence:**
- Industry context and domain-specific terminology
- Core business entities, relationships, and data models
- Business rules, constraints, and compliance requirements
- Domain expertise areas and specialized knowledge needs

**User Journey Mapping:**
- Primary user personas and their workflow patterns
- Critical user journeys and interaction flows
- Pain points, optimization opportunities, and success metrics
- User experience patterns and interface conventions

**Data & Integration Patterns:**
- Core data entities and their relationships
- External integrations, APIs, and service dependencies
- Data flow patterns and business process automation
- Reporting, analytics, and business intelligence needs

## 📋 Consultation Process

### Phase 1: Domain Context Discovery (2-3 minutes)
**Industry & Business Model Analysis:**
- Business domain identification (e-commerce, fintech, healthcare, etc.)
- Target market and customer segments
- Business model patterns (SaaS, marketplace, content, etc.)
- Regulatory or compliance considerations

**Intelligent Domain Questioning:**
- "I see payment processing code. Are you building for B2B, B2C, or both?"
- "Healthcare terminology in your models suggests HIPAA considerations. What's your compliance scope?"
- "E-commerce patterns detected. Are you handling inventory, orders, or payments directly?"

### Phase 2: Business Entity & Workflow Exploration (3-4 minutes)
**Core Business Logic Understanding:**
- Primary business entities (users, products, orders, projects, etc.)
- Entity relationships and business rule constraints
- Workflow patterns and business process flows
- State management and status transitions

**Adaptive Business Rule Discovery:**
- For E-commerce: "What's your product catalog structure? Do you handle variants, bundles, or subscriptions?"
- For Project Management: "How do you track project progress? Are there approval workflows or milestone gates?"
- For SaaS: "What's your user onboarding flow? Do you have different tiers or feature access patterns?"

### Phase 3: User Experience & Integration Context (2-3 minutes)
**User Journey Intelligence:**
- Primary user flows and success paths
- User types and permission/access patterns
- Key user actions and decision points
- User experience optimization priorities

**Integration & Data Context:**
- External service integrations (payments, email, analytics, etc.)
- Data import/export requirements and formats
- Reporting and analytics requirements
- Third-party API dependencies and patterns

## 🚀 Three Consultation Modes

### Quick Mode (5-7 minutes)
**Essential Domain Understanding:**
- Core business domain and primary use case
- Key business entities and basic relationships
- Primary user workflow and main success path
- Critical integrations or compliance requirements

### Standard Mode (7-10 minutes) - Default
**Comprehensive Domain Profile:**
- Complete business context with industry specifics
- Full entity relationship mapping and business rules
- Multiple user journeys and workflow patterns
- Integration patterns and data flow understanding

### Comprehensive Mode (10-15 minutes)
**Deep Domain Consultation:**
- Advanced business rule exploration and edge cases
- Complex workflow analysis and optimization opportunities
- Detailed compliance and regulatory requirement discussion
- Long-term domain evolution and scaling considerations

## 🔄 Session Management Integration

### Pause/Resume Support
- Save domain discovery progress with `/manage-session-state pause`
- Resume domain consultation with `/consult-domain resume`
- Session state preserved in `.claude/consultation-state.json`
- Full context restoration including business understanding and user responses

### Integration with Full Consultation
- Can be run standalone or as part of `/begin-consultation`
- Domain findings inform technical decisions and context generation
- Business context influences code suggestions and architectural recommendations
- Progress tracked within overall consultation workflow

### User Control Throughout Process
- **Navigation**: `skip`, `back`, `skip section` commands available
- **Pace Control**: Switch between quick/standard/comprehensive modes mid-session
- **Clarification**: `clarify`, `example`, `more detail` for deeper business understanding
- **Validation**: `review`, `summary` to confirm domain understanding

## 💡 Interactive Dialogue Examples

### Business Domain Discovery Dialogue:
```
🏢 Domain Intelligence: Business Context Discovery

I've analyzed your codebase and found business-related patterns:
- User authentication and role management
- Payment processing integration (Stripe)
- Email notification system
- Order/invoice generation

Let me understand your specific business domain:

1. Business Model: Are you building a SaaS platform, e-commerce site, or 
   marketplace? What's your primary revenue model?

2. Target Users: Who are your primary users? Are they businesses, consumers, 
   or internal teams? What's their technical expertise level?

3. Core Value Proposition: What's the main problem you're solving? What 
   success looks like for your users?

[User provides domain-specific context that builds business understanding]
```

### Business Entity Exploration:
```
📊 Business Logic Analysis

Based on your database models and API endpoints, I can see:
- User management with roles/permissions
- Product or service catalog structure
- Transaction/order processing workflow
- Notification and communication system

Let's map your business logic:

1. Core Entities: What are your main business objects? How do they relate 
   to each other? (e.g., Users → Orders → Products → Inventory)

2. Business Rules: What are the key constraints? (e.g., "Orders can't be 
   cancelled after shipping", "Users need approval for premium features")

3. Workflow States: What are the key status transitions? (e.g., 
   draft → review → approved → published for content workflows)

[Dialogue adapts based on detected business patterns and domain type]
```

### User Journey Mapping:
```
👥 User Experience Flow Analysis

I want to understand your users' journey through your application:

1. User Onboarding: How do new users get started? Is there a setup process,
   tutorial, or guided first-time experience?

2. Primary Actions: What are the 3-5 most important things users do in your
   application? What does a "successful session" look like?

3. User Types: Do you have different user types with different permissions
   or workflows? (Admin, regular user, guest, etc.)

4. Success Metrics: How do you measure user success? What indicates that
   users are getting value from your platform?

[Builds understanding of user patterns that inform UX-aware code suggestions]
```

## 🎯 Domain Understanding Output

### Generated Domain Context Files
After consultation completion, you'll have:

**Business Domain Context** (`.claude/context/business-domain.md`):
- Complete industry context and domain-specific terminology
- Business model understanding and revenue patterns
- Regulatory/compliance requirements and constraints
- Domain expertise areas and specialized knowledge

**Business Logic Context** (`.claude/context/business-logic.md`):
- Core business entities and their relationships
- Business rules, constraints, and validation patterns
- Workflow states and transition logic
- Data integrity and business process flows

**User Journey Context** (`.claude/context/user-experience.md`):
- Primary user personas and their workflow patterns
- Critical user journeys and success paths
- User experience optimization opportunities
- Interface patterns and user interaction conventions

**Integration Context** (`.claude/context/integrations.md`):
- External service dependencies and API patterns
- Data import/export requirements and formats
- Third-party integration patterns and error handling
- Business intelligence and reporting requirements

### Enhanced CLAUDE.md Integration
Domain findings automatically enhance your project memory with:
- Domain-specific terminology for accurate communication
- Business context for appropriate solution suggestions
- User journey awareness for UX-conscious recommendations
- Business rule understanding for compliant code suggestions

## 🔧 Usage Examples

```bash
# Start focused domain consultation
/consult-domain

# Quick business overview (5-7 minutes)
/consult-domain quick

# Comprehensive domain deep dive
/consult-domain comprehensive

# Resume paused domain consultation
/consult-domain resume

# Use within full consultation flow
/begin-consultation stage-3  # Equivalent to /consult-domain standard
```

## 🤖 Specialized Agent Integration

This consultation leverages specialized domain analysis agents:

**Business Context Agent**: Analyzes industry patterns and domain terminology
**Entity Relationship Agent**: Maps business logic and data model patterns
**User Journey Agent**: Identifies user workflow and experience patterns  
**Integration Analysis Agent**: Maps external dependencies and data flows

Agents collaborate to build comprehensive business understanding that enables domain-aware code suggestions and business-conscious technical recommendations.

## 🎯 Success Outcomes

After domain consultation, Claude will:
- **Speak your business language**: Use domain-specific terminology and concepts
- **Understand your users**: Consider user experience in technical recommendations
- **Respect business rules**: Factor business constraints into code suggestions
- **Consider workflow context**: Align technical solutions with business processes

**Result**: Claude becomes a business-aware technical expert who understands not just HOW to code, but WHAT the business needs and WHY.

## 💼 Domain-Specific Examples

### E-Commerce Domain Understanding:
```
After domain consultation, Claude will understand:
- "Inventory" vs "Stock" terminology preferences
- Cart abandonment vs checkout conversion optimization
- Payment processing vs billing cycle patterns
- Product catalog vs variant management approaches
- Order fulfillment vs shipping integration workflows
```

### SaaS Platform Domain Understanding:
```
After domain consultation, Claude will understand:
- User onboarding vs customer activation patterns
- Feature flag vs plan tier access control
- Usage analytics vs billing integration patterns
- Customer support vs user success workflows
- Multi-tenancy vs single-tenant architectural decisions
```

### Healthcare Domain Understanding:
```
After domain consultation, Claude will understand:
- Patient vs client terminology and privacy implications
- HIPAA compliance vs general security requirements
- Clinical workflow vs administrative process patterns
- Integration vs interoperability with healthcare systems
- Audit trail vs logging requirements for compliance
```

## Next Steps

1. **Test business understanding**: Ask Claude domain-specific questions
2. **Continue to workflow consultation**: Run `/consult-workflow` for team patterns
3. **Complete full consultation**: Use `/begin-consultation` for comprehensive setup
4. **Refine domain context**: Use `/update-context domain` for adjustments

**Time Investment**: 7-10 minutes for business intelligence that makes every technical recommendation contextually appropriate and business-conscious.