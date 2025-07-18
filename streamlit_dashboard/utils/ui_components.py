"""
Professional UI components for first-class MVP experience
Provides branding, loading states, error handling, and professional styling
"""

import streamlit as st
import time
from typing import Optional, Any, Callable
from contextlib import contextmanager


class UIBranding:
    """Professional branding and styling utilities"""
    
    # Brand colors
    PRIMARY_COLOR = "#1f77b4"      # Professional blue
    SECONDARY_COLOR = "#ff7f0e"    # Accent orange
    SUCCESS_COLOR = "#2ca02c"      # Success green
    WARNING_COLOR = "#d62728"      # Warning red
    INFO_COLOR = "#17becf"         # Info cyan
    
    # Typography
    TITLE_FONT = "sans-serif"
    BODY_FONT = "sans-serif"
    
    @staticmethod
    def render_hero_section():
        """Render professional hero section"""
        st.markdown("""
        <div style="
            background: linear-gradient(90deg, #1f77b4 0%, #17becf 100%);
            padding: 2rem;
            border-radius: 10px;
            margin-bottom: 2rem;
            text-align: center;
            color: white;
        ">
            <h1 style="margin: 0; font-size: 2.5rem; font-weight: 700;">
                🤖 Claude Code Framework Dashboard
            </h1>
            <p style="margin: 0.5rem 0 0 0; font-size: 1.2rem; opacity: 0.9;">
                Enterprise-grade prompt engineering platform
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    @staticmethod
    def render_feature_card(title: str, description: str, icon: str = "⚡", status: str = "available"):
        """Render professional feature card"""
        status_color = {
            "available": UIBranding.SUCCESS_COLOR,
            "limited": UIBranding.WARNING_COLOR,
            "unavailable": "#666666"
        }.get(status, UIBranding.INFO_COLOR)
        
        status_text = {
            "available": "✅ Available",
            "limited": "⚠️ Limited",
            "unavailable": "❌ Unavailable"
        }.get(status, "ℹ️ Unknown")
        
        st.markdown(f"""
        <div style="
            border: 2px solid {status_color};
            border-radius: 8px;
            padding: 1.5rem;
            margin: 1rem 0;
            background: linear-gradient(145deg, #ffffff 0%, #f8f9fa 100%);
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        ">
            <div style="display: flex; align-items: center; margin-bottom: 0.5rem;">
                <span style="font-size: 1.5rem; margin-right: 0.5rem;">{icon}</span>
                <h3 style="margin: 0; color: #333;">{title}</h3>
                <span style="margin-left: auto; color: {status_color}; font-weight: bold;">
                    {status_text}
                </span>
            </div>
            <p style="margin: 0; color: #666; line-height: 1.5;">{description}</p>
        </div>
        """, unsafe_allow_html=True)
    
    @staticmethod
    def render_page_header(title: str, description: str = "", icon: str = "📊"):
        """Render professional page header"""
        st.markdown(f"""
        <div style="
            border-bottom: 3px solid {UIBranding.PRIMARY_COLOR};
            padding-bottom: 1rem;
            margin-bottom: 2rem;
        ">
            <h1 style="
                color: {UIBranding.PRIMARY_COLOR};
                margin: 0;
                display: flex;
                align-items: center;
                font-size: 2rem;
                font-weight: 600;
            ">
                <span style="margin-right: 0.5rem; font-size: 1.8rem;">{icon}</span>
                {title}
            </h1>
            {f'<p style="margin: 0.5rem 0 0 0; color: #666; font-size: 1.1rem;">{description}</p>' if description else ''}
        </div>
        """, unsafe_allow_html=True)


class LoadingStates:
    """Professional loading states and progress indicators"""
    
    @staticmethod
    @contextmanager
    def loading_spinner(message: str = "Loading...", delay: float = 0.1):
        """Context manager for loading operations with spinner"""
        placeholder = st.empty()
        
        with placeholder.container():
            col1, col2, col3 = st.columns([1, 2, 1])
            with col2:
                st.markdown(f"""
                <div style="text-align: center; padding: 2rem;">
                    <div style="font-size: 2rem; margin-bottom: 1rem;">⏳</div>
                    <p style="color: #666;">{message}</p>
                </div>
                """, unsafe_allow_html=True)
        
        if delay > 0:
            time.sleep(delay)
        
        try:
            yield
        finally:
            placeholder.empty()
    
    @staticmethod
    @contextmanager
    def progress_operation(total_steps: int, operation_name: str = "Processing"):
        """Context manager for operations with progress tracking"""
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        class ProgressTracker:
            def __init__(self):
                self.current_step = 0
            
            def update(self, step_name: str = ""):
                self.current_step += 1
                progress = min(self.current_step / total_steps, 1.0)
                progress_bar.progress(progress)
                
                status_msg = f"{operation_name}: {step_name}" if step_name else operation_name
                status_text.text(f"Step {self.current_step}/{total_steps}: {status_msg}")
        
        tracker = ProgressTracker()
        
        try:
            yield tracker
        finally:
            progress_bar.empty()
            status_text.empty()
    
    @staticmethod
    def render_skeleton_screen(lines: int = 3):
        """Render skeleton loading screen"""
        for i in range(lines):
            width = [100, 80, 60, 90][i % 4]  # Varying widths for realism
            st.markdown(f"""
            <div style="
                width: {width}%;
                height: 20px;
                background: linear-gradient(90deg, #f0f0f0 25%, #e0e0e0 50%, #f0f0f0 75%);
                background-size: 200% 100%;
                animation: loading 1.5s infinite;
                border-radius: 4px;
                margin: 8px 0;
            "></div>
            """, unsafe_allow_html=True)
        
        # Add CSS animation
        st.markdown("""
        <style>
        @keyframes loading {
            0% { background-position: 200% 0; }
            100% { background-position: -200% 0; }
        }
        </style>
        """, unsafe_allow_html=True)


class ErrorHandling:
    """Professional error handling and user guidance"""
    
    @staticmethod
    def render_error_page(error_type: str, title: str, message: str, suggestions: list = None):
        """Render professional error page"""
        error_icons = {
            "not_found": "🔍",
            "permission": "🔒", 
            "network": "🌐",
            "server": "⚙️",
            "validation": "⚠️",
            "timeout": "⏰",
            "generic": "❌"
        }
        
        icon = error_icons.get(error_type, error_icons["generic"])
        
        st.markdown(f"""
        <div style="
            text-align: center;
            padding: 3rem 2rem;
            border: 2px solid {UIBranding.WARNING_COLOR};
            border-radius: 12px;
            background: linear-gradient(145deg, #fff5f5 0%, #ffffff 100%);
            margin: 2rem 0;
        ">
            <div style="font-size: 4rem; margin-bottom: 1rem;">{icon}</div>
            <h2 style="color: {UIBranding.WARNING_COLOR}; margin-bottom: 1rem;">{title}</h2>
            <p style="color: #666; font-size: 1.1rem; margin-bottom: 1.5rem;">{message}</p>
        </div>
        """, unsafe_allow_html=True)
        
        if suggestions:
            st.subheader("💡 Try these suggestions:")
            for i, suggestion in enumerate(suggestions, 1):
                st.markdown(f"**{i}.** {suggestion}")
    
    @staticmethod
    def render_maintenance_page():
        """Render maintenance mode page"""
        st.markdown(f"""
        <div style="
            text-align: center;
            padding: 4rem 2rem;
            background: linear-gradient(145deg, #f8f9fa 0%, #ffffff 100%);
            border-radius: 12px;
            margin: 2rem 0;
        ">
            <div style="font-size: 4rem; margin-bottom: 1rem;">🔧</div>
            <h1 style="color: {UIBranding.PRIMARY_COLOR}; margin-bottom: 1rem;">
                System Maintenance
            </h1>
            <p style="color: #666; font-size: 1.1rem; margin-bottom: 1.5rem;">
                We're making improvements to provide you with a better experience.
            </p>
            <p style="color: #888; font-size: 1rem;">
                Please check back in a few minutes.
            </p>
        </div>
        """, unsafe_allow_html=True)


class ProfessionalComponents:
    """Additional professional UI components"""
    
    @staticmethod
    def render_metrics_card(title: str, value: str, change: str = "", trend: str = "neutral"):
        """Render professional metrics card"""
        trend_colors = {
            "up": UIBranding.SUCCESS_COLOR,
            "down": UIBranding.WARNING_COLOR,
            "neutral": "#666666"
        }
        
        trend_icons = {
            "up": "📈",
            "down": "📉",
            "neutral": "📊"
        }
        
        trend_color = trend_colors.get(trend, trend_colors["neutral"])
        trend_icon = trend_icons.get(trend, trend_icons["neutral"])
        
        st.markdown(f"""
        <div style="
            background: white;
            padding: 1.5rem;
            border-radius: 8px;
            border-left: 4px solid {UIBranding.PRIMARY_COLOR};
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            margin: 1rem 0;
        ">
            <div style="color: #666; font-size: 0.9rem; margin-bottom: 0.5rem;">
                {title}
            </div>
            <div style="
                font-size: 2rem;
                font-weight: bold;
                color: {UIBranding.PRIMARY_COLOR};
                margin-bottom: 0.5rem;
            ">
                {value}
            </div>
            {f'<div style="color: {trend_color}; font-size: 0.9rem;"><span style="margin-right: 0.25rem;">{trend_icon}</span>{change}</div>' if change else ''}
        </div>
        """, unsafe_allow_html=True)
    
    @staticmethod
    def render_status_badge(status: str, label: str = ""):
        """Render professional status badge"""
        status_config = {
            "healthy": {"color": UIBranding.SUCCESS_COLOR, "icon": "✅", "text": "Healthy"},
            "warning": {"color": UIBranding.WARNING_COLOR, "icon": "⚠️", "text": "Warning"},
            "error": {"color": UIBranding.WARNING_COLOR, "icon": "❌", "text": "Error"},
            "info": {"color": UIBranding.INFO_COLOR, "icon": "ℹ️", "text": "Info"},
            "loading": {"color": "#666666", "icon": "⏳", "text": "Loading"}
        }
        
        config = status_config.get(status, status_config["info"])
        display_text = label if label else config["text"]
        
        st.markdown(f"""
        <span style="
            background: {config['color']};
            color: white;
            padding: 0.25rem 0.75rem;
            border-radius: 20px;
            font-size: 0.85rem;
            font-weight: bold;
            display: inline-flex;
            align-items: center;
            margin: 0.25rem;
        ">
            <span style="margin-right: 0.25rem;">{config['icon']}</span>
            {display_text}
        </span>
        """, unsafe_allow_html=True)


def safe_component_render(component_func: Callable, component_name: str, 
                         app_config: Any, fallback_message: str = None):
    """
    Safely render a component with professional error handling
    """
    try:
        with LoadingStates.loading_spinner(f"Loading {component_name}...", delay=0.1):
            return component_func()
    except ImportError as e:
        ErrorHandling.render_error_page(
            "not_found",
            f"{component_name} Not Available",
            f"The {component_name} component is not available in this environment.",
            [
                "This feature may require additional dependencies",
                "Check if the framework directory is accessible",
                "Try refreshing the page or contact support"
            ]
        )
        return None
    except Exception as e:
        if app_config.debug_mode:
            st.error(f"Error loading {component_name}: {str(e)}")
            with st.expander("Technical Details"):
                import traceback
                st.code(traceback.format_exc())
        else:
            ErrorHandling.render_error_page(
                "generic",
                f"Unable to Load {component_name}",
                "We encountered an unexpected issue while loading this component.",
                [
                    "Try refreshing the page",
                    "Check your internet connection",
                    "Contact support if the problem persists"
                ]
            )
        return None