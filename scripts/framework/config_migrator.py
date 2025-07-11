#!/usr/bin/env python3
"""
Configuration Migration Tool for Claude Code Modular Prompts Framework

Helps users migrate from hardcoded framework settings to PROJECT_CONFIG.xml
configuration system, providing automated detection and migration assistance.

Author: Claude Code Framework
Version: 1.0.0
Date: 2025-07-11
"""

import os
import json
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple
import logging
import shutil
from datetime import datetime
from config_validator import ConfigValidator
from template_resolver import TemplateResolver


class ConfigMigrator:
    """
    Migrates projects from hardcoded framework to configuration-driven framework.
    """
    
    def __init__(self, project_root: Optional[str] = None):
        """
        Initialize configuration migrator.
        
        Args:
            project_root: Path to project root directory (default: current directory)
        """
        self.project_root = Path(project_root) if project_root else Path.cwd()
        self.config_file = self.project_root / "PROJECT_CONFIG.xml"
        self.template_file = self.project_root / "PROJECT_CONFIG_TEMPLATE.md"
        
        self.logger = logging.getLogger(__name__)
        
        # Language detection patterns
        self.language_patterns = {
            'javascript': ['package.json', 'node_modules', '.js', '.jsx'],
            'typescript': ['tsconfig.json', '.ts', '.tsx', 'package.json'],
            'python': ['requirements.txt', 'setup.py', 'pyproject.toml', '.py'],
            'java': ['pom.xml', 'build.gradle', '.java'],
            'go': ['go.mod', 'go.sum', '.go'],
            'rust': ['Cargo.toml', 'Cargo.lock', '.rs'],
            'php': ['composer.json', '.php'],
            'ruby': ['Gemfile', '.rb'],
            'csharp': ['.csproj', '.sln', '.cs'],
            'swift': ['Package.swift', '.swift']
        }
        
        # Framework detection patterns
        self.framework_patterns = {
            'react': ['react', 'jsx', 'tsx'],
            'angular': ['@angular', 'angular.json'],
            'vue': ['vue', '.vue'],
            'express': ['express'],
            'django': ['django', 'manage.py'],
            'flask': ['flask'],
            'spring': ['spring-boot', '@RestController'],
            'rails': ['rails', 'Gemfile'],
            'laravel': ['laravel', 'artisan']
        }
        
        # Directory structure patterns
        self.directory_patterns = {
            'source': ['src', 'app', 'lib', 'source'],
            'test': ['test', 'tests', '__tests__', 'spec'],
            'docs': ['docs', 'doc', 'documentation'],
            'scripts': ['scripts', 'bin', 'tools'],
            'config': ['config', 'configs', 'configuration']
        }
    
    def analyze_project(self) -> Dict[str, Any]:
        """
        Analyze the current project to determine appropriate configuration.
        
        Returns:
            Dictionary containing project analysis results
        """
        analysis = {
            'project_root': str(self.project_root),
            'timestamp': datetime.now().isoformat(),
            'detected_language': None,
            'detected_frameworks': [],
            'directory_structure': {},
            'existing_config': False,
            'migration_needed': True,
            'recommendations': []
        }
        
        # Check if configuration already exists
        if self.config_file.exists():
            analysis['existing_config'] = True
            analysis['migration_needed'] = False
            analysis['recommendations'].append("PROJECT_CONFIG.xml already exists")
        
        # Detect primary language
        analysis['detected_language'] = self._detect_primary_language()
        
        # Detect frameworks
        analysis['detected_frameworks'] = self._detect_frameworks()
        
        # Analyze directory structure
        analysis['directory_structure'] = self._analyze_directory_structure()
        
        # Generate recommendations
        analysis['recommendations'].extend(self._generate_recommendations(analysis))
        
        return analysis
    
    def _detect_primary_language(self) -> Optional[str]:
        """Detect the primary programming language of the project."""
        language_scores = {}
        
        for language, patterns in self.language_patterns.items():
            score = 0
            for pattern in patterns:
                if pattern.startswith('.'):
                    # File extension pattern
                    count = len(list(self.project_root.rglob(f'*{pattern}')))
                    score += count
                else:
                    # File name pattern
                    if (self.project_root / pattern).exists():
                        score += 10
            
            if score > 0:
                language_scores[language] = score
        
        if language_scores:
            return max(language_scores, key=language_scores.get)
        return None
    
    def _detect_frameworks(self) -> List[str]:
        """Detect frameworks used in the project."""
        detected_frameworks = []
        
        # Check package.json for JavaScript/TypeScript frameworks
        package_json = self.project_root / 'package.json'
        if package_json.exists():
            try:
                import json
                with open(package_json) as f:
                    package_data = json.load(f)
                
                dependencies = {}
                dependencies.update(package_data.get('dependencies', {}))
                dependencies.update(package_data.get('devDependencies', {}))
                
                for framework, patterns in self.framework_patterns.items():
                    for pattern in patterns:
                        if any(pattern in dep for dep in dependencies.keys()):
                            detected_frameworks.append(framework)
                            break
            except Exception as e:
                self.logger.warning(f"Error reading package.json: {e}")
        
        # Check for other framework indicators
        for framework, patterns in self.framework_patterns.items():
            for pattern in patterns:
                if pattern.startswith('@') or pattern.startswith('.'):
                    continue
                
                # Check for files containing framework indicators
                for file_path in self.project_root.rglob('*.py'):
                    try:
                        with open(file_path, 'r', encoding='utf-8') as f:
                            content = f.read()
                            if pattern in content and framework not in detected_frameworks:
                                detected_frameworks.append(framework)
                                break
                    except Exception:
                        continue
                
                if framework in detected_frameworks:
                    break
        
        return detected_frameworks
    
    def _analyze_directory_structure(self) -> Dict[str, Optional[str]]:
        """Analyze project directory structure."""
        structure = {
            'source': None,
            'test': None,
            'docs': None,
            'scripts': None,
            'config': None
        }
        
        for dir_type, patterns in self.directory_patterns.items():
            for pattern in patterns:
                candidate = self.project_root / pattern
                if candidate.exists() and candidate.is_dir():
                    structure[dir_type] = pattern
                    break
        
        return structure
    
    def _generate_recommendations(self, analysis: Dict[str, Any]) -> List[str]:
        """Generate migration recommendations based on analysis."""
        recommendations = []
        
        if analysis['detected_language']:
            recommendations.append(f"Detected {analysis['detected_language']} project")
        
        if analysis['detected_frameworks']:
            frameworks = ", ".join(analysis['detected_frameworks'])
            recommendations.append(f"Detected frameworks: {frameworks}")
        
        if not analysis['directory_structure']['source']:
            recommendations.append("Consider organizing source code in a dedicated directory")
        
        if not analysis['directory_structure']['test']:
            recommendations.append("Consider creating a dedicated test directory")
        
        return recommendations
    
    def create_config_from_analysis(self, analysis: Dict[str, Any], 
                                  project_name: Optional[str] = None) -> str:
        """
        Create PROJECT_CONFIG.xml content based on project analysis.
        
        Args:
            analysis: Project analysis results
            project_name: Override project name (default: directory name)
            
        Returns:
            XML configuration content
        """
        if not project_name:
            project_name = self.project_root.name
        
        language = analysis['detected_language'] or 'javascript'
        
        # Determine domain based on detected frameworks
        domain = self._determine_domain(analysis['detected_frameworks'], language)
        
        # Get directory structure with defaults
        dirs = analysis['directory_structure']
        source_dir = dirs.get('source') or 'src'
        test_dir = dirs.get('test') or 'tests'
        docs_dir = dirs.get('docs') or 'docs'
        scripts_dir = dirs.get('scripts') or 'scripts'
        config_dir = dirs.get('config') or 'config'
        
        # Generate commands based on language and frameworks
        commands = self._generate_commands(language, analysis['detected_frameworks'])
        
        # Generate quality standards based on language
        quality_standards = self._generate_quality_standards(language)
        
        config_template = f"""<?xml version="1.0" encoding="UTF-8"?>
<!-- Generated PROJECT_CONFIG.xml for {project_name} -->
<project_configuration version="1.0.0">
  <project_info>
    <name>{project_name}</name>
    <domain>{domain}</domain>
    <description>Migrated configuration for {project_name}</description>
    <primary_language>{language}</primary_language>
    <framework_stack>{self._format_framework_stack(language, analysis['detected_frameworks'])}</framework_stack>
  </project_info>

  <project_structure>
    <root_directory>.</root_directory>
    <source_directory>{source_dir}</source_directory>
    <test_directory>{test_dir}</test_directory>
    <docs_directory>{docs_dir}</docs_directory>
    <scripts_directory>{scripts_dir}</scripts_directory>
    <config_directory>{config_dir}</config_directory>
  </project_structure>

  <quality_standards>
    <test_coverage>
      <threshold>{quality_standards['coverage_threshold']}</threshold>
      <enforcement>BLOCKING</enforcement>
      <tool>{quality_standards['coverage_tool']}</tool>
    </test_coverage>
    <performance>
      <response_time_p95>{quality_standards['response_time']}</response_time_p95>
      <memory_limit>{quality_standards['memory_limit']}</memory_limit>
    </performance>
    <code_quality>
      <linter>{quality_standards['linter']}</linter>
      <formatter>{quality_standards['formatter']}</formatter>
      <type_checker>{quality_standards['type_checker']}</type_checker>
    </code_quality>
  </quality_standards>

  <development_workflow>
    <commands>
      <install>{commands['install']}</install>
      <test>{commands['test']}</test>
      <lint>{commands['lint']}</lint>
      <build>{commands['build']}</build>
      <run>{commands['run']}</run>
      <format>{commands['format']}</format>
    </commands>
    <git_workflow>
      <branch_pattern>feature/*</branch_pattern>
      <commit_style>conventional</commit_style>
      <pr_template>enabled</pr_template>
    </git_workflow>
  </development_workflow>

  <framework_behavior>
    <file_creation_policy>conservative</file_creation_policy>
    <documentation_generation>on-request</documentation_generation>
    <test_first_enforcement>strict</test_first_enforcement>
    <ai_temperature>
      <factual>0.2</factual>
      <analysis>0.3</analysis>
      <creative>0.7</creative>
    </ai_temperature>
  </framework_behavior>
</project_configuration>"""

        return config_template
    
    def _determine_domain(self, frameworks: List[str], language: str) -> str:
        """Determine project domain based on frameworks and language."""
        if 'react' in frameworks or 'angular' in frameworks or 'vue' in frameworks:
            return 'web-development'
        elif 'django' in frameworks or 'flask' in frameworks or 'rails' in frameworks:
            return 'web-development'
        elif language == 'swift' or language == 'kotlin':
            return 'mobile-engineering'
        elif language == 'python' and any(f in str(self.project_root) for f in ['data', 'ml', 'ai']):
            return 'data-analytics'
        elif language == 'go' or language == 'rust':
            return 'platform-engineering'
        else:
            return 'web-development'
    
    def _format_framework_stack(self, language: str, frameworks: List[str]) -> str:
        """Format framework stack description."""
        if frameworks:
            return f"{language}+{'+'.join(frameworks)}"
        else:
            return language
    
    def _generate_commands(self, language: str, frameworks: List[str]) -> Dict[str, str]:
        """Generate development commands based on language and frameworks."""
        commands = {
            'javascript': {
                'install': 'npm install',
                'test': 'npm test',
                'lint': 'npm run lint',
                'build': 'npm run build',
                'run': 'npm start',
                'format': 'npm run format'
            },
            'typescript': {
                'install': 'npm install',
                'test': 'npm test',
                'lint': 'npm run lint',
                'build': 'npm run build',
                'run': 'npm start',
                'format': 'npm run format'
            },
            'python': {
                'install': 'pip install -r requirements.txt',
                'test': 'pytest',
                'lint': 'pylint src/',
                'build': 'python setup.py build',
                'run': 'python -m src.main',
                'format': 'black .'
            },
            'java': {
                'install': 'mvn install',
                'test': 'mvn test',
                'lint': 'mvn checkstyle:check',
                'build': 'mvn package',
                'run': 'mvn spring-boot:run',
                'format': 'mvn fmt:format'
            },
            'go': {
                'install': 'go mod download',
                'test': 'go test ./...',
                'lint': 'golangci-lint run',
                'build': 'go build',
                'run': 'go run .',
                'format': 'gofmt -w .'
            }
        }
        
        return commands.get(language, commands['javascript'])
    
    def _generate_quality_standards(self, language: str) -> Dict[str, str]:
        """Generate quality standards based on language."""
        standards = {
            'javascript': {
                'coverage_threshold': '85',
                'coverage_tool': 'jest',
                'response_time': '200ms',
                'memory_limit': '512MB',
                'linter': 'eslint',
                'formatter': 'prettier',
                'type_checker': 'none'
            },
            'typescript': {
                'coverage_threshold': '90',
                'coverage_tool': 'jest',
                'response_time': '200ms',
                'memory_limit': '512MB',
                'linter': 'eslint',
                'formatter': 'prettier',
                'type_checker': 'typescript'
            },
            'python': {
                'coverage_threshold': '85',
                'coverage_tool': 'pytest-cov',
                'response_time': '500ms',
                'memory_limit': '1GB',
                'linter': 'pylint',
                'formatter': 'black',
                'type_checker': 'mypy'
            },
            'java': {
                'coverage_threshold': '80',
                'coverage_tool': 'jacoco',
                'response_time': '300ms',
                'memory_limit': '1GB',
                'linter': 'checkstyle',
                'formatter': 'google-java-format',
                'type_checker': 'javac'
            },
            'go': {
                'coverage_threshold': '90',
                'coverage_tool': 'go-cover',
                'response_time': '100ms',
                'memory_limit': '256MB',
                'linter': 'golangci-lint',
                'formatter': 'gofmt',
                'type_checker': 'go'
            }
        }
        
        return standards.get(language, standards['javascript'])
    
    def migrate_project(self, project_name: Optional[str] = None, 
                       dry_run: bool = False) -> Dict[str, Any]:
        """
        Perform complete project migration to configuration-driven framework.
        
        Args:
            project_name: Override project name
            dry_run: If True, don't actually create files
            
        Returns:
            Migration results dictionary
        """
        result = {
            'success': False,
            'analysis': {},
            'config_created': False,
            'backup_created': False,
            'validation_passed': False,
            'errors': [],
            'warnings': []
        }
        
        try:
            # Step 1: Analyze project
            self.logger.info("Analyzing project structure...")
            analysis = self.analyze_project()
            result['analysis'] = analysis
            
            if analysis['existing_config']:
                result['warnings'].append("PROJECT_CONFIG.xml already exists")
                if not dry_run:
                    return result
            
            # Step 2: Create backup if files exist
            if not dry_run and self.config_file.exists():
                backup_path = self.config_file.with_suffix('.xml.backup')
                shutil.copy2(self.config_file, backup_path)
                result['backup_created'] = True
                self.logger.info(f"Created backup at {backup_path}")
            
            # Step 3: Generate configuration
            self.logger.info("Generating PROJECT_CONFIG.xml...")
            config_content = self.create_config_from_analysis(analysis, project_name)
            
            if not dry_run:
                with open(self.config_file, 'w', encoding='utf-8') as f:
                    f.write(config_content)
                result['config_created'] = True
                self.logger.info(f"Created {self.config_file}")
            
            # Step 4: Validate configuration
            if not dry_run:
                validator = ConfigValidator(project_root=str(self.project_root))
                validation_result = validator.validate()
                result['validation_passed'] = validation_result['valid']
                
                if validation_result['errors']:
                    result['errors'].extend(validation_result['errors'])
                if validation_result['warnings']:
                    result['warnings'].extend(validation_result['warnings'])
            
            result['success'] = True
            self.logger.info("Migration completed successfully")
            
        except Exception as e:
            result['errors'].append(f"Migration failed: {e}")
            self.logger.error(f"Migration error: {e}")
        
        return result
    
    def create_migration_report(self, migration_result: Dict[str, Any]) -> str:
        """
        Create a comprehensive migration report.
        
        Args:
            migration_result: Results from migrate_project()
            
        Returns:
            Markdown report content
        """
        analysis = migration_result.get('analysis', {})
        
        report = f"""# Project Migration Report

**Project:** {self.project_root.name}  
**Date:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}  
**Status:** {'✅ SUCCESS' if migration_result['success'] else '❌ FAILED'}

## Project Analysis

**Detected Language:** {analysis.get('detected_language', 'Unknown')}  
**Detected Frameworks:** {', '.join(analysis.get('detected_frameworks', []))}  

### Directory Structure
"""
        
        dirs = analysis.get('directory_structure', {})
        for dir_type, path in dirs.items():
            status = '✅' if path else '❌'
            report += f"- **{dir_type.title()}:** {status} {path or 'Not found'}\n"
        
        report += f"""
## Migration Results

- **Configuration Created:** {'✅' if migration_result.get('config_created') else '❌'}
- **Backup Created:** {'✅' if migration_result.get('backup_created') else '❌'}
- **Validation Passed:** {'✅' if migration_result.get('validation_passed') else '❌'}
"""
        
        if migration_result.get('errors'):
            report += "\n### Errors\n"
            for error in migration_result['errors']:
                report += f"- ❌ {error}\n"
        
        if migration_result.get('warnings'):
            report += "\n### Warnings\n"
            for warning in migration_result['warnings']:
                report += f"- ⚠️ {warning}\n"
        
        recommendations = analysis.get('recommendations', [])
        if recommendations:
            report += "\n### Recommendations\n"
            for rec in recommendations:
                report += f"- 💡 {rec}\n"
        
        report += f"""
## Next Steps

1. **Review Configuration:** Check PROJECT_CONFIG.xml and adjust values as needed
2. **Test Framework:** Run framework commands to ensure they work with new configuration
3. **Update Documentation:** Document any project-specific configuration requirements
4. **Commit Changes:** Add PROJECT_CONFIG.xml to version control

## Configuration File

The PROJECT_CONFIG.xml file has been created at:  
`{self.config_file}`

This file can be customized to match your project's specific requirements.
"""
        
        return report


