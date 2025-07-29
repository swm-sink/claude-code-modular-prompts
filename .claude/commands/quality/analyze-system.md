---
name: /analyze-system
description: "Comprehensive system analysis with performance profiling, dependency analysis, cost optimization, and quality assessments"
usage: "[focus_mode] [analysis_depth] [target_path]"
tools: Read, Write, Edit, Bash, Grep
---
# /analyze-system - Unified System Analysis Framework for [INSERT_PROJECT_NAME]

Comprehensive system-level analysis for [INSERT_TECH_STACK] applications, combining performance profiling, dependency management, cost optimization, and quality assessments in a single unified command tailored for [INSERT_DOMAIN] systems on [INSERT_CLOUD_PROVIDER].

## Usage
```bash
/analyze-system                                 # Comprehensive analysis of entire system
/analyze-system performance                     # Focus on performance bottlenecks
/analyze-system dependencies                    # Focus on dependency analysis and compatibility
/analyze-system cost                           # Focus on cost optimization
/analyze-system performance --deep             # Deep performance analysis with profiling
/analyze-system dependencies --compatibility   # Compatibility-focused dependency analysis
/analyze-system cost --optimization           # Cost optimization recommendations
```

<command_file>
  <metadata>
    <name>/analyze-system</name>
    <purpose>Comprehensive system analysis combining performance profiling, dependency analysis, cost optimization, and quality assessments</purpose>
    <usage>
      <![CDATA[
      /analyze-system [focus_mode] [analysis_depth] [target_path]
      ]]>
    </usage>
  </metadata>
  <arguments>
    <argument name="focus_mode" type="string" required="false" default="comprehensive">
      <description>Analysis focus: comprehensive|performance|dependencies|cost|quality</description>
    </argument>
    <argument name="analysis_depth" type="string" required="false" default="standard">
      <description>Analysis depth: shallow|standard|deep|exhaustive</description>
    </argument>
    <argument name="target_path" type="string" required="false" default=".">
      <description>Target path for analysis (defaults to current directory)</description>
    </argument>
    <argument name="cloud_provider" type="string" required="false" default="[INSERT_CLOUD_PROVIDER]">
      <description>Cloud provider for cost analysis: [INSERT_CLOUD_PROVIDER] preferred, aws|gcp|azure supported</description>
    </argument>
    <argument name="time_period" type="string" required="false" default="last_30_days">
      <description>Time period for cost analysis: last_7_days|last_30_days|last_month|custom</description>
    </argument>
  </arguments>
  <examples>
    <example>
      <description>Comprehensive system analysis</description>
      <usage>/analyze-system</usage>
    </example>
    <example>
      <description>Deep performance analysis with memory profiling</description>
      <usage>/analyze-system performance --deep</usage>
    </example>
    <example>
      <description>Compatibility-focused dependency analysis</description>
      <usage>/analyze-system dependencies --compatibility</usage>
    </example>
    <example>
      <description>Cost optimization analysis for AWS</description>
      <usage>/analyze-system cost --optimization aws</usage>
    </example>
  </examples>
  <claude_prompt>
    <prompt>
      <!-- Standard DRY Components -->
      <include>components/validation/validation-framework.md</include>
      <include>components/workflow/command-execution.md</include>
      <include>components/workflow/error-handling.md</include>
      <include>components/interaction/progress-reporting.md</include>
      <include>components/analysis/codebase-discovery.md</include>
      <include>components/analysis/dependency-mapping.md</include>
      <include>components/workflow/report-generation.md</include>

You are a senior system architect and analysis specialist. The user wants comprehensive system analysis combining performance, dependencies, cost, and security assessments.

**Analysis Framework:**

Based on the focus_mode parameter, execute the appropriate analysis strategy:

**1. COMPREHENSIVE MODE (default):**
- Execute all analysis modules with balanced depth
- Generate unified system health report
- Prioritize findings by business impact
- Cross-reference issues between domains

**2. PERFORMANCE MODE:**
- **Bottleneck Detection**: Algorithmic complexity, hot paths, memory leaks, I/O blocking
- **Performance Patterns**: N+1 queries, unnecessary nested loops, synchronous operations
- **Metrics Analysis**: Response times, throughput, resource utilization
- **Profiling**: CPU, memory, database, network analysis
- **Optimization Recommendations**: Actionable performance improvements

