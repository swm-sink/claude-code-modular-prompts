# Validation Scripts Directory

This directory contains comprehensive validation and quality assurance scripts for framework compliance, quality gates, and automated testing.

## Scripts Overview

### Core Validation
- `validate.py` - **Primary framework validation tool**
  - Validates framework structure and module integrity
  - Checks version consistency across all modules
  - Verifies dependency relationships
  - Ensures compliance with framework rules
  - **Usage**: `python internal/validation/validate.py`

### Specialized Validators
- `validation-agent.py` - Automated validation agent for continuous compliance
- `trace-compliance-validator.py` - TRACE framework compliance validation
- `automated_qa_pipeline.py` - Comprehensive QA automation pipeline
- `prompt_quality_assessor.py` - Quality assessment for prompt engineering
- `prompt_change_analyzer.py` - Analysis of prompt modifications and impacts

## Validation Categories

### Framework Compliance
**Purpose**: Ensure framework follows established standards and rules

Scripts:
- `validate.py` - Core compliance checking
- `validation-agent.py` - Continuous compliance monitoring
- `trace-compliance-validator.py` - TRACE framework standards

**Usage**:
```bash
# Run full framework validation
python internal/validation/validate.py

# Start validation agent
python internal/validation/validation-agent.py

# Validate TRACE compliance
python internal/validation/trace-compliance-validator.py
```

### Quality Assurance
**Purpose**: Automated quality assessment and improvement recommendations

Scripts:
- `automated_qa_pipeline.py` - Complete QA workflow
- `prompt_quality_assessor.py` - Prompt quality analysis
- `prompt_change_analyzer.py` - Change impact analysis

**Usage**:
```bash
# Run full QA pipeline
python internal/validation/automated_qa_pipeline.py

# Assess prompt quality
python internal/validation/prompt_quality_assessor.py

# Analyze prompt changes
python internal/validation/prompt_change_analyzer.py
```

## Validation Workflow

1. **Pre-Development**: Run validation before making changes
2. **During Development**: Use continuous validation agents
3. **Pre-Commit**: Validate all changes before committing
4. **Post-Deployment**: Verify deployment quality and compliance

## Key Features

### Framework Validation (`validate.py`)
- **Comprehensive Checks**: 14+ validation categories
- **Predictive Analytics**: Quality scoring and trend analysis
- **Compliance Enforcement**: July 2025 temporal standards
- **Issue Categorization**: Organized by severity and type
- **Remediation Guidance**: Actionable recommendations

### Quality Assessment
- **Automated QA**: End-to-end quality pipeline
- **Performance Metrics**: Response time and efficiency tracking
- **Compliance Monitoring**: Real-time framework adherence
- **Risk Assessment**: Predictive quality scoring

## Output and Reports

All validation scripts generate detailed reports:
- **Analytics Reports**: Stored in `.claude/analytics/`
- **Quality Scores**: 0-100 scoring with improvement recommendations
- **Issue Tracking**: Categorized by type and severity
- **Trend Analysis**: Historical quality and compliance tracking

## Usage Notes

- **Run from project root**: All scripts expect to be run from repository root
- **Regular Validation**: Run validation frequently during development
- **Pre-Commit**: Always validate before committing changes
- **Continuous Integration**: Integrate validation into CI/CD pipeline

## Error Handling

- **Graceful Degradation**: Scripts handle missing dependencies
- **Detailed Logging**: Comprehensive error reporting
- **Recovery Options**: Guidance for fixing validation failures
- **Exit Codes**: Proper exit codes for automation integration

## Requirements

- Python 3.8+
- Framework access and read permissions
- Optional: Analytics storage permissions
- Understanding of framework validation rules