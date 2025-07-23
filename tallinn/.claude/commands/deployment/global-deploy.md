---
name: /global-deploy
description: Advanced global deployment with multi-region orchestration, geographic optimization, and intelligent traffic management
usage: /global-deploy [deployment_scope] [region_strategy]
tools: Read, Write, Edit, Bash, Grep
---

# Advanced global deployment with multi-region orchestration, geographic optimization, and intelligent traffic management

**Usage**: `/global-deploy $TARGET_REGIONS $STRATEGY $LOCALIZE`

## Key Arguments

- **$TARGET_REGIONS** (required): Target regions for deployment (e.g., "US,EU,APAC" or "global").
- **$STRATEGY** (optional): Deployment strategy: blue-green, canary, or rolling.
- **$LOCALIZE** (optional): Localization mode: auto (Claude-driven) or manual (user-guided).

## Examples

```bash
/global-deploy "global" --strategy=blue-green --localize=auto
```
*Deploy globally with automatic localization*

```bash
/global-deploy "US,EU,JP" --strategy=canary --localize=manual
```
*Deploy to specific regions with canary rollout*

## Core Logic

components/validation/input-validation.md
 components/workflow/command-execution.md
 components/workflow/error-handling.md
 components/interaction/progress-reporting.md

 components/context/adaptive-thinking.md
 components/actions/parallel-execution.md
 components/orchestration/dag-orchestrator.md
 components/quality/anti-pattern-detection.md
 components/deployment/multi-region-strategies.md

 You are an expert global deployment orchestrator with deep knowledge of international markets, cultural nuances, and regional technology preferences. Execute intelligent global deployment using Claude's native capabilities.

 **Global Deployment Intelligence**:

**regional_analysis**:

**market_intelligence**:

 Analyze target regions for deployment optimization:
 - **North America (US/CA)**: High cloud adoption, privacy-conscious, performance-focused
 - **Europe (EU/UK)**: GDPR compliance critical, quality-focused, data sovereignty requirements
 - **Asia Pacific (JP/KR/SG/AU)**: Mobile-first, efficiency-oriented, relationship-driven adoption
 - **Latin America (BR/MX/AR)**: Cost-sensitive, community-driven, localization important
 - **Middle East & Africa (UAE/ZA)**: Emerging adoption, infrastructure considerations, cultural sensitivity
 - **India**: Cost-optimization focus, English proficiency, massive scale requirements
 - **China**: Unique regulatory environment, local partnerships essential, performance critical

**cultural_adaptation**:


*[Additional logic optimized for execution...]*

## Execution Pattern

1. **Input Processing**: Validate and process $ARGUMENTS
2. **Core Execution**: Execute main command logic
3. **Output Generation**: Generate structured results

