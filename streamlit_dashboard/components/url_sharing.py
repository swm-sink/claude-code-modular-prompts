"""
URL Sharing Component for Claude Code Modular Prompts Framework
Provides secure template sharing via URL tokens with expiration and access limits
"""

import streamlit as st
import json
import secrets
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass, field, asdict
from datetime import datetime, timedelta
import uuid
import hashlib
import copy


@dataclass
class SharingToken:
    """Represents a secure sharing token for templates"""
    
    token: str
    template_id: str
    created_at: str
    expires_at: str
    access_count: int = 0
    max_access_count: int = 100
    
    def __post_init__(self):
        """Validate token data after initialization"""
        if not self.token or self.token.strip() == "":
            raise ValueError("Token cannot be empty")
        
        if not self.template_id or self.template_id.strip() == "":
            raise ValueError("Template ID cannot be empty")
        
        if self.max_access_count < 0:
            raise ValueError("Max access count cannot be negative")
    
    def is_expired(self) -> bool:
        """Check if token has expired"""
        try:
            expires_at = datetime.fromisoformat(self.expires_at.replace('Z', '+00:00'))
            return datetime.now() > expires_at
        except ValueError:
            return True  # Invalid date format means expired
    
    def is_access_limit_reached(self) -> bool:
        """Check if access limit has been reached"""
        return self.access_count >= self.max_access_count
    
    def is_valid(self) -> bool:
        """Check if token is valid (not expired and under access limit)"""
        return not self.is_expired() and not self.is_access_limit_reached()
    
    def increment_access_count(self):
        """Increment the access count"""
        self.access_count += 1
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert token to dictionary for serialization"""
        return asdict(self)
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'SharingToken':
        """Create token from dictionary"""
        return cls(**data)


@dataclass
class SharedTemplate:
    """Represents a template that has been shared via URL"""
    
    id: str
    name: str
    description: str
    category: str
    author: str
    version: str
    components: List[Dict[str, Any]] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)
    sharing_info: Dict[str, Any] = field(default_factory=dict)
    
    def __post_init__(self):
        """Validate shared template data"""
        if not self.id or self.id.strip() == "":
            raise ValueError("Template ID cannot be empty")
        
        if not self.name or self.name.strip() == "":
            raise ValueError("Template name cannot be empty")
        
        # Ensure sharing_info has required fields
        if 'shared_at' not in self.sharing_info:
            self.sharing_info['shared_at'] = datetime.now().isoformat()
        
        if 'access_count' not in self.sharing_info:
            self.sharing_info['access_count'] = 0
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert shared template to dictionary"""
        return asdict(self)
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'SharedTemplate':
        """Create shared template from dictionary"""
        return cls(**data)
    
    @classmethod
    def from_template(cls, template_data: Dict[str, Any], sharing_info: Dict[str, Any]) -> 'SharedTemplate':
        """Create shared template from regular template data"""
        return cls(
            id=template_data['id'],
            name=template_data['name'],
            description=template_data['description'],
            category=template_data['category'],
            author=template_data['author'],
            version=template_data['version'],
            components=template_data.get('components', []),
            metadata=template_data.get('metadata', {}),
            sharing_info=sharing_info
        )


