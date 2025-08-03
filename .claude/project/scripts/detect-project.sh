#!/bin/bash
# Project Detection Script for /adapt-to-project command
# This script detects project type and generates replacement values

set -e

PROJECT_DIR="${1:-.}"
OUTPUT_FILE="${2:-/tmp/project-detection.json}"

echo "🔍 Detecting project type in: $PROJECT_DIR"

# Initialize detection results
PROJECT_NAME=""
DOMAIN=""
TECH_STACK=""
PRIMARY_LANGUAGE=""
TESTING_FRAMEWORK=""
CI_CD_PLATFORM="GitHub Actions"

# Detect project name from directory
PROJECT_NAME=$(basename "$PROJECT_DIR")

# Check for different project types
if [ -f "$PROJECT_DIR/package.json" ]; then
    echo "📦 Found package.json - JavaScript/Node.js project detected"
    PRIMARY_LANGUAGE="JavaScript"
    
    # Extract project name from package.json if available
    if command -v jq >/dev/null 2>&1; then
        PKG_NAME=$(jq -r '.name // empty' "$PROJECT_DIR/package.json" 2>/dev/null)
        if [ -n "$PKG_NAME" ]; then
            PROJECT_NAME="$PKG_NAME"
        fi
    fi
    
    # Check for React
    if grep -q '"react"' "$PROJECT_DIR/package.json" 2>/dev/null; then
        echo "⚛️ React detected"
        DOMAIN="web-dev"
        TECH_STACK="React, Node.js"
        TESTING_FRAMEWORK="Jest"
    else
        echo "🟢 Node.js project detected"
        DOMAIN="backend"
        TECH_STACK="Node.js"
        TESTING_FRAMEWORK="Jest"
    fi
    
elif [ -f "$PROJECT_DIR/requirements.txt" ] || [ -f "$PROJECT_DIR/setup.py" ] || [ -f "$PROJECT_DIR/pyproject.toml" ]; then
    echo "🐍 Python project detected"
    PRIMARY_LANGUAGE="Python"
    DOMAIN="backend"
    TECH_STACK="Python"
    TESTING_FRAMEWORK="pytest"
    
    # Check for data science indicators
    if grep -qi -E "(pandas|numpy|scikit-learn|tensorflow|pytorch)" "$PROJECT_DIR/requirements.txt" 2>/dev/null ||
       find "$PROJECT_DIR" -name "*.ipynb" -type f | head -1 | grep -q ".*"; then
        echo "📊 Data Science project detected"
        DOMAIN="data-science"
        TECH_STACK="Python, pandas, numpy"
    fi
    
elif [ -f "$PROJECT_DIR/pom.xml" ]; then
    echo "☕ Java Maven project detected"
    PRIMARY_LANGUAGE="Java"
    DOMAIN="backend"
    TECH_STACK="Java, Maven"
    TESTING_FRAMEWORK="JUnit"
    
    # Try to extract project name from pom.xml
    if command -v xmllint >/dev/null 2>&1; then
        ARTIFACT_ID=$(xmllint --xpath "//artifactId/text()" "$PROJECT_DIR/pom.xml" 2>/dev/null | head -1)
        if [ -n "$ARTIFACT_ID" ]; then
            PROJECT_NAME="$ARTIFACT_ID"
        fi
    fi
    
elif [ -f "$PROJECT_DIR/build.gradle" ]; then
    echo "🐘 Java Gradle project detected"
    PRIMARY_LANGUAGE="Java"
    DOMAIN="backend"
    TECH_STACK="Java, Gradle"
    TESTING_FRAMEWORK="JUnit"
    
elif [ -f "$PROJECT_DIR/go.mod" ]; then
    echo "🐹 Go project detected"
    PRIMARY_LANGUAGE="Go"
    DOMAIN="backend"
    TECH_STACK="Go"
    TESTING_FRAMEWORK="Go Test"
    
elif [ -f "$PROJECT_DIR/Cargo.toml" ]; then
    echo "🦀 Rust project detected"
    PRIMARY_LANGUAGE="Rust"
    DOMAIN="backend"
    TECH_STACK="Rust"
    TESTING_FRAMEWORK="Cargo Test"
    
else
    echo "❓ Unknown project type - using defaults"
    PRIMARY_LANGUAGE="Unknown"
    DOMAIN="general"
    TECH_STACK="Mixed"
    TESTING_FRAMEWORK="Manual"
fi

# Generate JSON output
cat > "$OUTPUT_FILE" << EOF
{
  "project_name": "$PROJECT_NAME",
  "domain": "$DOMAIN",
  "tech_stack": "$TECH_STACK",
  "primary_language": "$PRIMARY_LANGUAGE",
  "testing_framework": "$TESTING_FRAMEWORK",
  "ci_cd_platform": "$CI_CD_PLATFORM"
}
EOF

echo "✅ Detection complete! Results saved to $OUTPUT_FILE"
echo ""
echo "📋 Detected Configuration:"
echo "  Project Name: $PROJECT_NAME"
echo "  Domain: $DOMAIN" 
echo "  Tech Stack: $TECH_STACK"
echo "  Primary Language: $PRIMARY_LANGUAGE"
echo "  Testing Framework: $TESTING_FRAMEWORK"
echo "  CI/CD Platform: $CI_CD_PLATFORM"