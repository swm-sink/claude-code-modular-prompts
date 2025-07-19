# Init-Research Command - Analyze existing project before setup

**Description**: Analyze existing project before setup

────────────────────────────────────────────────────────────────────────────────

| version | last_updated | status | readiness |
|---------|--------------|--------|-----------|
| 3.0.0   | 2025-07-12   | stable | 95%       |

────────────────────────────────────────────────────────────────────────────────


────────────────────────────────────────────────────────────────────────────────

```xml
<command name="init-research" category="initialization" enforcement="BLOCKING">
  
  <purpose>
    Research-driven framework configuration with atomic commits safety, evidence-based best practices, and comprehensive domain optimization with Claude 4 enhancement.
  </purpose>
  
  <scope>
    <includes>Domain research, best practices analysis, evidence-based configuration, cutting-edge technique integration</includes>
    <excludes>Manual configuration, outdated practices, assumption-based setup</excludes>
    <boundaries>All research must be from 2025 sources with atomic commits for instant rollback</boundaries>
  </scope>
  
  <input_specification>
    <required_arguments>Domain/industry type, technology stack, project scale and complexity</required_arguments>
    <context_requirements>Research access, project context, quality standards requirements</context_requirements>
    <preconditions>Internet access for research, valid project directory, git repository available</preconditions>
  </input_specification>
  
  <output_specification>
    <deliverables>Research-backed PROJECT_CONFIG.xml, best practices documentation, source citations, atomic commit trail</deliverables>
    <success_criteria>Comprehensive research completed, evidence-based configuration generated, rollback capability established</success_criteria>
    <artifacts>PROJECT_CONFIG.xml, research report, source citations, configuration justification, atomic commit history</artifacts>
  </output_specification>
</command>
```

Research-driven framework configuration with atomic commits safety.

## Thinking Pattern - Claude 4 Enhanced

```xml
<thinking_pattern enforcement="MANDATORY">
  
  <checkpoint id="1" verify="true" enforcement="BLOCKING" thinking_mode="interleaved">
    <action>Pre-Research Atomic Commit: Create secure rollback point before research and configuration</action>
    <interleaved_thinking enforcement="MANDATORY">
      <pre_analysis>
        - What is the current state that must be preserved before research begins?
        - What research-driven changes will be made that need rollback capability?
        - How can we ensure instant recovery if research leads to incorrect configuration?
      </pre_analysis>
      <critical_thinking minimum_time="30_seconds">
        - [Safety Question: Is the current state safely preserved before research-driven changes?]
        - [Research Question: What evidence-based research approach will be most effective?]
        - [Recovery Question: Can we rollback if research findings prove inadequate?]
      </critical_thinking>
    </interleaved_thinking>
    <atomic_commit enforcement="MANDATORY">
      <pre_operation>git add -A && git commit -m "PRE-OP: init-research - backup state before research-driven configuration"</pre_operation>
      <validation>Research baseline established for instant rollback</validation>
      <rollback_capability>Available via: git reset --hard HEAD~1</rollback_capability>
    </atomic_commit>
  </checkpoint>
  
  <checkpoint id="2" verify="true" enforcement="BLOCKING" thinking_mode="research">
    <action>Comprehensive Domain Research: Evidence-based research of current best practices and standards</action>
    <interleaved_thinking enforcement="MANDATORY">
      <research_scope>
        - What are the current 2025 best practices for this domain and tech stack?
        - What industry standards and proven patterns should be applied?
        - What cutting-edge techniques are being adopted in leading organizations?
        - What quality standards and security requirements are current?
      </research_scope>
      <critical_thinking minimum_time="60_seconds">
        - [Evidence Question: Are research sources current and authoritative (2025 only)?]
        - [Completeness Question: Is research comprehensive across all relevant areas?]
        - [Quality Question: Do findings represent proven best practices vs experimental approaches?]
      </critical_thinking>
    </interleaved_thinking>
    <module_delegation enforcement="MANDATORY">
      <research_modules>
        <module>development/domain-research-analyzer.md</module>
        <module>patterns/best-practices-discovery.md</module>
        <module>patterns/technology-stack-optimization.md</module>
      </research_modules>
    </module_delegation>
  </checkpoint>
  
  <checkpoint id="3" verify="true" enforcement="BLOCKING" thinking_mode="interleaved">
    <action>Evidence-Based Configuration Synthesis: Transform research findings into optimal framework configuration</action>
    <interleaved_thinking enforcement="MANDATORY">
      <synthesis_process>
        - How should research findings be translated into specific configuration settings?
        - What proven patterns should be implemented in the framework setup?
        - How should quality thresholds be set based on industry standards?
        - What domain-specific optimizations should be applied?
      </synthesis_process>
      <critical_thinking minimum_time="45_seconds">
        - [Translation Question: Are research findings properly translated into actionable configuration?]
        - [Evidence Question: Is each configuration choice backed by research evidence?]
        - [Optimization Question: Does the configuration represent optimal setup for this domain?]
      </critical_thinking>
    </interleaved_thinking>
    <atomic_commit enforcement="MANDATORY">
      <operation_execution>git add PROJECT_CONFIG.xml research-report.md && git commit -m "OP-EXEC: init-research configuration - evidence-based PROJECT_CONFIG.xml with research backing"</operation_execution>
      <validation>Configuration generated with comprehensive research backing</validation>
      <rollback_trigger>Configuration errors trigger: git reset --hard HEAD~1</rollback_trigger>
    </atomic_commit>
  </checkpoint>
  
  <checkpoint id="4" verify="true" enforcement="BLOCKING" thinking_mode="interleaved">
    <action>Research-Driven Setup Validation: Comprehensive validation of research-backed configuration</action>
    <interleaved_thinking enforcement="MANDATORY">
      <validation_scope>
        - Does the configuration accurately reflect research findings?
        - Are all research-backed recommendations properly implemented?
        - Is the setup optimized for current industry best practices?
        - Are sources properly documented for future reference?
      </validation_scope>
      <critical_thinking minimum_time="30_seconds">
        - [Accuracy Question: Does the final configuration accurately implement research findings?]
        - [Completeness Question: Are all research recommendations addressed in the setup?]
        - [Documentation Question: Are research sources properly cited for future validation?]
      </critical_thinking>
    </interleaved_thinking>
    <atomic_commit enforcement="MANDATORY">
      <post_operation>git add -A && git commit -m "POST-OP: init-research complete - research-driven configuration validated with source documentation"</post_operation>
      <validation>Research-backed setup validated and atomic commit trail established</validation>
      <rollback_trigger>Validation failure triggers: git reset --hard HEAD~2 (return to pre-research)</rollback_trigger>
    </atomic_commit>
  </checkpoint>
  
</thinking_pattern>
```

