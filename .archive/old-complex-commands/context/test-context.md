---
name: test-context
description: Run comprehensive context validation tests to measure context effectiveness and quality
usage: "test-context [baseline|enhanced|compare|report] [--domain|--technical|--workflow|--agents]"
allowed-tools: [Read, Write, Edit, LS, Glob, Grep, Bash, TodoWrite]
category: context
version: "1.0"
---

# Test Context: Context Effectiveness Validation Framework

## Purpose: Measure & Validate Context Quality

The `/test-context` command provides comprehensive testing to measure how effectively your generated context improves Claude's understanding of your project. Through systematic before/after comparisons, domain-specific testing, and quality metrics, it proves that context engineering delivers measurable value.

**Testing Philosophy**: Evidence over assumption, measurement over opinion, systematic over ad-hoc, actionable over academic.

## 🧪 Context Testing Framework

### Baseline Testing Mode
**Usage**: `/test-context baseline`

Establishes baseline Claude performance without project-specific context:

```
Baseline Test Suite:
├── Domain Knowledge Test (10 questions)
│   ├── "What is the primary business domain?"
│   ├── "What are the key user workflows?"
│   ├── "What terminology is specific to this project?"
│   └── "What are the main data entities?"
│
├── Technical Architecture Test (10 questions)
│   ├── "What frameworks are used in this project?"
│   ├── "How is the project structured?"
│   ├── "What are the deployment patterns?"
│   └── "What testing strategies are employed?"
│
├── Workflow Process Test (10 questions)
│   ├── "What is the development workflow?"
│   ├── "How are code reviews conducted?"
│   ├── "What are common troubleshooting steps?"
│   └── "How do new team members get onboarded?"
│
└── Code Understanding Test (10 questions)
    ├── File location questions
    ├── Pattern recognition questions
    ├── Best practice questions
    └── Project-specific convention questions
```

**Output**: Baseline scores and response quality assessment saved to `.claude/context/test-results/baseline-YYYY-MM-DD.json`

### Enhanced Testing Mode
**Usage**: `/test-context enhanced`

Tests Claude performance WITH full project context loaded:

```
Enhanced Test Suite (Same Questions):
├── All 40 questions from baseline test
├── Context-informed responses expected
├── Project-specific terminology usage
├── Accurate technical details
├── Workflow-aware recommendations
└── Domain-appropriate suggestions
```

**Integration**: Automatically loads all context layers:
- Foundation context (CLAUDE.md)
- Domain context (business rules, workflows, terminology)
- Technical context (architecture, frameworks, deployment)
- Workflow context (development, review, troubleshooting)
- Agent context (specialized knowledge)

### Comparison Testing Mode
**Usage**: `/test-context compare [--detailed|--summary|--export]`

Direct before/after comparison with quantitative metrics:

```
Context Effectiveness Report:
┌─────────────────────┬──────────┬──────────┬──────────────┐
│ Test Category       │ Baseline │ Enhanced │ Improvement  │
├─────────────────────┼──────────┼──────────┼──────────────┤
│ Domain Knowledge    │ 3.2/10   │ 8.7/10   │ +171%        │
│ Technical Accuracy  │ 4.1/10   │ 9.2/10   │ +124%        │
│ Workflow Awareness  │ 2.8/10   │ 8.9/10   │ +218%        │
│ Code Understanding  │ 3.9/10   │ 8.4/10   │ +115%        │
├─────────────────────┼──────────┼──────────┼──────────────┤
│ Overall Score       │ 3.5/10   │ 8.8/10   │ +151%        │
└─────────────────────┴──────────┴──────────┴──────────────┘

Response Quality Metrics:
├── Specificity: Generic → Project-specific
├── Accuracy: Assumptions → Factual knowledge
├── Relevance: Broad advice → Targeted guidance
├── Terminology: Generic terms → Project vocabulary
└── Actionability: Vague suggestions → Specific steps
```

### Automated Report Generation
**Usage**: `/test-context report [--weekly|--monthly|--trends]`

