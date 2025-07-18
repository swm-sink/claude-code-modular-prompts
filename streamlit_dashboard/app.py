"""
Main Streamlit application for Claude Code Modular Prompts Framework Dashboard
Follows separation of concerns - handles only configuration and routing
"""

import streamlit as st
from pathlib import Path
from components.command_explorer import CommandExplorer
from components.module_visualizer import ModuleVisualizer
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


class AppConfig:
    """Configuration class for the Streamlit dashboard"""
    
    # Use absolute path to ensure correct resolution
    FRAMEWORK_PATH = Path("/Users/smenssink/Documents/Github/claude-code-modular-prompts/.claude")
    PAGE_TITLE = "Claude Code Framework Dashboard"
    PAGE_ICON = "🧠"
    
    # Page configuration
    LAYOUT = "wide"
    INITIAL_SIDEBAR_STATE = "expanded"
    
    # Navigation options
    NAVIGATION_PAGES = [
        "Framework Overview",
        "Command Explorer", 
        "Module Visualizer",
        "Prompt Constructor",
        "Visual Flow Builder",
        "Dependency Graph",
        "Prompt Preview",
        "Template Manager",
        "URL Sharing",
        "AI Routing Engine",
        "Decision Tree Visualizer",
        "A/B Testing Framework",
        "Prompt Testing Sandbox",
        "Quality Gates",
        "Routing Simulator",
        "Meta Framework",
        "Performance Monitor",
        "Usage Analytics"
    ]


def setup_navigation():
    """Set up the navigation menu for the dashboard"""
    st.set_page_config(
        page_title=AppConfig.PAGE_TITLE,
        page_icon=AppConfig.PAGE_ICON,
        layout=AppConfig.LAYOUT,
        initial_sidebar_state=AppConfig.INITIAL_SIDEBAR_STATE
    )
    
    # Create navigation in sidebar
    with st.sidebar:
        st.title("📊 Dashboard Navigation")
        selected_page = st.radio(
            "Choose a page:",
            AppConfig.NAVIGATION_PAGES
        )
    
    # Track page view for analytics
    try:
        track_page_view(selected_page)
    except Exception:
        # Don't let analytics errors break the app
        pass
    
    return selected_page


