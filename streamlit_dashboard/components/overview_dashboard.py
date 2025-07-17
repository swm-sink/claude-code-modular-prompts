"""
Overview dashboard component for Claude Code Modular Prompts Framework
Provides high-level framework statistics and component summaries
"""

import streamlit as st
import pandas as pd
from typing import List, Dict, Any, Optional
from data.models import Framework, Command, Module


class OverviewDashboard:
    """Dashboard component for displaying framework overview and statistics"""
    
    def __init__(self):
        """Initialize the overview dashboard"""
        pass
    
    def render(self):
        """Render the complete overview dashboard"""
        self._render_header()
        
        try:
            framework = self._load_framework_data()
            self._render_dashboard_content(framework)
        except Exception as e:
            self._handle_error(e)
    
    def _render_header(self):
        """Render the dashboard header"""
        st.title("🧠 Claude Code Framework Overview")
        st.markdown("""
        This dashboard provides a comprehensive overview of the Claude Code Modular Prompts Framework,
        including commands, modules, and their relationships.
        """)
    
    def _load_framework_data(self) -> Framework:
        """Load and parse framework data"""
        from data.framework_parser import FrameworkParser
        
        parser = FrameworkParser()
        framework_data = parser.parse()
        
        return Framework.from_dict({
            'path': framework_data.get('structure', {}).get('path', '/.claude'),
            'commands': framework_data.get('commands', []),
            'modules': framework_data.get('modules', []),
            'name': 'Claude Code Modular Prompts Framework',
            'version': '3.0.0'
        })
    
    def _render_dashboard_content(self, framework: Framework):
        """Render the main dashboard content"""
        self.display_stats(framework)
        self.show_commands_summary(framework.commands)
        self.show_modules_summary(framework.modules)
    
    def _handle_error(self, error: Exception):
        """Handle and display errors"""
        st.error(f"Error loading framework data: {str(error)}")
        st.info("Please ensure the .claude directory exists and contains valid framework files.")
    
    def display_stats(self, framework: Optional[Framework]):
        """Display framework statistics and key metrics"""
        if not self._validate_framework(framework):
            return
        
        stats = self._get_framework_stats(framework)
        if stats is None:
            return
        
        st.subheader("📊 Framework Statistics")
        self._display_main_metrics(stats)
        self._display_category_breakdown(stats)
    
    def _validate_framework(self, framework: Optional[Framework]) -> bool:
        """Validate framework data availability"""
        if framework is None:
            st.error("No framework data available")
            return False
        return True
    
    def _get_framework_stats(self, framework: Framework) -> Optional[Dict[str, Any]]:
        """Get framework statistics with error handling"""
        try:
            stats = framework.statistics()
            if stats is None:
                st.error("Framework statistics are not available")
                return None
            return stats
        except Exception:
            st.error("Unable to generate framework statistics")
            return None
    
    def _display_main_metrics(self, stats: Dict[str, Any]):
        """Display main framework metrics"""
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric(
                label="Total Commands",
                value=stats.get('total_commands', 0),
                help="Number of available framework commands"
            )
        
        with col2:
            st.metric(
                label="Total Modules",
                value=stats.get('total_modules', 0),
                help="Number of framework modules"
            )
        
        with col3:
            st.metric(
                label="Total Components",
                value=stats.get('total_components', 0),
                help="Combined commands and modules"
            )
    
    def _display_category_breakdown(self, stats: Dict[str, Any]):
        """Display category breakdown tables"""
        st.subheader("📋 Category Breakdown")
        
        # Commands by category
        commands_by_category = stats.get('commands_by_category', {})
        if commands_by_category:
            st.write("**Commands by Category:**")
            cmd_df = pd.DataFrame(list(commands_by_category.items()), 
                                columns=['Category', 'Count'])
            st.dataframe(cmd_df, use_container_width=True)
        
        # Modules by category
        modules_by_category = stats.get('modules_by_category', {})
        if modules_by_category:
            st.write("**Modules by Category:**")
            mod_df = pd.DataFrame(list(modules_by_category.items()), 
                                columns=['Category', 'Count'])
            st.dataframe(mod_df, use_container_width=True)
    
    def show_commands_summary(self, commands: List[Command]):
        """Display summary of available commands"""
        st.subheader("⚡ Available Commands")
        
        if not commands:
            st.info("No commands found in the framework")
            return
        
        # Search functionality
        search_term = st.text_input("🔍 Search Commands", placeholder="Enter command name...")
        
        # Filter and display commands
        filtered_commands = self._filter_commands(commands, search_term)
        if not filtered_commands:
            self._show_no_results_message(search_term)
            return
        
        self._display_commands_table(filtered_commands)
        self._show_commands_count(filtered_commands, commands)
    
    def _filter_commands(self, commands: List[Command], search_term: str) -> List[Command]:
        """Filter commands based on search term"""
        if not search_term:
            return commands
        
        return [
            cmd for cmd in commands 
            if search_term.lower() in cmd.name.lower() or 
            (cmd.description and search_term.lower() in cmd.description.lower())
        ]
    
    def _show_no_results_message(self, search_term: str):
        """Display no results message"""
        st.warning(f"No commands found matching '{search_term}'")
    
    def _display_commands_table(self, commands: List[Command]):
        """Display commands in a table format"""
        command_data = [
            {
                'name': cmd.name,
                'category': cmd.category,
                'description': cmd.description or 'No description available',
                'path': cmd.path
            }
            for cmd in commands
        ]
        
        df = pd.DataFrame(command_data)
        st.dataframe(df, use_container_width=True)
    
    def _show_commands_count(self, filtered_commands: List[Command], all_commands: List[Command]):
        """Display commands count information"""
        st.caption(f"Showing {len(filtered_commands)} of {len(all_commands)} commands")
    
    def show_modules_summary(self, modules: List[Module]):
        """Display summary of available modules"""
        st.subheader("🧩 Framework Modules")
        
        if not modules:
            st.info("No modules found in the framework")
            return
        
        # Category filter
        categories = self._get_module_categories(modules)
        category_filter = st.selectbox(
            "Filter by Category",
            options=["All Categories"] + categories,
            index=0
        )
        
        # Filter and display modules
        filtered_modules = self._filter_modules_by_category(modules, category_filter)
        self._display_modules_by_category(filtered_modules, categories)
        self._show_modules_count(filtered_modules, modules)
    
    def _get_module_categories(self, modules: List[Module]) -> List[str]:
        """Get sorted list of module categories"""
        return sorted(list(set(module.category for module in modules)))
    
    def _filter_modules_by_category(self, modules: List[Module], category_filter: str) -> List[Module]:
        """Filter modules by selected category"""
        if category_filter == "All Categories":
            return modules
        
        return [mod for mod in modules if mod.category == category_filter]
    
    def _display_modules_by_category(self, filtered_modules: List[Module], categories: List[str]):
        """Display modules grouped by category"""
        if len(categories) > 1:
            # Show expandable sections by category
            for category in categories:
                category_modules = [mod for mod in filtered_modules if mod.category == category]
                if category_modules:
                    with st.expander(f"📁 {category.title()} ({len(category_modules)} modules)"):
                        self._display_modules_table(category_modules)
        else:
            # Show all modules in a single table
            self._display_modules_table(filtered_modules)
    
    def _show_modules_count(self, filtered_modules: List[Module], all_modules: List[Module]):
        """Display modules count information"""
        st.caption(f"Showing {len(filtered_modules)} of {len(all_modules)} modules")
    
    def _display_modules_table(self, modules: List[Module]):
        """Display modules in a table format"""
        if not modules:
            return
        
        module_data = self._prepare_module_data(modules)
        df = pd.DataFrame(module_data)
        st.dataframe(df, use_container_width=True)
    
    def _prepare_module_data(self, modules: List[Module]) -> List[Dict[str, Any]]:
        """Prepare module data for table display"""
        return [
            {
                'name': mod.name,
                'category': mod.category,
                'description': mod.description or 'No description available',
                'version': mod.version or 'N/A',
                'dependencies': len(mod.dependencies) if mod.dependencies else 0,
                'tags': ', '.join(mod.tags) if mod.tags else 'None'
            }
            for mod in modules
        ]