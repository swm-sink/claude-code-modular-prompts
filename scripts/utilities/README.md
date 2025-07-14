# Utility Scripts

General purpose utilities for framework users to analyze, visualize, and maintain their framework setup.

## Scripts

### `check-duplications.py`
**Purpose**: Scans for duplicate content across modules and suggests consolidation

**Features**:
- Identifies redundant implementations
- Suggests consolidation opportunities
- Maintains framework DRY principles
- Generates consolidation reports

**Usage**:
```bash
python scripts/utilities/check-duplications.py
```

**Output**: Reports duplicate content and provides consolidation suggestions.

### `visualize.py`
**Purpose**: Creates visual representations of framework structure and dependencies

**Features**:
- Module dependency visualization
- Framework structure diagrams
- Command routing path visualization
- Integration maps

**Usage**:
```bash
python scripts/utilities/visualize.py
```

**Output**: Generates visual diagrams and dependency graphs.

## Use Cases

### Maintenance
- **Duplicate Detection**: Find and eliminate redundant code
- **Structure Analysis**: Understand framework organization
- **Dependency Mapping**: Visualize module relationships

### Development
- **Architecture Review**: Visual framework architecture
- **Refactoring Support**: Identify consolidation opportunities
- **Documentation**: Generate visual documentation

## Requirements

- Python 3.8+
- Framework read access
- Optional: Graphing libraries for visualization

## Output

- Visualization outputs are saved to configured output directories
- Reports are generated in standard formats
- Git ignores temporary output files

## Notes

- Run from project root directory
- Safe to run multiple times
- No framework modifications - read-only operations