def main():
    """CLI interface for configuration migration."""
    import argparse
    
    parser = argparse.ArgumentParser(description="Configuration Migration Tool")
    parser.add_argument('--project-root', help="Project root directory")
    parser.add_argument('--analyze', action='store_true', help="Analyze project only")
    parser.add_argument('--migrate', action='store_true', help="Perform migration")
    parser.add_argument('--project-name', help="Override project name")
    parser.add_argument('--dry-run', action='store_true', help="Dry run (don't create files)")
    parser.add_argument('--report', help="Generate migration report to file")
    parser.add_argument('--verbose', '-v', action='store_true', help="Verbose output")
    
    args = parser.parse_args()
    
    # Setup logging
    level = logging.DEBUG if args.verbose else logging.INFO
    logging.basicConfig(level=level, format='%(levelname)s: %(message)s')
    
    migrator = ConfigMigrator(project_root=args.project_root)
    
    try:
        if args.analyze:
            analysis = migrator.analyze_project()
            print(json.dumps(analysis, indent=2))
        
        elif args.migrate:
            result = migrator.migrate_project(
                project_name=args.project_name,
                dry_run=args.dry_run
            )
            
            if args.report:
                report = migrator.create_migration_report(result)
                with open(args.report, 'w') as f:
                    f.write(report)
                print(f"Migration report saved to {args.report}")
            
            print(f"Migration {'completed' if result['success'] else 'failed'}")
            if result['errors']:
                for error in result['errors']:
                    print(f"ERROR: {error}")
        
        else:
            parser.print_help()
    
    except Exception as e:
        logging.error(f"Error: {e}")
        return 1
    
    return 0


if __name__ == "__main__":
    exit(main())