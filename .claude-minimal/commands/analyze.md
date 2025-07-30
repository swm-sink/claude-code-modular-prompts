---
name: /analyze
description: "Analyze code, architecture, problems, or performance issues"  
usage: /analyze "what to analyze" [file-path]
category: core
tools: Read, Bash, Grep, Glob, LS
---

# Universal Code & System Analysis

**Deep analysis of code, architecture, performance, or any technical problem.**

## Analysis Types

### Code Analysis
```
/analyze "this function is confusing" src/utils/parser.js
/analyze "code quality issues in my project"
/analyze "architecture problems in my microservices"
```

### Performance Analysis  
```
/analyze "why is my app slow?"
/analyze "database performance issues"
/analyze "frontend bundle size problems"
```

### Problem Diagnosis
```
/analyze "users report login failures"  
/analyze "memory usage keeps growing"
/analyze "API response times are inconsistent"
```

### Architecture Review
```
/analyze "is my system architecture scalable?"
/analyze "security vulnerabilities in my setup"
/analyze "technical debt in the codebase"
```

## What I'll Examine

**🔍 Code Level:**
- Function complexity and readability
- Design patterns and anti-patterns  
- Error handling completeness
- Code duplication and maintainability
- Security vulnerabilities

**🏗️ Architecture Level:**
- System design and scalability
- Component coupling and cohesion
- Data flow and dependencies
- Performance bottlenecks
- Infrastructure concerns

**📊 Project Level:**  
- Overall code quality metrics
- Technical debt assessment
- Testing coverage gaps
- Documentation completeness
- Development workflow issues

## Analysis Outputs

### Detailed Reports
- **Root cause identification**
- **Impact assessment** (critical/medium/low)
- **Specific recommendations** with code examples
- **Implementation priority** ranking
- **Effort estimation** for fixes

### Visual Insights
- **Architecture diagrams** for complex systems
- **Flow charts** for process analysis  
- **Dependency graphs** for coupling analysis
- **Performance profiles** with bottleneck identification

## Example Analysis Sessions

### Performance Investigation
```
👤 /analyze "my React app renders are slow"

🤖 Analyzing React performance...
🤖 Scanning components for render issues...

📊 FINDINGS:
🔴 Critical Issues (3):
   • UserList.jsx: Renders entire list on every update
   • Dashboard.jsx: No memo usage with expensive calculations  
   • DataTable.jsx: Inefficient key prop usage

🟡 Optimization Opportunities (5):
   • Bundle size: 2.3MB (target: <1MB)
   • Unused dependencies: 12 packages
   • Large images not optimized

💡 RECOMMENDATIONS:
1. Implement React.memo for UserList
2. Add useMemo for Dashboard calculations
3. Use react-window for large lists
4. Optimize images with next/image

🕒 Estimated effort: 4-6 hours
```

### Architecture Assessment
```
👤 /analyze "scalability of my microservices architecture"

🤖 Analyzing microservices architecture...
🤖 Examining service boundaries and communication...

🏗️ ARCHITECTURE HEALTH:
✅ Good: Service separation, API design
⚠️  Concerns: Database per service not implemented
🔴 Issues: Synchronous inter-service calls

📈 SCALABILITY ASSESSMENT:
• Current load: ~1000 requests/minute  
• Projected bottlenecks at: ~5000 requests/minute
• Critical path: User service → Payment service

🎯 SCALING RECOMMENDATIONS:
1. Implement async messaging (RabbitMQ/Kafka)
2. Add database sharding for user service
3. Implement circuit breaker pattern
4. Add caching layer (Redis)
```

## Multi-Language Intelligence

**Automatically adapts analysis to:**
- **JavaScript/TypeScript**: React patterns, Node.js performance, bundle optimization
- **Python**: Django/Flask patterns, pandas performance, memory profiling  
- **Java**: Spring patterns, JVM tuning, concurrency analysis
- **Go**: Goroutine patterns, memory allocation, performance profiling
- **And many more...**

## Integration with Development

**Actionable Results:**
- Code examples for fixes
- Configuration changes needed
- Tool recommendations
- Monitoring suggestions
- Testing strategies

**Development Workflow:**
1. Run `/analyze` to understand issues
2. Use `/task` to implement recommended fixes
3. Use `/test` to verify improvements
4. Use `/review` to validate changes

## Analysis Depth Levels

**Quick Scan**: Surface-level issues and obvious improvements
**Deep Dive**: Comprehensive analysis with detailed recommendations  
**Expert Review**: Architecture-level analysis with strategic guidance

## Ready for Analysis?

Tell me what you'd like analyzed:

```
/analyze "performance issues in my app"
/analyze "code quality problems" 
/analyze "why my tests are flaky"
/analyze "security vulnerabilities"
```

I'll provide detailed insights and actionable recommendations!