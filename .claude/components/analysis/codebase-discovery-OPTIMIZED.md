# Codebase Discovery

**Purpose**: Systematic codebase analysis including project structure, technology stack detection, code organization mapping, and dependency analysis.

**Usage**: 
- Scan root directory for configuration files (package.json, pom.xml, Cargo.toml)
- Identify source, test, and build directories with standard naming patterns
- Detect technology stack, frameworks, and architectural patterns automatically
- Map module hierarchies, entry points, and component relationships
- Analyze internal and external dependencies for comprehensive understanding

**Compatibility**: 
- **Works with**: dependency-mapping, find-relevant-code, search-files, file-reader
- **Requires**: Access to project root directory and file system
- **Conflicts**: None (foundational analysis component)

**Implementation**:
```python
# Comprehensive codebase discovery
def discover_codebase(project_root):
    discovery_result = CodebaseDiscovery()
    
    # 1. Project Structure Analysis
    config_files = scan_configuration_files(project_root)
    directories = identify_standard_directories(project_root)
    
    # 2. Technology Stack Detection
    tech_stack = detect_technology_stack(config_files)
    frameworks = identify_frameworks_and_libraries(config_files)
    
    # 3. Code Organization Mapping
    entry_points = find_entry_points(directories['src'])
    module_hierarchy = map_module_relationships(directories['src'])
    
    # 4. Dependency Analysis
    internal_deps = analyze_internal_dependencies(module_hierarchy)
    external_deps = extract_external_dependencies(config_files)
    
    return CodebaseMap(
        structure=directories,
        technology=tech_stack,
        frameworks=frameworks,
        organization=module_hierarchy,
        dependencies={'internal': internal_deps, 'external': external_deps}
    )

# Technology stack detection helper
def detect_technology_stack(config_files):
    stack = {}
    if 'package.json' in config_files:
        stack['language'] = 'JavaScript/TypeScript'
        stack['runtime'] = 'Node.js'
    elif 'pom.xml' in config_files:
        stack['language'] = 'Java'
        stack['build_system'] = 'Maven'
    elif 'Cargo.toml' in config_files:
        stack['language'] = 'Rust'
        stack['build_system'] = 'Cargo'
    return stack
```

**Category**: analysis | **Complexity**: moderate | **Time**: 2 hours