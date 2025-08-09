---
name: test-agents
description: Validate agent effectiveness with project scenarios and performance benchmarks
usage: "test-agents [agent-name|all] [--scenario=type] [--benchmark] [--continuous]"
allowed-tools: [Read, Write, Edit, Bash, Grep, Glob, LS, TodoWrite]
category: agents
argument-hint: "[agent-name|all] [--test-options]"
version: "1.0"
---

# Test Agents: Validate Specialized Agent Effectiveness

## Purpose: Comprehensive Agent Performance Validation

The `/test-agents` command validates your specialized agents using real project scenarios, measuring their effectiveness, accuracy, and specialization compliance. This ensures agents provide genuine value and maintain quality standards over time.

**Agent Testing Philosophy**: Evidence-based validation, realistic scenario testing, measurable performance metrics, continuous improvement feedback, transparent quality assessment.

## 🎯 Comprehensive Testing Framework

### Multi-Dimensional Agent Validation
- **Scenario Testing**: Real-world project scenarios that match agent specialization
- **Performance Benchmarking**: Response time, accuracy, and quality measurements
- **Specialization Compliance**: Verify agents stay within defined expertise boundaries
- **Integration Testing**: Validate agent collaboration and handoff effectiveness

### Continuous Quality Assurance
- **Baseline Establishment**: Set performance baselines for each agent type
- **Regression Detection**: Identify when agent performance degrades over time
- **Improvement Tracking**: Monitor agent enhancement and capability growth
- **Comparative Analysis**: Compare agent performance against project team standards

## 🧪 Agent Testing Scenarios

### Core Coordination Agent Tests

**🏗️ Architecture Agent Testing**
```bash
/test-agents architecture --scenario=system-design
```

**Test Scenarios**:
1. **System Design Challenge** (5 minutes)
   - Present complex architectural decision scenario
   - Evaluate recommendation quality and trade-off analysis
   - Measure alignment with project's architectural principles
   - Validate performance impact considerations

2. **Framework Integration Analysis** (3 minutes)
   - Analyze integration patterns for new technology addition
   - Assess compatibility with existing architecture
   - Evaluate migration strategy recommendations
   - Validate security and performance implications

3. **Scalability Planning** (4 minutes)
   - Present growing load and usage scenarios
   - Evaluate scaling strategy recommendations
   - Assess resource planning and optimization guidance
   - Validate cost-benefit analysis accuracy

**Success Criteria**:
- Architecture recommendations align with project patterns (>95%)
- Trade-off analysis includes performance, security, maintainability (100%)
- Response time under 2 seconds for complex scenarios (target)
- Integration suggestions maintain architectural consistency (>95%)

**⚙️ Code Generation Agent Testing**
```bash
/test-agents code-generation --scenario=component-creation
```

**Test Scenarios**:
1. **Component Generation** (4 minutes)
   - Request creation of project-specific component
   - Evaluate code quality and pattern adherence
   - Validate consistency with existing codebase style
   - Assess integration with project architecture

2. **API Endpoint Creation** (5 minutes)
   - Generate REST/GraphQL endpoints following project patterns
   - Validate error handling and response format consistency
   - Assess authentication and authorization implementation
   - Evaluate testing and documentation generation

3. **Database Integration** (4 minutes)
   - Generate data access layer following project ORM patterns
   - Validate query optimization and error handling
   - Assess transaction management and connection pooling
   - Evaluate migration script generation

**Success Criteria**:
- Generated code compiles without errors (100%)
- Code follows project conventions and style guide (>95%)
- Integration with existing components works seamlessly (>95%)
- Performance characteristics meet project requirements (>90%)

**🧪 Testing Agent Testing**
```bash
/test-agents testing --scenario=tdd-enforcement
```

**Test Scenarios**:
1. **TDD Workflow Enforcement** (6 minutes)
   - Present feature development scenario requiring TDD
   - Evaluate test-first approach and Red-Green-Refactor enforcement
   - Validate code deletion penalty for non-TDD work
   - Assess test quality and coverage achievement

2. **Test Suite Creation** (5 minutes)
   - Generate comprehensive test suites for complex features
   - Validate unit, integration, and acceptance test coverage
   - Assess test maintainability and readability
   - Evaluate test execution performance and reliability

3. **Quality Gate Validation** (3 minutes)
   - Apply project-specific quality gates to code changes
   - Validate coverage thresholds and quality metrics
   - Assess integration with CI/CD pipeline requirements
   - Evaluate failure reporting and remediation guidance

