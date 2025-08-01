# Component Optimization Action Plan
## Achieving "Many Small Components, Fewer Commands"

*Generated: 2025-07-31*
*Purpose: Concrete action plan to transform architecture from 91:88 to 200:50 ratio*

## Current vs Target Architecture

### Current State (1:1 Ratio)
- **91 Components** (mostly multi-purpose)
- **88 Commands** (mostly monolithic)
- **Reuse Rate**: <23%
- **Average Component Size**: ~100 lines
- **Component References**: Only 17/88 commands use components

### Target State (4:1 Ratio)
- **200 Components** (all single-purpose)
- **50 Commands** (all component assemblies)
- **Reuse Rate**: >60%
- **Average Component Size**: <30 lines
- **Component References**: 50/50 commands use components

## Phase 1: Component Decomposition (Weeks 1-2)

### Week 1: Core Component Breakdown

#### Day 1-2: Atomic Component Decomposition
**Current**: 21 multi-purpose atomic components
**Target**: 60 single-purpose atomic components

**Actions**:
1. Decompose `workflow-coordinator.md` → 6 components
2. Decompose `data-transformer.md` → 5 components
3. Decompose `git-operations.md` → 10 components
4. Decompose `test-runner.md` → 4 components
5. Split remaining 17 atomic components → 35 components

**Deliverables**:
- 60 new atomic component files
- Updated component index
- Migration guide for existing commands

#### Day 3-4: Orchestration Component Breakdown
**Current**: 7 complex orchestration components
**Target**: 25 simple orchestration components

**Actions**:
1. Decompose `dag-orchestrator.md` → 7 components
2. Decompose `agent-orchestration.md` → 5 components
3. Decompose `task-planning.md` → 4 components
4. Split remaining 4 orchestration components → 9 components

**Deliverables**:
- 25 new orchestration component files
- Orchestration pattern documentation
- Assembly examples

#### Day 5: Security Component Refinement
**Current**: 10 security components (some overlap)
**Target**: 15 focused security components

**Actions**:
1. Split `input-validation-framework.md` → 3 validators
2. Add missing: `rate-limiter.md`, `session-manager.md`, `audit-logger.md`
3. Merge overlapping path validation components
4. Create `security-assembly-patterns.md`

### Week 2: New Component Categories

#### Day 6-7: Data Processing Components (New Category)
**Target**: 25 data processing components

**New Components**:
- Input: `csv-parser.md`, `json-parser.md`, `xml-parser.md`, `yaml-parser.md`
- Transform: `field-mapper.md`, `value-converter.md`, `data-filter.md`, `data-aggregator.md`
- Validate: `schema-validator.md`, `type-validator.md`, `range-validator.md`
- Output: `csv-writer.md`, `json-writer.md`, `xml-writer.md`, `report-formatter.md`
- Stream: `stream-reader.md`, `stream-processor.md`, `stream-writer.md`
- Batch: `batch-processor.md`, `batch-splitter.md`, `batch-merger.md`

#### Day 8-9: Control Flow Components (New Category)
**Target**: 20 control flow components

**New Components**:
- Conditional: `if-then.md`, `switch-case.md`, `pattern-match.md`
- Loops: `for-each.md`, `while-loop.md`, `do-until.md`
- Flow: `sequence.md`, `parallel.md`, `pipeline.md`, `branch.md`
- State: `state-store.md`, `state-transition.md`, `state-validator.md`
- Events: `event-emitter.md`, `event-listener.md`, `event-aggregator.md`

#### Day 10: Integration Components (New Category)
**Target**: 15 integration components

**New Components**:
- API: `rest-client.md`, `graphql-client.md`, `webhook-handler.md`
- Database: `db-connector.md`, `query-builder.md`, `result-mapper.md`
- Message: `queue-publisher.md`, `queue-consumer.md`, `topic-subscriber.md`
- File: `ftp-client.md`, `s3-client.md`, `file-watcher.md`

## Phase 2: Command Consolidation (Weeks 3-4)

### Week 3: Command Analysis and Merging

#### Day 11-12: Testing Command Consolidation
**Current**: 5 testing commands
**Target**: 2 testing commands

**Actions**:
1. Merge: `test.md`, `test-unit.md`, `test-integration.md`, `test-e2e.md`
   → `/test [type] [options]` (assembly of test components)
2. Keep: `mutation.md` → `/test-advanced mutation` (specialized assembly)

**Component Assembly**:
```yaml
/test:
  components:
    - test-discoverer
    - test-filter
    - test-executor
    - test-reporter
    - coverage-collector (optional)
    - parallel-coordinator (optional)
```

#### Day 13-14: Security Command Consolidation
**Current**: 5 security commands
**Target**: 2 security commands

**Actions**:
1. Merge: `secure-audit.md`, `secure-scan.md`, `secure-assess.md`
   → `/security check [type]` (assembly of security components)
2. Keep: `secure-manage.md` → `/security manage` (management assembly)

#### Day 15: Analysis Command Consolidation
**Current**: 4 analysis commands
**Target**: 1 analysis command

