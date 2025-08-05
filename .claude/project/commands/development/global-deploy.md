---
name: /global-deploy
description: Advanced global deployment with AI-driven localization and multi-region orchestration (v1.0)
version: "1.0"
usage: '/global-deploy [regions] [--strategy blue-green|canary|rolling] [--localize auto|manual] [--compliance]'
category: development
allowed-tools:
- Read
- Write
- Edit
- Bash
- Grep
- WebSearch
dependencies:
- /deploy
- /env-setup
- /protocol
- /monitor
validation:
  pre-execution: "Validate regions, check compliance requirements, verify infrastructure"
  during-execution: "Monitor deployment progress, track performance metrics, manage traffic"
  post-execution: "Verify global health, validate localization, confirm compliance"
interactive-consultation:
  layer-integration: "Phase 1: Single region deploy, Phase 2: Multi-region with basic routing, Phase 3: Full global orchestration"
  options:
    - name: regional
      description: "Deploy to single region with basic configuration"
    - name: multi-region
      description: "Deploy across regions with traffic management"
    - name: global
      description: "Full global deployment with cultural adaptation"
safety-checks:
  - "Regional compliance validation"
  - "Data sovereignty verification"
  - "Cultural sensitivity review"
  - "Performance baseline checks"
error-recovery:
  - "Regional rollback capabilities"
  - "Traffic rerouting procedures"
  - "Cross-region failover"
performance:
  - "CDN optimization"
  - "Regional caching strategies"
  - "Load balancing algorithms"
ai-features:
  - "Intelligent region selection"
  - "Cultural adaptation engine"
  - "Automatic localization"
  - "Performance prediction"
---

# Global Deployment Orchestrator (v1.0)

Advanced global deployment system with AI-driven localization, cultural intelligence, and multi-region orchestration capabilities.

## 🌍 Interactive Consultation Phases

### Phase 1: Regional Deployment (5 minutes)
```bash
/global-deploy US              # Deploy to single region
/global-deploy EU --gdpr        # EU deployment with compliance
/global-deploy APAC --optimize  # Asia-Pacific with CDN optimization
```

### Phase 2: Multi-Region Deployment (15 minutes)
```bash
/global-deploy "US,EU,APAC" --strategy canary
/global-deploy "US,EU" --traffic-split 70:30
/global-deploy global --exclude "CN,RU"
```

### Phase 3: Full Global Orchestration (30+ minutes)
```bash
/global-deploy global --localize auto --compliance full
/global-deploy global --strategy blue-green --cultural-adapt
/global-deploy global --ai-optimize --predict-performance
```

## 🧠 AI-Powered Global Intelligence

### Regional Market Analysis
The system automatically analyzes each target region:

```yaml
regional_intelligence:
  north_america:
    cloud_adoption: high
    preferences: "performance, self-service, automation"
    compliance: "SOC2, CCPA, state-specific"
    peak_hours: "9AM-5PM EST/PST"
    
  europe:
    cloud_adoption: medium-high
    preferences: "privacy, quality, sustainability"
    compliance: "GDPR, national laws, data residency"
    peak_hours: "9AM-6PM CET"
    
  asia_pacific:
    cloud_adoption: varied
    preferences: "mobile-first, efficiency, relationships"
    compliance: "country-specific, data localization"
    peak_hours: "varied by country"
```

### Cultural Adaptation Engine
```python
cultural_adaptations = {
    "japan": {
        "ui_density": "high",
        "error_handling": "polite, indirect",
        "color_scheme": "avoid white (funeral)",
        "support": "high-touch, apologetic"
    },
    "germany": {
        "ui_density": "medium",
        "error_handling": "direct, technical",
        "privacy": "maximum transparency",
        "support": "self-service preferred"
    },
    "brazil": {
        "ui_density": "medium",
        "error_handling": "friendly, helpful",
        "community": "social features important",
        "support": "personal touch valued"
    }
}
```

## 🚀 Deployment Strategies

### Blue-Green Global Deployment
```bash
/global-deploy global --strategy blue-green
```
**Process:**
1. **Parallel Infrastructure**: Create green environment in all regions
2. **Regional Validation**: Test each region independently
3. **Coordinated Switch**: Synchronized traffic cutover
4. **Instant Rollback**: One-command global rollback

### Intelligent Canary Rollout
```bash
/global-deploy global --strategy canary --ai-guided
```
**Features:**
- AI selects pilot regions based on risk tolerance
- Automatic performance analysis
- Cultural feedback integration
- Adaptive rollout speed

### Follow-the-Sun Rolling Deployment
```bash
/global-deploy global --strategy rolling --timezone-aware
```
**Benefits:**
- Deploy during each region's low-traffic window
- 24/7 deployment team coordination
- Continuous monitoring handoff
- Zero global downtime

