#!/usr/bin/env python3
"""
Project Initialization Wizard for Claude Code Framework

Comprehensive project setup automation that:
- Analyzes existing project structure
- Detects tech stack automatically  
- Generates appropriate PROJECT_CONFIG.xml
- Sets up development environment
- Configures quality gates and testing
- Initializes framework files

Author: Claude Code Framework - Phase 2.2 Automation
Version: 1.0.0
Date: 2025-07-15
"""

import os
import sys
import json
import shutil
import subprocess
from pathlib import Path
from typing import Dict, List, Optional, Tuple
import argparse
import logging
from dataclasses import dataclass, asdict


@dataclass
class ProjectAnalysis:
    """Results of project structure analysis"""
    name: str
    root_path: Path
    tech_stack: Dict[str, str]
    existing_files: List[str]
    dependencies: Dict[str, List[str]]
    project_type: str
    confidence_score: float
    recommendations: List[str]


@dataclass 
class InitializationConfig:
    """Configuration for project initialization"""
    project_name: str
    domain: str
    primary_language: str
    framework: str
    database: str
    testing_framework: str
    setup_git_hooks: bool = True
    create_directories: bool = True
    generate_examples: bool = True
    configure_quality_gates: bool = True


class TechStackDetector:
    """Automatically detects project technology stack"""
    
    LANGUAGE_PATTERNS = {
        'python': ['requirements.txt', 'pyproject.toml', 'setup.py', 'Pipfile', '*.py'],
        'javascript': ['package.json', 'yarn.lock', 'package-lock.json', '*.js'],
        'typescript': ['tsconfig.json', '*.ts', '*.tsx'],
        'java': ['pom.xml', 'build.gradle', '*.java'],
        'go': ['go.mod', 'go.sum', '*.go'],
        'rust': ['Cargo.toml', 'Cargo.lock', '*.rs'],
        'php': ['composer.json', '*.php'],
        'ruby': ['Gemfile', 'Gemfile.lock', '*.rb'],
        'swift': ['Package.swift', '*.swift'],
        'kotlin': ['*.kt', '*.kts'],
        'csharp': ['*.csproj', '*.cs'],
        'cpp': ['CMakeLists.txt', 'Makefile', '*.cpp', '*.hpp']
    }
    
    FRAMEWORK_PATTERNS = {
        'python': {
            'django': ['manage.py', 'settings.py', 'urls.py'],
            'flask': ['app.py', 'flask'],
            'fastapi': ['fastapi', 'main.py'],
            'pytest': ['pytest.ini', 'conftest.py']
        },
        'javascript': {
            'react': ['src/App.js', 'public/index.html', 'react'],
            'vue': ['vue.config.js', 'src/main.js', 'vue'],
            'angular': ['angular.json', 'src/app'],
            'express': ['app.js', 'server.js', 'express'],
            'nextjs': ['next.config.js', 'pages/']
        },
        'typescript': {
            'react': ['src/App.tsx', 'react'],
            'angular': ['angular.json', '@angular'],
            'nestjs': ['nest-cli.json', '@nestjs']
        }
    }
    
    DATABASE_PATTERNS = {
        'postgresql': ['postgresql', 'psycopg2', 'pg'],
        'mysql': ['mysql', 'pymysql', 'mysql2'],
        'mongodb': ['mongodb', 'mongoose', 'pymongo'],
        'sqlite': ['sqlite3', 'sqlite'],
        'redis': ['redis', 'redis-py']
    }
    
    def __init__(self, project_root: Path):
        self.project_root = project_root
        self.logger = logging.getLogger(__name__)
    
    def detect_language(self) -> Tuple[str, float]:
        """Detect primary programming language with confidence score"""
        language_scores = {}
        
        for language, patterns in self.LANGUAGE_PATTERNS.items():
            score = 0
            for pattern in patterns:
                if pattern.startswith('*.'):
                    # File extension pattern
                    ext = pattern[1:]
                    count = len(list(self.project_root.glob(f"**/*{ext}")))
                    score += count * 0.1
                else:
                    # Specific file pattern
                    if (self.project_root / pattern).exists():
                        score += 1.0
                    # Check in subdirectories too
                    matches = list(self.project_root.glob(f"**/{pattern}"))
                    score += len(matches) * 0.5
            
            if score > 0:
                language_scores[language] = score
        
        if not language_scores:
            return 'python', 0.1  # Default fallback
        
        primary_language = max(language_scores, key=language_scores.get)
        confidence = min(language_scores[primary_language] / 3.0, 1.0)
        
        return primary_language, confidence
    
    def detect_framework(self, language: str) -> Tuple[str, float]:
        """Detect framework for given language"""
        if language not in self.FRAMEWORK_PATTERNS:
            return 'generic', 0.1
        
        framework_scores = {}
        
        for framework, patterns in self.FRAMEWORK_PATTERNS[language].items():
            score = 0
            for pattern in patterns:
                if (self.project_root / pattern).exists():
                    score += 1.0
                
                # Check package.json or requirements for dependencies
                if self._check_dependency(pattern, language):
                    score += 0.5
                
                # Check in subdirectories
                matches = list(self.project_root.glob(f"**/{pattern}"))
                score += len(matches) * 0.3
            
            if score > 0:
                framework_scores[framework] = score
        
        if not framework_scores:
            return 'generic', 0.1
        
        primary_framework = max(framework_scores, key=framework_scores.get)
        confidence = min(framework_scores[primary_framework] / 2.0, 1.0)
        
        return primary_framework, confidence
    
    def detect_database(self) -> Tuple[str, float]:
        """Detect database technology"""
        database_scores = {}
        
        for database, patterns in self.DATABASE_PATTERNS.items():
            score = 0
            for pattern in patterns:
                if self._check_dependency(pattern, None):
                    score += 1.0
            
            if score > 0:
                database_scores[database] = score
        
        if not database_scores:
            return 'sqlite', 0.1  # Default fallback
        
        primary_database = max(database_scores, key=database_scores.get)
        confidence = min(database_scores[primary_database] / 1.0, 1.0)
        
        return primary_database, confidence
    
    def _check_dependency(self, dependency: str, language: Optional[str]) -> bool:
        """Check if dependency exists in project files"""
        # Check package.json
        package_json = self.project_root / "package.json"
        if package_json.exists():
            try:
                with open(package_json) as f:
                    data = json.load(f)
                    deps = {**data.get('dependencies', {}), **data.get('devDependencies', {})}
                    if any(dependency in dep for dep in deps.keys()):
                        return True
            except:
                pass
        
        # Check requirements.txt
        requirements = self.project_root / "requirements.txt"
        if requirements.exists():
            try:
                with open(requirements) as f:
                    content = f.read()
                    if dependency in content:
                        return True
            except:
                pass
        
        # Check pyproject.toml
        pyproject = self.project_root / "pyproject.toml"
        if pyproject.exists():
            try:
                with open(pyproject) as f:
                    content = f.read()
                    if dependency in content:
                        return True
            except:
                pass
        
        return False
    
    def detect_project_type(self, language: str, framework: str) -> str:
        """Determine overall project type/domain"""
        type_indicators = {
            'web-development': ['react', 'vue', 'angular', 'django', 'flask', 'express', 'nextjs'],
            'mobile-engineering': ['react-native', 'flutter', 'swift', 'kotlin'],
            'data-analytics': ['jupyter', 'pandas', 'numpy', 'matplotlib', 'seaborn'],
            'machine-learning': ['tensorflow', 'pytorch', 'scikit-learn', 'keras'],
            'devops-platform': ['docker', 'kubernetes', 'terraform', 'ansible'],
            'game-development': ['unity', 'unreal', 'godot'],
            'enterprise-tools': ['spring', 'hibernate', '.net'],
            'platform-engineering': ['microservices', 'api', 'grpc']
        }
        
        for project_type, indicators in type_indicators.items():
            if framework in indicators:
                return project_type
            
            # Check for dependencies
            for indicator in indicators:
                if self._check_dependency(indicator, language):
                    return project_type
        
        return 'general-development'


