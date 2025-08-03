# Prompt Engineering Best Practices

*The positive counterpart to anti-patterns - showing the right way to do prompt engineering*

## Table of Contents
1. [Core Principles](#core-principles)
2. [Clarity and Specificity](#clarity-and-specificity)
3. [Context Management](#context-management)
4. [Modularity and Reusability](#modularity-and-reusability)
5. [Testing and Validation](#testing-and-validation)
6. [Security and Safety](#security-and-safety)
7. [Performance Optimization](#performance-optimization)
8. [Quality Assurance](#quality-assurance)
9. [Success Measurement](#success-measurement)
10. [Advanced Techniques](#advanced-techniques)

---

## Core Principles

### 1. Simplicity Over Complexity
**✅ DO:**
- Maximum 3 levels of directory nesting
- One clear purpose per command
- Atomic, focused functionality
- Direct, unambiguous language

**Example:**
```markdown
---
name: /analyze-code
description: Analyzes code for security vulnerabilities
usage: /analyze-code [file-path]
tests: tests/unit/test_analyze_code.py
---
```

**❌ AVOID:**
- Nested command hierarchies
- Multi-purpose commands that "do everything"
- Vague or abstract descriptions

### 2. Implementation Over Documentation
**✅ DO:**
- 1:5 documentation-to-code ratio maximum
- Working code before extensive docs
- Test-driven development approach
- Practical examples over theoretical explanations

**Measurement:** If documentation exceeds 20% of total project files, simplify.

### 3. Quality Over Quantity
**✅ DO:**
- 50-70 curated, tested commands
- Each command serves unique purpose
- High reliability and performance
- Comprehensive test coverage

**❌ AVOID:**
- 150+ commands with overlap
- Untested implementations
- Duplicate functionality

---

## Clarity and Specificity

### 4. Precise Instruction Design

**✅ EXCELLENT:**
```
Analyze the security vulnerabilities in the provided JavaScript code, focusing on:
1. XSS injection points
2. Authentication bypasses  
3. Data validation gaps
Return findings in JSON format with line numbers and severity levels.
```

**❌ POOR:**
```
Help me with my code security
```

### 5. Structured Input Patterns

**✅ Template Pattern:**
```markdown
**Task:** [Specific action]
**Context:** [Essential background only]
**Constraints:** [Clear limitations]
**Output Format:** [Exact specification]
**Success Criteria:** [Measurable outcomes]
```

**Example Implementation:**
```markdown
**Task:** Extract API endpoints from Express.js route files
**Context:** Node.js REST API with authentication middleware
**Constraints:** Only GET and POST routes, ignore middleware-only files
**Output Format:** JSON array with {method, path, handler} objects
**Success Criteria:** 100% endpoint coverage, valid JSON output
```

### 6. Contextual Boundaries

**✅ Essential Context Only:**
- Current task requirements
- Relevant architectural constraints
- Specific technical requirements
- Direct dependencies only

**❌ Context Pollution:**
- Historical project decisions
- Unrelated system components
- Excessive background information
- Multiple unrelated examples

---

## Context Management

### 7. Hierarchical Context Loading

**✅ Optimal Loading Order:**
```markdown
1. Core principles (this file)
2. Task-specific context
3. Technical constraints
4. Examples (if needed)
5. Anti-patterns (for reference)
```

**✅ Context Window Optimization:**
- Load only essential information
- Use progressive disclosure
- Cache frequently accessed patterns
- Monitor context utilization (<5% waste)

### 8. Dynamic Context Adaptation

**✅ Context Selection Strategy:**
```python
def select_context(task_type, complexity_level):
    base_context = load_core_principles()
    
    if task_type == "security":
        context += load_security_patterns()
    elif task_type == "performance":
        context += load_performance_patterns()
    
    if complexity_level > 3:
        context += load_advanced_techniques()
    
    return optimize_context_window(context)
```

### 9. Context Validation

**✅ Pre-execution Checks:**
- Verify context relevance (>80% applicable)
- Check context freshness (<30 days old)
- Validate cross-references
- Ensure no contradictory guidance

---

## Modularity and Reusability

### 10. Component-Based Architecture

**✅ Modular Command Structure:**
```
.claude/
├── components/           # Reusable prompt components
│   ├── security/        # Security-focused prompts
│   ├── analysis/        # Code analysis prompts
│   └── testing/         # Test generation prompts
├── commands/            # Specific implementations
└── templates/           # Base templates
```

### 11. Template Standardization

**✅ Command Template:**
```markdown
---
name: /[command-name]
description: [One-line purpose]
category: [core|development|security|testing|analysis|utilities]
tools: [List of required tools]
dependencies: [Other commands this relies on]
tests: tests/unit/test_[command_name].py
performance_target: <100ms
security_level: [low|medium|high]
---

# [Command Name]

## Purpose
[2-3 sentence description]

## Usage
```
/[command-name] [arguments]
```

## Implementation
[Core logic here]

## Validation
[Success criteria and error handling]
```

### 12. Component Composition

**✅ Reusable Components:**
```markdown
# Security validation component
@component security_validation
- Input sanitization
- Output validation  
- Permission verification
- Audit logging

# Performance monitoring component
@component performance_monitoring
- Execution timing
- Memory usage tracking
- Response time validation
- Bottleneck identification
```

---

## Testing and Validation

### 13. Test-Driven Development (TDD)

**✅ Mandatory TDD Process:**

**Phase 1: RED (Write Failing Test)**
```python
def test_security_analysis():
    """Test must fail initially - no implementation exists"""
    result = execute_command("/analyze-security", "sample_code.js")
    assert result.success == True
    assert result.vulnerabilities_found >= 0
    assert result.performance_ms < 100
    assert result.output_format == "json"
```

**Phase 2: GREEN (Minimal Implementation)**
```markdown
---
name: /analyze-security
description: Analyzes code for security vulnerabilities
tests: tests/unit/test_analyze_security.py
---

# Implementation that makes test pass
```

**Phase 3: REFACTOR (Improve with Safety Net)**
```python
def test_security_analysis_comprehensive():
    """Enhanced tests for refactored implementation"""
    # All previous tests must still pass
    # Additional tests for improved functionality
```

### 14. Comprehensive Test Coverage

**✅ Required Test Categories:**

**Unit Tests:**
```python
def test_command_functionality():
    """Core functionality validation"""
    # Input validation
    # Output format verification
    # Error handling
    # Edge case coverage
```

**Security Tests:**
```python
def test_command_security():
    """Security validation - mandatory"""
    # Input sanitization
    # Output validation
    # Permission checks
    # Vulnerability scanning
```

**Performance Tests:**
```python
def test_command_performance():
    """Performance benchmarking - <100ms required"""
    start_time = time.time()
    result = execute_command()
    execution_time = (time.time() - start_time) * 1000
    assert execution_time < 100  # Hard limit
```

**Integration Tests:**
```python
def test_command_integration():
    """Claude Code integration validation"""
    # Tool interaction
    # Context loading
    # Memory management
    # Error propagation
```

### 15. Quality Gates

**✅ Pre-commit Requirements:**
```bash
# All must pass before commit
pytest --cov=. --cov-fail-under=90     # Test coverage
bandit -r . --severity-level medium    # Security scan
performance-test --max-time=100ms      # Performance validation
integration-test --claude-code         # Integration check
```

---

## Security and Safety

### 16. Defensive Security Patterns

**✅ Input Validation:**
```python
def validate_input(user_input):
    """Mandatory input validation"""
    if not user_input:
        raise SecurityError("Empty input not allowed")
    
    if len(user_input) > MAX_INPUT_SIZE:
        raise SecurityError(f"Input exceeds {MAX_INPUT_SIZE} characters")
    
    # Sanitize against injection attacks
    sanitized = html.escape(user_input)
    sanitized = sanitized.replace(";", "").replace("--", "")
    
    return sanitized
```

**✅ Output Sanitization:**
```python
def sanitize_output(output):
    """Mandatory output sanitization"""
    # Remove sensitive information
    output = re.sub(r'api[_-]?key\s*[:=]\s*[^\s]+', 'api_key=***', output, flags=re.IGNORECASE)
    output = re.sub(r'password\s*[:=]\s*[^\s]+', 'password=***', output, flags=re.IGNORECASE)
    
    # Validate output format
    if not is_valid_format(output):
        raise SecurityError("Output format validation failed")
    
    return output
```

### 17. Permission Management

**✅ Least Privilege Principle:**
```json
{
  "tool_permissions": {
    "read": ["*.md", "*.json", "*.py"],
    "write": ["tests/*", "docs/*"],
    "execute": ["pytest", "bandit", "performance-test"],
    "denied": ["rm", "sudo", "chmod +x"]
  }
}
```

### 18. Audit and Monitoring

**✅ Security Monitoring:**
```python
@security_monitor
def execute_command(command, args):
    """Execute with comprehensive security logging"""
    audit_log.info(f"Command execution: {command} with args: {sanitize_args(args)}")
    
    try:
        result = command_executor(command, args)
        audit_log.info(f"Command success: {command}")
        return result
    except Exception as e:
        audit_log.error(f"Command failure: {command}, error: {str(e)}")
        raise
```

---

## Performance Optimization

### 19. Response Time Requirements

**✅ Performance Targets:**
- Command execution: <100ms (hard limit)
- Context loading: <50ms
- Memory usage: <50MB per command
- Context window utilization: >95%

**✅ Performance Monitoring:**
```python
@performance_test(max_time=100, max_memory=50)
def test_command_performance():
    """Automatic performance validation"""
    with performance_monitor() as monitor:
        result = execute_command()
        assert monitor.response_time < 100
        assert monitor.memory_usage < 50
        assert monitor.context_efficiency > 0.95
```

### 20. Optimization Strategies

**✅ Context Caching:**
```python
@lru_cache(maxsize=128)
def load_context(context_type):
    """Cache frequently accessed context"""
    return load_context_from_file(context_type)
```

**✅ Lazy Loading:**
```python
def load_command_context(command_name):
    """Load only essential context initially"""
    core_context = load_core_context()
    
    # Load additional context only if needed
    if requires_security_context(command_name):
        core_context.extend(load_security_context())
    
    return core_context
```

### 21. Memory Management

**✅ Efficient Context Loading:**
```python
def optimize_context_window(contexts):
    """Optimize context for efficiency"""
    # Remove redundant information
    deduplicated = remove_duplicates(contexts)
    
    # Prioritize by relevance
    prioritized = sort_by_relevance(deduplicated)
    
    # Trim to fit context window
    optimized = trim_to_window_size(prioritized)
    
    return optimized
```

---

## Quality Assurance

### 22. Iterative Refinement

**✅ Continuous Improvement Process:**
```python
def iterative_prompt_refinement(initial_prompt):
    """Systematic prompt improvement"""
    prompt = initial_prompt
    
    for iteration in range(MAX_ITERATIONS):
        # Test current prompt
        results = test_prompt(prompt)
        
        # Analyze performance
        performance = analyze_results(results)
        
        # If satisfactory, stop
        if performance.meets_criteria():
            break
            
        # Refine based on feedback
        prompt = refine_prompt(prompt, performance.feedback)
    
    return prompt
```

### 23. Cross-Validation

**✅ Multi-Model Testing:**
```python
def cross_validate_prompt(prompt, test_cases):
    """Test prompt across different models"""
    results = {}
    
    for model in ["claude-3", "gpt-4", "local-model"]:
        model_results = []
        for test_case in test_cases:
            result = execute_prompt(prompt, test_case, model)
            model_results.append(result)
        
        results[model] = analyze_consistency(model_results)
    
    return results
```

### 24. Performance Metrics

**✅ Comprehensive Measurement:**
```python
class PromptMetrics:
    def __init__(self):
        self.accuracy = 0.0
        self.consistency = 0.0
        self.response_time = 0.0
        self.resource_usage = 0.0
        self.user_satisfaction = 0.0
    
    def calculate_overall_score(self):
        """Weighted score calculation"""
        return (
            self.accuracy * 0.3 +
            self.consistency * 0.2 +
            (1 - self.response_time / 100) * 0.2 +  # Normalized to 100ms
            (1 - self.resource_usage / 50) * 0.1 +   # Normalized to 50MB
            self.user_satisfaction * 0.2
        )
```

---

## Success Measurement

### 25. Key Performance Indicators (KPIs)

**✅ Quality Metrics (Enforced):**
- Test coverage: ≥90%
- Security vulnerabilities: 0
- Performance: <100ms response time
- Code quality: A+ grade
- Documentation coverage: 100%

**✅ User Experience Metrics:**
- Task completion rate: >95%
- User satisfaction score: >9/10
- Error rate: <1%
- Support ticket volume: <5% of usage

### 26. Automated Monitoring

**✅ Real-time Quality Dashboard:**
```yaml
metrics:
  test_coverage: 90%+
  security_vulnerabilities: 0
  performance_baseline: <100ms
  command_count: 50-70 (curated)
  documentation_completeness: 100%
  user_satisfaction: 9/10+
  uptime: 99.9%+
  error_rate: <1%
```

### 27. Continuous Feedback Loop

**✅ Improvement Process:**
```python
def continuous_improvement():
    """Automated improvement cycle"""
    # Collect metrics
    metrics = collect_performance_metrics()
    
    # Identify improvement opportunities
    opportunities = analyze_metrics(metrics)
    
    # Prioritize by impact
    prioritized = prioritize_improvements(opportunities)
    
    # Implement improvements
    for improvement in prioritized[:3]:  # Top 3 priorities
        implement_improvement(improvement)
        
    # Measure impact
    new_metrics = collect_performance_metrics()
    impact = calculate_improvement_impact(metrics, new_metrics)
    
    # Log results
    log_improvement_results(improvement, impact)
```

---

## Advanced Techniques

### 28. Chain-of-Thought (CoT) Prompting

**✅ Structured Reasoning:**
```markdown
**Task:** Analyze security vulnerability

**Step 1:** Identify potential entry points
- User input fields
- API endpoints
- File upload functionality

**Step 2:** Trace data flow
- Input validation points
- Data transformation steps
- Output generation

**Step 3:** Evaluate security controls
- Authentication mechanisms
- Authorization checks
- Input sanitization

**Conclusion:** [Security assessment based on analysis]
```

### 29. Self-Consistency Validation

**✅ Multi-Pass Verification:**
```python
def self_consistency_check(prompt, test_case, iterations=5):
    """Verify consistency across multiple runs"""
    results = []
    
    for i in range(iterations):
        result = execute_prompt(prompt, test_case)
        results.append(result)
    
    # Calculate consistency score
    consistency = calculate_consistency(results)
    
    if consistency < 0.8:  # 80% consistency threshold
        raise ValidationError("Prompt lacks consistency")
    
    return most_common_result(results)
```

### 30. Retrieval-Augmented Generation (RAG)

**✅ Grounded Responses:**
```python
def rag_prompt_execution(query, knowledge_base):
    """Execute prompt with external knowledge grounding"""
    # Retrieve relevant context
    relevant_docs = knowledge_base.retrieve(query, top_k=5)
    
    # Construct grounded prompt
    grounded_prompt = f"""
    Based on the following verified information:
    {format_retrieved_docs(relevant_docs)}
    
    Answer the following query:
    {query}
    
    Provide citations for all factual claims.
    """
    
    return execute_prompt(grounded_prompt)
```

### 31. Step-Back Prompting

**✅ High-Level Reasoning First:**
```markdown
**High-Level Question:** What are the fundamental principles of secure code analysis?

**Answer:** 
1. Input validation and sanitization
2. Output encoding and validation
3. Authentication and authorization
4. Secure data handling
5. Error handling and logging

**Specific Question:** How do I check for XSS vulnerabilities in this JavaScript code?

**Answer:** [Detailed analysis based on fundamental principles]
```

---

## Implementation Guidelines

### 32. Development Workflow

**✅ Systematic Approach:**
```bash
# 1. Analysis Phase
- Document command purpose
- Define input/output specifications
- Identify security considerations
- Plan performance requirements

# 2. Test-First Implementation
- Write failing unit tests
- Write security validation tests
- Write performance benchmark tests
- Write integration tests

# 3. Minimal Implementation
- Implement core functionality
- Ensure all tests pass
- Validate security requirements
- Confirm performance benchmarks

# 4. Quality Validation
- Run full test suite (90%+ coverage)
- Security audit (zero vulnerabilities)
- Performance validation (<100ms)
- Integration testing

# 5. Documentation and Review
- Update documentation
- Code review (mandatory)
- Final validation
- Atomic commit with tests
```

### 33. Error Handling Patterns

**✅ Graceful Degradation:**
```python
def robust_command_execution(command, args):
    """Execute command with comprehensive error handling"""
    try:
        # Validate inputs
        validated_args = validate_inputs(args)
        
        # Execute with timeout
        result = execute_with_timeout(command, validated_args, timeout=100)
        
        # Validate outputs
        validated_result = validate_outputs(result)
        
        return validated_result
        
    except ValidationError as e:
        log_error(f"Validation failed: {e}")
        return create_error_response("VALIDATION_ERROR", str(e))
        
    except TimeoutError as e:
        log_error(f"Command timeout: {e}")
        return create_error_response("TIMEOUT_ERROR", "Command execution exceeded time limit")
        
    except SecurityError as e:
        log_security_incident(f"Security violation: {e}")
        return create_error_response("SECURITY_ERROR", "Security validation failed")
        
    except Exception as e:
        log_error(f"Unexpected error: {e}")
        return create_error_response("INTERNAL_ERROR", "An unexpected error occurred")
```

### 34. Documentation Standards

**✅ Comprehensive Documentation:**
```markdown
# Command Documentation Template

## Purpose
[Brief description of command functionality]

## Usage
```
/command-name [arguments]
```

## Performance Metrics
- Response time: <100ms
- Memory usage: <50MB
- Test coverage: >90%
- Security level: [low|medium|high]

## Security Considerations
- Input validation: [describe approach]
- Output sanitization: [describe measures]
- Permission requirements: [list requirements]

## Testing
- Unit tests: `tests/unit/test_command_name.py`
- Security tests: `tests/security/test_command_name_security.py`
- Performance tests: `tests/performance/test_command_name_perf.py`
- Integration tests: `tests/integration/test_command_name_integration.py`

## Examples
[Practical usage examples with expected outputs]

## Error Handling
[Common error scenarios and responses]
```

---

## Factual Documentation Practices

### 34. Document What Is, Not What Impresses

**✅ Core Principle:** Documentation should reflect reality, not aspirations or theater.

**DO:**
- State concrete changes: "Consolidated 67 commands into 34"
- Use metrics only when measured: "Test file count: 127"
- Acknowledge limitations: "Functional testing not performed"
- Use neutral language: "Updated", "Modified", "Implemented"
- Report actual counts: "Processed 47 files" (if counted)
- Label estimates clearly: "Estimated 50-70 commands"

**DON'T:**
- Invent metrics: "87.3% improvement" (unless measured)
- Use theatrical language: "Revolutionary", "Exceptional", "Groundbreaking"
- Claim unverifiable success: "Optimal performance achieved"
- Create fake validation: Scripts that test nothing
- Cite specific percentages without data
- Use superlatives without evidence

**Example - Bad:**
```markdown
"Achieved exceptional 91.3% enhancement in system performance through revolutionary optimization delivering groundbreaking improvements with comprehensive validation suite confirming transformational success."
```

**Example - Good:**
```markdown
"Refactored data processing logic. Modified 12 files. Performance impact not measured. Structural validation completed; functional testing requires manual execution."
```

### 35. Metrics Guidelines

**✅ When to Use Numbers:**

1. **Counted Items**: "Processed 47 files", "34 commands remain"
2. **Measured Values**: "Response time: 87ms" (with benchmark)
3. **Verified Coverage**: "Test coverage: 72%" (from coverage tool)
4. **Actual Errors**: "Fixed 12 linting errors"

**✅ When NOT to Use Numbers:**

1. **Unmeasured Performance**: Avoid "3x faster" without benchmarks
2. **Subjective Quality**: No "91% quality improvement"
3. **User Experience**: No metrics without user data
4. **Complexity Reduction**: No percentages without measurement tools

**✅ Honest Reporting Template:**

```markdown
## Changes Made
- Action: [What was done]
- Files Modified: [Actual count]
- Tests: [What type, if any]
- Metrics: [Only if measured]
- Limitations: [What wasn't done]
- Next Steps: [If applicable]
```

### 36. Validation Honesty

**✅ Structural vs Functional:**

**Structural Validation (Can be automated):**
- File existence checks
- Syntax validation
- Import verification
- Directory structure
- Pattern matching

**Functional Validation (Requires execution):**
- Command behavior
- Performance benchmarks
- Integration testing
- User acceptance
- Error handling

**✅ Accurate Validation Reporting:**

```python
# GOOD: Honest about what's being tested
def validate_structure():
    """Verify file structure only - not functionality"""
    print("Checking file existence...")
    # Only structural checks
    
# BAD: Claims more than it does
def validate_everything():
    """Comprehensive validation suite"""
    print("✅ 100% VALIDATION SUCCESS")  # Misleading
```

---

## Conclusion

Effective prompt engineering requires systematic application of proven techniques, continuous measurement, and iterative improvement. Success depends on:

1. **Clear, specific instructions** that eliminate ambiguity
2. **Comprehensive testing** at all levels (unit, security, performance, integration)
3. **Modular, reusable components** that promote consistency
4. **Robust security measures** implemented throughout
5. **Performance optimization** with measurable targets
6. **Continuous quality assurance** with automated monitoring

**Remember:** Great prompts are engineered, not discovered. Apply these practices systematically, measure results rigorously, and improve continuously.

---

## Success Criteria Checklist

- [ ] Command serves single, clear purpose
- [ ] Implementation matches documentation exactly
- [ ] All four test categories implemented and passing
- [ ] Security validation comprehensive and thorough
- [ ] Performance meets <100ms requirement
- [ ] Context loading optimized (<5% waste)
- [ ] Error handling covers all scenarios
- [ ] Documentation complete and accurate
- [ ] Quality gates all pass automatically
- [ ] User satisfaction >9/10

**When all criteria are met, the prompt engineering implementation is complete.**

---

*Generated: 2025-07-25*  
*Strategy: Evidence-based best practices*  
*Quality Standard: Production-ready*  
*Measurement: Continuous validation*