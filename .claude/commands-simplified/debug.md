# /debug - Debugging & Troubleshooting

**Version**: 1.0.0 | **Status**: Basic | **Last Updated**: 2025-07-09

---

## Purpose

Debug issues and troubleshoot problems systematically using proven debugging methodologies. Ideal for investigating bugs, performance issues, failures, and unexpected behavior.

**Note**: This is a simplified version that focuses on core debugging functionality without complex diagnostic frameworks.

---

## How It Works

### 1. Problem Investigation
- **Issue Analysis**: Understand the problem and its symptoms
- **Environment Assessment**: Analyze the context and environment
- **Reproduction**: Attempt to reproduce the issue consistently
- **Data Collection**: Gather relevant logs, errors, and evidence

### 2. Root Cause Analysis
- **Hypothesis Formation**: Develop theories about potential causes
- **Testing**: Test hypotheses systematically
- **Evidence Evaluation**: Analyze evidence and eliminate possibilities
- **Cause Identification**: Identify the root cause of the issue

### 3. Solution Development
- **Fix Planning**: Plan the appropriate fix or workaround
- **Implementation**: Implement the solution safely
- **Testing**: Verify the fix resolves the issue
- **Validation**: Ensure no new issues are introduced

### 4. Prevention & Documentation
- **Documentation**: Document the issue and solution
- **Prevention**: Identify ways to prevent similar issues
- **Monitoring**: Set up monitoring to detect similar problems
- **Knowledge Sharing**: Share findings with team

---

## Usage Examples

```bash
# Debug specific error
/debug "Database connection timeout error"

# Debug performance issue
/debug "Application slow response time" --focus performance

# Debug test failure
/debug "Unit tests failing intermittently" --focus testing

# Debug production issue
/debug "Users unable to login" --environment production

# Debug with specific context
/debug "Memory leak in payment processing" --context payment-service
```

---

## What It Does

### Issue Investigation
- Analyzes symptoms and error messages
- Examines logs and system information
- Identifies patterns and correlations
- Gathers relevant diagnostic data

### Root Cause Analysis
- Systematically eliminates potential causes
- Tests hypotheses with targeted experiments
- Analyzes code paths and execution flow
- Identifies the underlying problem

### Solution Implementation
- Develops targeted fixes or workarounds
- Implements solutions safely and incrementally
- Verifies fixes resolve the original issue
- Ensures no regression or new issues

### Prevention Strategy
- Identifies systemic issues and improvements
- Suggests monitoring and alerting enhancements
- Recommends process improvements
- Creates documentation and knowledge base

---

## Debugging Types

### Bug Investigation
```
PURPOSE: Identify and fix software bugs
APPROACH: Reproduction, analysis, root cause identification
OUTPUT: Bug report, fix implementation, prevention strategy
```

### Performance Debugging
```
PURPOSE: Identify and resolve performance issues
APPROACH: Profiling, bottleneck identification, optimization
OUTPUT: Performance analysis, optimization recommendations, monitoring
```

### System Troubleshooting
```
PURPOSE: Resolve system-level issues and failures
APPROACH: System analysis, component testing, integration debugging
OUTPUT: System health assessment, fixes, monitoring improvements
```

### Test Debugging
```
PURPOSE: Identify and fix test failures and flakiness
APPROACH: Test analysis, isolation, environment investigation
OUTPUT: Test fixes, stability improvements, test infrastructure updates
```

---

## Output Format

### Debug Summary
```
ISSUE: [problem-description]
SEVERITY: [low/medium/high/critical]
ENVIRONMENT: [development/staging/production]
STATUS: [investigating/analyzing/fixing/resolved]
```

### Investigation Results
```
SYMPTOMS: [observed-symptoms-and-behavior]
EVIDENCE: [logs-errors-and-diagnostic-data]
PATTERNS: [identified-patterns-and-correlations]
REPRODUCTION: [reproduction-steps-and-consistency]
```

### Root Cause Analysis
```
HYPOTHESES: [tested-hypotheses-and-theories]
ANALYSIS: [analysis-methods-and-findings]
ROOT_CAUSE: [identified-root-cause]
CONTRIBUTING_FACTORS: [additional-factors-and-context]
```

### Solution Implementation
```
SOLUTION: [implemented-fix-or-workaround]
TESTING: [verification-and-validation-results]
IMPACT: [solution-impact-and-side-effects]
DEPLOYMENT: [deployment-and-rollout-plan]
```

### Prevention Strategy
```
MONITORING: [monitoring-and-alerting-improvements]
PREVENTION: [measures-to-prevent-recurrence]
DOCUMENTATION: [issue-and-solution-documentation]
KNOWLEDGE_SHARING: [team-communication-and-learning]
```

---

## Debugging Methodology

### 1. Problem Definition
- Clearly define the issue and symptoms
- Gather initial information and context
- Assess severity and impact
- Set investigation priorities

### 2. Information Gathering
- Collect logs, error messages, and traces
- Examine system metrics and performance data
- Interview users or stakeholders
- Document environmental factors

### 3. Hypothesis Generation
- Brainstorm potential causes
- Prioritize hypotheses by likelihood
- Consider both technical and process factors
- Plan testing approach for each hypothesis

### 4. Testing and Analysis
- Test hypotheses systematically
- Isolate variables and components
- Analyze results and gather evidence
- Eliminate or confirm potential causes

