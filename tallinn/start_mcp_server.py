#!/usr/bin/env python3
"""
Claude Code MCP Server Startup Script

This script provides a convenient way to start the Claude Code MCP server
with various configuration options and environment setup.

Usage:
    python start_mcp_server.py
    python start_mcp_server.py --dev
    python start_mcp_server.py --log-level DEBUG
"""

import asyncio
import os
import sys
import argparse
import logging
from pathlib import Path

# Add the project root to Python path
project_root = Path(__file__).parent.absolute()
sys.path.insert(0, str(project_root))

try:
    from mcp_server import ClaudeCodeMCPServer
except ImportError as e:
    print(f"Error importing MCP server: {e}", file=sys.stderr)
    print("Make sure MCP dependencies are installed: pip install mcp", file=sys.stderr)
    sys.exit(1)


def setup_logging(log_level: str, dev_mode: bool = False):
    """Setup logging configuration."""
    level = getattr(logging, log_level.upper())
    
    # Configure logging format
    if dev_mode:
        format_str = '%(asctime)s - %(name)s - %(levelname)s - [%(filename)s:%(lineno)d] - %(message)s'
    else:
        format_str = '%(asctime)s - %(levelname)s - %(message)s'
    
    logging.basicConfig(
        level=level,
        format=format_str,
        handlers=[
            logging.StreamHandler(sys.stderr),
            logging.FileHandler(project_root / 'mcp_server.log', mode='a')
        ]
    )


def check_dependencies():
    """Check if all required dependencies are available."""
    missing_deps = []
    
    try:
        import mcp
    except ImportError:
        missing_deps.append("mcp")
    
    if missing_deps:
        print("Missing required dependencies:", file=sys.stderr)
        for dep in missing_deps:
            print(f"  - {dep}", file=sys.stderr)
        print("\nInstall with: pip install " + " ".join(missing_deps), file=sys.stderr)
        return False
    
    return True


def validate_project_structure():
    """Validate that the project has the expected structure."""
    required_dirs = [
        ".claude/commands",
        "claude_prompt_factory/components"
    ]
    
    missing_dirs = []
    for dir_path in required_dirs:
        full_path = project_root / dir_path
        if not full_path.exists():
            missing_dirs.append(dir_path)
    
    if missing_dirs:
        print("Warning: Missing expected directories:", file=sys.stderr)
        for dir_path in missing_dirs:
            print(f"  - {dir_path}", file=sys.stderr)
        print("\nThe MCP server may not find all resources.", file=sys.stderr)
        return False
    
    return True


def validate_commands():
    """Validate that commands directory exists and has content."""
    commands_dir = project_root / ".claude" / "commands"
    
    if not commands_dir.exists():
        print("Error: Commands directory not found at .claude/commands", file=sys.stderr)
        return False
    
    command_count = len(list(commands_dir.rglob("*.md")))
    if command_count == 0:
        print("Warning: No commands found in .claude/commands", file=sys.stderr)
        return False
    
    print(f"✓ Found {command_count} commands in .claude/commands", file=sys.stderr)
    return True


def print_startup_info(args):
    """Print startup information."""
    print("=" * 60, file=sys.stderr)
    print("🚀 Claude Code MCP Server", file=sys.stderr)
    print("=" * 60, file=sys.stderr)
    print(f"📁 Project Root: {project_root}", file=sys.stderr)
    print(f"📊 Log Level: {args.log_level}", file=sys.stderr)
    print(f"🔧 Dev Mode: {args.dev}", file=sys.stderr)
    print(f"📝 Log File: {project_root / 'mcp_server.log'}", file=sys.stderr)
    
    # Show resource counts
    commands_dir = project_root / ".claude" / "commands"
    components_dir = project_root / "claude_prompt_factory" / "components"
    
    if commands_dir.exists():
        command_count = len(list(commands_dir.rglob("*.md")))
        print(f"📋 Commands Available: {command_count}", file=sys.stderr)
    
    if components_dir.exists():
        component_count = len(list(components_dir.rglob("*.md")))
        print(f"🧩 Components Available: {component_count}", file=sys.stderr)
    
    print("=" * 60, file=sys.stderr)
    print("🎯 MCP Resources will be exposed at:", file=sys.stderr)
    print("   claude-code://commands/*", file=sys.stderr)
    print("   claude-code://components/*", file=sys.stderr)
    print("=" * 60, file=sys.stderr)
    print("⚡ Server starting... (Press Ctrl+C to stop)", file=sys.stderr)
    print("=" * 60, file=sys.stderr)


async def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Start Claude Code MCP Server",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python start_mcp_server.py                    # Start server with default settings
  python start_mcp_server.py --dev              # Start in development mode with detailed logging
  python start_mcp_server.py --log-level DEBUG  # Start with debug logging
        """
    )
    
    parser.add_argument(
        "--log-level",
        default="INFO",
        choices=["DEBUG", "INFO", "WARNING", "ERROR"],
        help="Logging level (default: INFO)"
    )
    parser.add_argument(
        "--dev",
        action="store_true",
        help="Enable development mode with detailed logging"
    )
    parser.add_argument(
        "--project-root",
        default=str(project_root),
        help="Project root directory (defaults to script directory)"
    )
    
    args = parser.parse_args()
    
    # Setup logging
    log_level = "DEBUG" if args.dev else args.log_level
    setup_logging(log_level, args.dev)
    
    logger = logging.getLogger(__name__)
    
    try:
        # Validate dependencies
        if not check_dependencies():
            sys.exit(1)
        
        # Validate project structure
        validate_project_structure()
        
        # Validate commands directory
        if not validate_commands():
            print("❌ Command validation failed. MCP server may not work properly.", file=sys.stderr)
        
        # Print startup info
        print_startup_info(args)
        
        # Initialize and start server
        logger.info("Initializing Claude Code MCP Server...")
        server = ClaudeCodeMCPServer(args.project_root)
        
        logger.info("Starting MCP server...")
        await server.run_server()
        
    except KeyboardInterrupt:
        logger.info("Server stopped by user")
        print("\n👋 Claude Code MCP Server stopped", file=sys.stderr)
    except Exception as e:
        logger.error(f"Server error: {e}")
        print(f"\n❌ Server error: {e}", file=sys.stderr)
        if args.dev:
            import traceback
            traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    # Set the event loop policy for better Windows compatibility
    if sys.platform == "win32":
        asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())
    
    asyncio.run(main())