**Success Criteria**:
- TDD enforcement prevents non-tested code (100% compliance)
- Test coverage meets project standards (>85% minimum)
- Test execution time remains within acceptable limits (<2 minutes)
- Quality gate validation accurately identifies issues (>95%)

**🔍 Debugging Agent Testing**
```bash
/test-agents debugging --scenario=error-diagnosis
```

**Test Scenarios**:
1. **Error Pattern Recognition** (4 minutes)
   - Present common error scenarios from project history
   - Evaluate diagnosis accuracy and root cause identification
   - Assess debugging strategy recommendations
   - Validate fix suggestion effectiveness

2. **Performance Issue Analysis** (5 minutes)
   - Present performance degradation scenarios
   - Evaluate bottleneck identification and analysis
   - Assess optimization recommendation quality
   - Validate monitoring and alerting guidance

3. **Integration Problem Resolution** (4 minutes)
   - Present API integration and data flow issues
   - Evaluate problem isolation and diagnosis approach
   - Assess solution recommendation accuracy
   - Validate prevention strategy effectiveness

**Success Criteria**:
- Root cause identification accuracy >90% for known issue patterns
- Debugging strategy reduces resolution time by >50%
- Solution recommendations resolve issues without side effects (>95%)
- Prevention strategies reduce issue recurrence (>80%)

### Specialized Function Agent Tests

**📝 Documentation Agent Testing**
```bash
/test-agents documentation --scenario=api-documentation
```

**Test Scenarios**:
1. **API Documentation Generation** (4 minutes)
   - Generate comprehensive API documentation from code
   - Evaluate completeness, accuracy, and clarity
   - Validate consistency with project documentation standards
   - Assess maintainability and update procedures

2. **Code Comment Enhancement** (3 minutes)
   - Enhance existing code with appropriate comments
   - Evaluate comment quality and usefulness
   - Validate consistency with project commenting standards
   - Assess impact on code readability and maintainability

**Success Criteria**:
- Documentation accuracy matches implemented functionality (>98%)
- Completeness covers all required documentation elements (100%)
- Readability score meets project standards (target: >4.0/5.0)
- Update synchronization with code changes (>95%)

**👥 Review Agent Testing**
```bash
/test-agents review --scenario=code-review
```

**Test Scenarios**:
1. **Code Review Process** (5 minutes)
   - Review code changes against project standards
   - Evaluate issue identification and severity assessment
   - Validate adherence to team code review checklist
   - Assess improvement recommendation quality

2. **Standards Enforcement** (3 minutes)
   - Apply project-specific coding standards to code samples
   - Evaluate consistency with team conventions
   - Validate security and performance standard compliance
   - Assess refactoring recommendation appropriateness

**Success Criteria**:
- Issue detection accuracy matches human reviewer findings (>90%)
- Standard compliance validation covers all defined criteria (100%)
- Recommendation quality improves code maintainability (>85%)
- Review consistency across similar code patterns (>95%)

## 📊 Performance Benchmarking System

### Response Time Benchmarks
```bash
/test-agents all --benchmark --response-time
```

**Benchmark Categories**:
- **Simple Queries**: Basic agent consultation (target: <1s)
- **Complex Analysis**: Deep analysis and recommendations (target: <3s)
- **Code Generation**: Creating project-specific code (target: <5s)
- **Multi-Agent Coordination**: Collaborative agent workflows (target: <10s total)

### Accuracy Measurements
```bash
/test-agents all --benchmark --accuracy
```

**Accuracy Metrics**:
- **Technical Accuracy**: Correctness of technical recommendations (target: >95%)
- **Context Relevance**: Appropriateness for specific project context (target: >90%)
- **Specialization Compliance**: Staying within agent expertise boundaries (target: 100%)
- **Integration Consistency**: Compatibility with existing project patterns (target: >95%)

### Quality Scoring System
```bash
/test-agents all --benchmark --quality-score
```

**Quality Dimensions**:
- **Usefulness**: How helpful is the agent contribution (1-5 scale)
- **Completeness**: Does the response address all aspects of the request (1-5 scale)
- **Clarity**: How clear and understandable is the guidance (1-5 scale)
- **Actionability**: Can the user immediately act on the recommendations (1-5 scale)

## 🔄 Continuous Testing and Monitoring

### Automated Background Testing
```bash
/test-agents all --continuous --interval=daily
```

