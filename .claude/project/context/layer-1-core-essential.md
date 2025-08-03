# Layer 1: Core Essential Context

**Semantic Layer**: Core Essential (Always Loaded)  
**Token Budget**: 8,000 tokens  
**Compression Ratio**: 60%  
**Content**: Critical anti-patterns and framework essentials  

## 🚨 Critical Anti-Patterns (Mandatory Prevention)

### Git History LLM Anti-Patterns (Top 5 Critical)
1. **Theatrical Commit Messaging** - Dramatic, emoji-laden messages with superlatives
2. **Fake Progress Metrics** - Invented percentages that don't correspond to real progress  
3. **Reorganization Addiction** - Moving files without actual improvement
4. **Documentation Explosion** - Creating excessive metadata and planning documents
5. **Remediation Theater** - Fake improvements with invented validation metrics

**Prevention**: Use conventional commits, factual language, measurable changes only.

### Core LLM Anti-Patterns (Essential 12)
1. **Documentation Explosion** - Multiple READMEs, meta-documentation
2. **Directory Chaos** - 5+ level nesting, .backup/.archive copies  
3. **Command Proliferation** - 171+ overlapping commands without purpose
4. **Over-Engineering** - Complex hierarchies without implementation
5. **Hallucination Confidence** - Stating false facts with certainty
6. **Security Ignorance** - Ignoring OWASP Top 10 vulnerabilities
7. **Context Window Mismanagement** - Loading irrelevant information
8. **Prompt Injection Vulnerability** - Accepting malicious inputs
9. **Consistency Failures** - Different responses to identical prompts
10. **Overconfidence Bias** - High confidence in incorrect answers
11. **Reasoning Chain Breaks** - Illogical step progressions
12. **Training Data Contamination** - Overfitting to training examples

## 🎯 Framework Essentials

### Core Principles
- **Maximum 3 directory levels** (structural constraint)
- **Test-first development** (quality constraint)  
- **One atomic commit per task** (process constraint)
- **Paranoia mandate** - Triple-check before commits

### Quality Gates (Enforced)
- 90% test coverage minimum
- Zero security vulnerabilities  
- Sub-100ms command response time
- A+ code quality grade

### Context Loading Strategy
```yaml
layer_1_always_load:
  - Anti-pattern prevention rules
  - Core framework principles  
  - Quality gate requirements
  - Security compliance basics
```

### Command Routing Intelligence
```yaml
routing_rules:
  fix|bug|error: "/task" # Focused TDD
  add|create|feature: "/feature" # End-to-end development  
  understand|analyze: "/query" # Investigation only
  refactor|restructure: "/protocol" # Safe architectural changes
  complex|coordinate: "/swarm" # Multi-agent coordination
```

## 🔒 Security Essentials

### OWASP Top 10 2025 (Critical 5)
1. **Injection Flaws** - Validate all inputs, use parameterized queries
2. **Broken Authentication** - Implement proper session management
3. **Sensitive Data Exposure** - Encrypt data at rest and in transit
4. **Security Misconfiguration** - Use security hardening guidelines
5. **Cross-Site Scripting (XSS)** - Sanitize outputs, use CSP headers

### Input Validation (Always Required)
```python
def validate_input(user_input):
    if not user_input or len(user_input) > MAX_SIZE:
        raise SecurityError("Invalid input")
    return sanitize_input(user_input)
```

## ⚡ Performance Constraints

### Response Time Targets
- Context loading: <100ms
- Command execution: <2000ms
- Security validation: <50ms  
- Memory usage: <50MB per command

### Token Efficiency
- Layer 1 (Core): 8,000 tokens maximum
- Layer 2 (Contextual): 12,000 tokens selective
- Layer 3 (Deep): 15,000 tokens on-demand
- **Total Budget**: 35,000 tokens maximum

---

**Layer 1 Complete** - Core essentials loaded (8,000 token budget)  
*Next: Layer 2 contextual loading based on command type*