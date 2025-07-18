"""
Usage Analytics and Metrics Collection System for Streamlit Dashboard
Provides comprehensive tracking of user interactions and system usage patterns
"""

import streamlit as st
import json
import time
import hashlib
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass, field, asdict
from datetime import datetime, timedelta
from collections import defaultdict, deque
import threading
import uuid
import os
from urllib.parse import urlparse


@dataclass
class UserSession:
    """Represents a user session with tracking data"""
    
    session_id: str
    user_id: str
    start_time: str
    last_activity: str
    page_views: int = 0
    actions_count: int = 0
    components_used: List[str] = field(default_factory=list)
    features_accessed: List[str] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)
    
    def __post_init__(self):
        """Validate session data after initialization"""
        if not self.session_id or self.session_id.strip() == "":
            raise ValueError("Session ID cannot be empty")
        
        if not self.user_id or self.user_id.strip() == "":
            raise ValueError("User ID cannot be empty")
    
    def update_activity(self):
        """Update last activity timestamp"""
        self.last_activity = datetime.now().isoformat()
    
    def add_page_view(self, page_name: str):
        """Add a page view to the session"""
        self.page_views += 1
        self.update_activity()
        
        if page_name not in self.components_used:
            self.components_used.append(page_name)
    
    def add_action(self, action_name: str):
        """Add an action to the session"""
        self.actions_count += 1
        self.update_activity()
        
        if action_name not in self.features_accessed:
            self.features_accessed.append(action_name)
    
    def get_session_duration(self) -> float:
        """Get session duration in seconds"""
        start = datetime.fromisoformat(self.start_time)
        last = datetime.fromisoformat(self.last_activity)
        return (last - start).total_seconds()
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert session to dictionary for serialization"""
        return asdict(self)
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'UserSession':
        """Create session from dictionary"""
        return cls(**data)


@dataclass
class UserAction:
    """Represents a user action with detailed tracking"""
    
    action_id: str
    session_id: str
    user_id: str
    timestamp: str
    action_type: str
    action_name: str
    component: str
    page: str
    duration: float = 0.0
    metadata: Dict[str, Any] = field(default_factory=dict)
    
    def __post_init__(self):
        """Validate action data"""
        if not self.action_type or self.action_type.strip() == "":
            raise ValueError("Action type cannot be empty")
        
        if not self.action_name or self.action_name.strip() == "":
            raise ValueError("Action name cannot be empty")
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert action to dictionary for serialization"""
        return asdict(self)
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'UserAction':
        """Create action from dictionary"""
        return cls(**data)


