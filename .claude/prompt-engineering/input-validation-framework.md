# Input Validation Framework

| version | last_updated | status | security_level |
|---------|--------------|--------|----------------|
| 1.0.0   | 2025-07-20   | production | critical |

## Purpose

Comprehensive input validation framework following OWASP 2025 standards with whitelist-based validation, schema enforcement, and context-aware sanitization for all user inputs.

## Security Philosophy

**Defense in Depth**: Multiple validation layers ensure malicious inputs cannot penetrate the system.
**Whitelist Approach**: Only explicitly allowed patterns and values are accepted.
**Fail Secure**: Invalid inputs result in secure failure states, not bypasses.

## Core Validation Components

### 1. Whitelist-Based Validation Patterns

```xml
<whitelist_validation enforcement="BLOCKING">
  <input_categories>
    <command_names>
      <pattern>^/(auto|task|feature|query|swarm|session|protocol|init|docs|chain|meta|context-prime)$</pattern>
      <max_length>20</max_length>
      <case_sensitive>true</case_sensitive>
    </command_names>
    
    <file_paths>
      <pattern>^[a-zA-Z0-9._/\-]{1,500}$</pattern>
      <prohibited_sequences>\.\./, \\, \x00, \x0A, \x0D</prohibited_sequences>
      <required_extensions>.md, .py, .js, .ts, .json, .xml, .txt</required_extensions>
    </file_paths>
    
    <project_names>
      <pattern>^[a-zA-Z0-9\-_]{1,50}$</pattern>
      <prohibited_words>admin, root, system, config, secret, password</prohibited_words>
    </project_names>
    
    <user_content>
      <pattern>^[a-zA-Z0-9\s\-_.,:;!?()\[\]{}'"/@#$%&*+=]{1,5000}$</pattern>
      <script_detection>&lt;script|javascript:|data:|vbscript:|onload=|onerror=</script_detection>
      <injection_patterns>SELECT\s+|INSERT\s+|DELETE\s+|DROP\s+|UNION\s+|exec\(|eval\(</injection_patterns>
    </user_content>
  </input_categories>
</whitelist_validation>
```

### 2. Schema-Based Validation System

```xml
<schema_validation enforcement="MANDATORY">
  <command_schema>
    <structure>
      <command_name type="string" required="true" validation="whitelist"/>
      <parameters type="object" required="false" validation="schema"/>
      <context type="object" required="false" validation="sanitized"/>
      <options type="array" required="false" max_items="10"/>
    </structure>
    
    <parameter_schemas>
      <file_operation>
        <file_path type="string" validation="path_whitelist" max_length="500"/>
        <operation type="enum" values="read,write,edit,create" required="true"/>
        <content type="string" validation="content_sanitization" max_length="50000"/>
      </file_operation>
      
      <git_operation>
        <branch_name type="string" pattern="^[a-zA-Z0-9\-_/]{1,100}$"/>
        <commit_message type="string" max_length="500" validation="commit_sanitization"/>
        <file_paths type="array" max_items="100" item_validation="path_whitelist"/>
      </git_operation>
      
      <search_operation>
        <pattern type="string" max_length="200" validation="regex_sanitization"/>
        <scope type="enum" values="file,directory,content,global"/>
        <file_types type="array" max_items="20" item_pattern="^\.[a-z]{1,10}$"/>
      </search_operation>
    </parameter_schemas>
  </command_schema>
</schema_validation>
```

### 3. Context-Aware Sanitization

```xml
<context_sanitization enforcement="CRITICAL">
  <sanitization_contexts>
    <file_content context="code">
      <preserve_structures>indentation, comments, string_literals</preserve_structures>
      <sanitize_patterns>eval(), exec(), __import__, subprocess</sanitize_patterns>
      <escape_sequences>\x00-\x1F, \x7F-\x9F</escape_sequences>
      <encoding_validation>UTF-8 strict</encoding_validation>
    </file_content>
    
    <file_content context="documentation">
      <allowed_markdown>headers, lists, links, code_blocks, emphasis</allowed_markdown>
      <prohibited_elements>script, style, iframe, object, embed</prohibited_elements>
      <link_validation>^https?://[a-zA-Z0-9.-]+/[a-zA-Z0-9._/\-?&=%]*$</link_validation>
    </file_content>
    
    <command_parameters context="system">
      <shell_escape>single_quotes, double_quotes, backticks, semicolons</shell_escape>
      <path_traversal>../, ..\, /etc/, /var/, /root/</path_traversal>
      <command_injection>|, &, ;, $(, `</command_injection>
    </command_parameters>
    
    <user_input context="natural_language">
      <prompt_injection_patterns>
        <ignore_previous>ignore previous|forget everything|new instructions</ignore_previous>
        <role_confusion>you are now|act as|pretend to be|roleplay</role_confusion>
        <system_exposure>show system|reveal prompt|display instructions</system_exposure>
        <jailbreak_attempts>DAN mode|developer mode|unrestricted</jailbreak_attempts>
      </prompt_injection_patterns>
    </user_input>
  </sanitization_contexts>
