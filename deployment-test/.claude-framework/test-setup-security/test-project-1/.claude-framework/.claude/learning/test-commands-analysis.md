# Test Commands Overlap Analysis

**Date**: 2025-07-25
**Analyzed**: 6 test commands
**Consolidation Target**: 2 commands (/test and /test-e2e)

## Overlap Summary

### Common Features Across All Test Commands
1. **Coverage Analysis**: Found in test-unit, test-coverage, dev-test
2. **Report Generation**: Found in all 6 commands with similar formats
3. **Progress Reporting**: Identical component usage across all
4. **Error Handling**: Same error-handling component everywhere
5. **Validation Framework**: Shared by all commands

### Unique Features to Preserve

#### From test-unit.md:
- Automated test generation capability
- Function and edge case analysis
- Coverage gap identification

#### From test-integration.md:
- Environment setup automation (Docker Compose)
- Service dependency management
- Database seeding capabilities

#### From test-coverage.md:
- Advanced coverage analysis
- Gap detection algorithms
- Line/branch/function metrics

#### From test-report.md:
- Multi-format output (HTML, PDF, JSON)
- Trend analysis over time
- Consolidated reporting across test types

#### From dev-test.md:
- Pattern-based test filtering
- Parallel test execution
- Watch mode for continuous testing

#### From test-e2e.md:
- Browser automation (unique, keep separate)
- Visual testing and screenshots
- Cross-browser support

## Consolidation Decision

### Create Unified /test Command
Combining test-unit, test-integration, test-coverage, test-report, and dev-test into:

```bash
/test [type] [target] [options]
```

Where:
- **type**: unit|integration|coverage|report|all (default: all)
- **target**: file path, directory, or test pattern
- **options**: 
  - --coverage [level]: low|medium|high
  - --env [config]: environment config for integration tests
  - --format [type]: html|pdf|json|summary
  - --parallel: run tests in parallel
  - --watch: continuous testing mode
  - --gaps: focus on coverage gaps
  - --setup-db: setup database for integration tests

### Keep Separate:
- `/test-e2e`: Due to unique browser automation requirements

## Feature Mapping

| Original Command | Features | Destination |
|-----------------|----------|-------------|
| test-unit | Test generation, unit testing | /test unit |
| test-integration | Environment setup, integration | /test integration |
| test-coverage | Coverage analysis, gaps | /test coverage or --coverage |
| test-report | Multi-format reporting | /test report or --format |
| dev-test | Pattern filtering, watch mode | /test with --watch/--pattern |
| test-e2e | Browser automation | Keep as /test-e2e |

## Component Consolidation

### Shared Components (7):
- validation/validation-framework.md
- workflow/command-execution.md
- workflow/error-handling.md
- interaction/progress-reporting.md
- analysis/codebase-discovery.md
- workflow/report-generation.md
- testing/testing-framework.md

### Unique Components to Merge:
- deployment/auto-provision.md (from integration)
- reporting/generate-structured-report.md (standardize)

## Success Metrics
- Code reduction: ~60% (5 commands → 1)
- Feature preservation: 100%
- User experience: Simplified with consistent interface
- Maintainability: Single source of truth for testing