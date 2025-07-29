#!/usr/bin/env python3
"""
Comprehensive Command Analysis Script
Analyzes all 102 Claude Code commands for XML structures, security theater, and cleanup needs.
"""

import os
import re
import json
from pathlib import Path
from typing import Dict, List, Set

def analyze_command_file(file_path: str) -> Dict:
    """Analyze a single command file for patterns that need cleanup."""
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        return {"error": f"Failed to read file: {e}"}
    
    analysis = {
        "file_path": file_path,
        "is_deprecated": "/deprecated/" in file_path,
        "has_xml_structures": False,
        "has_security_theater": False,
        "has_python_code": False,
        "has_bash_code": False,
        "xml_patterns": [],
        "security_theater_patterns": [],
        "placeholders": [],
        "line_count": len(content.split('\n')),
        "size_bytes": len(content.encode('utf-8'))
    }
    
    # Check for XML structures
    xml_patterns = [
        r'<command_file>',
        r'<security>',
        r'<validation>',
        r'<input_validation>',
        r'<security_validation>',
        r'<metadata>',
        r'<arguments>',
        r'<examples>',
        r'<claude_prompt>',
        r'<include>',
        r'<!\[CDATA\[',
        r'</[a-zA-Z_]+>'
    ]
    
    for pattern in xml_patterns:
        matches = re.findall(pattern, content, re.IGNORECASE)
        if matches:
            analysis["has_xml_structures"] = True
            analysis["xml_patterns"].extend(matches)
    
    # Check for security theater patterns
    security_patterns = [
        r'input.*validation',
        r'security.*validation',
        r'sanitize.*input',
        r'validate_input',
        r'security_check',
        r'SecurityError',
        r'sanitized_description',
        r'placeholder_validation',
        r'blocked_content',
        r'dangerous patterns',
        r'validation_time',
        r'Performance tracking',
        r'SECURE.*validated successfully'
    ]
    
    for pattern in security_patterns:
        matches = re.findall(pattern, content, re.IGNORECASE)
        if matches:
            analysis["has_security_theater"] = True
            analysis["security_theater_patterns"].extend(matches)
    
    # Check for code blocks
    analysis["has_python_code"] = bool(re.search(r'```python', content))
    analysis["has_bash_code"] = bool(re.search(r'```bash', content))
    
    # Find placeholders
    placeholder_matches = re.findall(r'\[INSERT_[A-Z_]+\]', content)
    analysis["placeholders"] = list(set(placeholder_matches))
    
    return analysis

def categorize_command_priority(file_path: str, analysis: Dict) -> str:
    """Determine priority level for cleanup based on command importance."""
    
    file_name = os.path.basename(file_path)
    directory = os.path.dirname(file_path)
    
    # Critical core commands
    if "/core/" in file_path and file_name in ["task.md", "help.md", "auto.md"]:
        return "CRITICAL"
    
    # Important meta commands
    if "/meta/" in file_path:
        return "HIGH"
    
    # Deprecated commands (lower priority)
    if analysis["is_deprecated"]:
        return "LOW"
    
    # Active development/quality commands
    if any(x in file_path for x in ["/development/", "/quality/", "/testing/"]):
        return "HIGH"
    
    # Security commands
    if "/security/" in file_path:
        return "HIGH"
    
    # Database/DevOps commands
    if any(x in file_path for x in ["/database/", "/devops/"]):
        return "MEDIUM"
    
    # Specialized/experimental commands
    if any(x in file_path for x in ["/specialized/", "dag-", "swarm", "mutation"]):
        return "MEDIUM"
    
    # Default for other active commands
    return "MEDIUM" if not analysis["is_deprecated"] else "LOW"

def determine_cleanup_actions(analysis: Dict) -> List[str]:
    """Determine what cleanup actions are needed for this command."""
    
    actions = []
    
    if analysis["has_xml_structures"]:
        actions.append("Remove XML structures")
    
    if analysis["has_security_theater"]:
        actions.append("Remove security theater code")
    
    if analysis["has_python_code"]:
        actions.append("Remove/simplify Python code blocks")
    
    if len(analysis["placeholders"]) > 0:
        actions.append(f"Validate {len(analysis['placeholders'])} placeholders")
    
    if analysis["line_count"] > 200:
        actions.append("Consider simplifying - very long")
    
    if not actions:
        actions.append("Minimal cleanup needed")
    
    return actions

def main():
    """Main analysis function."""
    
    commands_dir = "/Users/smenssink/conductor/repo/claude-code-modular-prompts/casablanca/.claude/commands"
    results = []
    
    # Find all markdown files
    for root, dirs, files in os.walk(commands_dir):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                
                # Analyze the command
                analysis = analyze_command_file(file_path)
                
                # Determine priority and cleanup actions
                priority = categorize_command_priority(file_path, analysis)
                cleanup_actions = determine_cleanup_actions(analysis)
                
                # Create result entry
                result = {
                    **analysis,
                    "priority": priority,
                    "cleanup_actions": cleanup_actions,
                    "relative_path": file_path.replace(commands_dir, "").lstrip("/")
                }
                
                results.append(result)
    
    # Sort by priority and then by file path
    priority_order = {"CRITICAL": 0, "HIGH": 1, "MEDIUM": 2, "LOW": 3}
    results.sort(key=lambda x: (priority_order.get(x["priority"], 4), x["relative_path"]))
    
    # Generate summary statistics
    total_commands = len(results)
    deprecated_count = sum(1 for r in results if r["is_deprecated"])
    active_count = total_commands - deprecated_count
    
    xml_count = sum(1 for r in results if r["has_xml_structures"])
    security_theater_count = sum(1 for r in results if r["has_security_theater"])
    python_code_count = sum(1 for r in results if r["has_python_code"])
    
    priority_counts = {}
    for result in results:
        priority = result["priority"]
        priority_counts[priority] = priority_counts.get(priority, 0) + 1
    
    # Create comprehensive report
    report = {
        "summary": {
            "total_commands": total_commands,
            "active_commands": active_count,
            "deprecated_commands": deprecated_count,
            "commands_with_xml": xml_count,
            "commands_with_security_theater": security_theater_count,
            "commands_with_python_code": python_code_count,
            "priority_breakdown": priority_counts
        },
        "commands": results
    }
    
    # Save detailed JSON report
    with open("command_analysis_report.json", "w") as f:
        json.dump(report, f, indent=2)
    
    # Print summary to console
    print("=" * 80)
    print("CLAUDE CODE COMMANDS - COMPREHENSIVE CLEANUP INVENTORY")
    print("=" * 80)
    print(f"Total Commands Analyzed: {total_commands}")
    print(f"Active Commands: {active_count}")
    print(f"Deprecated Commands: {deprecated_count}")
    print()
    print("CLEANUP REQUIREMENTS:")
    print(f"- Commands with XML structures: {xml_count} ({xml_count/total_commands*100:.1f}%)")
    print(f"- Commands with security theater: {security_theater_count} ({security_theater_count/total_commands*100:.1f}%)")
    print(f"- Commands with Python code blocks: {python_code_count} ({python_code_count/total_commands*100:.1f}%)")
    print()
    print("PRIORITY BREAKDOWN:")
    for priority in ["CRITICAL", "HIGH", "MEDIUM", "LOW"]:
        count = priority_counts.get(priority, 0)
        print(f"- {priority}: {count} commands")
    
    print(f"\nDetailed report saved to: command_analysis_report.json")

if __name__ == "__main__":
    main()