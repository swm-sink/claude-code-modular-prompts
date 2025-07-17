# Validation Scripts

Framework validation and quality assurance tools ensuring integrity and compliance.

## Scripts

### `project_config_validator.py`
**Purpose**: Unified PROJECT_CONFIG.xml validation system

**Features**:
- Comprehensive XML schema validation
- Placeholder resolution testing
- Tier-aware validation (development, staging, production)
- Missing configuration detection
- Integration with framework defaults
- Minimal configuration generation

**Usage**:
```bash
# Validate current configuration
python scripts/validation/project_config_validator.py --validate

# Generate minimal configuration
python scripts/validation/project_config_validator.py --generate-minimal

# Validate with specific tier
python scripts/validation/project_config_validator.py --tier production --validate
```

### `reference_validator.py`
**Purpose**: Cross-reference and link validation across framework files

**Features**:
- Markdown reference validation
- Internal link checking
- External URL validation (optional)
- Broken link detection and reporting
- Automatic link fixing suggestions
- Comprehensive validation reports

**Usage**:
```bash
# Validate all references
python scripts/validation/reference_validator.py

# Fix broken internal references
python scripts/validation/reference_validator.py --fix

# Include external URL validation
python scripts/validation/reference_validator.py --check-external
```

### `performance_benchmark.py`
**Purpose**: Framework performance analysis and optimization measurement

**Features**:
- Framework response time benchmarking
- Memory usage analysis
- Token consumption tracking
- Command execution profiling
- Performance trend analysis
- Optimization recommendations

**Usage**:
```bash
# Basic performance benchmark
python scripts/validation/performance_benchmark.py

# Comprehensive analysis
python scripts/validation/performance_benchmark.py --comprehensive

# Compare with baseline
python scripts/validation/performance_benchmark.py --baseline previous_results.json
```

### `validate_all.sh`
**Purpose**: Comprehensive validation runner executing all validation checks

**Features**:
- Orchestrates all validation scripts
- Progress tracking and error reporting
- Parallel execution where possible
- Summary reporting with error counts
- CI/CD friendly exit codes

**Usage**:
```bash
# Run all validations
bash scripts/validation/validate_all.sh

# Run with verbose output
bash scripts/validation/validate_all.sh --verbose

# Quick validation (essential checks only)
bash scripts/validation/validate_all.sh --quick
```

## Quality Gates

The validation scripts enforce these quality gates:
- **Configuration Completeness** - All required configuration present
- **Reference Integrity** - No broken internal links
- **Performance Standards** - Response times within thresholds
- **Framework Compliance** - Adherence to framework conventions
- **Documentation Coverage** - All components documented

## Integration Points

Validation scripts integrate with:
- **Pre-commit hooks** for automatic validation
- **CI/CD pipelines** for deployment gating
- **Quality enforcement** for TDD compliance
- **Performance monitoring** for regression detection
- **Documentation maintenance** for accuracy assurance

## Exit Codes

All validation scripts use standardized exit codes:
- `0` - All validations passed
- `1` - General validation failures
- `2` - Configuration errors
- `3` - Reference/link errors
- `4` - Performance threshold failures

## Reports

Validation results are saved to:
- `internal/reports/` - Detailed validation reports
- Console output - Summary results
- CI/CD artifacts - For pipeline integration

## Automation

For automated validation:
```bash
# In CI/CD pipeline
bash scripts/validation/validate_all.sh || exit 1

# With pre-commit hooks
pre-commit run --all-files

# Scheduled health checks
python scripts/validation/performance_benchmark.py --automated
```