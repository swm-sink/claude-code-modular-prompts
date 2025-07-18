"""
Main Streamlit application for Claude Code Modular Prompts Framework Dashboard
Follows separation of concerns - handles only configuration and routing
"""

import streamlit as st
import os
import time
from pathlib import Path
from typing import Optional, Dict, Any
from components.command_explorer import CommandExplorer
from components.module_visualizer import PromptComponentExplorer as ModuleVisualizer
from components.framework_overview import FrameworkOverview
from components.prompt_constructor import PromptConstructor
from components.quality_gates import QualityGatesDashboard
from components.routing_simulator import RoutingSimulator
from components.meta_framework import MetaFrameworkControlPanel
from components.visual_flow_builder import VisualFlowBuilder
from components.dependency_graph import DependencyGraph
from components.prompt_preview import PromptPreview
from components.template_manager import TemplateManager
from components.routing_engine import RoutingEngine
from components.url_sharing import URLSharingManager
from components.performance_monitor import PerformanceMonitor
from components.usage_analytics import UsageAnalytics, track_page_view
from components.decision_tree_visualizer import DecisionTreeVisualizer
from components.ab_testing import ABTestingFramework
from components.prompt_sandbox import PromptSandbox
from components.context_aware_analyzer import ContextAwareAnalyzer
from components.success_pattern_detector import PromptPatternDiscovery
from components.natural_language_interface import NaturalLanguageInterface
from components.interactive_prompt_builder import InteractivePromptBuilder
from components.prompt_effectiveness_testing import PromptEffectivenessTesting
from components.ab_prompt_comparison import ABPromptComparison
from components.pattern_recognition_engine import PatternRecognitionEngine
from components.intelligent_recommendation_engine import IntelligentRecommendationEngine
from utils.session_manager import init_session_management
from utils.health_monitor import health_monitor
from utils.ui_components import UIBranding, LoadingStates, ErrorHandling, ProfessionalComponents, safe_component_render


class EnvironmentDetector:
    """Robust environment detection for dual-mode operation"""
    
    @staticmethod
    def detect_environment() -> str:
        """
        Detect the current environment with high reliability
        Returns: 'development', 'railway', or 'production'
        """
        # Railway environment detection
        if os.getenv('RAILWAY_ENVIRONMENT') or os.getenv('RAILWAY_PROJECT_ID'):
            return 'railway'
        
        # Generic production environment detection
        if os.getenv('ENVIRONMENT') == 'production' or os.getenv('NODE_ENV') == 'production':
            return 'production'
            
        # Default to development
        return 'development'
    
    @staticmethod
    def get_environment_info() -> Dict[str, Any]:
        """Get detailed environment information for debugging"""
        env = EnvironmentDetector.detect_environment()
        return {
            'environment': env,
            'railway_env': os.getenv('RAILWAY_ENVIRONMENT'),
            'railway_project': os.getenv('RAILWAY_PROJECT_ID'),
            'port': os.getenv('PORT'),
            'cwd': str(Path.cwd()),
            'python_path': os.getenv('PYTHONPATH'),
        }


class BaseEnvironmentConfig:
    """Base configuration class with common settings"""
    
    def __init__(self):
        self.environment = EnvironmentDetector.detect_environment()
        self.page_title = "Claude Code Framework Dashboard"
        self.page_icon = "🧠"
        self.layout = "wide"
        self.initial_sidebar_state = "expanded"
        
    def get_framework_path(self) -> Optional[Path]:
        """Get framework path - to be implemented by subclasses"""
        raise NotImplementedError
        
    def check_framework_availability(self) -> bool:
        """Check if framework components are available"""
        framework_path = self.get_framework_path()
        return framework_path is not None and framework_path.exists() and framework_path.is_dir()
        
    def get_available_components(self) -> Dict[str, bool]:
        """Get which components are available in this environment"""
        return {}


