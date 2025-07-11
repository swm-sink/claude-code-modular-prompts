# Domain Selection Wizard

| version | last_updated | status |
|---------|--------------|--------|
| 1.0.0   | 2025-07-11   | stable |

## 🧙‍♂️ Interactive Domain Selection

This wizard will help you identify the optimal domain configuration for your Claude Code Framework. Answer the questions below to get personalized recommendations.

## 📊 Domain Assessment

### Question 1: Primary Technology Stack
**What is your primary technology stack?**

A) **Mobile**: iOS (Swift), Android (Kotlin/Java), React Native, Flutter
B) **Web**: JavaScript/TypeScript, Python, Ruby, PHP, Go
C) **Data**: Python (pandas, numpy), R, SQL, Spark, Airflow
D) **Infrastructure**: Docker, Kubernetes, Terraform, AWS/Azure/GCP
E) **Enterprise**: Java, .NET, SAP, Oracle, Legacy systems
F) **AI/ML**: Python, PyTorch, TensorFlow, Jupyter, MLflow

**Your Answer**: _____

### Question 2: Primary Development Activities
**What do you spend most of your time doing?**

A) **User Interface Development**: Building screens, components, user experiences
B) **API Development**: Creating endpoints, integrations, microservices
C) **Data Analysis**: Analyzing data, creating reports, building models
D) **System Operations**: Managing infrastructure, deployments, monitoring
E) **Business Logic**: Implementing workflows, rules, processes
F) **Research & Experimentation**: Prototyping, testing hypotheses, exploring

**Your Answer**: _____

### Question 3: Team Size & Collaboration
**How large is your development team?**

A) **Solo Developer**: Just you, need comprehensive individual support
B) **Small Team (2-5)**: Close collaboration, shared responsibilities
C) **Medium Team (6-15)**: Specialized roles, coordination needed
D) **Large Team (16+)**: Complex coordination, standardization critical
E) **Cross-functional**: Mixed roles (dev, design, product, QA)
F) **Multiple Teams**: Coordinating across different teams/projects

**Your Answer**: _____

### Question 4: Quality Requirements
**What are your quality and compliance requirements?**

A) **High Performance**: Sub-second response times, scalability critical
B) **High Security**: Financial, healthcare, or sensitive data handling
C) **High Availability**: 99.9%+ uptime, disaster recovery
D) **Regulatory Compliance**: SOX, GDPR, HIPAA, PCI-DSS
E) **Rapid Iteration**: Fast prototyping, MVP development
F) **Standard Quality**: Normal business application requirements

**Your Answer**: _____

### Question 5: Development Methodology
**What development methodology do you follow?**

A) **Agile/Scrum**: Sprints, user stories, iterative development
B) **DevOps**: Continuous integration, automated deployment
C) **Waterfall**: Sequential phases, extensive documentation
D) **Lean Startup**: MVP, build-measure-learn cycles
E) **Research-Driven**: Hypothesis testing, experimentation
F) **Maintenance Mode**: Primarily bug fixes and small enhancements

**Your Answer**: _____

## 🎯 Domain Recommendations

Based on your answers, here are the recommended domain configurations:

### Mobile Development Domain
**Best for**: A-A, A-B, B-A, B-B combinations
**Optimal if you answered**:
- Primary tech: iOS, Android, React Native, Flutter
- Activities: UI development, app features
- Focus: User experience, app store deployment

**Framework Customizations**:
- UI/UX validation modules
- Device testing workflows
- App store deployment automation
- Performance optimization for mobile

### Data Analytics Domain
**Best for**: C-C, F-C, C-F combinations
**Optimal if you answered**:
- Primary tech: Python data stack, R, SQL
- Activities: Data analysis, reporting, modeling
- Focus: Data quality, experiment validation

**Framework Customizations**:
- Data validation modules
- Experiment design patterns
- Visualization quality gates
- Statistical analysis workflows

### Financial Technology Domain
**Best for**: B-B, E-B, with B-B or C-B quality requirements
**Optimal if you answered**:
- Technology: Enterprise or web stack
- Activities: Business logic, API development
- Quality: High security, regulatory compliance

**Framework Customizations**:
- Security compliance modules
- Audit trail requirements
- Risk management patterns
- Regulatory validation gates

### DevOps & Platform Domain
**Best for**: D-D, D-B, with B-B or C-B quality requirements
**Optimal if you answered**:
- Technology: Infrastructure tools
- Activities: System operations, deployment
- Quality: High availability, performance

**Framework Customizations**:
- Infrastructure as code patterns
- Deployment automation
- Monitoring and alerting
- Incident response workflows

