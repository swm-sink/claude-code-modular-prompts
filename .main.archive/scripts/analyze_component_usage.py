import re
from collections import defaultdict


def analyze_mermaid_file(file_path):
    """Parses a mermaid file to report on component usage."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        component_usage = defaultdict(list)
        node_names = {}

        # First pass: extract all node IDs and their labels (the real path)
        node_pattern = re.compile(r'(\S+)\["([^"]+)"\];')
        for node_id, node_label in node_pattern.findall(content):
            node_names[node_id] = node_label

        # Second pass: find "includes" relationships using the IDs
        edge_pattern = re.compile(r'(\S+)\s*-->\|includes\|\s*(\S+);')
        for source_id, target_id in edge_pattern.findall(content):
            if source_id in node_names and target_id in node_names:
                source_path = node_names[source_id]
                target_path = node_names[target_id]
                
                if target_path.startswith("components/"):
                    component_usage[target_path].append(source_path)
                
        return component_usage
        
    except FileNotFoundError:
        print(f"Error: Could not find file at {file_path}")
        return None


def main():
    """Main function to run the analysis."""
    usage = analyze_mermaid_file("dependency_graph.md")
    if usage:
        print("--- Component Usage Report ---")
        for component, commands in usage.items():
            print(f"\nComponent: {component}")
            print("  Used by:")
            for command in sorted(commands):
                print(f"    - {command}")
        print("\n--- End of Report ---")


if __name__ == "__main__":
    main() 