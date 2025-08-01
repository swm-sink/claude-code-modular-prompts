<prompt_component>
  <step name="Input Validation">
    <description>
      Comprehensive input validation for command arguments, ensuring type safety,
      format correctness, and security before execution.
    </description>
    <validation_types>
      1. **Type Validation**:
         - String: Non-empty, length limits, character restrictions
         - Number: Range validation, integer vs float
         - Boolean: True/false parsing
         - Array: Element count, element validation
         - Object: Required fields, nested validation
      
      2. **Format Validation**:
         - File paths: Existence, permissions, extensions
         - URLs: Protocol, domain, accessibility
         - Email: RFC compliance
         - Regex patterns: Valid syntax
         - JSON/YAML: Parse-ability
      
      3. **Security Validation**:
         - Path traversal prevention (../)
         - Command injection prevention
         - SQL injection prevention
         - Script injection prevention
         - Size limits enforcement
      
      4. **Business Logic Validation**:
         - Mutually exclusive options
         - Dependent field requirements
         - Valid option combinations
         - Context-specific rules
    </validation_types>
    <validation_patterns>
      ```javascript
      // String validation
      function validateString(value, options = {}) {
        if (!value || typeof value !== 'string') {
          throw new Error('Value must be a non-empty string');
        }
        if (options.minLength && value.length < options.minLength) {
          throw new Error(`Minimum length is ${options.minLength}`);
        }
        if (options.maxLength && value.length > options.maxLength) {
          throw new Error(`Maximum length is ${options.maxLength}`);
        }
        if (options.pattern && !options.pattern.test(value)) {
          throw new Error(`Value must match pattern: ${options.pattern}`);
        }
        return value.trim();
      }
      
      // Path validation
      function validatePath(path, options = {}) {
        if (path.includes('../') || path.includes('..\\')) {
          throw new Error('Path traversal not allowed');
        }
        if (options.mustExist && !fileExists(path)) {
          throw new Error(`Path does not exist: ${path}`);
        }
        if (options.extensions) {
          const ext = path.split('.').pop();
          if (!options.extensions.includes(ext)) {
            throw new Error(`Invalid file extension. Allowed: ${options.extensions.join(', ')}`);
          }
        }
        return path;
      }
      ```
    </validation_patterns>
    <error_messages>
      - Be specific about what's wrong
      - Provide the expected format/value
      - Suggest corrections when possible
      - Include validation context
      
      Examples:
      ❌ "Invalid input" (too vague)
      ✅ "Invalid file path: must end with .js or .ts"
      
      ❌ "Wrong format" (not helpful)
      ✅ "Date must be in YYYY-MM-DD format, got: 2024/12/25"
    </error_messages>
    <integration_example>
      ```xml
      <include>components/validation/input-validation.md</include>
      
      <arguments>
        <argument name="feature_name" type="string" required="true">
          <description>Feature name (alphanumeric, 3-50 chars)</description>
          <validation>
            <minLength>3</minLength>
            <maxLength>50</maxLength>
            <pattern>^[a-zA-Z0-9-_]+$</pattern>
          </validation>
        </argument>
      </arguments>
      ```
    </integration_example>
    <output>
      When implementing input validation:
      - Validate as early as possible
      - Provide clear, actionable error messages
      - Consider security implications
      - Allow for reasonable flexibility
      - Document validation rules clearly
    </output>
  </step>
</prompt_component>