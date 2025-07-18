"""
Unified Template Manager Component for Claude Code Modular Prompts Framework
Provides centralized template management with validation, categorization, and sharing capabilities
"""

import streamlit as st
import json
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass, field, asdict
from datetime import datetime
import re
import shutil
from enum import Enum
import uuid
from components.url_sharing import URLSharingManager


class TemplateCategory(Enum):
    """Template categories for organization"""
    
    DEVELOPMENT = "development"
    RESEARCH = "research"
    ANALYSIS = "analysis"
    DOCUMENTATION = "documentation"
    TESTING = "testing"
    CUSTOM = "custom"
    
    @classmethod
    def is_valid(cls, category: str) -> bool:
        """Check if category is valid"""
        if not category:
            return False
        return category in [c.value for c in cls]
    
    @classmethod
    def get_all_categories(cls) -> List[str]:
        """Get all available categories"""
        return [c.value for c in cls]


@dataclass
class Template:
    """Represents a unified template that works across all components"""
    
    id: str
    name: str
    description: str
    category: str
    author: str
    version: str
    components: List[Dict[str, Any]] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    
    def __post_init__(self):
        """Validate template data after initialization"""
        if not self.id or self.id.strip() == "":
            raise ValueError("Template ID cannot be empty")
        
        if not self.name or self.name.strip() == "":
            raise ValueError("Template name cannot be empty")
        
        if not TemplateCategory.is_valid(self.category):
            raise ValueError(f"Invalid template category: {self.category}")
        
        if not self.author or self.author.strip() == "":
            raise ValueError("Template author cannot be empty")
        
        if not self.version or self.version.strip() == "":
            raise ValueError("Template version cannot be empty")
        
        # Set timestamps if not provided
        if not self.created_at:
            self.created_at = datetime.now().isoformat()
        
        if not self.updated_at:
            self.updated_at = datetime.now().isoformat()
        
        # Ensure metadata has required fields
        if 'framework_version' not in self.metadata:
            self.metadata['framework_version'] = '3.0.0'
        
        if 'tags' not in self.metadata:
            self.metadata['tags'] = []
        
        if 'difficulty' not in self.metadata:
            self.metadata['difficulty'] = 'intermediate'
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert template to dictionary for serialization"""
        return asdict(self)
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Template':
        """Create template from dictionary"""
        return cls(**data)
    
    def update_timestamp(self):
        """Update the updated_at timestamp"""
        self.updated_at = datetime.now().isoformat()
    
    def add_component(self, component: Dict[str, Any]):
        """Add a component to the template"""
        if component not in self.components:
            self.components.append(component)
            self.update_timestamp()
    
    def remove_component(self, component_id: str):
        """Remove a component from the template"""
        self.components = [c for c in self.components if c.get('id') != component_id]
        self.update_timestamp()
    
    def get_component_count(self) -> int:
        """Get the number of components in the template"""
        return len(self.components)
    
    def get_tags(self) -> List[str]:
        """Get template tags"""
        return self.metadata.get('tags', [])
    
    def add_tag(self, tag: str):
        """Add a tag to the template"""
        if 'tags' not in self.metadata:
            self.metadata['tags'] = []
        
        if tag not in self.metadata['tags']:
            self.metadata['tags'].append(tag)
            self.update_timestamp()
    
    def remove_tag(self, tag: str):
        """Remove a tag from the template"""
        if 'tags' in self.metadata and tag in self.metadata['tags']:
            self.metadata['tags'].remove(tag)
            self.update_timestamp()


class TemplateValidator:
    """Validates templates against the framework and ensures compatibility"""
    
    def __init__(self, framework_path: Path):
        """Initialize template validator"""
        self.framework_path = framework_path
        self.current_framework_version = "3.0.0"
    
    def validate_template_components(self, template_data: Dict[str, Any]) -> Tuple[bool, List[str]]:
        """Validate that all template components exist in the framework"""
        errors = []
        
        components = template_data.get('components', [])
        
        for component in components:
            component_file = component.get('file', '')
            if not component_file:
                errors.append(f"Component missing file path: {component}")
                continue
            
            component_path = self.framework_path / component_file
            if not component_path.exists():
                errors.append(f"Component file not found: {component_file}")
        
        return len(errors) == 0, errors
    
    def validate_framework_version(self, template_version: str) -> bool:
        """Validate that template version is compatible with current framework"""
        if not template_version:
            return False
        
        try:
            # Simple version comparison - template version should be compatible
            template_major = int(template_version.split('.')[0])
            current_major = int(self.current_framework_version.split('.')[0])
            
            # Allow same major version
            return template_major == current_major
        except (ValueError, IndexError):
            return False
    
    def resolve_template_dependencies(self, template_data: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Resolve and add implicit dependencies for template components"""
        resolved_deps = []
        components = template_data.get('components', [])
        
        # Track existing components to avoid duplicates
        existing_components = set()
        for component in components:
            component_key = f"{component.get('type', '')}_{component.get('name', '')}"
            existing_components.add(component_key)
        
        for component in components:
            component_type = component.get('type', '')
            component_name = component.get('name', '')
            
            # Add implicit dependencies based on component type
            if component_type == 'command':
                # Commands typically need quality gates
                quality_gates_key = "system_universal-quality-gates"
                if quality_gates_key not in existing_components:
                    resolved_deps.append({
                        'type': 'system',
                        'name': 'universal-quality-gates',
                        'file': 'system/quality/universal-quality-gates.md',
                        'implicit': True
                    })
                    existing_components.add(quality_gates_key)
                
                # Task and feature commands often use TDD patterns
                if component_name in ['task', 'feature']:
                    tdd_key = "module_tdd-cycle-pattern"
                    if tdd_key not in existing_components:
                        resolved_deps.append({
                            'type': 'module',
                            'name': 'tdd-cycle-pattern',
                            'file': 'modules/patterns/tdd-cycle-pattern.md',
                            'implicit': True
                        })
                        existing_components.add(tdd_key)
        
        return resolved_deps
    
    def validate_template(self, template_data: Dict[str, Any]) -> Tuple[bool, List[str]]:
        """Comprehensive template validation"""
        errors = []
        
        # Validate required fields
        required_fields = ['id', 'name', 'description', 'category', 'author', 'version']
        for field in required_fields:
            if not template_data.get(field):
                errors.append(f"Missing required field: {field}")
        
        # Validate category
        category = template_data.get('category', '')
        if category and not TemplateCategory.is_valid(category):
            errors.append(f"Invalid category: {category}")
        
        # Validate framework version
        framework_version = template_data.get('metadata', {}).get('framework_version', '')
        if framework_version and not self.validate_framework_version(framework_version):
            errors.append(f"Incompatible framework version: {framework_version}")
        
        # Validate components
        components_valid, component_errors = self.validate_template_components(template_data)
        if not components_valid:
            errors.extend(component_errors)
        
        return len(errors) == 0, errors


