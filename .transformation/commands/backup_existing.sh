#!/usr/bin/env bash
# File: .transformation/commands/backup_existing.sh
set -euo pipefail

TIMESTAMP=$(date +%Y%m%d_%H%M%S)
BACKUP_DIR=".backup_${TIMESTAMP}"

if [[ -d ".claude" ]]; then
    echo "📦 Backing up existing .claude/ to $BACKUP_DIR/"
    mkdir -p "$BACKUP_DIR"
    cp -r .claude "$BACKUP_DIR/"
    echo "✅ Backup complete: $BACKUP_DIR"
    
    # Count items backed up
    ITEM_COUNT=$(find "$BACKUP_DIR/.claude" -type f | wc -l | tr -d ' ')
    echo "📊 Backed up $ITEM_COUNT files"
else
    echo "ℹ️  No existing .claude/ directory to backup"
fi