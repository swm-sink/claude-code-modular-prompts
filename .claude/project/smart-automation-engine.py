#!/usr/bin/env python3
"""
Smart Automation Engine
Intelligent placeholder replacement system with project context detection
Phase 3 - Smart Automation Implementation
"""

import os
import re
import json
import logging
from pathlib import Path
from typing import Dict, List, Set, Optional, Any
import subprocess

# Configure logging
logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(levelname)s: %(message)s', datefmt='%H:%M:%S')

class ProjectContextDetector:
    """Detects project context for smart placeholder replacement"""
    
    def __init__(self, project_path: str = "."):
        self.project_path = Path(project_path).resolve()
        
    def detect_project_metadata(self) -> Dict[str, str]:
        """Detect project name, organization, and basic metadata"""
        metadata = {}
        
        # Try package.json (Node.js/JavaScript)
        package_json = self.project_path / "package.json"
        if package_json.exists():
            try:
                with open(package_json) as f:
                    data = json.load(f)
                    metadata['project_name'] = data.get('name', '')
                    metadata['description'] = data.get('description', '')
                    if 'author' in data:
                        author = data['author']
                        if isinstance(author, str):
                            metadata['author'] = author
                        elif isinstance(author, dict):
                            metadata['author'] = author.get('name', '')
                    metadata['version'] = data.get('version', '')
            except Exception as e:
                logging.warning(f"Error reading package.json: {e}")
        
        # Try setup.py or pyproject.toml (Python)
        setup_py = self.project_path / "setup.py"
        pyproject_toml = self.project_path / "pyproject.toml"
        
        if setup_py.exists():
            try:
                content = setup_py.read_text()
                # Extract name from setup() call
                name_match = re.search(r'name=["\']([^"\']+)["\']', content)
                if name_match:
                    metadata['project_name'] = name_match.group(1)
            except Exception as e:
                logging.warning(f"Error reading setup.py: {e}")
        
        # Try Cargo.toml (Rust)
        cargo_toml = self.project_path / "Cargo.toml"
        if cargo_toml.exists():
            try:
                content = cargo_toml.read_text()
                name_match = re.search(r'name\s*=\s*["\']([^"\']+)["\']', content)
                if name_match:
                    metadata['project_name'] = name_match.group(1)
            except Exception as e:
                logging.warning(f"Error reading Cargo.toml: {e}")
        
        # Try git config for organization/author
        try:
            git_user = subprocess.run(['git', 'config', 'user.name'], 
                                    capture_output=True, text=True, cwd=self.project_path)
            if git_user.returncode == 0:
                metadata['git_user'] = git_user.stdout.strip()
                
            git_email = subprocess.run(['git', 'config', 'user.email'], 
                                     capture_output=True, text=True, cwd=self.project_path)
            if git_email.returncode == 0:
                metadata['git_email'] = git_email.stdout.strip()
                # Extract organization from email domain
                email = git_email.stdout.strip()
                if '@' in email:
                    domain = email.split('@')[1]
                    if domain not in ['gmail.com', 'yahoo.com', 'hotmail.com', 'outlook.com']:
                        metadata['organization'] = domain.split('.')[0].title()
        except Exception as e:
            logging.warning(f"Error reading git config: {e}")
        
        # Try directory name as fallback for project name
        if 'project_name' not in metadata:
            metadata['project_name'] = self.project_path.name
        
        return metadata
    
    def detect_technology_stack(self) -> Dict[str, Any]:
        """Detect technology stack and frameworks"""
        tech_stack = {
            'languages': [],
            'frameworks': [],
            'platforms': [],
            'databases': [],
            'testing_frameworks': [],
            'ci_cd_platform': '',
            'deployment_target': ''
        }
        
        # Language detection by file extensions
        file_extensions = {}
        for file_path in self.project_path.rglob("*"):
            if file_path.is_file() and file_path.suffix:
                ext = file_path.suffix.lower()
                file_extensions[ext] = file_extensions.get(ext, 0) + 1
        
        # Map extensions to languages
        language_map = {
            '.py': 'Python',
            '.js': 'JavaScript',
            '.ts': 'TypeScript',
            '.jsx': 'React/JavaScript',
            '.tsx': 'React/TypeScript',
            '.rs': 'Rust',
            '.go': 'Go',
            '.java': 'Java',
            '.cpp': 'C++',
            '.c': 'C',
            '.php': 'PHP',
            '.rb': 'Ruby',
            '.swift': 'Swift',
            '.kt': 'Kotlin',
            '.dart': 'Dart',
            '.cs': 'C#'
        }
        
        for ext, count in file_extensions.items():
            if ext in language_map and count > 2:  # At least 3 files
                tech_stack['languages'].append(language_map[ext])
        
        # Framework detection from package files
        package_json = self.project_path / "package.json"
        if package_json.exists():
            try:
                with open(package_json) as f:
                    data = json.load(f)
                    deps = {**data.get('dependencies', {}), **data.get('devDependencies', {})}
                    
                    # Framework detection
                    if 'react' in deps:
                        tech_stack['frameworks'].append('React')
                    if 'vue' in deps:
                        tech_stack['frameworks'].append('Vue.js')
                    if 'angular' in deps or '@angular/core' in deps:
                        tech_stack['frameworks'].append('Angular')
                    if 'express' in deps:
                        tech_stack['frameworks'].append('Express.js')
                    if 'next' in deps:
                        tech_stack['frameworks'].append('Next.js')
                    if 'svelte' in deps:
                        tech_stack['frameworks'].append('Svelte')
                    
                    # Testing frameworks
                    if 'jest' in deps:
                        tech_stack['testing_frameworks'].append('Jest')
                    if 'mocha' in deps:
                        tech_stack['testing_frameworks'].append('Mocha')
                    if 'vitest' in deps:
                        tech_stack['testing_frameworks'].append('Vitest')
                    if 'cypress' in deps:
                        tech_stack['testing_frameworks'].append('Cypress')
                    
                    # Database libraries
                    if 'mongoose' in deps:
                        tech_stack['databases'].append('MongoDB')
                    if 'pg' in deps or 'postgres' in deps:
                        tech_stack['databases'].append('PostgreSQL')
                    if 'mysql' in deps:
                        tech_stack['databases'].append('MySQL')
                    if 'redis' in deps:
                        tech_stack['databases'].append('Redis')
            except Exception as e:
                logging.warning(f"Error analyzing package.json: {e}")
        
        # Python requirements analysis
        requirements_files = ['requirements.txt', 'requirements.in', 'pyproject.toml']
        for req_file in requirements_files:
            req_path = self.project_path / req_file
            if req_path.exists():
                try:
                    content = req_path.read_text().lower()
                    if 'django' in content:
                        tech_stack['frameworks'].append('Django')
                    if 'flask' in content:
                        tech_stack['frameworks'].append('Flask')
                    if 'fastapi' in content:
                        tech_stack['frameworks'].append('FastAPI')
                    if 'pytest' in content:
                        tech_stack['testing_frameworks'].append('pytest')
                    if 'sqlalchemy' in content:
                        tech_stack['databases'].append('SQLAlchemy')
                except Exception as e:
                    logging.warning(f"Error reading {req_file}: {e}")
        
        # CI/CD platform detection
        if (self.project_path / ".github" / "workflows").exists():
            tech_stack['ci_cd_platform'] = 'GitHub Actions'
        elif (self.project_path / ".gitlab-ci.yml").exists():
            tech_stack['ci_cd_platform'] = 'GitLab CI'
        elif (self.project_path / "Jenkinsfile").exists():
            tech_stack['ci_cd_platform'] = 'Jenkins'
        elif (self.project_path / ".circleci").exists():
            tech_stack['ci_cd_platform'] = 'CircleCI'
        
        # Deployment target detection
        if (self.project_path / "Dockerfile").exists():
            tech_stack['deployment_target'] = 'Docker'
        if (self.project_path / "vercel.json").exists():
            tech_stack['deployment_target'] = 'Vercel'
        if (self.project_path / "netlify.toml").exists():
            tech_stack['deployment_target'] = 'Netlify'
        
        return tech_stack
    
    def detect_domain_context(self) -> Dict[str, str]:
        """Detect domain-specific context from project structure and content"""
        context = {}
        
        # Analyze directory structure
        directories = [d.name.lower() for d in self.project_path.iterdir() if d.is_dir()]
        
        # Domain detection patterns
        if any(d in directories for d in ['components', 'pages', 'public', 'static']):
            context['domain'] = 'web-development'
        elif any(d in directories for d in ['notebooks', 'data', 'models', 'analysis']):
            context['domain'] = 'data-science'
        elif any(d in directories for d in ['src', 'lib', 'bin', 'include']):
            context['domain'] = 'software-development'
        elif any(d in directories for d in ['api', 'routes', 'controllers', 'middleware']):
            context['domain'] = 'backend-development'
        
        # Workflow type detection
        if 'tests' in directories or 'test' in directories:
            context['workflow_type'] = 'test-driven'
        if any(d in directories for d in ['ci', 'deploy', 'scripts']):
            context['workflow_type'] = 'devops-focused'
        
        return context

