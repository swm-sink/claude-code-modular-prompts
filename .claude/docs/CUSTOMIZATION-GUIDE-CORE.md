# Customization Guide: Core Commands

This guide provides detailed instructions for customizing the 4 essential core commands that form the foundation of your Claude Code framework.

## Overview

Core commands are the most critical templates to customize correctly as they serve as entry points and primary workflows for your project. They include:

- **`/auto`** - Intelligent command router for natural language requests
- **`/help`** - Command guide and assistance system  
- **`/project-task`** - Project-level task coordination
- **`/task`** - Focused development task execution

## Command-by-Command Customization

### 1. `/task` Command

**File**: `.claude/commands/core/task.md`

**Purpose**: Primary workflow command for focused development tasks

#### Essential Placeholders to Replace

| Placeholder | Example Replacement | Impact |
|-------------|-------------------|---------|
| `[INSERT_PROJECT_NAME]` | `"MyWebApp"` | Personalizes all task descriptions |
| `[INSERT_TECH_STACK]` | `"React, Node.js, PostgreSQL"` | Influences approach and suggestions |
| `[INSERT_DOMAIN]` | `"web-dev"` | Determines best practices applied |
| `[INSERT_COMPANY_NAME]` | `"Acme Corp"` | References coding standards |
| `[INSERT_TESTING_FRAMEWORK]` | `"Jest"` | Determines testing approach |

#### Customization Examples

**Web Development Project**:
```markdown
Line 8: /task - Focused Development Workflow for ShopifyApp
Line 10: best practices for React, Node.js, MongoDB projects, with appropriate testing and quality standards for your e-commerce domain.
Line 28: I'll follow Shopify's coding standards and use Jest for testing when appropriate.
```

**Data Science Project**:
```markdown
Line 8: /task - Focused Development Workflow for MLPipeline
Line 10: best practices for Python, TensorFlow, PostgreSQL projects, with appropriate testing and quality standards for your machine-learning domain.
Line 28: I'll follow DataCorp's coding standards and use pytest for testing when appropriate.
```

**DevOps Project**:
```markdown
Line 8: /task - Focused Development Workflow for K8sCluster
Line 10: best practices for Go, Kubernetes, Terraform projects, with appropriate testing and quality standards for your infrastructure domain.
Line 28: I'll follow CloudOps's coding standards and use Go testing for testing when appropriate.
```

#### Domain-Specific Workflow Adaptations

**For Web Development**:
- Add emphasis on responsive design
- Include accessibility considerations
- Reference SEO best practices
- Include browser compatibility notes

**For Data Science**:
- Add data validation steps
- Include model evaluation phases
- Reference reproducibility requirements
- Include data privacy considerations

**For DevOps/Infrastructure**:
- Add security scanning steps
- Include deployment validation
- Reference infrastructure-as-code principles
- Include monitoring and alerting setup

### 2. `/help` Command

**File**: `.claude/commands/core/help.md`

**Purpose**: Primary navigation and assistance for your framework

#### Essential Placeholders to Replace

| Placeholder | Example Replacement | Context Usage |
|-------------|-------------------|---------------|
| `[INSERT_PROJECT_NAME]` | `"EcommerceAPI"` | Welcome message and context |
| `[INSERT_DOMAIN]` | `"api-development"` | Specific guidance references |
| `[INSERT_TECH_STACK]` | `"Node.js, Express, MySQL"` | Convention references |

#### Customization Strategy

**Add Your Commands List**: Update lines 23-27 with your actual commands:
```markdown
**Core Commands:**
- `/auto` - Intelligent command router for natural language requests
- `/task` - Focused development task execution  
- `/api-design` - Design and document REST APIs
- `/test-integration` - Run integration test suites
- `/deploy` - Deploy to staging/production environments
```

**Domain-Specific Tips**: Replace generic usage tips with domain-specific guidance:

