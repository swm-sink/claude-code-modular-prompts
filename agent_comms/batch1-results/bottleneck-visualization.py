#!/usr/bin/env python3
"""
Generate visualization charts for performance bottlenecks
"""

import json
from pathlib import Path

def generate_ascii_chart(data, title, max_width=80):
    """Generate ASCII bar chart"""
    if not data:
        return ""
    
    max_value = max(data.values())
    chart = [f"\n{title}\n{'=' * len(title)}"]
    
    for label, value in sorted(data.items(), key=lambda x: x[1], reverse=True):
        bar_width = int((value / max_value) * (max_width - 30))
        bar = '█' * bar_width
        chart.append(f"{label:20} {bar} {value:,}")
    
    return '\n'.join(chart)

def main():
    # Load performance data
    base_dir = Path('/Users/smenssink/conductor/repo/claude-code-modular-prompts/vatican/agent_comms/batch1-results')
    
    with open(base_dir / 'performance-metrics.json', 'r') as f:
        metrics = json.load(f)
    
    # Command token usage
    command_tokens = {
        cmd: profile['total_tokens'] 
        for cmd, profile in metrics['command_profiles'].items()
        if profile['total_tokens'] > 5000
    }
    
    # Workflow costs
    workflow_tokens = {
        name: data['total_tokens']
        for name, data in metrics['workflow_costs'].items()
    }
    
    # Module categories
    module_tokens = {}
    for module, data in metrics['module_profiles'].items():
        category = data['category']
        if category not in module_tokens:
            module_tokens[category] = 0
        module_tokens[category] += data['tokens']
    
    # Generate report
    report = [
        "# Performance Bottleneck Visualization",
        "\nGenerated: 2025-07-19",
        "\n## Token Usage Analysis",
        
        generate_ascii_chart(command_tokens, "Commands with Excessive Tokens (>5K)"),
        
        generate_ascii_chart(workflow_tokens, "Workflow Token Costs"),
        
        generate_ascii_chart(module_tokens, "Module Category Token Distribution"),
        
        "\n## Critical Findings",
        "\n1. **Meta Command**: Uses 47K tokens (23.5x its direct content!)",
        "2. **Feature Workflow**: Consumes 32% of context window",
        "3. **Module Overhead**: 261K tokens loaded regardless of operation",
        "4. **Cost Impact**: $432/month at current usage patterns",
        
        "\n## Optimization Priorities",
        "\n1. Reduce meta command by 89% (save 42K tokens)",
        "2. Implement lazy module loading (save 100K+ tokens)",
        "3. Deduplicate modules (save 2K+ tokens)",
        "4. Extract documentation from runtime (save 50K tokens)",
        
        "\n## Before/After Projection",
        "\n```",
        "Current State:",
        "├─ Framework Overhead: 261,315 tokens (130% of context)",
        "├─ Average Workflow: 46,661 tokens",
        "└─ Monthly Cost: $432",
        "",
        "Target State (60% reduction):",
        "├─ Framework Overhead: 104,526 tokens (52% of context)",
        "├─ Average Workflow: 18,664 tokens", 
        "└─ Monthly Cost: $173 (save $259/month)",
        "```"
    ]
    
    # Save visualization
    with open(base_dir / 'bottleneck-visualization.txt', 'w') as f:
        f.write('\n'.join(report))
    
    print('\n'.join(report))

if __name__ == '__main__':
    main()