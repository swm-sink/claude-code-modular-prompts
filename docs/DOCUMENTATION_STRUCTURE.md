# Documentation Structure - Canonical Sources

> **DRY Principle**: This document defines the single source of truth for all documentation topics. Always reference these canonical locations instead of duplicating content.

## Canonical Documentation Sources

### Framework Core
- **Framework Principles**: [`CLAUDE.md`](../CLAUDE.md)
  - Single source truth, Zero redundancy, Modular composition
  - Critical thinking rules, File discipline
  - Architecture and versioning

### Commands
- **Complete Command Reference**: [`docs/reference/commands-reference.md`](reference/commands-reference.md)
  - All command syntax, examples, and parameters
  - Best practices and usage patterns
  
- **Command Selection Guide**: [`docs/user-guide/commands/command-selection.md`](user-guide/commands/command-selection.md)
  - Decision trees and selection criteria
  - References command reference for examples

- **Command Implementation**: [`.claude/commands/`](../.claude/commands/)
  - Technical implementation details
  - Module integration specifications

### Installation & Setup
- **Installation Guide**: [`docs/getting-started/installation.md`](getting-started/installation.md)
  - All installation methods and options
  - Troubleshooting and verification
  
- **Quick Start**: [`docs/getting-started/quick-start.md`](getting-started/quick-start.md)
  - 5-minute setup (references Installation Guide)
  
- **First Commands**: [`docs/getting-started/first-commands.md`](getting-started/first-commands.md)
  - Initial command usage examples

### Configuration
- **Project Configuration**: [`docs/user-guide/customization/project-config.md`](user-guide/customization/project-config.md)
  - PROJECT_CONFIG.xml structure and options
  - Domain-specific configurations
  
- **Advanced Configuration**: [`docs/user-guide/customization/advanced-config.md`](user-guide/customization/advanced-config.md)
  - Performance tuning, team settings

### Quality Standards
- **Quality Gates**: [`CLAUDE.md#quality-gates`](../CLAUDE.md#quality-gates)
  - Master quality requirements
  
- **TDD Implementation**: [`.claude/system/quality/tdd.md`](../.claude/system/quality/tdd.md)
  - RED→GREEN→REFACTOR cycle details
  
- **Test Coverage**: [`.claude/system/quality/test-coverage.md`](../.claude/system/quality/test-coverage.md)
  - Coverage requirements and tooling

### Module System
- **Module Guide**: [`.claude/modules/MASTER_MODULE_GUIDE.md`](../.claude/modules/MASTER_MODULE_GUIDE.md)
  - Module structure and development
  
- **Module Runtime**: [`docs/advanced/framework-components/module-runtime-engine.md`](advanced/framework-components/module-runtime-engine.md)
  - Runtime architecture and integration

### Framework Architecture
- **Architecture Overview**: [`docs/advanced/framework-architecture.md`](advanced/framework-architecture.md)
  - High-level framework design
  
- **Claude 4 Optimization**: [`docs/advanced/claude-4-optimization.md`](advanced/claude-4-optimization.md)
  - Performance and optimization details

## Reference Guidelines

### When to Reference vs. Summarize

**Always Reference**:
- Command syntax and examples
- Installation procedures
- Configuration options
- Quality requirements
- Framework principles

**Summarize with Reference**:
- Key concepts with link to details
- Quick decision points with link to full guide
- Overview with link to comprehensive documentation

### Example References

```markdown
# Good - Reference to canonical source
For complete command examples, see [Commands Reference](../reference/commands-reference.md).

# Good - Brief summary with reference
The framework enforces TDD (RED→GREEN→REFACTOR). See [TDD Implementation](../../.claude/system/quality/tdd.md) for details.

# Bad - Duplicating content
The /auto command routes intelligently to the best approach...
[Full duplicate description]
```

## Maintenance

### Adding New Documentation
1. Check if topic already has a canonical source
2. If yes, add content to canonical location
3. If no, create new canonical source and update this guide
4. Reference from other documents, never duplicate

### Updating Documentation
1. Always update the canonical source
2. References automatically stay current
3. Run DRY validator to check compliance:
   ```bash
   python scripts/validation/dry-documentation-validator.py
   ```

### Documentation Standards
- One canonical source per topic
- Clear references instead of duplication
- Hierarchical organization
- Regular validation for DRY compliance

## Validation

Run regular checks to ensure DRY compliance:
```bash
# Check for duplicate content
python scripts/validation/dry-documentation-validator.py

# Review report
cat dry_validation_report.md
```

Target: Zero duplicate content blocks across documentation.