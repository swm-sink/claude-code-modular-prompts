#!/bin/bash
# export.sh - Package consultation results for sharing
# One of only 5 allowed scripts

set -e

echo "=æ Claude Context Architect - Export"
echo "==================================="

TIMESTAMP=$(date +%Y%m%d_%H%M%S)
EXPORT_DIR="claude-context-export-$TIMESTAMP"

# Create export directory
mkdir -p "$EXPORT_DIR"

# Copy generated content
cp -r .claude "$EXPORT_DIR/" 2>/dev/null || echo "No .claude directory to export"
cp -r outputs/generated-commands "$EXPORT_DIR/" 2>/dev/null || echo "No commands to export"
cp outputs/project-dna/PROJECT-DNA.md "$EXPORT_DIR/" 2>/dev/null || echo "No PROJECT-DNA to export"

# Create archive
tar -czf "$EXPORT_DIR.tar.gz" "$EXPORT_DIR"
rm -rf "$EXPORT_DIR"

echo " Exported to: $EXPORT_DIR.tar.gz"
echo ""
echo "Share this archive with your team to give them:"
echo "- Your project-specific commands"
echo "- Your PROJECT-DNA analysis"
echo "- Your custom context configuration"