**For Web Development**:
```markdown
**Usage Tips:**
1. **Start with /auto**: For component creation or feature requests
2. **Use /task for focused work**: Building individual components or features
3. **Try /component-gen**: For React/Vue component scaffolding
4. **Use /test**: For comprehensive testing workflows
```

**For Data Science**:
```markdown
**Usage Tips:**
1. **Start with /auto**: For data analysis or model requests
2. **Use /task for focused work**: Feature engineering or model training
3. **Try /notebook-run**: For Jupyter notebook workflows
4. **Use /analyze-system**: For data pipeline validation
```

### 3. `/auto` Command

**File**: `.claude/commands/core/auto.md`

**Purpose**: Intelligent request routing and natural language interface

#### Key Customization Areas

**Domain Recognition Patterns**: Update the command to recognize domain-specific requests

**Web Development Patterns**:
```markdown
I'll recognize requests like:
- "create a login component" → /component-gen
- "test the user service" → /test-integration  
- "deploy to staging" → /deploy
- "check API performance" → /analyze-system
```

**Data Science Patterns**:
```markdown
I'll recognize requests like:
- "analyze customer data" → /notebook-run
- "train the recommendation model" → /task
- "validate data pipeline" → /analyze-system  
- "generate report" → /quality
```

#### Command Routing Logic

Update the routing logic to match your available commands:
```markdown
**Available Routes:**
- Development tasks → /task
- Component creation → /component-gen (web-dev)
- Data analysis → /notebook-run (data-science)
- Testing requests → /test or /test-integration
- Deployment requests → /deploy
- Quality checks → /quality or /analyze-code
```

### 4. `/project-task` Command

**File**: `.claude/commands/core/project-task.md`

**Purpose**: Coordinate larger project-level initiatives

#### Essential Customizations

**Project Context**: Replace placeholders with your project specifics:
```markdown
I'll help coordinate project-level tasks for [YOUR_PROJECT_NAME], considering your team of [TEAM_SIZE] working with [TECH_STACK] in the [DOMAIN] domain.
```

**Task Categories**: Update categories to match your project types:

**Web Development Categories**:
- Feature development workflows
- Performance optimization projects
- Security audit initiatives
- UI/UX improvement campaigns

**Data Science Categories**:
- Model development lifecycles
- Data pipeline improvements
- Experiment tracking initiatives
- Production deployment workflows

**DevOps Categories**:
- Infrastructure modernization
- Security hardening projects
- Monitoring improvement initiatives
- Disaster recovery planning

## Advanced Customization Patterns

### 1. Tool Permission Customization

Each core command specifies allowed tools. Customize based on your needs:

**Web Development Project**:
```yaml
allowed-tools: Read, Write, Edit, Grep, Glob, Bash, WebFetch
```

**Data Science Project**:
```yaml
allowed-tools: Read, Write, Edit, Grep, Glob, NotebookRead, NotebookEdit
```

**DevOps Project**:
```yaml
allowed-tools: Read, Write, Edit, Bash, Grep, Glob
```

### 2. Argument Hints Customization

Update argument hints to match your domain:

**Web Development**:
```yaml
argument-hint: "[component_name or feature_description]"
```

**Data Science**:
```yaml
argument-hint: "[analysis_task or model_name]"
```

**DevOps**:
```yaml
argument-hint: "[infrastructure_task or deployment_target]"
```

### 3. Context-Aware Descriptions

Make descriptions specific to your use case:

**Generic**:
```yaml
description: "Execute a focused development task with best practices"
```

**Web Development**:
```yaml
description: "Build React components and features with responsive design and accessibility"
```

**Data Science**:
```yaml
description: "Perform data analysis, model training, and experiment tracking tasks"
```

**DevOps**:
```yaml
description: "Manage infrastructure, deployments, and monitoring with security best practices"
```

## Validation Checklist

After customizing core commands, verify:

### Functionality Validation
- [ ] All placeholders replaced with real values
- [ ] Command descriptions match your project reality
- [ ] Tool permissions align with your needs
- [ ] Example usage reflects your actual workflows

