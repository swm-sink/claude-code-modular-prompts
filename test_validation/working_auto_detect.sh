#!/bin/bash
# WORKING Auto-Detection Script
# Demonstrates FUNCTIONAL tech stack detection

detect_language() {
    if [ -f "package.json" ]; then echo "javascript"
    elif [ -f "requirements.txt" ] || [ -f "pyproject.toml" ]; then echo "python"
    elif [ -f "go.mod" ]; then echo "go"
    elif [ -f "Cargo.toml" ]; then echo "rust"
    elif [ -f "pom.xml" ]; then echo "java"
    else echo "generic"
    fi
}

detect_framework() {
    LANG=$(detect_language)
    case $LANG in
        javascript)
            if grep -q "react" package.json 2>/dev/null; then echo "react"
            elif grep -q "vue" package.json 2>/dev/null; then echo "vue"
            elif grep -q "express" package.json 2>/dev/null; then echo "express"
            else echo "vanilla-js"
            fi
            ;;
        python)
            if [ -f "manage.py" ]; then echo "django"
            elif [ -f "requirements.txt" ] && grep -q "flask" requirements.txt 2>/dev/null; then echo "flask"
            elif [ -f "requirements.txt" ] && grep -q "fastapi" requirements.txt 2>/dev/null; then echo "fastapi"
            else echo "python-generic"
            fi
            ;;
        *) echo "generic" ;;
    esac
}

detect_test_framework() {
    if [ -f "jest.config.js" ] || grep -q "jest" package.json 2>/dev/null; then echo "jest"
    elif [ -f "pytest.ini" ] || ([ -f "requirements.txt" ] && grep -q "pytest" requirements.txt 2>/dev/null); then echo "pytest"
    else echo "auto"
    fi
}

# Run detection
echo "=== WORKING AUTO-DETECTION RESULTS ==="
echo "Language: $(detect_language)"
echo "Framework: $(detect_framework)"
echo "Test Framework: $(detect_test_framework)"

# Generate appropriate defaults
LANG=$(detect_language)
FRAMEWORK=$(detect_framework)

echo ""
echo "=== SMART DEFAULTS GENERATED ==="
case $FRAMEWORK in
    react)
        echo "source_directory=src"
        echo "test_directory=src/__tests__"
        echo "build_directory=build"
        echo "test_tool=jest"
        echo "linter=eslint"
        echo "formatter=prettier"
        echo "coverage_threshold=80"
        ;;
    python-generic|django|flask|fastapi)
        echo "source_directory=src"
        echo "test_directory=tests"
        echo "test_tool=pytest"
        echo "linter=pylint"
        echo "formatter=black"
        echo "coverage_threshold=85"
        ;;
    *)
        echo "source_directory=src"
        echo "test_directory=tests"
        echo "coverage_threshold=75"
        ;;
esac