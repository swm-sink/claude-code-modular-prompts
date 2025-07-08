"""Comprehensive test suite for the validation tool."""

import os
import sys
import pytest
import tempfile
from pathlib import Path

# Add parent directory to path to import validate
sys.path.insert(0, str(Path(__file__).parent.parent))
from scripts import validate


class TestVersionTable:
    """Test version table validation."""
    
    def setup_method(self, method):
        """Save and restore working directory."""
        self.original_cwd = os.getcwd()
    
    def teardown_method(self, method):
        """Restore working directory."""
        os.chdir(self.original_cwd)
    
    def test_valid_version_table(self, tmp_path):
        """Test that valid version tables pass validation."""
        # Create test structure
        modules_dir = tmp_path / ".claude" / "modules"
        modules_dir.mkdir(parents=True, exist_ok=True)
        test_file = modules_dir / "test.md"
        test_file.write_text("""| version | last_updated | status |
|---------|--------------|--------|
| 1.0.0   | 2025-07-08   | stable |

# Test Module

────────────────────────────────────────────────────────────────────────────────

```xml
<module name="test">
  <purpose>Test module</purpose>
</module>
```
""")
        
        # Change to temp directory
        os.chdir(tmp_path)
        
        issues = validate.check_version_table()
        assert len(issues) == 0
    
    def test_missing_version_table(self, tmp_path):
        """Test that missing version tables are detected."""
        test_file = tmp_path / ".claude" / "modules" / "test.md"
        test_file.parent.mkdir(parents=True, exist_ok=True)
        test_file.write_text("""# Test Module

Content without version table.
""")
        
        os.chdir(tmp_path)
        issues = validate.check_version_table()
        assert any("Missing version table" in issue for issue in issues)
    
    def test_invalid_version_format(self, tmp_path):
        """Test that invalid version formats are detected."""
        test_file = tmp_path / ".claude" / "modules" / "test.md"
        test_file.parent.mkdir(parents=True, exist_ok=True)
        test_file.write_text("""| version | last_updated | status |
|---------|--------------|--------|
| v1.0    | 2025-01-08   | stable |
""")
        
        os.chdir(tmp_path)
        issues = validate.check_version_table()
        assert any("Invalid version format" in issue for issue in issues)
    
    def test_invalid_date_format(self, tmp_path):
        """Test that invalid date formats are detected."""
        test_file = tmp_path / ".claude" / "modules" / "test.md"
        test_file.parent.mkdir(parents=True, exist_ok=True)
        test_file.write_text("""| version | last_updated | status |
|---------|--------------|--------|
| 1.0.0   | 01/08/2025   | stable |
""")
        
        os.chdir(tmp_path)
        issues = validate.check_version_table()
        assert any("Invalid date format" in issue for issue in issues)
    
    def test_invalid_status(self, tmp_path):
        """Test that invalid status values are detected."""
        test_file = tmp_path / ".claude" / "modules" / "test.md"
        test_file.parent.mkdir(parents=True, exist_ok=True)
        test_file.write_text("""| version | last_updated | status |
|---------|--------------|--------|
| 1.0.0   | 2025-01-08   | active |
""")
        
        os.chdir(tmp_path)
        issues = validate.check_version_table()
        assert any("Invalid status" in issue for issue in issues)


class TestHorizontalSeparators:
    """Test horizontal separator validation."""
    
    def setup_method(self, method):
        """Save and restore working directory."""
        self.original_cwd = os.getcwd()
    
    def teardown_method(self, method):
        """Restore working directory."""
        os.chdir(self.original_cwd)
    
    def test_valid_separator(self, tmp_path):
        """Test that valid separators pass validation."""
        test_file = tmp_path / ".claude" / "modules" / "test.md"
        test_file.parent.mkdir(parents=True, exist_ok=True)
        separator = '─' * 80
        test_file.write_text(f"""| version | last_updated | status |
|---------|--------------|--------|
| 1.0.0   | 2025-07-08   | stable |

# Test Module

{separator}

Content here.
""")
        
        os.chdir(tmp_path)
        issues = validate.check_horizontal_separators()
        assert len([i for i in issues if "test.md" in i]) == 0
    
    def test_missing_separator(self, tmp_path):
        """Test that missing separators are detected."""
        test_file = tmp_path / ".claude" / "modules" / "test.md"
        test_file.parent.mkdir(parents=True, exist_ok=True)
        test_file.write_text("""| version | last_updated | status |
|---------|--------------|--------|
| 1.0.0   | 2025-07-08   | stable |

# Test Module

Content without separator.
""")
        
        os.chdir(tmp_path)
        issues = validate.check_horizontal_separators()
        assert any("Missing horizontal separator" in issue for issue in issues)
    
    def test_wrong_separator_length(self, tmp_path):
        """Test that wrong separator lengths are detected."""
        test_file = tmp_path / ".claude" / "modules" / "test.md"
        test_file.parent.mkdir(parents=True, exist_ok=True)
        test_file.write_text("""| version | last_updated | status |
|---------|--------------|--------|
| 1.0.0   | 2025-07-08   | stable |

# Test Module

────────────────────────

Content with short separator.
""")
        
        os.chdir(tmp_path)
        issues = validate.check_horizontal_separators()
        assert any("Missing horizontal separator" in issue for issue in issues)


