#!/usr/bin/env bash
# File: .submodule/detect_mode.sh
set -euo pipefail

# Function to find project root
find_project_root() {
    local dir="${1:-$(pwd)}"
    while [[ "$dir" != "/" ]]; do
        if [[ -f "$dir/.transformation/active" ]] || [[ -f "$dir/.transformation/MODE" ]]; then
            echo "$dir"
            return 0
        fi
        # Also check if we're in a git repo
        if git -C "$dir" rev-parse --show-toplevel >/dev/null 2>&1; then
            echo "$(git -C "$dir" rev-parse --show-toplevel)"
            return 0
        fi
        dir="$(dirname "$dir")"
    done
    echo "$(pwd)"
}

# Detect execution mode with multiple fallbacks
CLAUDE_ROOT="${CLAUDE_ROOT:-$(find_project_root)}"

# Method 1: Check marker file
if [[ -f "$CLAUDE_ROOT/.transformation/active" ]]; then
    CLAUDE_MODE="transformation"
# Method 2: Check backup marker
elif [[ -f "$CLAUDE_ROOT/.transformation/MODE" ]] && [[ "$(cat "$CLAUDE_ROOT/.transformation/MODE")" == "transformation" ]]; then
    CLAUDE_MODE="transformation"
# Method 3: Check environment variable override
elif [[ -n "${CLAUDE_MODE_OVERRIDE:-}" ]]; then
    CLAUDE_MODE="$CLAUDE_MODE_OVERRIDE"
# Default: Framework mode
else
    CLAUDE_MODE="framework"
fi

# Set scope based on mode
if [[ "$CLAUDE_MODE" == "transformation" ]]; then
    CLAUDE_SCOPE="$CLAUDE_ROOT"
    CLAUDE_CONTEXT_DIR="$CLAUDE_ROOT/.transformation/context"
else
    # In framework mode, find parent project root
    if [[ -d "$CLAUDE_ROOT/.git" ]] && git -C "$CLAUDE_ROOT" rev-parse --show-superproject-working-tree >/dev/null 2>&1; then
        CLAUDE_SCOPE="$(git -C "$CLAUDE_ROOT" rev-parse --show-superproject-working-tree)"
    else
        CLAUDE_SCOPE="$(cd "$CLAUDE_ROOT/../.." && pwd)"
    fi
    CLAUDE_CONTEXT_DIR="$CLAUDE_ROOT/.claude/framework/context"
fi

# Visual indicator
if [[ "$CLAUDE_MODE" == "transformation" ]]; then
    echo "🔄 MODE: Transformation (Stage 1) - Working on THIS project"
else
    echo "📦 MODE: Framework (Stage 2) - Working on PARENT project"
fi

# Export for child processes
export CLAUDE_MODE CLAUDE_SCOPE CLAUDE_CONTEXT_DIR CLAUDE_ROOT

# Validation
if [[ ! -d "$CLAUDE_SCOPE" ]]; then
    echo "⚠️  Warning: CLAUDE_SCOPE directory not found: $CLAUDE_SCOPE" >&2
fi