#!/usr/bin/env python3
"""
Smart Defaults Engine for PROJECT_CONFIG System
Automatically detects project context and provides intelligent configuration defaults

TASK 3: Create smart defaults for common tech stacks
Author: Agent 4 - Configuration System Simplification
"""

import os
import json
import re
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Any
from dataclasses import dataclass
from abc import ABC, abstractmethod


@dataclass
class TechStackDetection:
    """Results of tech stack detection"""
    primary_language: str
    framework_stack: str
    confidence: float
    detected_tools: Dict[str, str]
    project_type: str
    domain: str


class StackDetector(ABC):
    """Base class for technology stack detectors"""
    
    @abstractmethod
    def detect(self, project_root: Path) -> Optional[TechStackDetection]:
        """Detect if this stack is present in the project"""
        pass
    
    @abstractmethod
    def get_defaults(self) -> Dict[str, Any]:
        """Get default configuration for this stack"""
        pass


class ReactTypeScriptDetector(StackDetector):
    """Detects React + TypeScript projects"""
    
    def detect(self, project_root: Path) -> Optional[TechStackDetection]:
        confidence = 0.0
        indicators = []
        
        # Check package.json
        package_json = project_root / "package.json"
        if package_json.exists():
            try:
                with open(package_json) as f:
                    data = json.load(f)
                    deps = {**data.get("dependencies", {}), **data.get("devDependencies", {})}
                    
                    if "react" in deps:
                        confidence += 0.4
                        indicators.append("react dependency")
                    
                    if "typescript" in deps or "@types/react" in deps:
                        confidence += 0.3
                        indicators.append("typescript config")
                    
                    if "next" in deps or "@next/core" in deps:
                        confidence += 0.2
                        indicators.append("nextjs framework")
                        
            except (json.JSONDecodeError, FileNotFoundError):
                pass
        
        # Check for TypeScript config
        if (project_root / "tsconfig.json").exists():
            confidence += 0.2
            indicators.append("tsconfig.json")
        
        # Check for React components
        src_dirs = [project_root / "src", project_root / "components", project_root / "app"]
        for src_dir in src_dirs:
            if src_dir.exists():
                tsx_files = list(src_dir.glob("**/*.tsx"))
                if tsx_files:
                    confidence += 0.3
                    indicators.append(f"tsx components ({len(tsx_files)})")
                    break
        
        if confidence >= 0.7:
            return TechStackDetection(
                primary_language="typescript",
                framework_stack="react+typescript",
                confidence=confidence,
                detected_tools=self._detect_tools(project_root),
                project_type="web-frontend",
                domain="web-development"
            )
        
        return None
    
    def _detect_tools(self, project_root: Path) -> Dict[str, str]:
        tools = {}
        
        if (project_root / "package.json").exists():
            try:
                with open(project_root / "package.json") as f:
                    data = json.load(f)
                    scripts = data.get("scripts", {})
                    deps = {**data.get("dependencies", {}), **data.get("devDependencies", {})}
                    
                    # Test tools
                    if "jest" in deps or "test" in scripts:
                        tools["test_tool"] = "jest"
                    elif "vitest" in deps:
                        tools["test_tool"] = "vitest"
                    
                    # Linting
                    if "eslint" in deps:
                        tools["linter"] = "eslint"
                    
                    # Formatting
                    if "prettier" in deps:
                        tools["formatter"] = "prettier"
                    
                    # Build tools
                    if "vite" in deps:
                        tools["build_tool"] = "vite"
                    elif "webpack" in deps:
                        tools["build_tool"] = "webpack"
                    elif "next" in deps:
                        tools["build_tool"] = "next"
                        
            except (json.JSONDecodeError, FileNotFoundError):
                pass
        
        return tools
    
    def get_defaults(self) -> Dict[str, Any]:
        return {
            "project_structure": {
                "source_directory": "src",
                "test_directory": "src/__tests__",
                "build_directory": "dist"
            },
            "quality_standards": {
                "test_coverage": {
                    "threshold": 85,
                    "enforcement": "BLOCKING",
                    "tool": "jest"
                },
                "performance": {
                    "response_time_p95": "200ms",
                    "memory_limit": "512MB"
                },
                "code_quality": {
                    "linter": "eslint",
                    "formatter": "prettier",
                    "type_checker": "typescript"
                }
            },
            "development_workflow": {
                "commands": {
                    "install": "npm install",
                    "test": "npm test",
                    "build": "npm run build",
                    "lint": "npm run lint",
                    "format": "npm run format"
                }
            },
            "domain_specific_rules": [
                "Components must be accessible (WCAG 2.1 AA compliant)",
                "Use React hooks and functional components",
                "Implement responsive design with mobile-first approach",
                "Bundle size must be under 250KB gzipped",
                "Lighthouse performance score > 90"
            ],
            "framework_behavior": {
                "ai_temperature": {
                    "factual": 0.2,
                    "analysis": 0.3,
                    "creative": 0.7
                }
            }
        }


