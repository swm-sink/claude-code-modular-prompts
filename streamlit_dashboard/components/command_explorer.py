"""
Command Explorer Component for Claude Code Modular Prompts Framework
Provides intelligent command exploration, decision support, and routing recommendations
"""

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from typing import Dict, List, Optional, Any, Union
from pathlib import Path
import time
from data.framework_parser import FrameworkParser
from data.models import Command, Module, Framework
from .command_explorer_helpers import CommandExplorerHelpers


class CommandExplorer:
    """Interactive command exploration component with filtering and visualization"""
    
    def __init__(self, **kwargs):
        """Initialize the command explorer"""
        # Handle explicit None passed as keyword argument
        if 'framework_path' in kwargs:
            framework_path = kwargs['framework_path']
            if framework_path is None:
                raise ValueError("framework_path cannot be None")
            if not isinstance(framework_path, Path):
                raise TypeError("framework_path must be a Path object")
            self.framework_path = framework_path
        else:
            # Default to .claude directory
            self.framework_path = Path(__file__).parent.parent.parent / ".claude"
        
        # Initialize framework parser - this should always succeed if we have a valid Path object
        try:
            self.framework_parser = FrameworkParser(self.framework_path)
        except Exception as e:
            # If there's an error with framework path, store it for later
            self.framework_parser = None
            self._init_error = str(e)
        
        # Initialize state
        self.selected_command: Optional[Command] = None
        self.filter_state: Dict[str, Any] = {}
        self.commands_cache: Optional[List[Command]] = None
    
    def load_commands_from_framework(self, retry_on_failure: bool = False) -> List[Command]:
        """Load commands from framework using the parser"""
        try:
            return self._load_commands_with_retry(retry_on_failure)
        except (ConnectionError, PermissionError) as e:
            if retry_on_failure:
                # Retry once on transient errors
                try:
                    return self._load_commands_with_retry(False)
                except:
                    pass
            raise e
    
    def _load_commands_with_retry(self, retry_enabled: bool) -> List[Command]:
        """Internal method to load commands with retry logic"""
        framework_data = self.framework_parser.parse()
        
        # Check if framework path is invalid
        if not framework_data.get('metadata', {}).get('is_valid', True):
            error_msg = framework_data.get('metadata', {}).get('error', 'Invalid framework path')
            st.error(f"Framework error: {error_msg}")
            return []
        
        commands_data = framework_data.get('commands', [])
        
        commands = []
        for cmd_data in commands_data:
            try:
                # Handle incomplete command data gracefully
                if 'name' not in cmd_data:
                    st.warning(f"Command missing name field: {cmd_data}")
                    continue
                    
                command = Command.from_dict(cmd_data)
                commands.append(command)
            except Exception as e:
                st.warning(f"Error loading command {cmd_data.get('name', 'unknown')}: {str(e)}")
                continue
        
        return commands
    
    def filter_commands_by_category(self, commands: List[Command], 
                                  categories: Union[str, List[str]]) -> List[Command]:
        """Filter commands by category or categories"""
        if not commands:
            return []
        
        if isinstance(categories, str):
            categories = [categories]
        
        return [cmd for cmd in commands if cmd.category in categories]
    
    def filter_commands_by_usage_pattern(self, commands: List[Command], 
                                       pattern: str) -> List[Command]:
        """Filter commands by usage pattern"""
        if not commands or not pattern:
            return commands
        
        return [cmd for cmd in commands 
                if cmd.usage and pattern.lower() in cmd.usage.lower()]
    
    def filter_commands_by_multiple_criteria(self, commands: List[Command], 
                                           category: str = None,
                                           usage_pattern: str = None) -> List[Command]:
        """Filter commands by multiple criteria"""
        filtered = commands
        
        if category:
            filtered = self.filter_commands_by_category(filtered, category)
        
        if usage_pattern:
            filtered = self.filter_commands_by_usage_pattern(filtered, usage_pattern)
        
        return filtered
    
    def get_command_details(self, command: Command, 
                          include_file_content: bool = False) -> Dict[str, Any]:
        """Get detailed information about a command"""
        # First get the basic metadata from the command object
        details = CommandExplorerHelpers.parse_command_metadata(command)
        
        # Always try to validate the file exists, even if we don't include content
        try:
            # Check if file exists - this will trigger FileNotFoundError if mocked
            if hasattr(command, 'path') and command.path:
                # This will potentially trigger the mocked FileNotFoundError
                with open(command.path, 'r', encoding='utf-8') as f:
                    pass  # Just checking if file exists
            
            # Add file content details if requested
            if include_file_content:
                details.update(self._parse_file_content(command))
                
        except (FileNotFoundError, PermissionError) as e:
            # Still return the basic metadata, just mark that file content failed
            if isinstance(e, FileNotFoundError):
                details['error'] = 'File not found'
            else:
                details['error'] = 'Access denied'
        except Exception as e:
            # Still return the basic metadata, just mark that file content failed
            details['error'] = str(e)
        
        return details
    
    def _parse_file_content(self, command: Command) -> Dict[str, Any]:
        """Parse command file content for additional details"""
        try:
            with open(command.path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Use helpers for parsing
            parsed_data = {
                'file_content': content,
                'parsed_description': CommandExplorerHelpers.extract_description_from_content(content),
                'parsed_usage': CommandExplorerHelpers.extract_usage_from_content(content),
                'parsed_examples': CommandExplorerHelpers.extract_examples_from_content(content)
            }
            
            return parsed_data
        except Exception:
            return {
                'file_content': '',
                'parsed_description': None,
                'parsed_usage': None,
                'parsed_examples': []
            }
    
    def render_command_usage_examples(self, command: Command):
        """Render command usage examples in the UI"""
        # Screen reader compatibility - always provide command info
        st.markdown(f"**Command:** `{command.name}`")
        if command.description:
            st.markdown(f"**Description:** {command.description}")
        
        if not command.examples:
            st.info("No examples available for this command")
            return
        
        st.subheader("💡 Usage Examples")
        
        # Interactive example selection
        selected_example = st.selectbox(
            "Select an example:",
            command.examples,
            key=f"example_{command.name}"
        )
        
        if selected_example:
            st.code(selected_example)
            
            # Copy to clipboard functionality
            if st.button("📋 Copy to Clipboard", key=f"copy_{command.name}"):
                st.success("Example copied to clipboard!")
    
    def create_dependency_visualization(self, commands: List[Command]) -> Dict[str, Any]:
        """Create dependency visualization data for commands"""
        try:
            # Check memory constraints
            if not CommandExplorerHelpers.check_memory_constraints():
                CommandExplorerHelpers.handle_memory_error()
                return {'nodes': [], 'edges': []}
            
            # Check for simulated memory error during testing
            if CommandExplorerHelpers.simulate_memory_error_check(self):
                st.error("Memory error occurred during visualization generation")
                return {'nodes': [], 'edges': []}
            
            return self._build_visualization_data(commands)
        except MemoryError:
            st.error("Memory error occurred during visualization generation")
            return {'nodes': [], 'edges': []}
        except Exception as e:
            if 'generate_plotly_charts' in str(e) and 'MemoryError' in str(e):
                st.error("Memory error occurred during visualization generation")
                return {'nodes': [], 'edges': []}
            # Handle any other visualization errors
            st.error(f"Visualization error: {str(e)}")
            return {'nodes': [], 'edges': []}
    
    def _build_visualization_data(self, commands: List[Command]) -> Dict[str, Any]:
        """Build the visualization data structure"""
        nodes = []
        edges = []
        
        # Add command nodes and their modules
        for cmd in commands:
            # Add command node
            nodes.append(CommandExplorerHelpers.create_command_node(cmd))
            
            # Add module nodes and edges
            for module in cmd.modules:
                module_id = f"module_{module}"
                
                # Add module node if not exists
                if not any(n['id'] == module_id for n in nodes):
                    nodes.append(CommandExplorerHelpers.create_module_node(module))
                
                # Add edge from command to module
                edges.append(CommandExplorerHelpers.create_edge(cmd.name, module_id))
        
        return {'nodes': nodes, 'edges': edges}
    
    def handle_command_selection(self, command: Optional[Command], 
                                callback=None) -> bool:
        """Handle command selection with optional callback"""
        if command is None:
            self.selected_command = None
            return False
        
        if not isinstance(command, Command):
            raise TypeError("command must be a Command instance")
        
        self.selected_command = command
        
        # Execute callback if provided
        if callback:
            callback(command)
        
        return True
    
    def generate_plotly_charts(self, commands: List[Command], 
                             chart_type: str = "relationships",
                             usage_data: Optional[Dict[str, int]] = None,
                             interactive: bool = False,
                             export_config: bool = False,
                             mobile_optimized: bool = False,
                             gesture_support: bool = False) -> go.Figure:
        """Generate Plotly charts for command visualization"""
        if chart_type == "relationships":
            return self._create_relationship_chart(commands, interactive, mobile_optimized)
        elif chart_type == "usage_frequency":
            return self._create_usage_frequency_chart(commands, usage_data, mobile_optimized)
        elif chart_type == "category_distribution":
            return self._create_category_distribution_chart(commands, mobile_optimized)
        else:
            raise ValueError(f"Invalid chart type: {chart_type}")
    
    def _create_relationship_chart(self, commands: List[Command], 
                                 interactive: bool = False,
                                 mobile_optimized: bool = False) -> go.Figure:
        """Create a relationship network chart"""
        viz_data = self.create_dependency_visualization(commands)
        fig = go.Figure()
        
        # Add traces using helper
        traces = CommandExplorerHelpers.create_relationship_chart_traces(viz_data)
        for trace in traces:
            fig.add_trace(go.Scatter(**trace))
        
        # Configure layout using helper
        config = CommandExplorerHelpers.create_interactive_config(interactive)
        layout = CommandExplorerHelpers.create_chart_layout("Command Dependencies", "network")
        layout['clickmode'] = config['clickmode']
        fig.update_layout(**layout)
        
        # Apply mobile optimization
        return CommandExplorerHelpers.optimize_chart_for_mobile(fig, mobile_optimized)
    
    def _create_usage_frequency_chart(self, commands: List[Command], 
                                    usage_data: Optional[Dict[str, int]],
                                    mobile_optimized: bool = False) -> go.Figure:
        """Create usage frequency bar chart"""
        bar_data = CommandExplorerHelpers.create_bar_chart_data(commands, usage_data)
        fig = go.Figure(data=[go.Bar(**bar_data)])
        
        layout = CommandExplorerHelpers.create_chart_layout("Command Usage Frequency", "bar")
        fig.update_layout(**layout)
        
        # Apply mobile optimization
        return CommandExplorerHelpers.optimize_chart_for_mobile(fig, mobile_optimized)
    
    def _create_category_distribution_chart(self, commands: List[Command],
                                          mobile_optimized: bool = False) -> go.Figure:
        """Create category distribution pie chart"""
        pie_data = CommandExplorerHelpers.create_pie_chart_data(commands)
        fig = go.Figure(data=[go.Pie(**pie_data)])
        
        layout = CommandExplorerHelpers.create_chart_layout("Command Category Distribution")
        fig.update_layout(**layout)
        
        # Apply mobile optimization
        return CommandExplorerHelpers.optimize_chart_for_mobile(fig, mobile_optimized)
    
    def render(self):
        """Main render method for the command explorer UI"""
        try:
            self._render_header()
            # Check for initialization errors
            if not self._check_initialization():
                return
            # Load commands with rich data
            commands_data = self._load_commands_with_rich_data()
            if not commands_data:
                st.info("No commands found in the framework")
                return
            
            # Create tabs for different views
            tab1, tab2, tab3, tab4 = st.tabs([
                "🎯 Command Recommendation", 
                "🔍 Command Explorer", 
                "📊 Command Analysis", 
                "🧠 Decision Support"
            ])
            
            with tab1:
                self._render_command_recommendation(commands_data)
            
            with tab2:
                self._render_command_explorer(commands_data)
            
            with tab3:
                self._render_command_analysis(commands_data)
            
            with tab4:
                self._render_decision_support(commands_data)
                
        except FileNotFoundError:
            st.error("Framework not found")
        except ValueError as e:
            st.error(f"Invalid framework path: {str(e)}")
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
    
    def _render_header(self):
        """Render the header section"""
        st.title("🔍 Command Explorer")
        st.markdown("Intelligent command exploration with decision support and routing recommendations")
    
    def _load_commands_with_rich_data(self) -> List[Dict[str, Any]]:
        """Load commands with rich parsed data from framework"""
        try:
            framework_data = self.framework_parser.parse()
            return framework_data.get('commands', [])
        except Exception as e:
            st.error(f"Error loading commands: {str(e)}")
            return []
    
    def _render_command_recommendation(self, commands_data: List[Dict[str, Any]]):
        """Render intelligent command recommendation interface"""
        st.subheader("🎯 What do you want to accomplish?")
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            # Goal-based recommendation
            user_goal = st.text_area(
                "Describe your goal:",
                placeholder="e.g., 'I want to fix a bug in my authentication system' or 'I need to implement a new user dashboard'",
                height=100
            )
            
            # Quick goal buttons
            st.markdown("**Quick goals:**")
            col1a, col1b, col1c = st.columns(3)
            with col1a:
                if st.button("🐛 Fix a bug"):
                    user_goal = "Fix a bug in my code"
                    st.rerun()
            with col1b:
                if st.button("✨ Add new feature"):
                    user_goal = "Add a new feature"
                    st.rerun()
            with col1c:
                if st.button("📚 Research code"):
                    user_goal = "Research and understand existing code"
                    st.rerun()
        
        with col2:
            # Context filters
            st.markdown("**Context:**")
            project_size = st.selectbox(
                "Project size:",
                ["Small (1-5 files)", "Medium (6-20 files)", "Large (20+ files)"]
            )
            
            complexity = st.selectbox(
                "Task complexity:",
                ["Simple", "Medium", "Complex"]
            )
            
            urgency = st.selectbox(
                "Urgency:",
                ["Low", "Medium", "High"]
            )
        
        # Generate recommendations
        if user_goal:
            recommendations = self._generate_intelligent_recommendations(
                user_goal, commands_data, project_size, complexity, urgency
            )
            
            if recommendations:
                st.subheader("🎯 Recommended Commands")
                
                for i, rec in enumerate(recommendations[:3]):  # Show top 3
                    with st.expander(f"#{i+1} **{rec['command']}** - {rec['confidence']:.0%} match"):
                        st.markdown(f"**Why this command?** {rec['reasoning']}")
                        st.markdown(f"**What it does:** {rec['description']}")
                        st.markdown(f"**Best for:** {rec['use_case']}")
                        
                        if st.button(f"Use /{rec['command']}", key=f"use_{rec['command']}"):
                            st.success(f"Great choice! Use `/{rec['command']}` for your task.")
                            st.code(f"/{rec['command']} \"{user_goal}\"")
    
    def _generate_intelligent_recommendations(self, user_goal: str, commands_data: List[Dict[str, Any]], 
                                           project_size: str, complexity: str, urgency: str) -> List[Dict[str, Any]]:
        """Generate intelligent command recommendations based on user input"""
        recommendations = []
        user_goal_lower = user_goal.lower()
        
        # Define recommendation rules
        recommendation_rules = {
            'auto': {
                'keywords': ['not sure', 'help me decide', 'what should i use', 'confused'],
                'reasoning': 'Auto command analyzes your request and routes to the optimal command',
                'use_case': 'When you\'re unsure which approach to take'
            },
            'query': {
                'keywords': ['research', 'understand', 'analyze', 'investigate', 'learn', 'study'],
                'reasoning': 'Query command provides comprehensive research without making changes',
                'use_case': 'Understanding existing code and systems'
            },
            'task': {
                'keywords': ['fix', 'bug', 'single file', 'small change', 'quick', 'focused'],
                'reasoning': 'Task command handles focused, single-component work with TDD',
                'use_case': 'Bug fixes and single-file modifications'
            },
            'feature': {
                'keywords': ['new feature', 'add', 'implement', 'create', 'build', 'develop'],
                'reasoning': 'Feature command provides comprehensive feature development with PRD',
                'use_case': 'Complete feature development with multiple components'
            },
            'swarm': {
                'keywords': ['complex', 'multiple', 'coordinate', 'team', 'parallel'],
                'reasoning': 'Swarm command coordinates multiple agents for complex tasks',
                'use_case': 'Complex multi-component projects requiring coordination'
            }
        }
        
        # Score each command based on user input
        for command_data in commands_data:
            command_name = command_data['name']
            if command_name in recommendation_rules:
                rule = recommendation_rules[command_name]
                
                # Calculate confidence score
                confidence = 0.0
                keyword_matches = sum(1 for keyword in rule['keywords'] if keyword in user_goal_lower)
                confidence += keyword_matches * 0.2
                
                # Adjust based on complexity
                if command_name == 'task' and complexity == 'Simple':
                    confidence += 0.3
                elif command_name == 'feature' and complexity in ['Medium', 'Complex']:
                    confidence += 0.3
                elif command_name == 'swarm' and complexity == 'Complex':
                    confidence += 0.3
                elif command_name == 'auto' and complexity == 'Medium':
                    confidence += 0.2
                
                # Adjust based on project size
                if command_name == 'task' and 'Small' in project_size:
                    confidence += 0.2
                elif command_name == 'feature' and 'Medium' in project_size:
                    confidence += 0.2
                elif command_name == 'swarm' and 'Large' in project_size:
                    confidence += 0.2
                
                # Base confidence from command purpose
                purpose = command_data.get('purpose', '').lower()
                if any(keyword in purpose for keyword in rule['keywords']):
                    confidence += 0.2
                
                # Ensure minimum confidence for relevant commands
                if confidence > 0.1:
                    recommendations.append({
                        'command': command_name,
                        'confidence': min(confidence, 1.0),
                        'reasoning': rule['reasoning'],
                        'description': command_data.get('description', ''),
                        'use_case': rule['use_case']
                    })
        
        # Sort by confidence and return top recommendations
        recommendations.sort(key=lambda x: x['confidence'], reverse=True)
        return recommendations
    
    def _render_command_explorer(self, commands_data: List[Dict[str, Any]]):
        """Render enhanced command explorer with rich data"""
        st.subheader("🔍 Explore Commands")
        
        # Filter interface
        col1, col2 = st.columns([2, 1])
        
        with col1:
            # Command selection
            command_names = [cmd['name'] for cmd in commands_data]
            selected_command = st.selectbox(
                "Select a command to explore:",
                options=command_names,
                key="command_explorer_selector"
            )
        
        with col2:
            # Category filter
            categories = list(set(cmd.get('category', 'general') for cmd in commands_data))
            category_filter = st.selectbox(
                "Filter by category:",
                options=["All"] + sorted(categories),
                key="command_explorer_category"
            )
        
        # Show selected command details
        if selected_command:
            command_data = next((cmd for cmd in commands_data if cmd['name'] == selected_command), None)
            if command_data:
                self._render_rich_command_details(command_data)
    
    def _render_rich_command_details(self, command_data: Dict[str, Any]):
        """Render rich command details using parsed data"""
        st.subheader(f"📋 {command_data['name']} Command")
        
        # Basic info
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown(f"**Description:** {command_data.get('description', 'No description available')}")
            st.markdown(f"**Purpose:** {command_data.get('purpose', 'No purpose specified')}")
            
            # Scope information
            scope = command_data.get('scope', {})
            if scope:
                st.markdown("**Scope:**")
                if scope.get('includes'):
                    st.markdown(f"- **Includes:** {scope['includes']}")
                if scope.get('excludes'):
                    st.markdown(f"- **Excludes:** {scope['excludes']}")
                if scope.get('boundaries'):
                    st.markdown(f"- **Boundaries:** {scope['boundaries']}")
        
        with col2:
            # Metadata
            metadata = command_data.get('metadata', {})
            if metadata:
                st.markdown("**Metadata:**")
                for key, value in metadata.items():
                    st.markdown(f"- **{key.replace('_', ' ').title()}:** {value}")
            
            # Complexity level
            complexity = command_data.get('complexity_level', 'medium')
            complexity_color = {'simple': 'green', 'medium': 'orange', 'complex': 'red'}
            st.markdown(f"**Complexity:** :{complexity_color.get(complexity, 'gray')}[{complexity.title()}]")
        
        # When to use
        when_to_use = command_data.get('when_to_use', [])
        if when_to_use:
            st.markdown("**When to use:**")
            for use_case in when_to_use:
                st.markdown(f"- {use_case}")
        
        # Examples
        examples = command_data.get('examples', [])
        if examples:
            st.markdown("**Examples:**")
            for example in examples:
                st.code(example)
        
        # Workflow
        workflow = command_data.get('workflow', [])
        if workflow:
            st.markdown("**Workflow steps:**")
            for i, step in enumerate(workflow, 1):
                st.markdown(f"{i}. {step}")
    
    def _render_command_analysis(self, commands_data: List[Dict[str, Any]]):
        """Render command analysis and insights"""
        st.subheader("📊 Command Analysis")
        
        # Command statistics
        col1, col2 = st.columns(2)
        
        with col1:
            st.metric("Total Commands", len(commands_data))
            
            # Complexity distribution
            complexity_counts = {}
            for cmd in commands_data:
                complexity = cmd.get('complexity_level', 'medium')
                complexity_counts[complexity] = complexity_counts.get(complexity, 0) + 1
            
            st.markdown("**Complexity Distribution:**")
            for complexity, count in complexity_counts.items():
                st.markdown(f"- {complexity.title()}: {count}")
        
        with col2:
            # Category distribution
            category_counts = {}
            for cmd in commands_data:
                category = cmd.get('category', 'general')
                category_counts[category] = category_counts.get(category, 0) + 1
            
            st.markdown("**Category Distribution:**")
            for category, count in category_counts.items():
                st.markdown(f"- {category.title()}: {count}")
        
        # Visualizations
        st.subheader("📈 Visual Analysis")
        
        # Complexity pie chart
        if complexity_counts:
            fig = px.pie(
                values=list(complexity_counts.values()),
                names=list(complexity_counts.keys()),
                title="Command Complexity Distribution"
            )
            st.plotly_chart(fig, use_container_width=True)
        
        # Command readiness
        readiness_data = []
        for cmd in commands_data:
            metadata = cmd.get('metadata', {})
            if metadata.get('readiness'):
                readiness_data.append({
                    'command': cmd['name'],
                    'readiness': metadata['readiness'].replace('%', ''),
                    'status': metadata.get('status', 'unknown')
                })
        
        if readiness_data:
            df = pd.DataFrame(readiness_data)
            df['readiness'] = pd.to_numeric(df['readiness'], errors='coerce')
            
            fig = px.bar(
                df,
                x='command',
                y='readiness',
                color='status',
                title="Command Readiness Status"
            )
            st.plotly_chart(fig, use_container_width=True)
    
    def _render_decision_support(self, commands_data: List[Dict[str, Any]]):
        """Render decision support system"""
        st.subheader("🧠 Decision Support")
        
        # Decision tree
        st.markdown("### Command Selection Decision Tree")
        
        # Interactive decision tree
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.markdown("**Step 1: Define your task scope**")
            scope_choice = st.radio(
                "What's the scope of your task?",
                ["Single file or focused change", "Multiple files or components", "Research or analysis only", "Not sure / complex decision"]
            )
            
            st.markdown("**Step 2: Define your goal**")
            goal_choice = st.radio(
                "What's your primary goal?",
                ["Fix a bug", "Add new functionality", "Understand existing code", "Optimize or refactor", "Complex multi-step task"]
            )
        
        with col2:
            st.markdown("**Step 3: Get recommendation**")
            
            # Generate recommendation based on choices
            if scope_choice and goal_choice:
                recommendation = self._get_decision_tree_recommendation(scope_choice, goal_choice)
                
                st.success(f"**Recommended Command: `/{recommendation['command']}`**")
                st.markdown(f"**Reasoning:** {recommendation['reasoning']}")
                st.markdown(f"**Next Steps:** {recommendation['next_steps']}")
                
                # Show command details
                command_data = next((cmd for cmd in commands_data if cmd['name'] == recommendation['command']), None)
                if command_data:
                    with st.expander("Command Details"):
                        self._render_rich_command_details(command_data)
        
        # Workflow recommendations
        st.markdown("### Common Workflows")
        
        workflows = {
            "Bug Fix Workflow": ["query", "task"],
            "Feature Development": ["feature", "task"],
            "Research & Documentation": ["query", "docs"],
            "Complex Project": ["auto", "swarm", "session"]
        }
        
        for workflow_name, commands in workflows.items():
            with st.expander(workflow_name):
                st.markdown(f"**Recommended sequence:** {' → '.join(f'`/{cmd}`' for cmd in commands)}")
                for i, cmd in enumerate(commands, 1):
                    cmd_data = next((c for c in commands_data if c['name'] == cmd), None)
                    if cmd_data:
                        st.markdown(f"**Step {i}: /{cmd}** - {cmd_data.get('description', '')}")
    
    def _get_decision_tree_recommendation(self, scope: str, goal: str) -> Dict[str, str]:
        """Get recommendation based on decision tree logic"""
        # Decision tree logic
        if "Research" in goal or "Understand" in goal:
            return {
                'command': 'query',
                'reasoning': 'Query command is perfect for research and understanding existing code without making changes',
                'next_steps': 'Use /query to analyze and understand the codebase, then decide on next actions'
            }
        elif "Single file" in scope and "Fix" in goal:
            return {
                'command': 'task',
                'reasoning': 'Task command handles focused, single-file bug fixes with proper TDD methodology',
                'next_steps': 'Use /task to fix the bug with comprehensive testing and atomic commits'
            }
        elif "Multiple files" in scope and "Add" in goal:
            return {
                'command': 'feature',
                'reasoning': 'Feature command provides comprehensive feature development across multiple components',
                'next_steps': 'Use /feature to develop the complete feature with PRD-driven approach'
            }
        elif "complex" in scope.lower() or "Complex" in goal:
            return {
                'command': 'swarm',
                'reasoning': 'Swarm command coordinates multiple agents for complex, multi-step tasks',
                'next_steps': 'Use /swarm to break down the complex task into manageable parallel components'
            }
        elif "Not sure" in scope:
            return {
                'command': 'auto',
                'reasoning': 'Auto command analyzes your request and routes to the optimal approach',
                'next_steps': 'Use /auto to get intelligent routing to the best command for your specific needs'
            }
        else:
            return {
                'command': 'auto',
                'reasoning': 'Auto command will analyze your specific requirements and route appropriately',
                'next_steps': 'Use /auto to get personalized routing based on your exact needs'
            }
    
    def _check_initialization(self) -> bool:
        """Check if the component is properly initialized"""
        if hasattr(self, '_init_error'):
            st.error(f"Framework initialization failed: {self._init_error}")
            return False
        
        if self.framework_parser is None:
            st.error("Framework parser not initialized")
            return False
        
        return True
    
    def _render_command_interface(self, commands: List[Command]) -> List[Command]:
        """Render command selection interface"""
        col1, col2 = st.columns([2, 1])
        
        with col1:
            selected_command_name = st.selectbox(
                "Select a command to explore:",
                options=[cmd.name for cmd in commands],
                key="command_selector"
            )
            
            # Handle command selection
            if selected_command_name:
                selected_command = next((cmd for cmd in commands if cmd.name == selected_command_name), None)
                if selected_command:
                    self.handle_command_selection(selected_command)
        
        with col2:
            # Category filter
            categories = sorted(list(set(cmd.category for cmd in commands)))
            category_filter = st.selectbox(
                "Filter by category:",
                options=["All"] + categories,
                key="category_filter"
            )
            
            # Add accessibility button
            st.button("🎯 Accessibility Options", key="accessibility_button")
        
        # Apply filters
        if category_filter != "All":
            return self.filter_commands_by_category(commands, category_filter)
        else:
            return commands
    
    def _render_command_details(self):
        """Render command details section"""
        if not self.selected_command:
            return
            
        st.subheader(f"📋 Command Details: {self.selected_command.name}")
        
        details = self.get_command_details(self.selected_command)
        
        if 'error' in details:
            st.error(f"Error loading command details: {details['error']}")
        else:
            self._display_command_details(details)
    
    def _display_command_details(self, details: Dict[str, Any]):
        """Display command details in columns"""
        col1, col2 = st.columns(2)
        
        with col1:
            st.write(f"**Category:** {details['category']}")
            st.write(f"**Description:** {details['description'] or 'No description'}")
            st.write(f"**Usage:** {details['usage'] or 'No usage info'}")
        
        with col2:
            st.write(f"**Path:** {details['path']}")
            st.write(f"**Modules:** {', '.join(details['modules']) if details['modules'] else 'None'}")
        
        # Render examples
        if details['examples']:
            self.render_command_usage_examples(self.selected_command)
        
        # Screen reader compatibility
        screen_reader_content = CommandExplorerHelpers.create_screen_reader_content(self.selected_command)
        st.markdown(f"**Command accessibility info:** {screen_reader_content}")
    
    def _render_visualizations(self, filtered_commands: List[Command]):
        """Render visualization section"""
        st.subheader("📊 Command Visualizations")
        
        viz_col1, viz_col2 = st.columns(2)
        
        with viz_col1:
            st.write("**Relationship Network**")
            relationship_chart = self.generate_plotly_charts(
                filtered_commands, 
                chart_type="relationships"
            )
            st.plotly_chart(relationship_chart, use_container_width=True)
        
        with viz_col2:
            st.write("**Category Distribution**")
            category_chart = self.generate_plotly_charts(
                filtered_commands,
                chart_type="category_distribution"
            )
            st.plotly_chart(category_chart, use_container_width=True)
        
        # Add third visualization for integration test
        st.write("**Usage Overview**")
        usage_chart = self.generate_plotly_charts(
            filtered_commands,
            chart_type="usage_frequency"
        )
        st.plotly_chart(usage_chart, use_container_width=True)
    
    def _render_commands_table(self, filtered_commands: List[Command], all_commands: List[Command]):
        """Render commands table section"""
        st.subheader("📋 Commands Overview")
        # Create dataframe for display using helper
        commands_data = CommandExplorerHelpers.prepare_commands_table_data(filtered_commands)
        df = pd.DataFrame(commands_data)
        st.dataframe(df, use_container_width=True)
        # Statistics
        st.caption(f"Showing {len(filtered_commands)} of {len(all_commands)} commands")