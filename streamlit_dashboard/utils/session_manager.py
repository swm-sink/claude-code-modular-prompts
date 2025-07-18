"""
Session management for Streamlit dashboard.
Provides persistence of user configurations and progress across browser sessions.
"""

import streamlit as st
import json
from pathlib import Path
from typing import Dict, Any, Optional, List
from datetime import datetime
import uuid
import hashlib
from dataclasses import dataclass, asdict


@dataclass
class SessionData:
    """User session data structure"""
    session_id: str
    user_id: str
    created_at: str
    last_accessed: str
    prompt_builder_state: Dict[str, Any]
    navigation_preferences: Dict[str, Any]
    recent_activities: List[Dict[str, Any]]
    saved_configurations: List[Dict[str, Any]]
    performance_preferences: Dict[str, Any]


class SessionManager:
    """Manages user sessions and persistent state"""
    
    def __init__(self, storage_path: Path = None):
        """Initialize session manager"""
        self.storage_path = storage_path or Path("data/sessions")
        self.storage_path.mkdir(parents=True, exist_ok=True)
        
        # Initialize session
        self._initialize_session()
    
    def _initialize_session(self):
        """Initialize or restore user session"""
        
        # Generate or retrieve session ID
        if 'session_id' not in st.session_state:
            st.session_state.session_id = str(uuid.uuid4())
        
        # Generate user ID based on browser characteristics (simple approach)
        if 'user_id' not in st.session_state:
            # In production, this could be more sophisticated
            browser_info = str(st.session_state.get('_scriptrunner_id', 'anonymous'))
            st.session_state.user_id = hashlib.md5(browser_info.encode()).hexdigest()[:12]
        
        # Try to restore previous session
        self._restore_session()
        
        # Initialize session data if not exists
        if 'session_data' not in st.session_state:
            st.session_state.session_data = SessionData(
                session_id=st.session_state.session_id,
                user_id=st.session_state.user_id,
                created_at=datetime.now().isoformat(),
                last_accessed=datetime.now().isoformat(),
                prompt_builder_state={
                    'composition_workspace': [],
                    'selected_modules': [],
                    'constructed_prompt': '',
                    'effectiveness_score': 0.0,
                    'last_validation_results': {}
                },
                navigation_preferences={
                    'last_page': 'Framework Overview',
                    'favorite_pages': [],
                    'collapsed_sections': []
                },
                recent_activities=[],
                saved_configurations=[],
                performance_preferences={
                    'auto_save_enabled': True,
                    'auto_save_interval': 300,  # 5 minutes
                    'performance_mode': 'standard'
                }
            )
    
    def _restore_session(self):
        """Attempt to restore previous session"""
        try:
            session_file = self.storage_path / f"{st.session_state.user_id}.json"
            if session_file.exists():
                with open(session_file, 'r') as f:
                    data = json.load(f)
                
                # Convert to SessionData object
                st.session_state.session_data = SessionData(**data)
                
                # Update last accessed time
                st.session_state.session_data.last_accessed = datetime.now().isoformat()
                
                # Log restoration
                self.log_activity("session_restored", {
                    "previous_session": data.get('session_id', 'unknown'),
                    "restored_at": datetime.now().isoformat()
                })
                
        except Exception as e:
            # If restoration fails, we'll just start fresh
            st.warning(f"Could not restore previous session: {e}")
    
    def save_session(self):
        """Save current session state to persistent storage"""
        try:
            if 'session_data' in st.session_state:
                session_data = st.session_state.session_data
                session_data.last_accessed = datetime.now().isoformat()
                
                # Save to file
                session_file = self.storage_path / f"{session_data.user_id}.json"
                with open(session_file, 'w') as f:
                    json.dump(asdict(session_data), f, indent=2, ensure_ascii=False)
                
                return True
        except Exception as e:
            st.error(f"Failed to save session: {e}")
            return False
    
    def update_prompt_builder_state(self, state_data: Dict[str, Any]):
        """Update prompt builder state in session"""
        if 'session_data' in st.session_state:
            st.session_state.session_data.prompt_builder_state.update(state_data)
            
            # Auto-save if enabled
            if st.session_state.session_data.performance_preferences.get('auto_save_enabled', True):
                self.save_session()
    
    def get_prompt_builder_state(self) -> Dict[str, Any]:
        """Get current prompt builder state"""
        if 'session_data' in st.session_state:
            return st.session_state.session_data.prompt_builder_state
        return {}
    
    def update_navigation_preferences(self, preferences: Dict[str, Any]):
        """Update navigation preferences"""
        if 'session_data' in st.session_state:
            st.session_state.session_data.navigation_preferences.update(preferences)
            self.save_session()
    
    def get_navigation_preferences(self) -> Dict[str, Any]:
        """Get navigation preferences"""
        if 'session_data' in st.session_state:
            return st.session_state.session_data.navigation_preferences
        return {}
    
    def log_activity(self, activity_type: str, details: Dict[str, Any] = None):
        """Log user activity"""
        if 'session_data' in st.session_state:
            activity = {
                'timestamp': datetime.now().isoformat(),
                'type': activity_type,
                'details': details or {}
            }
            
            # Keep only last 50 activities
            st.session_state.session_data.recent_activities.append(activity)
            st.session_state.session_data.recent_activities = \
                st.session_state.session_data.recent_activities[-50:]
    
    def save_configuration(self, name: str, config_data: Dict[str, Any]):
        """Save a named configuration"""
        if 'session_data' in st.session_state:
            configuration = {
                'id': str(uuid.uuid4()),
                'name': name,
                'created_at': datetime.now().isoformat(),
                'config_data': config_data
            }
            
            st.session_state.session_data.saved_configurations.append(configuration)
            self.save_session()
            
            self.log_activity("configuration_saved", {
                "name": name,
                "config_id": configuration['id']
            })
            
            return configuration['id']
    
    def get_saved_configurations(self) -> List[Dict[str, Any]]:
        """Get all saved configurations"""
        if 'session_data' in st.session_state:
            return st.session_state.session_data.saved_configurations
        return []
    
    def load_configuration(self, config_id: str) -> Optional[Dict[str, Any]]:
        """Load a saved configuration by ID"""
        configs = self.get_saved_configurations()
        for config in configs:
            if config['id'] == config_id:
                self.log_activity("configuration_loaded", {
                    "name": config['name'],
                    "config_id": config_id
                })
                return config['config_data']
        return None
    
    def delete_configuration(self, config_id: str) -> bool:
        """Delete a saved configuration"""
        if 'session_data' in st.session_state:
            configs = st.session_state.session_data.saved_configurations
            original_count = len(configs)
            
            st.session_state.session_data.saved_configurations = [
                c for c in configs if c['id'] != config_id
            ]
            
            if len(st.session_state.session_data.saved_configurations) < original_count:
                self.save_session()
                self.log_activity("configuration_deleted", {"config_id": config_id})
                return True
        
        return False
    
    def get_recent_activities(self, limit: int = 10) -> List[Dict[str, Any]]:
        """Get recent user activities"""
        if 'session_data' in st.session_state:
            activities = st.session_state.session_data.recent_activities
            return activities[-limit:] if activities else []
        return []
    
    def get_session_statistics(self) -> Dict[str, Any]:
        """Get session statistics"""
        if 'session_data' not in st.session_state:
            return {}
        
        session_data = st.session_state.session_data
        
        # Calculate session duration
        created = datetime.fromisoformat(session_data.created_at)
        last_accessed = datetime.fromisoformat(session_data.last_accessed)
        duration = (last_accessed - created).total_seconds()
        
        # Activity statistics
        activities = session_data.recent_activities
        activity_types = {}
        for activity in activities:
            activity_type = activity.get('type', 'unknown')
            activity_types[activity_type] = activity_types.get(activity_type, 0) + 1
        
        return {
            'session_id': session_data.session_id,
            'user_id': session_data.user_id,
            'session_duration_minutes': round(duration / 60, 2),
            'total_activities': len(activities),
            'activity_breakdown': activity_types,
            'saved_configurations': len(session_data.saved_configurations),
            'prompt_builder_usage': bool(session_data.prompt_builder_state.get('composition_workspace')),
            'last_accessed': session_data.last_accessed
        }
    
    def clear_session(self):
        """Clear current session data"""
        if 'session_data' in st.session_state:
            # Log the clear action
            self.log_activity("session_cleared", {})
            
            # Clear session state
            del st.session_state.session_data
            
            # Remove persistent file
            try:
                session_file = self.storage_path / f"{st.session_state.user_id}.json"
                if session_file.exists():
                    session_file.unlink()
            except Exception as e:
                st.warning(f"Could not remove session file: {e}")
            
            # Reinitialize
            self._initialize_session()
    
    def export_session_data(self) -> str:
        """Export session data as JSON"""
        if 'session_data' in st.session_state:
            export_data = {
                'export_metadata': {
                    'export_type': 'session_data',
                    'export_timestamp': datetime.now().isoformat(),
                    'framework_version': '3.0.0'
                },
                'session_data': asdict(st.session_state.session_data)
            }
            return json.dumps(export_data, indent=2, ensure_ascii=False)
        return "{}"
    
    def render_session_management_ui(self):
        """Render session management UI in sidebar"""
        st.sidebar.markdown("---")
        st.sidebar.markdown("### 💾 Session Management")
        
        # Session info
        if 'session_data' in st.session_state:
            stats = self.get_session_statistics()
            
            with st.sidebar.expander("📊 Session Info", expanded=False):
                st.write(f"**User ID:** {stats['user_id'][:8]}...")
                st.write(f"**Duration:** {stats['session_duration_minutes']:.1f} min")
                st.write(f"**Activities:** {stats['total_activities']}")
                st.write(f"**Saved Configs:** {stats['saved_configurations']}")
            
            # Auto-save settings
            with st.sidebar.expander("⚙️ Auto-Save", expanded=False):
                current_prefs = st.session_state.session_data.performance_preferences
                
                auto_save = st.checkbox(
                    "Enable Auto-Save",
                    value=current_prefs.get('auto_save_enabled', True),
                    key="auto_save_enabled"
                )
                
                if auto_save != current_prefs.get('auto_save_enabled', True):
                    current_prefs['auto_save_enabled'] = auto_save
                    self.save_session()
                
                if auto_save:
                    interval = st.select_slider(
                        "Save Interval (minutes)",
                        options=[1, 5, 10, 15, 30],
                        value=current_prefs.get('auto_save_interval', 300) // 60,
                        key="auto_save_interval"
                    )
                    
                    if interval * 60 != current_prefs.get('auto_save_interval', 300):
                        current_prefs['auto_save_interval'] = interval * 60
                        self.save_session()
            
            # Session actions
            col1, col2 = st.sidebar.columns(2)
            
            with col1:
                if st.button("💾 Save", help="Save current session", use_container_width=True):
                    if self.save_session():
                        st.success("Session saved!")
                    else:
                        st.error("Save failed!")
            
            with col2:
                if st.button("🗑️ Clear", help="Clear session data", use_container_width=True):
                    self.clear_session()
                    st.success("Session cleared!")
                    st.rerun()


# Global session manager instance
_session_manager = None

def get_session_manager() -> SessionManager:
    """Get global session manager instance"""
    global _session_manager
    if _session_manager is None:
        _session_manager = SessionManager()
    return _session_manager

def init_session_management():
    """Initialize session management for the dashboard"""
    return get_session_manager()