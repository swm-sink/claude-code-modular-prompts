---
description: Advanced research agent with intelligent information gathering, analysis synthesis, and knowledge discovery
argument-hint: "[research_scope] [analysis_depth]"
allowed-tools: Read, Write, Edit, Bash, Grep
---

# /agent researcher - Advanced Research Agent

Sophisticated research agent with intelligent information gathering, comprehensive analysis synthesis, and automated knowledge discovery.

## Usage
```bash
/agent researcher academic                   # Academic research and analysis
/agent researcher --market                   # Market research and trends
/agent researcher --technical                # Technical research and evaluation
/agent researcher --comprehensive            # Comprehensive multi-domain research
```

<command_file>
  <metadata>
    <n>/agent researcher</n>
    <purpose>Advanced research agent with intelligent information gathering, analysis synthesis, and knowledge discovery</purpose>
    <usage>
      <![CDATA[
      /agent researcher [research_scope]
      ]]>
    </usage>
  </metadata>

  <arguments>
    <argument name="research_scope" type="string" required="false" default="academic">
      <description>Scope of research to conduct</description>
    </argument>
    <argument name="analysis_depth" type="string" required="false" default="comprehensive">
      <description>Depth of analysis and investigation</description>
    </argument>
  </arguments>
  
  <examples>
    <example>
      <description>Academic research and analysis</description>
      <usage>/agent researcher academic</usage>
    </example>
    <example>
      <description>Market research and trends</description>
      <usage>/agent researcher --market</usage>
    </example>
  </examples>

  <claude_prompt>
    <prompt>
      <!-- Standard DRY Components -->
      <include>components/validation/input-validation.md</include>
      <include>components/workflow/command-execution.md</include>
      <include>components/workflow/error-handling.md</include>
      <include>components/interaction/progress-reporting.md</include>
      <include>components/analysis/codebase-discovery.md</include>
      <include>components/analysis/dependency-mapping.md</include>
      <include>components/workflow/report-generation.md</include>

You are an advanced research agent specialist. The user wants to deploy intelligent research capabilities with comprehensive information gathering and analysis.

**Research Process:**
1. **Domain Analysis**: Analyze research domain and define scope
2. **Information Gathering**: Systematic collection of relevant information and sources
3. **Analysis Synthesis**: Synthesize findings into coherent insights and patterns
4. **Knowledge Discovery**: Identify breakthrough insights and novel connections
5. **Report Generation**: Create comprehensive research reports and recommendations

**Implementation Strategy:**
- Deploy intelligent information gathering and source analysis
- Implement systematic research methodologies and frameworks
- Apply advanced analysis techniques for insight generation
- Synthesize findings from multiple sources and perspectives
- Generate actionable research reports and knowledge bases

<include component="components/analytics/business-intelligence.md" />
<include component="components/reasoning/tree-of-thoughts.md" />
<include component="components/reporting/generate-structured-report.md" />
    </prompt>
  </claude_prompt>

  <dependencies>
    <includes_components>
      <!-- Standard DRY Components -->
      <component>components/validation/input-validation.md</component>
      <component>components/workflow/command-execution.md</component>
      <component>components/workflow/error-handling.md</component>
      <component>components/interaction/progress-reporting.md</component>
      <component>components/analysis/codebase-discovery.md</component>
      <component>components/analysis/dependency-mapping.md</component>
      <component>components/workflow/report-generation.md</component>
      <!-- Command-specific components -->
      <component>components/analytics/business-intelligence.md</component>
      <component>components/reasoning/tree-of-thoughts.md</component>
      <component>components/reporting/generate-structured-report.md</component>
    </includes_components>
    <uses_config_values>
      <value>research.domains.enabled</value>
      <value>analysis.depth.default</value>
    </uses_config_values>
  </dependencies>
</command_file> 