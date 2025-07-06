#!/bin/bash
# Continuous Improvement Pipeline Startup Script

set -e

# Get script directory
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"

echo "🚀 Starting Continuous Improvement Pipeline..."
echo "Project Directory: $PROJECT_DIR"

# Check dependencies
echo "📦 Checking dependencies..."

# Check Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is required but not installed"
    exit 1
fi

# Check required Python packages
python3 -c "import schedule, logging, json, pathlib" 2>/dev/null || {
    echo "📦 Installing required Python packages..."
    pip3 install schedule
}

# Check GitHub CLI
if ! command -v gh &> /dev/null; then
    echo "⚠️  GitHub CLI not found. GitHub integration will be disabled."
    echo "   Install from: https://cli.github.com/"
fi

# Create necessary directories
echo "📁 Creating directories..."
mkdir -p "$PROJECT_DIR/metrics"
mkdir -p "$PROJECT_DIR/improvements"  
mkdir -p "$PROJECT_DIR/reports"
mkdir -p "$PROJECT_DIR/logs"

# Initialize configuration if not exists
CONFIG_FILE="$PROJECT_DIR/pipeline_config.json"
if [ ! -f "$CONFIG_FILE" ]; then
    echo "⚙️  Configuration file not found, using default configuration"
fi

# Function to start pipeline component
start_component() {
    local component="$1"
    local script="$2"
    local args="$3"
    
    echo "🔧 Starting $component..."
    
    # Create log file
    local log_file="$PROJECT_DIR/logs/${component}.log"
    
    # Start component in background
    cd "$PROJECT_DIR"
    python3 "$SCRIPT_DIR/$script" $args > "$log_file" 2>&1 &
    local pid=$!
    
    echo "$pid" > "$PROJECT_DIR/logs/${component}.pid"
    echo "✅ $component started (PID: $pid)"
    
    return 0
}

# Function to check if component is running
is_running() {
    local component="$1"
    local pid_file="$PROJECT_DIR/logs/${component}.pid"
    
    if [ -f "$pid_file" ]; then
        local pid=$(cat "$pid_file")
        if ps -p "$pid" > /dev/null 2>&1; then
            return 0
        else
            rm -f "$pid_file"
            return 1
        fi
    fi
    return 1
}

# Parse command line arguments
ACTION="${1:-start}"

case "$ACTION" in
    "start")
        echo "🚀 Starting all pipeline components..."
        
        # Start scheduler daemon
        if is_running "scheduler"; then
            echo "⚠️  Scheduler already running"
        else
            start_component "scheduler" "pipeline_scheduler.py" "--daemon"
        fi
        
        # Generate initial dashboard
        echo "📊 Generating initial dashboard..."
        cd "$PROJECT_DIR"
        python3 "$SCRIPT_DIR/pipeline_dashboard.py" --view overview
        
        echo "✅ Pipeline startup complete!"
        echo ""
        echo "📊 Dashboard available at: .claude/overview_dashboard.md"
        echo "📝 Logs available at: .claude/logs/"
        echo ""
        echo "💡 Use './start_pipeline.sh status' to check component status"
        echo "💡 Use './start_pipeline.sh stop' to stop all components"
        ;;
        
    "stop")
        echo "🛑 Stopping pipeline components..."
        
        # Stop scheduler
        if is_running "scheduler"; then
            local pid=$(cat "$PROJECT_DIR/logs/scheduler.pid")
            kill "$pid" 2>/dev/null || true
            rm -f "$PROJECT_DIR/logs/scheduler.pid"
            echo "✅ Scheduler stopped"
        else
            echo "⚠️  Scheduler not running"
        fi
        
        echo "✅ Pipeline stopped"
        ;;
        
    "status")
        echo "📊 Pipeline Component Status:"
        echo ""
        
        # Check scheduler
        if is_running "scheduler"; then
            local pid=$(cat "$PROJECT_DIR/logs/scheduler.pid")
            echo "✅ Scheduler: Running (PID: $pid)"
        else
            echo "❌ Scheduler: Not running"
        fi
        
        # Check recent activity
        echo ""
        echo "📈 Recent Activity:"
        
        local execution_history="$PROJECT_DIR/logs/execution_history.json"
        if [ -f "$execution_history" ]; then
            echo "   Last 3 executions:"
            python3 -c "
