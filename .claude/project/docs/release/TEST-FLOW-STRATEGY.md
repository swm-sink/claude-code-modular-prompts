# Comprehensive Test Flow Strategy

## Overview

Multiple test scenarios to validate the adaptation engine across different use cases, domains, and edge conditions.

## Test Scenarios

### 1. Quick Start Test - Basic Web Dev Project

**Purpose**: Validate the happy path for a typical web developer

**Setup**:
```bash
mkdir test-web-project && cd test-web-project
git init
echo '{"name": "test-app", "dependencies": {"react": "^18.0.0"}}' > package.json
```

**Test Flow**:
1. Run `setup.sh` with git submodule method
2. Execute `/adapt-to-project --express`
3. Answer all 50 questions for web-dev scenario
4. Verify placeholder replacement
5. Check readiness score (target: 85%+)

**Validation**:
- All placeholders replaced in commands
- project-config.yaml properly populated
- Appropriate commands selected for React project
- No errors during adaptation

### 2. Enterprise Test - Complex Security Requirements

**Purpose**: Validate enterprise-grade adaptation with high security

**Setup**:
```bash
mkdir test-enterprise && cd test-enterprise
git init
echo '<project><security>SOC2</security></project>' > security-requirements.xml
mvn archetype:generate -DgroupId=com.enterprise -DartifactId=secure-app
```

**Test Flow**:
1. Run `setup.sh` with direct copy method
2. Execute `/adapt-to-project --guided`
3. Select "high" security level
4. Choose enterprise workflow options
5. Validate security configurations

**Validation**:
- Tool permissions set to "ask" for sensitive operations
- Security hooks enabled
- Audit logging commands included
- Compliance-focused adaptations

### 3. Data Science Test - Jupyter & ML Workflow

**Purpose**: Validate adaptation for data science projects

**Setup**:
```bash
mkdir test-datascience && cd test-datascience
git init
echo "pandas==2.0.0\nscikit-learn==1.3.0" > requirements.txt
touch analysis.ipynb
```

**Test Flow**:
1. Run `setup.sh` with selective import
2. Choose data science components only
3. Execute `/adapt-to-project`
4. Verify ML-specific adaptations

**Validation**:
- Jupyter notebook commands included
- Data analysis patterns selected
- Python-specific configurations
- ML workflow adaptations

### 4. Edge Case Test - Partial Adaptation & Recovery

**Purpose**: Test interruption, recovery, and undo capabilities

**Test Flow**:
1. Start adaptation process
2. Interrupt midway (Ctrl+C simulation)
3. Resume with `/adapt-to-project --resume`
4. Complete adaptation
5. Test `/undo-adaptation`
6. Re-run adaptation

**Validation**:
- Partial state properly saved
- Resume works correctly
- Undo restores previous state
- No data corruption

### 5. Update Flow Test - Framework Synchronization

**Purpose**: Validate updating framework while preserving customizations

**Setup**:
1. Complete full adaptation
2. Modify some commands locally
3. Simulate framework update

**Test Flow**:
1. Run `/sync-from-reference`
2. Review proposed updates
3. Accept selective updates
4. Verify customizations preserved

**Validation**:
- Local changes not overwritten
- New framework features added
- Conflict resolution works
- History properly tracked

### 6. Multi-Domain Test - Mixed Technology Stack

**Purpose**: Test complex projects with multiple technologies

**Setup**:
```bash
# Project with React frontend, Python backend, PostgreSQL
mkdir test-fullstack && cd test-fullstack
echo '{"name": "frontend"}' > frontend/package.json
echo "flask==2.3.0" > backend/requirements.txt
echo "DATABASE_URL=postgresql://..." > .env
```

**Test Flow**:
1. Run adaptation detecting multiple stacks
2. Configure for fullstack development
3. Verify cross-stack adaptations

**Validation**:
- Both frontend and backend detected
- API commands configured for both
- Database commands for PostgreSQL
- Deployment considers full stack

### 7. Performance Test - Large Project Adaptation

**Purpose**: Validate performance with many files/placeholders

**Test Flow**:
1. Create project with 100+ files
2. Run adaptation in express mode
3. Measure time for each phase
4. Check memory usage

**Performance Targets**:
- Setup: <30 seconds
- Adaptation: <3 minutes
- Placeholder replacement: <1 minute
- Total time: <5 minutes

### 8. Community Pattern Test - Import & Export

**Purpose**: Test sharing adaptation patterns

**Test Flow**:
1. Complete custom adaptation
2. Run `/export-adaptation-pattern`
3. In new project, import pattern
4. Verify pattern application

**Validation**:
- Export creates valid pattern file
- Import applies configurations
- Customizations transfer correctly
- Attribution maintained

## Test Automation Script

```bash
#!/bin/bash
# test-adaptation-engine.sh

run_test() {
    local test_name=$1
    local test_dir=$2
    echo "Running: $test_name"
    
    # Create test environment
    mkdir -p "$test_dir"
    cd "$test_dir"
    
    # Run specific test scenario
    case $test_name in
        "quick-start")
            test_quick_start
            ;;
        "enterprise")
            test_enterprise
            ;;
        "data-science")
            test_data_science
            ;;
        *)
            echo "Unknown test: $test_name"
            ;;
    esac
    
    # Validate results
    validate_adaptation
    
    # Cleanup
    cd ..
    rm -rf "$test_dir"
}

validate_adaptation() {
    # Check readiness score
    .claude/validate.sh
    
    # Check for unreplaced placeholders
    if grep -r "INSERT_" .claude/commands/; then
        echo "FAIL: Unreplaced placeholders found"
        return 1
    fi
    
    echo "PASS: Adaptation validated"
    return 0
}

# Run all tests
for test in quick-start enterprise data-science edge-case update multi-domain performance community; do
    run_test "$test" "test-$test-$$"
done
```

## Success Criteria

### Functional Success
- All test scenarios pass
- Readiness scores >80% for all tests
- No unreplaced placeholders
- Commands work in Claude Code

### Performance Success
- Total adaptation <5 minutes
- Responsive during interaction
- No memory issues

### User Experience Success
- Clear guidance throughout
- Helpful error messages
- Intuitive flow
- Easy recovery from mistakes

## Test Reporting

Generate report showing:
1. Test scenario results
2. Adaptation times
3. Readiness scores
4. Issues found
5. Performance metrics

---
*Test Strategy Version: 1.0*
*Covers: Core flows, edge cases, performance, and user experience*