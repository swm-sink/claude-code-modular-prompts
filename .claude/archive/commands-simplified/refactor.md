# /refactor - Code Refactoring

**Version**: 1.0.0 | **Status**: Basic | **Last Updated**: 2025-07-09

---

## Purpose

Improve code structure, design, and maintainability through systematic refactoring while preserving functionality. Ideal for code cleanup, architecture improvements, and technical debt reduction.

**Note**: This is a simplified version that focuses on core refactoring functionality without complex quality gate enforcement.

---

## How It Works

### 1. Code Analysis
- **Quality Assessment**: Analyze current code quality and structure
- **Problem Identification**: Identify code smells and improvement opportunities
- **Impact Analysis**: Assess refactoring impact and dependencies
- **Strategy Planning**: Plan refactoring approach and phases

### 2. Refactoring Planning
- **Scope Definition**: Define refactoring scope and boundaries
- **Safety Measures**: Plan safety nets and rollback procedures
- **Test Strategy**: Ensure comprehensive test coverage
- **Phased Approach**: Break refactoring into manageable phases

### 3. Refactoring Implementation
- **Safe Refactoring**: Implement changes incrementally and safely
- **Test Validation**: Ensure tests pass at each step
- **Design Improvement**: Apply design patterns and best practices
- **Code Cleanup**: Remove duplication and improve readability

### 4. Validation & Documentation
- **Quality Validation**: Verify improvements in code quality
- **Performance Testing**: Ensure no performance degradation
- **Documentation Updates**: Update documentation to reflect changes
- **Knowledge Sharing**: Share refactoring insights and lessons learned

---

## Usage Examples

```bash
# Refactor specific component
/refactor "user authentication module"

# Remove code duplication
/refactor "extract common utility functions" --focus duplication

# Improve code structure
/refactor "reorganize database layer" --focus structure

# Apply design patterns
/refactor "implement strategy pattern for payment processing" --focus patterns

# Performance refactoring
/refactor "optimize query performance" --focus performance
```

---

## What It Does

### Code Analysis
- Identifies code smells and anti-patterns
- Analyzes code structure and organization
- Assesses maintainability and readability
- Evaluates performance characteristics

### Refactoring Planning
- Creates safe refactoring strategy
- Plans incremental improvement phases
- Identifies risks and mitigation strategies
- Ensures comprehensive test coverage

### Safe Implementation
- Implements changes incrementally
- Maintains functionality throughout process
- Validates changes with tests
- Provides rollback capabilities

### Quality Improvement
- Improves code structure and design
- Reduces technical debt
- Enhances maintainability
- Optimizes performance when needed

---

## Refactoring Types

### Structural Refactoring
```
PURPOSE: Improve code organization and structure
APPROACH: Extract methods, classes, modules; reorganize code
OUTPUT: Better organized, more maintainable code
```

### Design Pattern Refactoring
```
PURPOSE: Apply design patterns for better architecture
APPROACH: Implement patterns like Strategy, Factory, Observer
OUTPUT: More flexible, extensible code architecture
```

### Performance Refactoring
```
PURPOSE: Improve code performance and efficiency
APPROACH: Optimize algorithms, data structures, resource usage
OUTPUT: Faster, more efficient code execution
```

### Technical Debt Reduction
```
PURPOSE: Reduce accumulated technical debt
APPROACH: Code cleanup, documentation, test improvement
OUTPUT: Cleaner, more maintainable codebase
```

---

## Output Format

### Refactoring Summary
```
REFACTORING_TYPE: [structural/design/performance/debt-reduction]
SCOPE: [components-or-areas-refactored]
COMPLEXITY: [low/medium/high]
STATUS: [planned/in-progress/completed]
```

### Analysis Results
```
CODE_SMELLS: [identified-code-smells]
OPPORTUNITIES: [improvement-opportunities]
RISKS: [potential-risks-and-mitigation]
DEPENDENCIES: [affected-components-and-systems]
```

