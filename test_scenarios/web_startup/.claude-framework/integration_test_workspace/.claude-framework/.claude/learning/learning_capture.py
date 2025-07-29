#!/usr/bin/env python3
"""
Learning Capture Script for Claude Code Modular System Transformation

Captures insights and patterns after every 5-10 commits to facilitate
continuous improvement and anti-pattern discovery.
"""

import json
import subprocess
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional


class LearningCapture:
    """Captures and documents learning insights from git commits."""
    
    def __init__(self, learning_dir: Path = Path(".claude/learning")):
        self.learning_dir = learning_dir
        self.learning_dir.mkdir(parents=True, exist_ok=True)
        self.insights_file = self.learning_dir / "insights.json"
        self.antipatterns_file = self.learning_dir / "discovered-antipatterns.md"
        
    def get_commits(self, commit_range: str) -> List[Dict[str, str]]:
        """Retrieve commit information for the specified range."""
        cmd = ["git", "log", "--oneline", "--format=%H|%s|%an|%ad", commit_range]
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        commits = []
        for line in result.stdout.strip().split('\n'):
            if line:
                hash_id, subject, author, date = line.split('|')
                commits.append({
                    "hash": hash_id,
                    "subject": subject,
                    "author": author,
                    "date": date
                })
        return commits
    
    def capture_learning(self, commit_range: str = "HEAD~5..HEAD") -> Dict:
        """Capture learning insights from recent commits."""
        commits = self.get_commits(commit_range)
        
        learning_entry = {
            "timestamp": datetime.now().isoformat(),
            "commits_analyzed": commits,
            "patterns": {
                "successful": [],
                "failed": [],
                "unexpected": []
            },
            "antipatterns_discovered": [],
            "process_improvements": [],
            "technical_insights": []
        }
        
        # Questions to systematically answer
        questions = {
            "successful": "What worked better than expected?",
            "failed": "What failed and why?",
            "patterns": "What patterns are emerging?",
            "stop": "What should we stop doing?",
            "start": "What should we start doing?",
            "antipatterns": "What antipatterns did we discover?"
        }
        
        return learning_entry, questions
    
    def save_learning(self, learning_entry: Dict) -> None:
        """Save learning entry to JSON file."""
        existing_entries = []
        if self.insights_file.exists():
            with open(self.insights_file, 'r') as f:
                existing_entries = json.load(f)
        
        existing_entries.append(learning_entry)
        
        with open(self.insights_file, 'w') as f:
            json.dump(existing_entries, f, indent=2)
    
    def update_antipatterns(self, new_antipatterns: List[str]) -> None:
        """Update the discovered antipatterns documentation."""
        if not new_antipatterns:
            return
            
        with open(self.antipatterns_file, 'a') as f:
            f.write(f"\n\n## Discovered on {datetime.now().strftime('%Y-%m-%d')}\n\n")
            for antipattern in new_antipatterns:
                f.write(f"- {antipattern}\n")
    
    def generate_learning_report(self, phase: int) -> str:
        """Generate a markdown report of learnings for a phase."""
        report = f"""# Phase {phase} Learning Report

**Generated**: {datetime.now().strftime('%Y-%m-%d %H:%M')}

## Summary

This report captures insights and learnings from Phase {phase} of the Claude Code 
Modular System transformation.

## Key Learnings

### What Worked Well
- [To be filled based on insights]

### Challenges Encountered
- [To be filled based on insights]

### Antipatterns Discovered
- [To be filled based on insights]

### Process Improvements
- [To be filled based on insights]

## Metrics
- Commits analyzed: [count]
- Patterns identified: [count]
- Antipatterns discovered: [count]

## Recommendations for Next Phase
- [To be filled based on analysis]

---
*This report should be reviewed and updated with specific insights before committing.*
"""
        return report
    
    def holistic_review(self, phase_number: int) -> Dict:
        """Perform comprehensive review after a phase."""
        # Get all commits for the phase
        # This is a placeholder - in practice, you'd determine the commit range for the phase
        
        review = {
            "phase": phase_number,
            "timestamp": datetime.now().isoformat(),
            "duration": "calculate_duration()",
            "metrics": {
                "files_changed": 0,  # To be calculated
                "complexity_reduction": 0,  # To be calculated
                "test_coverage": 0,  # To be calculated
                "antipatterns_fixed": 0  # To be calculated
            },
            "learnings": {
                "technical": [],
                "process": [],
                "architectural": []
            },
            "next_phase_adjustments": []
        }
        
        # Key questions for holistic review
        holistic_questions = [
            "Did we achieve the phase goal?",
            "What unexpected challenges arose?",
            "How did our approach evolve?",
            "What would we do differently?",
            "What patterns will help next phase?",
            "What new antipatterns emerged?"
        ]
        
        return review, holistic_questions


def main():
    """Main function for interactive learning capture."""
    capture = LearningCapture()
    
    print("Learning Capture Tool for Claude Code Transformation")
    print("=" * 50)
    
    # Example usage
    learning_entry, questions = capture.capture_learning()
    
    print("\nRecent commits analyzed:")
    for commit in learning_entry["commits_analyzed"]:
        print(f"  - {commit['hash'][:7]}: {commit['subject']}")
    
    print("\nPlease reflect on these questions:")
    for key, question in questions.items():
        print(f"  - {question}")
    
    print("\nUse this tool after every 5-10 commits to capture insights.")
    print("Run with different commit ranges as needed: capture_learning('HEAD~10..HEAD')")


if __name__ == "__main__":
    main()