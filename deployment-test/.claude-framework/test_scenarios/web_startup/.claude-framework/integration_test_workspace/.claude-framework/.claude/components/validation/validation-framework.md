<prompt_component>
  <step name="Comprehensive Validation Framework">
    <description>
Unified validation framework that ensures data integrity, format compliance, and security across all inputs, outputs, and configurations. Provides comprehensive validation for command arguments, structured data formats, and compliance with Claude Code standards.
    </description>
  </step>

  <validation_framework>
    <input_validation>
      <!-- Comprehensive input validation for command arguments -->
      <validation_types>
        <type_validation>
          <string_validation>
            - Non-empty validation with trimming
            - Length limits (min/max characters)
            - Character restrictions and allowed patterns
            - Encoding validation (UTF-8 compliance)
            - Whitespace normalization
          </string_validation>
          
          <number_validation>
            - Type checking (integer vs float)
            - Range validation (min/max values)
            - Precision and scale limits
            - NaN and Infinity handling
            - Unit conversion validation
          </number_validation>
          
          <boolean_validation>
            - True/false parsing flexibility
            - String representation handling ("yes"/"no", "1"/"0")
            - Null and undefined handling
            - Default value management
          </boolean_validation>
          
          <array_validation>
            - Element count limits
            - Element type validation
            - Uniqueness constraints
            - Order preservation
            - Nested array handling
          </array_validation>
          
          <object_validation>
            - Required field checking
            - Nested object validation
            - Schema compliance
            - Property type validation
            - Dynamic property handling
          </object_validation>
        </type_validation>
        
        <format_validation>
          <file_path_validation>
            - Path existence checking
            - Permission validation
            - Extension verification
            - Symlink resolution
            - Cross-platform compatibility
          </file_path_validation>
          
          <url_validation>
            - Protocol verification (http/https)
            - Domain name validation
            - Port range checking
            - Query parameter validation
            - URL encoding compliance
          </url_validation>
          
          <pattern_validation>
            - Email RFC compliance
            - Phone number formats
            - Date/time formats (ISO 8601)
            - Custom regex patterns
            - Locale-specific formats
          </pattern_validation>
          
          <structured_data_validation>
            - JSON parse-ability and schema
            - YAML syntax and structure
            - XML well-formedness
            - CSV format compliance
            - Configuration file formats
          </structured_data_validation>
        </format_validation>
        
        <security_validation>
          <injection_prevention>
            - Path traversal prevention (../, ..\)
            - Command injection prevention
            - SQL injection prevention
            - Script injection prevention
            - Template injection prevention
          </injection_prevention>
          
          <resource_limits>
            - File size limitations
            - String length caps
            - Array size boundaries
            - Memory usage limits
            - Execution time constraints
          </resource_limits>
          
          <content_filtering>
            - Malicious pattern detection
            - Sensitive data masking
            - PII detection and handling
            - Forbidden keyword blocking
            - Content type verification
          </content_filtering>
        </security_validation>
        
        <business_logic_validation>
          <relationship_validation>
            - Mutually exclusive options
            - Dependent field requirements
            - Valid option combinations
            - Context-specific rules
            - Cross-field validation
          </relationship_validation>
          
          <state_validation>
            - Workflow state transitions
            - Precondition checking
            - Postcondition verification
            - Invariant maintenance
            - Consistency rules
          </state_validation>
        </business_logic_validation>
      </validation_types>
      
      <validation_implementation>
        ```javascript
        // Comprehensive validation class
        class ValidationFramework {
          // String validation with all checks
          validateString(value, options = {}) {
            if (!value || typeof value !== 'string') {
              throw new ValidationError('Value must be a non-empty string');
            }
            
            const trimmed = value.trim();
            
            if (options.minLength && trimmed.length < options.minLength) {
              throw new ValidationError(`Minimum length is ${options.minLength}, got ${trimmed.length}`);
            }
            
            if (options.maxLength && trimmed.length > options.maxLength) {
              throw new ValidationError(`Maximum length is ${options.maxLength}, got ${trimmed.length}`);
            }
            
            if (options.pattern && !options.pattern.test(trimmed)) {
              throw new ValidationError(`Value must match pattern: ${options.pattern}`);
            }
            
            if (options.forbidden && options.forbidden.some(f => trimmed.includes(f))) {
              throw new ValidationError('Value contains forbidden characters or patterns');
            }
            
            return trimmed;
          }
          
          // Path validation with security checks
          validatePath(path, options = {}) {
            // Security check first
            if (path.includes('../') || path.includes('..\\')) {
              throw new SecurityError('Path traversal detected - access denied');
            }
            
            // Normalize path for platform
            const normalized = path.replace(/\\/g, '/');
            
            if (options.mustExist && !this.fileExists(normalized)) {
              throw new ValidationError(`Path does not exist: ${normalized}`);
            }
            
            if (options.permissions && !this.hasPermissions(normalized, options.permissions)) {
              throw new ValidationError(`Insufficient permissions for: ${normalized}`);
            }
            
            if (options.extensions) {
              const ext = normalized.split('.').pop().toLowerCase();
              if (!options.extensions.includes(ext)) {
                throw new ValidationError(`Invalid extension. Allowed: ${options.extensions.join(', ')}`);
              }
            }
            
            return normalized;
          }
          
          // Complex object validation
          validateObject(obj, schema) {
            const errors = [];
            
            // Check required fields
            for (const field of schema.required || []) {
              if (!(field in obj)) {
                errors.push(`Missing required field: ${field}`);
              }
            }
            
            // Validate each field
            for (const [key, value] of Object.entries(obj)) {
              if (schema.properties && schema.properties[key]) {
                try {
                  this.validateField(value, schema.properties[key]);
                } catch (error) {
                  errors.push(`${key}: ${error.message}`);
                }
              } else if (!schema.additionalProperties) {
                errors.push(`Unknown property: ${key}`);
              }
            }
            
            if (errors.length > 0) {
              throw new ValidationError(`Object validation failed:\n${errors.join('\n')}`);
            }
            
            return obj;
          }
        }
        ```
      </validation_implementation>
    </input_validation>
    
    <structure_validation>
      <!-- Validation for structured formats -->
      <yaml_frontmatter>
        <requirements>
          <format_rules>
            - Must start with `---` on first line
            - Must end with `---` on its own line  
            - Valid YAML syntax between delimiters
            - No trailing spaces or tabs
            - Consistent indentation (2 spaces)
          </format_rules>
          
          <required_fields>
            - description: Clear command description (5-15 words)
            - argument-hint: User-friendly argument format
            - allowed-tools: Comma-separated list of Claude Code tools
          </required_fields>
          
          <optional_fields>
            - tags: Searchable command tags
            - complexity: low, medium, or high
            - category: Primary categorization
            - version: Command version number
            - deprecated: Deprecation notice
          </optional_fields>
        </requirements>
        
        <validation_template>
          ```yaml
          ---
          description: {action_verb} {target_object} {qualifier}
          argument-hint: "[required_arg] <optional_arg>"
          allowed-tools: Read, Write, Edit, Bash, Grep
          tags: category, subcategory, feature
          complexity: medium
          ---
          ```
        </validation_template>
      </yaml_frontmatter>
      
      <xml_structure>
        <requirements>
          <document_structure>
            - Root element: `<command_file>` required
            - Well-formed XML with matching tags
            - Proper CDATA sections for code/scripts
            - No unescaped special characters (&, <, >)
            - Consistent indentation (2 spaces)
          </document_structure>
          
          <required_sections>
            - metadata: Command name, purpose, usage
            - arguments: Argument definitions with types
            - steps: Execution steps with instructions
            - output: Expected output format/structure
          </required_sections>
          
          <optional_sections>
            - examples: Usage examples with context
            - dependencies: Component dependencies
            - error_handling: Error scenarios/recovery
            - performance: Performance considerations
            - integration: Integration patterns
          </optional_sections>
        </requirements>
        
        <xml_template>
          ```xml
          <command_file>
            <metadata>
              <name>{command_name}</name>
              <purpose>{clear_purpose}</purpose>
              <usage><![CDATA[{usage_pattern}]]></usage>
            </metadata>
            
            <arguments>
              <argument name="{name}" type="{type}" required="{boolean}">
                <description>{description}</description>
                <validation>{rules}</validation>
              </argument>
            </arguments>
            
            <steps>
              <step name="{step_name}">
                <description>{step_description}</description>
                <implementation><![CDATA[{code}]]></implementation>
              </step>
            </steps>
            
            <o>{expected_output}</o>
          </command_file>
          ```
        </xml_template>
      </xml_structure>
      
      <json_schema_validation>
        <schema_features>
          - JSON Schema Draft 7 compliance
          - Type definitions and constraints
          - Pattern properties for dynamic keys
          - Conditional schema validation
          - Cross-property dependencies
        </schema_features>
        
        <implementation>
          ```json
          {
            "$schema": "http://json-schema.org/draft-07/schema#",
            "type": "object",
            "required": ["name", "type", "config"],
            "properties": {
              "name": {
                "type": "string",
                "minLength": 3,
                "maxLength": 50,
                "pattern": "^[a-zA-Z0-9-_]+$"
              },
              "type": {
                "type": "string",
                "enum": ["command", "component", "template"]
              },
              "config": {
                "type": "object",
                "additionalProperties": true
              }
            },
            "dependencies": {
              "type": {
                "oneOf": [
                  {
                    "properties": {
                      "type": { "const": "command" },
                      "config": {
                        "required": ["tools", "complexity"]
                      }
                    }
                  }
                ]
              }
            }
          }
          ```
        </implementation>
      </json_schema_validation>
    </structure_validation>
    
    <output_validation>
      <!-- Validation for command outputs -->
      <result_validation>
        <format_checking>
          - Expected output structure compliance
          - Data type verification
          - Field presence validation
          - Value range checking
          - Encoding verification
        </format_checking>
        
        <content_validation>
          - Business rule compliance
          - Referential integrity
          - Calculation accuracy
          - State consistency
          - Error absence verification
        </content_validation>
      </result_validation>
      
      <error_handling>
        <error_message_standards>
          <principles>
            - Be specific about what's wrong
            - Provide the expected format/value
            - Suggest corrections when possible
            - Include validation context
            - Avoid technical jargon
          </principles>
          
          <examples>
            ```
            ❌ "Invalid input" (too vague)
            ✅ "Invalid file path: must end with .js or .ts"
            
            ❌ "Wrong format" (not helpful)  
            ✅ "Date must be in YYYY-MM-DD format, got: 2024/12/25"
            
            ❌ "Validation failed" (no context)
            ✅ "Email validation failed: missing @ symbol in 'user.example.com'"
            ```
          </examples>
        </error_message_standards>
        
        <error_recovery>
          - Graceful degradation options
          - Fallback value suggestions
          - Partial success handling
          - Retry guidance
          - Alternative approaches
        </error_recovery>
      </error_handling>
    </output_validation>
    
    <integration_patterns>
      <!-- How to integrate validation into commands -->
      <command_integration>
        ```xml
        <include>components/validation/input-validation.md</include>
        
        <arguments>
          <argument name="feature_name" type="string" required="true">
            <description>Feature name (alphanumeric, 3-50 chars)</description>
            <validation>
              <type>string</type>
              <minLength>3</minLength>
              <maxLength>50</maxLength>
              <pattern>^[a-zA-Z0-9-_]+$</pattern>
              <forbidden>['admin', 'root', 'system']</forbidden>
            </validation>
          </argument>
          
          <argument name="options" type="object" required="false">
            <description>Configuration options</description>
            <validation>
              <type>object</type>
              <schema>{
                "properties": {
                  "dryRun": { "type": "boolean" },
                  "verbose": { "type": "boolean" },
                  "timeout": { "type": "number", "min": 0, "max": 3600 }
                }
              }</schema>
            </validation>
          </argument>
        </arguments>
        ```
      </command_integration>
      
      <best_practices>
        <timing>
          - Validate as early as possible
          - Perform security checks first
          - Cache validation results when appropriate
          - Batch validation for efficiency
        </timing>
        
        <flexibility>
          - Allow reasonable variations
          - Provide sensible defaults
          - Support common formats
          - Enable validation overrides
        </flexibility>
        
        <maintainability>
          - Document all validation rules
          - Centralize validation logic
          - Use consistent error formats
          - Version validation schemas
        </maintainability>
      </best_practices>
    </integration_patterns>
  </validation_framework>

  <o>
Comprehensive validation framework implemented with multi-layer protection:

**Input Validation:** Type, format, security, and business logic validation
**Structure Validation:** YAML frontmatter, XML structure, JSON schema compliance
**Security Features:** Injection prevention, resource limits, content filtering
**Error Handling:** Clear messages, recovery guidance, graceful degradation
**Integration:** Easy command integration with consistent patterns
**Standards Compliance:** Claude Code requirements fully supported
  </o>
</prompt_component>