"""Claude Code Modular Framework.

This module provides the core framework functionality for the Claude Code
modular agent system.
"""

__version__ = "3.0.0"

# Core framework components
from .validator import FrameworkValidator
from .loader import ModuleLoader
from .metrics import QualityMetrics

__all__ = [
    "FrameworkValidator",
    "ModuleLoader", 
    "QualityMetrics",
    "__version__"
]