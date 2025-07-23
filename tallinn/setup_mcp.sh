#!/bin/bash
"""
Claude Code MCP Server Setup Script

This script sets up the MCP server for Claude Code, including:
- Installing required dependencies
- Creating simplified commands
- Validating configuration
- Testing server functionality

Usage:
    ./setup_mcp.sh
    ./setup_mcp.sh --dev
    ./setup_mcp.sh --install-only
"""

set -e  # Exit on any error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Configuration
PROJECT_ROOT=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
VENV_DIR="$PROJECT_ROOT/venv_mcp"
PYTHON_CMD="python3"

print_header() {
    echo -e "${BLUE}============================================${NC}"
    echo -e "${BLUE} Claude Code MCP Server Setup${NC}"
    echo -e "${BLUE}============================================${NC}"
    echo ""
}

print_status() {
    echo -e "${GREEN}✓${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}⚠${NC} $1"
}

print_error() {
    echo -e "${RED}✗${NC} $1"
}

print_info() {
    echo -e "${BLUE}ℹ${NC} $1"
}

check_python() {
    print_info "Checking Python installation..."
    
    if ! command -v $PYTHON_CMD &> /dev/null; then
        print_error "Python 3 not found. Please install Python 3.8 or later."
        exit 1
    fi
    
    PYTHON_VERSION=$($PYTHON_CMD --version 2>&1 | cut -d' ' -f2)
    print_status "Found Python $PYTHON_VERSION"
}

setup_virtual_environment() {
    print_info "Setting up virtual environment..."
    
    if [ ! -d "$VENV_DIR" ]; then
        $PYTHON_CMD -m venv "$VENV_DIR"
        print_status "Created virtual environment at $VENV_DIR"
    else
        print_status "Virtual environment already exists"
    fi
    
    # Activate virtual environment
    source "$VENV_DIR/bin/activate"
    print_status "Activated virtual environment"
    
    # Update pip
    pip install --upgrade pip wheel
    print_status "Updated pip and wheel"
}

install_dependencies() {
    print_info "Installing MCP dependencies..."
    
    # First install the core MCP package
    if pip install mcp>=1.0.0 anyio>=4.0.0 pydantic>=2.0.0; then
        print_status "MCP dependencies installed successfully"
    else
        print_warning "Failed to install MCP from PyPI, trying alternative installation..."
        
        # Try installing from GitHub or alternative source
        pip install git+https://github.com/modelcontextprotocol/python-sdk.git
        pip install anyio>=4.0.0 pydantic>=2.0.0
        
        if [ $? -eq 0 ]; then
            print_status "MCP dependencies installed from alternative source"
        else
            print_error "Failed to install MCP dependencies"
            print_info "You may need to install MCP manually or check for updated installation instructions"
        fi
    fi
    
    # Install other project dependencies
    if [ -f "$PROJECT_ROOT/requirements.txt" ]; then
        print_info "Installing project dependencies..."
        pip install -r "$PROJECT_ROOT/requirements.txt"
        print_status "Project dependencies installed"
    fi
}

create_simplified_commands() {
    print_info "Creating simplified commands..."
    
    if [ -f "$PROJECT_ROOT/scripts/simplify_commands.py" ]; then
        $PYTHON_CMD "$PROJECT_ROOT/scripts/simplify_commands.py" --priority-only --output "$PROJECT_ROOT/.claude/commands"
        print_status "Simplified commands created successfully"
    else
        print_warning "Command simplifier script not found, skipping..."
    fi
}

validate_structure() {
    print_info "Validating project structure..."
    
    REQUIRED_DIRS=(
        "claude_prompt_factory/commands"
        "claude_prompt_factory/components"
        ".claude"
    )
    
    REQUIRED_FILES=(
        "mcp_server.py"
        "start_mcp_server.py"
        "mcp_config.json"
        "claude_desktop_config.json"
    )
    
    for dir in "${REQUIRED_DIRS[@]}"; do
        if [ -d "$PROJECT_ROOT/$dir" ]; then
            print_status "Directory exists: $dir"
        else
            print_warning "Directory missing: $dir"
        fi
    done
    
    for file in "${REQUIRED_FILES[@]}"; do
        if [ -f "$PROJECT_ROOT/$file" ]; then
            print_status "File exists: $file"
        else
            print_error "File missing: $file"
        fi
    done
}

