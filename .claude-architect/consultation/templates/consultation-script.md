# Master Consultation Script Template
# Complete 20-30 minute interactive discovery conversation flow
# Purpose: Transform consultation architecture into executable conversation

## Consultation Opening & Welcome (2 minutes)

### Initial Context Setting
```
🎯 **Welcome to Claude Context Architect Deep Discovery**

Hi! I'm excited to help transform Claude into YOUR project expert through 
a comprehensive understanding of your specific project. This will be a 
20-30 minute conversation where we'll explore:

1. **Your Project** - What makes it unique and valuable
2. **Technical Architecture** - How it's built and organized  
3. **Business Domain** - The knowledge and terminology that matters
4. **Team Preferences** - How your team likes to work

You'll see immediate value as we build understanding together, and at the 
end, you'll have a completely personalized Claude setup that speaks your 
language and understands your patterns.

**You're in complete control:**
- Say "skip" to move past any question
- Say "pause" if you need to step away  
- Say "back" to revise or add to previous answers
- Say "quick mode" for essential questions only
- Say "deep mode" for comprehensive exploration

Ready to dive in and discover your project together?
```

### User Control Orientation
```
**Quick Reference - You can say anytime:**
- `skip` - Next question
- `back` - Previous question  
- `pause` - Save and pause
- `quick mode` - Essential only
- `deep mode` - Full exploration
- `review` - Check understanding

**Time Expectation:** 20-30 minutes total, broken into 4 natural stages
**Your Benefit:** Claude that truly understands YOUR specific project

Let's start! 🚀
```

## Stage 1: Project Discovery Script (5-7 minutes)

### Opening Transition
```
## 🔍 **Stage 1: Project Discovery** (5-7 minutes)

Let's start by understanding what makes your project unique and special. 
This foundation helps me ask the right technical and business questions in 
the next stages.
```

### Core Question Flow
```
**Q1: Project Essence**
"Tell me about your project - what are you building and what problem does it solve?"

[Listen for: Project type, purpose, value proposition]
[Adaptive follow-ups based on response clarity]
[If unclear]: "Could you give me a specific example of how someone would use this?"
[If too technical]: "Who benefits from this - what's the human impact?"

**Understanding Check**: "So you're building [SUMMARY] that [VALUE]. Is that right?"

---

**Q2: Scale and Context**  
"What's the current size and stage? Are we talking about something brand new, 
actively growing, or more established?"

[Listen for: Project maturity, development stage]
[Follow-up]: "How many people are actively working on this?"
[If team size unclear]: "Are you flying solo, small team, or larger group?"

**Understanding Check**: "Got it - [STAGE] project with [TEAM_SIZE], complexity level seems [COMPLEXITY]."

---

**Q3: Goals and Challenges**
"What's working well right now, and what's the biggest challenge or pain point 
you're facing?"

[Listen for: Current state, problems, motivations]
[Follow-up]: "What brought you to want better Claude integration? What are you hoping Claude can help with?"
[Future focus]: "If this Claude setup is working perfectly in 6 months, what would that look like?"

**Understanding Check**: "Main goal is [PRIMARY_GOAL], success looks like [SUCCESS_VISION], 
biggest challenge is [CHALLENGE]. Accurate?"
```

### Stage 1 Validation & Transition
```
## 📋 **Stage 1 Summary**
"Let me confirm what I understand about your project:

- **Project Type**: [TYPE] - [DESCRIPTION]
- **Team**: [SIZE] people at [STAGE] stage  
- **Domain**: [DOMAIN/INDUSTRY]
- **Main Goal**: [PRIMARY_GOAL]
- **Current Challenge**: [MAIN_CHALLENGE]

Does this capture the essence of what we're working with?"

[Allow corrections/additions]

**Transition**: "Perfect! Now let's dive into the technical architecture so I 
can understand how your code is structured. This takes about 7-10 minutes."
```

## Stage 2: Technical Deep Dive Script (7-10 minutes)