class ProjectInitializer:
    """Main project initialization orchestrator"""
    
    def __init__(self, project_root: Optional[Path] = None):
        self.project_root = project_root or Path.cwd()
        self.detector = TechStackDetector(self.project_root)
        self.logger = logging.getLogger(__name__)
        
        # Framework paths
        self.claude_md_path = self.project_root / "CLAUDE.md"
        self.config_path = self.project_root / "PROJECT_CONFIG.xml"
        self.claude_dir = self.project_root / ".claude"
    
    def analyze_project(self) -> ProjectAnalysis:
        """Comprehensive project analysis"""
        project_name = self.project_root.name
        
        # Detect tech stack
        language, lang_confidence = self.detector.detect_language()
        framework, framework_confidence = self.detector.detect_framework(language)
        database, db_confidence = self.detector.detect_database()
        project_type = self.detector.detect_project_type(language, framework)
        
        # Analyze existing files
        existing_files = []
        important_files = [
            'CLAUDE.md', 'PROJECT_CONFIG.xml', '.claude/',
            'README.md', '.gitignore', 'LICENSE'
        ]
        
        for file in important_files:
            file_path = self.project_root / file
            if file_path.exists():
                existing_files.append(file)
        
        # Gather dependencies
        dependencies = self._analyze_dependencies()
        
        # Calculate overall confidence
        confidence_score = (lang_confidence + framework_confidence + db_confidence) / 3.0
        
        # Generate recommendations
        recommendations = self._generate_recommendations(
            language, framework, database, existing_files, confidence_score
        )
        
        return ProjectAnalysis(
            name=project_name,
            root_path=self.project_root,
            tech_stack={
                'language': language,
                'framework': framework,
                'database': database
            },
            existing_files=existing_files,
            dependencies=dependencies,
            project_type=project_type,
            confidence_score=confidence_score,
            recommendations=recommendations
        )
    
    def _analyze_dependencies(self) -> Dict[str, List[str]]:
        """Analyze project dependencies"""
        dependencies = {'production': [], 'development': [], 'detected': []}
        
        # package.json
        package_json = self.project_root / "package.json"
        if package_json.exists():
            try:
                with open(package_json) as f:
                    data = json.load(f)
                    dependencies['production'].extend(data.get('dependencies', {}).keys())
                    dependencies['development'].extend(data.get('devDependencies', {}).keys())
            except:
                pass
        
        # requirements.txt
        requirements = self.project_root / "requirements.txt"
        if requirements.exists():
            try:
                with open(requirements) as f:
                    deps = [line.split('==')[0].split('>=')[0].strip() 
                           for line in f if line.strip() and not line.startswith('#')]
                    dependencies['production'].extend(deps)
            except:
                pass
        
        return dependencies
    
    def _generate_recommendations(self, language: str, framework: str, database: str, 
                                existing_files: List[str], confidence: float) -> List[str]:
        """Generate setup recommendations"""
        recommendations = []
        
        if confidence < 0.5:
            recommendations.append(f"Low detection confidence ({confidence:.1%}) - manual review recommended")
        
        if 'CLAUDE.md' not in existing_files:
            recommendations.append("Install CLAUDE.md framework file")
        
        if 'PROJECT_CONFIG.xml' not in existing_files:
            recommendations.append(f"Create PROJECT_CONFIG.xml for {language}/{framework} stack")
        
        if '.claude/' not in existing_files:
            recommendations.append("Initialize .claude/ framework directory structure")
        
        if 'README.md' not in existing_files:
            recommendations.append("Create comprehensive README.md")
        
        if '.gitignore' not in existing_files:
            recommendations.append(f"Create .gitignore for {language} projects")
        
        # Tech stack specific recommendations
        if language == 'python':
            if 'pytest' not in str(self.project_root):
                recommendations.append("Set up pytest testing framework")
            recommendations.append("Configure Black code formatting")
            recommendations.append("Set up virtual environment")
        
        elif language == 'javascript' or language == 'typescript':
            recommendations.append("Configure ESLint and Prettier")
            recommendations.append("Set up Jest testing framework")
        
        elif language == 'java':
            recommendations.append("Configure Maven or Gradle build system")
            recommendations.append("Set up JUnit testing")
        
        # Framework specific
        if framework == 'django':
            recommendations.append("Configure Django settings for development/production")
        elif framework == 'react':
            recommendations.append("Set up React testing library")
        
        return recommendations
    
    def interactive_setup(self) -> InitializationConfig:
        """Interactive project setup wizard"""
        print("\n🚀 Claude Code Framework - Project Initialization Wizard")
        print("=" * 60)
        
        # Analyze existing project
        print("\n📊 Analyzing project structure...")
        analysis = self.analyze_project()
        
        print(f"\n✅ Project Analysis Complete!")
        print(f"📁 Project: {analysis.name}")
        print(f"🔧 Detected Tech Stack:")
        print(f"   Language: {analysis.tech_stack['language']}")
        print(f"   Framework: {analysis.tech_stack['framework']}")
        print(f"   Database: {analysis.tech_stack['database']}")
        print(f"📈 Detection Confidence: {analysis.confidence_score:.1%}")
        
        if analysis.recommendations:
            print(f"\n💡 Recommendations:")
            for rec in analysis.recommendations:
                print(f"   • {rec}")
        
        # Get user confirmation/customization
        print(f"\n🎯 Configuration Setup")
        project_name = input(f"Project name [{analysis.name}]: ").strip() or analysis.name
        
        # Domain selection
        domains = [
            'web-development', 'mobile-engineering', 'data-analytics',
            'machine-learning', 'devops-platform', 'game-development',
            'enterprise-tools', 'platform-engineering', 'general-development'
        ]
        
        print(f"\nAvailable domains:")
        for i, domain in enumerate(domains):
            marker = "👈 detected" if domain == analysis.project_type else ""
            print(f"  {i+1}. {domain} {marker}")
        
        domain_choice = input(f"Select domain [detected: {analysis.project_type}]: ").strip()
        if domain_choice.isdigit() and 1 <= int(domain_choice) <= len(domains):
            domain = domains[int(domain_choice) - 1]
        else:
            domain = analysis.project_type
        
        # Language confirmation
        language = input(f"Primary language [{analysis.tech_stack['language']}]: ").strip() or analysis.tech_stack['language']
        framework = input(f"Framework [{analysis.tech_stack['framework']}]: ").strip() or analysis.tech_stack['framework']
        database = input(f"Database [{analysis.tech_stack['database']}]: ").strip() or analysis.tech_stack['database']
        
        # Setup options
        print(f"\n⚙️  Setup Options")
        setup_git_hooks = input("Set up git hooks? [Y/n]: ").strip().lower() not in ['n', 'no']
        create_directories = input("Create missing directories? [Y/n]: ").strip().lower() not in ['n', 'no']
        generate_examples = input("Generate example files? [Y/n]: ").strip().lower() not in ['n', 'no']
        configure_quality_gates = input("Configure quality gates? [Y/n]: ").strip().lower() not in ['n', 'no']
        
        return InitializationConfig(
            project_name=project_name,
            domain=domain,
            primary_language=language,
            framework=framework,
            database=database,
            setup_git_hooks=setup_git_hooks,
            create_directories=create_directories,
            generate_examples=generate_examples,
            configure_quality_gates=configure_quality_gates
        )
    
    def initialize_project(self, config: InitializationConfig, force: bool = False) -> bool:
        """Execute project initialization"""
        print(f"\n🔧 Initializing project with configuration:")
        print(f"   Name: {config.project_name}")
        print(f"   Domain: {config.domain}")
        print(f"   Tech Stack: {config.primary_language}/{config.framework}/{config.database}")
        
        try:
            # Step 1: Create CLAUDE.md if needed
            if not self.claude_md_path.exists() or force:
                self._create_claude_md()
                print("✅ Created CLAUDE.md framework file")
            
            # Step 2: Create PROJECT_CONFIG.xml
            if not self.config_path.exists() or force:
                self._create_project_config(config)
                print("✅ Generated PROJECT_CONFIG.xml")
            
            # Step 3: Create directory structure
            if config.create_directories:
                self._create_directories(config)
                print("✅ Created project directories")
            
            # Step 4: Setup git hooks
            if config.setup_git_hooks:
                self._setup_git_hooks()
                print("✅ Configured git hooks")
            
            # Step 5: Generate examples
            if config.generate_examples:
                self._generate_examples(config)
                print("✅ Generated example files")
            
            # Step 6: Configure quality gates
            if config.configure_quality_gates:
                self._configure_quality_gates(config)
                print("✅ Configured quality gates")
            
            print(f"\n🎉 Project initialization complete!")
            print(f"📝 Next steps:")
            print(f"   1. Review generated PROJECT_CONFIG.xml")
            print(f"   2. Customize framework settings as needed")
            print(f"   3. Start using framework commands: /auto, /task, /feature")
            
            return True
            
        except Exception as e:
            print(f"❌ Initialization failed: {e}")
            self.logger.error(f"Initialization error: {e}")
            return False
    
    def _create_claude_md(self):
        """Create CLAUDE.md framework file"""
        # Copy from template or create basic version
        claude_template = self.project_root / "CLAUDE.md.template"
        if claude_template.exists():
            shutil.copy2(claude_template, self.claude_md_path)
        else:
            # Create basic CLAUDE.md
            basic_claude = """# CLAUDE.md - Framework Control Document

| version | last_updated | status |
|---------|--------------|--------|
| 3.0.0   | 2025-07-15   | active |

This project uses the Claude Code Modular Prompts Framework for enhanced development workflows.

## Quick Start

Use these commands for development:
- `/auto "describe what you want"` - Intelligent task routing
- `/task "specific development task"` - Single component development  
- `/feature "new feature description"` - Complete feature development
- `/query "research question"` - Code analysis and research

## Configuration

Project-specific settings are in PROJECT_CONFIG.xml. Customize for your tech stack and requirements.
"""
            with open(self.claude_md_path, 'w') as f:
                f.write(basic_claude)
    
    def _create_project_config(self, config: InitializationConfig):
        """Generate PROJECT_CONFIG.xml"""
        # Use the unified validator to generate config
        sys.path.append(str(self.project_root / "scripts" / "validation"))
        try:
            from project_config_validator import UnifiedProjectConfigValidator
            validator = UnifiedProjectConfigValidator(self.project_root)
            xml_content = validator.generate_minimal_config(
                config.project_name, config.domain, config.primary_language
            )
            
            # Customize for specific framework and database
            xml_content = xml_content.replace(
                '<framework>auto-detect</framework>',
                f'<framework>{config.framework}</framework>'
            )
            xml_content = xml_content.replace(
                '<database>auto-detect</database>',
                f'<database>{config.database}</database>'
            )
            
            with open(self.config_path, 'w') as f:
                f.write(xml_content)
                
        except ImportError:
            # Fallback to simple XML generation
            simple_config = f"""<?xml version="1.0" encoding="UTF-8"?>
<project_configuration version="1.0.0">
  <project_info>
    <name>{config.project_name}</name>
    <domain>{config.domain}</domain>
    <primary_language>{config.primary_language}</primary_language>
    <framework>{config.framework}</framework>
    <database>{config.database}</database>
  </project_info>
  
  <project_structure>
    <source_directory>src</source_directory>
    <test_directory>tests</test_directory>
    <docs_directory>docs</docs_directory>
  </project_structure>
  
  <quality_standards>
    <test_coverage>
      <threshold>90</threshold>
      <enforcement>BLOCKING</enforcement>
    </test_coverage>
  </quality_standards>
  
  <development_workflow>
    <commands>
      <test>auto-detect</test>
      <lint>auto-detect</lint>
      <build>auto-detect</build>
    </commands>
  </development_workflow>
</project_configuration>"""
            
            with open(self.config_path, 'w') as f:
                f.write(simple_config)
    
    def _create_directories(self, config: InitializationConfig):
        """Create standard project directories"""
        directories = [
            'src', 'tests', 'docs', 'scripts',
            '.claude', '.claude/modules', '.claude/commands'
        ]
        
        for dir_name in directories:
            dir_path = self.project_root / dir_name
            dir_path.mkdir(parents=True, exist_ok=True)
    
    def _setup_git_hooks(self):
        """Setup git hooks using existing script"""
        hook_script = self.project_root / "scripts" / "setup" / "setup_precommit.sh"
        if hook_script.exists():
            try:
                subprocess.run(['bash', str(hook_script)], 
                             cwd=self.project_root, check=True, capture_output=True)
            except subprocess.CalledProcessError as e:
                self.logger.warning(f"Git hook setup failed: {e}")
    
    def _generate_examples(self, config: InitializationConfig):
        """Generate basic example files"""
        examples_dir = self.project_root / "examples"
        examples_dir.mkdir(exist_ok=True)
        
        # Create basic example README
        example_readme = """# Examples

This directory contains examples for the Claude Code Framework.

## Basic Usage

```bash
# Research existing code
/query "understand the authentication system"

# Single task development
/task "add email validation to user registration"

# Complete feature development  
/feature "implement user dashboard with activity tracking"
```

## Project-Specific Examples

Add your project-specific examples here as you develop patterns and workflows.
"""
        
        with open(examples_dir / "README.md", 'w') as f:
            f.write(example_readme)
    
    def _configure_quality_gates(self, config: InitializationConfig):
        """Configure quality gates and testing"""
        # Create basic test file if none exists
        tests_dir = self.project_root / "tests"
        tests_dir.mkdir(exist_ok=True)
        
        test_init = tests_dir / "__init__.py"
        if not test_init.exists():
            test_init.touch()
        
        # Language-specific test setup
        if config.primary_language == 'python':
            self._setup_python_testing()
        elif config.primary_language in ['javascript', 'typescript']:
            self._setup_js_testing()
    
    def _setup_python_testing(self):
        """Setup Python-specific testing configuration"""
        # Create pytest.ini if it doesn't exist
        pytest_ini = self.project_root / "pytest.ini"
        if not pytest_ini.exists():
            pytest_config = """[tool:pytest]
testpaths = tests
python_files = test_*.py
python_functions = test_*
addopts = --verbose --cov=src --cov-report=term-missing
"""
            with open(pytest_ini, 'w') as f:
                f.write(pytest_config)
    
    def _setup_js_testing(self):
        """Setup JavaScript/TypeScript testing configuration"""
        # Add to package.json if it exists
        package_json = self.project_root / "package.json"
        if package_json.exists():
            try:
                with open(package_json) as f:
                    data = json.load(f)
                
                if 'scripts' not in data:
                    data['scripts'] = {}
                
                data['scripts'].update({
                    'test': 'jest',
                    'test:coverage': 'jest --coverage',
                    'test:watch': 'jest --watch'
                })
                
                with open(package_json, 'w') as f:
                    json.dump(data, f, indent=2)
            except:
                pass