class LocalDevelopmentConfig(BaseEnvironmentConfig):
    """Configuration for local development environment"""
    
    def __init__(self):
        super().__init__()
        self.load_env_file = True
        self.full_functionality = True
        self.debug_mode = True
        
    def get_framework_path(self) -> Optional[Path]:
        """
        Get framework path using relative path resolution with fallbacks
        Supports:
        1. Environment variable override (CLAUDE_FRAMEWORK_PATH)
        2. Relative path from project root
        3. Multiple fallback locations
        """
        # 1. Check for environment variable override
        env_path = os.getenv('CLAUDE_FRAMEWORK_PATH')
        if env_path:
            path = Path(env_path)
            if path.exists():
                return path
        
        # 2. Calculate relative path from streamlit_dashboard to project root
        current_dir = Path(__file__).parent  # streamlit_dashboard directory
        project_root = current_dir.parent    # claude-code-modular-prompts directory
        framework_path = project_root / ".claude"
        
        if framework_path.exists():
            return framework_path
        
        # 3. Fallback: try common relative locations
        fallback_paths = [
            Path("../.claude"),           # One level up
            Path("../../.claude"),        # Two levels up
            Path(".claude"),              # Current directory
        ]
        
        for fallback in fallback_paths:
            if fallback.exists():
                return fallback.resolve()
        
        # 4. Return None if framework not found (graceful degradation)
        return None
        
    def get_available_components(self) -> Dict[str, bool]:
        """All components available in local development"""
        return {
            "Framework Overview": True,
            "Command Explorer": True,
            "Prompt Component Explorer": True,
            "Prompt Optimization Assistant": True,
            "Prompt Pattern Discovery": True,
            "Natural Language Interface": True,
            "Prompt Constructor": True,
            "Interactive Prompt Builder": True,
            "Prompt Effectiveness Testing": True,
            "A/B Prompt Comparison": True,
            "Pattern Recognition Engine": True,
            "Intelligent Recommendation Engine": True,
            "Visual Flow Builder": True,
            "Dependency Graph": True,
            "Prompt Preview": True,
            "Template Manager": True,
            "URL Sharing": True,
            "AI Routing Engine": True,
            "Decision Tree Visualizer": True,
            "A/B Testing Framework": True,
            "Prompt Testing Sandbox": True,
            "Quality Gates": True,
            "Routing Simulator": True,
            "Meta Framework": True,
            "Performance Monitor": True,
            "Usage Analytics": True,
            "Health Monitor": True,
        }


class RailwayProductionConfig(BaseEnvironmentConfig):
    """Configuration for Railway production environment"""
    
    def __init__(self):
        super().__init__()
        self.load_env_file = False
        self.full_functionality = False
        self.debug_mode = False
        
    def get_framework_path(self) -> Optional[Path]:
        """
        Try to find framework path in Railway environment
        Returns None if not available (graceful degradation)
        """
        # Check environment variable override
        env_path = os.getenv('FRAMEWORK_PATH')
        if env_path:
            path = Path(env_path)
            if path.exists():
                return path
        
        # Try common Railway deployment paths
        potential_paths = [
            Path.cwd().parent / '.claude',  # If running from streamlit_dashboard/
            Path('/app/.claude'),           # Railway app root
            Path('.claude'),                # Current directory
            Path('../.claude')              # Parent directory
        ]
        
        for path in potential_paths:
            if path.exists() and path.is_dir():
                return path
                
        # Return None for graceful degradation
        return None
        
    def get_available_components(self) -> Dict[str, bool]:
        """Limited components available in Railway production"""
        has_framework = self.check_framework_availability()
        
        # Core components that work without framework
        core_components = {
            "Prompt Testing Sandbox": True,
            "A/B Testing Framework": True,
            "A/B Prompt Comparison": True,
            "Performance Monitor": True,
            "Usage Analytics": True,
            "Health Monitor": True,
            "URL Sharing": True,
            "Template Manager": True,
        }
        
        # Framework-dependent components
        framework_components = {
            "Framework Overview": has_framework,
            "Command Explorer": has_framework,
            "Prompt Component Explorer": has_framework,
            "Prompt Optimization Assistant": has_framework,
            "Prompt Pattern Discovery": has_framework,
            "Natural Language Interface": has_framework,
            "Prompt Constructor": has_framework,
            "Interactive Prompt Builder": has_framework,
            "Prompt Effectiveness Testing": has_framework,
            "Pattern Recognition Engine": has_framework,
            "Intelligent Recommendation Engine": has_framework,
            "Visual Flow Builder": has_framework,
            "Dependency Graph": has_framework,
            "Prompt Preview": has_framework,
            "AI Routing Engine": has_framework,
            "Decision Tree Visualizer": has_framework,
            "Quality Gates": has_framework,
            "Routing Simulator": has_framework,
            "Meta Framework": has_framework,
        }
        
        return {**core_components, **framework_components}


