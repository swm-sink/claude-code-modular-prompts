#!/bin/bash
# 🛡️ FORTRESS STARTUP - Automated Permission Protection
# Run this at shell startup to ensure permissions are always protected

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
FORTRESS_PY="$SCRIPT_DIR/permission_fortress.py"

echo "🏰 PERMISSION FORTRESS STARTUP PROTECTION"
echo "========================================"

# Check if we're in a Claude Code project
if [ -d ".claude" ] || [ -d "$HOME/.claude" ]; then
    # Run fortress check
    if [ -f "$FORTRESS_PY" ]; then
        python "$FORTRESS_PY" check
        
        # Start monitor in background if check passed
        if [ $? -eq 0 ]; then
            echo ""
            echo "🛡️ Starting background monitor..."
            nohup python "$FORTRESS_PY" monitor 30 > /dev/null 2>&1 &
            MONITOR_PID=$!
            echo "✅ Monitor running (PID: $MONITOR_PID)"
            echo ""
            echo "💡 Commands available:"
            echo "   fortress check    - Manual fortress check"
            echo "   fortress monitor  - Start monitoring"
            echo "   fortress nuclear  - Emergency reset"
            echo "   fortress stop     - Stop monitor"
        else
            echo "❌ Fortress check failed! Run: fortress nuclear"
        fi
    else
        echo "⚠️ Permission fortress not found at: $FORTRESS_PY"
    fi
else
    echo "ℹ️ Not in a Claude Code environment"
fi

# Add fortress alias for easy access
alias fortress="python '$FORTRESS_PY'"
alias fortress-stop="pkill -f 'permission_fortress.py monitor'"

echo "✅ Fortress aliases configured"