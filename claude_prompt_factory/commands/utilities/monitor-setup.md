# Monitor Setup Command

**Command**: `/monitor setup`  
**Category**: 📊 Monitoring  
**Purpose**: Setup comprehensive monitoring infrastructure for development and production systems

## Command Execution

You are setting up monitoring infrastructure with industry best practices for 2025.

### 1. Assess Current Environment
- Identify project type (web app, API, AI/ML, microservices)
- Check existing monitoring tools (logs, metrics, APM)
- Evaluate infrastructure (cloud, on-premise, containerized)
- Document current observability gaps

### 2. Configure Core Monitoring Stack
- **Metrics Collection**: Setup Prometheus, CloudWatch, or DataDog
- **Logging**: Configure structured logging (JSON format preferred)
- **Tracing**: Implement OpenTelemetry for distributed tracing
- **Health Checks**: Create endpoint monitoring and availability checks

### 3. Initialize Key Metrics
- **Performance**: Response time, throughput, error rates
- **Infrastructure**: CPU, memory, disk, network utilization
- **Business**: User activity, conversion rates, feature usage
- **AI/LLM**: Token usage, model latency, accuracy metrics (if applicable)

### 4. Setup Alerting Rules
- **Critical**: System down, high error rates (>5%)
- **Warning**: Performance degradation, resource limits (>80%)
- **Info**: Deployment notifications, unusual patterns
- Configure notification channels (Slack, email, PagerDuty)

### 5. Verify Monitoring Works
- Generate test metrics and alerts
- Validate data collection pipelines
- Test alerting notification delivery
- Create monitoring dashboard with key KPIs
- Document monitoring runbook

## Success Criteria
✅ Metrics collection functioning  
✅ Structured logging enabled  
✅ Alerting rules configured  
✅ Dashboard accessible  
✅ Documentation updated