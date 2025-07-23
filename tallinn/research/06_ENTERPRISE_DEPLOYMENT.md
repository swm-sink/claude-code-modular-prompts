# Enterprise Deployment and Security

## Overview

Claude Code provides enterprise-grade deployment options with built-in security, privacy, and compliance features. Organizations can deploy through Anthropic's API, Amazon Bedrock, or Google Cloud Vertex AI.

## Deployment Options

### 1. Anthropic API (Direct)

**Configuration:**
```bash
export ANTHROPIC_API_KEY="sk-ant-..."
claude
```

**Features:**
- Direct access to latest models
- Simple setup
- Pay-per-use pricing
- Global availability

### 2. Amazon Bedrock

**Configuration:**
```bash
# Enable Bedrock
export CLAUDE_CODE_USE_BEDROCK=1
export AWS_REGION=us-east-1
export ANTHROPIC_MODEL=anthropic.claude-4-opus-20250514-v1:0

# Optional settings
export DISABLE_PROMPT_CACHING=1  # If not supported in region
export ANTHROPIC_BEDROCK_BASE_URL=https://your-gateway.com  # For LLM gateway
```

**Authentication Methods:**
1. **IAM Roles** (Recommended for EC2/ECS)
   ```bash
   # Automatic role assumption
   aws configure
   ```

2. **IAM Identity Center (SSO)**
   ```bash
   aws configure sso
   aws sso login
   ```

3. **Access Keys** (Development only)
   ```bash
   export AWS_ACCESS_KEY_ID=...
   export AWS_SECRET_ACCESS_KEY=...
   ```

**Security Certifications:**
- **FedRAMP High**: Approved for high-sensitivity government workloads
- **FedRAMP Moderate**: Standard government compliance
- **DoD IL2**: Unclassified DoD information
- **DoD IL4/5**: Controlled Unclassified Information (CUI)

**Performance Benefits:**
- Prompt caching: 90% cost reduction, 85% latency reduction
- Regional deployment for data residency
- VPC endpoint support for network isolation

### 3. Google Cloud Vertex AI

**Configuration:**
```bash
# Enable Vertex AI
export CLAUDE_CODE_USE_VERTEX=1
export CLOUD_ML_REGION=us-central1
export ANTHROPIC_VERTEX_PROJECT_ID=your-project-id

# Authentication
gcloud auth application-default login
```

**Enterprise Examples:**
- **Replit**: Uses Vertex AI for scalability, integrates with Cloud Run, Cloud SQL, BigQuery
- **Augment**: SOC 2 Level 2 certified deployment, "everything stays inside Google Cloud"

**Integration Benefits:**
- Native GCP service integration
- Cloud IAM for access control
- VPC Service Controls
- Cloud Audit Logging

## Corporate Infrastructure Support

### 1. Proxy Configuration

**HTTP/HTTPS Proxy:**
```bash
export HTTP_PROXY=http://proxy.company.com:8080
export HTTPS_PROXY=http://proxy.company.com:8080
export NO_PROXY=localhost,127.0.0.1,.company.internal
```

**SSL/TLS with Corporate CA:**
```bash
export NODE_EXTRA_CA_CERTS=/path/to/company-ca-bundle.crt
export SSL_CERT_FILE=/path/to/company-ca-bundle.crt
```

### 2. LLM Gateway Integration

**Purpose:**
- Centralized model access
- Usage tracking and budgeting
- Audit logging
- Rate limiting

**Configuration:**
```bash
# For Bedrock gateway
export ANTHROPIC_BEDROCK_BASE_URL=https://llm-gateway.company.com
export CLAUDE_CODE_SKIP_BEDROCK_AUTH=1  # Gateway handles auth

# For Vertex gateway
export ANTHROPIC_VERTEX_BASE_URL=https://llm-gateway.company.com
export CLAUDE_CODE_SKIP_VERTEX_AUTH=1  # Gateway handles auth
```

**AWS Gateway Example:**
Organizations can implement generative AI gateways on AWS for:
- Cost tracking across teams
- Usage attribution
- Compliance logging
- Model governance

### 3. Centralized Management

**Managed Permissions:**
Security teams can configure:
- Allowed/denied tools
- File access restrictions
- Network access controls
- Command execution limits

**Configuration Override Prevention:**
Central configs cannot be overwritten by local settings, ensuring compliance.

## Security Best Practices

### 1. Authentication & Authorization