class TemplateManager:
    """Unified template manager for all framework components"""
    
    def __init__(self, template_storage_path: Path, framework_path: Path):
        """Initialize template manager"""
        self.template_storage_path = template_storage_path
        self.framework_path = framework_path
        self.validator = TemplateValidator(framework_path)
        
        # Ensure storage directory exists
        self.template_storage_path.mkdir(parents=True, exist_ok=True)
        
        # Initialize URL sharing manager
        sharing_storage_path = self.template_storage_path / "sharing"
        self.url_sharing_manager = URLSharingManager(sharing_storage_path)
        
        # Initialize metadata index
        self.metadata_index = {}
        self._rebuild_metadata_index()
    
    def _rebuild_metadata_index(self):
        """Rebuild the metadata index from all template files"""
        self.metadata_index = {}
        
        for template_file in self.template_storage_path.glob("*.json"):
            try:
                with open(template_file, 'r') as f:
                    template_data = json.load(f)
                
                template_id = template_data.get('id', '')
                if template_id:
                    # Store metadata without components for faster access
                    metadata = template_data.copy()
                    metadata.pop('components', None)
                    self.metadata_index[template_id] = metadata
            except Exception:
                # Skip corrupted files
                continue
    
    def _get_template_file_path(self, template_id: str) -> Path:
        """Get the file path for a template"""
        return self.template_storage_path / f"{template_id}.json"
    
    def save_template(self, template_data: Dict[str, Any]) -> bool:
        """Save a template to storage"""
        try:
            # Validate template before saving
            is_valid, errors = self.validator.validate_template(template_data)
            if not is_valid:
                st.error(f"Template validation failed: {', '.join(errors)}")
                return False
            
            # Create Template object to ensure proper structure
            template = Template(**template_data)
            
            # Save to file
            template_file = self._get_template_file_path(template.id)
            with open(template_file, 'w') as f:
                json.dump(template.to_dict(), f, indent=2)
            
            # Update metadata index
            metadata = template.to_dict()
            metadata.pop('components', None)
            self.metadata_index[template.id] = metadata
            
            return True
        except Exception as e:
            st.error(f"Error saving template: {str(e)}")
            return False
    
    def load_template(self, template_id: str) -> Optional[Dict[str, Any]]:
        """Load a template from storage"""
        try:
            template_file = self._get_template_file_path(template_id)
            if not template_file.exists():
                return None
            
            with open(template_file, 'r') as f:
                template_data = json.load(f)
            
            return template_data
        except Exception as e:
            st.error(f"Error loading template: {str(e)}")
            return None
    
    def list_templates(self) -> List[Dict[str, Any]]:
        """List all templates with metadata"""
        return list(self.metadata_index.values())
    
    def search_templates(self, 
                        category: Optional[str] = None,
                        tags: Optional[List[str]] = None,
                        name_contains: Optional[str] = None,
                        author: Optional[str] = None) -> List[Dict[str, Any]]:
        """Search templates based on criteria"""
        results = []
        
        for template_metadata in self.metadata_index.values():
            matches = True
            
            # Filter by category
            if category and template_metadata.get('category') != category:
                matches = False
            
            # Filter by tags
            if tags and matches:
                template_tags = template_metadata.get('metadata', {}).get('tags', [])
                if not any(tag in template_tags for tag in tags):
                    matches = False
            
            # Filter by name
            if name_contains and matches:
                template_name = template_metadata.get('name', '').lower()
                if name_contains.lower() not in template_name:
                    matches = False
            
            # Filter by author
            if author and matches:
                template_author = template_metadata.get('author', '').lower()
                if author.lower() not in template_author:
                    matches = False
            
            if matches:
                results.append(template_metadata)
        
        return results
    
    def delete_template(self, template_id: str) -> bool:
        """Delete a template"""
        try:
            template_file = self._get_template_file_path(template_id)
            if template_file.exists():
                template_file.unlink()
            
            # Remove from metadata index
            if template_id in self.metadata_index:
                del self.metadata_index[template_id]
            
            return True
        except Exception as e:
            st.error(f"Error deleting template: {str(e)}")
            return False
    
    def validate_template(self, template_data: Dict[str, Any]) -> Tuple[bool, List[str]]:
        """Validate a template"""
        return self.validator.validate_template(template_data)
    
    def get_template_categories(self) -> List[str]:
        """Get all available template categories"""
        return TemplateCategory.get_all_categories()
    
    def export_template(self, template_id: str, export_path: Path) -> bool:
        """Export a template to a file"""
        try:
            template_data = self.load_template(template_id)
            if not template_data:
                st.error(f"Template not found: {template_id}")
                return False
            
            # Add export metadata
            export_data = template_data.copy()
            export_data['export_info'] = {
                'exported_at': datetime.now().isoformat(),
                'framework_version': '3.0.0'
            }
            
            with open(export_path, 'w') as f:
                json.dump(export_data, f, indent=2)
            
            return True
        except Exception as e:
            st.error(f"Error exporting template: {str(e)}")
            return False
    
    def import_template(self, import_path: Path) -> bool:
        """Import a template from a file"""
        try:
            with open(import_path, 'r') as f:
                template_data = json.load(f)
            
            # Remove export metadata if present
            template_data.pop('export_info', None)
            
            # Validate before importing
            is_valid, errors = self.validator.validate_template(template_data)
            if not is_valid:
                st.error(f"Template validation failed: {', '.join(errors)}")
                return False
            
            # Check if template already exists
            template_id = template_data.get('id', '')
            if template_id in self.metadata_index:
                st.warning(f"Template {template_id} already exists. Overwriting...")
            
            return self.save_template(template_data)
        except Exception as e:
            st.error(f"Error importing template: {str(e)}")
            return False
    
    def get_template_metadata(self, template_id: str) -> Optional[Dict[str, Any]]:
        """Get template metadata without loading full template"""
        return self.metadata_index.get(template_id)
    
    def duplicate_template(self, source_id: str, new_id: str, new_name: str) -> bool:
        """Duplicate a template with new ID and name"""
        try:
            source_template = self.load_template(source_id)
            if not source_template:
                st.error(f"Source template not found: {source_id}")
                return False
            
            # Create duplicate with new ID and name
            duplicate_template = source_template.copy()
            duplicate_template['id'] = new_id
            duplicate_template['name'] = new_name
            duplicate_template['created_at'] = datetime.now().isoformat()
            duplicate_template['updated_at'] = datetime.now().isoformat()
            
            return self.save_template(duplicate_template)
        except Exception as e:
            st.error(f"Error duplicating template: {str(e)}")
            return False
    
    def get_templates_by_category(self, category: str) -> List[Dict[str, Any]]:
        """Get all templates in a specific category"""
        return self.search_templates(category=category)
    
    def get_template_usage_stats(self) -> Dict[str, Any]:
        """Get usage statistics for templates"""
        stats = {
            'total_templates': len(self.metadata_index),
            'categories': {},
            'tags': {},
            'authors': {}
        }
        
        for template_metadata in self.metadata_index.values():
            # Count by category
            category = template_metadata.get('category', 'unknown')
            stats['categories'][category] = stats['categories'].get(category, 0) + 1
            
            # Count by tags
            tags = template_metadata.get('metadata', {}).get('tags', [])
            for tag in tags:
                stats['tags'][tag] = stats['tags'].get(tag, 0) + 1
            
            # Count by author
            author = template_metadata.get('author', 'unknown')
            stats['authors'][author] = stats['authors'].get(author, 0) + 1
        
        return stats
    
    def render_template_gallery_ui(self):
        """Render the template gallery user interface"""
        st.title("📚 Template Gallery")
        
        # Template statistics
        stats = self.get_template_usage_stats()
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Total Templates", stats['total_templates'])
        with col2:
            st.metric("Categories", len(stats['categories']))
        with col3:
            st.metric("Unique Tags", len(stats['tags']))
        with col4:
            st.metric("Authors", len(stats['authors']))
        
        # Search and filter interface
        st.subheader("🔍 Search & Filter")
        
        col1, col2 = st.columns(2)
        
        with col1:
            search_name = st.text_input("Search by name", placeholder="Enter template name...")
            selected_category = st.selectbox(
                "Filter by category",
                options=["All"] + self.get_template_categories(),
                index=0
            )
        
        with col2:
            search_author = st.text_input("Search by author", placeholder="Enter author name...")
            available_tags = list(stats['tags'].keys())
            selected_tags = st.multiselect("Filter by tags", options=available_tags)
        
        # Search templates
        search_category = selected_category if selected_category != "All" else None
        search_tags = selected_tags if selected_tags else None
        search_name_filter = search_name if search_name else None
        search_author_filter = search_author if search_author else None
        
        templates = self.search_templates(
            category=search_category,
            tags=search_tags,
            name_contains=search_name_filter,
            author=search_author_filter
        )
        
        # Display templates
        st.subheader(f"📖 Templates ({len(templates)} found)")
        
        if not templates:
            st.info("No templates found matching your criteria.")
            return
        
        # Display templates in a grid
        for i in range(0, len(templates), 2):
            cols = st.columns(2)
            
            for j, col in enumerate(cols):
                if i + j < len(templates):
                    template = templates[i + j]
                    
                    with col:
                        with st.container():
                            st.markdown(f"**{template['name']}**")
                            st.markdown(f"*{template['description']}*")
                            st.markdown(f"**Category:** {template['category']}")
                            st.markdown(f"**Author:** {template['author']}")
                            st.markdown(f"**Version:** {template['version']}")
                            
                            # Show tags
                            tags = template.get('metadata', {}).get('tags', [])
                            if tags:
                                tag_str = " ".join([f"`{tag}`" for tag in tags])
                                st.markdown(f"**Tags:** {tag_str}")
                            
                            # Action buttons
                            col1, col2, col3 = st.columns(3)
                            
                            with col1:
                                if st.button("📄 View", key=f"view_{template['id']}"):
                                    st.session_state[f"view_template_{template['id']}"] = True
                            
                            with col2:
                                if st.button("📋 Use", key=f"use_{template['id']}"):
                                    st.session_state[f"use_template_{template['id']}"] = True
                            
                            with col3:
                                if st.button("📥 Export", key=f"export_{template['id']}"):
                                    export_path = Path(f"{template['id']}_export.json")
                                    if self.export_template(template['id'], export_path):
                                        st.success(f"Exported to {export_path}")
                            
                            # Add sharing functionality
                            col1, col2 = st.columns(2)
                            with col1:
                                if st.button("🔗 Share Template", key=f"share_{template['id']}"):
                                    st.session_state[f"sharing_{template['id']}"] = True
                            
                            with col2:
                                if st.button("📊 View Stats", key=f"stats_{template['id']}"):
                                    st.session_state[f"stats_{template['id']}"] = True
                            
                            # Handle sharing dialog
                            if st.session_state.get(f"sharing_{template['id']}", False):
                                with st.expander("🔗 Share Template", expanded=True):
                                    self._render_template_sharing_dialog(template)
                            
                            st.divider()
        
        # Template management actions
        st.subheader("🛠️ Template Management")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Import Template**")
            uploaded_file = st.file_uploader("Upload template file", type=['json'])
            if uploaded_file:
                import tempfile
                with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as tmp:
                    tmp.write(uploaded_file.read().decode())
                    tmp_path = Path(tmp.name)
                
                if st.button("Import Template"):
                    if self.import_template(tmp_path):
                        st.success("Template imported successfully!")
                        st.rerun()
                    else:
                        st.error("Failed to import template")
        
        with col2:
            st.markdown("**Template Statistics**")
            if st.button("📊 View Detailed Stats"):
                st.json(stats)
    
    def _render_template_sharing_dialog(self, template: Dict[str, Any]):
        """Render template sharing dialog"""
        st.markdown(f"**Share Template: {template['name']}**")
        
        # Get full template data
        full_template = self.load_template(template['id'])
        if not full_template:
            st.error("Template not found")
            return
        
        # Sharing options
        col1, col2 = st.columns(2)
        
        with col1:
            expires_in_days = st.slider(
                "Expires in days", 
                min_value=1, 
                max_value=365, 
                value=30,
                key=f"expires_{template['id']}"
            )
        
        with col2:
            max_access_count = st.number_input(
                "Max access count", 
                min_value=1, 
                max_value=10000, 
                value=100,
                key=f"max_access_{template['id']}"
            )
        
        # Base URL input
        base_url = st.text_input(
            "Base URL (optional)", 
            value="https://example.com/share",
            key=f"base_url_{template['id']}"
        )
        
        # Generate sharing URL
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("Generate Share URL", key=f"generate_{template['id']}"):
                try:
                    share_url = self.url_sharing_manager.generate_sharing_url(
                        template_data=full_template,
                        base_url=base_url,
                        expires_in_days=expires_in_days,
                        max_access_count=max_access_count
                    )
                    
                    st.success("Share URL generated!")
                    st.code(share_url)
                    
                    # Store in session state for copying
                    st.session_state[f"share_url_{template['id']}"] = share_url
                    
                except Exception as e:
                    st.error(f"Error generating share URL: {str(e)}")
        
        with col2:
            if st.button("Close", key=f"close_sharing_{template['id']}"):
                st.session_state[f"sharing_{template['id']}"] = False
                st.rerun()
        
        # Display existing share URL if available
        if st.session_state.get(f"share_url_{template['id']}"):
            st.markdown("**Generated Share URL:**")
            st.code(st.session_state[f"share_url_{template['id']}"])
            
            if st.button("📋 Copy URL", key=f"copy_{template['id']}"):
                st.success("URL copied to clipboard!")
    
    def render_url_sharing_tab(self):
        """Render URL sharing management tab"""
        st.subheader("🔗 URL Sharing Management")
        
        # Sharing statistics
        stats = self.url_sharing_manager.get_sharing_statistics()
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Shared Templates", stats['total_shared_templates'])
        with col2:
            st.metric("Active Tokens", stats['active_tokens'])
        with col3:
            st.metric("Total Accesses", stats['total_access_count'])
        with col4:
            st.metric("Expired Tokens", stats['expired_tokens'])
        
        # Token management
        st.subheader("🔑 Token Management")
        
        # Validate token
        token_to_validate = st.text_input("Enter token to validate")
        
        if st.button("Validate Token"):
            if token_to_validate:
                is_valid, error_msg = self.url_sharing_manager.validate_sharing_token(token_to_validate)
                if is_valid:
                    st.success("✅ Token is valid")
                    token_info = self.url_sharing_manager.get_token_info(token_to_validate)
                    if token_info:
                        st.json(token_info.to_dict())
                else:
                    st.error(f"❌ Token is invalid: {error_msg}")
        
        # Cleanup expired tokens
        if st.button("🧹 Cleanup Expired Tokens"):
            cleaned_count = self.url_sharing_manager.cleanup_expired_tokens()
            if cleaned_count > 0:
                st.success(f"Cleaned up {cleaned_count} expired tokens")
                st.rerun()
            else:
                st.info("No expired tokens to clean up")
        
        # List shared templates
        st.subheader("📋 Shared Templates")
        
        shared_templates = self.url_sharing_manager.list_shared_templates()
        
        if not shared_templates:
            st.info("No templates have been shared yet.")
        else:
            for template in shared_templates:
                with st.expander(f"📄 {template['name']} ({template['category']})"):
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        st.markdown(f"**Description:** {template['description']}")
                        st.markdown(f"**Author:** {template['author']}")
                        st.markdown(f"**Version:** {template['version']}")
                        st.markdown(f"**Components:** {len(template['components'])}")
                    
                    with col2:
                        sharing_info = template.get('sharing_info', {})
                        st.markdown(f"**Shared At:** {sharing_info.get('shared_at', 'Unknown')}")
                        st.markdown(f"**Shared By:** {sharing_info.get('shared_by', 'Unknown')}")
                        st.markdown(f"**Access Count:** {sharing_info.get('access_count', 0)}")
                        
                        if st.button(f"🗑️ Revoke Share", key=f"revoke_shared_{template['id']}"):
                            # Find and revoke associated tokens
                            revoked_count = 0
                            for token, token_info in self.url_sharing_manager.tokens_index.items():
                                if token_info.template_id == template['id']:
                                    if self.url_sharing_manager.revoke_sharing_token(token):
                                        revoked_count += 1
                            
                            if revoked_count > 0:
                                st.success(f"Revoked {revoked_count} sharing token(s)")
                                st.rerun()
                            else:
                                st.warning("No active tokens found to revoke")
    
    def render_template_gallery_ui(self):
        """Render the template gallery user interface"""
        # Create tabs for different views
        tab1, tab2, tab3 = st.tabs(["📚 Template Gallery", "🔗 URL Sharing", "📊 Statistics"])
        
        with tab1:
            self._render_gallery_tab()
        
        with tab2:
            self.render_url_sharing_tab()
        
        with tab3:
            self._render_statistics_tab()
    
    def _render_gallery_tab(self):
        """Render the main template gallery tab"""
        st.title("📚 Template Gallery")
        
        # Template statistics
        stats = self.get_template_usage_stats()
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Total Templates", stats['total_templates'])
        with col2:
            st.metric("Categories", len(stats['categories']))
        with col3:
            st.metric("Unique Tags", len(stats['tags']))
        with col4:
            st.metric("Authors", len(stats['authors']))
        
        # Search and filter interface
        st.subheader("🔍 Search & Filter")
        
        col1, col2 = st.columns(2)
        
        with col1:
            search_name = st.text_input("Search by name", placeholder="Enter template name...")
            selected_category = st.selectbox(
                "Filter by category",
                options=["All"] + self.get_template_categories(),
                index=0
            )
        
        with col2:
            search_author = st.text_input("Search by author", placeholder="Enter author name...")
            available_tags = list(stats['tags'].keys())
            selected_tags = st.multiselect("Filter by tags", options=available_tags)
        
        # Search templates
        search_category = selected_category if selected_category != "All" else None
        search_tags = selected_tags if selected_tags else None
        search_name_filter = search_name if search_name else None
        search_author_filter = search_author if search_author else None
        
        templates = self.search_templates(
            category=search_category,
            tags=search_tags,
            name_contains=search_name_filter,
            author=search_author_filter
        )
        
        # Display templates
        st.subheader(f"📖 Templates ({len(templates)} found)")
        
        if not templates:
            st.info("No templates found matching your criteria.")
            return
        
        # Display templates in a grid
        for i in range(0, len(templates), 2):
            cols = st.columns(2)
            
            for j, col in enumerate(cols):
                if i + j < len(templates):
                    template = templates[i + j]
                    
                    with col:
                        with st.container():
                            st.markdown(f"**{template['name']}**")
                            st.markdown(f"*{template['description']}*")
                            st.markdown(f"**Category:** {template['category']}")
                            st.markdown(f"**Author:** {template['author']}")
                            st.markdown(f"**Version:** {template['version']}")
                            
                            # Show tags
                            tags = template.get('metadata', {}).get('tags', [])
                            if tags:
                                tag_str = " ".join([f"`{tag}`" for tag in tags])
                                st.markdown(f"**Tags:** {tag_str}")
                            
                            # Action buttons
                            col1, col2, col3 = st.columns(3)
                            
                            with col1:
                                if st.button("📄 View", key=f"view_{template['id']}"):
                                    st.session_state[f"view_template_{template['id']}"] = True
                            
                            with col2:
                                if st.button("📋 Use", key=f"use_{template['id']}"):
                                    st.session_state[f"use_template_{template['id']}"] = True
                            
                            with col3:
                                if st.button("📥 Export", key=f"export_{template['id']}"):
                                    export_path = Path(f"{template['id']}_export.json")
                                    if self.export_template(template['id'], export_path):
                                        st.success(f"Exported to {export_path}")
                            
                            # Add sharing functionality
                            col1, col2 = st.columns(2)
                            with col1:
                                if st.button("🔗 Share Template", key=f"share_{template['id']}"):
                                    st.session_state[f"sharing_{template['id']}"] = True
                            
                            with col2:
                                if st.button("📊 View Stats", key=f"stats_{template['id']}"):
                                    st.session_state[f"stats_{template['id']}"] = True
                            
                            # Handle sharing dialog
                            if st.session_state.get(f"sharing_{template['id']}", False):
                                with st.expander("🔗 Share Template", expanded=True):
                                    self._render_template_sharing_dialog(template)
                            
                            st.divider()
        
        # Template management actions
        st.subheader("🛠️ Template Management")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Import Template**")
            uploaded_file = st.file_uploader("Upload template file", type=['json'])
            if uploaded_file:
                import tempfile
                with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as tmp:
                    tmp.write(uploaded_file.read().decode())
                    tmp_path = Path(tmp.name)
                
                if st.button("Import Template"):
                    if self.import_template(tmp_path):
                        st.success("Template imported successfully!")
                        st.rerun()
                    else:
                        st.error("Failed to import template")
        
        with col2:
            st.markdown("**Template Statistics**")
            if st.button("📊 View Detailed Stats"):
                st.json(stats)
    
    def _render_statistics_tab(self):
        """Render the statistics tab"""
        st.title("📊 Template & Sharing Statistics")
        
        # Template statistics
        template_stats = self.get_template_usage_stats()
        sharing_stats = self.url_sharing_manager.get_sharing_statistics()
        
        # Combined metrics
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Total Templates", template_stats['total_templates'])
        with col2:
            st.metric("Shared Templates", sharing_stats['total_shared_templates'])
        with col3:
            st.metric("Total Shares", sharing_stats['total_access_count'])
        with col4:
            st.metric("Active Tokens", sharing_stats['active_tokens'])
        
        # Detailed statistics
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("📚 Template Statistics")
            st.json(template_stats)
        
        with col2:
            st.subheader("🔗 Sharing Statistics")
            st.json(sharing_stats)
    
    def render(self):
        """Main render method for Template Manager"""
        self.render_template_gallery_ui()