**Actions**:
1. Merge: `analyze-code.md`, `analyze-system.md`, `quality-metrics.md`
   → `/analyze [target] [metrics]` (assembly of analysis components)

### Week 4: Command Transformation

#### Day 16-17: Convert Utility Commands to Components
**Target**: Remove 15 utility commands, add as components

**Conversions**:
- `/format` → `code-formatter.md` component
- `/validate` → `validation-runner.md` component
- `/git-commit` → Use existing `git-commit.md` component
- `/quick-fix` → `quick-fix-suggester.md` component

#### Day 18-19: Create Showcase Commands
**Target**: 10 new showcase commands demonstrating assembly

**New Commands**:
1. `/build-pipeline` - Assembles 8-10 components
2. `/data-flow` - Assembles 6-8 data components
3. `/api-gateway` - Assembles 5-7 integration components
4. `/workflow-automation` - Assembles 10-12 components
5. `/monitoring-stack` - Assembles 7-9 components

#### Day 20: Command Documentation Update
**Actions**:
1. Update all remaining commands to show component usage
2. Create assembly pattern guide
3. Document component selection criteria

## Phase 3: Infrastructure Development (Weeks 5-6)

### Week 5: Component Discovery System

#### Component Registry
```yaml
# .claude/components/registry.yaml
components:
  file-reader:
    category: atomic
    complexity: simple
    compatible_with: [data-transformer, error-handler]
    incompatible_with: [file-writer]
    common_assemblies: [data-pipeline, file-processor]
```

#### Discovery Command
```markdown
# /discover-components

Find components for your use case:
/discover-components "read and transform data"

Results:
- file-reader (atomic/io)
- data-parser (data/input)
- data-transformer (data/transform)
- error-handler (atomic/error)

Suggested Assembly:
file-reader → data-parser → data-transformer → error-handler
```

### Week 6: Assembly Tools

#### Component Assembler
```markdown
# /assemble-command

Interactive command builder:
1. Describe your goal
2. Select from suggested components
3. Configure component connections
4. Generate command template
```

#### Compatibility Validator
```python
# scripts/validate-assembly.py
def validate_assembly(components):
    # Check compatibility matrix
    # Verify interface matching
    # Detect circular dependencies
    # Return validation report
```

## Phase 4: Documentation and Examples (Weeks 7-8)

### Week 7: Pattern Library

#### Assembly Patterns Documentation
1. **Sequential Pipeline**: A → B → C → D
2. **Parallel Processing**: A → [B||C||D] → E
3. **Conditional Flow**: A → (B|C) → D
4. **Error Recovery**: A → B → (error? → C) → D
5. **Fan-out/Fan-in**: A → [B,C,D] → [E,F] → G

#### Component Composition Guide
- When to decompose further
- How to identify reusable parts
- Component naming conventions
- Interface design principles

### Week 8: Testing and Validation

#### Component Testing Framework
```python
# Each component gets:
- Unit tests for core functionality
- Integration tests with common partners
- Performance benchmarks
- Example usage tests
```

#### Command Assembly Tests
```python
# Each command gets:
- Component integration tests
- End-to-end workflow tests
- Performance profiling
- Error scenario tests
```

## Success Metrics and Monitoring

### Week-by-Week Targets

| Week | Components | Commands | Ratio | Reuse Rate |
|------|------------|----------|-------|------------|
| 0    | 91         | 88       | 1.0:1 | <23%       |
| 1    | 120        | 88       | 1.4:1 | 25%        |
| 2    | 165        | 88       | 1.9:1 | 30%        |
| 3    | 180        | 75       | 2.4:1 | 40%        |
| 4    | 200        | 50       | 4.0:1 | 50%        |
| 8    | 200        | 50       | 4.0:1 | >60%       |

### Quality Checkpoints

**After Each Phase**:
1. Component single-responsibility audit
2. Command assembly verification
3. Reusability measurement
4. Documentation completeness
5. Test coverage analysis

## Risk Mitigation

### Potential Risks and Mitigations

1. **Risk**: Breaking existing functionality
   - **Mitigation**: Maintain compatibility layer during transition

2. **Risk**: Over-decomposition making assembly complex
   - **Mitigation**: Follow "Rule of Three" - decompose when needed 3+ times

3. **Risk**: Poor component discovery
   - **Mitigation**: Invest heavily in discovery tools and documentation

4. **Risk**: Performance degradation from many small components
   - **Mitigation**: Component caching and assembly optimization

## Expected Outcomes

### For AI/Claude
- Clear understanding of each component's purpose
- Easy component discovery and suggestion
- Natural assembly of components for new use cases
- Improved prompt generation from components

### for Users
- Faster command creation from existing components
- Better understanding of available functionality
- Easier customization through component swapping
- More reliable and tested building blocks

### For Maintainers
- Easier to fix bugs (isolated components)
- Simple to add new functionality
- Clear testing boundaries
- Version components independently

## Conclusion

This action plan transforms the current 91:88 architecture into a 200:50 architecture over 8 weeks, achieving the goal of "many small prompt components and fewer example commands built using them." The plan is concrete, measurable, and includes specific deliverables for each phase.