**Multi-Factor Authentication:**
- Enforce MFA for all Claude Code users
- Use hardware security keys when possible
- Regular credential rotation

**Role-Based Access Control:**
```json
{
  "roles": {
    "developer": {
      "allowed_tools": ["Read", "Write", "Grep"],
      "denied_tools": ["Bash"]
    },
    "admin": {
      "allowed_tools": ["*"],
      "denied_tools": []
    }
  }
}
```

### 2. Data Protection

**Encryption:**
- Data in transit: TLS 1.2+
- Data at rest: Provider-managed encryption
- Key management: AWS KMS or Google Cloud KMS

**Data Residency:**
- Deploy in specific regions for compliance
- Use regional endpoints
- Configure data retention policies

### 3. Network Security

**VPC Deployment:**
```yaml
# AWS VPC Endpoint
aws ec2 create-vpc-endpoint \
  --vpc-id vpc-12345678 \
  --service-name com.amazonaws.region.bedrock-runtime
```

**Firewall Rules:**
- Whitelist only necessary endpoints
- Block direct internet access
- Use private endpoints when available

### 4. Audit & Compliance

**Logging Configuration:**
```json
{
  "logging": {
    "level": "info",
    "destinations": ["cloudwatch", "splunk"],
    "include_prompts": false,  // Privacy consideration
    "include_outputs": false,
    "include_metadata": true
  }
}
```

**Compliance Reports:**
- Usage analytics
- Access patterns
- Security incidents
- Performance metrics

## Enterprise Features

### 1. Team Collaboration

**Shared Configuration:**
```bash
# Project-level config
cat > .claude/enterprise.json << EOF
{
  "model": "claude-opus-4",
  "max_tokens": 4096,
  "temperature": 0.7,
  "allowed_paths": ["src/", "tests/"],
  "denied_paths": ["secrets/", ".env"]
}
EOF
```

**Centralized Commands:**
Store in version control:
```
.claude/
├── commands/
│   ├── security-review.md
│   ├── compliance-check.md
│   └── architecture-review.md
└── enterprise.json
```

### 2. Cost Management

**Budget Controls:**
```json
{
  "budgets": {
    "monthly_limit": 10000,
    "daily_limit": 500,
    "per_user_limit": 100,
    "alert_thresholds": [0.5, 0.75, 0.9]
  }
}
```

**Usage Tracking:**
```bash
# Generate usage report
claude usage --format csv --start 2025-01-01 --end 2025-01-31

# Real-time monitoring
claude monitor --dashboard
```

### 3. Performance at Scale

**Load Balancing:**
- Multiple region deployment
- Automatic failover
- Request routing optimization

**Caching Strategy:**
- Prompt caching for repeated queries
- Response caching for deterministic operations
- Context caching for large codebases

## Deployment Patterns

### 1. Developer Workstations

```bash
# Installation script
#!/bin/bash
npm install -g @anthropic-ai/claude-code
claude configure --enterprise
claude login --sso
```

### 2. CI/CD Integration

```yaml
# GitHub Actions
- name: Claude Code Analysis
  env:
    CLAUDE_CODE_USE_BEDROCK: 1
    AWS_REGION: us-east-1
  run: |
    claude -p "Review code for security vulnerabilities" \
      --output-format json > security-report.json
```

### 3. Container Deployment

```dockerfile
FROM node:18-alpine
RUN npm install -g @anthropic-ai/claude-code
ENV CLAUDE_CODE_USE_VERTEX=1
COPY .claude /root/.claude
CMD ["claude", "server", "--port", "8080"]
```

## Security Incident Response

### 1. Access Revocation
```bash
# Immediate key rotation
claude admin revoke-key --user user@company.com

# Audit trail
claude admin audit --user user@company.com --days 30
```

### 2. Data Retention
- Configure automatic log deletion
- Implement data classification
- Regular compliance audits

### 3. Monitoring & Alerts
```json
{
  "alerts": {
    "suspicious_activity": {
      "threshold": 100,
      "window": "1h",
      "notify": ["security@company.com"]
    }
  }
}
```

## Compliance Frameworks

### Supported Standards
- **SOC 2 Type II**
- **ISO 27001**
- **HIPAA** (with BAA)
- **GDPR**
- **CCPA**

### Implementation Guidelines
1. Enable audit logging
2. Configure data retention
3. Implement access controls
4. Regular security reviews
5. Incident response procedures