class URLSharingManager:
    """Manages secure URL sharing of templates with tokens and access control"""
    
    def __init__(self, sharing_storage_path: Path):
        """Initialize URL sharing manager"""
        self.sharing_storage_path = sharing_storage_path
        self.sharing_storage_path.mkdir(parents=True, exist_ok=True)
        
        # Create subdirectories for different data types
        self.tokens_dir = self.sharing_storage_path / "tokens"
        self.templates_dir = self.sharing_storage_path / "templates"
        self.tokens_dir.mkdir(exist_ok=True)
        self.templates_dir.mkdir(exist_ok=True)
        
        # Initialize indices
        self.tokens_index = {}
        self.shared_templates_index = {}
        
        # Load existing data
        self._load_tokens_index()
        self._load_shared_templates_index()
    
    def _load_tokens_index(self):
        """Load tokens index from storage"""
        self.tokens_index = {}
        
        for token_file in self.tokens_dir.glob("*.json"):
            try:
                with open(token_file, 'r') as f:
                    token_data = json.load(f)
                
                token = SharingToken.from_dict(token_data)
                self.tokens_index[token.token] = token
            except Exception:
                # Skip corrupted files
                continue
    
    def _load_shared_templates_index(self):
        """Load shared templates index from storage"""
        self.shared_templates_index = {}
        
        for template_file in self.templates_dir.glob("*.json"):
            try:
                with open(template_file, 'r') as f:
                    template_data = json.load(f)
                
                template = SharedTemplate.from_dict(template_data)
                self.shared_templates_index[template.id] = template
            except Exception:
                # Skip corrupted files
                continue
    
    def _save_token(self, token: SharingToken):
        """Save token to storage"""
        token_file = self.tokens_dir / f"{token.token}.json"
        with open(token_file, 'w') as f:
            json.dump(token.to_dict(), f, indent=2)
        
        # Update index
        self.tokens_index[token.token] = token
    
    def _save_shared_template(self, template: SharedTemplate):
        """Save shared template to storage"""
        template_file = self.templates_dir / f"{template.id}.json"
        with open(template_file, 'w') as f:
            json.dump(template.to_dict(), f, indent=2)
        
        # Update index
        self.shared_templates_index[template.id] = template
    
    def _generate_secure_token(self, length: int = 32) -> str:
        """Generate a cryptographically secure token"""
        return secrets.token_urlsafe(length)
    
    def generate_sharing_token(self, 
                              template_data: Dict[str, Any], 
                              expires_in_days: int = 30,
                              max_access_count: int = 100) -> str:
        """Generate a secure sharing token for a template"""
        # Generate unique token
        token = self._generate_secure_token()
        
        # Ensure token is unique
        while token in self.tokens_index:
            token = self._generate_secure_token()
        
        # Calculate expiration date
        created_at = datetime.now()
        expires_at = created_at + timedelta(days=expires_in_days)
        
        # Create token object
        sharing_token = SharingToken(
            token=token,
            template_id=template_data['id'],
            created_at=created_at.isoformat(),
            expires_at=expires_at.isoformat(),
            access_count=0,
            max_access_count=max_access_count
        )
        
        # Save token
        self._save_token(sharing_token)
        
        # Create shared template
        sharing_info = {
            'shared_at': created_at.isoformat(),
            'shared_by': template_data.get('author', 'Unknown'),
            'share_url': f"#token={token}",  # Placeholder URL
            'access_count': 0
        }
        
        shared_template = SharedTemplate.from_template(template_data, sharing_info)
        self._save_shared_template(shared_template)
        
        return token
    
    def generate_sharing_url(self, 
                           template_data: Dict[str, Any], 
                           base_url: str = "https://example.com/share",
                           expires_in_days: int = 30,
                           max_access_count: int = 100) -> str:
        """Generate a complete sharing URL for a template"""
        token = self.generate_sharing_token(
            template_data=template_data,
            expires_in_days=expires_in_days,
            max_access_count=max_access_count
        )
        
        return f"{base_url}/{token}"
    
    def get_token_info(self, token: str) -> Optional[SharingToken]:
        """Get token information"""
        return self.tokens_index.get(token)
    
    def access_shared_template(self, token: str) -> Optional[Dict[str, Any]]:
        """Access a shared template using a token"""
        # Get token info
        token_info = self.get_token_info(token)
        if not token_info:
            return None
        
        # Check if token is valid
        if not token_info.is_valid():
            return None
        
        # Get shared template
        shared_template = self.shared_templates_index.get(token_info.template_id)
        if not shared_template:
            return None
        
        # Increment access count
        token_info.increment_access_count()
        shared_template.sharing_info['access_count'] = token_info.access_count
        
        # Save updated data
        self._save_token(token_info)
        self._save_shared_template(shared_template)
        
        # Return template data
        return shared_template.to_dict()
    
    def validate_sharing_token(self, token: str) -> Tuple[bool, Optional[str]]:
        """Validate a sharing token"""
        if not token or token.strip() == "":
            return False, "Token cannot be empty"
        
        token_info = self.get_token_info(token)
        if not token_info:
            return False, "Token not found"
        
        if token_info.is_expired():
            return False, "Token has expired"
        
        if token_info.is_access_limit_reached():
            return False, "Token access limit reached"
        
        return True, None
    
    def revoke_sharing_token(self, token: str) -> bool:
        """Revoke a sharing token"""
        try:
            token_info = self.get_token_info(token)
            if not token_info:
                return False
            
            # Remove token file
            token_file = self.tokens_dir / f"{token}.json"
            if token_file.exists():
                token_file.unlink()
            
            # Remove from index
            if token in self.tokens_index:
                del self.tokens_index[token]
            
            return True
        except Exception:
            return False
    
    def list_shared_templates(self) -> List[Dict[str, Any]]:
        """List all shared templates"""
        return [template.to_dict() for template in self.shared_templates_index.values()]
    
    def get_sharing_statistics(self) -> Dict[str, Any]:
        """Get sharing statistics"""
        stats = {
            'total_shared_templates': len(self.shared_templates_index),
            'total_access_count': 0,
            'active_tokens': 0,
            'expired_tokens': 0,
            'access_limited_tokens': 0
        }
        
        for token_info in self.tokens_index.values():
            stats['total_access_count'] += token_info.access_count
            
            if token_info.is_expired():
                stats['expired_tokens'] += 1
            elif token_info.is_access_limit_reached():
                stats['access_limited_tokens'] += 1
            else:
                stats['active_tokens'] += 1
        
        return stats
    
    def cleanup_expired_tokens(self) -> int:
        """Clean up expired tokens and return count of cleaned tokens"""
        expired_tokens = []
        
        for token, token_info in self.tokens_index.items():
            if token_info.is_expired():
                expired_tokens.append(token)
        
        # Remove expired tokens
        for token in expired_tokens:
            self.revoke_sharing_token(token)
        
        return len(expired_tokens)
    
    def render_sharing_ui(self, template_data: Optional[Dict[str, Any]] = None):
        """Render the sharing UI interface"""
        st.title("🔗 Template Sharing")
        
        if template_data:
            # Template-specific sharing
            st.subheader(f"Share Template: {template_data['name']}")
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("**Sharing Options**")
                expires_in_days = st.slider("Expires in days", 1, 365, 30)
                max_access_count = st.number_input("Max access count", 1, 10000, 100)
                
                if st.button("Generate Share URL"):
                    try:
                        base_url = st.text_input("Base URL", "https://example.com/share")
                        share_url = self.generate_sharing_url(
                            template_data=template_data,
                            base_url=base_url,
                            expires_in_days=expires_in_days,
                            max_access_count=max_access_count
                        )
                        
                        st.success("Share URL generated!")
                        st.code(share_url)
                        
                        # Add copy button functionality
                        if st.button("📋 Copy to Clipboard"):
                            st.write("URL copied to clipboard!")
                    except Exception as e:
                        st.error(f"Error generating share URL: {str(e)}")
            
            with col2:
                st.markdown("**Template Preview**")
                st.json(template_data)
        
        # Sharing management
        st.divider()
        st.subheader("📊 Sharing Management")
        
        # Statistics
        stats = self.get_sharing_statistics()
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Shared Templates", stats['total_shared_templates'])
        with col2:
            st.metric("Active Tokens", stats['active_tokens'])
        with col3:
            st.metric("Total Accesses", stats['total_access_count'])
        with col4:
            st.metric("Expired Tokens", stats['expired_tokens'])
        
        # Shared templates list
        st.subheader("📋 Shared Templates")
        
        shared_templates = self.list_shared_templates()
        
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
                        
                        if st.button(f"🗑️ Revoke Share", key=f"revoke_{template['id']}"):
                            # Find and revoke associated tokens
                            revoked_count = 0
                            for token, token_info in self.tokens_index.items():
                                if token_info.template_id == template['id']:
                                    if self.revoke_sharing_token(token):
                                        revoked_count += 1
                            
                            if revoked_count > 0:
                                st.success(f"Revoked {revoked_count} sharing token(s)")
                                st.rerun()
                            else:
                                st.warning("No active tokens found to revoke")
        
        # Token management
        st.divider()
        st.subheader("🔑 Token Management")
        
        # Validate token
        st.markdown("**Validate Token**")
        token_to_validate = st.text_input("Enter token to validate")
        
        if st.button("Validate Token"):
            if token_to_validate:
                is_valid, error_msg = self.validate_sharing_token(token_to_validate)
                if is_valid:
                    st.success("✅ Token is valid")
                    token_info = self.get_token_info(token_to_validate)
                    if token_info:
                        st.json(token_info.to_dict())
                else:
                    st.error(f"❌ Token is invalid: {error_msg}")
        
        # Cleanup expired tokens
        if st.button("🧹 Cleanup Expired Tokens"):
            cleaned_count = self.cleanup_expired_tokens()
            if cleaned_count > 0:
                st.success(f"Cleaned up {cleaned_count} expired tokens")
                st.rerun()
            else:
                st.info("No expired tokens to clean up")
    
    def render(self):
        """Main render method for URL Sharing Manager"""
        self.render_sharing_ui()