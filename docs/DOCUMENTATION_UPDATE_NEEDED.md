# Documentation Update Requirements - New Init Commands

| Date | 2025-07-11 |
|------|------------|
| Status | Analysis Complete |
| Purpose | Identify documentation files needing updates for new /init-* commands |

## Summary

With the introduction of four new initialization commands in `.claude/start_here/`, several documentation files need updates to reference these new commands and reduce reliance on manual configuration.

## New Init Commands to Document

1. **`/init-custom`** - Existing codebase auto-configuration
2. **`/init-new`** - Interactive new project setup  
3. **`/init-research`** - Domain-specific research & configuration
4. **`/init-validate`** - Multi-agent framework validation

## Files Requiring Updates

### High Priority (Manual Configuration References)

#### 1. `GETTING_STARTED.md` ⚠️ HIGH PRIORITY
- **Issue**: Shows manual PROJECT_CONFIG.xml editing in "Step 2: Configure PROJECT_CONFIG.xml (1 minute)"
- **Update Needed**: Add section showing new init commands as easier alternatives
- **Suggested Addition**: 
  - "Easy Setup with Init Commands" section before manual configuration
  - Show `/init-custom` for existing projects, `/init-new` for new projects

#### 2. `docs/CUSTOMIZATION_GUIDE.md` ⚠️ HIGH PRIORITY  
- **References Found**: Multiple `/init` command references
  - Line 10: `/init --wizard`
  - Line 148: `/init --config PROJECT_CONFIG.dev.xml`
  - Line 210: `/init --validate` 
  - Line 235: `/init --debug`
  - Line 256: `/init --wizard`
  - Line 263: `/init --help`
- **Update Needed**: Update to reference new `/init-validate` and other new commands

#### 3. `PROJECT_CONFIG_TEMPLATE.md` ⚠️ MEDIUM PRIORITY
- **Reference Found**: Line 152: `/init --config PROJECT_CONFIG.xml`
- **Update Needed**: Mention new init commands as alternatives to manual configuration

#### 4. `examples/project-configs/README.md` ⚠️ MEDIUM PRIORITY
- **References Found**: 
  - "Initialize the framework": `/init --config PROJECT_CONFIG.xml`
  - "Test with `/init --validate`"
  - "Run `/init --help`"
- **Update Needed**: Reference new `/init-validate` command and other new commands

### Low Priority (Installation References)

#### 5. `README.md` 📝 LOW PRIORITY
- **Issue**: Shows manual installation process only
- **Update Needed**: Mention new init commands in "Quick Start" section
- **Note**: No direct init references, but could benefit from mentioning easier setup

#### 6. `USER_GUIDE.md` ✅ NO UPDATE NEEDED
- **Status**: No relevant init command references found

#### 7. `docs/COMMAND_SELECTION_GUIDE.md` ✅ NO UPDATE NEEDED  
- **Status**: No init command references found

#### 8. `docs/COMMAND_SYSTEM_GUIDE.md` ✅ NO UPDATE NEEDED
- **Status**: No init command references found

#### 9. `scripts/README.md` ✅ NO UPDATE NEEDED
- **Status**: No init command references found

## Recommended Update Strategy

### Phase 1: High Priority Files
1. **GETTING_STARTED.md**: Add "Easy Setup with Init Commands" section before manual configuration
2. **docs/CUSTOMIZATION_GUIDE.md**: Update all `/init` references to include new commands
3. **PROJECT_CONFIG_TEMPLATE.md**: Add section on new init commands
4. **examples/project-configs/README.md**: Update init command references

### Phase 2: Integration
- Ensure all documentation consistently references the new commands
- Update any cross-references between documents
- Add command examples showing the new init commands in action

### Key Messaging
- **Emphasize Ease**: New init commands eliminate manual configuration
- **Show Alternatives**: Present new commands as easier alternatives to manual setup  
- **Maintain Backward Compatibility**: Keep manual configuration instructions but position as advanced/optional

## Benefits of Documentation Updates

1. **Reduced Setup Friction**: Users discover easier initialization methods
2. **Better User Experience**: Clear guidance on when to use which init command
3. **Consistency**: All documentation points to the new streamlined setup process
4. **Discoverability**: New init commands become more visible to users