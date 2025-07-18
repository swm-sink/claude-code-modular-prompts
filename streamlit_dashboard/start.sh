#!/bin/bash

# Railway startup script for Streamlit
# Handles PORT environment variable properly

# Default port if not set
PORT=${PORT:-8080}

echo "Starting Streamlit on port $PORT"

# Start Streamlit with Railway-compatible configuration
streamlit run app.py \
  --server.port=$PORT \
  --server.address=0.0.0.0 \
  --server.headless=true \
  --browser.gatherUsageStats=false