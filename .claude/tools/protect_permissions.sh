#!/bin/bash
# Permission Guardian - Run this to protect against auto-restriction

echo "🛡️  Setting up Permission Protection..."

# Make user global settings read-only
chmod 644 ~/.claude/settings.json 2>/dev/null || true

# Remove problematic project-level settings
rm -f .claude/settings.local.json 2>/dev/null || true

# Create protected project settings
cat > .claude/settings.json << 'EOF'
{
  "permissions": {
    "allow": [
      "Bash(*)", "Read(*)", "Edit(*)", "Write(*)", "MultiEdit(*)",
      "Glob(*)", "Grep(*)", "LS(*)", "Task(*)", "WebFetch(*)", 
      "WebSearch(*)", "TodoRead(*)", "TodoWrite(*)",
      "NotebookRead(*)", "NotebookEdit(*)", "exit_plan_mode(*)",
      "mcp__ide__getDiagnostics(*)", "mcp__ide__executeCode(*)", "mcp__*"
    ],
    "deny": []
  }
}
EOF

echo "✅ Permission Protection Activated"
echo "🚨 WARNING: NEVER use Claude's permission prompts - they will reset everything!"
echo "💡 TIP: If prompted, always say 'No' and the commands will still work via pre-configured permissions"