class AppConfig:
    """Main application configuration with environment detection"""
    
    def __init__(self):
        self.environment = EnvironmentDetector.detect_environment()
        
        # Initialize environment-specific configuration
        if self.environment == 'development':
            self.config = LocalDevelopmentConfig()
        else:
            self.config = RailwayProductionConfig()
            
        # Load environment variables if needed
        if self.config.load_env_file:
            self._load_env_file()
            
    def _load_env_file(self):
        """Load .env file for local development"""
        env_file = Path('.env')
        if env_file.exists():
            from dotenv import load_dotenv
            load_dotenv()
            
    @property
    def FRAMEWORK_PATH(self) -> Optional[Path]:
        """Get the framework path from environment-specific config"""
        return self.config.get_framework_path()
        
    @property
    def PAGE_TITLE(self) -> str:
        return self.config.page_title
        
    @property
    def PAGE_ICON(self) -> str:
        return self.config.page_icon
        
    @property
    def LAYOUT(self) -> str:
        return self.config.layout
        
    @property
    def INITIAL_SIDEBAR_STATE(self) -> str:
        return self.config.initial_sidebar_state
        
    def get_available_components(self) -> Dict[str, bool]:
        """Get which components are available"""
        return self.config.get_available_components()
        
    def is_framework_available(self) -> bool:
        """Check if framework is available"""
        return self.config.check_framework_availability()
        
    def get_environment_info(self) -> Dict[str, Any]:
        """Get environment information for display"""
        return EnvironmentDetector.get_environment_info()
        
    @property 
    def NAVIGATION_PAGES(self) -> list:
        """Get available navigation pages based on environment"""
        available_components = self.get_available_components()
        all_pages = [
            # === GETTING STARTED ===
            "Framework Overview",
            # === EXPLORATION PHASE ===
            "Command Explorer", 
            "Prompt Component Explorer",
            "Prompt Pattern Discovery",
            # === OPTIMIZATION PHASE ===
            "Prompt Optimization Assistant",
            "Intelligent Recommendation Engine",
            "Pattern Recognition Engine",
            # === BUILDING PHASE ===
            "Interactive Prompt Builder",
            "Natural Language Interface",
            "Prompt Constructor",
            "Visual Flow Builder",
            # === TESTING PHASE ===
            "Prompt Effectiveness Testing",
            "A/B Prompt Comparison",
            "Prompt Testing Sandbox", 
            "A/B Testing Framework",
            # === ANALYSIS TOOLS ===
            "Dependency Graph",
            "Prompt Preview",
            "Decision Tree Visualizer",
            "AI Routing Engine",
            # === MANAGEMENT TOOLS ===
            "Template Manager",
            "URL Sharing",
            "Quality Gates",
            "Routing Simulator",
            # === ADVANCED FEATURES ===
            "Meta Framework",
            "Performance Monitor",
            "Usage Analytics"
        ]
        
        # Filter pages based on availability in current environment
        return [page for page in all_pages if available_components.get(page, False)]


def setup_navigation():
    """Set up the navigation menu for the dashboard with dual-environment support"""
    # Initialize configuration
    app_config = AppConfig()
    
    st.set_page_config(
        page_title=app_config.PAGE_TITLE,
        page_icon=app_config.PAGE_ICON,
        layout=app_config.LAYOUT,
        initial_sidebar_state=app_config.INITIAL_SIDEBAR_STATE
    )
    
    # Initialize session management
    session_manager = init_session_management()
    
    # Create enhanced navigation in sidebar
    with st.sidebar:
        st.title("🧠 Claude Code Framework")
        st.markdown("**Prompt Engineering Dashboard**")
        
        # Add environment status display
        env_info = app_config.get_environment_info()
        framework_available = app_config.is_framework_available()
        
        st.markdown("---")
        st.markdown("### 🌍 Environment Status")
        
        # Environment indicator
        env_color = "🟢" if env_info['environment'] == 'development' else "🟡"
        st.markdown(f"{env_color} **Environment**: {env_info['environment'].title()}")
        
        # Framework availability indicator
        framework_color = "🟢" if framework_available else "🔴"
        framework_status = "Available" if framework_available else "Limited Mode"
        st.markdown(f"{framework_color} **Framework**: {framework_status}")
        
        # Show framework path if available
        if app_config.FRAMEWORK_PATH:
            with st.expander("Framework Details", expanded=False):
                st.code(f"Path: {app_config.FRAMEWORK_PATH}")
                if not framework_available:
                    st.warning("⚠️ Framework directory not found. Running in limited mode with core components only.")
        
        # Add workflow guidance
        st.markdown("---")
        st.markdown("### 🚀 Quick Start Guide")
        
        if framework_available:
            st.markdown("""
            **New to prompt engineering?**
            1. 📖 Start with **Framework Overview**
            2. 🔍 Explore **Prompt Components**
            3. 🔧 Build with **Interactive Builder**
            4. 🧪 Test with **Effectiveness Testing**
            """)
        else:
            st.markdown("""
            **Limited Mode Active**
            Available features:
            • 🧪 Prompt Testing Sandbox
            • ⚖️ A/B Testing Framework
            • 📊 Performance Monitor
            • 📈 Usage Analytics
            """)
        
        st.markdown("---")
        st.markdown("### 📋 Navigation")
        
        # Get available components for current environment
        available_components = app_config.get_available_components()
        
        # Organize pages by sections, filtering by availability
        all_page_sections = {
            "🎯 Getting Started": ["Framework Overview"],
            "🔍 Exploration": [
                "Command Explorer", 
                "Prompt Component Explorer",
                "Prompt Pattern Discovery"
            ],
            "🚀 Optimization": [
                "Prompt Optimization Assistant",
                "Intelligent Recommendation Engine",
                "Pattern Recognition Engine"
            ],
            "🔧 Building": [
                "Interactive Prompt Builder",
                "Natural Language Interface", 
                "Prompt Constructor",
                "Visual Flow Builder"
            ],
            "🧪 Testing": [
                "Prompt Effectiveness Testing",
                "A/B Prompt Comparison",
                "Prompt Testing Sandbox",
                "A/B Testing Framework"
            ],
            "📊 Analysis": [
                "Dependency Graph",
                "Prompt Preview", 
                "Decision Tree Visualizer",
                "AI Routing Engine"
            ],
            "📁 Management": [
                "Template Manager",
                "URL Sharing",
                "Quality Gates",
                "Routing Simulator"
            ],
            "⚙️ Advanced": [
                "Meta Framework",
                "Performance Monitor",
                "Usage Analytics"
            ]
        }
        
        # Filter sections to only include available components
        page_sections = {}
        for section_name, pages in all_page_sections.items():
            available_pages = [page for page in pages if available_components.get(page, False)]
            if available_pages:  # Only include sections with available pages
                page_sections[section_name] = available_pages
        
        # Create expandable sections
        selected_page = None
        for section, pages in page_sections.items():
            with st.expander(section, expanded=(section == "🎯 Getting Started")):
                for page in pages:
                    if st.button(page, key=f"nav_{page}", use_container_width=True):
                        selected_page = page
        
        # If no page selected, default to the first available page
        if selected_page is None:
            if available_components.get("Framework Overview", False):
                selected_page = "Framework Overview"
            elif available_components.get("Prompt Testing Sandbox", False):
                selected_page = "Prompt Testing Sandbox"
            else:
                # Fallback to first available page
                available_pages = [page for page, available in available_components.items() if available]
                selected_page = available_pages[0] if available_pages else "Usage Analytics"
        
        # Show current selection and availability info
        st.markdown("---")
        st.markdown(f"**Current:** {selected_page}")
        
        # Show component count for transparency
        total_available = sum(1 for available in available_components.values() if available)
        total_components = len(available_components)
        st.markdown(f"**Available Components:** {total_available}/{total_components}")
        
        # Render session management UI
        session_manager.render_session_management_ui()
    
    # Track page view for analytics and update navigation preferences
    try:
        track_page_view(selected_page)
        session_manager.update_navigation_preferences({'last_page': selected_page})
        session_manager.log_activity('page_navigation', {'page': selected_page})
    except Exception:
        # Don't let analytics errors break the app
        pass
    
    return selected_page, app_config


