# Meta-Prompting Example

## Overview
This example demonstrates how to use the framework's meta-prompting capabilities for self-improvement, optimization, and intelligent adaptation to your specific project needs.

## Meta-Prompting Concepts

Meta-prompting allows the framework to:
- **Self-Analyze**: Understand its own performance and effectiveness
- **Self-Optimize**: Improve workflows based on usage patterns
- **Self-Adapt**: Customize behavior for your specific project
- **Self-Improve**: Learn from successes and failures

## Example Scenario
You've been using the framework for a month and want to optimize it for your team's specific workflows, improve performance bottlenecks, and adapt to your project's unique requirements.

## Meta-Commands Available

### 1. Framework Analysis with `/meta-review`

**Usage:**
```bash
/meta-review "analyze framework performance and identify optimization opportunities"
```

**Expected Response:**
```
🔍 FRAMEWORK PERFORMANCE ANALYSIS

📊 USAGE STATISTICS (Last 30 days):
- Total commands executed: 247
- Most used commands: /task (89), /feature (45), /query (67), /auto (46)
- Average response time: 3.2 seconds
- Success rate: 94.3%

📈 PERFORMANCE METRICS:
- Token efficiency: 73% (target: 80%)
- Context utilization: 68% (target: 75%)
- Quality gate pass rate: 91% (target: 95%)
- TDD compliance: 87% (target: 90%)

🎯 OPTIMIZATION OPPORTUNITIES:
1. High-frequency patterns detected in /task usage
2. Repeated context loading in /feature workflows
3. Suboptimal module loading sequence
4. Redundant quality checks in similar operations

🔧 RECOMMENDED IMPROVEMENTS:
- Implement task pattern caching (20% speed improvement)
- Optimize feature context management (15% efficiency gain)
- Streamline module loading order (10% faster startup)
- Create project-specific quality gate shortcuts

📋 COMPLIANCE ASSESSMENT:
✅ All commands follow framework standards
✅ Quality gates properly enforced
⚠️ Some modules could benefit from optimization
⚠️ Context management has room for improvement
```

### 2. Self-Optimization with `/meta-optimize`

**Usage:**
```bash
/meta-optimize "improve task command performance based on usage patterns"
```

**Expected Response:**
```
🚀 FRAMEWORK OPTIMIZATION INITIATED

🔍 PATTERN ANALYSIS:
- Detected: 89 /task commands in last 30 days
- Common patterns: Python function creation (34%), Bug fixes (28%), Test additions (22%)
- Context similarity: 67% overlap in codebase analysis
- Module usage: tdd.md (89%), task-management.md (89%), patterns/validation-pattern.md (71%)

💡 OPTIMIZATION STRATEGIES:
1. Create cached context snapshots for similar tasks
2. Pre-load frequently used modules
3. Implement intelligent context reuse
4. Optimize TDD workflow for your codebase

🔧 IMPLEMENTING OPTIMIZATIONS:

1. Context Caching Enhancement:
```xml
<context_cache>
  <python_functions>
    <cached_analysis>project_structure, import_patterns, test_conventions</cached_analysis>
    <reuse_threshold>80%</reuse_threshold>
    <expiration>24_hours</expiration>
  </python_functions>
</context_cache>
```

2. Module Pre-loading:
```xml
<module_preload>
  <high_frequency_modules>
    <module>system/quality/tdd.md</module>
    <module>development/task-management.md</module>
    <module>patterns/validation-pattern.md</module>
  </high_frequency_modules>
</module_preload>
```

3. TDD Workflow Optimization:
```xml
<tdd_optimization>
  <python_specific>
    <test_framework>pytest</test_framework>
    <naming_convention>test_function_name</naming_convention>
    <assertion_style>assert statements</assertion_style>
  </python_specific>
</tdd_optimization>
```

📈 EXPECTED IMPROVEMENTS:
- /task response time: 3.8s → 2.1s (45% improvement)
- Context loading: 1.2s → 0.4s (67% improvement)
- Module initialization: 0.8s → 0.3s (62% improvement)
- Overall efficiency: 73% → 89% (22% improvement)

✅ OPTIMIZATION APPLIED: Framework updated with performance improvements
```

### 3. Adaptive Learning with `/meta-evolve`

**Usage:**
```bash
/meta-evolve "adapt framework behavior based on our team's coding patterns"
```

**Expected Response:**
```
🧠 FRAMEWORK EVOLUTION ANALYSIS

📊 TEAM CODING PATTERNS DETECTED:
- Code style: Black formatter, 88 char line length
- Test preference: pytest with fixtures and parametrize
- Documentation: Google-style docstrings
- Error handling: Custom exception classes
- Architecture: Clean architecture with dependency injection

🔄 ADAPTIVE IMPROVEMENTS:

1. Code Generation Templates:
```python
# Evolved function template based on team patterns
def {function_name}(self, {parameters}) -> {return_type}:
    """
    {description}
    
    Args:
        {parameter_docs}
    
    Returns:
        {return_docs}
    
    Raises:
        {exception_docs}
    """
    try:
        # Implementation
        {implementation}
        return {return_value}
    except Exception as e:
        logger.error(f"Error in {function_name}: {e}")
        raise {CustomException}(f"Failed to {operation}: {e}")
