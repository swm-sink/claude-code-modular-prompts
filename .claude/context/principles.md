# Core Principles

## Development Philosophy

1. **Simplicity over complexity** - Maximum 3 levels of directory nesting
2. **Implementation over documentation** - 1:5 docs-to-code ratio maximum
3. **Quality over quantity** - 50 curated commands, not 150+
4. **Test-first development** - Tests before implementation, always
5. **Atomic commits** - One thing at a time

## Commit Standards

```
type: Brief description (<50 chars)

- What changed
- Why it changed
- Test coverage: XX%
```

Types: cleanup, feat, test, docs, refactor

## Performance Requirements

- Commands execute in <100ms
- Memory usage <50MB per command
- Context window optimization (<5% waste)

## Quality Gates

- Test coverage: 90% minimum
- Security vulnerabilities: 0
- Directory depth: 3 maximum
- Code without tests: BLOCKED