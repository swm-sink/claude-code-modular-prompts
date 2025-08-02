# Apply Code Changes

**Purpose**: Carefully apply approved code changes with validation, ensuring correct implementation without introducing errors.

**Usage**: 
- Applies changes only within approved plan scope
- Validates syntax correctness after modifications
- Runs relevant unit tests when available
- Generates precise code edits for target files
- Provides summary of applied changes

**Compatibility**: 
- **Works with**: file-writer, git-operations, test-runner, validation-framework
- **Requires**: approved_plan, target_files, change_specifications
- **Conflicts**: None (universal action component)

**Implementation**:
```yaml
apply_changes:
  scope: approved_plan_only
  validation: syntax_check
  testing: run_unit_tests
  summary: changes_applied
```

**Category**: actions | **Complexity**: simple | **Time**: 15 minutes