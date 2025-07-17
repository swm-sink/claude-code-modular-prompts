"""
Main Streamlit application for Claude Code Modular Prompts Framework Dashboard
Follows separation of concerns - handles only configuration and routing
"""

import streamlit as st
from pathlib import Path


class AppConfig:
    """Configuration class for the Streamlit dashboard"""
    
    FRAMEWORK_PATH = Path(__file__).parent.parent / ".claude"
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
        "Quality Gates",
        "Routing Simulator",
        "Meta Framework"
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
    
    return selected_page


def route_to_page(page_name):
    """Route to the appropriate page based on selection"""
    
    # Define page configurations for better maintainability
    page_configs = {
        "Framework Overview": {
            "title": "🏗️ Framework Overview",
            "message": "Framework overview component will be implemented here"
        },
        "Command Explorer": {
            "title": "🔍 Command Explorer", 
            "message": "Command explorer component will be implemented here"
        },
        "Module Visualizer": {
            "title": "🧩 Module Visualizer",
            "message": "Module visualizer component will be implemented here"
        },
        "Prompt Constructor": {
            "title": "🔨 Prompt Constructor",
            "message": "Prompt constructor component will be implemented here"
        },
        "Quality Gates": {
            "title": "🛡️ Quality Gates",
            "message": "Quality gates component will be implemented here"
        },
        "Routing Simulator": {
            "title": "🎯 Routing Simulator",
            "message": "Routing simulator component will be implemented here"
        },
        "Meta Framework": {
            "title": "🌟 Meta Framework",
            "message": "Meta framework component will be implemented here"
        }
    }
    
    # Route to the appropriate page
    if page_name in page_configs:
        config = page_configs[page_name]
        st.title(config["title"])
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