### Integration Validation  
- [ ] `/auto` correctly routes to your available commands
- [ ] `/help` lists all your customized commands
- [ ] `/task` references your actual tech stack and standards
- [ ] `/project-task` matches your project structure

### Domain Alignment
- [ ] Language and examples match your domain
- [ ] Best practices align with your industry standards
- [ ] Workflow steps match your development process
- [ ] Testing approaches use your actual frameworks

## Common Customization Patterns

### Minimal Customization (15 minutes)
1. Replace core placeholders (project name, tech stack, domain)
2. Update command lists in `/help`
3. Add 2-3 domain-specific examples
4. Validate with `/validate-adaptation`

### Standard Customization (45 minutes)
1. Complete minimal customization
2. Add domain-specific workflow steps
3. Customize tool permissions
4. Update argument hints and descriptions
5. Add project-specific best practices

### Advanced Customization (2+ hours)
1. Complete standard customization
2. Add custom routing logic to `/auto`
3. Create domain-specific command categories
4. Add compliance and security requirements
5. Integrate with existing team standards

## Domain-Specific Examples

### E-commerce Web Application

**Project Context**:
- Name: "ShopifyStore"
- Tech Stack: "React, Node.js, PostgreSQL, Redis"
- Domain: "e-commerce"
- Team: 8 developers
- Company: "RetailCorp"

**Customized `/task` excerpt**:
```markdown
# /task - Focused Development Workflow for ShopifyStore

I'll help you implement a specific development task using best practices for React, Node.js, PostgreSQL, Redis projects, with appropriate testing and quality standards for your e-commerce domain.

## Approach
1. **Analysis**: Understand requirements and user journey impact
2. **Design**: Plan with responsive design and accessibility
3. **Implementation**: Follow RetailCorp's coding standards
4. **Testing**: Use Jest and Cypress for comprehensive testing
5. **Performance**: Optimize for conversion and loading speed
6. **Documentation**: Update API docs and user guides

I'll follow RetailCorp's coding standards and use Jest for testing when appropriate.
```

### Machine Learning Platform

**Project Context**:
- Name: "MLPipeline"
- Tech Stack: "Python, TensorFlow, Apache Airflow, PostgreSQL"
- Domain: "machine-learning"
- Team: 5 data scientists
- Company: "DataCorp"

**Customized `/task` excerpt**:
```markdown
# /task - Focused Development Workflow for MLPipeline

I'll help you implement a specific development task using best practices for Python, TensorFlow, Apache Airflow, PostgreSQL projects, with appropriate testing and quality standards for your machine-learning domain.

## Approach
1. **Analysis**: Understand data requirements and model objectives
2. **Design**: Plan with reproducibility and scalability in mind
3. **Implementation**: Follow DataCorp's ML engineering standards
4. **Testing**: Use pytest and validate model performance
5. **Monitoring**: Add logging and performance metrics
6. **Documentation**: Update model cards and pipeline docs

I'll follow DataCorp's coding standards and use pytest for testing when appropriate.
```

## Troubleshooting

### Common Issues

**"Commands don't reflect my project"**
- Solution: Complete placeholder replacement first
- Use domain-specific language throughout
- Add relevant examples from your actual work

**"Too generic, not helpful"**
- Solution: Add specific best practices for your domain
- Include your actual tools and frameworks
- Reference your real coding standards

**"Team members confused by commands"**
- Solution: Add clear usage examples
- Include argument hints that match your terminology
- Update help command with your actual workflow

### Recovery Steps

If customization goes wrong:
1. Use `/undo-adaptation --level=placeholders-only`
2. Start with minimal customization approach
3. Test each change with `/validate-adaptation`
4. Get team feedback before completing full customization

---

*Next: See `CUSTOMIZATION-GUIDE-DEVELOPMENT.md` for development command customization patterns.*