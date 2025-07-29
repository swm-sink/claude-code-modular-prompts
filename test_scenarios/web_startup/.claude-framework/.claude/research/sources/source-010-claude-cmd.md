# Source #10: Claude CMD - Commands Manager

### Metadata
- **URL**: https://github.com/kiliczsh/claude-cmd
- **Author/Organization**: kiliczsh (Community)
- **Date**: 2025 (Active)
- **Type**: Community/Tool

### Verification Status
- ✅ Command management system
- ✅ Shows .claude directory hierarchy
- ✅ Settings.json configuration
- ✅ CLAUDE.md usage patterns
- ✅ 184+ command repository

### Rating: 4/5

### Key Patterns Observed

1. **Configuration Hierarchy**:
   ```
   ~/.claude/              # Global configuration
   ├── commands/          # Installed commands
   ├── settings.json      # Global settings
   └── CLAUDE.md          # Global instructions
   
   Project/
   ├── CLAUDE.md          # Project instructions
   ├── CLAUDE.local.md    # Local overrides
   └── .claude/           # Project configuration
   ```

2. **Command Management Pattern**:
   ```bash
   claude-cmd install git-helper
   claude-cmd search git
   claude-cmd list
   claude-cmd remove outdated-command
   ```

3. **Dynamic Content Loading**:
   - Remote command repositories
   - Local command development
   - Version management
   - Security profiles

### Code Examples

```bash
# Install a command from repository
claude-cmd install git-helper

# Search available commands
claude-cmd search "test"

# List installed commands
claude-cmd list --verbose
```

### Insights & Innovations

- Command marketplace concept
- Hierarchical configuration
- Local override support
- Community command sharing

### Practical Applications

- Team command standardization
- Command discovery and sharing
- Project-specific overrides
- Centralized command management

### Limitations/Caveats

- Requires separate installation
- Additional layer of complexity
- Community command quality varies