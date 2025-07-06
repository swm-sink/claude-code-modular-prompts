#!/bin/bash
# 🚨 EMERGENCY PERMISSION RECOVERY - COPY/PASTE THIS IF EVERYTHING BREAKS

# ONE-LINER EMERGENCY RECOVERY (copy and run this):
# curl -sL https://raw.githubusercontent.com/anthropics/claude-code/main/emergency-recovery.sh | bash || (rm -f .claude/settings.local.json && ln -sf ~/.claude/settings.json .claude/settings.local.json && echo '{"permissions":{"allow":["Bash(*)","Read(*)","Edit(*)","Write(*)","MultiEdit(*)","Glob(*)","Grep(*)","LS(*)","Task(*)","WebFetch(*)","WebSearch(*)","TodoRead(*)","TodoWrite(*)","NotebookRead(*)","NotebookEdit(*)","exit_plan_mode(*)","mcp__ide__getDiagnostics(*)","mcp__ide__executeCode(*)","mcp__*"],"deny":["Bash(rm -rf /:*)","Bash(sudo su:*)","Bash(dd:*)","Bash(mkfs:*)"]},"env":{"CLAUDE_CODE_ENABLE_TELEMETRY":"1"},"model":"opus"}' > ~/.claude/settings.json)

echo "🚨 EMERGENCY PERMISSION RECOVERY"
echo "================================"

# Step 1: Remove broken local settings
echo "1️⃣ Removing broken local settings..."
rm -f .claude/settings.local.json

# Step 2: Create comprehensive global settings
echo "2️⃣ Creating comprehensive global settings..."
mkdir -p ~/.claude

cat > ~/.claude/settings.json << 'EOF'
{
  "permissions": {
    "allow": [
      "Bash(*)",
      "Read(*)",
      "Edit(*)",
      "Write(*)",
      "MultiEdit(*)",
      "Glob(*)",
      "Grep(*)",
      "LS(*)",
      "Task(*)",
      "WebFetch(*)",
      "WebSearch(*)",
      "TodoRead(*)",
      "TodoWrite(*)",
      "NotebookRead(*)",
      "NotebookEdit(*)",
      "exit_plan_mode(*)",
      "mcp__ide__getDiagnostics(*)",
      "mcp__ide__executeCode(*)",
      "mcp__*"
    ],
    "deny": [
      "Bash(rm -rf /:*)",
      "Bash(sudo su:*)",
      "Bash(dd:*)",
      "Bash(mkfs:*)"
    ]
  },
  "env": {
    "CLAUDE_CODE_ENABLE_TELEMETRY": "1"
  },
  "model": "opus"
}
EOF

# Step 3: Create symlink
echo "3️⃣ Creating protective symlink..."
ln -sf ~/.claude/settings.json .claude/settings.local.json

# Step 4: Verify
echo "4️⃣ Verifying recovery..."
if [ -L .claude/settings.local.json ] && [ -f ~/.claude/settings.json ]; then
    echo "✅ RECOVERY SUCCESSFUL!"
    echo ""
    echo "🛡️ Protection Status:"
    echo "   Global settings: ~/.claude/settings.json ✅"
    echo "   Local symlink: .claude/settings.local.json → ~/.claude/settings.json ✅"
    echo ""
    echo "⚠️ IMPORTANT: NEVER click 'Yes' on permission prompts!"
    echo "   Commands will work via pre-configured permissions."
else
    echo "❌ RECOVERY FAILED - Manual intervention required"
    echo "Contact support or check GitHub issues"
fi