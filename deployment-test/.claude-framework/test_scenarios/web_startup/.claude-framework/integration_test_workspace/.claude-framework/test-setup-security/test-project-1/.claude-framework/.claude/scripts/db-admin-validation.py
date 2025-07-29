#!/usr/bin/env python3
"""
Database Administration Consolidation Validation Script

This script validates that the db-admin consolidation is complete and correct:
1. Verifies all deprecated database commands have proper deprecation notices
2. Validates the unified db-admin command contains all functionality
3. Checks that all operations (migrate, backup, restore, seed) are supported
4. Ensures deprecation notices are consistent and properly formatted
"""

import os
import re
import yaml
from pathlib import Path
from typing import Dict, List, Set, Optional
from datetime import datetime

class DatabaseConsolidationValidator:
    """Validates the database command consolidation."""
    
    def __init__(self, claude_dir: Path):
        self.claude_dir = claude_dir
        self.commands_dir = claude_dir / "commands"
        self.specialized_dir = self.commands_dir / "specialized"
        
        # Expected database operations
        self.expected_operations = {"migrate", "backup", "restore", "seed"}
        
        # Deprecated database commands
        self.deprecated_commands = [
            "db-migrate.md",
            "db-backup.md", 
            "db-restore.md",
            "db-seed.md"
        ]
        
        # Validation results
        self.errors: List[str] = []
        self.warnings: List[str] = []
        self.results: Dict[str, any] = {}
    
    def validate_frontmatter(self, file_path: Path, content: str) -> Dict[str, any]:
        """Validate YAML frontmatter in a command file."""
        lines = content.split('\n')
        if not lines[0].strip() == '---':
            return {"error": "Missing YAML frontmatter opening"}
        
        # Find closing frontmatter delimiter
        end_idx = None
        for i, line in enumerate(lines[1:], 1):
            if line.strip() == '---':
                end_idx = i
                break
        
        if end_idx is None:
            return {"error": "Missing YAML frontmatter closing"}
        
        # Parse YAML frontmatter
        yaml_content = '\n'.join(lines[1:end_idx])
        try:
            frontmatter = yaml.safe_load(yaml_content)
            return {"frontmatter": frontmatter}
        except yaml.YAMLError as e:
            return {"error": f"Invalid YAML: {e}"}
    
    def validate_deprecated_command(self, file_path: Path) -> Dict[str, any]:
        """Validate a deprecated database command."""
        if not file_path.exists():
            return {"error": f"File not found: {file_path}"}
        
        content = file_path.read_text()
        fm_result = self.validate_frontmatter(file_path, content)
        
        if "error" in fm_result:
            return fm_result
        
        frontmatter = fm_result["frontmatter"]
        result = {"frontmatter": frontmatter, "checks": {}}
        
        # Check required deprecation fields
        required_fields = {
            "deprecated": True,
            "deprecation_date": str,
            "deprecation_deadline": str,
            "deprecation_replacement": str,
            "deprecation_reason": str
        }
        
        for field, expected_type in required_fields.items():
            if field not in frontmatter:
                result["checks"][f"missing_{field}"] = False
            elif field == "deprecated":
                result["checks"]["deprecated_true"] = frontmatter[field] is True
            elif expected_type == str:
                result["checks"][f"valid_{field}"] = isinstance(frontmatter[field], str) and len(frontmatter[field]) > 0
        
        # Check deprecation notice in content
        deprecation_notice_pattern = r"⚠️\s*\*\*DEPRECATION NOTICE\*\*\s*⚠️"
        result["checks"]["has_deprecation_notice"] = bool(re.search(deprecation_notice_pattern, content))
        
        # Check replacement command mentioned
        command_name = file_path.stem
        operation = command_name.replace("db-", "")
        expected_replacement = f"/db-admin {operation}"
        result["checks"]["mentions_replacement"] = expected_replacement in content
        
        return result
    
    def validate_unified_command(self) -> Dict[str, any]:
        """Validate the unified db-admin command."""
        admin_file = self.specialized_dir / "db-admin.md"
        
        if not admin_file.exists():
            return {"error": "Unified db-admin command not found"}
        
        content = admin_file.read_text()
        fm_result = self.validate_frontmatter(admin_file, content)
        
        if "error" in fm_result:
            return fm_result
        
        result = {"frontmatter": fm_result["frontmatter"], "checks": {}}
        
        # Check that command is not deprecated
        frontmatter = fm_result["frontmatter"]
        result["checks"]["not_deprecated"] = frontmatter.get("deprecated") is not True
        
        # Check all operations are supported
        for operation in self.expected_operations:
            pattern = f"/db-admin {operation}"
            result["checks"][f"supports_{operation}"] = pattern in content
        
        # Check for comprehensive examples
        result["checks"]["has_examples"] = "<examples>" in content and "</examples>" in content
        
        # Check for proper XML structure
        result["checks"]["has_command_file_xml"] = "<command_file>" in content and "</command_file>" in content
        result["checks"]["has_claude_prompt"] = "<claude_prompt>" in content and "</claude_prompt>" in content
        
        # Check for operation routing logic
        result["checks"]["has_operation_router"] = "## Operation Router" in content
        result["checks"]["has_migrate_section"] = "### MIGRATE Operations" in content
        result["checks"]["has_backup_section"] = "### BACKUP Operations" in content
        result["checks"]["has_restore_section"] = "### RESTORE Operations" in content
        result["checks"]["has_seed_section"] = "### SEED Operations" in content
        
        return result
    
    def validate_consistency(self) -> Dict[str, any]:
        """Validate consistency across all database commands."""
        result = {"checks": {}}
        
        # Check that all deprecated commands have same deprecation date
        deprecation_dates = set()
        deprecation_deadlines = set()
        
        for cmd_file in self.deprecated_commands:
            file_path = self.commands_dir / cmd_file
            if file_path.exists():
                content = file_path.read_text()
                fm_result = self.validate_frontmatter(file_path, content)
                if "frontmatter" in fm_result:
                    fm = fm_result["frontmatter"]
                    if "deprecation_date" in fm:
                        deprecation_dates.add(fm["deprecation_date"])
                    if "deprecation_deadline" in fm:
                        deprecation_deadlines.add(fm["deprecation_deadline"])
        
        result["checks"]["consistent_deprecation_dates"] = len(deprecation_dates) <= 1
        result["checks"]["consistent_deprecation_deadlines"] = len(deprecation_deadlines) <= 1
        
        # Check that all commands reference the same replacement
        replacements = set()
        for cmd_file in self.deprecated_commands:
            file_path = self.commands_dir / cmd_file
            if file_path.exists():
                content = file_path.read_text()
                fm_result = self.validate_frontmatter(file_path, content)
                if "frontmatter" in fm_result:
                    fm = fm_result["frontmatter"]
                    if "deprecation_replacement" in fm:
                        base_replacement = fm["deprecation_replacement"].split()[0]  # Get "/db-admin" part
                        replacements.add(base_replacement)
        
        result["checks"]["consistent_replacement_command"] = len(replacements) <= 1 and "/db-admin" in replacements
        
        return result
    
    def run_validation(self) -> Dict[str, any]:
        """Run complete validation of database consolidation."""
        print("🔍 Validating Database Administration Consolidation...")
        print("=" * 60)
        
        self.results = {
            "deprecated_commands": {},
            "unified_command": {},
            "consistency": {},
            "summary": {}
        }
        
        # Validate deprecated commands
        print("\n📋 Validating Deprecated Commands:")
        for cmd_file in self.deprecated_commands:
            file_path = self.commands_dir / cmd_file
            print(f"  Checking {cmd_file}...")
            
            validation_result = self.validate_deprecated_command(file_path)
            self.results["deprecated_commands"][cmd_file] = validation_result
            
            if "error" in validation_result:
                self.errors.append(f"{cmd_file}: {validation_result['error']}")
                print(f"    ❌ ERROR: {validation_result['error']}")
            else:
                # Check individual validation results
                checks = validation_result.get("checks", {})
                passed = sum(1 for v in checks.values() if v is True)
                total = len(checks)
                
                if passed == total:
                    print(f"    ✅ All checks passed ({passed}/{total})")
                else:
                    print(f"    ⚠️  Some checks failed ({passed}/{total})")
                    for check, result in checks.items():
                        if not result:
                            self.warnings.append(f"{cmd_file}: Failed check {check}")
                            print(f"      - ❌ {check}")
        
        # Validate unified command
        print("\n🔧 Validating Unified Command:")
        print("  Checking db-admin.md...")
        
        unified_result = self.validate_unified_command()
        self.results["unified_command"] = unified_result
        
        if "error" in unified_result:
            self.errors.append(f"db-admin.md: {unified_result['error']}")
            print(f"    ❌ ERROR: {unified_result['error']}")
        else:
            checks = unified_result.get("checks", {})
            passed = sum(1 for v in checks.values() if v is True)
            total = len(checks)
            
            if passed == total:
                print(f"    ✅ All checks passed ({passed}/{total})")
            else:
                print(f"    ⚠️  Some checks failed ({passed}/{total})")
                for check, result in checks.items():
                    if not result:
                        self.warnings.append(f"db-admin.md: Failed check {check}")
                        print(f"      - ❌ {check}")
        
        # Validate consistency
        print("\n🔄 Validating Consistency:")
        consistency_result = self.validate_consistency()
        self.results["consistency"] = consistency_result
        
        checks = consistency_result.get("checks", {})
        passed = sum(1 for v in checks.values() if v is True)
        total = len(checks)
        
        if passed == total:
            print(f"  ✅ All consistency checks passed ({passed}/{total})")
        else:
            print(f"  ⚠️  Some consistency checks failed ({passed}/{total})")
            for check, result in checks.items():
                if not result:
                    self.warnings.append(f"Consistency: Failed check {check}")
                    print(f"    - ❌ {check}")
        
        # Generate summary
        self.results["summary"] = {
            "total_errors": len(self.errors),
            "total_warnings": len(self.warnings),
            "deprecated_commands_count": len(self.deprecated_commands),
            "unified_command_exists": "error" not in unified_result,
            "validation_timestamp": datetime.now().isoformat()
        }
        
        # Print summary
        print("\n" + "=" * 60)
        print("📊 Validation Summary:")
        print(f"  Deprecated commands validated: {len(self.deprecated_commands)}")
        print(f"  Unified command exists: {'✅' if self.results['summary']['unified_command_exists'] else '❌'}")
        print(f"  Total errors: {len(self.errors)}")
        print(f"  Total warnings: {len(self.warnings)}")
        
        if self.errors:
            print(f"\n❌ ERRORS:")
            for error in self.errors:
                print(f"  - {error}")
        
        if self.warnings:
            print(f"\n⚠️  WARNINGS:")
            for warning in self.warnings:
                print(f"  - {warning}")
        
        if not self.errors and not self.warnings:
            print("\n🎉 Database consolidation validation PASSED! All checks successful.")
        elif not self.errors:
            print(f"\n✅ Database consolidation validation PASSED with {len(self.warnings)} warnings.")
        else:
            print(f"\n❌ Database consolidation validation FAILED with {len(self.errors)} errors.")
        
        return self.results


def main():
    """Main validation entry point."""
    # Find the .claude directory
    current_dir = Path.cwd()
    claude_dir = None
    
    # Look for .claude directory in current path or parent paths
    for path in [current_dir] + list(current_dir.parents):
        potential_claude = path / ".claude"
        if potential_claude.exists() and potential_claude.is_dir():
            claude_dir = potential_claude
            break
    
    if not claude_dir:
        print("❌ Could not find .claude directory")
        exit(1)
    
    print(f"📁 Using Claude directory: {claude_dir}")
    
    validator = DatabaseConsolidationValidator(claude_dir)
    results = validator.run_validation()
    
    # Exit with appropriate code
    if validator.errors:
        exit(1)
    else:
        exit(0)


if __name__ == "__main__":
    main()