Comprehensive context effectiveness reports with trends and insights:

```
Context Health Report - Week of [Date]
=====================================

Executive Summary:
├── Context Effectiveness: 8.8/10 (Excellent)
├── Response Quality: 91% project-specific
├── User Satisfaction: 4.7/5 stars
└── Recommendation: Minor optimization in technical layer

Detailed Metrics:
├── Domain Context Performance: 9.1/10
│   ├── Business rule understanding: Excellent
│   ├── User workflow recognition: Excellent
│   ├── Terminology usage: Very Good
│   └── Data model comprehension: Excellent
│
├── Technical Context Performance: 8.9/10
│   ├── Framework knowledge: Excellent
│   ├── Architecture understanding: Excellent
│   ├── Deployment awareness: Good (improvement opportunity)
│   └── Testing strategy alignment: Very Good
│
├── Workflow Context Performance: 8.4/10
│   ├── Development process adherence: Very Good
│   ├── Code review integration: Good
│   ├── Troubleshooting effectiveness: Excellent
│   └── Onboarding guidance: Very Good
│
└── Agent Context Performance: 9.0/10
    ├── Domain expert responses: Excellent
    ├── Architect recommendations: Excellent
    ├── Review assistant accuracy: Very Good
    └── Debug specialist effectiveness: Excellent

Improvement Recommendations:
1. Enhance deployment context with more infrastructure details
2. Update code review workflows with recent team changes
3. Add more troubleshooting scenarios for edge cases
4. Consider creating specialized security expert agent
```

## 🎯 Specialized Context Testing

### Domain-Specific Testing
**Usage**: `/test-context --domain`

Focused testing of domain knowledge and business logic understanding:

```
Domain Test Categories:
├── Business Logic Tests
│   ├── Rule application scenarios
│   ├── Edge case handling
│   ├── Business process flow
│   └── Domain constraint validation
│
├── User Experience Tests
│   ├── User journey understanding
│   ├── Workflow optimization
│   ├── Pain point identification
│   └── Feature prioritization
│
├── Data Model Tests
│   ├── Entity relationship understanding
│   ├── Data flow comprehension
│   ├── Schema evolution awareness
│   └── Integration point knowledge
│
└── Terminology Tests
    ├── Domain vocabulary usage
    ├── Acronym expansion
    ├── Context-appropriate language
    └── Stakeholder communication
```

### Technical Testing
**Usage**: `/test-context --technical`

Deep technical architecture and framework knowledge validation:

```
Technical Test Categories:
├── Architecture Tests
│   ├── System design understanding
│   ├── Component interaction knowledge
│   ├── Scalability consideration
│   └── Performance optimization
│
├── Framework Tests
│   ├── Framework-specific patterns
│   ├── Best practice adherence
│   ├── Anti-pattern avoidance
│   └── Version-specific features
│
├── Infrastructure Tests
│   ├── Deployment environment knowledge
│   ├── Configuration management
│   ├── Monitoring and logging
│   └── Security implementation
│
└── Testing Strategy Tests
    ├── Test pyramid adherence
    ├── Coverage expectations
    ├── CI/CD integration
    └── Quality gates
```

### Workflow Testing
**Usage**: `/test-context --workflow`

Team process and development workflow validation:

```
Workflow Test Categories:
├── Development Process Tests
│   ├── Feature development flow
│   ├── Branch management
│   ├── Code review process
│   └── Release management
│
├── Quality Assurance Tests
│   ├── Testing standards
│   ├── Code quality metrics
│   ├── Performance benchmarks
│   └── Security requirements
│
├── Collaboration Tests
│   ├── Team communication
│   ├── Knowledge sharing
│   ├── Decision making
│   └── Conflict resolution
│
└── Maintenance Tests
    ├── Bug triage process
    ├── Technical debt management
    ├── Documentation updates
    └── Dependency management
```

### Agent Specialization Testing
**Usage**: `/test-context --agents`