def route_to_page(page_name):
    """Route to the appropriate page based on selection"""
    
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
        "Module Visualizer": {
            "title": "🧩 Module Visualizer",
            "component": "module_visualizer"
        },
        "Prompt Constructor": {
            "title": "🔨 Prompt Constructor",
            "component": "prompt_constructor"
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
        st.title(config["title"])
        
        # Handle component rendering
        if "component" in config:
            if config["component"] == "command_explorer":
                try:
                    # Verify framework path exists
                    if not AppConfig.FRAMEWORK_PATH.exists():
                        st.error(f"Framework directory not found at: {AppConfig.FRAMEWORK_PATH}")
                        return
                    
                    explorer = CommandExplorer(framework_path=AppConfig.FRAMEWORK_PATH)
                    explorer.render()
                except Exception as e:
                    st.error(f"Error loading Command Explorer: {str(e)}")
                    with st.expander("Error Details"):
                        import traceback
                        st.code(traceback.format_exc())
            elif config["component"] == "module_visualizer":
                try:
                    # Verify framework path exists
                    if not AppConfig.FRAMEWORK_PATH.exists():
                        st.error(f"Framework directory not found at: {AppConfig.FRAMEWORK_PATH}")
                        return
                        
                    visualizer = ModuleVisualizer(framework_path=AppConfig.FRAMEWORK_PATH)
                    visualizer.render()
                except Exception as e:
                    st.error(f"Error loading Module Visualizer: {str(e)}")
                    with st.expander("Error Details"):
                        import traceback
                        st.code(traceback.format_exc())
            elif config["component"] == "framework_overview":
                try:
                    # Verify framework path exists
                    if not AppConfig.FRAMEWORK_PATH.exists():
                        st.error(f"Framework directory not found at: {AppConfig.FRAMEWORK_PATH}")
                        return
                        
                    overview = FrameworkOverview(framework_path=AppConfig.FRAMEWORK_PATH)
                    overview.render()
                except Exception as e:
                    st.error(f"Error loading Framework Overview: {str(e)}")
                    with st.expander("Error Details"):
                        import traceback
                        st.code(traceback.format_exc())
            elif config["component"] == "prompt_constructor":
                try:
                    # Verify framework path exists
                    if not AppConfig.FRAMEWORK_PATH.exists():
                        st.error(f"Framework directory not found at: {AppConfig.FRAMEWORK_PATH}")
                        return
                        
                    constructor = PromptConstructor(framework_path=AppConfig.FRAMEWORK_PATH)
                    constructor.render()
                except Exception as e:
                    st.error(f"Error loading Prompt Constructor: {str(e)}")
                    with st.expander("Error Details"):
                        import traceback
                        st.code(traceback.format_exc())
            elif config["component"] == "visual_flow_builder":
                try:
                    # Verify framework path exists
                    if not AppConfig.FRAMEWORK_PATH.exists():
                        st.error(f"Framework directory not found at: {AppConfig.FRAMEWORK_PATH}")
                        return
                        
                    flow_builder = VisualFlowBuilder(framework_path=AppConfig.FRAMEWORK_PATH)
                    flow_builder.render()
                except Exception as e:
                    st.error(f"Error loading Visual Flow Builder: {str(e)}")
                    with st.expander("Error Details"):
                        import traceback
                        st.code(traceback.format_exc())
            elif config["component"] == "dependency_graph":
                try:
                    # Verify framework path exists
                    if not AppConfig.FRAMEWORK_PATH.exists():
                        st.error(f"Framework directory not found at: {AppConfig.FRAMEWORK_PATH}")
                        return
                        
                    dependency_graph = DependencyGraph(framework_path=AppConfig.FRAMEWORK_PATH)
                    dependency_graph.render()
                except Exception as e:
                    st.error(f"Error loading Dependency Graph: {str(e)}")
                    with st.expander("Error Details"):
                        import traceback
                        st.code(traceback.format_exc())
            elif config["component"] == "prompt_preview":
                try:
                    # Verify framework path exists
                    if not AppConfig.FRAMEWORK_PATH.exists():
                        st.error(f"Framework directory not found at: {AppConfig.FRAMEWORK_PATH}")
                        return
                        
                    prompt_preview = PromptPreview(framework_path=AppConfig.FRAMEWORK_PATH)
                    prompt_preview.render()
                except Exception as e:
                    st.error(f"Error loading Prompt Preview: {str(e)}")
                    with st.expander("Error Details"):
                        import traceback
                        st.code(traceback.format_exc())
            elif config["component"] == "template_manager":
                try:
                    # Verify framework path exists
                    if not AppConfig.FRAMEWORK_PATH.exists():
                        st.error(f"Framework directory not found at: {AppConfig.FRAMEWORK_PATH}")
                        return
                    
                    # Create template storage directory if it doesn't exist
                    template_storage_path = Path("templates")
                    template_manager = TemplateManager(
                        template_storage_path=template_storage_path,
                        framework_path=AppConfig.FRAMEWORK_PATH
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
                    if not AppConfig.FRAMEWORK_PATH.exists():
                        st.error(f"Framework directory not found at: {AppConfig.FRAMEWORK_PATH}")
                        return
                        
                    # Use current working directory as project path for analysis
                    project_path = Path.cwd()
                    routing_engine = RoutingEngine(
                        framework_path=AppConfig.FRAMEWORK_PATH,
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
                    if not AppConfig.FRAMEWORK_PATH.exists():
                        st.error(f"Framework directory not found at: {AppConfig.FRAMEWORK_PATH}")
                        return
                        
                    decision_tree_visualizer = DecisionTreeVisualizer(framework_path=AppConfig.FRAMEWORK_PATH)
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
                    if not AppConfig.FRAMEWORK_PATH.exists():
                        st.error(f"Framework directory not found at: {AppConfig.FRAMEWORK_PATH}")
                        return
                        
                    dashboard = QualityGatesDashboard(framework_path=AppConfig.FRAMEWORK_PATH)
                    dashboard.render()
                except Exception as e:
                    st.error(f"Error loading Quality Gates Dashboard: {str(e)}")
                    with st.expander("Error Details"):
                        import traceback
                        st.code(traceback.format_exc())
            elif config["component"] == "routing_simulator":
                try:
                    # Verify framework path exists
                    if not AppConfig.FRAMEWORK_PATH.exists():
                        st.error(f"Framework directory not found at: {AppConfig.FRAMEWORK_PATH}")
                        return
                        
                    simulator = RoutingSimulator(framework_path=AppConfig.FRAMEWORK_PATH)
                    simulator.render()
                except Exception as e:
                    st.error(f"Error loading Routing Simulator: {str(e)}")
                    with st.expander("Error Details"):
                        import traceback
                        st.code(traceback.format_exc())
            elif config["component"] == "meta_framework":
                try:
                    # Verify framework path exists
                    if not AppConfig.FRAMEWORK_PATH.exists():
                        st.error(f"Framework directory not found at: {AppConfig.FRAMEWORK_PATH}")
                        return
                        
                    meta_panel = MetaFrameworkControlPanel(framework_path=AppConfig.FRAMEWORK_PATH)
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
        else:
            st.info(config["message"])
    else:
        st.error(f"Unknown page: {page_name}")


def main():
    """Main application entry point"""
    # Setup navigation and get selected page
    selected_page = setup_navigation()
    
    # Route to the selected page
    route_to_page(selected_page)


if __name__ == "__main__":
    main()