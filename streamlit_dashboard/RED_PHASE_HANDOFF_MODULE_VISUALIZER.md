# RED Phase Handoff Documentation: Module Visualizer

## TDD RED Phase Complete - Agent A2 to Agent B2 Handoff

### Executive Summary
RED phase successfully completed with 113 failing tests and 5 passing guidance tests, providing comprehensive architecture definition for Module Visualizer component.

### Test Suite Overview
- **Total Tests**: 118 tests
- **Failed Tests**: 113 (expected - component not implemented)
- **Passed Tests**: 5 (guidance and specification tests)
- **Coverage Areas**: 14 major functional areas
- **File Location**: `/tests/test_module_visualizer.py`

### Component Architecture Defined

#### Core Requirements
1. **ModuleVisualizer Class**
   - Framework path initialization with validation
   - FrameworkParser integration
   - Module state management
   - Layout configuration system

2. **Data Loading System**
   - Load modules from framework directory
   - Parse module dependencies with circular detection
   - Support for 100+ modules with <2s load time
   - Comprehensive metadata extraction

3. **Filtering & Search**
   - Category-based filtering (patterns, system, meta, etc.)
   - Content search (name, description, file content)
   - Type and complexity filtering
   - Regex search support

4. **Tree Navigation**
   - Hierarchical module organization
   - Expandable category nodes
   - Search integration
   - Nested category support

5. **Network Visualization**
   - NetworkX dependency graphs
   - Multiple layout algorithms (spring, circular, kamada_kawai)
   - Interactive zoom/pan controls
   - Color coding by category

6. **Complexity Analysis**
   - Module complexity calculation
   - AST-based analysis
   - Interactive heatmaps
   - Category grouping

7. **Usage Analytics**
   - Frequency charts (bar, pie, donut)
   - Pattern analysis
   - Category distribution
   - Historical trend support

8. **Export Capabilities**
   - PNG/SVG visualization export
   - JSON data export
   - Metadata inclusion
   - Custom sizing options

### Test Categories Breakdown

#### 1. Initialization (6 tests)
- Module existence validation
- Framework path handling
- Default parameter setup
- Required method verification
- Layout configuration

#### 2. Data Loading (8 tests)
- Framework integration
- Large dataset handling (150+ modules)
- Empty directory handling
- Missing directory error handling
- Metadata extraction
- Dependency parsing with circular detection

#### 3. Filtering (9 tests)
- Single/multiple category filtering
- Type and complexity filtering
- Content search (name, description, file)
- Case-insensitive search
- Regex support

#### 4. Tree Navigation (7 tests)
- Basic tree structure
- Nested categories
- Dependency inclusion
- Rendering with search
- Node expansion
- Error handling

#### 5. Network Visualization (7 tests)
- Dependency graph creation
- Multiple layout algorithms
- Color coding
- Interactive features
- Zoom/pan controls
- Performance with large graphs

#### 6. Complexity Analysis (5 tests)
- Basic complexity calculation
- Category grouping
- AST analysis
- File error handling
- Interactive heatmaps

#### 7. Usage Analysis (8 tests)
- Frequency charts (bar, pie, donut)
- Pattern analysis
- Missing data handling
- Historical trends
- Category distribution

#### 8. User Interaction (8 tests)
- Module selection handling
- Details panel rendering
- Filter controls
- UI state management
- Callback execution
- Zoom/pan controls

#### 9. Export Functionality (8 tests)
- PNG export with custom options
- SVG export
- JSON data export
- Metadata inclusion
- All format integration

#### 10. Error Handling (9 tests)
- Graceful degradation
- Missing framework data
- Invalid paths
- Corrupted files
- Memory constraints
- Recovery mechanisms

#### 11. Performance (8 tests)
- Load time benchmarks (<2s for 100+ modules)
- Render time benchmarks (<1.5s for 50 modules)
- Memory usage constraints (<15MB for 200 modules)
- Interactive response time (<50ms)
- Concurrent access handling

#### 12. Accessibility (6 tests)
- ARIA labels and descriptions
- Keyboard navigation
- Screen reader compatibility
- Color contrast validation
- High contrast mode
- Text size scalability

#### 13. Mobile Responsiveness (5 tests)
- Touch interaction support
- Responsive layout validation
- Mobile performance optimization
- Gesture handling
- Mobile filter controls

#### 14. Integration (7 tests)
- FrameworkParser integration
- Data model compatibility
- Streamlit component integration
- Command Explorer compatibility
- Data flow validation
- State management
- Configuration compatibility

#### 15. File Constraints (4 tests)
- File size constraint (<500 LOC)
- Appropriate imports
- Separation of concerns
- Cyclomatic complexity (≤10 per method)

