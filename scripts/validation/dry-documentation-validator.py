#!/usr/bin/env python3
"""
DRY Documentation Validator
Identifies duplicate documentation content across the framework
"""

import os
import re
import hashlib
from collections import defaultdict
from pathlib import Path
import json

class DRYValidator:
    def __init__(self, root_dir="."):
        self.root_dir = Path(root_dir)
        self.content_hashes = defaultdict(list)
        self.duplicate_patterns = defaultdict(list)
        self.canonical_sources = {}
        
    def find_markdown_files(self):
        """Find all markdown files in the project"""
        return list(self.root_dir.rglob("*.md"))
    
    def extract_content_blocks(self, file_path):
        """Extract meaningful content blocks from a markdown file"""
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract different types of content blocks
        blocks = []
        
        # Headers and their content
        header_pattern = r'^(#{1,6})\s+(.+?)(?=^#{1,6}|\Z)'
        for match in re.finditer(header_pattern, content, re.MULTILINE | re.DOTALL):
            level = len(match.group(1))
            header = match.group(2).strip()
            section_content = match.group(0)
            
            # Skip very short sections
            if len(section_content) > 100:
                blocks.append({
                    'type': 'section',
                    'level': level,
                    'header': header,
                    'content': section_content,
                    'file': str(file_path),
                    'hash': hashlib.md5(section_content.encode()).hexdigest()
                })
        
        # Code blocks
        code_pattern = r'```(\w+)?\n(.*?)```'
        for match in re.finditer(code_pattern, content, re.DOTALL):
            lang = match.group(1) or 'text'
            code_content = match.group(2)
            if len(code_content) > 50:
                blocks.append({
                    'type': 'code',
                    'language': lang,
                    'content': code_content,
                    'file': str(file_path),
                    'hash': hashlib.md5(code_content.encode()).hexdigest()
                })
        
        # XML blocks
        xml_pattern = r'<(\w+)[^>]*>.*?</\1>'
        for match in re.finditer(xml_pattern, content, re.DOTALL):
            xml_content = match.group(0)
            if len(xml_content) > 100:
                blocks.append({
                    'type': 'xml',
                    'content': xml_content,
                    'file': str(file_path),
                    'hash': hashlib.md5(xml_content.encode()).hexdigest()
                })
        
        return blocks
    
    def find_duplicates(self):
        """Find duplicate content across all markdown files"""
        duplicates = defaultdict(list)
        
        md_files = self.find_markdown_files()
        
        # Skip certain directories
        skip_dirs = ['node_modules', '.git', '.pytest_cache', 'agent-communications', 'internal/reports']
        
        for file_path in md_files:
            # Skip files in directories we want to ignore
            if any(skip_dir in str(file_path) for skip_dir in skip_dirs):
                continue
                
            blocks = self.extract_content_blocks(file_path)
            
            for block in blocks:
                duplicates[block['hash']].append(block)
        
        # Filter to only keep actual duplicates
        return {k: v for k, v in duplicates.items() if len(v) > 1}
    
    def find_pattern_duplicates(self):
        """Find similar patterns that may not be exact duplicates"""
        patterns = {
            'command_descriptions': r'/(\w+)\s+(command|-).*?(Purpose|Syntax|Characteristics)',
            'installation_steps': r'(git clone|cp -r|Copy framework|Installation)',
            'tdd_cycle': r'(RED|Test).*?(GREEN|Implement).*?(REFACTOR|Refactor)',
            'framework_principles': r'(Single source|Zero redundancy|Modular composition)',
            'quality_gates': r'(Quality gates?|TDD.*?mandatory|Coverage.*?\d+%)',
            'project_config': r'(PROJECT_CONFIG\.xml|project_configuration|<project_info>)'
        }
        
        pattern_matches = defaultdict(lambda: defaultdict(list))
        
        md_files = self.find_markdown_files()
        skip_dirs = ['node_modules', '.git', '.pytest_cache', 'agent-communications', 'internal/reports']
        
        for file_path in md_files:
            if any(skip_dir in str(file_path) for skip_dir in skip_dirs):
                continue
                
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            for pattern_name, pattern in patterns.items():
                matches = re.finditer(pattern, content, re.IGNORECASE | re.DOTALL)
                for match in matches:
                    context = content[max(0, match.start()-100):min(len(content), match.end()+100)]
                    pattern_matches[pattern_name][str(file_path)].append({
                        'match': match.group(0)[:200],
                        'context': context[:300],
                        'position': match.start()
                    })
        
        return pattern_matches
    
    def suggest_canonical_sources(self, duplicates):
        """Suggest canonical source locations for duplicate content"""
        suggestions = {}
        
        for hash_val, blocks in duplicates.items():
            # Determine best canonical location based on file path
            files = [block['file'] for block in blocks]
            
            # Priority order for canonical sources
            priority_paths = [
                'CLAUDE.md',
                'docs/reference/',
                'docs/getting-started/',
                'docs/user-guide/',
                '.claude/commands/README.md',
                '.claude/modules/README.md'
            ]
            
            canonical = None
            for priority in priority_paths:
                for file in files:
                    if priority in file:
                        canonical = file
                        break
                if canonical:
                    break
            
            if not canonical:
                # Default to shortest path (likely most general location)
                canonical = min(files, key=len)
            
            suggestions[hash_val] = {
                'canonical': canonical,
                'duplicates': [f for f in files if f != canonical],
                'content_preview': blocks[0]['content'][:200] + '...' if len(blocks[0]['content']) > 200 else blocks[0]['content']
            }
        
        return suggestions
    
    def generate_report(self):
        """Generate comprehensive DRY validation report"""
        print("Finding duplicate content blocks...")
        duplicates = self.find_duplicates()
        
        print("Finding pattern duplicates...")
        pattern_duplicates = self.find_pattern_duplicates()
        
        print("Suggesting canonical sources...")
        canonical_suggestions = self.suggest_canonical_sources(duplicates)
        
        report = {
            'summary': {
                'total_duplicate_blocks': len(duplicates),
                'total_files_with_duplicates': len(set(f for blocks in duplicates.values() for block in blocks for f in [block['file']])),
                'pattern_categories': len(pattern_duplicates)
            },
            'exact_duplicates': canonical_suggestions,
            'pattern_duplicates': pattern_duplicates
        }
        
        return report
    
    def save_report(self, report, output_file="dry_validation_report.json"):
        """Save report to file"""
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        
        # Also create a markdown report
        md_report = self.format_markdown_report(report)
        md_file = output_file.replace('.json', '.md')
        with open(md_file, 'w', encoding='utf-8') as f:
            f.write(md_report)
            
        return output_file, md_file
    
    def format_markdown_report(self, report):
        """Format report as markdown"""
        md = "# DRY Documentation Validation Report\n\n"
        md += "## Summary\n\n"
        md += f"- Total duplicate content blocks: {report['summary']['total_duplicate_blocks']}\n"
        md += f"- Files with duplicate content: {report['summary']['total_files_with_duplicates']}\n"
        md += f"- Pattern categories found: {report['summary']['pattern_categories']}\n\n"
        
        md += "## Exact Duplicates\n\n"
        for i, (hash_val, info) in enumerate(report['exact_duplicates'].items(), 1):
            md += f"### Duplicate Block {i}\n"
            md += f"**Canonical Source**: `{info['canonical']}`\n\n"
            md += f"**Duplicated in**:\n"
            for dup in info['duplicates']:
                md += f"- `{dup}`\n"
            md += f"\n**Content Preview**:\n```\n{info['content_preview']}\n```\n\n"
        
        md += "## Pattern Duplicates\n\n"
        for pattern_name, files in report['pattern_duplicates'].items():
            if files:
                md += f"### {pattern_name.replace('_', ' ').title()}\n"
                md += f"Found in {len(files)} files:\n"
                for file in list(files.keys())[:10]:  # Limit to first 10
                    md += f"- `{file}` ({len(files[file])} occurrences)\n"
                md += "\n"
        
        return md

if __name__ == "__main__":
    validator = DRYValidator()
    report = validator.generate_report()
    
    json_file, md_file = validator.save_report(report)
    print(f"\nReport saved to:")
    print(f"- JSON: {json_file}")
    print(f"- Markdown: {md_file}")
    
    print(f"\nSummary:")
    print(f"- Found {report['summary']['total_duplicate_blocks']} duplicate content blocks")
    print(f"- Affecting {report['summary']['total_files_with_duplicates']} files")
    print(f"- {report['summary']['pattern_categories']} pattern categories identified")