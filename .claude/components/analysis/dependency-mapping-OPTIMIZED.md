# Dependency Analysis and Mapping

**Purpose**: Standardized dependency analysis across projects mapping internal modules, external libraries, and architectural relationships with issue detection.

**Usage**: 
- Discovers dependency files (package.json, requirements.txt, Cargo.toml, pom.xml, go.mod)
- Maps internal module relationships and detects circular dependencies
- Analyzes external dependencies (direct/transitive, versions, security)
- Identifies tightly coupled components and architectural smells
- Provides structured analysis with actionable recommendations

**Compatibility**: 
- **Works with**: codebase-discovery, pattern-extraction, framework-validation
- **Requires**: dependency_files, import_analysis, vulnerability_database
- **Conflicts**: None (universal analysis tool)

**Implementation**:
```yaml
dependency_mapping:
  internal: [modules, imports, circular_detection]
  external: [direct, transitive, versions, security]
  insights: [coupling, refactoring, architecture]
  output: structured_analysis_report
```

**Category**: analysis | **Complexity**: simple | **Time**: 30 minutes