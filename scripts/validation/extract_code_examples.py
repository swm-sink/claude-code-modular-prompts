#!/usr/bin/env python3
"""
Extract code examples from markdown files for validation.
Part of Agent V24: Example Validator.
"""

import os
import re
import json
from pathlib import Path
from typing import Dict, List, Tuple
from collections import defaultdict

def extract_code_blocks(file_path: str) -> List[Dict[str, str]]:
    """Extract all code blocks from a markdown file."""
    blocks = []
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Pattern to match code blocks with optional language specifier
    pattern = r'```(\w*)\n(.*?)```'
    matches = re.findall(pattern, content, re.DOTALL)
    
    for i, (language, code) in enumerate(matches):
        if not language:
            language = 'unknown'
        
        blocks.append({
            'file': file_path,
            'language': language.lower(),
            'code': code.strip(),
            'line_number': content[:content.find(f'```{language}\n{code}')].count('\n') + 1,
            'index': i
        })
    
    return blocks

def categorize_examples(examples: List[Dict[str, str]]) -> Dict[str, List[Dict[str, str]]]:
    """Categorize code examples by language."""
    categorized = defaultdict(list)
    
    for example in examples:
        categorized[example['language']].append(example)
    
    return dict(categorized)

def main():
    """Main function to extract and categorize all code examples."""
    # Find all markdown files
    md_files = []
    for root, dirs, files in os.walk('.'):
        # Skip certain directories
        if any(skip in root for skip in ['.git', 'node_modules', '__pycache__']):
            continue
        
        for file in files:
            if file.endswith('.md'):
                md_files.append(os.path.join(root, file))
    
    # Extract code examples
    all_examples = []
    for file_path in sorted(md_files):
        examples = extract_code_blocks(file_path)
        all_examples.extend(examples)
    
    # Categorize by language
    categorized = categorize_examples(all_examples)
    
    # Print summary
    print(f"Total markdown files analyzed: {len(md_files)}")
    print(f"Total code examples found: {len(all_examples)}")
    print("\nExamples by language:")
    
    for language, examples in sorted(categorized.items()):
        print(f"  {language}: {len(examples)} examples")
    
    # Save results
    output_file = 'code_examples_extracted.json'
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump({
            'total_files': len(md_files),
            'total_examples': len(all_examples),
            'by_language': {lang: len(exs) for lang, exs in categorized.items()},
            'examples': categorized
        }, f, indent=2)
    
    print(f"\nDetailed results saved to: {output_file}")
    
    return categorized

if __name__ == "__main__":
    main()