Validation of specialized agent knowledge and capabilities:

```
Agent Test Categories:
├── Domain Expert Agent Tests
│   ├── Business rule expertise
│   ├── Stakeholder communication
│   ├── Requirements analysis
│   └── Domain modeling
│
├── Technical Architect Agent Tests
│   ├── System design guidance
│   ├── Technology selection
│   ├── Performance optimization
│   └── Scalability planning
│
├── Code Review Agent Tests
│   ├── Code quality assessment
│   ├── Best practice enforcement
│   ├── Security vulnerability detection
│   └── Performance issue identification
│
└── Debug Specialist Agent Tests
    ├── Problem diagnosis
    ├── Root cause analysis
    ├── Solution recommendation
    └── Prevention strategies
```

## 📊 Context Quality Metrics

### Response Quality Scoring
Each test response is scored across multiple dimensions:

```
Scoring Criteria (1-10 scale):
├── Accuracy: Factual correctness of information
├── Specificity: Project-specific vs generic response
├── Completeness: Comprehensive coverage of question
├── Relevance: Appropriateness to project context
├── Actionability: Practical value of recommendations
└── Terminology: Correct use of project vocabulary

Overall Score: Weighted average across all criteria
Quality Band: Excellent (9-10), Very Good (7-8), Good (5-6), Poor (<5)
```

### Context Coverage Analysis
Measures how effectively context files are utilized:

```
Coverage Metrics:
├── File Utilization: % of context files referenced in responses
├── Cross-Reference Usage: How often context links are followed
├── Layer Integration: Balance across context hierarchy layers
├── Information Density: Value derived per token of context
└── Update Recency: How current the context information is
```

### Performance Impact Assessment
Evaluates the cost-benefit of context loading:

```
Performance Metrics:
├── Token Usage: Context tokens vs response quality improvement
├── Response Time: Impact of context loading on speed  
├── Context Freshness: Age of context vs effectiveness
├── Maintenance Overhead: Effort to keep context current
└── User Productivity: Time saved by better responses
```

## 🔧 Test Automation & Integration

### Automated Testing Schedule
Context tests can run automatically to monitor context health:

```bash
# Daily light testing
/test-context baseline --quick --save

# Weekly comprehensive testing  
/test-context enhanced --full --report

# Monthly trend analysis
/test-context report --monthly --trends --export
```

### Continuous Context Validation
Integration with project workflows for ongoing context quality:

```
Integration Points:
├── Git Hooks: Run tests when context files change
├── CI/CD Pipeline: Include context validation in builds
├── Development Workflow: Test before major context updates
├── Team Meetings: Weekly context health reviews
└── Onboarding: New team member context effectiveness testing
```

### Test Result Storage
Structured storage of test results for trend analysis:

```
.claude/context/test-results/
├── baseline/
│   ├── 2024-01-15-baseline.json
│   ├── 2024-01-22-baseline.json
│   └── ...
├── enhanced/
│   ├── 2024-01-15-enhanced.json
│   ├── 2024-01-22-enhanced.json
│   └── ...
├── reports/
│   ├── weekly-2024-W03.json
│   ├── monthly-2024-01.json
│   └── trend-analysis-2024-Q1.json
└── archives/
    └── [older test results]
```

## 🎯 Success Validation

### Context Effectiveness Validation
Proves that context engineering delivers measurable value:

- **Quantitative**: Numerical scores showing improvement percentages
- **Qualitative**: Response quality improvements with specific examples
- **User Validation**: Team member confirmation of response quality
- **Productivity**: Time savings and reduced clarification needs

### Context Health Monitoring
Ongoing validation of context system performance:

- **Freshness**: Context stays current with project evolution
- **Coverage**: All important project aspects have appropriate context
- **Integration**: Context layers work together effectively  
- **Optimization**: Context provides maximum value for token cost

---

**Remember**: Context testing isn't just about proving context works - it's about continuously improving context quality and ensuring the system delivers real value to your development team.