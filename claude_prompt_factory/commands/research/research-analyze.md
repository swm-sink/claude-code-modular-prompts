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

## Claude Prompt

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

<include component="components/analytics/business-intelligence.md" />
<include component="components/reasoning/tree-of-thoughts.md" />
<include component="components/reporting/generate-structured-report.md" />

## Dependencies

- `components/analytics/business-intelligence.md`
- `components/reasoning/tree-of-thoughts.md`
- `components/reporting/generate-structured-report.md`
- `research.methodologies.systematic`
- `analysis.statistical.frameworks` 