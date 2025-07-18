# Development Guide - Claude Code Modular Prompts Dashboard

## Overview

This guide provides comprehensive information for developers who want to contribute to, extend, or maintain the Claude Code Modular Prompts Dashboard. It covers architecture, development practices, testing procedures, and deployment strategies.

## Table of Contents

1. [Architecture Overview](#architecture-overview)
2. [Development Environment Setup](#development-environment-setup)
3. [Code Structure](#code-structure)
4. [Component Development](#component-development)
5. [Testing Strategy](#testing-strategy)
6. [Quality Assurance](#quality-assurance)
7. [Performance Optimization](#performance-optimization)
8. [Deployment](#deployment)
9. [Contributing Guidelines](#contributing-guidelines)
10. [Troubleshooting](#troubleshooting)

## Architecture Overview

### System Architecture

The dashboard follows a modular architecture with clear separation of concerns:

```
┌─────────────────────────────────────────────────────────────┐
│                     Streamlit Frontend                     │
├─────────────────────────────────────────────────────────────┤
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐        │
│  │  Framework  │  │  Template   │  │ URL Sharing │        │
│  │  Explorer   │  │  Manager    │  │  Manager    │        │
│  └─────────────┘  └─────────────┘  └─────────────┘        │
├─────────────────────────────────────────────────────────────┤
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐        │
│  │ Performance │  │   Command   │  │   Module    │        │
│  │  Monitor    │  │  Explorer   │  │ Visualizer  │        │
│  └─────────────┘  └─────────────┘  └─────────────┘        │
├─────────────────────────────────────────────────────────────┤
│                  Core Components Layer                     │
├─────────────────────────────────────────────────────────────┤
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐        │
│  │ Data Access │  │ Validation  │  │   Caching   │        │
│  │    Layer    │  │   Engine    │  │   System    │        │
│  └─────────────┘  └─────────────┘  └─────────────┘        │
└─────────────────────────────────────────────────────────────┘
```

### Key Design Principles

1. **Modularity**: Each component is self-contained and reusable
2. **Separation of Concerns**: Clear boundaries between UI, logic, and data
3. **Testability**: All components are designed for easy testing
4. **Performance**: Efficient data handling and caching strategies
5. **Scalability**: Architecture supports growth and feature additions

### Technology Stack

- **Frontend**: Streamlit (Python web framework)
- **Visualization**: Plotly, Bokeh, NetworkX
- **Data Processing**: Pandas, NumPy
- **File Handling**: Python pathlib, JSON
- **Testing**: pytest, pytest-cov, pytest-mock
- **Performance**: psutil for system monitoring
- **Security**: secrets module for token generation

## Development Environment Setup

### Prerequisites

1. **Python 3.8+**
2. **Git**
3. **Virtual Environment Manager** (venv, conda, or pipenv)
4. **Code Editor** (VS Code, PyCharm, or similar)

### Installation Steps

1. **Clone the Repository**
   ```bash
   git clone https://github.com/swm-sink/claude-code-modular-prompts.git
   cd claude-code-modular-prompts/streamlit_dashboard
   ```

2. **Create Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Install Development Dependencies**
   ```bash
   pip install -r requirements-dev.txt
   ```

5. **Set up Pre-commit Hooks**
   ```bash
   pre-commit install
   ```

### Development Configuration

Create a `.env` file in the project root:

```env
# Development settings
STREAMLIT_SERVER_PORT=8501
STREAMLIT_SERVER_ADDRESS=localhost
STREAMLIT_BROWSER_GATHER_USAGE_STATS=false
STREAMLIT_LOGGER_LEVEL=debug

# Framework settings
CLAUDE_FRAMEWORK_PATH=../.claude
TEMPLATES_PATH=./templates
SHARING_STORAGE_PATH=./sharing
LOGS_PATH=./logs

# Performance monitoring
ENABLE_PERFORMANCE_MONITORING=true
METRICS_RETENTION_DAYS=30
```

## Code Structure

### Directory Layout

```
streamlit_dashboard/
├── app.py                      # Main application entry point
├── requirements.txt            # Production dependencies
├── requirements-dev.txt        # Development dependencies
├── .env                       # Environment configuration
├── .gitignore                 # Git ignore rules
├── components/                # Core components
│   ├── __init__.py
│   ├── framework_overview.py  # Framework explorer
│   ├── template_manager.py    # Template management
│   ├── url_sharing.py         # URL sharing functionality
│   ├── performance_monitor.py # Performance monitoring
│   ├── command_explorer.py    # Command exploration
│   └── module_visualizer.py   # Module visualization
├── tests/                     # Test suite
│   ├── __init__.py
│   ├── test_framework_overview.py
│   ├── test_template_manager.py
│   ├── test_url_sharing.py
│   ├── test_performance_monitor.py
│   ├── test_command_explorer.py
│   └── test_module_visualizer.py
├── docs/                      # Documentation
│   ├── USER_GUIDE.md
│   ├── API_DOCUMENTATION.md
│   └── DEVELOPMENT_GUIDE.md
├── utils/                     # Utility functions
│   ├── __init__.py
│   ├── file_operations.py
│   ├── validation.py
│   └── caching.py
├── data/                      # Data storage
│   ├── templates/
│   ├── sharing/
│   └── cache/
└── assets/                    # Static assets
    ├── css/
    ├── js/
    └── images/
```

### Component Structure

Each component follows a standardized structure:

```python
"""
Component Name - Brief Description
Detailed component description and purpose
"""

import streamlit as st
from typing import Dict, List, Any, Optional
from dataclasses import dataclass
from pathlib import Path

@dataclass
class ComponentData:
    """Data structure for component state"""
    pass

class ComponentName:
    """Main component class"""
    
    def __init__(self, config: Dict[str, Any]):
        """Initialize component with configuration"""
        self.config = config
        self._initialize_component()
    
    def _initialize_component(self):
        """Internal initialization logic"""
        pass
    
    def render(self):
        """Main render method - entry point for UI"""
        pass
    
    def _render_section(self):
        """Private render methods for specific sections"""
        pass
    
    def validate_input(self, data: Any) -> bool:
        """Validate input data"""
        pass
    
    def get_component_state(self) -> Dict[str, Any]:
        """Get current component state"""
        pass
```

## Component Development

### Creating New Components

1. **Create Component File**
   ```bash
   touch components/new_component.py
   ```

2. **Implement Component Class**
   ```python
   import streamlit as st
   from typing import Dict, Any
   
   class NewComponent:
       def __init__(self, config: Dict[str, Any]):
           self.config = config
       
       def render(self):
           st.subheader("New Component")
           # Component implementation
   ```

3. **Add to Main Application**
   ```python
   # In app.py
   from components.new_component import NewComponent
   
   if selected_page == "New Component":
       component = NewComponent(config)
       component.render()
   ```

4. **Create Tests**
   ```python
   # In tests/test_new_component.py
   import pytest
   from components.new_component import NewComponent
   
   def test_component_initialization():
       component = NewComponent({})
       assert component is not None
   ```

### Component Guidelines

1. **Single Responsibility**: Each component should have one clear purpose
2. **Configuration-Driven**: Use configuration objects for flexibility
3. **State Management**: Properly handle Streamlit session state
4. **Error Handling**: Implement comprehensive error handling
5. **Documentation**: Include docstrings and type hints
6. **Testing**: Maintain high test coverage

### UI/UX Best Practices

1. **Consistent Layout**: Use consistent spacing and alignment
2. **Responsive Design**: Ensure components work on different screen sizes
3. **Loading States**: Show loading indicators for long operations
4. **Error Messages**: Provide clear, actionable error messages
5. **Accessibility**: Follow accessibility guidelines

## Testing Strategy

### Test Types

1. **Unit Tests**: Test individual functions and methods
2. **Integration Tests**: Test component interactions
3. **UI Tests**: Test user interface behavior
4. **Performance Tests**: Test system performance
5. **End-to-End Tests**: Test complete workflows

### Test Structure

```python
"""
Test module for ComponentName
Tests all functionality including edge cases and error conditions
"""

import pytest
import tempfile
from pathlib import Path
from unittest.mock import MagicMock, patch
from components.component_name import ComponentName

class TestComponentName:
    """Test class for ComponentName"""
    
    @pytest.fixture
    def component_config(self):
        """Fixture providing test configuration"""
        return {
            "setting1": "value1",
            "setting2": "value2"
        }
    
    @pytest.fixture
    def mock_streamlit(self):
        """Fixture providing mocked Streamlit functions"""
        with patch('streamlit.session_state') as mock_session:
            yield mock_session
    
    def test_component_initialization(self, component_config):
        """Test component can be initialized properly"""
        component = ComponentName(component_config)
        assert component.config == component_config
    
    def test_component_render(self, component_config, mock_streamlit):
        """Test component renders without errors"""
        component = ComponentName(component_config)
        # Should not raise any exceptions
        component.render()
    
    def test_validation_success(self, component_config):
        """Test successful validation"""
        component = ComponentName(component_config)
        assert component.validate_input(valid_input) is True
    
    def test_validation_failure(self, component_config):
        """Test validation failure"""
        component = ComponentName(component_config)
        assert component.validate_input(invalid_input) is False
    
    def test_error_handling(self, component_config):
        """Test error handling"""
        component = ComponentName(component_config)
        with pytest.raises(ExpectedError):
            component.problematic_method()
```

### Running Tests

```bash
# Run all tests
pytest

# Run tests with coverage
pytest --cov=components

# Run tests for specific component
pytest tests/test_component_name.py

# Run tests with verbose output
pytest -v

# Run tests and generate HTML coverage report
pytest --cov=components --cov-report=html
```

### Test Coverage Requirements

- **Minimum Coverage**: 90% line coverage
- **Critical Components**: 95% line coverage
- **All Public Methods**: Must be tested
- **Error Conditions**: Must be tested
- **Edge Cases**: Must be covered

## Quality Assurance

### Code Quality Standards

1. **PEP 8 Compliance**: Follow Python style guide
2. **Type Hints**: Use type hints for all public methods
3. **Docstrings**: Document all classes and public methods
4. **Error Handling**: Comprehensive error handling
5. **Logging**: Appropriate logging levels

### Code Review Process

1. **Pull Request Requirements**:
   - All tests must pass
   - Code coverage must meet requirements
   - Documentation must be updated
   - Performance impact must be assessed

2. **Review Checklist**:
   - [ ] Code follows style guidelines
   - [ ] Tests cover new functionality
   - [ ] Documentation is updated
   - [ ] Performance is acceptable
   - [ ] Security considerations addressed

### Static Analysis Tools

```bash
# Install development tools
pip install black flake8 mypy isort

# Format code
black .

# Check style
flake8 .

# Type checking
mypy components/

# Sort imports
isort .
```

### Pre-commit Configuration

```yaml
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/psf/black
    rev: 22.3.0
    hooks:
      - id: black
  - repo: https://github.com/pycqa/flake8
    rev: 4.0.1
    hooks:
      - id: flake8
  - repo: https://github.com/pycqa/isort
    rev: 5.10.1
    hooks:
      - id: isort
  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: v0.950
    hooks:
      - id: mypy
```

## Performance Optimization

### Performance Monitoring

1. **Built-in Monitoring**: Use the performance monitor component
2. **Profiling**: Profile code to identify bottlenecks
3. **Memory Usage**: Monitor memory consumption
4. **Response Times**: Track API response times

### Optimization Strategies

1. **Caching**: Cache expensive operations
   ```python
   import streamlit as st
   
   @st.cache_data
   def expensive_operation(data):
       # Expensive computation
       return result
   ```

2. **Lazy Loading**: Load data only when needed
   ```python
   class LazyComponent:
       def __init__(self):
           self._data = None
       
       @property
       def data(self):
           if self._data is None:
               self._data = load_expensive_data()
           return self._data
   ```

3. **Pagination**: Paginate large datasets
   ```python
   def paginate_data(data, page_size=50):
       total_pages = (len(data) + page_size - 1) // page_size
       page = st.selectbox("Page", range(1, total_pages + 1))
       start_idx = (page - 1) * page_size
       end_idx = start_idx + page_size
       return data[start_idx:end_idx]
   ```

### Performance Benchmarks

- **Page Load Time**: < 2 seconds
- **Component Render Time**: < 500ms
- **Memory Usage**: < 512MB for typical operations
- **API Response Time**: < 200ms for cached data

## Deployment

### Development Deployment

```bash
# Run development server
streamlit run app.py

# Run with custom configuration
streamlit run app.py --server.port 8502
```

### Production Deployment

#### Railway Deployment

1. **Configure Railway**
   ```json
   {
     "build": {
       "builder": "NIXPACKS"
     },
     "deploy": {
       "healthcheckPath": "/healthz",
       "startCommand": "streamlit run app.py --server.port $PORT --server.address 0.0.0.0"
     }
   }
   ```

2. **Environment Variables**
   ```bash
   PORT=8501
   STREAMLIT_SERVER_HEADLESS=true
   STREAMLIT_BROWSER_GATHER_USAGE_STATS=false
   ```

#### Docker Deployment

```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

#### Health Check Endpoint

```python
# Add to app.py
def health_check():
    """Health check endpoint for deployment"""
    return {"status": "healthy", "timestamp": datetime.now().isoformat()}

if st.query_params.get("health"):
    st.json(health_check())
```

## Contributing Guidelines

### Development Workflow

1. **Fork the Repository**
2. **Create Feature Branch**
   ```bash
   git checkout -b feature/new-component
   ```

3. **Implement Changes**
   - Follow code standards
   - Add comprehensive tests
   - Update documentation

4. **Run Quality Checks**
   ```bash
   pytest --cov=components
   black .
   flake8 .
   mypy .
   ```

5. **Submit Pull Request**
   - Clear description of changes
   - Reference related issues
   - Include testing results

### Commit Message Format

```
type(scope): brief description

Detailed description of changes including:
- What was changed
- Why it was changed
- Any breaking changes

Closes #issue-number
```

Types:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes
- `refactor`: Code refactoring
- `test`: Test additions or changes
- `perf`: Performance improvements

### Documentation Requirements

1. **Code Documentation**:
   - Docstrings for all public methods
   - Type hints for all parameters
   - Usage examples in docstrings

2. **User Documentation**:
   - Update user guide for new features
   - API documentation updates
   - Development guide updates

3. **Change Documentation**:
   - Update CHANGELOG.md
   - Document breaking changes
   - Migration guides if needed

## Troubleshooting

### Common Development Issues

1. **Import Errors**
   ```python
   # Ensure proper Python path
   import sys
   sys.path.append('.')
   ```

2. **Streamlit Session State Issues**
   ```python
   # Initialize session state properly
   if 'key' not in st.session_state:
       st.session_state.key = default_value
   ```

3. **Testing Issues**
   ```python
   # Mock Streamlit functions properly
   with patch('streamlit.session_state') as mock_session:
       mock_session.__getitem__ = MagicMock(return_value=value)
       mock_session.__setitem__ = MagicMock()
   ```

### Debugging Techniques

1. **Enable Debug Logging**
   ```python
   import logging
   logging.basicConfig(level=logging.DEBUG)
   ```

2. **Use Streamlit Debugging**
   ```python
   st.write("Debug:", variable)
   st.json(debug_data)
   ```

3. **Performance Profiling**
   ```python
   import cProfile
   import pstats
   
   profiler = cProfile.Profile()
   profiler.enable()
   # Code to profile
   profiler.disable()
   stats = pstats.Stats(profiler)
   stats.sort_stats('cumulative')
   stats.print_stats(10)
   ```

### Getting Help

1. **Documentation**: Check this guide and API documentation
2. **Tests**: Look at existing tests for examples
3. **Issues**: Search existing GitHub issues
4. **Community**: Ask questions in discussions
5. **Code Review**: Request review from maintainers

---

*Last Updated: 2025-07-18*
*Version: 1.0.0*