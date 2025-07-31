# Scripts Directory

This directory contains automation scripts, validation tools, and testing frameworks used for project maintenance and quality assurance.

## Script Categories

### Setup and Validation Scripts
- **`adapt.sh`** - Project adaptation automation
- **`validate-adaptation.sh`** - Validates template customizations
- **`validate-demo.sh`** - Demo validation testing
- **`validate-project-consolidation.sh`** - Project structure validation

### YAML and Compliance Scripts
- **`fix-yaml-compliance.py`** - Converts `tools:` to `allowed-tools:` fields
- **`fix_yaml_compliance_comprehensive.py`** - Comprehensive YAML field standardization
- **`final_yaml_validation.py`** - Final YAML structure validation
- **`optimized-yaml-validator.py`** - Efficient YAML validation
- **`validate-yaml-compliance.py`** - YAML compliance checking
- **`yaml_compliance_verification.py`** - Verification framework

### Testing and Quality Assurance
- **`comprehensive-test-framework.py`** - Main testing framework
- **`enhanced-comprehensive-test-framework.py`** - Advanced testing capabilities
- **`integration-test-suite.py`** - Integration testing framework
- **`component_integration_test.py`** - Component interaction testing

### Performance and Benchmarking
- **`performance-benchmarking-system.py`** - Performance measurement tools
- **`performance-benchmark-tests.py`** - Benchmark test suites
- **`performance-optimization-implementation.py`** - Performance improvement tools

### Documentation and Analysis
- **`documentation-accuracy-fix.py`** - Documentation error correction
- **`documentation-sync-validator.py`** - Cross-document validation
- **`fix-command-count-accuracy.py`** - Command count verification

### Comprehensive Review Scripts
- **`comprehensive-100-point-review.py`** - 100-point quality assessment
- **`comprehensive_50_step_deep_review_results.py`** - Deep analysis framework
- **`final-production-optimization-review.py`** - Production readiness review

### Quality Subdirectory (`quality/`)
- **`performance-benchmark.py`** - Performance testing tools
- **`component-stack-benchmark.py`** - Component performance analysis
- **`workflow-performance-benchmark.py`** - Workflow efficiency testing

## Usage Guidelines

### For Project Maintenance
1. Use YAML compliance scripts after making template changes
2. Run validation scripts before committing changes
3. Execute testing frameworks to verify system integrity

### For Quality Assurance
1. Performance scripts help identify bottlenecks
2. Documentation scripts ensure accuracy and consistency
3. Review scripts provide comprehensive project assessment

### For Development
1. Testing frameworks validate new features
2. Integration scripts verify component interactions
3. Benchmark scripts measure performance impact

## Important Notes

- **Test scripts first** - Many scripts modify files, always test on copies
- **Check dependencies** - Some scripts require specific Python packages
- **Review output** - Scripts generate detailed reports in `reports/` directory
- **Use version control** - Always commit before running major modification scripts

*For script-specific usage, see individual file headers and documentation.*