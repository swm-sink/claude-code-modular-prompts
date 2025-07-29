# Integration Testing Template

## Test Overview
- **Test Suite**: [Integration test name]
- **Commands Under Test**: [List of commands being tested together]
- **Components Under Test**: [List of components being validated]
- **Test Environment**: [Claude Code version, OS, setup details]
- **Test Date**: [YYYY-MM-DD]

## Integration Scope

### ✅ Command-to-Command Integration
- **Primary Command**: `/command-name`
- **Related Commands**: [List commands that work together]
- **Workflow**: [Describe typical usage pattern]
- **Dependencies**: [List command dependencies]

### ✅ Component Integration Matrix
| Component A | Component B | Compatibility | Issues | Notes |
|-------------|-------------|---------------|---------|-------|
| [component-1] | [component-2] | ✅/❌/⚠️ | [list] | [notes] |
| [component-1] | [component-3] | ✅/❌/⚠️ | [list] | [notes] |

### ✅ Tool Integration
- **Tools Required**: [List Claude Code tools needed]
- **Tool Conflicts**: [Any tools that conflict with each other]
- **Permission Requirements**: [Minimum tool permissions needed]

## Pre-Test Setup

### ✅ Environment Preparation
```bash
# 1. Claude Code Environment Setup
echo "Setting up Claude Code environment..."
# Verify Claude Code installation
# Check configuration
# Validate tool permissions

# 2. Test Project Setup  
echo "Creating test project structure..."
# Create minimal project structure
# Add necessary files for testing
# Configure .claude/settings.json

# 3. Component Availability Check
echo "Verifying component availability..."
# Check all required components exist
# Validate component syntax
# Test component loading
```

### ✅ Baseline Testing
- [ ] Individual commands work in isolation
- [ ] Individual components load without errors
- [ ] All required tools are available and functional
- [ ] Test environment is clean and consistent

## Integration Test Cases

### Test Case 1: Basic Command Integration
```bash
# Test: Commands work together in sequence
echo "=== Test Case 1: Basic Command Integration ==="

# Step 1: Execute primary command
echo "Executing primary command..."
# /primary-command [args]
# Capture output and verify success

# Step 2: Execute related command with primary command output
echo "Executing dependent command..."
# /related-command [using output from step 1]
# Verify integration works correctly

# Step 3: Validate combined results
echo "Validating integration results..."
# Check that combined workflow produces expected outcome
# Verify no data loss or corruption between commands
```

### Test Case 2: Component Interaction Testing
```bash
# Test: Components work together without conflicts
echo "=== Test Case 2: Component Interaction Testing ==="

# Step 1: Load command with multiple components
echo "Testing component combination..."
# Load command that uses multiple components
# Verify all components load successfully
# Check for any conflicts or duplicate functionality

# Step 2: Execute command with component interactions
echo "Executing command with component interactions..."
# Run command and monitor component behavior
# Verify components enhance rather than interfere with each other
# Check component execution order and dependencies
```

### Test Case 3: Error Propagation Testing
```bash
# Test: Errors are handled properly across integration points
echo "=== Test Case 3: Error Propagation Testing ==="

# Step 1: Introduce controlled errors
echo "Testing error handling in integrated workflow..."
# Cause intentional error in first command
# Verify error is properly propagated and handled
# Ensure subsequent commands receive appropriate error state

# Step 2: Recovery testing
echo "Testing error recovery..."
# Test that workflow can recover from errors
# Verify cleanup happens appropriately
# Check that partial results are handled correctly
```

### Test Case 4: Performance Integration Testing
```bash
# Test: Performance remains acceptable in integrated scenarios
echo "=== Test Case 4: Performance Integration Testing ==="

# Step 1: Measure individual command performance
echo "Measuring baseline performance..."
# Time individual command execution
# Measure resource usage for each command
# Record baseline metrics

# Step 2: Measure integrated performance
echo "Measuring integrated performance..."
# Time complete workflow execution
# Measure total resource usage
# Compare against sum of individual performances
# Identify any performance degradation
```

### Test Case 5: Concurrent Usage Testing
```bash
# Test: Commands and components handle concurrent usage
echo "=== Test Case 5: Concurrent Usage Testing ==="

# Step 1: Simulate concurrent command execution
echo "Testing concurrent command usage..."
# Run multiple commands simultaneously
# Verify no resource conflicts
# Check that commands don't interfere with each other

# Step 2: Test shared component usage
echo "Testing shared component usage..."
# Multiple commands using same components
# Verify component state is handled correctly
# Check for any race conditions or conflicts
```

## Claude Code Specific Integration Tests