def route_to_page(page_name, app_config):
    """Route to the appropriate page based on selection with environment awareness"""
    
    # Check if the requested page is available in current environment
    available_components = app_config.get_available_components()
    if not available_components.get(page_name, False):
        st.error(f"⚠️ Component '{page_name}' is not available in {app_config.environment} environment")
        
        # Show available alternatives
        available_pages = [page for page, available in available_components.items() if available]
        if available_pages:
            st.info(f"Available components: {', '.join(available_pages[:5])}")
        return
    
    # Define page configurations for better maintainability
    page_configs = {
        "Framework Overview": {
            "title": "🏗️ Framework Overview",
            "component": "framework_overview"
        },
        "Command Explorer": {
            "title": "🔍 Command Explorer", 
            "component": "command_explorer"
        },
        "Prompt Component Explorer": {
            "title": "🔧 Prompt Component Explorer",
            "component": "module_visualizer"
        },
        "Prompt Optimization Assistant": {
            "title": "🚀 Prompt Optimization Assistant",
            "component": "context_aware_analyzer"
        },
        "Prompt Pattern Discovery": {
            "title": "🔍 Prompt Pattern Discovery",
            "component": "prompt_pattern_discovery"
        },
        "Natural Language Interface": {
            "title": "🗣️ Natural Language Interface",
            "component": "natural_language_interface"
        },
        "Prompt Constructor": {
            "title": "🔨 Prompt Constructor",
            "component": "prompt_constructor"
        },
        "Interactive Prompt Builder": {
            "title": "🔧 Interactive Prompt Builder",
            "component": "interactive_prompt_builder"
        },
        "Prompt Effectiveness Testing": {
            "title": "🧪 Prompt Effectiveness Testing",
            "component": "prompt_effectiveness_testing"
        },
        "A/B Prompt Comparison": {
            "title": "⚖️ A/B Prompt Comparison",
            "component": "ab_prompt_comparison"
        },
        "Pattern Recognition Engine": {
            "title": "🧠 Pattern Recognition Engine",
            "component": "pattern_recognition_engine"
        },
        "Intelligent Recommendation Engine": {
            "title": "🎯 Intelligent Recommendation Engine",
            "component": "intelligent_recommendation_engine"
        },
        "Visual Flow Builder": {
            "title": "🎯 Visual Flow Builder",
            "component": "visual_flow_builder"
        },
        "Dependency Graph": {
            "title": "🔗 Dependency Graph",
            "component": "dependency_graph"
        },
        "Prompt Preview": {
            "title": "🔍 Real-time Prompt Preview",
            "component": "prompt_preview"
        },
        "Template Manager": {
            "title": "📚 Template Manager",
            "component": "template_manager"
        },
        "URL Sharing": {
            "title": "🔗 URL Sharing",
            "component": "url_sharing"
        },
        "AI Routing Engine": {
            "title": "🎯 AI-Powered Routing Engine",
            "component": "routing_engine"
        },
        "Decision Tree Visualizer": {
            "title": "🌳 Decision Tree Visualizer",
            "component": "decision_tree_visualizer"
        },
        "A/B Testing Framework": {
            "title": "🧪 A/B Testing Framework",
            "component": "ab_testing"
        },
        "Prompt Testing Sandbox": {
            "title": "🧪 Prompt Testing Sandbox",
            "component": "prompt_sandbox"
        },
        "Quality Gates": {
            "title": "🛡️ Quality Gates",
            "component": "quality_gates"
        },
        "Routing Simulator": {
            "title": "🎯 Routing Simulator",
            "component": "routing_simulator"
        },
        "Meta Framework": {
            "title": "🌟 Meta Framework",
            "component": "meta_framework"
        },
        "Performance Monitor": {
            "title": "📊 Performance Monitor",
            "component": "performance_monitor"
        },
        "Usage Analytics": {
            "title": "📈 Usage Analytics",
            "component": "usage_analytics"
        }
    }
    
    # Route to the appropriate page
    if page_name in page_configs:
        config = page_configs[page_name]
        
        # Handle component rendering
        if "component" in config:
            if config["component"] == "command_explorer":
                try:
                    # Verify framework path exists
                    if not app_config.FRAMEWORK_PATH or not app_config.FRAMEWORK_PATH.exists():
                        st.error(f"Framework directory not found at: {app_config.FRAMEWORK_PATH}")
                        return
                    
                    explorer = CommandExplorer(framework_path=app_config.FRAMEWORK_PATH)
                    explorer.render()
                except Exception as e:
                    st.error(f"Error loading Command Explorer: {str(e)}")
                    with st.expander("Error Details"):
                        import traceback
                        st.code(traceback.format_exc())
            elif config["component"] == "module_visualizer":
                try:
                    # Verify framework path exists
                    if not app_config.FRAMEWORK_PATH or not app_config.FRAMEWORK_PATH.exists():
                        st.error(f"Framework directory not found at: {app_config.FRAMEWORK_PATH}")
                        return
                        
                    visualizer = ModuleVisualizer(framework_path=app_config.FRAMEWORK_PATH)
                    visualizer.render()
                except Exception as e:
                    st.error(f"Error loading Module Visualizer: {str(e)}")
                    with st.expander("Error Details"):
                        import traceback
                        st.code(traceback.format_exc())
            elif config["component"] == "context_aware_analyzer":
                try:
                    # Verify framework path exists
                    if not app_config.FRAMEWORK_PATH.exists():
                        st.error(f"Framework directory not found at: {app_config.FRAMEWORK_PATH}")
                        return
                        
                    analyzer = ContextAwareAnalyzer(framework_path=app_config.FRAMEWORK_PATH)
                    analyzer.render()
                except Exception as e:
                    st.error(f"Error loading Context-Aware Analyzer: {str(e)}")
                    with st.expander("Error Details"):
                        import traceback
                        st.code(traceback.format_exc())
            elif config["component"] == "prompt_pattern_discovery":
                try:
                    # Verify framework path exists
                    if not app_config.FRAMEWORK_PATH.exists():
                        st.error(f"Framework directory not found at: {app_config.FRAMEWORK_PATH}")
                        return
                        
                    pattern_discovery = PromptPatternDiscovery(framework_path=app_config.FRAMEWORK_PATH)
                    pattern_discovery.render()
                except Exception as e:
                    st.error(f"Error loading Prompt Pattern Discovery: {str(e)}")
                    with st.expander("Error Details"):
                        import traceback
                        st.code(traceback.format_exc())
            elif config["component"] == "natural_language_interface":
                try:
                    # Verify framework path exists
                    if not app_config.FRAMEWORK_PATH.exists():
                        st.error(f"Framework directory not found at: {app_config.FRAMEWORK_PATH}")
                        return
                        
                    interface = NaturalLanguageInterface(framework_path=app_config.FRAMEWORK_PATH)
                    interface.render()
                except Exception as e:
                    st.error(f"Error loading Natural Language Interface: {str(e)}")
                    with st.expander("Error Details"):
                        import traceback
                        st.code(traceback.format_exc())
            elif config["component"] == "framework_overview":
                try:
                    # Verify framework path exists
                    if not app_config.FRAMEWORK_PATH.exists():
                        st.error(f"Framework directory not found at: {app_config.FRAMEWORK_PATH}")
                        return
                        
                    overview = FrameworkOverview(framework_path=app_config.FRAMEWORK_PATH)
                    overview.render()
                except Exception as e:
                    st.error(f"Error loading Framework Overview: {str(e)}")
                    with st.expander("Error Details"):
                        import traceback
                        st.code(traceback.format_exc())
            elif config["component"] == "prompt_constructor":
                try:
                    # Verify framework path exists
                    if not app_config.FRAMEWORK_PATH.exists():
                        st.error(f"Framework directory not found at: {app_config.FRAMEWORK_PATH}")
                        return
                        
                    constructor = PromptConstructor(framework_path=app_config.FRAMEWORK_PATH)
                    constructor.render()
                except Exception as e:
                    st.error(f"Error loading Prompt Constructor: {str(e)}")
                    with st.expander("Error Details"):
                        import traceback
                        st.code(traceback.format_exc())
            elif config["component"] == "interactive_prompt_builder":
                try:
                    # Verify framework path exists
                    if not app_config.FRAMEWORK_PATH.exists():
                        st.error(f"Framework directory not found at: {app_config.FRAMEWORK_PATH}")
                        return
                        
                    builder = InteractivePromptBuilder(framework_path=app_config.FRAMEWORK_PATH)
                    builder.render()
                except Exception as e:
                    st.error(f"Error loading Interactive Prompt Builder: {str(e)}")
                    with st.expander("Error Details"):
                        import traceback
                        st.code(traceback.format_exc())
            elif config["component"] == "prompt_effectiveness_testing":
                try:
                    # Verify framework path exists
                    if not app_config.FRAMEWORK_PATH.exists():
                        st.error(f"Framework directory not found at: {app_config.FRAMEWORK_PATH}")
                        return
                        
                    testing = PromptEffectivenessTesting(framework_path=app_config.FRAMEWORK_PATH)
                    testing.render()
                except Exception as e:
                    st.error(f"Error loading Prompt Effectiveness Testing: {str(e)}")
                    with st.expander("Error Details"):
                        import traceback
                        st.code(traceback.format_exc())
            elif config["component"] == "ab_prompt_comparison":
                try:
                    # Verify framework path exists
                    if not app_config.FRAMEWORK_PATH.exists():
                        st.error(f"Framework directory not found at: {app_config.FRAMEWORK_PATH}")
                        return
                        
                    ab_comparison = ABPromptComparison(framework_path=app_config.FRAMEWORK_PATH)
                    ab_comparison.render()
                except Exception as e:
                    st.error(f"Error loading A/B Prompt Comparison: {str(e)}")
                    with st.expander("Error Details"):
                        import traceback
                        st.code(traceback.format_exc())
            elif config["component"] == "pattern_recognition_engine":
                try:
                    # Verify framework path exists
                    if not app_config.FRAMEWORK_PATH.exists():
                        st.error(f"Framework directory not found at: {app_config.FRAMEWORK_PATH}")
                        return
                        
                    pattern_engine = PatternRecognitionEngine(framework_path=app_config.FRAMEWORK_PATH)
                    pattern_engine.render()
                except Exception as e:
                    st.error(f"Error loading Pattern Recognition Engine: {str(e)}")
                    with st.expander("Error Details"):
                        import traceback
                        st.code(traceback.format_exc())
            elif config["component"] == "intelligent_recommendation_engine":
                try:
                    # Verify framework path exists
                    if not app_config.FRAMEWORK_PATH.exists():
                        st.error(f"Framework directory not found at: {app_config.FRAMEWORK_PATH}")
                        return
                        
                    recommendation_engine = IntelligentRecommendationEngine(framework_path=app_config.FRAMEWORK_PATH)
                    recommendation_engine.render()
                except Exception as e:
                    st.error(f"Error loading Intelligent Recommendation Engine: {str(e)}")
                    with st.expander("Error Details"):
                        import traceback
                        st.code(traceback.format_exc())
            elif config["component"] == "visual_flow_builder":
                try:
                    # Verify framework path exists
                    if not app_config.FRAMEWORK_PATH.exists():
                        st.error(f"Framework directory not found at: {app_config.FRAMEWORK_PATH}")
                        return
                        
                    flow_builder = VisualFlowBuilder(framework_path=app_config.FRAMEWORK_PATH)
                    flow_builder.render()
                except Exception as e:
                    st.error(f"Error loading Visual Flow Builder: {str(e)}")
                    with st.expander("Error Details"):
                        import traceback
                        st.code(traceback.format_exc())
            elif config["component"] == "dependency_graph":
                try:
                    # Verify framework path exists
                    if not app_config.FRAMEWORK_PATH.exists():
                        st.error(f"Framework directory not found at: {app_config.FRAMEWORK_PATH}")
                        return
                        
                    dependency_graph = DependencyGraph(framework_path=app_config.FRAMEWORK_PATH)
                    dependency_graph.render()
                except Exception as e:
                    st.error(f"Error loading Dependency Graph: {str(e)}")
                    with st.expander("Error Details"):
                        import traceback
                        st.code(traceback.format_exc())
            elif config["component"] == "prompt_preview":
                try:
                    # Verify framework path exists
                    if not app_config.FRAMEWORK_PATH.exists():
                        st.error(f"Framework directory not found at: {app_config.FRAMEWORK_PATH}")
                        return
                        
                    prompt_preview = PromptPreview(framework_path=app_config.FRAMEWORK_PATH)
                    prompt_preview.render()
                except Exception as e:
                    st.error(f"Error loading Prompt Preview: {str(e)}")
                    with st.expander("Error Details"):
                        import traceback
                        st.code(traceback.format_exc())
            elif config["component"] == "template_manager":
                try:
                    # Verify framework path exists
                    if not app_config.FRAMEWORK_PATH.exists():
                        st.error(f"Framework directory not found at: {app_config.FRAMEWORK_PATH}")
                        return
                    
                    # Create template storage directory if it doesn't exist
                    template_storage_path = Path("templates")
                    template_manager = TemplateManager(
                        template_storage_path=template_storage_path,
                        framework_path=app_config.FRAMEWORK_PATH
                    )
                    template_manager.render()
                except Exception as e:
                    st.error(f"Error loading Template Manager: {str(e)}")
                    with st.expander("Error Details"):
                        import traceback
                        st.code(traceback.format_exc())
            elif config["component"] == "url_sharing":
                try:
                    # Create sharing storage directory if it doesn't exist
                    sharing_storage_path = Path("sharing")
                    url_sharing_manager = URLSharingManager(sharing_storage_path=sharing_storage_path)
                    url_sharing_manager.render()
                except Exception as e:
                    st.error(f"Error loading URL Sharing Manager: {str(e)}")
                    with st.expander("Error Details"):
                        import traceback
                        st.code(traceback.format_exc())
            elif config["component"] == "routing_engine":
                try:
                    # Verify framework path exists
                    if not app_config.FRAMEWORK_PATH.exists():
                        st.error(f"Framework directory not found at: {app_config.FRAMEWORK_PATH}")
                        return
                        
                    # Use current working directory as project path for analysis
                    project_path = Path.cwd()
                    routing_engine = RoutingEngine(
                        framework_path=app_config.FRAMEWORK_PATH,
                        project_path=project_path
                    )
                    routing_engine.render()
                except Exception as e:
                    st.error(f"Error loading AI Routing Engine: {str(e)}")
                    with st.expander("Error Details"):
                        import traceback
                        st.code(traceback.format_exc())
            elif config["component"] == "decision_tree_visualizer":
                try:
                    # Verify framework path exists
                    if not app_config.FRAMEWORK_PATH.exists():
                        st.error(f"Framework directory not found at: {app_config.FRAMEWORK_PATH}")
                        return
                        
                    decision_tree_visualizer = DecisionTreeVisualizer(framework_path=app_config.FRAMEWORK_PATH)
                    decision_tree_visualizer.render()
                except Exception as e:
                    st.error(f"Error loading Decision Tree Visualizer: {str(e)}")
                    with st.expander("Error Details"):
                        import traceback
                        st.code(traceback.format_exc())
            elif config["component"] == "ab_testing":
                try:
                    # Create A/B testing storage directory if it doesn't exist
                    ab_testing_storage_path = Path("data/ab_testing")
                    ab_testing_framework = ABTestingFramework(storage_path=ab_testing_storage_path)
                    ab_testing_framework.render()
                except Exception as e:
                    st.error(f"Error loading A/B Testing Framework: {str(e)}")
                    with st.expander("Error Details"):
                        import traceback
                        st.code(traceback.format_exc())
            elif config["component"] == "prompt_sandbox":
                try:
                    # Create prompt sandbox storage directory if it doesn't exist
                    prompt_sandbox_storage_path = Path("data/prompt_sandbox")
                    prompt_sandbox = PromptSandbox(storage_path=prompt_sandbox_storage_path)
                    prompt_sandbox.render()
                except Exception as e:
                    st.error(f"Error loading Prompt Testing Sandbox: {str(e)}")
                    with st.expander("Error Details"):
                        import traceback
                        st.code(traceback.format_exc())
            elif config["component"] == "quality_gates":
                try:
                    # Verify framework path exists
                    if not app_config.FRAMEWORK_PATH.exists():
                        st.error(f"Framework directory not found at: {app_config.FRAMEWORK_PATH}")
                        return
                        
                    dashboard = QualityGatesDashboard(framework_path=app_config.FRAMEWORK_PATH)
                    dashboard.render()
                except Exception as e:
                    st.error(f"Error loading Quality Gates Dashboard: {str(e)}")
                    with st.expander("Error Details"):
                        import traceback
                        st.code(traceback.format_exc())
            elif config["component"] == "routing_simulator":
                try:
                    # Verify framework path exists
                    if not app_config.FRAMEWORK_PATH.exists():
                        st.error(f"Framework directory not found at: {app_config.FRAMEWORK_PATH}")
                        return
                        
                    simulator = RoutingSimulator(framework_path=app_config.FRAMEWORK_PATH)
                    simulator.render()
                except Exception as e:
                    st.error(f"Error loading Routing Simulator: {str(e)}")
                    with st.expander("Error Details"):
                        import traceback
                        st.code(traceback.format_exc())
            elif config["component"] == "meta_framework":
                try:
                    # Verify framework path exists
                    if not app_config.FRAMEWORK_PATH.exists():
                        st.error(f"Framework directory not found at: {app_config.FRAMEWORK_PATH}")
                        return
                        
                    meta_panel = MetaFrameworkControlPanel(framework_path=app_config.FRAMEWORK_PATH)
                    meta_panel.render()
                except Exception as e:
                    st.error(f"Error loading Meta Framework Control Panel: {str(e)}")
                    with st.expander("Error Details"):
                        import traceback
                        st.code(traceback.format_exc())
            elif config["component"] == "performance_monitor":
                try:
                    # Create logs directory if it doesn't exist
                    logs_path = Path("logs")
                    performance_monitor = PerformanceMonitor(log_dir=logs_path)
                    performance_monitor.render()
                except Exception as e:
                    st.error(f"Error loading Performance Monitor: {str(e)}")
                    with st.expander("Error Details"):
                        import traceback
                        st.code(traceback.format_exc())
            elif config["component"] == "usage_analytics":
                try:
                    # Create analytics storage directory if it doesn't exist
                    analytics_storage_path = Path("data/analytics")
                    usage_analytics = UsageAnalytics(storage_path=analytics_storage_path)
                    usage_analytics.render()
                except Exception as e:
                    st.error(f"Error loading Usage Analytics: {str(e)}")
                    with st.expander("Error Details"):
                        import traceback
                        st.code(traceback.format_exc())
            elif config["component"] == "health_monitor":
                try:
                    # Render health monitoring dashboard
                    health_monitor.render_health_dashboard()
                except Exception as e:
                    st.error(f"Error loading Health Monitor: {str(e)}")
                    if app_config.debug_mode:
                        with st.expander("Error Details"):
                            import traceback
                            st.code(traceback.format_exc())
                    else:
                        health_monitor.log_error(e, "health_monitor_render")
        else:
            st.info(config["message"])
    else:
        st.error(f"Unknown page: {page_name}")