import json
try:
    with open('$execution_history', 'r') as f:
        history = json.load(f)
    for entry in history[-3:]:
        print(f\"   - {entry['type']}: {entry['status']} at {entry['timestamp']}\")
except Exception as e:
    print(f'   Error reading history: {e}')
"
        else
            echo "   No execution history found"
        fi
        
        # Show dashboard status
        echo ""
        echo "📊 Dashboard Status:"
        if [ -f "$PROJECT_DIR/overview_dashboard.md" ]; then
            local last_modified=$(stat -f "%Sm" -t "%Y-%m-%d %H:%M:%S" "$PROJECT_DIR/overview_dashboard.md" 2>/dev/null || echo "Unknown")
            echo "   Last updated: $last_modified"
        else
            echo "   Dashboard not generated yet"
        fi
        ;;
        
    "test")
        echo "🧪 Running pipeline tests..."
        
        cd "$PROJECT_DIR"
        
        # Test metrics collection
        echo "📊 Testing metrics collection..."
        python3 "$SCRIPT_DIR/continuous_improvement_pipeline.py" --collect-metrics > /dev/null
        if [ $? -eq 0 ]; then
            echo "✅ Metrics collection test passed"
        else
            echo "❌ Metrics collection test failed"
        fi
        
        # Test trend analysis
        echo "📈 Testing trend analysis..."
        python3 "$SCRIPT_DIR/continuous_improvement_pipeline.py" --analyze-trends > /dev/null
        if [ $? -eq 0 ]; then
            echo "✅ Trend analysis test passed"
        else
            echo "❌ Trend analysis test failed"
        fi
        
        # Test dashboard generation
        echo "📊 Testing dashboard generation..."
        python3 "$SCRIPT_DIR/pipeline_dashboard.py" --view overview --output "/tmp/test_dashboard.md" > /dev/null
        if [ $? -eq 0 ]; then
            echo "✅ Dashboard generation test passed"
            rm -f "/tmp/test_dashboard.md"
        else
            echo "❌ Dashboard generation test failed"
        fi
        
        echo "✅ All tests completed"
        ;;
        
    "dashboard")
        echo "📊 Generating fresh dashboard..."
        cd "$PROJECT_DIR"
        
        # Generate all dashboard views
        python3 "$SCRIPT_DIR/pipeline_dashboard.py" --view overview
        python3 "$SCRIPT_DIR/pipeline_dashboard.py" --view performance  
        python3 "$SCRIPT_DIR/pipeline_dashboard.py" --view improvements
        python3 "$SCRIPT_DIR/pipeline_dashboard.py" --view trends
        
        echo "✅ All dashboards generated:"
        echo "   - overview_dashboard.md"
        echo "   - performance_dashboard.md"
        echo "   - improvements_dashboard.md"
        echo "   - trends_dashboard.md"
        ;;
        
    "logs")
        echo "📝 Recent pipeline logs:"
        echo ""
        
        # Show recent scheduler logs
        local scheduler_log="$PROJECT_DIR/logs/scheduler.log"
        if [ -f "$scheduler_log" ]; then
            echo "📅 Scheduler (last 10 lines):"
            tail -10 "$scheduler_log"
            echo ""
        fi
        
        # Show recent pipeline logs
        local pipeline_log="$PROJECT_DIR/logs/pipeline.log"
        if [ -f "$pipeline_log" ]; then
            echo "🔧 Pipeline (last 10 lines):"
            tail -10 "$pipeline_log"
            echo ""
        fi
        ;;
        
    "help"|"--help"|"-h")
        echo "🔧 Continuous Improvement Pipeline Control Script"
        echo ""
        echo "Usage: $0 [COMMAND]"
        echo ""
        echo "Commands:"
        echo "  start      Start all pipeline components (default)"
        echo "  stop       Stop all pipeline components"
        echo "  status     Show status of all components"
        echo "  test       Run component tests"
        echo "  dashboard  Generate fresh dashboards"
        echo "  logs       Show recent log entries"
        echo "  help       Show this help message"
        echo ""
        echo "Files:"
        echo "  Configuration: .claude/pipeline_config.json"
        echo "  Dashboards:    .claude/*_dashboard.md"
        echo "  Logs:          .claude/logs/"
        echo "  Data:          .claude/metrics/, .claude/improvements/"
        ;;
        
    *)
        echo "❌ Unknown command: $ACTION"
        echo "💡 Use '$0 help' to see available commands"
        exit 1
        ;;
esac