class PythonDjangoDetector(StackDetector):
    """Detects Python + Django projects"""
    
    def detect(self, project_root: Path) -> Optional[TechStackDetection]:
        confidence = 0.0
        indicators = []
        
        # Check for Django files
        if (project_root / "manage.py").exists():
            confidence += 0.5
            indicators.append("manage.py")
        
        # Check requirements files
        req_files = ["requirements.txt", "pyproject.toml", "Pipfile"]
        for req_file in req_files:
            req_path = project_root / req_file
            if req_path.exists():
                try:
                    content = req_path.read_text()
                    if "django" in content.lower():
                        confidence += 0.4
                        indicators.append(f"django in {req_file}")
                        break
                except (UnicodeDecodeError, FileNotFoundError):
                    pass
        
        # Check for Django project structure
        potential_dirs = [d for d in project_root.iterdir() if d.is_dir() and not d.name.startswith('.')]
        for directory in potential_dirs:
            if (directory / "settings.py").exists() or (directory / "urls.py").exists():
                confidence += 0.3
                indicators.append("django project structure")
                break
        
        if confidence >= 0.7:
            return TechStackDetection(
                primary_language="python",
                framework_stack="django+python",
                confidence=confidence,
                detected_tools=self._detect_tools(project_root),
                project_type="web-backend",
                domain="web-development"
            )
        
        return None
    
    def _detect_tools(self, project_root: Path) -> Dict[str, str]:
        tools = {"test_tool": "django-test", "linter": "pylint", "formatter": "black"}
        
        # Check for specific tools in requirements
        req_files = ["requirements.txt", "requirements-dev.txt", "pyproject.toml"]
        for req_file in req_files:
            req_path = project_root / req_file
            if req_path.exists():
                try:
                    content = req_path.read_text().lower()
                    
                    if "pytest" in content:
                        tools["test_tool"] = "pytest"
                    if "coverage" in content:
                        tools["coverage_tool"] = "coverage.py"
                    if "flake8" in content:
                        tools["linter"] = "flake8"
                    if "mypy" in content:
                        tools["type_checker"] = "mypy"
                        
                except (UnicodeDecodeError, FileNotFoundError):
                    pass
        
        return tools
    
    def get_defaults(self) -> Dict[str, Any]:
        return {
            "project_structure": {
                "source_directory": ".",
                "test_directory": "tests",
                "build_directory": "build"
            },
            "quality_standards": {
                "test_coverage": {
                    "threshold": 90,
                    "enforcement": "BLOCKING",
                    "tool": "coverage.py"
                },
                "performance": {
                    "response_time_p95": "300ms",
                    "memory_limit": "1GB"
                },
                "code_quality": {
                    "linter": "pylint",
                    "formatter": "black",
                    "type_checker": "mypy"
                }
            },
            "development_workflow": {
                "commands": {
                    "install": "pip install -r requirements.txt",
                    "test": "python manage.py test",
                    "run": "python manage.py runserver",
                    "migrate": "python manage.py migrate",
                    "lint": "pylint .",
                    "format": "black ."
                }
            },
            "domain_specific_rules": [
                "Follow Django best practices and conventions",
                "Use Django ORM for database operations",
                "Implement proper authentication and authorization",
                "Follow REST API design principles",
                "Use Django's built-in security features"
            ],
            "security_requirements": {
                "authentication": "django-auth",
                "data_encryption": "at-rest+in-transit",
                "vulnerability_scanning": "bandit"
            }
        }