class TestXMLBlocks:
    """Test XML block validation."""
    
    def setup_method(self, method):
        """Save and restore working directory."""
        self.original_cwd = os.getcwd()
    
    def teardown_method(self, method):
        """Restore working directory."""
        os.chdir(self.original_cwd)
    
    def test_valid_xml_blocks(self, tmp_path):
        """Test that properly wrapped XML blocks pass validation."""
        test_file = tmp_path / ".claude" / "modules" / "test.md"
        test_file.parent.mkdir(parents=True, exist_ok=True)
        test_file.write_text("""| version | last_updated | status |
|---------|--------------|--------|
| 1.0.0   | 2025-07-08   | stable |

# Test Module

```xml
<module name="test">
  <purpose>Test module</purpose>
</module>
```
""")
        
        os.chdir(tmp_path)
        issues = validate.check_xml_blocks()
        assert len([i for i in issues if "test.md" in i]) == 0
    
    def test_unwrapped_xml(self, tmp_path):
        """Test that unwrapped XML content is detected."""
        test_file = tmp_path / ".claude" / "modules" / "test.md"
        test_file.parent.mkdir(parents=True, exist_ok=True)
        test_file.write_text("""| version | last_updated | status |
|---------|--------------|--------|
| 1.0.0   | 2025-07-08   | stable |

# Test Module

<module name="test">
  <purpose>Test module without xml wrapper</purpose>
</module>
""")
        
        os.chdir(tmp_path)
        issues = validate.check_xml_blocks()
        assert any("XML content not wrapped" in issue for issue in issues)
    
    def test_unclosed_xml_block(self, tmp_path):
        """Test that unclosed XML blocks are detected."""
        test_file = tmp_path / ".claude" / "modules" / "test.md"
        test_file.parent.mkdir(parents=True, exist_ok=True)
        test_file.write_text("""| version | last_updated | status |
|---------|--------------|--------|
| 1.0.0   | 2025-07-08   | stable |

# Test Module

```xml
<module name="test">
  <purpose>Test module without closing backticks</purpose>
</module>
""")
        
        os.chdir(tmp_path)
        issues = validate.check_xml_blocks()
        assert any("Unclosed ```xml block" in issue for issue in issues)


class TestFormatConsistency:
    """Test format consistency validation."""
    
    def setup_method(self, method):
        """Save and restore working directory."""
        self.original_cwd = os.getcwd()
    
    def teardown_method(self, method):
        """Restore working directory."""
        os.chdir(self.original_cwd)
    
    def test_missing_empty_line_after_version(self, tmp_path):
        """Test that missing empty line after version table is detected."""
        test_file = tmp_path / ".claude" / "modules" / "test.md"
        test_file.parent.mkdir(parents=True, exist_ok=True)
        test_file.write_text("""| version | last_updated | status |
|---------|--------------|--------|
| 1.0.0   | 2025-07-08   | stable |
# Test Module

Content here.
""")
        
        os.chdir(tmp_path)
        issues = validate.check_format_consistency()
        assert any("Missing empty line after version table" in issue for issue in issues)
    
    def test_missing_empty_line_after_separator(self, tmp_path):
        """Test that missing empty line after separator is detected."""
        test_file = tmp_path / ".claude" / "modules" / "test.md"
        test_file.parent.mkdir(parents=True, exist_ok=True)
        separator = '─' * 80
        test_file.write_text(f"""| version | last_updated | status |
|---------|--------------|--------|
| 1.0.0   | 2025-07-08   | stable |

# Test Module

{separator}
Content without empty line after separator.
""")
        
        os.chdir(tmp_path)
        issues = validate.check_format_consistency()
        assert any("Missing empty line after separator" in issue for issue in issues)
    
    def test_file_too_short(self, tmp_path):
        """Test that files that are too short are detected."""
        test_file = tmp_path / ".claude" / "modules" / "test.md"
        test_file.parent.mkdir(parents=True, exist_ok=True)
        test_file.write_text("""| version | last_updated | status |
|---------|--------------|--------|
| 1.0.0   | 2025-07-08   | stable |
""")
        
        os.chdir(tmp_path)
        issues = validate.check_format_consistency()
        assert any("File too short" in issue for issue in issues)