### Opening Transition
```
## ⚙️ **Stage 2: Technical Deep Dive** (7-10 minutes)

Now I understand your project context. Let's explore the technical side - 
how your code is organized, what frameworks you're using, and how you develop 
and deploy. This helps me understand what kind of commands and context will 
be most valuable.

I'll ask about three areas:
1. Architecture and tech stack (3-4 minutes)
2. Development workflow and testing (2-3 minutes)
3. Performance needs and constraints (2-3 minutes)
```

### Technical Question Flow
```
**Q1: Architecture Foundation**
"Let's start with the big picture - how is your application structured? 
Monolith, microservices, or something in between?"

[Listen for: Architecture pattern]
[Follow-up]: "What's your main tech stack - languages, frameworks, database?"

[Adaptive deep dive based on detected stack]
[React detected]: "State management approach? Component organization?"
[Node detected]: "Express/Fastify? API structure? Async patterns?"
[Python detected]: "Django/Flask/FastAPI? Module organization? ORM usage?"

**Understanding Check**: "So [TECH_STACK] in [ARCHITECTURE_PATTERN] structure, 
following [PATTERNS]. Sound right?"

---

**Q2: Development Workflow**
"What's your approach to testing? Unit tests, integration tests, end-to-end, 
or still building that up?"

[Listen for: Testing maturity, frameworks, coverage]
[Follow-up]: "How do you deploy? CI/CD pipeline, manual, or figuring it out?"
[If has CI]: "What's your setup - GitHub Actions, Jenkins, GitLab CI?"
[Tools]: "What development tools are essential - IDE, linters, debuggers?"

**Understanding Check**: "Testing with [TEST_APPROACH], deploying via [DEPLOYMENT], 
using [KEY_TOOLS]. Accurate?"

---

**Q3: Performance and Constraints**
"Any specific performance requirements or constraints? Response times, scalability 
needs, resource limitations?"

[Listen for: Performance needs, scaling challenges, technical debt]
[Follow-up]: "Any technical constraints - legacy integration, compliance, technology restrictions?"
[Monitoring]: "How do you handle errors and monitoring? Logging, error tracking?"

**Understanding Check**: "Performance focus on [PERFORMANCE_PRIORITIES], 
key constraints are [CONSTRAINTS]. Right?"
```

### Stage 2 Validation & Transition
```
## 📋 **Stage 2 Technical Summary**
"Technical landscape summary:

- **Architecture**: [ARCHITECTURE_PATTERN] using [PRIMARY_STACK]
- **Key Technologies**: [TECH_LIST]  
- **Development**: [WORKFLOW_SUMMARY]
- **Testing**: [TESTING_APPROACH]
- **Deployment**: [DEPLOYMENT_APPROACH]
- **Performance Focus**: [PERFORMANCE_PRIORITIES]
- **Constraints**: [MAIN_CONSTRAINTS]

Does this capture your technical setup accurately?"

**Transition**: "Excellent! Next let's explore the business domain - the knowledge, 
terminology, and workflows that make your project unique. About 7-10 minutes."
```

## Stage 3: Domain Extraction Script (7-10 minutes)

### Opening Transition
```
## 🏢 **Stage 3: Domain Extraction** (7-10 minutes)

Now I understand your technical foundation. Let's capture the business knowledge 
that makes your project special - the concepts, terminology, and workflows that 
Claude should understand to truly help you.

This helps Claude speak your domain language instead of giving generic responses.

Three areas to explore:
1. Core business concepts and terminology (3-4 minutes)
2. Key workflows and user journeys (2-3 minutes)  
3. Data relationships and integrations (2-3 minutes)
```

