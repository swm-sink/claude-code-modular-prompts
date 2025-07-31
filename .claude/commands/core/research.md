---
name: /research
description: Comprehensive research framework with source validation and actionable insights (v2.0)
version: 2.0
usage: '/research [topic] [--depth shallow|standard|comprehensive] [--focus technical|business|competitive] [--sources web|codebase|both]'
category: core
allowed-tools:
- Read
- Write
- Grep
- WebSearch
- WebFetch
dependencies:
- /analyze-code
- /query
- /validate-component
validation:
  pre-execution: Validate topic scope and research parameters
  during-execution: Verify source credibility and information accuracy
  post-execution: Ensure actionable recommendations are provided
progressive-disclosure:
  layer-integration: Layer 1 quick answers, Layer 2 detailed analysis, Layer 3 comprehensive research reports
  escalation-path: Quick lookup → detailed research → academic-level analysis
  de-escalation: Cached results speed up repeated research
safety-measures:
  - Verify source credibility
  - Cross-reference information
  - Flag outdated content
  - Highlight biases
error-recovery:
  no-results: Broaden search scope and suggest alternatives
  conflicting-info: Present multiple viewpoints with analysis
  source-unavailable: Use cached data with freshness warnings
---

# Research Framework for lusaka

I'll help you research topics relevant to your software-development project, providing comprehensive analysis and actionable insights for Python implementation.

## Usage

```bash
/research "authentication best practices"
/research "API design patterns" --depth comprehensive
/research "database optimization" --focus technical
/research "competitor analysis" --focus business
```

## Research Approach

1. **Topic Analysis**: Break down the research question
2. **Source Gathering**: Find relevant technical documentation and best practices
3. **Analysis**: Evaluate options and trade-offs
4. **Recommendations**: Provide specific guidance for lusaka
5. **Implementation Notes**: Connect research to practical next steps

I'll tailor the research to your Python environment and swm-sink's context.

## Depth Levels

- **Shallow**: Quick overview and key points
- **Standard**: Comprehensive analysis with examples
- **Comprehensive**: Deep dive with multiple perspectives and detailed implementation guidance