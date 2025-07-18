# Security Guidelines - Claude Code Framework Dashboard

## 🔒 Security Overview

This document outlines security best practices and guidelines for the Claude Code Framework Dashboard deployment and development.

## 🚨 Critical Security Rules

### Environment Variables & API Keys

1. **NEVER commit API keys or secrets**
   - All sensitive data MUST be in `.env` (which is gitignored)
   - Use `.env.template` for documenting required variables
   - Railway environment variables are set via CLI/dashboard only

2. **API Key Management**
   ```bash
   # ✅ CORRECT: Set in Railway dashboard/CLI
   railway variables set GEMINI_API_KEY=your_actual_key
   
   # ❌ NEVER: Hardcode in source code
   API_KEY = "AIza..." # NEVER DO THIS
   ```

3. **Environment Detection**
   - Local development: Uses `.env` file (gitignored)
   - Railway production: Uses Railway environment variables
   - Automatic fallback to environment-specific defaults

### Railway Deployment Security

1. **Environment Variables**
   ```bash
   # Required for production
   ENVIRONMENT=production
   GEMINI_API_KEY=your_key_here
   ```

2. **Security Headers (Automatic)**
   - Railway provides HTTPS by default
   - Security headers automatically configured
   - No additional SSL setup required

### Code Security

1. **Input Validation**
   - All user inputs validated before processing
   - Path traversal protection in file operations
   - JSON schema validation for API endpoints

2. **Error Handling**
   - No sensitive information in error messages
   - Graceful degradation for missing data
   - Structured logging without secrets

3. **Data Privacy**
   - Analytics session data NOT committed to git
   - User data stored temporarily and locally only
   - No persistent user data storage in production

## 🛡️ Security Checklist

### Pre-Deployment
- [ ] `.env` file contains only template values
- [ ] Real API keys set in Railway environment variables
- [ ] No hardcoded secrets in source code
- [ ] Error messages don't expose sensitive information
- [ ] Input validation implemented for all user inputs

### Production Monitoring
- [ ] Railway deployment logs monitored
- [ ] Error tracking configured (non-sensitive data only)
- [ ] Performance monitoring active
- [ ] Security headers validated

### Development
- [ ] Local `.env` file never committed
- [ ] API keys rotated regularly
- [ ] Dependencies regularly updated for security patches
- [ ] Security scanning integrated into development workflow

## 🔍 Security Verification

### Check for Exposed Secrets
```bash
# Search for potential hardcoded secrets
grep -r "API_KEY\|SECRET\|PASSWORD\|TOKEN" . --exclude-dir=.git --exclude="*.log"

# Verify .env is gitignored
git check-ignore .env || echo "WARNING: .env not in .gitignore!"

# Check git history for accidentally committed secrets
git log --oneline -p | grep -i "api.*key\|secret\|password"
```

### Railway Security Validation
```bash
# Verify environment variables are set
railway variables

# Check deployment security
railway logs | grep -i "error\|security\|auth"
```

## 🚨 Incident Response

### If API Key is Compromised
1. **Immediately revoke** the exposed API key
2. **Generate new** API key from provider
3. **Update** Railway environment variables
4. **Redeploy** application with new key
5. **Monitor** for unusual API usage

### If Security Breach Detected
1. **Document** the incident details
2. **Isolate** affected systems
3. **Rotate** all credentials
4. **Review** access logs
5. **Implement** additional safeguards

## 📞 Security Contacts

- **Repository Owner**: stefan.menssink@gmail.com
- **Emergency Response**: Create GitHub issue with 'security' label
- **API Provider**: Follow Gemini AI security reporting procedures

## 🔄 Security Updates

This document is regularly reviewed and updated. Last updated: 2025-07-18

### Version History
- v1.0.0 (2025-07-18): Initial security guidelines
- Focus on Railway deployment security
- Environment variable protection
- API key management best practices

---

**Remember**: Security is everyone's responsibility. When in doubt, err on the side of caution.