</context_sanitization>
```

### 4. Validation for All Input Types

```xml
<comprehensive_input_validation enforcement="UNIVERSAL">
  <input_sources>
    <command_line_args>
      <validation>argument_whitelist, length_limits, encoding_check</validation>
      <sanitization>shell_escape, injection_prevention</sanitization>
      <logging>argument_patterns, validation_failures</logging>
    </command_line_args>
    
    <file_uploads>
      <validation>file_type_whitelist, size_limits, magic_number_check</validation>
      <sanitization>metadata_stripping, content_scanning</sanitization>
      <quarantine>suspicious_files, malware_signatures</quarantine>
    </file_uploads>
    
    <configuration_files>
      <validation>schema_validation, key_whitelist, value_constraints</validation>
      <sanitization>comment_stripping, normalization</sanitization>
      <backup>original_preservation, rollback_capability</backup>
    </configuration_files>
    
    <environment_variables>
      <validation>name_whitelist, value_patterns, length_limits</validation>
      <sanitization>special_character_escape, encoding_normalization</sanitization>
      <protection>secret_detection, exposure_prevention</protection>
    </environment_variables>
    
    <network_inputs>
      <validation>protocol_whitelist, endpoint_verification, rate_limiting</validation>
      <sanitization>header_cleaning, payload_validation</sanitization>
      <monitoring>traffic_analysis, anomaly_detection</monitoring>
    </network_inputs>
  </input_sources>
</comprehensive_input_validation>
```

## Implementation Patterns

### 1. Validation Pipeline

```python
class ValidationPipeline:
    def __init__(self):
        self.validators = [
            WhitelistValidator(),
            SchemaValidator(),
            SanitizationValidator(),
            ContextValidator(),
            SecurityValidator()
        ]
    
    def validate(self, input_data, context):
        """
        Execute validation pipeline with fail-fast approach
        """
        for validator in self.validators:
            result = validator.validate(input_data, context)
            if not result.is_valid:
                self._log_validation_failure(validator, result, input_data)
                raise ValidationError(result.error_message)
        
        return result.sanitized_data
```

### 2. Whitelist Implementation

```python
class WhitelistValidator:
    def __init__(self):
        self.patterns = {
            'command': r'^/(auto|task|feature|query|swarm|session|protocol|init|docs|chain|meta|context-prime)$',
            'file_path': r'^[a-zA-Z0-9._/\-]{1,500}$',
            'user_content': r'^[a-zA-Z0-9\s\-_.,:;!?()\[\]{}'"/@#$%&*+=]{1,5000}$'
        }
    
    def validate(self, input_data, context):
        pattern = self.patterns.get(context.input_type)
        if not pattern:
            return ValidationResult(False, "Unknown input type")
        
        if not re.match(pattern, input_data):
            return ValidationResult(False, f"Input does not match whitelist for {context.input_type}")
        
        return ValidationResult(True, input_data)
```

### 3. Context-Aware Sanitization

```python
class ContextAwareSanitizer:
    def sanitize(self, input_data, context):
        if context.type == 'code':
            return self._sanitize_code(input_data)
        elif context.type == 'documentation':
            return self._sanitize_documentation(input_data)
        elif context.type == 'system':
            return self._sanitize_system_input(input_data)
        elif context.type == 'natural_language':
            return self._sanitize_user_input(input_data)
        
        return self._default_sanitization(input_data)
    
    def _sanitize_code(self, code):
        # Remove dangerous functions while preserving code structure
        dangerous_patterns = ['eval(', 'exec(', '__import__', 'subprocess']
        for pattern in dangerous_patterns:
            if pattern in code:
                raise SecurityError(f"Dangerous pattern detected: {pattern}")
        return code
    
    def _sanitize_user_input(self, user_input):
        # Check for prompt injection patterns
        injection_patterns = [
            'ignore previous', 'forget everything', 'new instructions',
            'you are now', 'act as', 'pretend to be',
            'show system', 'reveal prompt', 'display instructions'
        ]
        
        for pattern in injection_patterns:
            if pattern.lower() in user_input.lower():
                raise SecurityError(f"Potential prompt injection detected: {pattern}")
        
        return user_input
