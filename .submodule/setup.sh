#!/usr/bin/env bash
# File: .submodule/setup.sh
# Purpose: Initialize Claude Code Context Engineering in parent project
set -euo pipefail

echo "🚀 Claude Code Context Engineering Setup"
echo "========================================"

# Check if we're being run from a git repository
if ! git rev-parse --show-toplevel >/dev/null 2>&1; then
    echo "❌ Error: This script must be run from within a git repository"
    exit 1
fi

PROJECT_ROOT="$(git rev-parse --show-toplevel)"
SUBMODULE_PATH=".claude-context"

echo "📍 Project root: $PROJECT_ROOT"

# Check if submodule already exists
if [[ -d "$PROJECT_ROOT/$SUBMODULE_PATH" ]]; then
    echo "⚠️  Warning: $SUBMODULE_PATH already exists"
    read -p "Do you want to continue? (y/N) " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo "❌ Setup cancelled"
        exit 1
    fi
fi

# Add submodule
echo "📦 Adding Claude Context Engineering as submodule..."
cd "$PROJECT_ROOT"
git submodule add https://github.com/USER/claude-code-modular-prompts.git "$SUBMODULE_PATH"

# Initialize and update submodule
echo "🔄 Initializing submodule..."
git submodule init
git submodule update

# Create initial project structure
echo "🏗️  Creating project context structure..."
mkdir -p .claude/{context,domains,examples,indexes,memory}

# Create initial CLAUDE.md
if [[ ! -f "CLAUDE.md" ]]; then
    echo "📝 Creating CLAUDE.md navigation hub..."
    cat > CLAUDE.md << 'EOF'
# [Project Name] - Claude Code Configuration

## Project Overview
[Brief description of your project]

## Technology Stack
[Your technology stack]

## 🧭 Context Navigation Hub

### 📍 Master Navigation Entry Point
**Start Here**: `.claude/indexes/master-context-index.md`

### 🧭 Claude Code Integration
**Context Engineering System**: `.claude-context/` (git submodule)

### 🎯 Quick Navigation
- **Technical Domain**: `.claude/domains/technical/`
- **Business Domain**: `.claude/domains/business/`
- **Examples**: `.claude/examples/`
- **Memory**: `.claude/memory/`

---

*Powered by Claude Code Context Engineering System*
EOF
fi

# Set up mode detection
echo "🔧 Configuring mode detection..."
echo "framework" > "$SUBMODULE_PATH/.transformation/MODE"

echo "✅ Setup complete!"
echo ""
echo "Next steps:"
echo "1. Edit CLAUDE.md to describe your project"
echo "2. Run: $SUBMODULE_PATH/scaffolding/-1_context/foundation.md"
echo "3. Follow the progressive phases to build your context"
echo ""
echo "📚 Documentation: $SUBMODULE_PATH/.claude/framework/docs/"