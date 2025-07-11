# Simplified Commands - Official Onboarding System

**Version**: 1.0.0 | **Status**: Onboarding Tier | **Last Updated**: 2025-07-09

---

## Purpose: Framework Onboarding & Learning

This directory contains the **official onboarding system** for the Claude Code Framework. These 10 simplified commands provide a gentle introduction to framework concepts while delivering real value for development workflows.

### Two-Tier System Design

**Simplified Commands (This Directory)**:
- **Target**: New users, learning, quick tasks
- **Focus**: Core functionality without complexity
- **Benefits**: Lower barrier to entry, faster execution, easier understanding

**Full Framework Commands** (`.claude/commands/`):
- **Target**: Advanced users, complex projects, production workflows
- **Focus**: Complete framework integration with meta-prompting
- **Benefits**: Maximum power, quality gates, multi-agent coordination

### When to Use Each Tier

**Use Simplified Commands When**:
- Learning the framework for the first time
- Performing straightforward development tasks
- Working on personal projects or prototypes
- Wanting faster, more direct execution

**Graduate to Full Framework When**:
- Working on production systems
- Needing advanced quality gates and TDD enforcement
- Requiring multi-agent coordination
- Wanting meta-prompting and adaptive capabilities

---

## Available Commands

### 1. `/context-prime` - Project Context Establishment
- **Purpose**: Establish comprehensive project context for optimal development
- **Use Cases**: New project understanding, session context setup, project onboarding
- **Key Features**: Project analysis, recent activity review, pattern recognition
- **Output**: Project overview, development patterns, context summary

### 2. `/task` - Single Task Execution
- **Purpose**: Execute focused single tasks with basic TDD support
- **Use Cases**: Bug fixes, small features, targeted improvements
- **Key Features**: Research-first approach, test-driven development, quality focus
- **Output**: Completed task with tests and documentation

### 3. `/research` - Research & Analysis
- **Purpose**: Comprehensive research and analysis of codebases and technologies
- **Use Cases**: Understanding complex systems, investigating issues, exploring solutions
- **Key Features**: Multi-source investigation, pattern analysis, actionable insights
- **Output**: Research findings, analysis results, recommendations

### 4. `/feature` - Feature Development
- **Purpose**: End-to-end feature development from planning to deployment
- **Use Cases**: New features, significant enhancements, complex integrations
- **Key Features**: Complete development lifecycle, TDD integration, quality assurance
- **Output**: Complete feature with tests, documentation, and deployment preparation

### 5. `/review` - Code Review & Quality Analysis
- **Purpose**: Comprehensive code review and quality analysis
- **Use Cases**: Pre-deployment review, code quality assessment, security analysis
- **Key Features**: Multi-faceted analysis, security assessment, actionable feedback
- **Output**: Quality review report with recommendations and metrics

### 6. `/debug` - Debugging & Troubleshooting
- **Purpose**: Systematic debugging and problem-solving
- **Use Cases**: Bug investigation, performance issues, system failures
- **Key Features**: Root cause analysis, solution development, prevention strategy
- **Output**: Debug report with solutions and prevention measures

### 7. `/test` - Testing Workflows
- **Purpose**: Comprehensive testing workflows and TDD support
- **Use Cases**: Test creation, test execution, coverage analysis
- **Key Features**: Multi-level testing, automation support, quality assurance
- **Output**: Test results, coverage reports, quality metrics

### 8. `/refactor` - Code Refactoring
- **Purpose**: Systematic code improvement and technical debt reduction
- **Use Cases**: Code cleanup, architecture improvements, performance optimization
- **Key Features**: Safe refactoring, quality focus, incremental improvements
- **Output**: Improved code with quality metrics and documentation

### 9. `/docs` - Documentation Generation
- **Purpose**: Create and manage comprehensive documentation
- **Use Cases**: User guides, API documentation, technical specifications
- **Key Features**: Multiple content types, quality assurance, maintenance support
- **Output**: Well-structured documentation with style consistency

### 10. `/deploy` - Deployment & Production Workflows
- **Purpose**: Safe deployment and production workflows
- **Use Cases**: Production releases, environment management, rollback procedures
- **Key Features**: Safe deployment, monitoring, rollback capabilities
- **Output**: Successful deployment with monitoring and documentation

---

## Command Selection Guide

### For Understanding & Research
- **New to project**: Start with `/context-prime`
- **Research questions**: Use `/research`
- **Code investigation**: Use `/research` followed by `/review`

### For Development Work
- **Small changes**: Use `/task`
- **New features**: Use `/feature`
- **Code improvements**: Use `/refactor`

### For Quality & Maintenance
- **Code review**: Use `/review`
- **Testing**: Use `/test`
- **Bug fixing**: Use `/debug`

### For Documentation & Deployment
- **Documentation**: Use `/docs`
- **Deployment**: Use `/deploy`

---

## Typical Workflows

### New Project Onboarding
1. `/context-prime` - Establish project context
2. `/research` - Investigate specific areas of interest
3. `/task` or `/feature` - Begin development work

### Feature Development
1. `/context-prime` - Ensure current project context
2. `/research` - Research requirements and approach
3. `/feature` - End-to-end feature development
4. `/review` - Quality review before deployment
5. `/deploy` - Safe deployment to production

### Bug Investigation & Fix
1. `/context-prime` - Establish project context
2. `/debug` - Investigate and identify root cause
3. `/task` - Implement fix with tests
4. `/review` - Review fix quality
5. `/deploy` - Deploy fix to production

### Code Quality Improvement
1. `/context-prime` - Understand current state
2. `/review` - Analyze code quality issues
3. `/refactor` - Implement improvements
4. `/test` - Validate improvements
5. `/docs` - Update documentation

