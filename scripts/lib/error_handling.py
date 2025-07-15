#!/usr/bin/env python3
"""
Standardized Error Handling for Claude Code Framework Scripts

Provides consistent error handling, logging, and exit code patterns across all scripts.

Author: Claude Code Framework - Phase 2.3 Organization
Version: 1.0.0
Date: 2025-07-15
"""

import sys
import logging
import traceback
from typing import Optional, Callable, Any
from functools import wraps
from pathlib import Path


class ScriptError(Exception):
    """Base exception for script errors"""
    def __init__(self, message: str, exit_code: int = 1):
        super().__init__(message)
        self.exit_code = exit_code


class ValidationError(ScriptError):
    """Exception for validation failures"""
    def __init__(self, message: str):
        super().__init__(message, exit_code=2)


class ConfigurationError(ScriptError):
    """Exception for configuration issues"""
    def __init__(self, message: str):
        super().__init__(message, exit_code=3)


def setup_logging(name: str, verbose: bool = False, log_file: Optional[Path] = None) -> logging.Logger:
    """
    Setup standardized logging configuration
    
    Args:
        name: Logger name (usually __name__)
        verbose: Enable debug logging
        log_file: Optional log file path
    
    Returns:
        Configured logger instance
    """
    level = logging.DEBUG if verbose else logging.INFO
    
    # Create formatter
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    # Setup logger
    logger = logging.getLogger(name)
    logger.setLevel(level)
    
    # Clear any existing handlers
    logger.handlers.clear()
    
    # Console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(level)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    
    # File handler if specified
    if log_file:
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    
    return logger


def handle_errors(logger: Optional[logging.Logger] = None):
    """
    Decorator for standardized error handling in main functions
    
    Usage:
        @handle_errors(logger)
        def main():
            # Your main function code
            pass
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> int:
            try:
                result = func(*args, **kwargs)
                return result if isinstance(result, int) else 0
                
            except KeyboardInterrupt:
                if logger:
                    logger.info("Operation cancelled by user")
                else:
                    print("⚠️  Operation cancelled by user")
                return 130  # Standard exit code for SIGINT
                
            except ScriptError as e:
                if logger:
                    logger.error(f"Script error: {e}")
                else:
                    print(f"❌ Error: {e}")
                return e.exit_code
                
            except Exception as e:
                if logger:
                    logger.error(f"Unexpected error: {e}")
                    logger.debug(traceback.format_exc())
                else:
                    print(f"💥 Unexpected error: {e}")
                    if hasattr(sys, '_getframe'):  # Debug mode check
                        traceback.print_exc()
                return 1
                
        return wrapper
    return decorator


def validate_path(path: Path, must_exist: bool = True, must_be_file: bool = False, 
                 must_be_dir: bool = False) -> Path:
    """
    Validate path with clear error messages
    
    Args:
        path: Path to validate
        must_exist: Path must exist
        must_be_file: Path must be a file
        must_be_dir: Path must be a directory
    
    Returns:
        Validated Path object
    
    Raises:
        ValidationError: If validation fails
    """
    if must_exist and not path.exists():
        raise ValidationError(f"Path does not exist: {path}")
    
    if must_be_file and path.exists() and not path.is_file():
        raise ValidationError(f"Path is not a file: {path}")
    
    if must_be_dir and path.exists() and not path.is_dir():
        raise ValidationError(f"Path is not a directory: {path}")
    
    return path


def ensure_directory(path: Path, create_parents: bool = True) -> Path:
    """
    Ensure directory exists, creating if necessary
    
    Args:
        path: Directory path
        create_parents: Create parent directories if needed
    
    Returns:
        Path object
    
    Raises:
        ConfigurationError: If directory cannot be created
    """
    try:
        path.mkdir(parents=create_parents, exist_ok=True)
        return path
    except Exception as e:
        raise ConfigurationError(f"Cannot create directory {path}: {e}")


def safe_file_operation(operation: Callable, *args, **kwargs) -> Any:
    """
    Safely execute file operations with error handling
    
    Args:
        operation: File operation function to execute
        *args, **kwargs: Arguments for the operation
    
    Returns:
        Operation result
    
    Raises:
        ScriptError: If file operation fails
    """
    try:
        return operation(*args, **kwargs)
    except PermissionError as e:
        raise ScriptError(f"Permission denied: {e}")
    except FileNotFoundError as e:
        raise ScriptError(f"File not found: {e}")
    except IOError as e:
        raise ScriptError(f"IO error: {e}")


def confirm_action(message: str, default: bool = False) -> bool:
    """
    Ask user for confirmation with standardized prompt
    
    Args:
        message: Confirmation message
        default: Default choice if user just presses enter
    
    Returns:
        True if user confirms, False otherwise
    """
    suffix = " [Y/n]" if default else " [y/N]"
    response = input(f"{message}{suffix}: ").strip().lower()
    
    if not response:
        return default
    
    return response in ['y', 'yes', 'true', '1']


# Standard exit codes
EXIT_SUCCESS = 0
EXIT_GENERAL_ERROR = 1
EXIT_VALIDATION_ERROR = 2
EXIT_CONFIGURATION_ERROR = 3
EXIT_PERMISSION_ERROR = 4
EXIT_USER_CANCELLED = 130


def exit_with_code(code: int, message: Optional[str] = None, logger: Optional[logging.Logger] = None):
    """
    Exit with standardized code and message
    
    Args:
        code: Exit code
        message: Optional exit message
        logger: Optional logger for message
    """
    if message:
        if logger:
            if code == EXIT_SUCCESS:
                logger.info(message)
            else:
                logger.error(message)
        else:
            icon = "✅" if code == EXIT_SUCCESS else "❌"
            print(f"{icon} {message}")
    
    sys.exit(code)


# Context manager for temporary changes
class temporary_directory_change:
    """Context manager for temporarily changing working directory"""
    
    def __init__(self, new_dir: Path):
        self.new_dir = Path(new_dir)
        self.old_dir = Path.cwd()
    
    def __enter__(self):
        import os
        os.chdir(self.new_dir)
        return self.new_dir
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        import os
        os.chdir(self.old_dir)


# Example usage function for documentation
def example_usage():
    """
    Example of how to use the error handling utilities
    """
    # Setup logging
    logger = setup_logging(__name__, verbose=True)
    
    @handle_errors(logger)
    def main():
        logger.info("Starting example script")
        
        # Validate paths
        project_root = validate_path(Path.cwd(), must_exist=True, must_be_dir=True)
        logger.info(f"Project root: {project_root}")
        
        # Safe file operations
        def read_file(path):
            with open(path) as f:
                return f.read()
        
        try:
            content = safe_file_operation(read_file, "example.txt")
            logger.info(f"Read {len(content)} characters")
        except ScriptError as e:
            logger.warning(f"Could not read example file: {e}")
        
        # User confirmation
        if confirm_action("Continue with operation?", default=True):
            logger.info("User confirmed operation")
        else:
            logger.info("User cancelled operation")
            return EXIT_USER_CANCELLED
        
        logger.info("Script completed successfully")
        return EXIT_SUCCESS
    
    # Run main function
    return main()


if __name__ == "__main__":
    # Run example if executed directly
    exit_code = example_usage()
    sys.exit(exit_code)