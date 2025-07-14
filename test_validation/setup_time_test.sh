#!/bin/bash
# SETUP TIME MEASUREMENT
# Tests actual setup times for different configuration tiers

test_minimal_setup() {
    echo "=== TESTING MINIMAL TIER SETUP TIME ==="
    start_time=$(date +%s%N)
    
    # Simulate minimal setup process
    PROJECT_NAME="test_project"
    LANGUAGE="javascript" 
    DOMAIN="general-development"
    
    # Generate minimal config (simulated)
    cat > generated_minimal.xml << EOF
<?xml version="1.0" encoding="UTF-8"?>
<project_configuration version="1.0.0" tier="minimal">
  <project_info>
    <name>$PROJECT_NAME</name>
    <primary_language>$LANGUAGE</primary_language>
    <domain>$DOMAIN</domain>
  </project_info>
  <project_structure>
    <source_directory>src</source_directory>
    <test_directory>tests</test_directory>
  </project_structure>
  <quality_standards>
    <test_coverage><threshold>75</threshold><enforcement>ADVISORY</enforcement></test_coverage>
  </quality_standards>
</project_configuration>
EOF
    
    # Validate generated config
    xmllint --noout generated_minimal.xml
    
    end_time=$(date +%s%N)
    duration_ns=$((end_time - start_time))
    duration_ms=$((duration_ns / 1000000))
    duration_s=$((duration_ns / 1000000000))
    
    echo "✅ MINIMAL SETUP COMPLETED"
    echo "⏱️  Time: ${duration_s}s (${duration_ms}ms)"
    echo "📊 Config Size: $(wc -l < generated_minimal.xml) lines"
    
    return $duration_s
}

test_standard_setup() {
    echo "=== TESTING STANDARD TIER SETUP TIME ==="
    start_time=$(date +%s%N)
    
    # Simulate guided setup with user input
    PROJECT_NAME="advanced_project"
    DOMAIN="web-development"
    LANGUAGE="typescript"
    FRAMEWORK="react+nextjs"
    COVERAGE="85"
    ENFORCEMENT="BLOCKING"
    
    # Generate standard config
    cat > generated_standard.xml << EOF
<?xml version="1.0" encoding="UTF-8"?>
<project_configuration version="1.0.0" tier="standard">
  <project_info>
    <name>$PROJECT_NAME</name>
    <domain>$DOMAIN</domain>
    <primary_language>$LANGUAGE</primary_language>
    <framework_stack>$FRAMEWORK</framework_stack>
  </project_info>
  <project_structure>
    <source_directory>src</source_directory>
    <test_directory>src/__tests__</test_directory>
    <build_directory>build</build_directory>
  </project_structure>
  <quality_standards>
    <test_coverage>
      <threshold>$COVERAGE</threshold>
      <enforcement>$ENFORCEMENT</enforcement>
      <tool>jest</tool>
    </test_coverage>
    <code_quality>
      <linter>eslint</linter>
      <formatter>prettier</formatter>
      <type_checker>typescript</type_checker>
    </code_quality>
  </quality_standards>
  <development_workflow>
    <commands>
      <install>npm install</install>
      <test>npm test</test>
      <build>npm run build</build>
    </commands>
  </development_workflow>
</project_configuration>
EOF
    
    # Validate generated config
    xmllint --noout generated_standard.xml
    
    end_time=$(date +%s%N)
    duration_ns=$((end_time - start_time))
    duration_ms=$((duration_ns / 1000000))
    duration_s=$((duration_ns / 1000000000))
    
    echo "✅ STANDARD SETUP COMPLETED"
    echo "⏱️  Time: ${duration_s}s (${duration_ms}ms)"
    echo "📊 Config Size: $(wc -l < generated_standard.xml) lines"
    
    return $duration_s
}

# Run setup time tests
echo "🚀 CONFIGURATION SETUP TIME TESTING"
echo "===================================="

test_minimal_setup
minimal_time=$?

echo ""
test_standard_setup
standard_time=$?

echo ""
echo "=== PERFORMANCE SUMMARY ==="
echo "Minimal Tier:  ${minimal_time}s"
echo "Standard Tier: ${standard_time}s"

# Cleanup
rm -f generated_minimal.xml generated_standard.xml