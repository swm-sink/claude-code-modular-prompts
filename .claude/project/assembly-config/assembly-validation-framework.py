#!/usr/bin/env python3
"""
Assembly Validation Framework
Validates component combinations for compatibility, performance, and correctness.
Used by /assemble-command to ensure quality component assemblies.
"""

import json
import re
from typing import List, Dict, Set, Tuple, Optional
from dataclasses import dataclass
from enum import Enum

class ValidationLevel(Enum):
    ERROR = "error"
    WARNING = "warning"
    INFO = "info"

@dataclass
class ValidationResult:
    level: ValidationLevel
    message: str
    component: Optional[str] = None
    suggestion: Optional[str] = None

@dataclass
class ComponentInfo:
    name: str
    category: str
    requires: List[str]
    provides: List[str]
    compatible_with: List[str]
    incompatible_with: List[str]
    data_types: List[str]
    performance_impact: str

class AssemblyValidator:
    """Validates component assemblies for compatibility and best practices."""
    
    def __init__(self, compatibility_matrix_path: str):
        """Initialize validator with compatibility matrix."""
        with open(compatibility_matrix_path, 'r') as f:
            self.matrix = json.load(f)
        self.components = self._load_components()
    
    def _load_components(self) -> Dict[str, ComponentInfo]:
        """Load component information from compatibility matrix."""
        components = {}
        
        for category, category_components in self.matrix['component_compatibility_matrix']['compatibility_rules'].items():
            for comp_name, comp_data in category_components.items():
                components[comp_name] = ComponentInfo(
                    name=comp_name,
                    category=category,
                    requires=comp_data.get('requires', []),
                    provides=comp_data.get('provides', []),
                    compatible_with=comp_data.get('compatible_with', []),
                    incompatible_with=comp_data.get('incompatible_with', []),
                    data_types=comp_data.get('data_types', []),
                    performance_impact=comp_data.get('performance_impact', 'unknown')
                )
        
        return components
    
    def validate_assembly(self, component_list: List[str]) -> List[ValidationResult]:
        """Validate a complete component assembly."""
        results = []
        
        # Basic validation
        results.extend(self._validate_components_exist(component_list))
        results.extend(self._validate_compatibility(component_list))
        results.extend(self._validate_data_flow(component_list))
        results.extend(self._validate_dependencies(component_list))
        
        # Advanced validation
        results.extend(self._validate_performance(component_list))
        results.extend(self._validate_security(component_list))
        results.extend(self._validate_patterns(component_list))
        
        return results
    
    def _validate_components_exist(self, component_list: List[str]) -> List[ValidationResult]:
        """Check that all components exist in the system."""
        results = []
        
        for component in component_list:
            if component not in self.components:
                results.append(ValidationResult(
                    level=ValidationLevel.ERROR,
                    message=f"Component '{component}' does not exist",
                    component=component,
                    suggestion="Check component name spelling or browse available components with /assemble-command --browse"
                ))
        
        return results
    
    def _validate_compatibility(self, component_list: List[str]) -> List[ValidationResult]:
        """Check component compatibility."""
        results = []
        
        for i, component in enumerate(component_list):
            if component not in self.components:
                continue
                
            comp_info = self.components[component]
            
            # Check explicit incompatibilities
            for other_component in component_list:
                if other_component in comp_info.incompatible_with:
                    results.append(ValidationResult(
                        level=ValidationLevel.ERROR,
                        message=f"Component '{component}' is incompatible with '{other_component}'",
                        component=component,
                        suggestion=f"Remove one of these components or find alternative components"
                    ))
            
            # Check compatibility with adjacent components
            if i > 0:
                prev_component = component_list[i-1]
                if prev_component in self.components:
                    if not self._are_compatible(prev_component, component):
                        results.append(ValidationResult(
                            level=ValidationLevel.WARNING,
                            message=f"Components '{prev_component}' and '{component}' may not be directly compatible",
                            component=component,
                            suggestion="Consider adding a format-converter or adapter component between them"
                        ))
        
        return results
    
    def _are_compatible(self, comp1: str, comp2: str) -> bool:
        """Check if two components are compatible."""
        if comp1 not in self.components or comp2 not in self.components:
            return False
            
        comp1_info = self.components[comp1]
        comp2_info = self.components[comp2]
        
        # Universal compatibility
        if "*" in comp1_info.compatible_with or "*" in comp2_info.compatible_with:
            return True
            
        # Explicit compatibility
        return (comp2 in comp1_info.compatible_with or 
                comp1 in comp2_info.compatible_with)
    
    def _validate_data_flow(self, component_list: List[str]) -> List[ValidationResult]:
        """Validate data flow between components."""
        results = []
        
        for i in range(len(component_list) - 1):
            current = component_list[i]
            next_comp = component_list[i + 1]
            
            if current not in self.components or next_comp not in self.components:
                continue
                
            current_info = self.components[current]
            next_info = self.components[next_comp]
            
            # Check if current component provides what next component requires
            if next_info.requires:
                provided_types = set(current_info.provides)
                required_types = set(next_info.requires)
                
                if not provided_types.intersection(required_types):
                    results.append(ValidationResult(
                        level=ValidationLevel.WARNING,
                        message=f"Data flow mismatch: '{current}' provides {current_info.provides} but '{next_comp}' requires {next_info.requires}",
                        component=next_comp,
                        suggestion="Consider adding a data-transformer or format-converter component"
                    ))
        
        return results
    
    def _validate_dependencies(self, component_list: List[str]) -> List[ValidationResult]:
        """Check for circular dependencies and missing dependencies."""
        results = []
        
        # Check for circular dependencies (simplified check)
        seen = set()
        for component in component_list:
            if component in seen:
                results.append(ValidationResult(
                    level=ValidationLevel.ERROR,
                    message=f"Circular dependency detected: component '{component}' appears multiple times",
                    component=component,
                    suggestion="Remove duplicate components or restructure the workflow"
                ))
            seen.add(component)
        
        # Check for missing dependencies
        for component in component_list:
            if component not in self.components:
                continue
                
            comp_info = self.components[component]
            for required in comp_info.requires:
                # Check if any component in the list provides this requirement
                provided = False
                for other_comp in component_list:
                    if other_comp != component and other_comp in self.components:
                        if required in self.components[other_comp].provides:
                            provided = True
                            break
                
                if not provided:
                    results.append(ValidationResult(
                        level=ValidationLevel.WARNING,
                        message=f"Component '{component}' requires '{required}' but no component provides it",
                        component=component,
                        suggestion=f"Add a component that provides '{required}' or configure external data source"
                    ))
        
        return results
    
    def _validate_performance(self, component_list: List[str]) -> List[ValidationResult]:
        """Validate performance characteristics of the assembly."""
        results = []
        
        high_impact_components = []
        total_impact_score = 0
        
        impact_scores = {
            'minimal': 1,
            'low': 2, 
            'medium': 4,
            'high': 8,
            'very_high': 16
        }
        
        for component in component_list:
            if component not in self.components:
                continue
                
            impact = self.components[component].performance_impact
            score = impact_scores.get(impact, 2)
            total_impact_score += score
            
            if score >= 8:
                high_impact_components.append(component)
        
        # Warn about high-impact assemblies
        if total_impact_score > 20:
            results.append(ValidationResult(
                level=ValidationLevel.WARNING,
                message=f"High performance impact assembly (score: {total_impact_score})",
                suggestion="Consider optimizing by reducing heavy components or enabling parallel processing"
            ))
        
        if len(high_impact_components) > 2:
            results.append(ValidationResult(
                level=ValidationLevel.WARNING,
                message=f"Multiple high-impact components: {high_impact_components}",
                suggestion="Consider processing in stages or using parallel execution"
            ))
        
        return results
    
    def _validate_security(self, component_list: List[str]) -> List[ValidationResult]:
        """Validate security aspects of the assembly."""
        results = []
        
        # Check for security-sensitive operations without proper protection
        sensitive_components = [
            'file-reader', 'file-writer', 'api-caller', 'git-operations'
        ]
        
        security_components = [
            'input-validation', 'credential-protection', 'path-validation',
            'input-validation-framework', 'command-security-wrapper'
        ]
        
        has_sensitive = any(comp in component_list for comp in sensitive_components)
        has_security = any(comp in component_list for comp in security_components)
        
        if has_sensitive and not has_security:
            results.append(ValidationResult(
                level=ValidationLevel.WARNING,
                message="Assembly includes security-sensitive components without security validation",
                suggestion="Consider adding input-validation or other security components"
            ))
        
        return results
    
    def _validate_patterns(self, component_list: List[str]) -> List[ValidationResult]:
        """Validate against known good and bad patterns."""
        results = []
        
        # Check for anti-patterns
        patterns = self.matrix['component_compatibility_matrix'].get('compatibility_patterns', {})
        
        # Example: Check for proper error handling
        has_error_prone = any(
            comp in component_list 
            for comp in ['file-reader', 'api-caller', 'git-operations', 'data-transformer']
        )
        has_error_handler = 'error-handler' in component_list
        
        if has_error_prone and not has_error_handler:
            results.append(ValidationResult(
                level=ValidationLevel.WARNING,
                message="Assembly includes error-prone components without error handling",
                suggestion="Add error-handler component for better reliability"
            ))
        
        # Check for progress tracking in long-running operations
        heavy_components = [
            comp for comp in component_list 
            if comp in self.components and 
            self.components[comp].performance_impact in ['high', 'very_high']
        ]
        
        if len(heavy_components) > 1 and 'progress-indicator' not in component_list:
            results.append(ValidationResult(
                level=ValidationLevel.INFO,
                message="Long-running assembly would benefit from progress tracking",
                suggestion="Add progress-indicator component for better user experience"
            ))
        
        return results
    
    def suggest_optimizations(self, component_list: List[str]) -> List[ValidationResult]:
        """Suggest optimizations for the assembly."""
        results = []
        
        # Suggest parallel processing opportunities
        parallelizable = ['data-transformer', 'format-converter', 'content-sanitizer']
        parallel_candidates = [comp for comp in component_list if comp in parallelizable]
        
        if len(parallel_candidates) >= 2:
            results.append(ValidationResult(
                level=ValidationLevel.INFO,
                message=f"Components {parallel_candidates} could benefit from parallel processing",
                suggestion="Consider enabling parallel processing configuration"
            ))
        
        # Suggest caching opportunities
        expensive_ops = ['codebase-discovery', 'dependency-mapping', 'quality-metrics']
        if any(comp in component_list for comp in expensive_ops):
            results.append(ValidationResult(
                level=ValidationLevel.INFO,
                message="Assembly includes expensive operations that could benefit from caching",
                suggestion="Enable component caching to improve repeat execution performance"
            ))
        
        return results
    
    def generate_assembly_report(self, component_list: List[str]) -> Dict:
        """Generate comprehensive assembly analysis report."""
        validation_results = self.validate_assembly(component_list)
        optimization_suggestions = self.suggest_optimizations(component_list)
        
        # Count results by level
        error_count = len([r for r in validation_results if r.level == ValidationLevel.ERROR])
        warning_count = len([r for r in validation_results if r.level == ValidationLevel.WARNING])
        info_count = len([r for r in validation_results if r.level == ValidationLevel.INFO])
        
        # Calculate performance estimate
        performance_score = sum(
            {'minimal': 1, 'low': 2, 'medium': 4, 'high': 8, 'very_high': 16}.get(
                self.components.get(comp, ComponentInfo('', '', [], [], [], [], [], 'medium')).performance_impact,
                4
            ) for comp in component_list if comp in self.components
        )
        
        return {
            'assembly_valid': error_count == 0,
            'component_count': len(component_list),
            'validation_summary': {
                'errors': error_count,
                'warnings': warning_count,
                'info': info_count
            },
            'performance_estimate': {
                'score': performance_score,
                'category': 'low' if performance_score <= 10 else 'medium' if performance_score <= 20 else 'high',
                'estimated_time': '30s-2m' if performance_score <= 10 else '2-5m' if performance_score <= 20 else '5-15m'
            },
            'validation_results': [
                {
                    'level': result.level.value,
                    'message': result.message,
                    'component': result.component,
                    'suggestion': result.suggestion
                } for result in validation_results
            ],
            'optimizations': [
                {
                    'level': result.level.value,
                    'message': result.message,
                    'suggestion': result.suggestion
                } for result in optimization_suggestions
            ]
        }

def main():
    """Example usage of the validation framework."""
    validator = AssemblyValidator('component-compatibility-matrix.json')
    
    # Example component assembly
    test_assembly = [
        'file-reader',
        'input-validation', 
        'data-transformer',
        'output-formatter',
        'file-writer'
    ]
    
    # Validate the assembly
    report = validator.generate_assembly_report(test_assembly)
    
    print("Assembly Validation Report")
    print("=" * 50)
    print(f"Components: {test_assembly}")
    print(f"Assembly Valid: {report['assembly_valid']}")
    print(f"Performance: {report['performance_estimate']['category']} ({report['performance_estimate']['estimated_time']})")
    print()
    
    if report['validation_results']:
        print("Validation Issues:")
        for result in report['validation_results']:
            print(f"  {result['level'].upper()}: {result['message']}")
            if result['suggestion']:
                print(f"    Suggestion: {result['suggestion']}")
        print()
    
    if report['optimizations']:
        print("Optimization Suggestions:")
        for opt in report['optimizations']:
            print(f"  {opt['message']}")
            if opt['suggestion']:
                print(f"    {opt['suggestion']}")

if __name__ == '__main__':
    main()