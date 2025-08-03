# Environment Variables Reference

## Core Variables

### CLAUDE_MODE
- **Purpose**: Determines execution context
- **Values**: `transformation` | `framework`
- **Default**: `framework`
- **Set by**: `.submodule/detect_mode.sh`

### CLAUDE_ROOT
- **Purpose**: Root directory of the Claude Context Engineering system
- **Example**: `/path/to/project/.claude-context`
- **Default**: Auto-detected via git or pwd
- **Set by**: `.submodule/detect_mode.sh`

### CLAUDE_SCOPE
- **Purpose**: The project directory being operated on
- **In transformation mode**: Same as CLAUDE_ROOT
- **In framework mode**: Parent project root (usually `../..`)
- **Set by**: `.submodule/detect_mode.sh`

### CLAUDE_CONTEXT_DIR
- **Purpose**: Directory containing context files to load
- **In transformation mode**: `$CLAUDE_ROOT/.transformation/context`
- **In framework mode**: `$CLAUDE_ROOT/.claude/framework/context`
- **Set by**: `.submodule/detect_mode.sh`

## Override Variables

### CLAUDE_MODE_OVERRIDE
- **Purpose**: Force a specific mode regardless of markers
- **Values**: `transformation` | `framework`
- **Usage**: `export CLAUDE_MODE_OVERRIDE=transformation`
- **Use case**: Testing or debugging

## Usage Examples

### Detecting Mode in Commands
```bash
source .submodule/detect_mode.sh

if [[ "$CLAUDE_MODE" == "transformation" ]]; then
    echo "Working on transforming this project"
else
    echo "Working as framework in parent project"
fi
```

### Using Scope in Commands
```bash
# Always work relative to the project being operated on
cd "$CLAUDE_SCOPE"

# Find files in the target project
find "$CLAUDE_SCOPE" -name "*.md"
```

### Loading Context
```bash
# Load context appropriate to current mode
for context in "$CLAUDE_CONTEXT_DIR"/*.md; do
    # Process context file
done
```

## Debugging

### Check Current Settings
```bash
source .submodule/detect_mode.sh
echo "Mode: $CLAUDE_MODE"
echo "Root: $CLAUDE_ROOT"
echo "Scope: $CLAUDE_SCOPE"
echo "Context: $CLAUDE_CONTEXT_DIR"
```

### Force Transformation Mode
```bash
export CLAUDE_MODE_OVERRIDE=transformation
source .submodule/detect_mode.sh
```

## Best Practices

1. **Always source detect_mode.sh** at the start of commands
2. **Use CLAUDE_SCOPE** for all project-relative operations
3. **Check CLAUDE_MODE** before mode-specific logic
4. **Validate directories exist** before using them
5. **Export variables** for child processes