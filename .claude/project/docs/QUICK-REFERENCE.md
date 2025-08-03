# Quick Reference Guide
**Progressive Disclosure System - Command Summary**

## Choose Your Layer

```
┌─────────────────────────────────────────────────────────────┐
│                    WHICH LAYER FOR YOU?                     │
├─────────────────────────────────────────────────────────────┤
│ 🚀 Want instant results?           → Layer 1: /quick-command │
│ ⚙️  Need some customization?        → Layer 2: /build-command│
│ 🔧 Need maximum control?           → Layer 3: /assemble-command│
└─────────────────────────────────────────────────────────────┘
```

## Layer 1: Auto-Generation (80% of users)

### Command: `/quick-command`
**30-second success, zero learning curve**

#### Basic Usage
```bash
/quick-command [description]
```

#### Examples
```bash
# Search operations
/quick-command "find TODO comments in JavaScript files"
/quick-command "search for API calls"
/quick-command "find unused variables"

# Analysis operations  
/quick-command "analyze code quality"
/quick-command "check for security issues"
/quick-command "measure code complexity"

# Transform operations
/quick-command "convert JSON to YAML"
/quick-command "rename all variables"
/quick-command "modernize JavaScript code"

# Validation operations
/quick-command "validate JSON schema"
/quick-command "check code style"
/quick-command "verify API responses"

# Report operations
/quick-command "generate project summary"
/quick-command "create dependency report"
/quick-command "document API endpoints"
```

#### What You Get
- ✅ Working command in 30 seconds
- ✅ Intelligent defaults for 80% of cases
- ✅ No configuration required
- ✅ Clear upgrade path when needed

## Layer 2: Guided Customization (15% of users)

### Command: `/build-command`
**5-minute success with controlled customization**

#### Basic Usage
```bash
/build-command [type] [description] --customize
```

#### Examples
```bash
# Interactive customization
/build-command search "find security vulnerabilities" --customize
/build-command analyze "code quality metrics" --customize  
/build-command transform "JSON to database format" --customize

# Quick customization with options
/build-command search "API calls" --with file-types=js,ts output=detailed
/build-command analyze "performance" --with depth=thorough focus=bottlenecks
```

#### Customization Process
1. **Auto-generation** - Start with intelligent baseline
2. **Show 3-5 options** - Only relevant choices  
3. **Interactive preview** - See changes before applying
4. **Generate command** - Optimized for your needs

#### Available Customizations

**Search Commands:**
- File filtering (types, scope, hidden files)
- Pattern matching (case, regex, fixed strings)
- Output format (context, files only, detailed)
- Result sorting (path, relevance, date)

**Analysis Commands:**
- Analysis scope (file types, focus areas)
- Analysis depth (quick, standard, thorough)
- Metrics detail (summary, detailed, comprehensive)
- Issue filtering (severity levels)

**Transform Commands:**
- Input selection (patterns, directories, file lists)
- Backup strategy (none, simple, timestamped, git)
- Processing mode (safe, fast, strict, dry-run)
- Output handling (in-place, new directory, suffix)

**Validation Commands:**
- Validation scope (all files, specific types, changed only)
- Strictness level (permissive, standard, strict, pedantic)
- Auto-fix options (suggest, safe fixes, interactive)
- Report format (minimal, detailed, JSON, dashboard)

**Report Commands:**
- Report scope (overview, code focus, git history, dependencies)
- Time range (current, week, month, quarter, year)
- Output format (markdown, HTML, JSON, PDF)
- Detail level (summary, balanced, comprehensive)

## Layer 3: Component Assembly (5% of users)

### Command: `/assemble-command`
**15-30 minute success with maximum control**

#### Basic Usage
```bash
# Interactive assembly (recommended)
/assemble-command --interactive

# Template-based assembly
/assemble-command --from-template [template-name]

# Direct component assembly
/assemble-command --components "comp1,comp2,comp3"

# Browse components
/assemble-command --browse
```

#### Available Templates
```bash
# Security and compliance
/assemble-command --from-template security-audit
/assemble-command --from-template compliance-check

# Data processing
/assemble-command --from-template data-pipeline
/assemble-command --from-template etl-workflow

# Code analysis and transformation
/assemble-command --from-template code-migration
/assemble-command --from-template quality-assessment
```

#### Component Categories

**🧩 Atomic Components (21)** - Simple building blocks
```
Input/Output: file-reader, file-writer, parameter-parser, output-formatter
Data: data-transformer, format-converter, content-sanitizer
Workflow: state-manager, workflow-coordinator, dependency-resolver
Operations: git-operations, api-caller, test-runner, search-files
UX: progress-indicator, user-confirmation, error-handler, task-summary
```

**🔍 Analysis Components (15+)** - Code and data analysis
```
codebase-discovery, dependency-mapping, quality-metrics
anti-pattern-detection, framework-validation
```

**🚀 Orchestration Components (10+)** - Complex workflows
```
agent-orchestration, dag-orchestrator, task-planning
dependency-analysis, progress-tracking, task-execution
```

**🔒 Security Components (12+)** - Security and validation
```
credential-protection, input-validation-framework
prompt-injection-prevention, path-validation, owasp-compliance
```

