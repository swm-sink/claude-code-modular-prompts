# Automation Scripts

Complete project lifecycle automation tools for the Claude Code Framework.

## Scripts

### `deployment_pipeline.py`
**Purpose**: Comprehensive deployment orchestration with security scanning and rollback capabilities

**Features**:
- Multi-environment deployment support (local, development, staging, production)
- Integrated security scanning (dependency vulnerabilities, secret detection)
- Automatic rollback on failures
- Health checks and validation
- Git branch validation and clean working directory checks

**Usage**:
```bash
# Local deployment
python scripts/automation/deployment_pipeline.py --target local

# Staging deployment with dry run
python scripts/automation/deployment_pipeline.py --target staging --dry-run

# Production deployment with custom version
python scripts/automation/deployment_pipeline.py --target production --version v1.2.3
```

### `health_monitor.py`
**Purpose**: Framework health monitoring with real-time alerts and performance tracking

**Features**:
- Multi-category health monitoring (framework, configuration, performance, quality, security)
- Real-time status updates and alerts
- Performance benchmarking and trend analysis
- Resource usage monitoring
- Dependency health checking

**Usage**:
```bash
# Single health check
python scripts/automation/health_monitor.py --check-all

# Continuous monitoring
python scripts/automation/health_monitor.py --watch --interval 60

# Generate health report
python scripts/automation/health_monitor.py --report health_report.md
```

### `project_initializer.py`
**Purpose**: Intelligent project setup wizard with tech stack auto-detection

**Features**:
- Automatic technology stack detection (language, framework, database)
- Interactive setup wizard
- PROJECT_CONFIG.xml generation with project-specific settings
- Directory structure creation
- Git hooks configuration
- Quality gates setup

**Usage**:
```bash
# Interactive setup wizard
python scripts/automation/project_initializer.py

# Auto-detection mode
python scripts/automation/project_initializer.py --auto

# Direct configuration
python scripts/automation/project_initializer.py --name MyApp --domain web-development --language python
```

### `test_runner.py`
**Purpose**: Multi-framework testing automation with quality gate enforcement

**Features**:
- Multi-language test framework support (pytest, jest, go test, cargo test, etc.)
- Automatic framework detection
- Test coverage measurement and enforcement
- Quality gate validation (coverage thresholds, pass rates, performance)
- Comprehensive test reporting

**Usage**:
```bash
# Run all detected test frameworks
python scripts/automation/test_runner.py

# Run specific framework with coverage
python scripts/automation/test_runner.py --framework pytest

# Enforce quality gates
python scripts/automation/test_runner.py --enforce-gates --report test_report.md
```

## Integration

All automation scripts integrate with:
- **PROJECT_CONFIG.xml** for project-specific configuration
- **Quality gates** for TDD enforcement and standards compliance
- **Git workflows** for branch validation and commit hooks
- **CI/CD pipelines** through standardized exit codes
- **Framework health monitoring** for continuous improvement

## Common Options

Most scripts support these common options:
- `--project-root` - Specify project root directory
- `--verbose, -v` - Enable verbose debugging output
- `--dry-run` - Simulate operations without making changes
- `--report` - Generate detailed reports
- `--help` - Show comprehensive help with examples

## Error Handling

All scripts use standardized error handling with:
- Clear error messages with suggested fixes
- Appropriate exit codes for CI/CD integration
- Comprehensive logging for debugging
- Graceful degradation when dependencies are missing