### Implementation Plan
```
PHASES: [planned-refactoring-phases]
SAFETY_MEASURES: [safety-nets-and-rollback-procedures]
TEST_STRATEGY: [testing-approach-and-validation]
TIMELINE: [estimated-timeline-and-milestones]
```

### Quality Improvements
```
BEFORE: [code-quality-metrics-before]
AFTER: [code-quality-metrics-after]
IMPROVEMENTS: [specific-improvements-achieved]
PERFORMANCE: [performance-impact-assessment]
```

---

## Common Refactoring Patterns

### Extract Method
- **Purpose**: Break down large methods into smaller, focused ones
- **Benefits**: Improved readability, reusability, testability
- **Safety**: Preserve method behavior and return values

### Extract Class
- **Purpose**: Split large classes into smaller, focused classes
- **Benefits**: Better separation of concerns, easier maintenance
- **Safety**: Maintain class interfaces and relationships

### Move Method/Field
- **Purpose**: Relocate methods or fields to more appropriate classes
- **Benefits**: Better cohesion, reduced coupling
- **Safety**: Preserve access patterns and dependencies

### Rename Variable/Method
- **Purpose**: Improve code readability through better naming
- **Benefits**: Clearer intent, easier understanding
- **Safety**: Update all references consistently

### Replace Magic Numbers
- **Purpose**: Replace hardcoded values with named constants
- **Benefits**: Improved maintainability, clearer intent
- **Safety**: Ensure value consistency across usage

### Eliminate Duplication
- **Purpose**: Remove duplicate code through extraction
- **Benefits**: Reduced maintenance burden, consistency
- **Safety**: Preserve individual behavior variations

---

## Key Features

### ✅ Safe Refactoring
- Incremental changes with validation
- Comprehensive test coverage maintenance
- Rollback capabilities and safety nets
- Risk assessment and mitigation

### ✅ Quality Focus
- Code smell identification and resolution
- Design pattern application
- Best practice implementation
- Technical debt reduction

### ✅ Performance Awareness
- Performance impact assessment
- Optimization opportunities identification
- Efficiency improvements
- Resource usage optimization

### ✅ Systematic Approach
- Structured refactoring methodology
- Phased implementation strategy
- Documentation and knowledge sharing
- Continuous improvement focus

---

## Refactoring Process

### 1. Assessment Phase
- Analyze current code quality and structure
- Identify code smells and improvement opportunities
- Assess refactoring impact and dependencies
- Plan refactoring strategy and approach

### 2. Planning Phase
- Define refactoring scope and boundaries
- Plan safety measures and rollback procedures
- Ensure comprehensive test coverage
- Break refactoring into manageable phases

### 3. Implementation Phase
- Implement changes incrementally and safely
- Validate changes with tests at each step
- Apply design patterns and best practices
- Clean up code and remove duplication

### 4. Validation Phase
- Verify improvements in code quality
- Test performance impact
- Update documentation and comments
- Share knowledge and lessons learned

---

## Safety Measures

### Test Coverage
- **Before Refactoring**: Ensure comprehensive test coverage
- **During Refactoring**: Run tests after each change
- **After Refactoring**: Validate all tests still pass
- **Regression Testing**: Ensure no functionality lost

### Incremental Changes
- **Small Steps**: Make small, focused changes
- **Frequent Validation**: Validate changes frequently
- **Rollback Capability**: Maintain ability to rollback
- **Change Tracking**: Track all changes made

### Risk Mitigation
- **Impact Assessment**: Understand refactoring impact
- **Dependency Analysis**: Identify affected components
- **Backup Strategy**: Maintain code backups
- **Monitoring**: Monitor system behavior post-refactoring

---

## Best Practices

### When to Use
- **Code Smells**: When code smells are identified
- **Technical Debt**: When technical debt needs reduction
- **Performance Issues**: When performance improvements needed
- **Architecture Changes**: When architectural improvements beneficial

### Refactoring Tips
- Start with comprehensive test coverage
- Make small, incremental changes
- Focus on one refactoring goal at a time
- Document decisions and trade-offs
- Validate changes frequently