## What It Does

This command researches and applies the latest best practices:

1. **Domain Research**
   - Searches for current best practices in your domain
   - Identifies industry standards and patterns
   - Discovers recommended tools and workflows
   - Finds proven architectural approaches

2. **Evidence-Based Configuration**
   - Applies research findings to framework setup
   - Configures based on 2025 best practices
   - Implements recommended quality standards
   - Sets up optimal development workflows

3. **Custom Optimization**
   - Tailors framework to your specific needs
   - Incorporates cutting-edge techniques
   - Optimizes for your domain requirements
   - Ensures future-proof configuration

## Research Process

I'll conduct research on:

1. **Industry Best Practices**
   - "{domain} best practices 2025"
   - "{tech-stack} development patterns"
   - "{domain} quality standards"
   - "{framework} optimization techniques"

2. **Architecture Patterns**
   - Scalability approaches for your domain
   - Security requirements and standards
   - Performance optimization strategies
   - Testing methodologies

3. **Tool Ecosystems**
   - Recommended development tools
   - CI/CD best practices
   - Monitoring and observability
   - Developer experience optimization

## Example Research Areas

**For Web Development:**
- React/Vue/Angular best practices
- Performance optimization techniques
- Accessibility standards (WCAG 3.0)
- Security headers and CSP policies

**For Data Science:**
- MLOps best practices
- Reproducibility standards
- Model validation approaches
- Data pipeline patterns

**For Mobile Development:**
- Platform-specific guidelines
- Performance optimization
- Battery efficiency patterns
- App store requirements

## Configuration Output

Based on research, I'll generate:
- PROJECT_CONFIG.xml with researched settings
- Documentation of applied best practices
- Links to authoritative sources
- Recommendations for further optimization

## Benefits

- **Evidence-Based** - Configuration backed by research
- **Current Standards** - 2025 best practices applied
- **Domain Expertise** - Specialized for your field
- **Future-Proof** - Latest techniques and patterns

## Process Flow

1. Identify your domain and tech stack
2. Research current best practices
3. Analyze findings and patterns
4. Generate optimized configuration
5. Document sources and rationale

## Related Commands

- `/init-custom` - For existing projects
- `/init-new` - Interactive setup wizard
- `/init-validate` - Validate configuration

$ARGUMENTS