```

## Security Controls

### 1. Input Length Limits

```xml
<length_controls enforcement="STRICT">
  <limits>
    <command_name max="20" min="1"/>
    <file_path max="500" min="1"/>
    <file_content max="50000" min="0"/>
    <user_input max="5000" min="0"/>
    <parameter_value max="1000" min="0"/>
    <array_items max="100" min="0"/>
  </limits>
  
  <enforcement>
    <exceeds_limit action="reject" log="true" alert="true"/>
    <empty_required action="reject" log="true"/>
    <malformed_encoding action="reject" log="true"/>
  </enforcement>
</length_controls>
```

### 2. Character Set Restrictions

```xml
<character_restrictions enforcement="UNIVERSAL">
  <allowed_sets>
    <alphanumeric>a-zA-Z0-9</alphanumeric>
    <punctuation>-_.,:;!?()\[\]{}'"/@#$%&*+=</punctuation>
    <whitespace>space, tab</whitespace>
    <newlines>LF only (\n)</newlines>
  </allowed_sets>
  
  <prohibited_characters>
    <control>\x00-\x08, \x0B, \x0C, \x0E-\x1F, \x7F-\x9F</control>
    <unicode_exploits>\u202E, \u2066-\u2069, \uFEFF</unicode_exploits>
    <shell_special>`, |, &amp;, ;, $, \</shell_special>
  </prohibited_characters>
</character_restrictions>
```

### 3. Encoding Validation

```xml
<encoding_validation enforcement="MANDATORY">
  <supported_encodings>
    <primary>UTF-8 strict</primary>
    <fallback>ASCII</fallback>
  </supported_encodings>
  
  <validation_rules>
    <rule>All inputs must be valid UTF-8</rule>
    <rule>No byte order marks (BOM) allowed</rule>
    <rule>No overlong sequences permitted</rule>
    <rule>No surrogate pairs in UTF-8</rule>
  </validation_rules>
  
  <error_handling>
    <invalid_encoding action="reject" log="critical"/>
    <suspicious_patterns action="quarantine" alert="true"/>
  </error_handling>
</encoding_validation>
```

## Error Handling

### 1. Secure Failure Modes

```python
class SecureValidationError(Exception):
    def __init__(self, message, input_sample=None):
        # Never expose full input in error messages
        self.safe_message = self._create_safe_message(message)
        self.input_hash = hashlib.sha256(str(input_sample).encode()).hexdigest()[:8] if input_sample else None
        super().__init__(self.safe_message)
    
    def _create_safe_message(self, message):
        # Generic error messages to prevent information leakage
        return "Input validation failed. Please check input format and try again."
```

### 2. Logging and Monitoring

```xml
<security_logging enforcement="COMPREHENSIVE">
  <log_categories>
    <validation_failures level="warning" details="input_type, pattern_failed, timestamp"/>
    <injection_attempts level="critical" details="source_ip, input_hash, detection_rule"/>
    <encoding_violations level="error" details="encoding_type, byte_sequence, location"/>
    <whitelist_violations level="warning" details="input_type, expected_pattern, actual_sample"/>
  </log_categories>
  
  <alerting>
    <thresholds>
      <validation_failures count="10" window="1_minute" action="alert"/>
      <injection_attempts count="1" window="1_second" action="immediate_alert"/>
      <pattern_violations count="5" window="5_minutes" action="investigate"/>
    </thresholds>
  </alerting>
</security_logging>
```

## Integration Points

### 1. Framework Integration

```xml
<framework_integration enforcement="MANDATORY">
  <validation_checkpoints>
    <command_entry>All command inputs validated before processing</command_entry>
    <file_operations>All file paths and content validated before access</file_operations>
    <user_interactions>All user inputs sanitized before use</user_interactions>
    <system_calls>All system parameters validated before execution</system_calls>
  </validation_checkpoints>
  
  <quality_gates>
    <gate>Input validation must pass before any command execution</gate>
    <gate>All file operations must validate paths and content</gate>
    <gate>All user inputs must be sanitized and validated</gate>
    <gate>All system interactions must validate parameters</gate>
  </quality_gates>
</framework_integration>
```

### 2. Performance Considerations

```xml
<performance_optimization enforcement="BALANCED">
  <caching>
    <validation_results ttl="300" max_size="1000"/>
    <pattern_compilation cache="true" precompile="common_patterns"/>
    <whitelist_lookups index="true" memory_mapped="true"/>
  </caching>
  
  <optimization>
    <early_rejection>Fail fast on obvious violations</early_rejection>
    <lazy_evaluation>Defer expensive validations until needed</lazy_evaluation>
    <batch_processing>Validate multiple inputs together when possible</batch_processing>
  </optimization>
</performance_optimization>
```

