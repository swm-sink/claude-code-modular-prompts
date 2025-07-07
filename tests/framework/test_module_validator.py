"""Test module validation and structure."""

import os
import pytest
from pathlib import Path


class TestModuleValidator:
    """Test suite for module validation."""
    
    @pytest.fixture
    def modules_dir(self):
        """Get the modules directory path."""
        return Path(__file__).parent.parent.parent / ".claude" / "modules"
    
    def test_modules_directory_structure(self, modules_dir):
        """Test that modules directory has correct structure."""
        assert modules_dir.exists(), f"Modules directory not found at {modules_dir}"
        
        required_categories = ["security", "quality", "development", "patterns"]
        
        for category in required_categories:
            category_path = modules_dir / category
            assert category_path.exists(), f"Required category {category} not found"
            assert category_path.is_dir(), f"{category} is not a directory"
    
    def test_module_token_budget(self, modules_dir):
        """Test that modules stay within reasonable token budgets."""
        # Rough approximation: 1 token ≈ 4 characters
        # With 200k context window, 20% = 40k tokens = 160k chars max
        standard_limit = 2000 * 4     # 8k chars for standard modules
        complex_limit = 10000 * 4     # 40k chars for complex modules
        extreme_limit = 40000 * 4     # 160k chars for extremely complex modules (20% of 200k context)
        
        for module_file in modules_dir.rglob("*.md"):
            content = module_file.read_text()
            char_count = len(content)
            
            # Determine appropriate limit based on module type
            if "patterns" in str(module_file):
                # Pattern modules can be complex
                assert char_count <= extreme_limit, \
                    f"Module {module_file.relative_to(modules_dir)} exceeds extreme limit ({char_count} chars > {extreme_limit})"
            elif "testing" in str(module_file) or "development" in str(module_file):
                # Development and testing modules can be moderately complex
                assert char_count <= complex_limit, \
                    f"Module {module_file.relative_to(modules_dir)} exceeds complex limit ({char_count} chars > {complex_limit})"
            elif "security" in str(module_file) or "quality" in str(module_file):
                # Security and quality modules can be moderately complex
                assert char_count <= complex_limit, \
                    f"Module {module_file.relative_to(modules_dir)} exceeds complex limit ({char_count} chars > {complex_limit})"
            elif "planning" in str(module_file) or "automation" in str(module_file):
                # Planning and automation modules can be moderately complex
                assert char_count <= complex_limit, \
                    f"Module {module_file.relative_to(modules_dir)} exceeds complex limit ({char_count} chars > {complex_limit})"
            else:
                # Other modules should stay compact
                assert char_count <= standard_limit, \
                    f"Module {module_file.relative_to(modules_dir)} exceeds standard limit ({char_count} chars > {standard_limit})"
    
    def test_no_redundancy_between_modules(self, modules_dir):
        """Test that modules don't duplicate functionality."""
        module_purposes = {}
        
        for module_file in modules_dir.rglob("*.md"):
            content = module_file.read_text()
            
            # Extract purpose/description
            lines = content.split('\n')
            purpose_lines = [line for line in lines if 'purpose' in line.lower() or 'description' in line.lower()]
            
            if purpose_lines:
                purpose = ' '.join(purpose_lines[:3])  # First 3 purpose lines
                
                # Check for similar purposes
                for existing_module, existing_purpose in module_purposes.items():
                    if existing_module != module_file:
                        # Simple similarity check (could be more sophisticated)
                        overlap = len(set(purpose.split()) & set(existing_purpose.split()))
                        if overlap > 10:  # If more than 10 words overlap
                            import warnings
                            warnings.warn(f"Potential redundancy between {module_file.name} and {existing_module.name}")
                
                module_purposes[module_file] = purpose
    
    def test_module_has_metadata(self, modules_dir):
        """Test that modules have required metadata."""
        for module_file in modules_dir.rglob("*.md"):
            content = module_file.read_text()
            
            # Check for version table at the beginning
            lines = content.split('\n')
            assert len(lines) >= 3, f"Module {module_file.relative_to(modules_dir)} too short"
            assert lines[0].startswith('| version'), f"Module {module_file.relative_to(modules_dir)} missing version table"
            
            # Check for metadata section - modules use XML structure
            assert any(pattern in content for pattern in [
                "<metadata>", "## Metadata", 'name="', "<module name=", "<purpose>"
            ]), f"Module {module_file.relative_to(modules_dir)} missing metadata"
    
    def test_module_has_implementation(self, modules_dir):
        """Test that modules contain actual implementation."""
        for module_file in modules_dir.rglob("*.md"):
            content = module_file.read_text()
            
            # Modules should have implementation details - flexible for XML or markdown
            assert any(keyword in content for keyword in [
                "<implementation>", "## Implementation", "### Process",
                "### Steps", "### Workflow", "### Approach", "<actions>",
                "<phase ", "<process>", "<workflow>"
            ]), f"Module {module_file.relative_to(modules_dir)} missing implementation details"


class TestModuleDependencies:
    """Test module dependency management."""
    
    @pytest.fixture
    def modules_dir(self):
        """Get the modules directory path."""
        return Path(__file__).parent.parent.parent / ".claude" / "modules"
    
    def test_declared_dependencies_exist(self, modules_dir):
        """Test that all declared module dependencies exist."""
        for module_file in modules_dir.rglob("*.md"):
            content = module_file.read_text()
            
            # Find dependency declarations
            if "<dependency>" in content or "dependencies:" in content:
                lines = content.split('\n')
                for line in lines:
                    if "dependency" in line and ".md" in line:
                        # Extract module reference
                        import re
                        matches = re.findall(r'modules/[\w/\-]+\.md', line)
                        for match in matches:
                            dep_path = modules_dir.parent / match
                            assert dep_path.exists(), \
                                f"Module {module_file.name} references non-existent dependency {match}"
    
    def test_no_circular_dependencies(self, modules_dir):
        """Test that there are no circular dependencies."""
        dependencies = {}
        
        # Build dependency graph
        for module_file in modules_dir.rglob("*.md"):
            content = module_file.read_text()
            module_name = str(module_file.relative_to(modules_dir))
            dependencies[module_name] = []
            
            # Extract dependencies
            import re
            matches = re.findall(r'modules/([\w/\-]+)\.md', content)
            for match in matches:
                dependencies[module_name].append(f"{match}.md")
        
        # Check for cycles using DFS
        def has_cycle(node, visited, rec_stack):
            visited[node] = True
            rec_stack[node] = True
            
            for neighbor in dependencies.get(node, []):
                if neighbor not in visited:
                    if has_cycle(neighbor, visited, rec_stack):
                        return True
                elif rec_stack.get(neighbor, False):
                    return True
            
            rec_stack[node] = False
            return False
        
        visited = {}
        rec_stack = {}
        
        for module in dependencies:
            if module not in visited:
                assert not has_cycle(module, visited, rec_stack), \
                    f"Circular dependency detected involving {module}"