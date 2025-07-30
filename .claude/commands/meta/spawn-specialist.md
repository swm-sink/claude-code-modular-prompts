---
name: /spawn-specialist
description: "Create and launch specialized sub-agents for complex multi-domain tasks"
usage: /spawn-specialist <domain> <task-description> [--parallel] [--coordinated]
category: meta-commands
tools: Task, Read, Write, Edit, Bash, Glob, Grep
---

# Specialized Sub-Agent Spawning System

**Launch domain-specific sub-agents to handle complex tasks requiring specialized expertise.**

## How This Works (ADAPTIVE AUTOMATION WITH USER INPUT)

Interactive Meta-Prompting Cycle:
1. **Analyze your task** and suggest specialist combinations with reasoning
2. **Get your feedback** on specialist selection and priorities  
3. **Launch coordinated sub-agents** with dynamic workflow adaptation
4. **Request user input** at key decision points during execution
5. **Learn from your feedback** to improve future specialist recommendations
6. **Aggregate results** with user validation at each major milestone

## Available Specialist Domains

### Code Architecture Specialist
```
/spawn-specialist architecture "redesign authentication system for microservices"
```
- System design and architectural patterns
- Performance optimization and scalability
- Security architecture and threat modeling
- Integration patterns and API design

### Testing & Quality Specialist  
```
/spawn-specialist testing "create comprehensive test suite for React app"
```
- Unit, integration, and end-to-end testing
- Test automation and CI/CD integration
- Code coverage analysis and quality metrics
- Performance testing and benchmarking

### DevOps & Infrastructure Specialist
```
/spawn-specialist devops "set up production deployment pipeline"
```
- Container orchestration and Docker
- CI/CD pipeline design and implementation
- Cloud infrastructure and monitoring
- Security hardening and compliance

### Frontend Development Specialist
```
/spawn-specialist frontend "optimize React app performance and UX"
```
- React, Vue, Angular specialized knowledge
- Performance optimization and bundle analysis
- UI/UX best practices and accessibility
- Modern frontend tooling and workflows

### Backend API Specialist
```
/spawn-specialist backend "design scalable REST API with authentication"
```
- RESTful and GraphQL API design
- Database design and optimization
- Authentication and authorization systems
- Microservices and distributed systems

### Database & Data Specialist
```
/spawn-specialist database "optimize PostgreSQL queries and design schema"
```
- Database design and normalization
- Query optimization and performance tuning
- Data migration and ETL processes
- NoSQL and caching strategies

## Interactive Meta-Prompting Cycle (5 KEY IMPROVEMENTS)

### 1. Interactive User Feedback Loops
```
🤖 I suggest launching Architecture + Security specialists for this task.
   Architecture: System design and scalability patterns
   Security: Authentication and threat modeling
   
👤 Actually, I'm more concerned about performance than security right now.

🤖 Adjusting specialist selection:
   Architecture: Focus on performance-oriented design patterns
   Performance: Database optimization and caching strategies
   
   Proceeding with performance-focused approach...
```

### 2. Self-Improving Meta-Prompts
```javascript
// System learns from successful patterns
const learnedPatterns = {
  "React + performance issues": {
    bestSpecialists: ["frontend", "performance"],
    successfulPrompts: ["focus on bundle size", "prioritize Core Web Vitals"],
    userSatisfaction: 4.8/5
  }
}

// Automatically improves prompts for similar future tasks
```

### 3. Dynamic Workflow Adaptation
```
Initial Plan: Architecture → Backend → Testing
User Feedback: "Backend implementation revealed architecture flaws"
Adapted Plan: Architecture → Revised Architecture → Backend → Testing

🔄 Workflow automatically adjusted based on intermediate results
```

### 4. User Satisfaction Learning
```yaml
session_learning:
  user_preferences:
    - "Prefers detailed explanations over quick summaries"
    - "Values security considerations highly"
    - "Likes to validate major decisions before proceeding"
  
  successful_combinations:
    - specialists: ["architecture", "security"]
      satisfaction: 4.9/5
      context: "API design projects"
```

### 5. Smart Context Caching
```
🔍 Found similar work from previous session:
   "React authentication system" (3 days ago, 4.7/5 rating)
   
💡 Reusing validated patterns:
   ✅ JWT implementation approach (Architecture specialist)
   ✅ React Context patterns (Frontend specialist)  
   ✅ Security testing checklist (Testing specialist)
   
⚡ Estimated time saved: 40 minutes
```

## Sub-Agent Coordination Patterns