def configure_security():
    """Configure security settings and professional styling for the Streamlit app"""
    # Set security-related page config with professional branding
    st.set_page_config(
        page_title="Claude Code Framework Dashboard | Enterprise Prompt Engineering",
        page_icon="🤖",
        layout="wide",
        initial_sidebar_state="expanded",
        menu_items={
            'Report a bug': None,  # Disable default menu items for security
            'Get Help': None,
            'About': """# Claude Code Framework Dashboard
            
**Enterprise-Grade Prompt Engineering Platform**

🚀 **Features:**
- Advanced prompt optimization and testing
- Comprehensive framework management
- Real-time performance monitoring
- Secure multi-environment deployment

🔒 **Security:** Production-ready with comprehensive monitoring
⚡ **Performance:** Optimized for enterprise workloads
🎯 **Quality:** 98%+ test coverage with TDD methodology

*Powered by Claude 4 with advanced reasoning capabilities*
            """
        }
    )
    
    # Add professional CSS styling
    st.markdown("""
    <style>
    /* Professional color scheme */
    .stApp {
        background: linear-gradient(135deg, #f8f9fa 0%, #ffffff 100%);
    }
    
    /* Sidebar styling */
    .css-1d391kg {
        background: linear-gradient(180deg, #1f77b4 0%, #17becf 100%);
    }
    
    /* Main content styling */
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    
    /* Professional button styling */
    .stButton > button {
        background: linear-gradient(90deg, #1f77b4 0%, #17becf 100%);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.5rem 1rem;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        transform: translateY(-1px);
        box-shadow: 0 4px 8px rgba(31, 119, 180, 0.3);
    }
    
    /* Professional metrics styling */
    div[data-testid="metric-container"] {
        background: white;
        border: 1px solid #e0e0e0;
        padding: 1rem;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    
    /* Success message styling */
    .stSuccess {
        background: linear-gradient(90deg, #d4edda 0%, #c3e6cb 100%);
        border-left: 4px solid #28a745;
    }
    
    /* Warning message styling */
    .stWarning {
        background: linear-gradient(90deg, #fff3cd 0%, #ffeaa7 100%);
        border-left: 4px solid #ffc107;
    }
    
    /* Error message styling */
    .stError {
        background: linear-gradient(90deg, #f8d7da 0%, #f5c6cb 100%);
        border-left: 4px solid #dc3545;
    }
    </style>
    """, unsafe_allow_html=True)


