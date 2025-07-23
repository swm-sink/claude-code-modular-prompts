#!/bin/bash
# Staging Rollback Script

echo "🔄 Rolling back staging deployment..."

# Get previous deployment
PREVIOUS=$(railway deployments --json | jq -r '.[1].id')

if [ -z "$PREVIOUS" ]; then
    echo "❌ No previous deployment found"
    exit 1
fi

# Rollback
railway rollback $PREVIOUS --environment staging

echo "✅ Rollback completed"