### Parallel Execution
```
/spawn-specialist frontend "optimize component performance" --parallel
/spawn-specialist backend "optimize API response times" --parallel
```
Both agents work simultaneously on related but independent tasks.

### Coordinated Workflow
```
/spawn-specialist architecture "design system structure" --coordinated
```
Sequential execution where later agents build on earlier work:
1. Architecture specialist designs system
2. Backend specialist implements APIs based on architecture
3. Frontend specialist creates UI based on API contracts
4. Testing specialist validates entire system

### Multi-Domain Collaboration
```
/spawn-specialist "security,performance,testing" "audit and optimize entire application"
```
Multiple specialists collaborate on a single complex problem.

## Agent Specialization Profiles

### Architecture Specialist Capabilities
- **Design Patterns**: Factory, Observer, Strategy, MVC, MVVM
- **Architectural Styles**: Microservices, Serverless, Event-driven
- **Scalability**: Load balancing, caching, database sharding
- **Integration**: API gateways, message queues, webhooks

### Testing Specialist Capabilities
- **Testing Frameworks**: Jest, Mocha, pytest, JUnit, Cypress
- **Testing Types**: Unit, integration, e2e, performance, security
- **Test Automation**: CI/CD integration, automated reporting
- **Quality Metrics**: Coverage analysis, mutation testing

### DevOps Specialist Capabilities
- **Containerization**: Docker, Kubernetes, container optimization
- **CI/CD**: GitHub Actions, Jenkins, GitLab CI, deployment strategies
- **Infrastructure**: AWS, Azure, GCP, Terraform, monitoring
- **Security**: Secret management, compliance, vulnerability scanning

## Example Multi-Agent Session

```
👤 /spawn-specialist "architecture,backend,testing" "build user management system with auth"

🤖 Launching specialized sub-agents...

🏗️ Architecture Specialist:
   ✅ Designed microservices architecture for user management
   ✅ Planned JWT-based authentication with refresh tokens
   ✅ Specified API contracts and data models
   📄 Generated system design document

⚙️ Backend Specialist:
   ✅ Implemented user registration and login endpoints
   ✅ Added JWT middleware and token management
   ✅ Created PostgreSQL schema with proper indexing
   ✅ Added rate limiting and input validation

🧪 Testing Specialist:
   ✅ Created unit tests for all endpoints (95% coverage)
   ✅ Added integration tests for auth flow
   ✅ Set up automated security testing
   ✅ Configured CI/CD pipeline with test automation

🎯 Coordination Summary:
   - All agents worked from shared architecture specification
   - Backend implementation follows architectural contracts
   - Tests validate both individual components and system integration
   - Complete user management system ready for deployment
```

## Agent Communication Protocol

### Shared Context Management
Each specialist maintains and updates shared context:
```yaml
shared_context:
  project_requirements: "Original task specification"
  architecture_decisions: "Architectural choices and constraints"
  implementation_status: "Current progress and blockers"
  quality_metrics: "Test results and performance data"
```

### Cross-Agent Validation
Specialists validate each other's work:
- Architecture reviews implementation for pattern compliance
- Testing validates architectural decisions through integration tests
- DevOps validates deployment feasibility of architectural choices

## Quality Assurance Integration

### Multi-Perspective Validation
Each specialist reviews work from their domain perspective:
- **Security**: Authentication, authorization, data protection
- **Performance**: Scalability, optimization, resource usage
- **Maintainability**: Code quality, documentation, testability
- **Reliability**: Error handling, monitoring, recovery procedures

### Automated Quality Gates
Before completion, all outputs are validated:
```javascript
// Quality validation pipeline
const qualityChecks = [
  architectureCompliance(),
  securityValidation(),
  performanceBaseline(),
  testCoverage(),
  documentationCompleteness()
];
```

## Advanced Coordination Features

### Dynamic Agent Spawning  
```
/spawn-specialist "detect-needed-specialists" "complex enterprise migration project"
```
System analyzes requirements and automatically determines which specialists are needed.

### Learning from Collaboration
Agents learn from each other:
- Architecture patterns that work well with specific tech stacks
- Testing strategies that catch common implementation issues
- DevOps configurations that support specific architectural choices

### Result Synthesis
Final output combines all specialist perspectives:
- Complete implementation with architecture documentation
- Comprehensive test suite with quality metrics
- Deployment-ready configuration with monitoring
- Team onboarding guide with specialist insights

---

## Ready for Specialized Expertise?

Launch domain experts who bring deep knowledge and coordinated teamwork to complex development challenges.

**Example**: `/spawn-specialist "architecture,security" "design secure microservices authentication system"`