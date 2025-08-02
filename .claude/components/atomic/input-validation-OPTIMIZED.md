# Input Validation Component

**Purpose**: Validate user input to ensure data quality and security before processing

**Usage**: 
Check all incoming data for required parameters and correct data types
Verify input ranges, constraints, and format requirements (email, phone, etc.)
Return clear, actionable error messages when validation fails
Prevent invalid data from reaching downstream components or databases
Integrate at entry points of workflows to catch issues early

**Compatibility**: 
- **Works with**: parameter-parser, error-handler, response-validator, content-sanitizer
- **Requires**: validation_rules (object), input_data (any)
- **Conflicts**: output-formatter (different processing direction)

**Implementation**:
```javascript
// Basic validation with clear error messages
const rules = {
  required: ['name', 'email'],
  types: {age: 'number', email: 'email'},
  ranges: {age: {min: 0, max: 120}}
};

const result = validate_input(user_data, rules);
if (!result.valid) {
  return handle_error("validation", result.errors.join(", "));
}

// Continue processing only with validated data
process_validated_data(result.data);
```

**Category**: atomic | **Complexity**: moderate | **Time**: 15 minutes