### Domain Question Flow
```
**Q1: Business Concepts**
"What are the main 'things' your system works with? The core business entities 
that everything revolves around?"

[Provide examples]: "Like e-commerce works with Products, Orders, Customers. 
Healthcare works with Patients, Providers, Appointments. What are yours?"

[Listen for: Core entities, business concepts]
[Follow-up]: "Any specific terminology important in your domain? Industry jargon, 
company terms, or concepts with particular meaning?"
[Business rules]: "What are the most important business rules - the 'if this, then that' 
logic that governs how your system behaves?"

**Understanding Check**: "Core entities are [ENTITIES], key terminology includes [TERMS], 
main business rules are [RULES]. Correct?"

---

**Q2: User Workflows**
"What are the main things people do in your system? Walk me through the 2-3 most 
common or important user workflows."

[Listen for: Primary user journeys, admin workflows, system processes]
[Follow-up]: "Which workflows are most complex or error-prone? Where do people get stuck?"
[Process focus]: "Any important background processes or automated workflows?"

**Understanding Check**: "Key workflows: [USER_WORKFLOW], [ADMIN_WORKFLOW], [COMPLEX_WORKFLOW]. 
Captures the main pathways?"

---

**Q3: Data and Integrations**
"How do your main business entities relate to each other? Important connections 
and dependencies?"

[Listen for: Data relationships, entity connections]
[Follow-up]: "What external systems do you integrate with? Payment processors, 
APIs, third-party services?"
[Data flow]: "How does data flow through your system? Where does it come from, 
how is it processed, where does it go?"

**Understanding Check**: "Data relationships: [RELATIONSHIPS], integrations: [INTEGRATIONS], 
data flow: [DATA_FLOW]. Sound right?"
```

### Stage 3 Validation & Transition
```
## 📋 **Stage 3 Domain Summary**
"Business domain synthesis:

- **Core Entities**: [ENTITY_LIST]
- **Key Terminology**: [TERMINOLOGY_LIST]
- **Primary Workflows**: [WORKFLOW_LIST]
- **Business Rules**: [BUSINESS_RULES]
- **Integrations**: [INTEGRATION_LIST]
- **Data Patterns**: [DATA_PATTERNS]

Does this capture your domain essence?"

**Transition**: "Perfect! Final stage is quick - understanding your team's preferences 
and working style. About 3-5 minutes to make sure Claude matches your team's way of working."
```

## Stage 4: Preference Learning Script (3-5 minutes)

### Opening Transition
```
## 👥 **Stage 4: Preference Learning** (3-5 minutes)

Almost done! Now I understand your project, technical setup, and business domain. 
The final piece is making sure Claude works the way your team works.

Quick exploration of:
1. Coding standards and style (1-2 minutes)
2. Documentation and communication preferences (1-2 minutes)
3. Tool preferences and workflow habits (1-2 minutes)
```

### Preference Question Flow
```
**Q1: Coding Standards**
"Do you follow specific coding standards or style guidelines? Company standards, 
open source guides, or your own conventions?"

[Listen for: Style guide existence, conventions, quality priorities]
[Framework specific]: [Adapt based on detected stack - React/Node/Python/Java patterns]
[Priorities]: "What matters most - readability, performance, maintainability, or consistency?"

**Understanding Check**: "Coding approach: [STANDARDS_SUMMARY], priorities: [QUALITY_PRIORITIES]. Right?"

---

**Q2: Documentation and Communication**
"How detailed should code comments be? Comprehensive documentation, minimal comments, 
or somewhere in between?"

[Listen for: Comment style, explanation depth, documentation format]
[Follow-up]: "When Claude explains solutions, how much detail do you want? Brief, 
step-by-step, or contextual based on complexity?"
[Tone]: "What communication style works best? Formal/structured, conversational/friendly, 
or technical/precise?"

**Understanding Check**: "Documentation level: [DOC_STYLE], explanation depth: [EXPLANATION_LEVEL], 
communication: [COMMUNICATION_STYLE]. Accurate?"

---

**Q3: Tools and Workflow**
"What development tools are essential to your workflow? Any tools Claude should be aware of?"

[Listen for: IDE preferences, essential tools, workflow integration]
[Commands]: "For Claude commands, prefer short/quick, descriptive/self-documenting, 
or flexible with options?"
[Feedback]: "How do you prefer suggestions? Direct answers, options with pros/cons, 
step-by-step guidance, or context and reasoning?"

**Understanding Check**: "Tool focus: [TOOL_PREFERENCES], command style: [COMMAND_STYLE], 
feedback approach: [FEEDBACK_STYLE]. Sound right?"
```

