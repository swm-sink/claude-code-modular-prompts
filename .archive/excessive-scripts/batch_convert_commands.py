#!/usr/bin/env python3
"""
Batch Command Converter for Claude Code File Format Converter v2.0
Systematically converts all commands using the enhanced /task template pattern.
"""

import os
import yaml
import re
import shutil
from pathlib import Path
from typing import Dict, List, Any, Optional
from datetime import datetime
import argparse


class BatchCommandConverter:
    """Converts command templates to v2.0 enhanced format."""
    
    def __init__(self, project_root: str = None):
        self.project_root = Path(project_root or os.getcwd())
        self.commands_dir = self.project_root / ".claude" / "commands"
        self.template_file = self.commands_dir / "core" / "task.md"
        self.backup_dir = self.project_root / "backups" / f"pre-v2-conversion-{datetime.now().strftime('%Y%m%d-%H%M%S')}"
        
        # Category-specific configurations
        self.category_configs = {
            "core": {"tags": ["development", "implementation", "core"], "output_format": "structured"},
            "quality": {"tags": ["testing", "validation", "quality"], "output_format": "structured"},
            "specialized": {"tags": ["advanced", "specialized", "orchestration"], "output_format": "structured"},
            "meta": {"tags": ["meta", "adaptation", "configuration"], "output_format": "text"},
            "development": {"tags": ["development", "setup", "api"], "output_format": "code"},
            "devops": {"tags": ["devops", "deployment", "cicd"], "output_format": "structured"},
            "testing": {"tags": ["testing", "quality", "automation"], "output_format": "structured"},
            "database": {"tags": ["database", "data", "migration"], "output_format": "structured"},
            "security": {"tags": ["security", "audit", "validation"], "output_format": "structured"},
            "monitoring": {"tags": ["monitoring", "performance", "analytics"], "output_format": "structured"},
        }

    def create_backup(self):
        """Create backup of all commands before conversion."""
        print(f"Creating backup at: {self.backup_dir}")
        self.backup_dir.mkdir(parents=True, exist_ok=True)
        shutil.copytree(self.commands_dir, self.backup_dir / "commands")
        print("✅ Backup created successfully")

    def load_template(self) -> Dict[str, Any]:
        """Load the enhanced template from /task command."""
        if not self.template_file.exists():
            raise FileNotFoundError(f"Template file not found: {self.template_file}")
        
        content = self.template_file.read_text(encoding='utf-8')
        frontmatter, body = self._extract_yaml_frontmatter(content)
        
        return {
            "frontmatter": frontmatter,
            "body": body,
            "xml_structure": self._extract_xml_structure(body)
        }

    def convert_command(self, file_path: Path, dry_run: bool = False) -> Dict[str, Any]:
        """Convert a single command to v2.0 format."""
        if not file_path.exists():
            return {"success": False, "error": f"File not found: {file_path}"}
        
        try:
            # Read original content
            original_content = file_path.read_text(encoding='utf-8')
            original_frontmatter, original_body = self._extract_yaml_frontmatter(original_content)
            
            if not original_frontmatter:
                return {"success": False, "error": "No YAML frontmatter found"}
            
            # Determine category from file path
            category = self._determine_category(file_path)
            
            # Generate enhanced frontmatter
            enhanced_frontmatter = self._enhance_frontmatter(original_frontmatter, category)
            
            # Generate enhanced body with XML structure
            enhanced_body = self._enhance_body(original_body, original_frontmatter, category)
            
            # Combine enhanced content
            new_content = self._combine_content(enhanced_frontmatter, enhanced_body)
            
            if not dry_run:
                # Write enhanced content
                file_path.write_text(new_content, encoding='utf-8')
            
            return {
                "success": True,
                "file": str(file_path),
                "category": category,
                "enhancements": self._count_enhancements(original_frontmatter, enhanced_frontmatter),
                "xml_tags_added": self._count_xml_tags(enhanced_body),
                "size_change": f"{len(original_content)} → {len(new_content)} bytes"
            }
            
        except Exception as e:
            return {"success": False, "error": str(e), "file": str(file_path)}

    def batch_convert_category(self, category: str, dry_run: bool = False) -> Dict[str, Any]:
        """Convert all commands in a specific category."""
        category_dir = self.commands_dir / category
        if not category_dir.exists():
            return {"success": False, "error": f"Category directory not found: {category}"}
        
        results = {
            "category": category,
            "total_files": 0,
            "converted": 0,
            "failed": 0,
            "results": []
        }
        
        # Find all .md files in category
        md_files = list(category_dir.glob("*.md"))
        results["total_files"] = len(md_files)
        
        for file_path in md_files:
            # Skip the template file itself
            if file_path.name == "task.md" and category == "core":
                continue
                
            result = self.convert_command(file_path, dry_run)
            results["results"].append(result)
            
            if result["success"]:
                results["converted"] += 1
                print(f"✅ Converted: {file_path.name}")
            else:
                results["failed"] += 1
                print(f"❌ Failed: {file_path.name} - {result.get('error', 'Unknown error')}")
        
        return results

    def convert_all_commands(self, dry_run: bool = False) -> Dict[str, Any]:
        """Convert all commands in all categories."""
        print("🚀 Starting batch conversion of all commands...")
        
        if not dry_run:
            self.create_backup()
        
        overall_results = {
            "total_categories": 0,
            "total_files": 0,
            "total_converted": 0,
            "total_failed": 0,
            "category_results": {}
        }
        
        # Get all category directories
        categories = [d.name for d in self.commands_dir.iterdir() if d.is_dir()]
        overall_results["total_categories"] = len(categories)
        
        for category in categories:
            print(f"\n📁 Processing category: {category}")
            result = self.batch_convert_category(category, dry_run)
            
            overall_results["category_results"][category] = result
            overall_results["total_files"] += result["total_files"]
            overall_results["total_converted"] += result["converted"]
            overall_results["total_failed"] += result["failed"]
        
        # Print summary
        print(f"\n📊 CONVERSION SUMMARY:")
        print(f"   Categories: {overall_results['total_categories']}")
        print(f"   Total Files: {overall_results['total_files']}")
        print(f"   Converted: {overall_results['total_converted']}")
        print(f"   Failed: {overall_results['total_failed']}")
        
        if overall_results["total_failed"] == 0:
            print("🎉 All conversions completed successfully!")
        else:
            print(f"⚠️  {overall_results['total_failed']} conversions failed - check results for details")
        
        return overall_results

    def _extract_yaml_frontmatter(self, content: str):
        """Extract YAML frontmatter from markdown content."""
        if not content.startswith('---'):
            return {}, content
        
        try:
            parts = content.split('---', 2)
            if len(parts) < 3:
                return {}, content
            
            yaml_content = parts[1]
            body_content = parts[2]
            
            frontmatter = yaml.safe_load(yaml_content) or {}
            return frontmatter, body_content
        except yaml.YAMLError:
            return {}, content

    def _determine_category(self, file_path: Path) -> str:
        """Determine category from file path."""
        # Get the parent directory name
        category = file_path.parent.name
        return category if category in self.category_configs else "core"

    def _enhance_frontmatter(self, original: Dict[str, Any], category: str) -> Dict[str, Any]:
        """Generate enhanced v2.0 frontmatter."""
        enhanced = {}
        
        # Convert old 'name' field to 'command' (remove leading slash)
        if "name" in original:
            command_name = original["name"].lstrip("/")
            enhanced["command"] = command_name
        else:
            enhanced["command"] = original.get("command", "unknown")
        
        # Enhanced description
        enhanced["description"] = original.get("description", f"Enhanced {category} command with v2.0 capabilities")
        
        # Category from file location or original
        enhanced["category"] = original.get("category", category)
        
        # Generate parameters from usage if available
        enhanced["parameters"] = self._generate_parameters(original)
        
        # Generate usage examples
        enhanced["usage_examples"] = self._generate_usage_examples(enhanced["command"], category)
        
        # Generate prerequisites
        enhanced["prerequisites"] = self._generate_prerequisites(category)
        
        # Output format from category config
        enhanced["output_format"] = self.category_configs.get(category, {}).get("output_format", "structured")
        
        # Tags from category config plus custom
        base_tags = self.category_configs.get(category, {}).get("tags", ["enhanced"])
        enhanced["tags"] = base_tags + ["v2-enhanced"]
        
        # Version and metadata
        enhanced["version"] = "2.0"
        enhanced["author"] = "lusaka-template-library"
        enhanced["last_updated"] = datetime.now().strftime("%Y-%m-%d")
        
        # Preserve allowed-tools
        enhanced["allowed-tools"] = original.get("allowed-tools", original.get("tools", ["Read", "Write", "Edit"]))
        
        return enhanced

    def _generate_parameters(self, original: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Generate parameter definitions from original metadata."""
        parameters = []
        
        # Check if usage pattern suggests parameters
        usage = original.get("usage", "")
        if "[" in usage and "]" in usage:
            # Extract parameter patterns
            param_pattern = r'\[(.*?)\]'
            param_matches = re.findall(param_pattern, usage)
            
            for match in param_matches:
                parameters.append({
                    "name": match.upper().replace(" ", "_"),
                    "type": "string",
                    "required": True,
                    "description": f"Description of {match.lower()} parameter"
                })
        
        # Default parameter if none found
        if not parameters:
            command_name = original.get("name", original.get("command", "command")).lstrip("/")
            parameters.append({
                "name": "ARGUMENTS",
                "type": "string", 
                "required": False,
                "description": f"Arguments for {command_name} command"
            })
        
        return parameters

    def _generate_usage_examples(self, command: str, category: str) -> List[str]:
        """Generate usage examples based on command and category."""
        examples = [
            f"/{command} implement new feature",
            f"/{command} analyze current status",
            f"/{command} optimize performance"
        ]
        
        # Category-specific examples
        if category == "testing":
            examples = [
                f"/{command} run unit tests",
                f"/{command} validate integration",
                f"/{command} check test coverage"
            ]
        elif category == "devops":
            examples = [
                f"/{command} deploy to staging",
                f"/{command} setup production environment",
                f"/{command} configure monitoring"
            ]
        elif category == "database":
            examples = [
                f"/{command} migrate schema",
                f"/{command} backup production data",
                f"/{command} restore from backup"
            ]
        
        return examples

    def _generate_prerequisites(self, category: str) -> List[str]:
        """Generate prerequisites based on category."""
        common = ["Git repository initialized", "Project dependencies installed"]
        
        category_specific = {
            "devops": ["Docker installed", "CI/CD environment configured"],
            "database": ["Database connection configured", "Migration tools available"],
            "testing": ["Test framework installed", "Test environment configured"],
            "development": ["Development environment setup", "IDE configured"]
        }
        
        return common + category_specific.get(category, ["Development environment configured"])

    def _enhance_body(self, original_body: str, original_frontmatter: Dict, category: str) -> str:
        """Generate enhanced body with XML structure."""
        command_name = original_frontmatter.get("name", original_frontmatter.get("command", "command")).lstrip("/")
        
        # Extract key information from original body
        title_match = re.search(r'^#\s+(.+)', original_body, re.MULTILINE)
        original_title = title_match.group(1) if title_match else f"/{command_name} - Enhanced Command"
        
        # Build enhanced body with XML structure
        enhanced_body = f"""
# {original_title}

<context type="project">
{category.title()} command for lusaka template library specializing in Claude Code command development with comprehensive functionality and v2.0 enhancements.
</context>

<instructions>
Execute {category} operations using industry best practices and systematic approach. Process $ARGUMENTS with comprehensive analysis and implementation.
</instructions>

## Usage Examples

<examples>
<example>
<input>/{command_name} implement core functionality</input>
<expected_output>Complete implementation with proper structure, error handling, and documentation</expected_output>
</example>
<example>
<input>/{command_name} analyze current state</input>
<expected_output>Detailed analysis with actionable insights and recommendations</expected_output>
</example>
<example>
<input>/{command_name} optimize performance</input>
<expected_output>Performance improvements with metrics and validation</expected_output>
</example>
</examples>

## Implementation Workflow

<workflow type="sequential">
<task priority="high">
**Analysis Phase**: Understand requirements and context
- Parse $ARGUMENTS for specific requirements
- Identify affected components and dependencies
- Determine success criteria and validation approach
</task>

<task priority="high">
**Implementation Phase**: Execute core functionality
- Apply {category}-specific best practices
- Implement required changes with proper error handling
- Ensure compatibility and maintainability
</task>

<task priority="medium">
**Validation Phase**: Verify results and quality
- Test implementation against requirements
- Validate functionality and performance
- Document changes and provide usage guidance
</task>
</workflow>

<automation trigger="completion">
- Validate implementation quality and standards compliance
- Update relevant documentation and examples
- Provide summary of changes and next steps
</automation>

## Original Content

{original_body.strip()}
"""
        
        return enhanced_body

    def _combine_content(self, frontmatter: Dict[str, Any], body: str) -> str:
        """Combine enhanced frontmatter and body into complete content."""
        yaml_content = yaml.dump(frontmatter, default_flow_style=False, sort_keys=False)
        return f"---\n{yaml_content}---{body}"

    def _count_enhancements(self, original: Dict, enhanced: Dict) -> int:
        """Count the number of enhancements added."""
        v2_fields = ["parameters", "usage_examples", "prerequisites", "output_format", "tags", "version", "author", "last_updated"]
        return sum(1 for field in v2_fields if field in enhanced and field not in original)

    def _count_xml_tags(self, content: str) -> int:
        """Count XML tags in content."""
        return len(re.findall(r'<\w+', content))

    def _extract_xml_structure(self, body: str) -> List[str]:
        """Extract XML tag structure from body."""
        xml_tags = re.findall(r'<(\w+)', body)
        return list(set(xml_tags))


def main():
    """Main function with command line interface."""
    parser = argparse.ArgumentParser(description="Batch convert Claude Code commands to v2.0 format")
    parser.add_argument("--category", help="Convert specific category only")
    parser.add_argument("--dry-run", action="store_true", help="Perform dry run without making changes")
    parser.add_argument("--project-root", help="Project root directory")
    
    args = parser.parse_args()
    
    converter = BatchCommandConverter(args.project_root)
    
    try:
        if args.category:
            print(f"🎯 Converting category: {args.category}")
            result = converter.batch_convert_category(args.category, args.dry_run)
            print(f"\n📊 Results: {result['converted']}/{result['total_files']} converted successfully")
        else:
            print("🚀 Converting all commands to v2.0 format")
            result = converter.convert_all_commands(args.dry_run)
            print(f"\n🎉 Conversion completed: {result['total_converted']}/{result['total_files']} files converted")
    
    except Exception as e:
        print(f"❌ Conversion failed: {str(e)}")
        return 1
    
    return 0


if __name__ == "__main__":
    exit(main())