## 🔍 Automatic Localization

### AI-Driven Content Localization
```bash
/global-deploy EU --localize auto
```

**Automatically localizes:**
- User interface text
- Error messages
- Documentation
- Legal notices
- Marketing content

**Cultural considerations:**
- Formal vs informal language
- Technical terminology preferences
- Date/time formats
- Currency displays
- Color psychology

### Technical Localization
```yaml
technical_adaptations:
  payment_methods:
    US: ["credit_card", "paypal", "apple_pay"]
    EU: ["sepa", "ideal", "klarna"]
    JP: ["konbini", "line_pay", "paypay"]
    
  data_residency:
    EU: "frankfurt_datacenter"
    SG: "singapore_datacenter"
    AU: "sydney_datacenter"
    
  performance:
    mobile_first: ["IN", "ID", "PH"]
    desktop_focus: ["US", "DE", "UK"]
    balanced: ["JP", "KR", "SG"]
```

## 📊 Compliance & Regulations

### Automated Compliance Validation
```bash
/global-deploy EU --compliance auto-scan
```

**Checks performed:**
- GDPR compliance (EU)
- CCPA compliance (California)
- Data localization (Russia, China)
- Financial regulations (Singapore)
- Healthcare standards (HIPAA)

### Regional Compliance Matrix
```python
compliance_requirements = {
    "data_retention": {
        "EU": "user-controlled",
        "US": "7 years (financial)",
        "JP": "varies by industry"
    },
    "consent": {
        "EU": "explicit opt-in",
        "US": "opt-out acceptable",
        "CA": "explicit for minors"
    },
    "right_to_delete": {
        "EU": "mandatory",
        "CA": "mandatory",
        "other": "best practice"
    }
}
```

## 🌐 Traffic Management

### Intelligent Global Load Balancing
```bash
/global-deploy global --traffic-optimize
```

**Features:**
- GeoDNS routing
- Latency-based routing
- Cost optimization
- Failover automation

### Regional Traffic Distribution
```yaml
traffic_configuration:
  primary_regions:
    US: 40%
    EU: 35%
    APAC: 25%
    
  failover_pairs:
    US-EAST: US-WEST
    EU-WEST: EU-CENTRAL
    SG: JP
    
  cost_optimization:
    - Use regional CDNs
    - Compress assets by region
    - Cache based on usage patterns
```

## 📈 Performance Optimization

### Regional Performance Tuning
```bash
/global-deploy --analyze-performance
```

**Optimizations:**
- CDN placement strategy
- Regional caching rules
- Asset optimization
- Database replication

### AI Performance Prediction
```python
performance_predictions = {
    "peak_load": {
        "US": "Black Friday capable",
        "CN": "Singles Day ready",
        "IN": "Diwali scale prepared"
    },
    "latency_targets": {
        "tier1_cities": "<100ms",
        "tier2_cities": "<200ms",
        "rural": "<500ms"
    }
}
```

## 🔒 Security & Privacy

### Regional Security Posture
```bash
/global-deploy --security-audit
```

**Security adaptations:**
- Encryption standards by region
- Authentication methods
- Privacy controls
- Audit requirements

### Zero-Trust Global Architecture
- No implicit trust between regions
- Regional security perimeters
- Cross-region authentication
- Audit trail consolidation

## 📱 Monitoring & Observability

### Global Dashboard
```bash
/global-deploy --monitor
```

**Real-time metrics:**
- Regional health status
- Performance by geography
- Compliance violations
- User satisfaction scores

### Cultural Success Metrics
```yaml
success_metrics:
  adoption:
    - Daily active users by region
    - Feature usage patterns
    - Support ticket themes
    
  satisfaction:
    - Regional NPS scores
    - Cultural feedback analysis
    - Local competitor comparison
    
  business:
    - Revenue by region
    - Cost per user
    - Market penetration
```

## 🎯 Quick Deployment Examples

### E-commerce Global Launch
```bash
/global-deploy global --ecommerce --payment-local --tax-comply
```

### SaaS Multi-Region
```bash
/global-deploy "US,EU,APAC" --saas --data-residency --sla 99.99
```

### Mobile App Worldwide
```bash
/global-deploy global --mobile --app-store-optimize --cultural-ui
```

### Enterprise B2B
```bash
/global-deploy enterprise --compliance strict --support 24/7
```

---

Ready to deploy globally? Choose your approach:
- 🌍 **Quick Regional**: Start with single region
- 🌐 **Multi-Region**: Expand across continents
- 🚀 **Full Global**: Complete worldwide orchestration