### 5. Solution Development
- Develop targeted fix or workaround
- Consider multiple solution approaches
- Evaluate risks and trade-offs
- Plan implementation and testing

### 6. Verification and Deployment
- Test solution thoroughly
- Verify issue resolution
- Deploy fix safely
- Monitor for regression or new issues

---

## Key Features

### ✅ Systematic Approach
- Structured debugging methodology
- Logical problem-solving process
- Evidence-based analysis
- Comprehensive documentation

### ✅ Multi-Domain Support
- Software bugs and errors
- Performance and scalability issues
- System and infrastructure problems
- Testing and quality issues

### ✅ Solution-Focused
- Practical fix recommendations
- Workaround strategies
- Prevention measures
- Long-term improvements

### ✅ Knowledge Building
- Detailed documentation
- Lessons learned capture
- Best practice development
- Team knowledge sharing

---

## Common Debugging Scenarios

### Application Errors
- **Runtime Exceptions**: Unexpected errors and crashes
- **Logic Errors**: Incorrect behavior and results
- **Integration Issues**: Problems with external services
- **Configuration Problems**: Misconfiguration and setup issues

### Performance Issues
- **Slow Response Times**: Application performance problems
- **Memory Leaks**: Memory usage and garbage collection issues
- **CPU Bottlenecks**: High CPU usage and processing delays
- **Database Performance**: Query optimization and connection issues

### System Problems
- **Deployment Failures**: Deployment and configuration issues
- **Environment Issues**: Development, staging, production problems
- **Infrastructure Problems**: Server, network, and service issues
- **Monitoring Alerts**: System health and alerting issues

### Test Issues
- **Flaky Tests**: Intermittent test failures
- **Test Environment**: Testing infrastructure problems
- **Test Data**: Data-related test issues
- **CI/CD Pipeline**: Build and deployment pipeline problems

---

## Best Practices

### When to Use
- **Bug Reports**: When bugs are reported or discovered
- **Performance Issues**: When system performance degrades
- **System Failures**: When services or components fail
- **Test Failures**: When tests fail or become unreliable

### Debugging Tips
- Start with the most likely causes
- Use systematic elimination approach
- Document everything throughout the process
- Don't assume - verify with evidence
- Consider both technical and process factors

### Quality Guidelines
- Be thorough but efficient
- Focus on root causes, not just symptoms
- Implement sustainable fixes
- Include prevention measures
- Share knowledge and findings

---

## Error Handling

### Common Issues
- **Intermittent Problems**: Uses statistical analysis and monitoring
- **Complex Systems**: Breaks down into manageable components
- **Limited Information**: Suggests additional data collection
- **Multiple Causes**: Prioritizes by impact and likelihood

### Graceful Degradation
- Provides partial solutions when full resolution complex
- Suggests workarounds when immediate fixes not possible
- Maintains system stability during debugging
- Documents limitations and next steps

---

## Integration

### Works Well With
- `/context-prime` - For project context before debugging
- `/research` - For investigating complex technical issues
- `/task` - For implementing fixes and solutions
- `/review` - For reviewing fixes and prevention measures

### Typical Workflow
1. **Context**: `/context-prime` to understand project context
2. **Debug**: `/debug` to investigate and analyze the issue
3. **Research**: `/research` for complex technical investigation
4. **Implementation**: `/task` to implement fixes and solutions

---

## Debugging Tools & Techniques

### Investigation Techniques
- **Log Analysis**: Systematic log examination
- **Error Tracing**: Stack trace and error analysis
- **Performance Profiling**: Performance measurement and analysis
- **System Monitoring**: Real-time system observation

### Testing Approaches
- **Isolation Testing**: Component and integration testing
- **Regression Testing**: Ensuring fixes don't break existing functionality
- **Load Testing**: Performance and stress testing
- **Monitoring Validation**: Verifying monitoring and alerting

### Documentation Methods
- **Issue Tracking**: Detailed problem documentation
- **Solution Recording**: Fix implementation and rationale
- **Knowledge Base**: Reusable debugging knowledge
- **Process Improvement**: Debugging process refinement

---

## Prevention Strategies

### Monitoring Improvements
- Enhanced logging and metrics
- Proactive alerting and notifications
- Performance monitoring and thresholds
- Error tracking and analysis

### Process Improvements
- Code review and quality gates
- Testing strategy enhancements
- Deployment safety measures
- Documentation and knowledge sharing

### System Improvements
- Architecture and design improvements
- Error handling and resilience
- Performance optimization
- Security and reliability enhancements

---

## Differences from Full Framework

### Simplified Approach
- **No Complex XML**: Simple debugging workflow
- **No Module Dependencies**: Self-contained debugging logic
- **No Advanced Frameworks**: Basic debugging and analysis patterns
- **No Mandatory Enforcement**: Supportive debugging guidance

### Core Focus
- **Essential Debugging**: Core investigation, analysis, and resolution
- **Practical Solutions**: Actionable fixes and workarounds
- **Fast Execution**: Minimal overhead for quick debugging
- **Clear Results**: Well-structured debugging reports

---

**Note**: This simplified command provides core debugging functionality without the complexity of the full framework. For advanced features like complex diagnostic frameworks, multi-agent debugging coordination, or advanced system analysis, use the full framework commands.