# Auto Command Example

## Overview
The `/auto` command is your intelligent assistant that analyzes your request and automatically chooses the best approach. It's perfect when you're unsure which specific command to use or want the framework to make optimal decisions.

## When to Use `/auto`

✅ **Perfect for**:
- Unclear or complex requirements
- When you're not sure which command fits best
- Exploring what the framework can do
- Getting intelligent routing decisions
- Learning the framework capabilities

❌ **Not ideal for**:
- When you specifically want to practice a particular command
- Highly specific technical requirements that need exact control

## Example Scenario
You have a Python project and want to improve the code quality, but you're not sure what specific improvements are needed or which commands would be most appropriate.

## Step-by-Step Walkthrough

### 1. Setup Example Project
First, let's create a simple Python project that needs improvement:

```bash
mkdir auto-command-example
cd auto-command-example
git init

# Create a basic Python file with some issues
cat > calculator.py << 'EOF'
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

result = add(5, 3)
print(result)
EOF
```

### 2. Issue the Auto Command
Now let's ask the framework to analyze and improve our code:

```bash
/auto "analyze my calculator.py file and improve it following Python best practices"
```

### 3. Framework Analysis and Decision
The framework will analyze your request and project, then route to the most appropriate approach:

```
🧠 INTELLIGENT ROUTING ANALYSIS...

📊 PROJECT ANALYSIS:
- Language: Python detected
- File: calculator.py (basic arithmetic operations)
- Code quality: Needs improvement
- Testing: No tests found
- Documentation: Missing
- Error handling: None

🎯 ROUTING DECISION:
Based on your request "analyze and improve following best practices":
- Primary need: Code quality improvement
- Secondary need: Add testing framework
- Tertiary need: Documentation enhancement

🚀 OPTIMAL STRATEGY: Multi-command workflow
1. /query to analyze current code patterns
2. /task to implement individual improvements
3. Session management for tracking progress

EXECUTING PLAN...
```

### 4. Automated Query Analysis
The framework automatically runs analysis first:

```
🔍 CODE ANALYSIS (/query):
- Structure: 4 basic arithmetic functions
- Issues found: No error handling, no documentation, no tests
- Patterns: Simple function definitions, global execution
- Opportunities: Add type hints, docstrings, error handling, main guard

📋 IMPROVEMENT OPPORTUNITIES:
1. Add comprehensive docstrings
2. Implement type hints for better code clarity
3. Add division by zero error handling
4. Create main() function and guard
5. Add comprehensive test suite
6. Improve code organization
```

### 5. Automated Task Execution
Next, the framework automatically implements improvements:

```
🔧 IMPLEMENTING IMPROVEMENTS (/task):

STEP 1: TDD - Creating comprehensive tests...
```

The framework creates `test_calculator.py`:
```python
import pytest
from calculator import Calculator

class TestCalculator:
    """Test suite for Calculator class"""
    
    def setup_method(self):
        """Setup Calculator instance for each test"""
        self.calc = Calculator()
    
    def test_add_positive_numbers(self):
        """Test addition with positive numbers"""
        assert self.calc.add(5, 3) == 8
        assert self.calc.add(0, 0) == 0
    
    def test_add_negative_numbers(self):
        """Test addition with negative numbers"""
        assert self.calc.add(-5, -3) == -8
        assert self.calc.add(-5, 3) == -2
    
    def test_subtract_numbers(self):
        """Test subtraction operations"""
        assert self.calc.subtract(5, 3) == 2
        assert self.calc.subtract(3, 5) == -2
    
    def test_multiply_numbers(self):
        """Test multiplication operations"""
        assert self.calc.multiply(5, 3) == 15
        assert self.calc.multiply(-5, 3) == -15
        assert self.calc.multiply(0, 5) == 0
    
    def test_divide_numbers(self):
        """Test division operations"""
        assert self.calc.divide(6, 3) == 2
        assert self.calc.divide(5, 2) == 2.5
    
    def test_divide_by_zero(self):
        """Test division by zero raises appropriate error"""
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            self.calc.divide(5, 0)
```

