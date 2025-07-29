#!/bin/bash
# Claude Code Template Library Setup - Simple Copy Script

set -e

# Get target directory
TARGET_DIR="${1:-.}"

# Create absolute path
if [ ! -d "$TARGET_DIR" ]; then
    mkdir -p "$TARGET_DIR"
fi
TARGET_DIR=$(cd "$TARGET_DIR" && pwd)

# Get script directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Check if .claude directory exists in source
if [ ! -d "$SCRIPT_DIR/.claude" ]; then
    echo "Error: .claude directory not found in $SCRIPT_DIR"
    exit 1
fi

# Backup existing .claude if it exists
if [ -d "$TARGET_DIR/.claude" ]; then
    echo "Backing up existing .claude to .claude.backup"
    mv "$TARGET_DIR/.claude" "$TARGET_DIR/.claude.backup"
fi

# Copy .claude directory
echo "Copying Claude Code templates to $TARGET_DIR/.claude"
cp -r "$SCRIPT_DIR/.claude" "$TARGET_DIR/"

# Create basic CLAUDE.md if it doesn't exist
if [ ! -f "$TARGET_DIR/CLAUDE.md" ]; then
    echo "Creating CLAUDE.md"
    echo "# Claude Code Project" > "$TARGET_DIR/CLAUDE.md"
    echo "" >> "$TARGET_DIR/CLAUDE.md"
    echo "Claude Code template library installed on $(date)" >> "$TARGET_DIR/CLAUDE.md"
fi

echo "Setup complete! Claude Code templates installed in $TARGET_DIR/.claude"