# Anti-Pattern Detection

**Purpose**: Real-time detection and prevention of common anti-patterns in LLM-generated code including god objects, testing theatre, and hallucinated dependencies.

**Usage**: 
- Detect god objects through responsibility analysis and method counting
- Identify testing theatre with non-functional test validation
- Prevent premature optimization by analyzing performance impact
- Catch hallucinated dependencies and non-existent APIs
- Provide immediate feedback with alternative pattern suggestions

**Compatibility**: 
- **Works with**: quality-metrics, framework-validation, testing-framework, code analysis
- **Requires**: Code analysis capabilities and pattern recognition
- **Conflicts**: None (universal quality enhancement)

**Implementation**:
```python
# Anti-pattern detection system
class AntiPatternDetector:
    def __init__(self):
        self.patterns = {
            'god_object': GodObjectDetector(),
            'testing_theatre': TestingTheatreDetector(),
            'premature_optimization': PrematureOptimizationDetector(),
            'hallucinated_dependency': HallucinatedDependencyDetector()
        }
    
    def analyze_code(self, code_content, file_path):
        detected_patterns = []
        
        for pattern_name, detector in self.patterns.items():
            if detector.detect(code_content, file_path):
                severity = detector.get_severity()
                suggestions = detector.get_suggestions()
                detected_patterns.append({
                    'pattern': pattern_name,
                    'severity': severity,
                    'suggestions': suggestions,
                    'location': detector.get_location()
                })
        
        return AntiPatternReport(detected_patterns)

# God object detection
class GodObjectDetector:
    def detect(self, code_content, file_path):
        # Analyze class structure
        classes = self.extract_classes(code_content)
        
        for class_info in classes:
            # Check for excessive responsibilities
            if self.has_excessive_responsibilities(class_info):
                return True
                
        return False
    
    def has_excessive_responsibilities(self, class_info):
        # Multiple indicators of god object anti-pattern
        method_count = len(class_info['methods'])
        domain_count = self.count_responsibility_domains(class_info['methods'])
        file_size = class_info['line_count']
        import_domains = self.count_import_domains(class_info['imports'])
        
        return (method_count > 10 and domain_count > 3) or \
               (file_size > 500 and domain_count > 2) or \
               (import_domains > 5)
    
    def get_suggestions(self):
        return [
            "Extract distinct responsibilities into separate classes",
            "Use composition pattern to combine functionality",
            "Implement service layer for complex operations",
            "Apply single responsibility principle",
            "Consider factory or builder patterns for object creation"
        ]

# Testing theatre detection
class TestingTheatreDetector:
    def detect(self, code_content, file_path):
        if not self.is_test_file(file_path):
            return False
            
        tests = self.extract_test_methods(code_content)
        
        for test in tests:
            if self.is_non_functional_test(test):
                return True
                
        return False
    
    def is_non_functional_test(self, test_method):
        # Check for common testing theatre patterns
        has_assertions = self.has_meaningful_assertions(test_method)
        tests_behavior = self.tests_actual_behavior(test_method)
        has_setup = self.has_proper_setup(test_method)
        
        return not (has_assertions and tests_behavior and has_setup)
    
    def get_suggestions(self):
        return [
            "Add meaningful assertions that validate actual behavior",
            "Test edge cases and error conditions",
            "Verify state changes and side effects",
            "Use proper test data setup and teardown",
            "Focus on testing business logic, not implementation details"
        ]

# Hallucinated dependency detection
class HallucinatedDependencyDetector:
    def detect(self, code_content, file_path):
        imports = self.extract_imports(code_content)
        
        for import_statement in imports:
            if self.is_hallucinated_import(import_statement):
                return True
                
        return False
    
    def is_hallucinated_import(self, import_statement):
        # Check against known library database
        library_name = self.extract_library_name(import_statement)
        
        # Common hallucinated libraries
        hallucinated_libs = [
            'claude_api',  # Claude doesn't have an official API library
            'gpt4_client',  # Generic sounding but non-existent
            'automl_magic',  # Too-good-to-be-true naming
            'perfect_parser'  # Suspiciously perfect naming
        ]
        
        return library_name in hallucinated_libs or \
               self.has_suspicious_naming_pattern(library_name)

# Real-time feedback system
def provide_real_time_feedback(code_content, file_path):
    detector = AntiPatternDetector()
    report = detector.analyze_code(code_content, file_path)
    
    if report.has_issues():
        feedback = {
            'status': 'warning',
            'issues': report.get_issues(),
            'suggestions': report.get_all_suggestions(),
            'severity': report.get_max_severity()
        }
        return feedback
    
    return {'status': 'clean', 'message': 'No anti-patterns detected'}
```

**Category**: quality | **Complexity**: high | **Time**: 4 hours