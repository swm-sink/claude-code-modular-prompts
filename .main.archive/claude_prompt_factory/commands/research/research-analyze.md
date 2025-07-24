---
description: Advanced research analysis with systematic methodologies, data synthesis, and evidence evaluation frameworks
argument-hint: "[analysis_type] [methodology]"
allowed-tools: Read, Write, Edit, Bash, Grep
---

# /research analyze - Advanced Research Analysis

Sophisticated research analysis system with systematic methodologies, comprehensive data synthesis, and evidence evaluation frameworks.

## Usage
```bash
/research analyze literature                 # Literature review and analysis
/research analyze --systematic               # Systematic review methodology
/research analyze --meta                     # Meta-analysis framework
/research analyze --evidence                 # Evidence-based analysis
```

## Arguments

| Argument | Type | Required | Description |
|----------|------|----------|-------------|
| `type` | string | false | Analysis type (literature, systematic, meta, evidence). Default: literature. |
| `methodology` | string | false | Research methodology (quantitative, qualitative, mixed). Default: mixed. |

## Examples

```bash
/research analyze literature --systematic    # Systematic literature review
/research analyze --meta --quantitative     # Quantitative meta-analysis
/research analyze evidence --qualitative    # Qualitative evidence analysis
```

<command_file>
  <metadata>
    <n>/research analyze</n>
    <purpose>Advanced research analysis with systematic methodologies, data synthesis, and evidence evaluation frameworks</purpose>
    <usage>
      <![CDATA[
      /research analyze [analysis_type] [methodology]
      ]]>
    </usage>
  </metadata>

  <arguments>
    <argument name="analysis_type" type="string" required="false" default="literature">
      <description>Type of research analysis to perform</description>
    </argument>
    <argument name="methodology" type="string" required="false" default="mixed">
      <description>Research methodology to apply</description>
    </argument>
  </arguments>
  
  <examples>
    <example>
      <description>Systematic literature review</description>
      <usage>/research analyze literature --systematic</usage>
    </example>
    <example>
      <description>Meta-analysis with quantitative methodology</description>
      <usage>/research analyze --meta --quantitative</usage>
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
      <include>components/analytics/business-intelligence.md</include>
      <include>components/reasoning/tree-of-thoughts.md</include>
      <include>components/reporting/generate-structured-report.md</include>
      <include>components/analysis/literature-review.md</include>
      <include>components/research/methodology-frameworks.md</include>
      
You are a research analysis specialist. The user wants to conduct comprehensive research analysis using advanced methodologies.

**Analysis Process:**
1. **Research Scope Definition**: Define research questions and analysis scope
2. **Methodology Selection**: Choose appropriate research methodologies and frameworks
3. **Data Collection**: Systematic data collection and source identification
4. **Synthesis Framework**: Apply synthesis methodologies for evidence integration
5. **Quality Assessment**: Evaluate research quality and evidence strength

**Implementation Strategy:**
- Conduct systematic literature reviews with PRISMA guidelines
- Apply meta-analysis techniques for quantitative synthesis
- Implement qualitative analysis frameworks for thematic synthesis
- Use evidence grading systems (GRADE, SORT, etc.)
- Create comprehensive research databases and citation management
- Generate research reports with statistical analysis and visualization

    </prompt>
  </claude_prompt>

  <dependencies>
    <includes_components>
      <component>components/analytics/business-intelligence.md</component>
      <component>components/reasoning/tree-of-thoughts.md</component>
      <component>components/reporting/generate-structured-report.md</component>
    </includes_components>
    <uses_config_values>
      <value>research.methodologies.systematic</value>
      <value>analysis.statistical.frameworks</value>
    </uses_config_values>
  </dependencies>
</command_file> 