### 6. Improved Implementation
The framework then creates the improved `calculator.py`:

```python
"""
Calculator module providing basic arithmetic operations.

This module implements a Calculator class with methods for addition,
subtraction, multiplication, and division with proper error handling.
"""

from typing import Union

Number = Union[int, float]


class Calculator:
    """
    A calculator class that provides basic arithmetic operations.
    
    This calculator handles integer and floating-point arithmetic
    with appropriate error handling for edge cases.
    
    Example:
        >>> calc = Calculator()
        >>> calc.add(5, 3)
        8
        >>> calc.divide(10, 2)
        5.0
    """
    
    def add(self, a: Number, b: Number) -> Number:
        """
        Add two numbers together.
        
        Args:
            a: First number to add
            b: Second number to add
            
        Returns:
            The sum of a and b
            
        Example:
            >>> calc = Calculator()
            >>> calc.add(5, 3)
            8
        """
        return a + b
    
    def subtract(self, a: Number, b: Number) -> Number:
        """
        Subtract second number from first number.
        
        Args:
            a: Number to subtract from
            b: Number to subtract
            
        Returns:
            The difference (a - b)
            
        Example:
            >>> calc = Calculator()
            >>> calc.subtract(5, 3)
            2
        """
        return a - b
    
    def multiply(self, a: Number, b: Number) -> Number:
        """
        Multiply two numbers together.
        
        Args:
            a: First number to multiply
            b: Second number to multiply
            
        Returns:
            The product of a and b
            
        Example:
            >>> calc = Calculator()
            >>> calc.multiply(5, 3)
            15
        """
        return a * b
    
    def divide(self, a: Number, b: Number) -> float:
        """
        Divide first number by second number.
        
        Args:
            a: Number to be divided (dividend)
            b: Number to divide by (divisor)
            
        Returns:
            The quotient (a / b) as a float
            
        Raises:
            ValueError: If attempting to divide by zero
            
        Example:
            >>> calc = Calculator()
            >>> calc.divide(6, 3)
            2.0
        """
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b


def main() -> None:
    """
    Main function demonstrating calculator usage.
    
    Creates a calculator instance and performs sample calculations.
    """
    calc = Calculator()
    
    # Demonstrate basic operations
    print("Calculator Demo:")
    print(f"5 + 3 = {calc.add(5, 3)}")
    print(f"5 - 3 = {calc.subtract(5, 3)}")
    print(f"5 * 3 = {calc.multiply(5, 3)}")
    print(f"5 / 3 = {calc.divide(5, 3):.2f}")
    
    # Demonstrate error handling
    try:
        calc.divide(5, 0)
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```

### 7. Validation and Results
Finally, the framework validates the improvements:

```
✅ IMPROVEMENTS COMPLETED:

📈 BEFORE vs AFTER:
- Lines of code: 12 → 95 (with documentation and error handling)
- Functions: 4 simple functions → 1 class with 4 methods
- Documentation: 0% → 100% (all functions documented)
- Type hints: None → Complete type annotations
- Error handling: None → Division by zero protection
- Tests: 0 → 6 comprehensive test cases
- Code organization: Script → Proper module structure

🧪 TEST RESULTS:
pytest test_calculator.py -v
✅ test_add_positive_numbers PASSED
✅ test_add_negative_numbers PASSED  
✅ test_subtract_numbers PASSED
✅ test_multiply_numbers PASSED
✅ test_divide_numbers PASSED
✅ test_divide_by_zero PASSED

📊 QUALITY METRICS:
- Test coverage: 100%
- Type coverage: 100%
- Documentation: Complete
- Error handling: Implemented
- Code style: PEP 8 compliant

🎯 NEXT SUGGESTIONS:
- Consider adding more advanced operations (power, sqrt, etc.)
- Add input validation for string inputs
- Implement operation history tracking
- Add configuration file for number precision
```