#### 16. Implementation Guidance (5 tests - PASSING)
- Performance benchmarks
- Coverage analysis plan
- Integration specifications
- Module categories
- Visualization types

### Performance Benchmarks

#### Required Performance Targets
- **Load Time**: <2s for 100+ modules
- **Render Time**: <1.5s for 50 modules
- **Network Visualization**: <2s for 80 nodes
- **Interactive Response**: <50ms
- **Memory Usage**: <15MB for 200 modules
- **Dependency Parsing**: <1s for 100 modules

### Integration Requirements

#### Framework Integration
- **FrameworkParser**: `data.framework_parser.FrameworkParser`
- **Module Model**: `data.models.Module`
- **Framework Model**: `data.models.Framework`
- **Streamlit UI**: Standard Streamlit components
- **Plotly Visualization**: `plotly.graph_objects`
- **NetworkX Graphs**: `networkx.DiGraph`

#### Module Categories
- **patterns**: Core patterns and algorithms
- **development**: Development support modules
- **meta**: Meta-framework modules
- **system**: System and infrastructure modules
- **domain**: Domain-specific modules
- **templates**: Template and scaffolding modules

### File Structure Required

```
streamlit_dashboard/
├── components/
│   └── module_visualizer.py  # <500 LOC, Agent B2 creates this
├── tests/
│   └── test_module_visualizer.py  # 118 tests (complete)
└── RED_PHASE_HANDOFF_MODULE_VISUALIZER.md  # This file
```

### Key Implementation Notes for Agent B2

#### 1. Core Architecture
- Class: `ModuleVisualizer`
- Constructor: `__init__(self, framework_path=None)`
- Main render method: `render(self)`
- State management: `selected_module`, `filter_state`, `layout_config`

#### 2. Required Imports
```python
import streamlit as st
import plotly.graph_objects as go
import networkx as nx
from pathlib import Path
from typing import Dict, List, Optional, Any
from data.framework_parser import FrameworkParser
from data.models import Module, Framework
```

#### 3. Critical Methods (20 methods max)
- `load_modules_from_framework()`
- `parse_module_dependencies()`
- `filter_modules_by_category()`
- `search_modules_by_content()`
- `build_module_tree()`
- `create_dependency_graph()`
- `create_network_visualization()`
- `create_complexity_heatmap()`
- `create_usage_frequency_chart()`
- `handle_module_selection()`
- `render_module_details_panel()`
- `render_filter_controls()`
- `export_visualization_png()`
- `export_visualization_svg()`
- `export_module_data_json()`
- `render()`

#### 4. UI Layout Structure
```python
def render(self):
    st.title("Module Visualizer")
    
    # Load and filter modules
    modules = self.load_modules_from_framework()
    
    # Filter controls
    filters = self.render_filter_controls()
    
    # Main visualization area
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Network visualization or tree view
        # Complexity heatmap
        # Usage frequency charts
        
    with col2:
        # Module details panel
        # Filter controls
        # Export options
```

#### 5. Error Handling Pattern
```python
try:
    # Core functionality
    pass
except FileNotFoundError:
    st.error("Framework directory not found")
except Exception as e:
    st.error(f"Error: {e}")
    # Graceful degradation
```

### Success Criteria for Agent B2 GREEN Phase

1. **All 113 failing tests must pass**
2. **File size <500 LOC** (split helpers if needed)
3. **Performance benchmarks met**
4. **Accessibility compliance**
5. **Mobile responsiveness**
6. **Integration with existing framework**
7. **Error handling and graceful degradation**

### Test Execution Command
```bash
cd /Users/smenssink/Documents/Github/claude-code-modular-prompts/streamlit_dashboard
python -m pytest tests/test_module_visualizer.py -v
```

### Handoff Status
- **RED Phase**: ✅ COMPLETE (113 failing tests created)
- **GREEN Phase**: 🔄 READY FOR AGENT B2
- **REFACTOR Phase**: ⏳ PENDING

### Next Steps for Agent B2
1. Create `components/module_visualizer.py`
2. Implement ModuleVisualizer class
3. Run tests iteratively until all pass
4. Optimize for performance benchmarks
5. Ensure accessibility compliance
6. Validate integration with existing framework

### Quality Gates
- **TDD Compliance**: Strict RED-GREEN-REFACTOR cycle
- **Test Coverage**: 100% of implemented functionality
- **Performance**: All benchmarks must be met
- **Accessibility**: ARIA labels, keyboard navigation
- **Error Handling**: Graceful degradation for all scenarios

---

**Agent A2 RED Phase Complete**  
**Ready for Agent B2 GREEN Phase Implementation**  
**118 tests defined | 113 failing | 5 guidance tests passing**