# Railway Deployment Guide - Claude Code Framework Dashboard

## Overview
This document provides a comprehensive guide for deploying the Claude Code Framework Dashboard to Railway.app, including configuration, troubleshooting, and best practices.

## Project Information
- **Railway Project ID**: 381cfd91-ef2d-4f30-b467-e2fb2603b451
- **Account**: stefan.menssink@gmail.com
- **Framework**: Streamlit Dashboard for Claude Code Modular Prompts
- **Technology Stack**: Python 3.11, Streamlit, Plotly, NetworkX

## Deployment Configuration

### 1. Railway Configuration (`railway.json`)
```json
{
  "$schema": "https://railway.app/railway.schema.json",
  "build": {
    "builder": "NIXPACKS"
  },
  "deploy": {
    "startCommand": "streamlit run app.py --server.port=$PORT --server.address=0.0.0.0 --server.headless=true",
    "restartPolicyType": "ON_FAILURE",
    "restartPolicyMaxRetries": 10
  }
}
```

**Key Changes Made**:
- Changed from `DOCKERFILE` to `NIXPACKS` builder (Railway recommendation)
- Added explicit `startCommand` using Railway's `$PORT` environment variable
- Configured Streamlit for headless operation suitable for Railway

### 2. Dependencies (`requirements.txt`)
Core dependencies optimized for Railway deployment:
```
streamlit>=1.28.0
plotly>=5.17.0
pandas>=2.1.0
networkx>=3.2
pyvis>=0.3.0
bokeh>=3.2.0
numpy>=1.24.0
pyyaml>=6.0
xmltodict>=0.13.0
markdown>=3.4.0
beautifulsoup4>=4.12.0
streamlit-aggrid>=0.3.0
streamlit-option-menu>=0.3.0
pytest>=7.4.0
pytest-cov>=4.1.0
pytest-mock>=3.11.0
gunicorn>=21.2.0
```

## Deployment Steps

### Phase 1: Initial Setup
1. **Authenticate with Railway**:
   ```bash
   railway login
   # Use: stefan.menssink@gmail.com
   ```

2. **Create Service** (Required for multiple services):
   ```bash
   railway add --service streamlit-dashboard
   ```

3. **Link to Existing Project**:
   ```bash
   railway link 381cfd91-ef2d-4f30-b467-e2fb2603b451
   ```

### Phase 2: Deployment
1. **Deploy with Service Specification**:
   ```bash
   railway up --service=streamlit-dashboard
   ```

2. **Monitor Deployment**:
   ```bash
   railway logs --service=streamlit-dashboard
   ```

3. **Get Deployment URL**:
   ```bash
   railway domain --service=streamlit-dashboard
   ```

## Troubleshooting Common Issues

### Issue 1: "Multiple services found"
**Error**: `Multiple services found. Please specify a service via the --service flag`

**Solution**: Always specify the service name:
```bash
railway up --service=streamlit-dashboard
railway logs --service=streamlit-dashboard
```

### Issue 2: Port Configuration
**Problem**: Application not accessible after deployment

**Solution**: Ensure Railway's `$PORT` environment variable is used:
- In `railway.json`: `--server.port=$PORT`
- Railway automatically assigns port (usually 8080 or dynamic)

### Issue 3: Build Failures
**Problem**: DOCKERFILE builder issues

**Solution**: Use NIXPACKS builder (Railway's recommended approach for Python apps):
```json
{
  "build": {
    "builder": "NIXPACKS"
  }
}
```

## Environment Variables
Railway automatically provides:
- `$PORT`: Dynamic port assignment
- `$RAILWAY_*`: Various Railway-specific variables

## Performance Optimization

### Load Time Targets
- **Target**: <3 seconds initial load
- **Response Time**: <1 second for interactions
- **Memory Usage**: <50MB peak

### Optimization Strategies
1. **Streamlit Caching**: Implemented in components
2. **Lazy Loading**: Data loaded on-demand
3. **Efficient Data Structures**: Optimized parsing and rendering

## Quality Gates

### Validation Checklist
- [ ] Railway deployment successful
- [ ] Application accessible via provided URL
- [ ] All Phase 1 features functional
- [ ] Performance targets met
- [ ] Error handling working correctly
- [ ] Mobile responsiveness verified

### Testing on Railway
1. **Smoke Tests**:
   - Dashboard loads without errors
   - Navigation works correctly
   - Framework data displays properly

2. **Performance Tests**:
   - Load time measurement
   - Response time validation
   - Memory usage monitoring

3. **Integration Tests**:
   - Directory visualization renders
   - Search functionality works
   - Data parsing operates correctly

## Monitoring and Maintenance

### Log Monitoring
```bash
# Real-time logs
railway logs --service=streamlit-dashboard --follow

# Recent logs
railway logs --service=streamlit-dashboard --tail=100
```

### Health Checks
Railway automatically monitors application health:
- HTTP response codes
- Application startup time
- Memory and CPU usage

### Restart Policies
Configured in `railway.json`:
- **Policy**: `ON_FAILURE`
- **Max Retries**: 10
- **Automatic restart** on application crashes

## Security Considerations

### Environment Security
- No sensitive data in source code
- Environment variables for configuration
- HTTPS enforced by Railway by default

### Application Security
- Input validation in Streamlit components
- Safe file operations
- Error handling prevents information disclosure

## File References
- **Configuration**: `streamlit_dashboard/railway.json`
- **Dependencies**: `streamlit_dashboard/requirements.txt`
- **Application**: `streamlit_dashboard/app.py`
- **Components**: `streamlit_dashboard/components/`
- **Documentation**: `streamlit_dashboard/RAILWAY_DEPLOYMENT_GUIDE.md`

## Next Steps
1. Complete initial deployment validation
2. Monitor performance metrics
3. Implement Phase 2 features
4. Set up custom domain (optional)
5. Configure analytics and monitoring

## Support and Resources
- **Railway Documentation**: https://docs.railway.app/
- **Streamlit Deployment**: https://docs.streamlit.io/streamlit-community-cloud/deploy-your-app
- **Project Repository**: https://github.com/swm-sink/claude-code-modular-prompts

---
**Document Version**: 1.0  
**Last Updated**: 2025-07-17  
**Status**: Active Deployment Guide