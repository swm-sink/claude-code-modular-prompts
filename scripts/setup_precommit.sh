#!/bin/bash
# Setup script for pre-commit hooks

echo "🔧 Setting up pre-commit hooks for Claude Code Framework..."

# Check if pre-commit is installed
if ! command -v pre-commit &> /dev/null; then
    echo "📦 Installing pre-commit..."
    pip install pre-commit
else
    echo "✅ pre-commit is already installed"
fi

# Install the pre-commit hooks
echo "🪝 Installing git hooks..."
pre-commit install

# Run hooks on all files to verify setup
echo "🧪 Testing hooks on all files..."
pre-commit run --all-files || true

echo "✨ Pre-commit setup complete!"
echo ""
echo "The following hooks are now active:"
echo "  - Framework validation (runs on every commit)"
echo "  - Framework tests (runs when .py or .md files change)"
echo "  - Python formatting with Black"
echo "  - Python linting with Ruff"
echo "  - YAML validation"
echo "  - File size limits"
echo ""
echo "To skip hooks in an emergency, use: git commit --no-verify"