**⚡ Performance Components (8+)** - Optimization
```  
context-compression, component-cache, prompt-optimization
framework-optimization, autoprompt-framework
```

**🧠 Intelligence Components (10+)** - Advanced AI
```
cognitive-architecture, multi-agent-coordination
adaptive-thinking, meta-learning, react-reasoning
tree-of-thoughts-framework
```

#### Assembly Patterns
```bash
# Linear Pipeline: A → B → C → D
file-reader → data-transformer → output-formatter → file-writer

# Fan-out/Fan-in: A → [B1, B2, B3] → C  
input → [security-scan, quality-check, dependency-map] → report-merger

# Conditional: A → Decision → [B | C | D]
input → format-detector → [json-processor | csv-processor | xml-processor]

# Event-driven: Trigger → [Handler1, Handler2] → Aggregator
file-watcher → [security-scanner, quality-checker] → alert-aggregator
```

## Navigation Between Layers

### Escalation (Moving Up)
```bash
# Layer 1 → Layer 2
# When /quick-command isn't enough:
/build-command [type] [description] --customize

# Layer 2 → Layer 3  
# When guided customization isn't enough:
/assemble-command --interactive
```

### De-escalation (Moving Down)
```bash
# Layer 3 → Layer 2
# When assembly is too complex:
/build-command [workflow-type] --customize

# Layer 2 → Layer 1
# When you just want quick results:
/quick-command [simple-description]
```

## Common Workflows

### Security Analysis
```bash
# Layer 1: Quick security scan
/quick-command "find security vulnerabilities"

# Layer 2: Customized security analysis  
/build-command search "security issues" --with patterns=advanced scope=critical-files

# Layer 3: Comprehensive security audit
/assemble-command --from-template security-audit
```

### Code Quality Assessment
```bash
# Layer 1: Basic quality check
/quick-command "analyze code quality"

# Layer 2: Focused quality analysis
/build-command analyze "code quality" --with depth=thorough focus=maintainability

# Layer 3: Enterprise quality assessment
/assemble-command --from-template quality-assessment
```

### Data Processing
```bash
# Layer 1: Simple transformation
/quick-command "convert CSV to JSON"

# Layer 2: Custom data processing
/build-command transform "CSV data" --with validation=strict backup=timestamped

# Layer 3: Complete data pipeline
/assemble-command --from-template data-pipeline
```

## Troubleshooting

### Layer 1 Issues
**Problem**: Generated command doesn't match expectations
**Solution**: Try Layer 2 with `/build-command [type] [description] --customize`

### Layer 2 Issues  
**Problem**: Available options don't meet specific needs
**Solution**: Escalate to Layer 3 with `/assemble-command --interactive`

**Problem**: Too many options, feeling overwhelmed
**Solution**: Use Layer 1 with `/quick-command [simple-description]`

### Layer 3 Issues
**Problem**: Component compatibility errors
**Solution**: Check validation feedback, use suggested adapter components

**Problem**: Assembly too complex
**Solution**: Start with template using `/assemble-command --from-template [name]`

## Performance Expectations

### Layer 1 Performance
- **Generation time**: 15-30 seconds
- **Execution time**: Varies by command type
- **Learning time**: 0 minutes (instant)

### Layer 2 Performance  
- **Customization time**: 2-5 minutes
- **Execution time**: Optimized for your specific needs
- **Learning time**: 5 minutes (one-time)

### Layer 3 Performance
- **Assembly time**: 15-30 minutes
- **Execution time**: Highly optimized, enterprise-grade
- **Learning time**: 30-60 minutes (for component library)

## Best Practices

### Choosing the Right Layer
1. **Start with Layer 1** unless you know you need more
2. **Use Layer 2** when defaults aren't quite right
3. **Use Layer 3** only when you need maximum control
4. **Don't over-engineer** - simpler is often better

### Optimization Tips
- **Layer 1**: Trust the defaults, they work for 80% of cases
- **Layer 2**: Focus on the 2-3 most important customizations
- **Layer 3**: Plan your assembly, validate early and often

### When to Escalate
- **Layer 1 → 2**: Command works but results aren't optimal
- **Layer 2 → 3**: Need features not available in guided customization  
- **Never escalate** just because a higher layer exists

### When to De-escalate
- **Feeling overwhelmed** by choices or complexity
- **Spending too much time** on configuration vs. getting work done
- **Good enough solution** available at lower layer

## Getting Help

### Documentation
- **System Overview**: `.claude/docs/PROGRESSIVE-DISCLOSURE-SYSTEM.md`
- **Component Guide**: `.claude/docs/COMPONENT-ASSEMBLY-GUIDE.md`  
- **This Reference**: `.claude/docs/QUICK-REFERENCE.md`

### Interactive Help
- **Component Browser**: `/assemble-command --browse`
- **Template Explorer**: `/assemble-command --templates`
- **Interactive Assembly**: `/assemble-command --interactive`

### Command Help
- **Layer 1 Help**: `/quick-command --help`
- **Layer 2 Help**: `/build-command --help`
- **Layer 3 Help**: `/assemble-command --help`

Remember: **Use the simplest layer that meets your needs.** The progressive disclosure system is designed so you never have to deal with more complexity than necessary for your specific task!