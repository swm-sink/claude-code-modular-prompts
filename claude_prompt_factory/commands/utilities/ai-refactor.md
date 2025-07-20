# /ai refactor - AI-Powered Code Refactoring

**Command**: `/ai refactor [target] [options]`

## Purpose
Apply systematic AI-powered refactoring to improve code structure, performance, and readability while maintaining functionality.

## Core Capabilities
- **Structure Optimization**: Improve class/function organization
- **Performance Enhancement**: Optimize algorithms and data structures  
- **Readability Improvement**: Enhance naming, comments, documentation
- **Pattern Application**: Apply design patterns appropriately
- **Dependency Management**: Reduce coupling, improve cohesion

## Usage
```bash
/ai refactor file.py --focus=performance,readability
/ai refactor src/ --type=class --preserve-api
/ai refactor component.js --pattern=hooks --test-driven
```

## Options
- `--focus`: performance, readability, structure, patterns
- `--type`: function, class, module, package
- `--preserve-api`: Maintain public interface compatibility
- `--test-driven`: Run tests after each refactoring step
- `--interactive`: Confirm each suggested change
- `--depth`: shallow, medium, deep analysis

## Safety Features
- Automated backup before changes
- Test execution validation
- API compatibility checking
- Rollback on failure
- Change impact analysis

## Output
- Refactoring plan with priority ranking
- Before/after code comparisons
- Performance impact predictions
- Test coverage preservation report
- Documentation updates

## Integration
- Works with existing test suites
- Integrates with version control
- Supports multiple programming languages
- Compatible with CI/CD pipelines

**Quality Focus**: Systematic improvement without functionality loss