class TestCommandDelegation:
    """Test command delegation validation."""
    
    def setup_method(self, method):
        """Save and restore working directory."""
        self.original_cwd = os.getcwd()
    
    def teardown_method(self, method):
        """Restore working directory."""
        os.chdir(self.original_cwd)
    
    def test_orchestrator_commands_no_delegation(self, tmp_path):
        """Test that orchestrator commands don't need delegation blocks."""
        test_file = tmp_path / ".claude" / "commands" / "auto.md"
        test_file.parent.mkdir(parents=True, exist_ok=True)
        test_file.write_text("""| version | last_updated | status |
|---------|--------------|--------|
| 1.0.0   | 2025-07-08   | stable |

# Auto Command

Content without delegation block.
""")
        
        issue = validate.check_command_delegation(test_file)
        assert issue is None
    
    def test_regular_command_needs_delegation(self, tmp_path):
        """Test that regular commands need delegation blocks."""
        test_file = tmp_path / ".claude" / "commands" / "test.md"
        test_file.parent.mkdir(parents=True, exist_ok=True)
        test_file.write_text("""| version | last_updated | status |
|---------|--------------|--------|
| 1.0.0   | 2025-07-08   | stable |

# Test Command

Content without delegation block.
""")
        
        issue = validate.check_command_delegation(test_file)
        assert issue is not None
        assert "Missing delegation block" in issue


class TestModuleReferences:
    """Test module reference validation."""
    
    def test_valid_references(self, tmp_path):
        """Test that valid module references pass validation."""
        cmd_dir = tmp_path / ".claude" / "commands"
        mod_dir = tmp_path / ".claude" / "modules" / "test"
        cmd_dir.mkdir(parents=True, exist_ok=True)
        mod_dir.mkdir(parents=True, exist_ok=True)
        
        # Create referenced module
        mod_file = mod_dir / "test.md"
        mod_file.write_text("# Test Module")
        
        # Create command with reference
        cmd_file = cmd_dir / "test.md"
        cmd_file.write_text("""# Test Command

References modules/test/test.md
""")
        
        # Save original path and temporarily change
        original_cwd = os.getcwd()
        os.chdir(tmp_path)
        
        try:
            issues = validate.check_module_references()
            assert len(issues) == 0
        finally:
            os.chdir(original_cwd)
    
    def test_broken_references(self, tmp_path):
        """Test that broken module references are detected."""
        cmd_dir = tmp_path / ".claude" / "commands"
        cmd_dir.mkdir(parents=True, exist_ok=True)
        
        # Create command with broken reference
        cmd_file = cmd_dir / "test.md"
        cmd_file.write_text("""# Test Command

References modules/nonexistent/module.md
""")
        
        # Save original path and temporarily change
        original_cwd = os.getcwd()
        os.chdir(tmp_path)
        
        try:
            issues = validate.check_module_references()
            assert any("Broken reference" in issue for issue in issues)
        finally:
            os.chdir(original_cwd)


