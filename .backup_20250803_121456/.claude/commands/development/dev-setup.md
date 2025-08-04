---
name: /dev-setup
description: Setup development environment with automated dependency management and team onboarding (v1.0)
version: "1.0"
usage: '/dev-setup [--environment local|docker|cloud] [--tools all|minimal|custom] [--auto-configure]'
category: development
allowed-tools:
- Bash
- Write
- Read
- Edit
- Grep
dependencies:
- /env-setup
- /protocol
- /test
validation:
  pre-execution: "Check system requirements and available resources"
  during-execution: "Verify each installation step succeeds"
  post-execution: "Run comprehensive environment validation suite"
progressive-disclosure:
  layer-integration: "Layer 1: Quick setup script, Layer 2: Custom configurations, Layer 3: Full DevOps pipeline"
  options:
    - name: minimal
      description: "Basic development tools in 2 minutes"
    - name: standard
      description: "Full environment with testing and debugging"
    - name: enterprise
      description: "Complete DevOps toolchain with CI/CD"
safety-checks:
  - "System compatibility verification"
  - "Dependency conflict resolution"
  - "Security tool configuration"
  - "Backup existing configurations"
error-recovery:
  - "Rollback on installation failure"
  - "Alternative package sources"
  - "Manual fallback instructions"
performance:
  - "Parallel installation where possible"
  - "Cached dependency downloads"
  - "Optimized configuration loading"
team-features:
  - "Shared configuration templates"
  - "Onboarding automation"
  - "Environment synchronization"
---

# Development Environment Setup for your project (v1.0)

I'll help you set up a complete development environment with automated dependency management, team synchronization, and intelligent configuration detection.

## 🚀 Progressive Setup Options

### Layer 1: Quick Start (2 minutes)
```bash
/dev-setup --auto-configure  # Detects and configures everything automatically
```

### Layer 2: Customized Setup (5 minutes)
```bash
/dev-setup --environment docker --tools standard
/dev-setup --environment local --tools custom:vscode,pytest,black
```

### Layer 3: Enterprise Setup (15 minutes)
```bash
/dev-setup --enterprise --with-ci --with-monitoring
```

## 🔍 Intelligent Detection

The v1.0 setup automatically detects:
- Operating system and architecture
- Existing development tools
- Project requirements from config files
- Team size and collaboration needs
- Security and compliance requirements

## 🛠️ Environment Options

### Local Development
```bash
/dev-setup --environment local
```
**Features:**
- ✅ Native performance
- ✅ Direct hardware access
- ✅ Instant file watching
- ✅ Local debugging

**Auto-configured tools:**
- Python 3.11+ with pyenv
- Virtual environment management
- Pre-commit hooks
- IDE configurations

### Docker Development
```bash
/dev-setup --environment docker
```
**Features:**
- ✅ Consistent environments
- ✅ One-command startup
- ✅ Service orchestration
- ✅ Production parity

**Auto-generated files:**
- `Dockerfile` with multi-stage builds
- `docker-compose.yml` for services
- `.dockerignore` optimizations
- Volume configurations

### Cloud Development
```bash
/dev-setup --environment cloud
```
**Features:**
- ✅ Zero local setup
- ✅ Powerful cloud resources
- ✅ Real-time collaboration
- ✅ Automatic backups

**Supported platforms:**
- GitHub Codespaces
- GitPod
- AWS Cloud9
- Google Cloud Shell

## 📦 Tool Installation Profiles

### Minimal (2 minutes)
```bash
/dev-setup --tools minimal
```
- Python runtime
- pip/poetry
- Git
- Basic editor config

### Standard (5 minutes)
```bash
/dev-setup --tools standard
```
- Everything in minimal
- pytest + coverage
- Black + isort + flake8
- Pre-commit hooks
- Database tools
- API testing tools

### Custom Selection
```bash
/dev-setup --tools custom:pytest,black,mypy,docker
```

## 🔧 Project-Specific Configuration

### For Python Projects
```python
# Auto-detected from pyproject.toml or requirements.txt
dependencies = [
    "fastapi[all]",
    "sqlalchemy",
    "alembic",
    "pytest-asyncio"
]
```

### Database Setup (PostgreSQL)
- Local PostgreSQL with optimized settings
- Connection pool configuration
- Migration tool setup
- Test database creation
- Backup scheduling

### API Development (RESTful)
- OpenAPI documentation
- Request mocking tools
- Performance profiling
- Load testing setup

## 👥 Team Collaboration (1-5 developers)

### Automated Onboarding
```bash
# New team member runs:
/dev-setup --from-team-config
```

### Shared Configurations
- `.editorconfig` for consistent formatting
- `.gitignore` with Python best practices
- Git hooks for quality gates
- VS Code workspace settings

## 🔒 Security Configuration

### Standard Security Setup
- Secret management (python-dotenv)
- Git credential helper
- SSH key generation
- Security linters
- Dependency scanning

### Advanced Security
```bash
/dev-setup --security enhanced
```
- Pre-commit security checks
- SAST tool integration  
- Container scanning
- License compliance

## 🧪 Verification Suite

### Automatic Health Checks
```bash
# Run after setup:
/dev-setup --verify
```

**Checks performed:**
1. ✅ Python version and pip
2. ✅ Virtual environment activation
3. ✅ Database connectivity
4. ✅ API endpoint responses
5. ✅ Test suite execution
6. ✅ Linter configuration
7. ✅ Git hooks functionality

## 📊 Performance Optimizations

### Faster Setup
- Parallel downloads
- Cached dependencies
- Incremental updates
- Smart skip detection

### Development Speed
- File watcher optimization
- Hot reload configuration
- Test parallelization
- Build caching

## 🎯 Quick Commands

### Complete Setup
```bash
/dev-setup --auto-configure --verify
```

### Update Environment
```bash
/dev-setup --update
```

### Team Sync
```bash
/dev-setup --sync-team
```

### Troubleshooting
```bash
/dev-setup --diagnose
```

---

Ready to set up your development environment? Choose your setup approach:
- 🚀 **Quick**: Auto-configure everything
- ⚙️ **Custom**: Choose specific tools
- 🏢 **Enterprise**: Full DevOps suite