**3. DEPENDENCIES MODE:**
- **Dependency Mapping**: Comprehensive dependency graphs and relationships
- **Compatibility Analysis**: Dependency compatibility analysis with impact scoring
- **Version Analysis**: Compatibility and update requirements
- **Conflict Detection**: Dependency conflicts and resolution strategies
- **License Compliance**: License compatibility and compliance issues
- **Optimization Assessment**: Cleanup and optimization opportunities

**4. COST MODE:**
- **Resource Tracking**: Automated cloud resource cost tracking
- **Spending Analysis**: Pattern analysis, trends, and anomalies
- **Resource Tagging**: Cost attribution by project/service/environment
- **Waste Identification**: Idle resources and optimization opportunities
- **Optimization Recommendations**: Rightsizing, reserved instances, cleanup strategies

**5. QUALITY MODE:**
- **Quality Assessment**: Code quality and pattern analysis
- **OWASP Compliance**: Best practices validation
- **Configuration Review**: Configuration analysis
- **Risk Assessment**: Code risk scoring and prioritization

**Implementation Strategy:**

1. **Discovery Phase**: 
   - Identify system components and architecture
   - Map dependencies and relationships
   - Establish baseline metrics

2. **Analysis Phase**:
   - Execute focused analysis based on mode
   - Collect performance, quality, and cost data
   - Cross-reference findings across domains

3. **Assessment Phase**:
   - Evaluate findings against best practices
   - Calculate risk scores and business impact
   - Prioritize issues by severity and effort

4. **Reporting Phase**:
   - Generate structured analysis report
   - Provide actionable recommendations
   - Include implementation roadmap

**Analysis Depth Handling:**
- **Shallow**: Quick overview with major issues only
- **Standard**: Balanced analysis with key findings
- **Deep**: Comprehensive analysis with detailed profiling
- **Exhaustive**: Complete system audit with extensive documentation

      <include component="components/context/find-relevant-code.md" />
      <include component="components/analysis/codebase-discovery.md" />
      <include component="components/performance/auto-scaling.md" />
      <include component="components/performance/cost-optimization.md" />
      <include component="components/security/owasp-compliance.md" />
      <include component="components/analytics/business-intelligence.md" />
      <include component="components/context/adaptive-thinking.md" />
      <include component="components/reporting/generate-structured-report.md" />

**Output Format:**
Generate a comprehensive system analysis report with:
- Executive summary with key findings
- Detailed analysis per focus area
- Risk assessment and priority matrix
- Actionable recommendations with implementation timeline
- Cost-benefit analysis for proposed changes
- Integration points and dependencies between recommendations
    </prompt>
  </claude_prompt>
  <dependencies>
    <includes_components>
      <!-- Standard DRY Components -->
      <component>components/validation/validation-framework.md</component>
      <component>components/workflow/command-execution.md</component>
      <component>components/workflow/error-handling.md</component>
      <component>components/interaction/progress-reporting.md</component>
      <component>components/analysis/codebase-discovery.md</component>
      <component>components/analysis/dependency-mapping.md</component>
      <component>components/workflow/report-generation.md</component>
      
      <!-- Performance Analysis Components -->
      <component>components/context/find-relevant-code.md</component>
      <component>components/performance/auto-scaling.md</component>
      <component>components/context/adaptive-thinking.md</component>
      
      <!-- Dependency Analysis Components -->
      <component>components/security/owasp-compliance.md</component>
      
      <!-- Cost Analysis Components -->
      <component>components/performance/cost-optimization.md</component>
      <component>components/analytics/business-intelligence.md</component>
      
      <!-- Unified Reporting -->
      <component>components/reporting/generate-structured-report.md</component>
    </includes_components>
    <uses_config_values>
      <!-- Performance Configuration -->
      <value>paths.source</value>
      
      <!-- Dependency Configuration -->
      <value>dependencies.scan.security_level</value>
      <value>analysis.vulnerability.sources</value>
      
      <!-- Cost Configuration -->
      <value>cost_analysis.provider.credentials</value>
      <value>cost_optimization.recommendation_level</value>
      
      <!-- System Configuration -->
      <value>system.analysis.default_depth</value>
      <value>system.reporting.format</value>
    </uses_config_values>
  </dependencies>
</command_file>