---

## Key Differences from Full Framework

### Simplified Structure
- **No Complex XML**: Simple workflow descriptions instead of complex XML configurations
- **No Module Dependencies**: Self-contained logic without external module dependencies
- **No Advanced Frameworks**: Basic patterns instead of RISE, CARE, TRACE, etc.
- **No Mandatory Enforcement**: Supportive guidance instead of blocking enforcement

### Core Focus
- **Essential Functionality**: Focuses on core capabilities needed for most development workflows
- **Practical Quality**: Basic quality checks without complex gate systems
- **Fast Execution**: Minimal overhead for quick task completion
- **Clear Results**: Well-structured, actionable output

---

## Progression Path

### Learning Journey
1. **Start Here**: Use simplified commands to learn framework concepts
2. **Build Confidence**: Complete real projects with simplified commands
3. **Identify Needs**: Recognize when you need advanced features
4. **Graduate**: Move to full framework commands for production workflows

### Migration Indicators
**Consider Full Framework When**:
- Working on production systems requiring strict quality gates
- Needing multi-agent coordination for complex projects
- Wanting meta-prompting and adaptive intelligence
- Requiring advanced security and threat modeling
- Managing complex module dependencies

**Stay with Simplified When**:
- Learning and prototyping
- Personal projects and quick tasks
- Preferring simpler, more direct workflows
- Working solo without complex coordination needs

---

## Integration with Full Framework

### Compatibility
- **Shared Principles**: Both tiers follow same core development principles
- **Smooth Transition**: Knowledge gained here applies to full framework
- **Flexible Usage**: Can mix simplified and full commands as needed
- **Consistent Quality**: Both maintain code quality standards

### Framework Architecture
- **Onboarding Tier**: These simplified commands (`.claude/commands-simplified/`)
- **Production Tier**: Full framework commands (`.claude/commands/`)
- **Module System**: 100+ modules supporting full framework
- **Meta-Framework**: Self-improving capabilities in production tier

### Accessibility
- **Easier to Understand**: Simpler structure and clearer documentation
- **Lower Learning Curve**: Basic functionality that's easier to learn and use
- **Self-Contained**: No need to understand complex module interactions
- **Practical Examples**: Clear usage examples and typical workflows

---

## When to Use Simplified vs Full Framework

### Use Simplified Commands When:
- **Getting Started**: New to the framework or project
- **Basic Workflows**: Standard development tasks and workflows
- **Quick Tasks**: Need fast execution without complex setup
- **Learning**: Learning the framework concepts and patterns

### Use Full Framework Commands When:
- **Complex Projects**: Multi-component, complex architectural work
- **Advanced Features**: Need advanced framework capabilities
- **Enterprise Requirements**: Need complex quality gates and compliance
- **Team Coordination**: Multi-agent coordination and collaboration

---

## Getting Started

### 1. Choose Your Command
- Review the command descriptions above
- Select the command that best fits your current need
- Read the specific command documentation

### 2. Understand the Command
- Review the command's purpose and use cases
- Understand the workflow and expected output
- Check the examples and typical usage patterns

### 3. Execute the Command
- Use the command with appropriate parameters
- Follow the command's workflow guidance
- Review the output and recommendations

### 4. Iterate and Improve
- Use the command output to guide next steps
- Combine multiple commands for complex workflows
- Provide feedback and suggest improvements

---

## Best Practices

### Command Usage
- Start with `/context-prime` for new projects or sessions
- Use `/research` before complex implementation work
- Follow TDD principles with `/task` and `/feature`
- Use `/review` before deployment or major changes

### Quality Assurance
- Run tests frequently during development
- Review code quality regularly
- Document decisions and changes
- Monitor system health after deployment

### Workflow Optimization
- Combine commands for complex workflows
- Use appropriate command for task scope
- Iterate based on command output
- Build on previous command results

---

## Command Integration

### Sequential Usage
Many commands work well in sequence:
- `/context-prime` → `/research` → `/task`
- `/research` → `/feature` → `/review` → `/deploy`
- `/debug` → `/task` → `/test` → `/deploy`

### Parallel Usage
Some commands provide complementary perspectives:
- `/review` + `/test` for quality assessment
- `/research` + `/debug` for issue investigation
- `/refactor` + `/test` for code improvement

### Iterative Usage
Commands can be used iteratively for continuous improvement:
- Regular `/review` for code quality monitoring
- Periodic `/refactor` for technical debt reduction
- Continuous `/test` for quality assurance

---

## Support & Feedback

### Getting Help
- Review individual command documentation
- Check the examples and use cases
- Refer to the typical workflows section
- Use `/context-prime` to understand project context

### Providing Feedback
- Document any issues or limitations encountered
- Suggest improvements or additional features
- Share successful workflow patterns
- Contribute to documentation improvements

### Contributing
- Test commands in different scenarios
- Provide usage examples and patterns
- Suggest new command ideas
- Help improve documentation clarity

---

## Future Enhancements

### Planned Improvements
- Enhanced error handling and recovery
- Better integration between commands
- More comprehensive examples and tutorials
- Performance optimization and faster execution

### Community Contributions
- Additional command variations
- Domain-specific command extensions
- Integration with popular development tools
- Best practice sharing and documentation

---

## Conclusion

These simplified commands provide a solid foundation for development workflows while maintaining simplicity and accessibility. They offer essential functionality without the complexity of the full framework, making them ideal for getting started, learning, and handling standard development tasks.

For advanced features, complex orchestration, or enterprise requirements, consider using the full framework commands in `.claude/commands/`. Both approaches can be used together as needed.

**Remember**: The goal is to be productive and effective. Choose the approach that best fits your current needs and skill level.