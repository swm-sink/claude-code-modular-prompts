# Response Validator Component

**Purpose**: Validate response structure and content against expected schemas with comprehensive error reporting

**Usage**: 
Check response format matches expected schema and data structure requirements
Verify all required fields are present and properly formatted
Validate data types, value ranges, and constraint compliance
Ensure response completeness and accuracy for downstream processing
Handle unsupported formats with appropriate fallbacks and error messages
Flag structural inconsistencies and provide actionable validation feedback

**Compatibility**: 
- **Works with**: api-caller, input-validation, error-handler, data-transformer
- **Requires**: response_data (any), validation_schema (object)
- **Conflicts**: None known

**Implementation**:
```javascript
// Validate API response against expected schema
const schema = {
  required: ['status', 'data'],
  types: {
    status: 'string',
    data: 'object',
    timestamp: 'number'
  },
  constraints: {
    status: ['success', 'error', 'pending']
  }
};

const validation = validate_response(api_response, schema);
if (!validation.valid) {
  return handle_error("validation", `Invalid response: ${validation.errors.join(", ")}`);
}

// Continue with validated response
return process_validated_response(validation.data);
```

**Category**: atomic | **Complexity**: moderate | **Time**: 20 minutes