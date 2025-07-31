#!/bin/bash
# Production Installation Script for Claude Code Modular Prompts
set -e

echo "🚀 Installing Claude Code Modular Prompts Template Library..."

# Method 1: Git Submodule (Recommended)
if [ "$1" = "submodule" ]; then
    git submodule add https://github.com/swm-sink/claude-code-modular-prompts .claude-framework
    cd .claude-framework && ./setup.sh
    echo "✅ Installed as git submodule"
    
# Method 2: Direct Integration  
elif [ "$1" = "direct" ]; then
    git clone https://github.com/swm-sink/claude-code-modular-prompts
    cd claude-code-modular-prompts && ./setup.sh ../$(basename "$PWD")
    echo "✅ Installed via direct integration"
    
# Method 3: Quick Start (Default)
else
    if [ ! -d ".claude" ]; then
        mkdir -p .claude
    fi
    echo "📋 Template library ready for manual setup"
    echo "📖 Run /welcome command in Claude Code for guided setup"
fi

echo "🎉 Installation complete! Use /welcome command to get started."