```

2. Test Generation Templates:
```python
# Evolved test template based on team patterns
@pytest.fixture
def {fixture_name}():
    """Fixture for {description}"""
    return {fixture_value}

@pytest.mark.parametrize("{param_name}", [
    {test_cases}
])
def test_{function_name}_{test_aspect}({fixture_name}, {param_name}):
    """Test {function_name} {test_description}"""
    # Arrange
    {arrange_code}
    
    # Act
    result = {function_name}({parameters})
    
    # Assert
    assert {assertion}
```

3. Documentation Templates:
```python
# Evolved docstring template
class {ClassName}:
    """
    {class_description}
    
    This class implements {pattern} pattern and follows clean architecture
    principles with dependency injection.
    
    Attributes:
        {attribute_docs}
    
    Example:
        >>> {usage_example}
    """
```

🎯 BEHAVIORAL ADAPTATIONS:
- TDD workflow now uses pytest fixtures by default
- Error handling includes custom exception classes
- Code formatting follows team's 88-character limit
- Documentation uses Google-style docstrings
- Architecture suggestions include dependency injection

📈 LEARNING OUTCOMES:
- Framework now generates code matching team style
- Reduced manual formatting corrections by 85%
- Improved code review approval rate by 23%
- Decreased onboarding time for new team members by 40%

✅ EVOLUTION COMPLETE: Framework adapted to team preferences
```

### 4. Intelligent Governance with `/meta-govern`

**Usage:**
```bash
/meta-govern "ensure compliance with our project's quality standards"
```

**Expected Response:**
```
🛡️ GOVERNANCE COMPLIANCE ANALYSIS

📋 PROJECT QUALITY STANDARDS:
- Test coverage: 90% minimum (currently 87%)
- Code complexity: Max 10 (currently 12 in 3 files)
- Documentation: All public methods (currently 94%)
- Security: No high-severity issues (currently 2 issues)
- Performance: <200ms API response (currently 180ms avg)

🚨 COMPLIANCE VIOLATIONS DETECTED:
1. Test coverage below threshold in auth module (84%)
2. Cyclomatic complexity violation in user_service.py (complexity: 15)
3. Missing docstrings in 6 public methods
4. Security issue: hardcoded API key in config.py
5. Security issue: SQL injection vulnerability in search function

🔧 GOVERNANCE ENFORCEMENT:

1. Automated Quality Gates:
```xml
<quality_enforcement>
  <blocking_violations>
    <test_coverage_below>90</test_coverage_below>
    <complexity_above>10</complexity_above>
    <security_issues>high</security_issues>
  </blocking_violations>
  <warning_violations>
    <missing_docstrings>true</missing_docstrings>
    <performance_degradation>10_percent</performance_degradation>
  </warning_violations>
</quality_enforcement>
```

2. Compliance Monitoring:
```xml
<compliance_monitoring>
  <continuous_checks>
    <test_coverage>every_commit</test_coverage>
    <security_scan>daily</security_scan>
    <performance_test>every_deployment</performance_test>
  </continuous_checks>
</compliance_monitoring>
```

3. Remediation Guidance:
```bash
# Automated remediation suggestions
/task "increase test coverage in auth module to meet 90% threshold"
/task "refactor user_service.py to reduce complexity below 10"
/task "add docstrings to identified public methods"
/task "remove hardcoded API key and use environment variables"
/task "fix SQL injection vulnerability in search function"
```

📊 GOVERNANCE DASHBOARD:
- Quality score: 78/100 (target: 90+)
- Compliance violations: 5 (target: 0)
- Risk level: MEDIUM (target: LOW)
- Remediation time: 4 hours estimated

🎯 GOVERNANCE PLAN:
1. Immediate: Fix security vulnerabilities (2 hours)
2. Short-term: Increase test coverage (1 hour)
3. Medium-term: Refactor complex code (1 hour)
4. Ongoing: Monitor compliance continuously

✅ GOVERNANCE ACTIVE: Continuous monitoring enabled
```

### 5. Self-Diagnosis with `/meta-fix`

**Usage:**
```bash
/meta-fix "TDD workflow not being followed consistently"
```

**Expected Response:**
```
🔧 FRAMEWORK SELF-DIAGNOSIS

🔍 ISSUE ANALYSIS: TDD workflow not being followed consistently

📊 DIAGNOSTIC DATA:
- TDD compliance rate: 67% (target: 90%)
- Common pattern: Implementation before tests (23 instances)
- Bypassed RED phase: 31% of tasks
- Missing test coverage: 18% of new code
- Quality gate failures: 12% due to missing tests

🎯 ROOT CAUSE ANALYSIS:
1. Complex test setup discourages test-first approach
2. Unclear test requirements in user stories
3. Time pressure leading to shortcuts
4. Insufficient TDD training/awareness
5. Framework not enforcing TDD strictly enough

🚀 AUTOMATIC REMEDIATION:

1. Enhanced TDD Enforcement:
```xml
<tdd_enforcement upgrade="strict">
  <red_phase_validation>
    <require_failing_test>true</require_failing_test>
    <block_implementation>true</block_implementation>
    <validation_message>Write failing test first</validation_message>
  </red_phase_validation>
  
  <green_phase_validation>
    <require_passing_test>true</require_passing_test>
    <minimal_implementation>true</minimal_implementation>
    <validation_message>Implement minimal code to pass tests</validation_message>
  </green_phase_validation>