class PythonDataScienceDetector(StackDetector):
    """Detects Python + Data Science projects"""
    
    def detect(self, project_root: Path) -> Optional[TechStackDetection]:
        confidence = 0.0
        indicators = []
        
        # Check for Jupyter notebooks
        jupyter_files = list(project_root.glob("**/*.ipynb"))
        if jupyter_files:
            confidence += 0.4
            indicators.append(f"jupyter notebooks ({len(jupyter_files)})")
        
        # Check for data science libraries
        req_files = ["requirements.txt", "pyproject.toml", "environment.yml"]
        data_science_libs = ["pandas", "numpy", "scikit-learn", "tensorflow", "pytorch", "matplotlib", "seaborn", "jupyter"]
        
        for req_file in req_files:
            req_path = project_root / req_file
            if req_path.exists():
                try:
                    content = req_path.read_text().lower()
                    found_libs = [lib for lib in data_science_libs if lib in content]
                    if found_libs:
                        confidence += min(0.5, len(found_libs) * 0.1)
                        indicators.append(f"data science libs: {found_libs}")
                        break
                except (UnicodeDecodeError, FileNotFoundError):
                    pass
        
        # Check for data directories
        data_dirs = ["data", "datasets", "models", "notebooks"]
        for data_dir in data_dirs:
            if (project_root / data_dir).exists():
                confidence += 0.1
                indicators.append(f"{data_dir} directory")
        
        if confidence >= 0.6:
            return TechStackDetection(
                primary_language="python",
                framework_stack="pandas+scikit-learn+jupyter",
                confidence=confidence,
                detected_tools=self._detect_tools(project_root),
                project_type="data-analysis",
                domain="data-analytics"
            )
        
        return None
    
    def _detect_tools(self, project_root: Path) -> Dict[str, str]:
        tools = {"test_tool": "pytest", "linter": "pylint", "formatter": "black"}
        
        # Check for ML/Data tools
        if list(project_root.glob("**/*.ipynb")):
            tools["notebook_tool"] = "jupyter"
        
        return tools
    
    def get_defaults(self) -> Dict[str, Any]:
        return {
            "project_structure": {
                "source_directory": "src",
                "test_directory": "tests",
                "build_directory": "build",
                "data_directory": "data",
                "notebooks_directory": "notebooks"
            },
            "quality_standards": {
                "test_coverage": {
                    "threshold": 75,
                    "enforcement": "CONDITIONAL",
                    "tool": "pytest-cov"
                },
                "performance": {
                    "response_time_p95": "5000ms",
                    "memory_limit": "8GB"
                },
                "code_quality": {
                    "linter": "pylint",
                    "formatter": "black",
                    "type_checker": "mypy"
                }
            },
            "development_workflow": {
                "commands": {
                    "install": "pip install -r requirements.txt",
                    "test": "pytest",
                    "lint": "pylint src/",
                    "format": "black .",
                    "notebook": "jupyter lab"
                }
            },
            "domain_specific_rules": [
                "All data transformations must be reproducible",
                "Model experiments must be tracked with MLflow",
                "Data validation required for all pipeline inputs",
                "Feature engineering must be documented",
                "Model performance metrics must include fairness measures"
            ],
            "framework_behavior": {
                "ai_temperature": {
                    "factual": 0.1,
                    "analysis": 0.2,
                    "creative": 0.5
                }
            }
        }


class NodeExpressDetector(StackDetector):
    """Detects Node.js + Express projects"""
    
    def detect(self, project_root: Path) -> Optional[TechStackDetection]:
        confidence = 0.0
        indicators = []
        
        # Check package.json
        package_json = project_root / "package.json"
        if package_json.exists():
            try:
                with open(package_json) as f:
                    data = json.load(f)
                    deps = {**data.get("dependencies", {}), **data.get("devDependencies", {})}
                    
                    if "express" in deps:
                        confidence += 0.5
                        indicators.append("express dependency")
                    
                    if "node" in str(data.get("engines", {})):
                        confidence += 0.2
                        indicators.append("node engine specified")
                        
            except (json.JSONDecodeError, FileNotFoundError):
                pass
        
        # Check for common Express patterns
        js_files = list(project_root.glob("**/*.js")) + list(project_root.glob("**/*.ts"))
        for js_file in js_files[:10]:  # Check first 10 files
            try:
                content = js_file.read_text()
                if "express()" in content or "app.listen" in content:
                    confidence += 0.3
                    indicators.append("express app pattern")
                    break
            except (UnicodeDecodeError, FileNotFoundError):
                pass
        
        if confidence >= 0.6:
            return TechStackDetection(
                primary_language="javascript",
                framework_stack="express+node",
                confidence=confidence,
                detected_tools=self._detect_tools(project_root),
                project_type="web-backend",
                domain="web-development"
            )
        
        return None
    
    def _detect_tools(self, project_root: Path) -> Dict[str, str]:
        tools = {}
        
        if (project_root / "package.json").exists():
            try:
                with open(project_root / "package.json") as f:
                    data = json.load(f)
                    deps = {**data.get("dependencies", {}), **data.get("devDependencies", {})}
                    
                    if "jest" in deps:
                        tools["test_tool"] = "jest"
                    elif "mocha" in deps:
                        tools["test_tool"] = "mocha"
                    
                    if "eslint" in deps:
                        tools["linter"] = "eslint"
                    
                    if "prettier" in deps:
                        tools["formatter"] = "prettier"
                        
            except (json.JSONDecodeError, FileNotFoundError):
                pass
        
        return tools
    
    def get_defaults(self) -> Dict[str, Any]:
        return {
            "project_structure": {
                "source_directory": "src",
                "test_directory": "tests",
                "build_directory": "dist"
            },
            "quality_standards": {
                "test_coverage": {
                    "threshold": 80,
                    "enforcement": "BLOCKING",
                    "tool": "jest"
                },
                "performance": {
                    "response_time_p95": "300ms",
                    "memory_limit": "512MB"
                },
                "code_quality": {
                    "linter": "eslint",
                    "formatter": "prettier",
                    "type_checker": "none"
                }
            },
            "development_workflow": {
                "commands": {
                    "install": "npm install",
                    "test": "npm test",
                    "start": "npm start",
                    "dev": "npm run dev",
                    "lint": "npm run lint"
                }
            },
            "domain_specific_rules": [
                "Follow RESTful API design principles",
                "Implement proper error handling middleware",
                "Use environment variables for configuration",
                "Implement request validation",
                "Follow Node.js security best practices"
            ]
        }