## Key Benefits of `/auto`

### 🧠 Intelligent Decision Making
- **Context Aware**: Analyzes your project structure and needs
- **Best Practice Routing**: Chooses optimal command combinations
- **Adaptive Approach**: Adjusts strategy based on project complexity
- **Learning from Usage**: Gets better at routing over time

### 🚀 Efficiency Gains
- **No Command Memorization**: Don't need to know which specific command to use
- **Optimal Workflows**: Automatically chains commands for best results
- **Reduced Cognitive Load**: Focus on what you want, not how to ask for it
- **Faster Onboarding**: Great for framework beginners

### 🔧 Comprehensive Solutions
- **Multi-Step Planning**: Handles complex requirements automatically
- **Quality Enforcement**: Always includes testing and best practices
- **Error Prevention**: Identifies and prevents common issues
- **Complete Workflows**: Delivers production-ready solutions

## When Auto Routes to Other Commands

The `/auto` command intelligently chooses from these options:

### Routes to `/task` when:
- Single, focused improvement needed
- Clear, specific technical requirement
- Adding individual functions or features
- Simple bug fixes or enhancements

### Routes to `/query` when:
- Analysis or research needed first
- Understanding existing code required
- Exploring system architecture
- Investigating bugs or issues

### Routes to `/feature` when:
- Complete feature development required
- Multiple components need coordination
- Comprehensive planning needed
- System-wide integration required

### Uses Multi-Command Workflows when:
- Complex requirements need multiple approaches
- Analysis + Implementation + Validation needed
- Large-scale improvements or refactoring
- Learning or exploration combined with development

## Advanced Auto Usage

### Compound Requests
```bash
# The framework handles complex, multi-part requests
/auto "analyze my authentication system, find security issues, fix them, and add comprehensive tests"

# Automatically routes through:
# 1. /query for security analysis
# 2. Multiple /task commands for fixes
# 3. Test generation and validation
# 4. Security verification
```

### Context-Aware Suggestions
```bash
# Considers your entire project context
/auto "improve this file for production deployment"

# Framework considers:
# - Current deployment setup
# - Project dependencies
# - Performance requirements
# - Security standards
# - Team coding standards
```

### Learning Mode
```bash
# Ask for explanations of decisions
/auto "optimize this code and explain your reasoning"

# Framework provides:
# - Analysis of optimization opportunities
# - Explanation of chosen approaches
# - Alternative strategies considered
# - Learning guidance for similar situations
```

## Tips for Effective Auto Usage

### 1. Be Descriptive but Not Prescriptive
✅ **Good**: "improve error handling in my user authentication"  
❌ **Less effective**: "add try-catch to login function"

### 2. Include Context When Relevant
✅ **Good**: "optimize this API for high-traffic production use"  
❌ **Less effective**: "make this code faster"

### 3. Express Intent, Not Implementation
✅ **Good**: "make this code more maintainable for my team"  
❌ **Less effective**: "add comments and split functions"

### 4. Ask for Explanations When Learning
✅ **Good**: "refactor this code and explain the improvements"  
❌ **Less effective**: "refactor this code"

## Common Auto Patterns

### Code Quality Improvement
```bash
/auto "improve code quality in my project following industry best practices"
```

### Bug Investigation
```bash
/auto "my tests are failing, help me understand and fix the issues"
```

### Feature Development
```bash
/auto "add user authentication to my web application with proper security"
```

### Performance Optimization
```bash
/auto "my application is slow, analyze and optimize performance"
```

### Documentation and Testing
```bash
/auto "add comprehensive documentation and tests to my project"
```

The `/auto` command is your intelligent partner in development. It learns your preferences, understands your project context, and consistently delivers high-quality solutions by automatically choosing the best approach for each situation.

**Next Step**: Try [query-command.md](query-command.md) to learn focused code analysis and research capabilities.