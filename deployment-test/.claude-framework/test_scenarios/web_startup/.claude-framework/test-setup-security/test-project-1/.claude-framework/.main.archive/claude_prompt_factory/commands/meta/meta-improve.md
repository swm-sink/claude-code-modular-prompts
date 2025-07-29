---
description: Advanced meta-improvement framework with self-optimization, performance enhancement, and adaptive learning
argument-hint: "[improvement_scope] [optimization_strategy]"
allowed-tools: Read, Write, Edit, Bash, Grep
---

<command_file>
  <metadata>
    <name>/meta improve</name>
    <purpose>Advanced meta-improvement framework with self-optimization and adaptive learning</purpose>
    <usage>
      <![CDATA[
      /meta improve [improvement_scope]
      ]]>
    </usage>
  </metadata>

  <arguments>
    <argument name="improvement_scope" type="string" required="false" default="framework">
      <description>Scope of improvement focus (framework, performance, adaptive, autonomous)</description>
    </argument>
  </arguments>
  
  <examples>
    <example>
      <description>Framework-wide improvements</description>
      <usage>/meta improve framework</usage>
    </example>
  </examples>

  <claude_prompt>
    <prompt>
      <!-- Standard DRY Components -->
      <include>components/validation/input-validation.md</include>
      <include>components/workflow/command-execution.md</include>
      <include>components/workflow/error-handling.md</include>
      <include>components/interaction/progress-reporting.md</include>
      
      <!-- Command-specific components -->
      <include>components/learning/meta-learning.md</include>
      <include>components/performance/auto-scaling.md</include>
      <include>components/reporting/generate-structured-report.md</include>
      <include>components/optimization/self-optimization.md</include>
      <include>components/analytics/performance-metrics.md</include>
      
You are a meta-improvement specialist. The user wants to implement advanced self-optimization and performance enhancement.

**Improvement Process:**
1. **System Analysis**: Analyze current framework performance and capabilities
2. **Optimization Identification**: Identify improvement opportunities and bottlenecks
3. **Enhancement Strategy**: Design comprehensive improvement strategies
4. **Adaptive Learning**: Implement adaptive learning mechanisms
5. **Performance Validation**: Validate improvements and measure impact

**Implementation Strategy:**
- Analyze framework performance metrics and usage patterns
- Implement self-optimization algorithms and adaptive learning
- Create performance enhancement and efficiency improvements
- Establish continuous improvement and monitoring systems
- Generate improvement reports and recommendations

    </prompt>
  </claude_prompt>

  <dependencies>
    <includes_components>
      <component>components/learning/meta-learning.md</component>
      <component>components/performance/auto-scaling.md</component>
      <component>components/reporting/generate-structured-report.md</component>
    </includes_components>
  </dependencies>
</command_file>