### Stage 4 Validation & Complete Synthesis
```
## 📋 **Stage 4 Preferences Summary**
"Team working style:

- **Standards**: [STANDARDS_SUMMARY] 
- **Documentation**: [DOCUMENTATION_STYLE]
- **Communication**: [COMMUNICATION_PREFERENCES]
- **Commands**: [COMMAND_STYLE]
- **Tools**: [TOOL_PREFERENCES]

Captures how your team likes to work?"
```

## Complete Consultation Synthesis (3-5 minutes)

### Comprehensive Understanding Summary
```
## 🎯 **Complete Project Understanding**

Excellent! Here's everything I've learned about your project:

### **PROJECT FOUNDATION**
- **Type**: [PROJECT_TYPE]
- **Domain**: [DOMAIN_AREA] 
- **Team**: [TEAM_SIZE] at [PROJECT_STAGE] stage
- **Goals**: [PRIMARY_GOALS]

### **TECHNICAL ARCHITECTURE**  
- **Stack**: [TECH_STACK]
- **Architecture**: [ARCHITECTURE_PATTERN]
- **Development**: [WORKFLOW_SUMMARY]
- **Constraints**: [KEY_CONSTRAINTS]

### **BUSINESS DOMAIN**
- **Entities**: [CORE_ENTITIES]
- **Workflows**: [KEY_WORKFLOWS] 
- **Terminology**: [DOMAIN_TERMS]
- **Integrations**: [EXTERNAL_SYSTEMS]

### **TEAM PREFERENCES**
- **Style**: [CODING_STANDARDS]
- **Communication**: [COMMUNICATION_STYLE]
- **Documentation**: [DOCUMENTATION_LEVEL]
- **Tools**: [TOOL_PREFERENCES]

**Is this an accurate and complete picture of your project?**
[Allow final adjustments and confirmations]
```

### Generation Preparation & Next Steps
```
## 🚀 **Ready for Context Generation!**

This gives me everything I need to create a comprehensive Claude setup 
specifically tailored to YOUR project. I'll generate:

✅ **Multi-file context system** that makes Claude your project expert
✅ **Specialized agents** for your specific domain and technical needs
✅ **Custom commands** that match your workflows and preferences  
✅ **Documentation** that fits your team's style and standards

**Next Steps:**
1. I'll use this understanding to generate your personalized context architecture
2. Create specialized agents that understand your domain and technical patterns
3. Build custom commands optimized for your workflow and preferences
4. Validate everything works together and improves Claude's responses

**Total time invested:** [ACTUAL_TIME] minutes
**Value created:** Claude that truly understands and works with YOUR specific project

Ready to see your personalized Claude Context architecture come to life?
```

## Script Usage Guidelines

### Adaptive Application
- **Use as framework, not rigid script** - Adapt based on user responses and engagement
- **Follow user cues** - If they want to explore something deeper, follow that thread
- **Respect time preferences** - If they indicate time pressure, switch to quick mode
- **Maintain conversational flow** - Don't make it feel like an interrogation

### Quality Checkpoints
- **Validate understanding** at each stage transition
- **Confirm accuracy** before moving forward
- **Ask for clarification** when responses are unclear
- **Offer examples** when concepts seem confusing

### User Control Integration
- **Monitor for control commands** throughout the conversation
- **Respect pace preferences** and adjust accordingly
- **Enable easy navigation** between stages and questions
- **Provide clear progress indicators** so users know where they are

This script template provides the structure for conducting effective 20-30 minute consultations that build comprehensive understanding while maintaining user engagement and control.