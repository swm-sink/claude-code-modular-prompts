# /init-validate - Comprehensive Framework Validation

Validates your framework setup using multiple specialized agents to ensure everything is configured correctly.

## Usage
```
/init-validate
```

## What It Does

This command spawns 6 specialized validation agents that work in parallel:

1. **Documentation Validator**
   - Checks documentation completeness
   - Verifies all examples work
   - Ensures consistency across files
   - Validates README accuracy

2. **Module Dependency Validator**
   - Maps all module dependencies
   - Checks for missing references
   - Validates integration points
   - Ensures proper module loading

3. **Command Functionality Validator**
   - Tests all command examples
   - Verifies delegation patterns
   - Checks command availability
   - Validates usage instructions

4. **Configuration Validator**
   - Validates PROJECT_CONFIG.xml
   - Tests placeholder resolution
   - Checks path configurations
   - Ensures setting compatibility

5. **Quality Gate Validator**
   - Verifies quality gate setup
   - Tests enforcement mechanisms
   - Validates thresholds
   - Checks TDD compliance

6. **Integration Validator**
   - Tests end-to-end workflows
   - Validates system integration
   - Checks cross-component communication
   - Ensures production readiness

## Validation Process

Each agent performs:

1. **Comprehensive Analysis**
   - Deep inspection of their domain
   - Pattern recognition and verification
   - Consistency checking
   - Error detection

2. **Issue Identification**
   - Missing components
   - Broken references
   - Configuration errors
   - Integration gaps

3. **Automatic Fixes**
   - Resolves simple issues
   - Updates configurations
   - Fixes broken references
   - Corrects inconsistencies

4. **Detailed Reporting**
   - Validation status
   - Issues found and fixed
   - Remaining problems
   - Recommendations

## Example Output

```
/init-validate

🚀 Spawning 6 validation agents...

✅ Documentation Validator: 98% complete, 2 minor issues fixed
✅ Module Validator: All dependencies resolved
⚠️ Command Validator: 1 example needs updating
✅ Configuration Validator: PROJECT_CONFIG.xml valid
✅ Quality Gate Validator: All gates operational
✅ Integration Validator: System ready for production

📊 Overall Status: 95% READY
📝 Full report generated: validation-report-2025-07-11.md
```

## Benefits

- **Parallel Validation** - 6 agents work simultaneously
- **Comprehensive Coverage** - Every aspect validated
- **Automatic Fixes** - Common issues resolved
- **Production Confidence** - Ensures framework readiness

## Validation Areas

- Framework architecture integrity
- Command-module integration
- Configuration completeness
- Documentation accuracy
- Quality gate functionality
- Performance optimization
- Security compliance
- Error handling

## Related Commands

- `/init-custom` - Configure existing projects
- `/init-new` - Setup new projects
- `/init-research` - Research-based configuration

$ARGUMENTS