def main():
    """CLI interface for project initializer"""
    parser = argparse.ArgumentParser(
        description="Claude Code Framework Project Initializer",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python project_initializer.py                    # Interactive setup wizard
  python project_initializer.py --auto             # Auto-detect and initialize
  python project_initializer.py --name MyApp --domain web-development --language python
        """
    )
    
    parser.add_argument('--project-root', help="Project root directory (default: current)")
    parser.add_argument('--name', help="Project name")
    parser.add_argument('--domain', help="Project domain")
    parser.add_argument('--language', help="Primary programming language")
    parser.add_argument('--framework', help="Framework/library")
    parser.add_argument('--database', help="Database technology")
    parser.add_argument('--auto', action='store_true', help="Auto-detect and initialize")
    parser.add_argument('--force', action='store_true', help="Overwrite existing files")
    parser.add_argument('--verbose', '-v', action='store_true', help="Verbose output")
    
    args = parser.parse_args()
    
    # Setup logging
    level = logging.DEBUG if args.verbose else logging.INFO
    logging.basicConfig(level=level, format='%(levelname)s: %(message)s')
    
    try:
        initializer = ProjectInitializer(
            project_root=Path(args.project_root) if args.project_root else None
        )
        
        if args.auto:
            # Auto-detection mode
            analysis = initializer.analyze_project()
            config = InitializationConfig(
                project_name=analysis.name,
                domain=analysis.project_type,
                primary_language=analysis.tech_stack['language'],
                framework=analysis.tech_stack['framework'],
                database=analysis.tech_stack['database']
            )
        elif all([args.name, args.domain, args.language]):
            # Direct configuration mode
            config = InitializationConfig(
                project_name=args.name,
                domain=args.domain,
                primary_language=args.language,
                framework=args.framework or 'generic',
                database=args.database or 'sqlite'
            )
        else:
            # Interactive mode
            config = initializer.interactive_setup()
        
        # Execute initialization
        success = initializer.initialize_project(config, force=args.force)
        return 0 if success else 1
        
    except KeyboardInterrupt:
        print(f"\n⚠️  Initialization cancelled by user")
        return 1
    except Exception as e:
        logging.error(f"Initialization failed: {e}")
        return 1


if __name__ == "__main__":
    exit(main())