### ✅ Settings Integration
```bash
# Test: Commands respect Claude Code settings and configuration
echo "Testing Claude Code settings integration..."

# Test 1: Tool permissions
# Verify commands only use allowed tools
# Test behavior when tools are restricted

# Test 2: Memory management
# Test commands with different memory settings
# Verify memory usage stays within bounds

# Test 3: Hook integration
# Test commands with various hook configurations
# Verify hooks execute at appropriate times
```

### ✅ Session Management
```bash
# Test: Commands work properly within Claude Code sessions
echo "Testing Claude Code session management..."

# Test 1: Session persistence
# Test commands across session boundaries
# Verify state is maintained appropriately

# Test 2: Context management
# Test commands with different context loads
# Verify context doesn't cause conflicts

# Test 3: Multi-project usage
# Test commands across different project contexts
# Verify proper isolation and functionality
```

## Real-World Workflow Testing

### ✅ Typical User Workflows
**Workflow 1: Development Workflow**
```bash
# Simulate typical development workflow using integrated commands
echo "Testing development workflow..."
# /task "implement new feature"
# /secure-assess
# /test
# Verify complete workflow execution
```

**Workflow 2: Analysis Workflow**  
```bash
# Simulate analysis workflow
echo "Testing analysis workflow..."
# /analyze-code
# /quality-review
# /generate-report
# Verify analysis chain works end-to-end
```

**Workflow 3: Deployment Workflow**
```bash
# Simulate deployment workflow
echo "Testing deployment workflow..."
# /build
# /test-e2e
# /deploy
# Verify deployment pipeline integration
```

## Integration Validation Results

### ✅ Test Results Summary
| Test Case | Status | Duration | Issues | Notes |
|-----------|--------|----------|--------|-------|
| Basic Command Integration | ✅/❌/⚠️ | [time] | [count] | [summary] |
| Component Interaction | ✅/❌/⚠️ | [time] | [count] | [summary] |
| Error Propagation | ✅/❌/⚠️ | [time] | [count] | [summary] |
| Performance Integration | ✅/❌/⚠️ | [time] | [count] | [summary] |
| Concurrent Usage | ✅/❌/⚠️ | [time] | [count] | [summary] |

### ✅ Performance Metrics
- **Individual Command Average**: [X.X seconds]
- **Integrated Workflow Average**: [X.X seconds]  
- **Performance Overhead**: [X%]
- **Memory Usage Peak**: [XXX MB]
- **Resource Efficiency**: [Good/Acceptable/Poor]

### ✅ Issues Found

**Critical Issues (Block Integration)**
1. [List critical integration issues]
2. [Include impact and proposed fixes]

**High Priority Issues** 
1. [List important integration issues]
2. [Include workarounds if available]

**Medium Priority Issues**
1. [List moderate integration issues]
2. [Include optimization opportunities]

**Low Priority Issues**
1. [List minor integration issues]
2. [Include enhancement suggestions]

### ✅ Compatibility Assessment
- **Command Compatibility**: [Excellent/Good/Acceptable/Poor]
- **Component Compatibility**: [Excellent/Good/Acceptable/Poor]
- **Tool Integration**: [Excellent/Good/Acceptable/Poor]
- **Performance Impact**: [Minimal/Acceptable/Concerning/Severe]

### ✅ Recommendations

**Immediate Actions Required**
- [List actions needed before integration approval]
- [Include timelines and responsibilities]

**Future Improvements**
- [List optimization opportunities]
- [Include performance enhancement suggestions]

**Architecture Considerations**
- [List structural improvements for better integration]
- [Include long-term maintainability suggestions]

## Integration Approval

### ✅ Final Assessment
- [ ] **APPROVED** - Integration meets all quality and performance standards
- [ ] **CONDITIONAL** - Integration approved with specified fixes required
- [ ] **NEEDS REWORK** - Integration requires significant improvements
- [ ] **REJECTED** - Integration introduces unacceptable issues

### ✅ Sign-off Requirements
- [ ] **Technical Lead Approval**: Integration meets technical standards
- [ ] **Performance Review**: Integration meets performance requirements  
- [ ] **Security Review**: Integration doesn't introduce security issues
- [ ] **User Experience Review**: Integration maintains good user experience

### ✅ Next Steps
- **Approved Integrations**: [List components/commands approved for production]
- **Required Fixes**: [List specific fixes needed before approval]
- **Monitoring Requirements**: [List ongoing monitoring needs]
- **Next Review Date**: [YYYY-MM-DD]

### ✅ Test Archive
- **Test Data Location**: [Path to test files and results]
- **Log Files**: [Location of detailed test logs]
- **Performance Data**: [Location of performance benchmarks]
- **Issue Tracking**: [Links to issue tracking for found problems]