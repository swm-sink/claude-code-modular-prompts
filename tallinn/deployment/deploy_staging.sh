#!/bin/bash
# Staging Deployment Script

echo "🚀 Deploying to Staging Environment..."

# Check Railway CLI
if ! command -v railway &> /dev/null; then
    echo "❌ Railway CLI not found. Please install: npm i -g @railway/cli"
    exit 1
fi

# Validate environment
if [ ! -f "deployment/railway.json" ]; then
    echo "❌ Railway configuration not found"
    exit 1
fi

# Run pre-deployment checks
echo "📋 Running pre-deployment checks..."
python3 scripts/quality_gates_validation.py

# Deploy to Railway
echo "🚂 Deploying to Railway..."
railway up --environment staging

# Wait for deployment
echo "⏳ Waiting for deployment to complete..."
sleep 30

# Run health check
echo "💓 Running health check..."
STAGING_URL=$(railway status --json | jq -r '.url')
curl -f "$STAGING_URL/health" || exit 1

echo "✅ Deployment successful!"
echo "🌐 Staging URL: $STAGING_URL"