## Testing Strategy

### 1. Validation Testing

```python
class TestInputValidation:
    def test_whitelist_enforcement(self):
        validator = WhitelistValidator()
        
        # Valid inputs should pass
        assert validator.validate("valid_input", context).is_valid
        
        # Invalid inputs should fail
        with pytest.raises(ValidationError):
            validator.validate("../../../etc/passwd", path_context)
    
    def test_injection_prevention(self):
        sanitizer = ContextAwareSanitizer()
        
        # SQL injection attempts should be blocked
        with pytest.raises(SecurityError):
            sanitizer.sanitize("'; DROP TABLE users; --", sql_context)
        
        # Script injection should be blocked
        with pytest.raises(SecurityError):
            sanitizer.sanitize("<script>alert('xss')</script>", html_context)
```

### 2. Security Testing

```xml
<security_testing enforcement="COMPREHENSIVE">
  <test_categories>
    <injection_testing>
      <sql_injection>Standard payloads, blind injection, time-based</sql_injection>
      <script_injection>XSS, script tags, event handlers</script_injection>
      <command_injection>Shell metacharacters, command chaining</command_injection>
      <prompt_injection>Role confusion, instruction override, context escape</prompt_injection>
    </injection_testing>
    
    <bypass_testing>
      <encoding_bypass>URL encoding, HTML entities, Unicode normalization</encoding_bypass>
      <length_bypass>Buffer overflow attempts, truncation attacks</length_bypass>
      <character_bypass>Null bytes, control characters, homographs</character_bypass>
    </bypass_testing>
    
    <fuzzing>
      <random_inputs>Generated test cases, edge cases</random_inputs>
      <malformed_data>Invalid encoding, corrupted structures</malformed_data>
      <boundary_testing>Maximum lengths, edge values</boundary_testing>
    </fuzzing>
  </test_categories>
</security_testing>
```

## Compliance and Standards

### 1. OWASP 2025 Compliance

```xml
<owasp_compliance version="2025">
  <controls>
    <A01_broken_access_control>Input validation prevents unauthorized access</A01_broken_access_control>
    <A02_cryptographic_failures>Secure input handling prevents data exposure</A02_cryptographic_failures>
    <A03_injection>Comprehensive injection prevention</A03_injection>
    <A04_insecure_design>Security-first validation design</A04_insecure_design>
    <A05_security_misconfiguration>Secure defaults, proper validation</A05_security_misconfiguration>
  </controls>
</owasp_compliance>
```

### 2. Security Standards

```xml
<security_standards compliance="MANDATORY">
  <standards>
    <input_validation>NIST SP 800-53 SI-10</input_validation>
    <data_validation>ISO 27001 A.14.2.1</data_validation>
    <secure_coding>CWE-20, CWE-79, CWE-89, CWE-94</secure_coding>
    <prompt_security>NIST AI RMF 1.0</prompt_security>
  </standards>
</security_standards>
```

## Usage Examples

### 1. Command Validation

```python
# Validate command input
try:
    validated_command = input_validator.validate(
        user_input="/task implement authentication",
        context=CommandContext(type='command', source='user')
    )
except ValidationError as e:
    logger.warning(f"Invalid command input: {e}")
    return error_response("Invalid command format")
```

### 2. File Path Validation

```python
# Validate file paths
try:
    safe_path = input_validator.validate(
        file_path="src/auth/login.py",
        context=FileContext(type='file_path', operation='read')
    )
except ValidationError as e:
    logger.error(f"Unsafe file path: {e}")
    raise SecurityError("File access denied")
```

### 3. Content Sanitization

```python
# Sanitize user content
try:
    clean_content = content_sanitizer.sanitize(
        user_content="User's documentation text...",
        context=ContentContext(type='documentation', format='markdown')
    )
except SecurityError as e:
    logger.critical(f"Security violation detected: {e}")
    return rejection_response("Content contains prohibited elements")
```

## Deployment Checklist

- [ ] All input validation patterns tested and verified
- [ ] Whitelist patterns cover all expected input types
- [ ] Schema validation schemas defined for all data structures
- [ ] Context-aware sanitization implemented for all input contexts
- [ ] Security logging configured and tested
- [ ] Performance benchmarks established
- [ ] Integration tests pass with framework
- [ ] Security tests pass with no bypasses found
- [ ] Error handling provides secure failure modes
- [ ] Monitoring and alerting configured

---

**Critical Security Note**: This input validation framework implements defense-in-depth security with multiple validation layers. All inputs are validated, sanitized, and monitored. Any bypasses or security issues should be reported immediately as critical security incidents.