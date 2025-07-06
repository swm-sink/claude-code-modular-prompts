#!/usr/bin/env python3
"""
Prompt Search and Retrieval Tool
Search for prompts by category, tags, or content
"""

import json
import re
from pathlib import Path
from typing import Dict, List, Optional, Union
import argparse
from datetime import datetime

class PromptSearcher:
    """Search and retrieve prompts from the storage system"""
    
    def __init__(self, prompts_dir: Path):
        """Initialize with prompts directory"""
        self.prompts_dir = prompts_dir
        self.prompts_cache = {}
        self._load_prompts()
    
    def _load_prompts(self):
        """Load all prompts into cache"""
        for prompt_file in self.prompts_dir.glob('**/*.json'):
            if 'archived' in prompt_file.parts:
                continue
            if prompt_file.name == 'prompt-schema.json':
                continue
            
            try:
                with open(prompt_file, 'r') as f:
                    data = json.load(f)
                    data['_file_path'] = str(prompt_file)
                    self.prompts_cache[data['id']] = data
            except Exception as e:
                print(f"Error loading {prompt_file}: {e}")
    
    def search(self, 
               query: Optional[str] = None,
               category: Optional[str] = None,
               tags: Optional[List[str]] = None,
               version: Optional[str] = None) -> List[Dict]:
        """Search prompts based on criteria"""
        results = []
        
        for prompt_id, prompt in self.prompts_cache.items():
            # Category filter
            if category and prompt.get('category') != category:
                continue
            
            # Version filter
            if version and prompt.get('version') != version:
                continue
            
            # Tag filter
            if tags:
                prompt_tags = set(prompt.get('metadata', {}).get('tags', []))
                if not any(tag in prompt_tags for tag in tags):
                    continue
            
            # Query search
            if query:
                query_lower = query.lower()
                searchable = [
                    prompt.get('name', ''),
                    prompt.get('description', ''),
                    prompt.get('prompt', {}).get('template', ''),
                    ' '.join(prompt.get('metadata', {}).get('tags', []))
                ]
                if not any(query_lower in text.lower() for text in searchable):
                    continue
            
            results.append(prompt)
        
        return sorted(results, key=lambda x: x.get('metadata', {}).get('updated', ''), reverse=True)
    
    def get_prompt(self, prompt_id: str) -> Optional[Dict]:
        """Get a specific prompt by ID"""
        return self.prompts_cache.get(prompt_id)
    
    def get_by_reference(self, reference: str) -> Optional[Dict]:
        """Get prompt by reference (e.g., 'features-api-endpoint-v1.0.0')"""
        # Try direct ID lookup first
        if reference in self.prompts_cache:
            return self.prompts_cache[reference]
        
        # Try to find by filename pattern
        for prompt in self.prompts_cache.values():
            file_path = Path(prompt['_file_path'])
            category = prompt['category']
            prompt_id = prompt['id']
            version = prompt['version']
            expected_name = f"{category}-{prompt_id.replace(f'{category}-', '')}-v{version}.json"
            if file_path.name == f"{reference}.json":
                return prompt
        
        return None
    
    def list_categories(self) -> Dict[str, int]:
        """List all categories with counts"""
        categories = {}
        for prompt in self.prompts_cache.values():
            cat = prompt.get('category', 'unknown')
            categories[cat] = categories.get(cat, 0) + 1
        return categories
    
    def list_tags(self) -> Dict[str, int]:
        """List all tags with counts"""
        tags = {}
        for prompt in self.prompts_cache.values():
            for tag in prompt.get('metadata', {}).get('tags', []):
                tags[tag] = tags.get(tag, 0) + 1
        return sorted(tags.items(), key=lambda x: x[1], reverse=True)
    
    def format_prompt(self, prompt: Dict, variables: Optional[Dict] = None) -> str:
        """Format a prompt with variables"""
        template = prompt.get('prompt', {}).get('template', '')
        
        if not variables:
            return template
        
        # Simple variable replacement (not full Handlebars)
        result = template
        for var_name, var_value in variables.items():
            result = result.replace(f"{{{{{var_name}}}}}", str(var_value))
        
        return result
    
    def print_prompt_info(self, prompt: Dict, detailed: bool = False):
        """Print prompt information"""
        print(f"\n{'='*60}")
        print(f"ID: {prompt['id']}")
        print(f"Name: {prompt['name']}")
        print(f"Version: {prompt['version']}")
        print(f"Category: {prompt['category']}")
        print(f"Description: {prompt['description']}")
        
        metadata = prompt.get('metadata', {})
        print(f"Tags: {', '.join(metadata.get('tags', []))}")
        print(f"Author: {metadata.get('author', 'unknown')}")
        print(f"Updated: {metadata.get('updated', 'unknown')}")
        
        if detailed:
            print(f"\nVariables:")
            for var in prompt.get('prompt', {}).get('variables', []):
                req = "required" if var.get('required', True) else "optional"
                print(f"  - {var['name']} ({var['type']}, {req}): {var['description']}")
            
            print(f"\nPerformance:")
            perf = prompt.get('performance', {})
            print(f"  - Estimated tokens: {perf.get('estimatedTokens', 'unknown')}")
            print(f"  - Complexity: {perf.get('complexity', 'unknown')}")
            print(f"  - Timeout: {perf.get('timeout', 'unknown')}s")


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description='Search and retrieve Claude Code prompts'
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Commands')
    
    # Search command
    search_parser = subparsers.add_parser('search', help='Search prompts')
    search_parser.add_argument('-q', '--query', help='Search query')
    search_parser.add_argument('-c', '--category', help='Filter by category')
    search_parser.add_argument('-t', '--tags', nargs='+', help='Filter by tags')
    search_parser.add_argument('-d', '--detailed', action='store_true', help='Show detailed info')
    
    # Get command
    get_parser = subparsers.add_parser('get', help='Get specific prompt')
    get_parser.add_argument('reference', help='Prompt ID or reference')
    get_parser.add_argument('-f', '--format', action='store_true', help='Show formatted template')
    get_parser.add_argument('-v', '--vars', help='JSON variables for formatting')
    
    # List command
    list_parser = subparsers.add_parser('list', help='List categories or tags')
    list_parser.add_argument('type', choices=['categories', 'tags'], help='What to list')
    
    args = parser.parse_args()
    
    # Initialize searcher
    prompts_dir = Path(__file__).parent.parent / 'prompts'
    searcher = PromptSearcher(prompts_dir)
    
    if args.command == 'search':
        results = searcher.search(
            query=args.query,
            category=args.category,
            tags=args.tags
        )
        
        print(f"Found {len(results)} prompts")
        for prompt in results:
            searcher.print_prompt_info(prompt, detailed=args.detailed)
    
    elif args.command == 'get':
        prompt = searcher.get_by_reference(args.reference)
        if not prompt:
            prompt = searcher.get_prompt(args.reference)
        
        if prompt:
            searcher.print_prompt_info(prompt, detailed=True)
            
            if args.format:
                print(f"\nTemplate:")
                print("-" * 60)
                if args.vars:
                    try:
                        variables = json.loads(args.vars)
                        print(searcher.format_prompt(prompt, variables))
                    except json.JSONDecodeError:
                        print("Error: Invalid JSON for variables")
                        print(prompt.get('prompt', {}).get('template', ''))
                else:
                    print(prompt.get('prompt', {}).get('template', ''))
        else:
            print(f"Prompt not found: {args.reference}")
    
    elif args.command == 'list':
        if args.type == 'categories':
            categories = searcher.list_categories()
            print("\nCategories:")
            for cat, count in categories.items():
                print(f"  {cat}: {count} prompts")
        
        elif args.type == 'tags':
            tags = searcher.list_tags()
            print("\nTags (by frequency):")
            for tag, count in tags[:20]:  # Top 20 tags
                print(f"  {tag}: {count} prompts")
    
    else:
        parser.print_help()


if __name__ == '__main__':
    main()