def main():
    """Main application entry point with dual-environment support and security"""
    # Configure security settings and professional styling
    configure_security()
    
    # Render professional hero section
    UIBranding.render_hero_section()
    
    # Setup navigation and get selected page with configuration
    with LoadingStates.loading_spinner("Initializing dashboard...", delay=0.2):
        selected_page, app_config = setup_navigation()
    
    # Show environment status with professional badge
    col1, col2, col3 = st.columns([2, 1, 1])
    with col1:
        env = EnvironmentDetector.detect_environment()
        if env == "development":
            ProfessionalComponents.render_status_badge("healthy", "Development Mode")
        elif env == "railway":
            ProfessionalComponents.render_status_badge("info", "Production Mode")
        else:
            ProfessionalComponents.render_status_badge("warning", f"{env.title()} Mode")
    
    with col2:
        # Show framework availability
        if app_config.FRAMEWORK_PATH and app_config.FRAMEWORK_PATH.exists():
            ProfessionalComponents.render_status_badge("healthy", "Framework Available")
        else:
            ProfessionalComponents.render_status_badge("warning", "Limited Mode")
    
    with col3:
        # Show component count
        total_available = sum(1 for available in app_config.get_available_components().values() if available)
        total_components = len(app_config.get_available_components())
        ProfessionalComponents.render_status_badge("info", f"{total_available}/{total_components} Components")
    
    st.markdown("---")
    
    # Route to the selected page with environment-aware configuration
    route_to_page(selected_page, app_config)


if __name__ == "__main__":
    main()