class TestFileLimits:
    """Test file limit validation."""
    
    def setup_method(self, method):
        """Save and restore working directory."""
        self.original_cwd = os.getcwd()
    
    def teardown_method(self, method):
        """Restore working directory."""
        os.chdir(self.original_cwd)
    
    def test_module_limit_exceeded(self, tmp_path):
        """Test that module limit violations are detected."""
        category_dir = tmp_path / ".claude" / "modules" / "test_category"
        category_dir.mkdir(parents=True, exist_ok=True)
        
        # Create 4 modules (limit is 3)
        for i in range(4):
            module_file = category_dir / f"module{i}.md"
            module_file.write_text(f"# Module {i}")
        
        os.chdir(tmp_path)
        issues = validate.check_file_limits()
        assert any("Module limit exceeded" in issue for issue in issues)
        assert any("4/3 modules" in issue for issue in issues)
    
    def test_report_limit_exceeded(self, tmp_path):
        """Test that report limit violations are detected."""
        # Create 6 reports (limit is 5)
        for i in range(6):
            report_file = tmp_path / f"TEST_REPORT_{i}.md"
            report_file.write_text(f"# Report {i}")
        
        os.chdir(tmp_path)
        issues = validate.check_file_limits()
        assert any("Report limit exceeded" in issue for issue in issues)
        assert any("6/5 reports" in issue for issue in issues)
    
    def test_docs_limit_exceeded(self, tmp_path):
        """Test that docs limit violations are detected."""
        docs_subdir = tmp_path / "docs" / "test_docs"
        docs_subdir.mkdir(parents=True, exist_ok=True)
        
        # Create 21 docs (limit is 20)
        for i in range(21):
            doc_file = docs_subdir / f"doc{i}.md"
            doc_file.write_text(f"# Doc {i}")
        
        os.chdir(tmp_path)
        issues = validate.check_file_limits()
        assert any("Docs limit exceeded" in issue for issue in issues)
        assert any("21/20 files" in issue for issue in issues)
    
    def test_limits_within_bounds(self, tmp_path):
        """Test that files within limits pass validation."""
        # Create structure within limits
        category_dir = tmp_path / ".claude" / "modules" / "test_category"
        category_dir.mkdir(parents=True, exist_ok=True)
        
        # Create 3 modules (at limit)
        for i in range(3):
            module_file = category_dir / f"module{i}.md"
            module_file.write_text(f"# Module {i}")
        
        # Create 5 reports (at limit)
        for i in range(5):
            report_file = tmp_path / f"TEST_REPORT_{i}.md"
            report_file.write_text(f"# Report {i}")
        
        os.chdir(tmp_path)
        issues = validate.check_file_limits()
        assert len([i for i in issues if "limit exceeded" in i.lower()]) == 0


class TestPatternUsage:
    """Test pattern usage validation."""
    
    def setup_method(self, method):
        """Save and restore working directory."""
        self.original_cwd = os.getcwd()
    
    def teardown_method(self, method):
        """Restore working directory."""
        os.chdir(self.original_cwd)
    
    def test_valid_pattern_reference(self, tmp_path):
        """Test that valid pattern references pass validation."""
        patterns_dir = tmp_path / ".claude" / "modules" / "patterns"
        patterns_dir.mkdir(parents=True, exist_ok=True)
        
        # Create pattern library
        pattern_lib = patterns_dir / "pattern-library.md"
        pattern_lib.write_text("""# Pattern Library
        
        Pattern: parallel_execution
        Pattern: smart_memoization
        """)
        
        # Create module using patterns
        module_file = patterns_dir / "test.md"
        module_file.write_text("""# Test Module
        
        <uses_pattern from="patterns/pattern-library.md">parallel_execution</uses_pattern>
        <uses_pattern from="patterns/pattern-library.md">smart_memoization</uses_pattern>
        """)
        
        os.chdir(tmp_path)
        issues = validate.check_pattern_usage()
        assert len(issues) == 0
    
    def test_broken_pattern_file_reference(self, tmp_path):
        """Test that broken pattern file references are detected."""
        module_dir = tmp_path / ".claude" / "modules" / "test"
        module_dir.mkdir(parents=True, exist_ok=True)
        
        module_file = module_dir / "test.md"
        module_file.write_text("""# Test Module
        
        <uses_pattern from="patterns/nonexistent.md">some_pattern</uses_pattern>
        """)
        
        os.chdir(tmp_path)
        issues = validate.check_pattern_usage()
        assert any("Broken pattern reference" in issue for issue in issues)
        assert any("nonexistent.md" in issue for issue in issues)
    
    def test_pattern_not_found_in_file(self, tmp_path):
        """Test that patterns not found in referenced file are detected."""
        patterns_dir = tmp_path / ".claude" / "modules" / "patterns"
        patterns_dir.mkdir(parents=True, exist_ok=True)
        
        # Create pattern library without the referenced pattern
        pattern_lib = patterns_dir / "pattern-library.md"
        pattern_lib.write_text("""# Pattern Library
        
        Pattern: different_pattern
        """)
        
        # Create module using non-existent pattern
        module_file = patterns_dir / "test.md"
        module_file.write_text("""# Test Module
        
        <uses_pattern from="patterns/pattern-library.md">nonexistent_pattern</uses_pattern>
        """)
        
        os.chdir(tmp_path)
        issues = validate.check_pattern_usage()
        assert any("Pattern 'nonexistent_pattern' not found" in issue for issue in issues)