### Quality Guidelines
- Preserve existing functionality
- Improve code readability and maintainability
- Apply appropriate design patterns
- Reduce code duplication
- Enhance performance when possible

---

## Error Handling

### Common Issues
- **Breaking Changes**: Prevents functionality loss through testing
- **Complex Dependencies**: Breaks refactoring into smaller phases
- **Performance Impact**: Monitors and optimizes performance
- **Integration Issues**: Validates integration points

### Graceful Degradation
- Provides partial refactoring when full refactoring complex
- Suggests alternative approaches when blocked
- Maintains system stability during refactoring
- Documents limitations and future improvements

---

## Integration

### Works Well With
- `/context-prime` - For project context before refactoring
- `/review` - For code quality assessment
- `/test` - For ensuring test coverage and validation
- `/task` - For implementing specific refactoring tasks

### Typical Workflow
1. **Context**: `/context-prime` to understand project context
2. **Review**: `/review` to assess code quality and identify issues
3. **Refactor**: `/refactor` to implement improvements
4. **Test**: `/test` to validate refactoring results

---

## Refactoring Metrics

### Code Quality Metrics
- **Complexity**: Cyclomatic complexity reduction
- **Duplication**: Code duplication elimination
- **Cohesion**: Class and module cohesion improvement
- **Coupling**: Reduced coupling between components

### Maintainability Metrics
- **Readability**: Code readability improvement
- **Documentation**: Documentation quality enhancement
- **Testability**: Test coverage and quality improvement
- **Modularity**: Better code organization and modularity

### Performance Metrics
- **Execution Time**: Performance improvement measurement
- **Memory Usage**: Memory efficiency optimization
- **Resource Utilization**: Resource usage optimization
- **Scalability**: Scalability characteristic improvement

---

## Refactoring Strategies

### Big Bang Refactoring
- **Approach**: Complete refactoring in one major effort
- **Benefits**: Comprehensive improvement, clean result
- **Risks**: High risk, difficult rollback
- **Use Cases**: Small codebases, isolated components

### Incremental Refactoring
- **Approach**: Gradual refactoring over time
- **Benefits**: Lower risk, easier validation
- **Risks**: May take longer, requires discipline
- **Use Cases**: Large codebases, production systems

### Strangler Fig Pattern
- **Approach**: Gradually replace old code with new
- **Benefits**: Minimal risk, continuous improvement
- **Risks**: Temporary complexity increase
- **Use Cases**: Legacy system modernization

---

## Common Code Smells

### Method-Level Smells
- **Long Methods**: Methods that are too long
- **Large Classes**: Classes with too many responsibilities
- **Long Parameter Lists**: Methods with too many parameters
- **Duplicate Code**: Repeated code blocks

### Class-Level Smells
- **God Class**: Classes that know too much
- **Feature Envy**: Methods using other classes excessively
- **Inappropriate Intimacy**: Classes that are too tightly coupled
- **Refused Bequest**: Subclasses that don't use parent functionality

### Design-Level Smells
- **Divergent Change**: Classes that change for multiple reasons
- **Shotgun Surgery**: Changes that affect many classes
- **Primitive Obsession**: Overuse of primitive types
- **Data Clumps**: Groups of data that appear together

---

## Differences from Full Framework

### Simplified Approach
- **No Complex XML**: Simple refactoring workflow
- **No Module Dependencies**: Self-contained refactoring logic
- **No Advanced Frameworks**: Basic refactoring patterns
- **No Mandatory Enforcement**: Supportive refactoring guidance

### Core Focus
- **Essential Refactoring**: Core code improvement and restructuring
- **Practical Safety**: Basic safety measures and validation
- **Fast Execution**: Minimal overhead for quick refactoring
- **Clear Results**: Well-structured refactoring outcomes

---

**Note**: This simplified command provides core refactoring functionality without the complexity of the full framework. For advanced features like complex quality gates, multi-agent refactoring coordination, or advanced architectural refactoring, use the full framework commands.