test_server() {
    print_info "Testing MCP server..."
    
    # Test import
    if $PYTHON_CMD -c "import sys; sys.path.insert(0, '$PROJECT_ROOT'); import mcp_server; print('MCP server imports successfully')" 2>/dev/null; then
        print_status "MCP server can be imported successfully"
    else
        print_warning "MCP server import test failed - this may be due to missing MCP dependencies"
    fi
    
    # Test configuration
    if [ -f "$PROJECT_ROOT/mcp_config.json" ]; then
        if $PYTHON_CMD -c "import json; json.load(open('$PROJECT_ROOT/mcp_config.json'))" 2>/dev/null; then
            print_status "MCP configuration is valid JSON"
        else
            print_error "MCP configuration JSON is invalid"
        fi
    fi
}

update_claude_config() {
    print_info "Updating Claude Desktop configuration..."
    
    CONFIG_FILE="$PROJECT_ROOT/claude_desktop_config.json"
    
    if [ -f "$CONFIG_FILE" ]; then
        # Update the PYTHONPATH in the configuration
        sed -i.backup "s|\"PYTHONPATH\": \".*\"|\"PYTHONPATH\": \"$PROJECT_ROOT\"|g" "$CONFIG_FILE"
        print_status "Updated PYTHONPATH in Claude Desktop configuration"
        
        # Make startup script executable
        chmod +x "$PROJECT_ROOT/start_mcp_server.py"
        print_status "Made startup script executable"
    else
        print_warning "Claude Desktop configuration not found"
    fi
}

show_next_steps() {
    echo ""
    echo -e "${BLUE}============================================${NC}"
    echo -e "${BLUE} Setup Complete!${NC}"
    echo -e "${BLUE}============================================${NC}"
    echo ""
    echo -e "${GREEN}Next Steps:${NC}"
    echo ""
    echo "1. Restart Claude Desktop to load the MCP server"
    echo ""
    echo "2. Test the server manually:"
    echo "   source $VENV_DIR/bin/activate"
    echo "   python3 start_mcp_server.py --dev"
    echo ""
    echo "3. In Claude, you should see 'claude-code-mcp' resources available"
    echo ""
    echo "4. Use the following tools in Claude:"
    echo "   - execute_command: Run Claude Code commands"
    echo "   - list_commands: Browse available commands"
    echo "   - get_command_info: Get detailed command information"
    echo ""
    echo -e "${GREEN}Configuration Files:${NC}"
    echo "   - MCP Server: $PROJECT_ROOT/mcp_server.py"
    echo "   - Startup Script: $PROJECT_ROOT/start_mcp_server.py"
    echo "   - Configuration: $PROJECT_ROOT/mcp_config.json"
    echo "   - Claude Config: $PROJECT_ROOT/claude_desktop_config.json"
    echo ""
    echo -e "${GREEN}Logs and Debugging:${NC}"
    echo "   - Server logs: $PROJECT_ROOT/mcp_server.log"
    echo "   - Debug mode: python3 start_mcp_server.py --dev"
    echo ""
    echo -e "${YELLOW}Note: If MCP dependencies failed to install, you may need to:${NC}"
    echo "   - Check for updated MCP installation instructions"
    echo "   - Install from source or alternative repositories"
    echo "   - Use a different Python environment"
    echo ""
}

main() {
    local dev_mode=false
    local install_only=false
    
    # Parse arguments
    while [[ $# -gt 0 ]]; do
        case $1 in
            --dev)
                dev_mode=true
                shift
                ;;
            --install-only)
                install_only=true
                shift
                ;;
            -h|--help)
                echo "Usage: $0 [--dev] [--install-only] [--help]"
                echo "  --dev          Enable development mode"
                echo "  --install-only Only install dependencies, skip other setup"
                echo "  --help         Show this help message"
                exit 0
                ;;
            *)
                print_error "Unknown option: $1"
                exit 1
                ;;
        esac
    done
    
    print_header
    
    cd "$PROJECT_ROOT"
    
    check_python
    setup_virtual_environment
    install_dependencies
    
    if [ "$install_only" = false ]; then
        create_simplified_commands
        validate_structure
        update_claude_config
        test_server
        show_next_steps
    else
        print_status "Dependencies installed successfully (install-only mode)"
    fi
}

# Run main function with all arguments
main "$@"