class SmartPlaceholderReplacer:
    """Intelligent placeholder replacement engine"""
    
    def __init__(self, project_path: str = "."):
        self.detector = ProjectContextDetector(project_path)
        self.replacement_cache = {}
        
    def generate_replacement_map(self) -> Dict[str, str]:
        """Generate comprehensive replacement map from project analysis"""
        if self.replacement_cache:
            return self.replacement_cache
        
        logging.info("🔍 Analyzing project context...")
        
        metadata = self.detector.detect_project_metadata()
        tech_stack = self.detector.detect_technology_stack()
        domain_context = self.detector.detect_domain_context()
        
        replacement_map = {}
        
        # Project metadata replacements (90% automation potential)
        if 'project_name' in metadata:
            replacement_map['[INSERT_PROJECT_NAME]'] = metadata['project_name']
        if 'organization' in metadata:
            replacement_map['[INSERT_COMPANY_NAME]'] = metadata['organization']
        elif 'git_user' in metadata:
            replacement_map['[INSERT_COMPANY_NAME]'] = metadata['git_user']
        
        # Technology stack replacements (80% automation potential)
        if tech_stack['languages']:
            primary_lang = tech_stack['languages'][0]
            replacement_map['[INSERT_TECH_STACK]'] = ', '.join(tech_stack['languages'])
            replacement_map['[INSERT_PRIMARY_LANGUAGE]'] = primary_lang
        
        if tech_stack['frameworks']:
            replacement_map['[INSERT_FRAMEWORK]'] = tech_stack['frameworks'][0]
        
        if tech_stack['testing_frameworks']:
            replacement_map['[INSERT_TESTING_FRAMEWORK]'] = tech_stack['testing_frameworks'][0]
        else:
            # Smart defaults based on language
            if 'python' in str(tech_stack['languages']).lower():
                replacement_map['[INSERT_TESTING_FRAMEWORK]'] = 'pytest'
            elif 'javascript' in str(tech_stack['languages']).lower() or 'typescript' in str(tech_stack['languages']).lower():
                replacement_map['[INSERT_TESTING_FRAMEWORK]'] = 'Jest'
            else:
                replacement_map['[INSERT_TESTING_FRAMEWORK]'] = 'Unit Testing'
        
        if tech_stack['ci_cd_platform']:
            replacement_map['[INSERT_CI_CD_PLATFORM]'] = tech_stack['ci_cd_platform']
        
        if tech_stack['databases']:
            replacement_map['[INSERT_DATABASE_TYPE]'] = tech_stack['databases'][0]
        
        if tech_stack['deployment_target']:
            replacement_map['[INSERT_DEPLOYMENT_TARGET]'] = tech_stack['deployment_target']
        
        # Domain-specific replacements (50% automation potential)
        if 'domain' in domain_context:
            replacement_map['[INSERT_DOMAIN]'] = domain_context['domain']
        else:
            replacement_map['[INSERT_DOMAIN]'] = 'software-development'  # Smart default
        
        if 'workflow_type' in domain_context:
            replacement_map['[INSERT_WORKFLOW_TYPE]'] = domain_context['workflow_type']
        else:
            replacement_map['[INSERT_WORKFLOW_TYPE]'] = 'agile-development'  # Smart default
        
        # Enhanced smart defaults for common placeholders (many were missing)
        replacement_map['[INSERT_ENVIRONMENT]'] = 'development'
        replacement_map['[INSERT_PORT]'] = '3000'
        replacement_map['[INSERT_API_VERSION]'] = 'v1'
        replacement_map['[INSERT_SECURITY_LEVEL]'] = 'standard'
        replacement_map['[INSERT_USER_BASE]'] = 'developers'
        replacement_map['[INSERT_PERFORMANCE_LEVEL]'] = 'standard'
        replacement_map['[INSERT_SCALABILITY_LEVEL]'] = 'medium'
        replacement_map['[INSERT_MONITORING_LEVEL]'] = 'basic'
        replacement_map['[INSERT_BACKUP_FREQUENCY]'] = 'daily'
        replacement_map['[INSERT_RETENTION_PERIOD]'] = '30 days'
        replacement_map['[INSERT_COMPLIANCE_LEVEL]'] = 'standard'
        replacement_map['[INSERT_ACCESS_LEVEL]'] = 'team-based'
        replacement_map['[INSERT_INTEGRATION_TYPE]'] = 'REST API'
        replacement_map['[INSERT_NOTIFICATION_CHANNEL]'] = 'email'
        replacement_map['[INSERT_LOG_LEVEL]'] = 'info'
        replacement_map['[INSERT_CACHE_STRATEGY]'] = 'memory'
        replacement_map['[INSERT_SESSION_TIMEOUT]'] = '30 minutes'
        replacement_map['[INSERT_REQUEST_TIMEOUT]'] = '30 seconds'
        replacement_map['[INSERT_MAX_CONNECTIONS]'] = '100'
        replacement_map['[INSERT_RATE_LIMIT]'] = '1000/hour'
        replacement_map['[INSERT_API_STYLE]'] = 'RESTful'
        replacement_map['[INSERT_PERFORMANCE_PRIORITY]'] = 'balanced'
        replacement_map['[INSERT_CLOUD_PROVIDER]'] = 'AWS'
        replacement_map['[INSERT_COMPLIANCE_REQUIREMENTS]'] = 'basic'
        replacement_map['[INSERT_DATA_RETENTION]'] = '1 year'
        replacement_map['[INSERT_ENCRYPTION_LEVEL]'] = 'AES-256'
        replacement_map['[INSERT_AUTHENTICATION_METHOD]'] = 'OAuth2'
        replacement_map['[INSERT_AUTHORIZATION_STRATEGY]'] = 'role-based'
        replacement_map['[INSERT_ERROR_HANDLING_STRATEGY]'] = 'graceful-degradation'
        replacement_map['[INSERT_VALIDATION_STRATEGY]'] = 'strict'
        replacement_map['[INSERT_CONCURRENCY_MODEL]'] = 'async'
        replacement_map['[INSERT_SCALING_STRATEGY]'] = 'horizontal'
        replacement_map['[INSERT_LOAD_BALANCING]'] = 'round-robin'
        replacement_map['[INSERT_HEALTH_CHECK_INTERVAL]'] = '30 seconds'
        replacement_map['[INSERT_METRICS_COLLECTION]'] = 'enabled'
        replacement_map['[INSERT_ALERTING_THRESHOLD]'] = '95%'
        replacement_map['[INSERT_DOCUMENTATION_FORMAT]'] = 'Markdown'
        replacement_map['[INSERT_VERSION_CONTROL_STRATEGY]'] = 'Git Flow'
        replacement_map['[INSERT_BRANCHING_STRATEGY]'] = 'feature-branch'
        replacement_map['[INSERT_MERGE_STRATEGY]'] = 'squash-merge'
        replacement_map['[INSERT_RELEASE_STRATEGY]'] = 'semantic-versioning'
        replacement_map['[INSERT_ROLLBACK_STRATEGY]'] = 'blue-green'
        replacement_map['[INSERT_CONFIGURATION_FORMAT]'] = 'YAML'
        replacement_map['[INSERT_SECRET_MANAGEMENT]'] = 'environment-variables'
        replacement_map['[INSERT_CONTAINER_RUNTIME]'] = 'Docker'
        replacement_map['[INSERT_ORCHESTRATION_PLATFORM]'] = 'Kubernetes'
        replacement_map['[INSERT_SERVICE_MESH]'] = 'Istio'
        replacement_map['[INSERT_MESSAGE_QUEUE]'] = 'Redis'
        replacement_map['[INSERT_SEARCH_ENGINE]'] = 'Elasticsearch'
        replacement_map['[INSERT_CDN_PROVIDER]'] = 'CloudFlare'
        replacement_map['[INSERT_DNS_PROVIDER]'] = 'CloudFlare'
        replacement_map['[INSERT_SSL_PROVIDER]'] = 'Let\'s Encrypt'
        replacement_map['[INSERT_MONITORING_TOOL]'] = 'Prometheus'
        replacement_map['[INSERT_LOGGING_TOOL]'] = 'Winston'
        replacement_map['[INSERT_APM_TOOL]'] = 'New Relic'
        replacement_map['[INSERT_MONITORING_PLATFORM]'] = 'Prometheus'
        replacement_map['[INSERT_TEST_FRAMEWORK]'] = replacement_map.get('[INSERT_TESTING_FRAMEWORK]', 'Unit Testing')
        replacement_map['[INSERT_CODE_STYLE]'] = 'PEP8' if 'python' in str(tech_stack['languages']).lower() else 'Standard'
        replacement_map['[INSERT_PROJECT_TYPE]'] = 'web-application'
        replacement_map['[INSERT_XXX]'] = 'placeholder'  # Generic fallback
        replacement_map['[INSERT_BUILD_TOOL]'] = 'npm' if 'javascript' in str(tech_stack['languages']).lower() else 'make'
        replacement_map['[INSERT_PACKAGE_MANAGER]'] = 'npm' if 'javascript' in str(tech_stack['languages']).lower() else 'pip'
        replacement_map['[INSERT_DEPENDENCY_MANAGER]'] = 'package.json' if 'javascript' in str(tech_stack['languages']).lower() else 'requirements.txt'
        replacement_map['[INSERT_RUNTIME_VERSION]'] = 'latest'
        replacement_map['[INSERT_NODE_VERSION]'] = '18' if 'javascript' in str(tech_stack['languages']).lower() else 'N/A'
        replacement_map['[INSERT_PYTHON_VERSION]'] = '3.9' if 'python' in str(tech_stack['languages']).lower() else 'N/A'
        
        # Team size default (user preference - 20% automation)
        replacement_map['[INSERT_TEAM_SIZE]'] = '1-5 developers'
        
        # Enhanced technology stack defaults based on common patterns
        if not tech_stack['ci_cd_platform']:
            replacement_map['[INSERT_CI_CD_PLATFORM]'] = 'GitHub Actions'  # Most common default
        
        if not tech_stack['databases']:
            if 'javascript' in str(tech_stack['languages']).lower():
                replacement_map['[INSERT_DATABASE_TYPE]'] = 'MongoDB'
            elif 'python' in str(tech_stack['languages']).lower():
                replacement_map['[INSERT_DATABASE_TYPE]'] = 'PostgreSQL'
            else:
                replacement_map['[INSERT_DATABASE_TYPE]'] = 'SQLite'
        
        if not tech_stack['deployment_target']:
            if tech_stack['frameworks'] and any('react' in f.lower() for f in tech_stack['frameworks']):
                replacement_map['[INSERT_DEPLOYMENT_TARGET]'] = 'Vercel'
            elif 'docker' in str(tech_stack).lower():
                replacement_map['[INSERT_DEPLOYMENT_TARGET]'] = 'Docker'
            else:
                replacement_map['[INSERT_DEPLOYMENT_TARGET]'] = 'Cloud Server'
        
        self.replacement_cache = replacement_map
        
        logging.info(f"✅ Generated {len(replacement_map)} automatic replacements")
        return replacement_map
    
    def replace_placeholders_in_content(self, content: str, replacement_map: Dict[str, str]) -> str:
        """Replace placeholders in content using replacement map"""
        modified_content = content
        replacements_made = 0
        
        for placeholder, replacement in replacement_map.items():
            if placeholder in modified_content:
                modified_content = modified_content.replace(placeholder, replacement)
                replacements_made += 1
        
        return modified_content, replacements_made
    
    def process_command_file(self, file_path: Path, replacement_map: Dict[str, str]) -> Dict[str, Any]:
        """Process a single command file with smart replacements"""
        try:
            original_content = file_path.read_text()
            modified_content, replacements_made = self.replace_placeholders_in_content(
                original_content, replacement_map
            )
            
            # Count total placeholders for automation percentage
            total_placeholders = len(re.findall(r'\[INSERT_[A-Z_]+\]', original_content))
            automation_percentage = (replacements_made / total_placeholders * 100) if total_placeholders > 0 else 0
            
            return {
                'file_path': str(file_path),
                'original_content': original_content,
                'modified_content': modified_content,
                'total_placeholders': total_placeholders,
                'replacements_made': replacements_made,
                'automation_percentage': automation_percentage,
                'fully_automated': replacements_made == total_placeholders
            }
        except Exception as e:
            logging.error(f"Error processing {file_path}: {e}")
            return None
    
    def calculate_overall_automation(self, results: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Calculate overall automation statistics"""
        total_placeholders = sum(r['total_placeholders'] for r in results if r)
        total_replacements = sum(r['replacements_made'] for r in results if r)
        
        automation_percentage = (total_replacements / total_placeholders * 100) if total_placeholders > 0 else 0
        
        fully_automated_files = sum(1 for r in results if r and r['fully_automated'])
        partially_automated_files = sum(1 for r in results if r and r['replacements_made'] > 0 and not r['fully_automated'])
        non_automated_files = sum(1 for r in results if r and r['replacements_made'] == 0)
        
        return {
            'total_placeholders': total_placeholders,
            'total_replacements': total_replacements,
            'automation_percentage': automation_percentage,
            'fully_automated_files': fully_automated_files,
            'partially_automated_files': partially_automated_files,
            'non_automated_files': non_automated_files,
            'target_achieved': automation_percentage >= 70
        }

def main():
    """Main automation engine execution"""
    logging.info("🚀 SMART AUTOMATION ENGINE")
    logging.info("=" * 60)
    
    # Initialize automation system
    replacer = SmartPlaceholderReplacer()
    
    # Generate replacement map
    replacement_map = replacer.generate_replacement_map()
    
    # Display detected context
    print(f"\n🔍 DETECTED PROJECT CONTEXT")
    print(f"=" * 50)
    for placeholder, replacement in replacement_map.items():
        print(f"{placeholder} → {replacement}")
    
    print(f"\n📊 AUTOMATION SUMMARY")
    print(f"=" * 50)
    print(f"Automatic Replacements Available: {len(replacement_map)}")
    print(f"Ready for Smart Automation: ✅")
    
    return replacement_map

if __name__ == "__main__":
    main()