**Continuous Monitoring Features**:
- **Daily Health Checks**: Automated validation of agent responsiveness and accuracy
- **Performance Trend Analysis**: Track agent performance over time
- **Regression Detection**: Alert when agent performance drops below thresholds
- **Context Currency**: Verify agents stay current with project evolution

### Performance Degradation Alerts
```bash
/test-agents --monitor --alert-thresholds="accuracy<90%,response-time>3s"
```

**Alert Conditions**:
- **Accuracy Drop**: Agent accuracy falls below defined thresholds
- **Response Degradation**: Response times exceed acceptable limits  
- **Specialization Drift**: Agent responses move outside expertise boundaries
- **Integration Failures**: Agent collaboration effectiveness decreases

## 📈 Test Results Analysis and Reporting

### Comprehensive Test Reports
```bash
/test-agents architecture --report=detailed
```

**Report Components**:
1. **Executive Summary**: Overall agent performance and health status
2. **Scenario Results**: Detailed results for each test scenario
3. **Performance Benchmarks**: Response time, accuracy, and quality metrics
4. **Trend Analysis**: Performance changes over time
5. **Improvement Recommendations**: Specific actions to enhance agent effectiveness

### Comparative Analysis
```bash
/test-agents --compare --baseline=last-month
```

**Comparison Features**:
- **Historical Performance**: Compare current results with previous test runs
- **Cross-Agent Analysis**: Compare performance across different agent types
- **Industry Benchmarks**: Compare against best-practice performance standards
- **Project Evolution**: Track how agent performance changes as project grows

## 🎯 Test-Driven Agent Improvement

### Scenario-Based Enhancement
```bash
/test-agents debugging --scenario=custom --improve-based-on-results
```

**Improvement Process**:
1. **Gap Identification**: Identify specific areas where agent performance is suboptimal
2. **Scenario Creation**: Develop targeted test scenarios for improvement areas
3. **Knowledge Enhancement**: Update agent knowledge base with project-specific learnings
4. **Validation Testing**: Re-test to validate improvements achieve desired results

### Performance Optimization
```bash
/test-agents all --optimize --target-metrics="response-time<2s,accuracy>95%"
```

**Optimization Features**:
- **Context Optimization**: Streamline agent knowledge for faster access
- **Response Caching**: Cache common responses for improved speed
- **Model Fine-tuning**: Adjust agent behavior based on test results
- **Integration Optimization**: Improve agent collaboration efficiency

## ⚡ Usage Examples

### Test Individual Agents
```bash
# Test specific agent with realistic scenarios
/test-agents architecture --scenario=all
/test-agents testing --scenario=tdd-enforcement  
/test-agents debugging --scenario=error-diagnosis
```

### Comprehensive Agent Team Testing
```bash
# Test all active agents with performance benchmarks
/test-agents all --benchmark --detailed-report

# Continuous monitoring setup
/test-agents all --continuous --alert-email=team@company.com
```

### Custom Testing Scenarios
```bash
# Create project-specific test scenarios
/test-agents code-generation --custom-scenario="microservice-api-creation"
/test-agents security --custom-scenario="oauth-implementation-review"
```

### Performance Analysis and Improvement
```bash
# Analyze performance trends
/test-agents all --trend-analysis --period=30-days

# Optimize underperforming agents
/test-agents performance refactoring --optimize --target-accuracy=95%
```

## 🔗 Integration with Agent Management

### Seamless Workflow Integration
- **Pre-Activation Testing**: Validate agents before making them available
- **Performance-Based Recommendations**: Suggest agent combinations based on test results
- **Quality-Driven Updates**: Trigger agent updates when performance degrades
- **Coordination Optimization**: Use test results to improve multi-agent workflows

### Feedback Loop
- **Test Results Feed Training**: Agent performance data improves future agent generation
- **User Feedback Integration**: Combine automated testing with user satisfaction metrics
- **Continuous Learning**: Agents learn from test scenarios and performance patterns
- **Project Evolution Tracking**: Tests adapt as project needs and patterns evolve

## 🚀 Success Criteria

**Testing Completeness**: All active agents tested with project-relevant scenarios (100%)
**Performance Validation**: All agents meet or exceed defined performance thresholds (>90%)
**Quality Assurance**: Continuous monitoring maintains agent effectiveness over time
**Improvement Tracking**: Clear evidence of agent performance enhancement through testing

**🎯 Final Result**: High-confidence validation that your specialized agents provide genuine value, maintain quality standards, and continuously improve their effectiveness for your specific project needs.