</tdd_enforcement>
```

2. Simplified Test Templates:
```python
# Auto-generated test template
def test_{function_name}_should_{expected_behavior}():
    """Test that {function_name} {expected_behavior}"""
    # Arrange
    {arrange_code}
    
    # Act & Assert
    with pytest.raises({ExpectedException}):
        {function_call}
```

3. TDD Guidance Integration:
```xml
<tdd_guidance>
  <red_phase_help>
    <message>Write a failing test that describes the expected behavior</message>
    <template>Provide test template based on function signature</template>
  </red_phase_help>
  
  <green_phase_help>
    <message>Implement minimal code to make the test pass</message>
    <template>Provide implementation skeleton</template>
  </green_phase_help>
</tdd_guidance>
```

📈 REMEDIATION RESULTS:
- TDD compliance improved from 67% to 94%
- Test-first violations reduced by 89%
- Quality gate failures due to missing tests: 12% → 2%
- Developer satisfaction with TDD process: +34%

✅ SELF-DIAGNOSIS COMPLETE: TDD workflow optimized and enforced
```

## Advanced Meta-Prompting Techniques

### 6. Continuous Learning Loop

**Setup continuous improvement:**
```bash
/meta-optimize "create learning loop for framework improvement"
```

**Implementation:**
```xml
<continuous_learning>
  <data_collection>
    <success_patterns>Track successful command patterns</success_patterns>
    <failure_analysis>Analyze failed attempts and errors</failure_analysis>
    <performance_metrics>Monitor response times and efficiency</performance_metrics>
  </data_collection>
  
  <learning_algorithms>
    <pattern_recognition>Identify recurring successful patterns</pattern_recognition>
    <optimization_suggestions>Suggest improvements based on data</optimization_suggestions>
    <adaptation_rules>Create adaptive behavior rules</adaptation_rules>
  </learning_algorithms>
  
  <feedback_loop>
    <weekly_analysis>Analyze collected data every week</weekly_analysis>
    <monthly_optimization>Apply optimizations monthly</monthly_optimization>
    <quarterly_evolution>Major adaptations quarterly</quarterly_evolution>
  </feedback_loop>
</continuous_learning>
```

### 7. Team-Specific Optimization

**Optimize for team collaboration:**
```bash
/meta-evolve "optimize framework for team collaboration and knowledge sharing"
```

**Team Adaptations:**
```xml
<team_optimization>
  <knowledge_sharing>
    <code_patterns>Share successful code patterns across team</code_patterns>
    <best_practices>Propagate best practices from senior developers</best_practices>
    <common_solutions>Build library of common solutions</common_solutions>
  </knowledge_sharing>
  
  <collaboration_features>
    <peer_review>Integrate code review suggestions</peer_review>
    <pair_programming>Support pair programming workflows</pair_programming>
    <documentation>Auto-generate team documentation</documentation>
  </collaboration_features>
</team_optimization>
```

## Key Benefits of Meta-Prompting

### ✅ Self-Improvement
- **Automatic Optimization**: Framework improves itself based on usage
- **Pattern Recognition**: Learns from successful interactions
- **Adaptive Behavior**: Adjusts to team and project needs
- **Continuous Learning**: Gets better over time

### ✅ Intelligent Governance
- **Compliance Monitoring**: Ensures quality standards are met
- **Automated Remediation**: Suggests fixes for violations
- **Risk Management**: Identifies and mitigates risks
- **Audit Trail**: Maintains compliance documentation

### ✅ Performance Enhancement
- **Bottleneck Identification**: Finds and fixes performance issues
- **Resource Optimization**: Efficient use of computational resources
- **Workflow Streamlining**: Eliminates redundant operations
- **Predictive Optimization**: Anticipates and prevents issues

## Best Practices for Meta-Prompting

### 1. Start Simple
- Begin with basic meta-review commands
- Gradually introduce more complex meta-operations
- Monitor impact of each optimization

### 2. Data-Driven Decisions
- Collect performance metrics before optimization
- Measure improvement after changes
- Use evidence-based optimization strategies

### 3. Incremental Improvement
- Make small, measurable improvements
- Test changes before full implementation
- Maintain rollback capabilities

### 4. Human Oversight
- Review meta-prompting suggestions
- Approve major framework changes
- Maintain human control over governance

This example demonstrates how meta-prompting enables the framework to become an intelligent, self-improving system that adapts to your specific needs while maintaining quality and compliance standards.