### Data Engineering Domain
**Best for**: C-C, C-D, with A-A or C-C quality requirements
**Optimal if you answered**:
- Technology: Big data stack
- Activities: Data processing, pipeline development
- Quality: High performance, scalability

**Framework Customizations**:
- Pipeline orchestration patterns
- Data quality validation
- Scalability optimization
- Stream processing workflows

### Enterprise Tools Domain
**Best for**: E-E, E-B, with C-C or D-D methodology
**Optimal if you answered**:
- Technology: Enterprise platforms
- Activities: Business logic, integration
- Team: Large or cross-functional

**Framework Customizations**:
- Integration patterns
- Enterprise security
- Compliance frameworks
- Legacy system handling

### Web Development Domain
**Best for**: B-B, B-A, with A-A or E-E methodology
**Optimal if you answered**:
- Technology: Web stack
- Activities: API/UI development
- Methodology: Agile or rapid iteration

**Framework Customizations**:
- Full-stack development patterns
- API design guidelines
- Frontend/backend coordination
- Performance optimization

### Machine Learning Domain
**Best for**: F-F, F-C, with E-E or F-F methodology
**Optimal if you answered**:
- Technology: ML/AI stack
- Activities: Research, experimentation
- Methodology: Research-driven

**Framework Customizations**:
- Experiment tracking
- Model validation
- ML pipeline patterns
- Research documentation

## 🔍 Domain Selection Matrix

| Your Answers | Recommended Domain | Confidence | Alternative |
|-------------|-------------------|------------|-------------|
| A-A-A/B-A-A | Mobile Development | 95% | Web Development |
| B-B-B/C-B-A | Web Development | 90% | Enterprise Tools |
| C-C-A/B-A-A | Data Analytics | 95% | Data Engineering |
| D-D-B/C-B-B | DevOps & Platform | 90% | Enterprise Tools |
| E-E-C/D-C-C | Enterprise Tools | 85% | Web Development |
| F-F-A/B-E-E | Machine Learning | 90% | Data Analytics |

## 🎨 Customization Preview

### Sample Command Adaptations by Domain

**Mobile Development**:
```
/task "implement swipe gesture for photo gallery"
→ Includes UI testing, device compatibility checks, accessibility validation

/feature "add offline sync capability"
→ Includes data persistence, conflict resolution, sync strategies
```

**Data Analytics**:
```
/task "analyze user engagement patterns"
→ Includes statistical validation, visualization requirements, data quality checks

/feature "build predictive churn model"
→ Includes experiment design, model validation, performance monitoring
```

**Financial Technology**:
```
/task "implement transaction validation"
→ Includes security checks, audit logging, compliance validation

/feature "add payment processing"
→ Includes PCI compliance, risk assessment, fraud detection
```

## 🚀 Next Steps

### Based on Your Selection

1. **Confirm Domain Choice**: Review the recommendation and alternatives
2. **Customize Configuration**: Run the domain-specific setup
3. **Validate Integration**: Test the adapted framework
4. **Team Onboarding**: Share configuration with your team

### Commands to Run

```bash
# Start with your selected domain
/adapt --domain=your-selected-domain --interactive

# Validate the configuration
/validate --comprehensive

# Generate team documentation
/docs --create-team-guide --domain=your-selected-domain
```

## 🔧 Advanced Configuration

### Multi-Domain Projects
If your project spans multiple domains:

```bash
# Primary domain with secondary capabilities
/adapt --domain=primary-domain --secondary=secondary-domain

# Example: Web app with ML components
/adapt --domain=web-development --secondary=machine-learning
```

### Custom Domain Definition
For unique requirements:

```bash
# Create custom domain configuration
/adapt --domain=custom --interactive --advanced
```

## 📊 Validation Checklist

After domain selection, verify:

- [ ] **Commands Work**: All framework commands execute correctly
- [ ] **Domain Fit**: Framework understands your specific needs
- [ ] **Quality Gates**: Validation rules match your standards
- [ ] **Performance**: Commands complete within acceptable timeframes
- [ ] **Team Alignment**: Configuration matches team workflow

## 🎯 Success Metrics

Your domain selection is successful when:

- **Task Completion**: 90%+ of your typical tasks are handled well
- **Time Savings**: 40%+ faster development compared to manual work
- **Quality Consistency**: 95%+ consistency in code quality
- **Team Adoption**: 80%+ team members actively use the framework

---

**🎉 Ready to proceed with your domain selection? Run the adaptation command with your chosen domain!**

```bash
/adapt --domain=your-chosen-domain --interactive
```