class TestDependencyDeclarations:
    """Test dependency declaration validation."""
    
    def setup_method(self, method):
        """Save and restore working directory."""
        self.original_cwd = os.getcwd()
    
    def teardown_method(self, method):
        """Restore working directory."""
        os.chdir(self.original_cwd)
    
    def test_valid_dependencies(self, tmp_path):
        """Test that valid dependencies pass validation."""
        modules_dir = tmp_path / ".claude" / "modules"
        commands_dir = tmp_path / ".claude" / "commands"
        modules_dir.mkdir(parents=True, exist_ok=True)
        commands_dir.mkdir(parents=True, exist_ok=True)
        
        # Create dependency files
        dep1 = modules_dir / "dep1.md"
        dep1.write_text("# Dependency 1")
        
        dep2 = commands_dir / "dep2.md"
        dep2.write_text("# Dependency 2")
        
        # Create file with dependencies
        test_file = modules_dir / "test.md"
        test_file.write_text("""# Test Module
        
        <depends_on>
            modules/dep1.md
            commands/dep2.md
        </depends_on>
        """)
        
        os.chdir(tmp_path)
        issues = validate.check_dependency_declarations()
        assert len(issues) == 0
    
    def test_broken_dependencies(self, tmp_path):
        """Test that broken dependencies are detected."""
        modules_dir = tmp_path / ".claude" / "modules"
        modules_dir.mkdir(parents=True, exist_ok=True)
        
        test_file = modules_dir / "test.md"
        test_file.write_text("""# Test Module
        
        <depends_on>
            modules/nonexistent.md
            commands/missing.md
            some-other-file.md
        </depends_on>
        """)
        
        os.chdir(tmp_path)
        issues = validate.check_dependency_declarations()
        assert len([i for i in issues if "Broken dependency" in i]) >= 3
    
    def test_relative_module_dependencies(self, tmp_path):
        """Test that relative module paths are resolved correctly."""
        modules_dir = tmp_path / ".claude" / "modules" / "test"
        modules_dir.mkdir(parents=True, exist_ok=True)
        
        # Create dependency
        dep_file = modules_dir / "dependency.md"
        dep_file.write_text("# Dependency")
        
        # Create file with relative dependency
        test_file = modules_dir / "test.md"
        test_file.write_text("""# Test Module
        
        <depends_on>
            test/dependency.md
        </depends_on>
        """)
        
        os.chdir(tmp_path)
        issues = validate.check_dependency_declarations()
        assert len(issues) == 0


class TestEdgeCases:
    """Test edge cases and error handling."""
    
    def setup_method(self, method):
        """Save and restore working directory."""
        self.original_cwd = os.getcwd()
    
    def teardown_method(self, method):
        """Restore working directory."""
        os.chdir(self.original_cwd)
    
    def test_empty_file(self, tmp_path):
        """Test handling of empty files."""
        test_file = tmp_path / ".claude" / "modules" / "empty.md"
        test_file.parent.mkdir(parents=True, exist_ok=True)
        test_file.write_text("")
        
        os.chdir(tmp_path)
        issues = validate.check_version_table()
        assert any("Missing version table" in issue for issue in issues)
    
    def test_malformed_version_table(self, tmp_path):
        """Test handling of malformed version tables."""
        test_file = tmp_path / ".claude" / "modules" / "malformed.md"
        test_file.parent.mkdir(parents=True, exist_ok=True)
        test_file.write_text("""| version | last_updated |
|---------|
| 1.0.0   | 2025-01-08
""")
        
        os.chdir(tmp_path)
        issues = validate.check_version_table()
        assert any("Invalid version table format" in issue for issue in issues)
    
    def test_unicode_handling(self, tmp_path):
        """Test handling of Unicode characters."""
        test_file = tmp_path / ".claude" / "modules" / "unicode.md"
        test_file.parent.mkdir(parents=True, exist_ok=True)
        separator = '─' * 80
        test_file.write_text(f"""| version | last_updated | status |
|---------|--------------|--------|
| 1.0.0   | 2025-07-08   | stable |

# Test Module 🚀

{separator}

```xml
<module name="test">
  <purpose>Test with emojis 🎯</purpose>
</module>
```
""")
        
        # Should not raise any Unicode errors
        os.chdir(tmp_path)
        issues = validate.check_horizontal_separators()
        issues.extend(validate.check_xml_blocks())
        # File should be valid
        assert len([i for i in issues if "unicode.md" in i]) == 0


if __name__ == "__main__":
    pytest.main([__file__, "-v"])