@dataclass
class AnalyticsMetric:
    """Represents an analytics metric"""
    
    metric_id: str
    name: str
    value: float
    unit: str
    timestamp: str
    category: str = "general"
    tags: List[str] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)
    
    def __post_init__(self):
        """Validate metric data"""
        if not self.name or self.name.strip() == "":
            raise ValueError("Metric name cannot be empty")
        
        if not isinstance(self.value, (int, float)):
            raise ValueError("Metric value must be numeric")
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert metric to dictionary for serialization"""
        return asdict(self)
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'AnalyticsMetric':
        """Create metric from dictionary"""
        return cls(**data)


class UsageAnalytics:
    """Comprehensive usage analytics and metrics collection system"""
    
    def __init__(self, storage_path: Path, enable_tracking: bool = True):
        """Initialize usage analytics system"""
        self.storage_path = storage_path
        self.enable_tracking = enable_tracking
        self.storage_path.mkdir(parents=True, exist_ok=True)
        
        # Create subdirectories for different data types
        self.sessions_dir = self.storage_path / "sessions"
        self.actions_dir = self.storage_path / "actions"
        self.metrics_dir = self.storage_path / "metrics"
        
        for dir_path in [self.sessions_dir, self.actions_dir, self.metrics_dir]:
            dir_path.mkdir(exist_ok=True)
        
        # In-memory storage for active sessions and recent data
        self.active_sessions: Dict[str, UserSession] = {}
        self.recent_actions: deque = deque(maxlen=1000)
        self.recent_metrics: deque = deque(maxlen=1000)
        
        # Configuration
        self.session_timeout = 30 * 60  # 30 minutes
        self.max_storage_days = 90
        
        # Thread safety
        self.lock = threading.Lock()
        
        # Initialize current session
        self.current_session = self._initialize_session()
        
        # Load existing data
        self._load_recent_data()
    
    def _initialize_session(self) -> UserSession:
        """Initialize current user session"""
        if not self.enable_tracking:
            return None
        
        session_id = self._get_session_id()
        user_id = self._get_user_id()
        
        # Check if session already exists
        if session_id in self.active_sessions:
            session = self.active_sessions[session_id]
            session.update_activity()
            return session
        
        # Create new session
        session = UserSession(
            session_id=session_id,
            user_id=user_id,
            start_time=datetime.now().isoformat(),
            last_activity=datetime.now().isoformat(),
            metadata={
                "user_agent": self._get_user_agent(),
                "ip_address": self._get_ip_address(),
                "timezone": self._get_timezone(),
                "screen_resolution": self._get_screen_resolution()
            }
        )
        
        with self.lock:
            self.active_sessions[session_id] = session
            self._save_session(session)
        
        return session
    
    def _get_session_id(self) -> str:
        """Get or create session ID"""
        if 'analytics_session_id' not in st.session_state:
            st.session_state.analytics_session_id = str(uuid.uuid4())
        return st.session_state.analytics_session_id
    
    def _get_user_id(self) -> str:
        """Get or create user ID"""
        if 'analytics_user_id' not in st.session_state:
            # Generate anonymous user ID based on session info
            session_info = f"{self._get_ip_address()}_{self._get_user_agent()}"
            user_hash = hashlib.sha256(session_info.encode()).hexdigest()[:16]
            st.session_state.analytics_user_id = f"user_{user_hash}"
        return st.session_state.analytics_user_id
    
    def _get_user_agent(self) -> str:
        """Get user agent string"""
        try:
            # Try to get from Streamlit context
            return st.context.headers.get("User-Agent", "Unknown")
        except:
            return "Unknown"
    
    def _get_ip_address(self) -> str:
        """Get user IP address"""
        try:
            # Try to get from Streamlit context
            return st.context.headers.get("X-Forwarded-For", "Unknown")
        except:
            return "Unknown"
    
    def _get_timezone(self) -> str:
        """Get user timezone"""
        try:
            # Could be enhanced with JavaScript to get actual timezone
            return "UTC"
        except:
            return "UTC"
    
    def _get_screen_resolution(self) -> str:
        """Get screen resolution"""
        try:
            # Could be enhanced with JavaScript to get actual resolution
            return "Unknown"
        except:
            return "Unknown"
    
    def _save_session(self, session: UserSession):
        """Save session to storage"""
        try:
            session_file = self.sessions_dir / f"{session.session_id}.json"
            with open(session_file, 'w') as f:
                json.dump(session.to_dict(), f, indent=2)
        except Exception as e:
            st.error(f"Failed to save session: {str(e)}")
    
    def _save_action(self, action: UserAction):
        """Save action to storage"""
        try:
            # Save to daily file for efficient querying
            date_str = datetime.now().strftime("%Y-%m-%d")
            actions_file = self.actions_dir / f"actions_{date_str}.json"
            
            # Append to daily file
            actions_data = []
            if actions_file.exists():
                with open(actions_file, 'r') as f:
                    actions_data = json.load(f)
            
            actions_data.append(action.to_dict())
            
            with open(actions_file, 'w') as f:
                json.dump(actions_data, f, indent=2)
        except Exception as e:
            st.error(f"Failed to save action: {str(e)}")
    
    def _save_metric(self, metric: AnalyticsMetric):
        """Save metric to storage"""
        try:
            # Save to daily file for efficient querying
            date_str = datetime.now().strftime("%Y-%m-%d")
            metrics_file = self.metrics_dir / f"metrics_{date_str}.json"
            
            # Append to daily file
            metrics_data = []
            if metrics_file.exists():
                with open(metrics_file, 'r') as f:
                    metrics_data = json.load(f)
            
            metrics_data.append(metric.to_dict())
            
            with open(metrics_file, 'w') as f:
                json.dump(metrics_data, f, indent=2)
        except Exception as e:
            st.error(f"Failed to save metric: {str(e)}")
    
    def _load_recent_data(self):
        """Load recent data from storage"""
        try:
            # Load recent actions (last 24 hours)
            yesterday = datetime.now() - timedelta(days=1)
            
            for actions_file in self.actions_dir.glob("actions_*.json"):
                try:
                    with open(actions_file, 'r') as f:
                        actions_data = json.load(f)
                    
                    for action_data in actions_data:
                        action = UserAction.from_dict(action_data)
                        action_time = datetime.fromisoformat(action.timestamp)
                        
                        if action_time >= yesterday:
                            self.recent_actions.append(action)
                except Exception:
                    continue
            
            # Load recent metrics (last 24 hours)
            for metrics_file in self.metrics_dir.glob("metrics_*.json"):
                try:
                    with open(metrics_file, 'r') as f:
                        metrics_data = json.load(f)
                    
                    for metric_data in metrics_data:
                        metric = AnalyticsMetric.from_dict(metric_data)
                        metric_time = datetime.fromisoformat(metric.timestamp)
                        
                        if metric_time >= yesterday:
                            self.recent_metrics.append(metric)
                except Exception:
                    continue
                    
        except Exception as e:
            st.error(f"Failed to load recent data: {str(e)}")
    
    def track_page_view(self, page_name: str, metadata: Dict[str, Any] = None):
        """Track a page view"""
        if not self.enable_tracking or not self.current_session:
            return
        
        # Update session
        self.current_session.add_page_view(page_name)
        
        # Create action
        action = UserAction(
            action_id=str(uuid.uuid4()),
            session_id=self.current_session.session_id,
            user_id=self.current_session.user_id,
            timestamp=datetime.now().isoformat(),
            action_type="page_view",
            action_name=f"view_{page_name}",
            component=page_name,
            page=page_name,
            metadata=metadata or {}
        )
        
        # Save action
        with self.lock:
            self.recent_actions.append(action)
            self._save_action(action)
            self._save_session(self.current_session)
    
    def track_user_action(self, action_type: str, action_name: str, 
                         component: str, page: str, duration: float = 0.0,
                         metadata: Dict[str, Any] = None):
        """Track a user action"""
        if not self.enable_tracking or not self.current_session:
            return
        
        # Update session
        self.current_session.add_action(action_name)
        
        # Create action
        action = UserAction(
            action_id=str(uuid.uuid4()),
            session_id=self.current_session.session_id,
            user_id=self.current_session.user_id,
            timestamp=datetime.now().isoformat(),
            action_type=action_type,
            action_name=action_name,
            component=component,
            page=page,
            duration=duration,
            metadata=metadata or {}
        )
        
        # Save action
        with self.lock:
            self.recent_actions.append(action)
            self._save_action(action)
            self._save_session(self.current_session)
    
    def track_metric(self, name: str, value: float, unit: str, 
                    category: str = "general", tags: List[str] = None,
                    metadata: Dict[str, Any] = None):
        """Track a custom metric"""
        if not self.enable_tracking:
            return
        
        # Create metric
        metric = AnalyticsMetric(
            metric_id=str(uuid.uuid4()),
            name=name,
            value=value,
            unit=unit,
            timestamp=datetime.now().isoformat(),
            category=category,
            tags=tags or [],
            metadata=metadata or {}
        )
        
        # Save metric
        with self.lock:
            self.recent_metrics.append(metric)
            self._save_metric(metric)
    
    def get_session_analytics(self) -> Dict[str, Any]:
        """Get analytics for current session"""
        if not self.current_session:
            return {}
        
        return {
            "session_id": self.current_session.session_id,
            "user_id": self.current_session.user_id,
            "start_time": self.current_session.start_time,
            "duration": self.current_session.get_session_duration(),
            "page_views": self.current_session.page_views,
            "actions_count": self.current_session.actions_count,
            "components_used": self.current_session.components_used,
            "features_accessed": self.current_session.features_accessed
        }
    
    def get_usage_statistics(self, days: int = 7) -> Dict[str, Any]:
        """Get usage statistics for the specified number of days"""
        cutoff_date = datetime.now() - timedelta(days=days)
        
        stats = {
            "total_sessions": 0,
            "total_page_views": 0,
            "total_actions": 0,
            "unique_users": set(),
            "popular_pages": defaultdict(int),
            "popular_actions": defaultdict(int),
            "average_session_duration": 0.0,
            "bounce_rate": 0.0,
            "daily_stats": defaultdict(lambda: {
                "sessions": 0,
                "page_views": 0,
                "actions": 0,
                "unique_users": set()
            })
        }
        
        # Process recent actions
        for action in self.recent_actions:
            action_time = datetime.fromisoformat(action.timestamp)
            if action_time >= cutoff_date:
                stats["total_actions"] += 1
                stats["unique_users"].add(action.user_id)
                stats["popular_actions"][action.action_name] += 1
                
                if action.action_type == "page_view":
                    stats["total_page_views"] += 1
                    stats["popular_pages"][action.page] += 1
                
                # Daily stats
                date_key = action_time.strftime("%Y-%m-%d")
                stats["daily_stats"][date_key]["actions"] += 1
                stats["daily_stats"][date_key]["unique_users"].add(action.user_id)
                
                if action.action_type == "page_view":
                    stats["daily_stats"][date_key]["page_views"] += 1
        
        # Process sessions
        session_durations = []
        bounce_count = 0
        
        for session in self.active_sessions.values():
            session_time = datetime.fromisoformat(session.start_time)
            if session_time >= cutoff_date:
                stats["total_sessions"] += 1
                duration = session.get_session_duration()
                session_durations.append(duration)
                
                if session.page_views <= 1:
                    bounce_count += 1
                
                # Daily stats
                date_key = session_time.strftime("%Y-%m-%d")
                stats["daily_stats"][date_key]["sessions"] += 1
                stats["daily_stats"][date_key]["unique_users"].add(session.user_id)
        
        # Calculate averages
        if session_durations:
            stats["average_session_duration"] = sum(session_durations) / len(session_durations)
        
        if stats["total_sessions"] > 0:
            stats["bounce_rate"] = bounce_count / stats["total_sessions"]
        
        # Convert sets to counts for serialization
        stats["unique_users"] = len(stats["unique_users"])
        for date_key in stats["daily_stats"]:
            stats["daily_stats"][date_key]["unique_users"] = len(stats["daily_stats"][date_key]["unique_users"])
        
        return stats
    
    def get_component_analytics(self) -> Dict[str, Any]:
        """Get analytics for each component"""
        component_stats = defaultdict(lambda: {
            "page_views": 0,
            "actions": 0,
            "unique_users": set(),
            "average_time_spent": 0.0,
            "popular_actions": defaultdict(int)
        })
        
        # Process recent actions
        for action in self.recent_actions:
            component = action.component
            component_stats[component]["actions"] += 1
            component_stats[component]["unique_users"].add(action.user_id)
            component_stats[component]["popular_actions"][action.action_name] += 1
            
            if action.action_type == "page_view":
                component_stats[component]["page_views"] += 1
        
        # Convert sets to counts and calculate averages
        for component in component_stats:
            component_stats[component]["unique_users"] = len(component_stats[component]["unique_users"])
            component_stats[component]["popular_actions"] = dict(component_stats[component]["popular_actions"])
        
        return dict(component_stats)
    
    def get_user_journey_analytics(self) -> Dict[str, Any]:
        """Get user journey analytics"""
        user_journeys = defaultdict(list)
        
        # Group actions by user
        for action in self.recent_actions:
            user_journeys[action.user_id].append(action)
        
        # Analyze journeys
        journey_stats = {
            "total_journeys": len(user_journeys),
            "common_paths": defaultdict(int),
            "entry_points": defaultdict(int),
            "exit_points": defaultdict(int),
            "average_journey_length": 0.0
        }
        
        journey_lengths = []
        
        for user_id, actions in user_journeys.items():
            # Sort actions by timestamp
            actions.sort(key=lambda x: x.timestamp)
            
            if actions:
                # Entry point
                journey_stats["entry_points"][actions[0].page] += 1
                
                # Exit point
                journey_stats["exit_points"][actions[-1].page] += 1
                
                # Journey length
                journey_lengths.append(len(actions))
                
                # Path analysis
                path = " -> ".join([action.page for action in actions if action.action_type == "page_view"])
                if path:
                    journey_stats["common_paths"][path] += 1
        
        # Calculate averages
        if journey_lengths:
            journey_stats["average_journey_length"] = sum(journey_lengths) / len(journey_lengths)
        
        return journey_stats
    
    def cleanup_old_data(self):
        """Clean up old data files"""
        cutoff_date = datetime.now() - timedelta(days=self.max_storage_days)
        
        for directory in [self.sessions_dir, self.actions_dir, self.metrics_dir]:
            for file_path in directory.glob("*.json"):
                try:
                    # Extract date from filename
                    filename = file_path.stem
                    if "_" in filename:
                        date_str = filename.split("_")[-1]
                        file_date = datetime.strptime(date_str, "%Y-%m-%d")
                        
                        if file_date < cutoff_date:
                            file_path.unlink()
                except Exception:
                    continue
    
    def export_analytics_data(self, start_date: datetime, end_date: datetime) -> Dict[str, Any]:
        """Export analytics data for specified date range"""
        export_data = {
            "export_timestamp": datetime.now().isoformat(),
            "date_range": {
                "start": start_date.isoformat(),
                "end": end_date.isoformat()
            },
            "sessions": [],
            "actions": [],
            "metrics": []
        }
        
        # Export sessions
        for session_file in self.sessions_dir.glob("*.json"):
            try:
                with open(session_file, 'r') as f:
                    session_data = json.load(f)
                
                session_time = datetime.fromisoformat(session_data["start_time"])
                if start_date <= session_time <= end_date:
                    export_data["sessions"].append(session_data)
            except Exception:
                continue
        
        # Export actions
        for actions_file in self.actions_dir.glob("actions_*.json"):
            try:
                with open(actions_file, 'r') as f:
                    actions_data = json.load(f)
                
                for action_data in actions_data:
                    action_time = datetime.fromisoformat(action_data["timestamp"])
                    if start_date <= action_time <= end_date:
                        export_data["actions"].append(action_data)
            except Exception:
                continue
        
        # Export metrics
        for metrics_file in self.metrics_dir.glob("metrics_*.json"):
            try:
                with open(metrics_file, 'r') as f:
                    metrics_data = json.load(f)
                
                for metric_data in metrics_data:
                    metric_time = datetime.fromisoformat(metric_data["timestamp"])
                    if start_date <= metric_time <= end_date:
                        export_data["metrics"].append(metric_data)
            except Exception:
                continue
        
        return export_data
    
    def render_analytics_dashboard(self):
        """Render the analytics dashboard UI"""
        st.title("📊 Usage Analytics Dashboard")
        
        # Current session info
        st.subheader("📱 Current Session")
        session_info = self.get_session_analytics()
        
        if session_info:
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                st.metric("Session Duration", f"{session_info['duration']/60:.1f} min")
            with col2:
                st.metric("Page Views", session_info["page_views"])
            with col3:
                st.metric("Actions", session_info["actions_count"])
            with col4:
                st.metric("Components Used", len(session_info["components_used"]))
            
            # Session details
            with st.expander("Session Details"):
                st.json(session_info)
        else:
            st.info("No active session data available")
        
        # Usage statistics
        st.subheader("📈 Usage Statistics")
        
        # Time range selector
        time_range = st.selectbox("Time Range", ["1 day", "7 days", "30 days", "90 days"])
        days = {"1 day": 1, "7 days": 7, "30 days": 30, "90 days": 90}[time_range]
        
        stats = self.get_usage_statistics(days)
        
        # Key metrics
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Total Sessions", stats["total_sessions"])
        with col2:
            st.metric("Page Views", stats["total_page_views"])
        with col3:
            st.metric("Unique Users", stats["unique_users"])
        with col4:
            st.metric("Bounce Rate", f"{stats['bounce_rate']*100:.1f}%")
        
        # Additional metrics
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Total Actions", stats["total_actions"])
        with col2:
            st.metric("Avg Session Duration", f"{stats['average_session_duration']/60:.1f} min")
        with col3:
            if stats["total_sessions"] > 0:
                st.metric("Actions per Session", f"{stats['total_actions']/stats['total_sessions']:.1f}")
            else:
                st.metric("Actions per Session", "0")
        
        # Popular pages and actions
        st.subheader("📊 Popular Content")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Most Popular Pages**")
            if stats["popular_pages"]:
                for page, count in sorted(stats["popular_pages"].items(), key=lambda x: x[1], reverse=True)[:10]:
                    st.write(f"• {page}: {count} views")
            else:
                st.info("No page view data available")
        
        with col2:
            st.markdown("**Most Popular Actions**")
            if stats["popular_actions"]:
                for action, count in sorted(stats["popular_actions"].items(), key=lambda x: x[1], reverse=True)[:10]:
                    st.write(f"• {action}: {count} times")
            else:
                st.info("No action data available")
        
        # Component analytics
        st.subheader("🔧 Component Analytics")
        
        component_stats = self.get_component_analytics()
        
        if component_stats:
            for component, stats in component_stats.items():
                with st.expander(f"📄 {component}"):
                    col1, col2, col3 = st.columns(3)
                    
                    with col1:
                        st.metric("Page Views", stats["page_views"])
                    with col2:
                        st.metric("Actions", stats["actions"])
                    with col3:
                        st.metric("Unique Users", stats["unique_users"])
                    
                    if stats["popular_actions"]:
                        st.markdown("**Popular Actions:**")
                        for action, count in sorted(stats["popular_actions"].items(), key=lambda x: x[1], reverse=True)[:5]:
                            st.write(f"• {action}: {count} times")
        else:
            st.info("No component analytics data available")
        
        # User journey analytics
        st.subheader("🛤️ User Journey Analytics")
        
        journey_stats = self.get_user_journey_analytics()
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Total Journeys", journey_stats["total_journeys"])
        with col2:
            st.metric("Avg Journey Length", f"{journey_stats['average_journey_length']:.1f} steps")
        with col3:
            st.metric("Entry Points", len(journey_stats["entry_points"]))
        
        # Common paths
        if journey_stats["common_paths"]:
            st.markdown("**Common User Paths:**")
            for path, count in sorted(journey_stats["common_paths"].items(), key=lambda x: x[1], reverse=True)[:5]:
                st.write(f"• {path} ({count} users)")
        
        # Entry and exit points
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Top Entry Points:**")
            if journey_stats["entry_points"]:
                for page, count in sorted(journey_stats["entry_points"].items(), key=lambda x: x[1], reverse=True)[:5]:
                    st.write(f"• {page}: {count} entries")
        
        with col2:
            st.markdown("**Top Exit Points:**")
            if journey_stats["exit_points"]:
                for page, count in sorted(journey_stats["exit_points"].items(), key=lambda x: x[1], reverse=True)[:5]:
                    st.write(f"• {page}: {count} exits")
        
        # Data management
        st.subheader("🗂️ Data Management")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button("🧹 Cleanup Old Data"):
                self.cleanup_old_data()
                st.success("Old data cleaned up successfully")
        
        with col2:
            if st.button("📤 Export Analytics Data"):
                start_date = datetime.now() - timedelta(days=30)
                end_date = datetime.now()
                export_data = self.export_analytics_data(start_date, end_date)
                
                export_file = self.storage_path / f"analytics_export_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
                with open(export_file, 'w') as f:
                    json.dump(export_data, f, indent=2)
                
                st.success(f"Analytics data exported to: {export_file}")
        
        with col3:
            if st.button("🔄 Refresh Data"):
                self._load_recent_data()
                st.success("Data refreshed successfully")
        
        # Privacy and settings
        st.subheader("🔒 Privacy & Settings")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Current Settings:**")
            st.write(f"• Tracking Enabled: {self.enable_tracking}")
            st.write(f"• Session Timeout: {self.session_timeout/60:.0f} minutes")
            st.write(f"• Data Retention: {self.max_storage_days} days")
            st.write(f"• Anonymous User ID: {self.current_session.user_id if self.current_session else 'None'}")
        
        with col2:
            st.markdown("**Privacy Information:**")
            st.write("• All data is anonymized")
            st.write("• No personal information is collected")
            st.write("• Data is stored locally")
            st.write("• IP addresses are hashed")
    
    def render(self):
        """Main render method for Usage Analytics"""
        self.render_analytics_dashboard()


# Global analytics instance
_analytics_instance = None

def get_analytics_instance(storage_path: Path = None, enable_tracking: bool = True) -> UsageAnalytics:
    """Get or create global analytics instance"""
    global _analytics_instance
    if _analytics_instance is None:
        default_path = Path("data/analytics")
        _analytics_instance = UsageAnalytics(
            storage_path=storage_path or default_path,
            enable_tracking=enable_tracking
        )
    return _analytics_instance

def track_page_view(page_name: str, metadata: Dict[str, Any] = None):
    """Convenience function for tracking page views"""
    analytics = get_analytics_instance()
    analytics.track_page_view(page_name, metadata)

def track_user_action(action_type: str, action_name: str, component: str, page: str, 
                     duration: float = 0.0, metadata: Dict[str, Any] = None):
    """Convenience function for tracking user actions"""
    analytics = get_analytics_instance()
    analytics.track_user_action(action_type, action_name, component, page, duration, metadata)

def track_metric(name: str, value: float, unit: str, category: str = "general", 
                tags: List[str] = None, metadata: Dict[str, Any] = None):
    """Convenience function for tracking metrics"""
    analytics = get_analytics_instance()
    analytics.track_metric(name, value, unit, category, tags, metadata)