class SmartDefaultsEngine:
    """Main engine for smart defaults detection and generation"""
    
    def __init__(self):
        self.detectors = [
            ReactTypeScriptDetector(),
            PythonDjangoDetector(),
            PythonDataScienceDetector(),
            NodeExpressDetector()
        ]
    
    def detect_tech_stack(self, project_root: str | Path) -> Optional[TechStackDetection]:
        """Detect the technology stack of a project"""
        project_path = Path(project_root)
        
        if not project_path.exists():
            return None
        
        best_detection = None
        best_confidence = 0.0
        
        for detector in self.detectors:
            detection = detector.detect(project_path)
            if detection and detection.confidence > best_confidence:
                best_detection = detection
                best_confidence = detection.confidence
        
        return best_detection
    
    def generate_minimal_config(self, project_root: str | Path) -> Dict[str, Any]:
        """Generate minimal tier configuration with auto-detection"""
        detection = self.detect_tech_stack(project_root)
        
        if detection:
            # Find the appropriate detector and get its defaults
            for detector in self.detectors:
                test_detection = detector.detect(Path(project_root))
                if (test_detection and 
                    test_detection.framework_stack == detection.framework_stack):
                    defaults = detector.get_defaults()
                    break
            else:
                defaults = self._generic_defaults()
        else:
            defaults = self._generic_defaults()
        
        # Build minimal config
        config = {
            "project_info": {
                "name": Path(project_root).name,
                "domain": detection.domain if detection else "general-development",
                "primary_language": detection.primary_language if detection else "auto-detect",
                "framework_stack": detection.framework_stack if detection else "auto-detect"
            },
            **defaults
        }
        
        return config
    
    def generate_standard_config(self, project_root: str | Path, user_inputs: Dict[str, Any]) -> Dict[str, Any]:
        """Generate standard tier configuration with guided inputs"""
        minimal_config = self.generate_minimal_config(project_root)
        
        # Merge user inputs with smart defaults
        config = minimal_config.copy()
        config["project_info"].update(user_inputs.get("project_info", {}))
        
        if "quality_standards" in user_inputs:
            config["quality_standards"].update(user_inputs["quality_standards"])
        
        return config
    
    def _generic_defaults(self) -> Dict[str, Any]:
        """Generic defaults for unknown project types"""
        return {
            "project_structure": {
                "source_directory": "src",
                "test_directory": "tests",
                "build_directory": "build"
            },
            "quality_standards": {
                "test_coverage": {
                    "threshold": 80,
                    "enforcement": "ADVISORY",
                    "tool": "auto-detect"
                },
                "performance": {
                    "response_time_p95": "500ms",
                    "memory_limit": "512MB"
                },
                "code_quality": {
                    "linter": "auto-detect",
                    "formatter": "auto-detect",
                    "type_checker": "auto-detect"
                }
            },
            "development_workflow": {
                "commands": {
                    "install": "auto-detect",
                    "test": "auto-detect",
                    "build": "auto-detect",
                    "lint": "auto-detect"
                }
            },
            "domain_specific_rules": [
                "Follow language-specific best practices",
                "Implement proper error handling",
                "Use semantic versioning",
                "Maintain clear documentation"
            ]
        }


def main():
    """Example usage of the Smart Defaults Engine"""
    engine = SmartDefaultsEngine()
    
    # Example: Detect current project
    current_project = Path.cwd()
    detection = engine.detect_tech_stack(current_project)
    
    if detection:
        print(f"Detected: {detection.framework_stack}")
        print(f"Confidence: {detection.confidence:.2f}")
        print(f"Domain: {detection.domain}")
        
        config = engine.generate_minimal_config(current_project)
        print("\nGenerated minimal config:")
        print(json.dumps(config, indent=2))
    else:
        print("No specific tech stack detected, using generic defaults")


if __name__ == "__main__":
    main()