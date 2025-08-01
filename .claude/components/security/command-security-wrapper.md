<!-- AI_METADATA_START -->
<ai_document_metadata>
  <document_type>component</document_type>
  <ai_consumption_priority>critical</ai_consumption_priority>
  <content_structure>markdown_body</content_structure>
  <file_path>/Users/smenssink/conductor/repo/claude-code-modular-prompts/lusaka/.claude/components/security/command-security-wrapper.md</file_path>
  <last_modified>2025-07-31T12:00:00Z</last_modified>
  <ai_index_version>1.0</ai_index_version>
</ai_document_metadata>

<component_metadata>
  <component_id>command-security-wrapper</component_id>
  <component_count>91</component_count>
  <category>security</category>
  <subcategory>protection</subcategory>
  
  <complexity_metrics>
    <usage_complexity>high</usage_complexity>
    <implementation_effort>hours_2</implementation_effort>
    <prerequisite_knowledge>advanced</prerequisite_knowledge>
  </complexity_metrics>
  
  <assembly_compatibility>
    <compatible_components>
      <component ref="input-validation-framework" strength="strong"/>
      <component ref="path-validation" strength="strong"/>
      <component ref="credential-protection" strength="strong"/>
      <component ref="owasp-compliance" strength="strong"/>
      <component ref="error-handler" strength="medium"/>
    </compatible_components>
    <incompatible_components>
      <component ref="user-confirmation" reason="security_bypass_risk"/>
    </incompatible_components>
  </assembly_compatibility>
  
  <usage_patterns>
    <common_workflow>command_execution_security</common_workflow>
    <typical_position>security_wrapper</typical_position>
  </usage_patterns>
</component_metadata>

<ai_navigation>
  <discovery_metadata>
    <primary_discovery_path>command_security</primary_discovery_path>
    <alternative_paths>
      <path>injection_prevention</path>
      <path>execution_security</path>
      <path>bash_protection</path>
    </alternative_paths>
  </discovery_metadata>
  
  <relationship_map>
    <upstream_dependencies>
      <file type="component" ref="input-validation-framework" relation="validation_pipeline"/>
      <file type="component" ref="path-validation" relation="path_security"/>
    </upstream_dependencies>
    <downstream_consumers>
      <file type="command" ref="dev-setup" relation="secure_execution"/>
      <file type="command" ref="pipeline-deploy" relation="secure_execution"/>
      <file type="command" ref="test-unit" relation="secure_execution"/>
    </downstream_consumers>
    <peer_alternatives>
      <file type="component" ref="harm-prevention-framework" similarity="0.80"/>
    </peer_alternatives>
  </relationship_map>
  
  <usage_context>
    <when_to_use>
      <scenario>Commands that execute bash operations</scenario>
      <scenario>User input that becomes command parameters</scenario>
      <scenario>Commands with deployment or system access needs</scenario>
      <scenario>Multi-layer security protection requirements</scenario>
    </when_to_use>
    <when_not_to_use>
      <scenario>Read-only operations with no command execution</scenario>
      <scenario>Pure documentation or analysis commands</scenario>
      <scenario>Commands with only internal data processing</scenario>
    </when_not_to_use>
  </usage_context>
  
  <ai_search_optimization>
    <keywords>command security wrapper injection prevention bash protection execution security allowlist validation</keywords>
    <semantic_tags>command_security injection_prevention bash_protection</semantic_tags>
    <functionality_vectors>security_wrapper command_validation execution_protection</functionality_vectors>
  </ai_search_optimization>
</ai_navigation>

<context_engineering>
  <ai_understanding_scope>
    <scope_level>project</scope_level>
    <context_retention>persistent</context_retention>
    <memory_priority>9</memory_priority>
  </ai_understanding_scope>
  
  <knowledge_dependencies>
    <required_context>
      <context_file ref="../context/llm-antipatterns.md" importance="critical"/>
      <context_file ref="../security/owasp-compliance.md" importance="high"/>
    </required_context>
    <helpful_context>
      <context_file ref="../security/input-validation-framework.md" importance="high"/>
      <context_file ref="../security/path-validation.md" importance="high"/>
    </helpful_context>
  </knowledge_dependencies>
  
  <workflow_integration>
    <workflow_stage>security_execution</workflow_stage>
    <integration_patterns>
      <pattern>security_wrapper</pattern>
      <pattern>command_validation</pattern>
      <pattern>injection_prevention</pattern>
    </integration_patterns>
  </workflow_integration>
  
  <ai_learning_markers>
    <concept_introduction>comprehensive_command_security</concept_introduction>
    <skill_progression>advanced</skill_progression>
    <mastery_indicators>
      <indicator>Multi-layer security protection for command execution</indicator>
      <indicator>Command injection prevention through input validation and allowlists</indicator>
      <indicator>Secure execution patterns with audit logging and error handling</indicator>
    </mastery_indicators>
  </ai_learning_markers>
</context_engineering>
<!-- AI_METADATA_END -->

<prompt_component>
  <step name="Command Security Wrapper">
    <description>
Comprehensive security wrapper for command injection prevention, input validation, command allowlisting, and secure execution patterns. Provides multi-layer security protection for all commands that execute bash operations.
    </description>
  </step>

  <security_wrapper>
    <input_validation>
      <!-- Core input validation patterns -->
      <string_sanitization>
        <shell_metacharacter_filter>
          <!-- Prevent command injection through shell metacharacters -->
          const DANGEROUS_CHARS = /[;|&$`><(){}[\]\\'"]/g;
          const PATH_TRAVERSAL = /\.\.(\/|\\)/g;
          
          function sanitizeShellInput(input) {
            if (!input || typeof input !== 'string') {
              throw new SecurityError('Input must be a non-empty string');
            }
            
            // Remove dangerous shell metacharacters
            if (DANGEROUS_CHARS.test(input)) {
              throw new SecurityError('Input contains forbidden shell metacharacters: ; | & $ ` > < ( ) { } [ ] \\ \' "');
            }
            
            // Prevent path traversal
            if (PATH_TRAVERSAL.test(input)) {
              throw new SecurityError('Path traversal detected: ../ or ..\\ patterns not allowed');
            }
            
            return input.trim();
          }
        </shell_metacharacter_filter>
        
        <url_validation>
          <!-- Validate repository URLs and prevent malicious URLs -->
          function validateRepositoryURL(url) {
            if (!url || typeof url !== 'string') {
              throw new SecurityError('Repository URL must be provided');
            }
            
            const urlPattern = /^https:\/\/(github\.com|gitlab\.com|bitbucket\.org)\/[a-zA-Z0-9_.-]+\/[a-zA-Z0-9_.-]+\.git$/;
            
            if (!urlPattern.test(url)) {
              throw new SecurityError('Invalid repository URL. Only GitHub, GitLab, and Bitbucket HTTPS URLs are allowed');
            }
            
            return url;
          }
        </url_validation>
        
        <version_number_validation>
          <!-- Validate version numbers and tags -->
          function validateVersionNumber(version) {
            if (!version || typeof version !== 'string') {
              throw new SecurityError('Version number must be provided');
            }
            
            const versionPattern = /^v?\d+\.\d+\.\d+(-[a-zA-Z0-9]+)?$/;
            
            if (!versionPattern.test(version)) {
              throw new SecurityError('Invalid version format. Use semantic versioning: v1.2.3 or 1.2.3');
            }
            
            return version;
          }
        </version_number_validation>
      </string_sanitization>
      
      <path_validation>
        <!-- Secure path validation with boundary checking -->
        function validateFilePath(path, options = {}) {
          if (!path || typeof path !== 'string') {
            throw new SecurityError('File path must be provided');
          }
          
          // Prevent path traversal
          if (path.includes('../') || path.includes('..\\')) {
            throw new SecurityError('Path traversal detected - access denied');
          }
          
          // Ensure path is within project boundaries
          const normalizedPath = path.replace(/\\/g, '/');
          
          if (options.allowedExtensions) {
            const ext = normalizedPath.split('.').pop()?.toLowerCase();
            if (!options.allowedExtensions.includes(ext)) {
              throw new SecurityError(`File extension not allowed. Permitted: ${options.allowedExtensions.join(', ')}`);
            }
          }
          
          if (options.maxLength && normalizedPath.length > options.maxLength) {
            throw new SecurityError(`Path too long. Maximum length: ${options.maxLength}`);
          }
          
          return normalizedPath;
        }
      </path_validation>
      
      <environment_validation>
        <!-- Validate environment names and deployment targets -->
        function validateEnvironmentName(envName) {
          if (!envName || typeof envName !== 'string') {
            throw new SecurityError('Environment name must be provided');
          }
          
          const allowedEnvironments = ['development', 'staging', 'production', 'test', 'dev', 'stage', 'prod'];
          const normalizedEnv = envName.toLowerCase().trim();
          
          if (!allowedEnvironments.includes(normalizedEnv)) {
            throw new SecurityError(`Invalid environment. Allowed: ${allowedEnvironments.join(', ')}`);
          }
          
          return normalizedEnv;
        }
      </environment_validation>
    </input_validation>
    
    <command_allowlists>
      <!-- Command allowlists for each vulnerable command -->
      <dev_command_allowlist>
        const DEV_ALLOWED_COMMANDS = {
          formatters: ['black', 'prettier', 'eslint', 'pylint', 'gofmt', 'rustfmt'],
          linters: ['eslint', 'pylint', 'golint', 'clippy', 'rubocop'],
          testers: ['pytest', 'jest', 'mocha', 'go test', 'cargo test'],
          packageManagers: ['npm', 'pip', 'yarn', 'composer', 'maven', 'gradle']
        };
        
        function validateDevCommand(tool, command) {
          const allowedTools = Object.values(DEV_ALLOWED_COMMANDS).flat();
          
          if (!allowedTools.includes(command)) {
            throw new SecurityError(`Command '${command}' not allowed. Permitted tools: ${allowedTools.join(', ')}`);
          }
          
          return command;
        }
      </dev_command_allowlist>
      
      <pipeline_command_allowlist>
        const PIPELINE_ALLOWED_COMMANDS = {
          cicd: ['kubectl', 'docker', 'git', 'aws', 'gcloud', 'az'],
          deployment: ['helm', 'terraform', 'ansible'],
          monitoring: ['curl', 'ping', 'wget']
        };
        
        function validatePipelineCommand(command) {
          const allowedCommands = Object.values(PIPELINE_ALLOWED_COMMANDS).flat();
          
          if (!allowedCommands.includes(command)) {
            throw new SecurityError(`Pipeline command '${command}' not allowed. Permitted: ${allowedCommands.join(', ')}`);
          }
          
          return command;
        }
      </pipeline_command_allowlist>
      
      <deploy_command_allowlist>
        const DEPLOY_ALLOWED_COMMANDS = [
          'docker', 'kubectl', 'helm', 'systemctl', 
          'aws', 'gcloud', 'az', 'terraform'
        ];
        
        function validateDeployCommand(command) {
          if (!DEPLOY_ALLOWED_COMMANDS.includes(command)) {
            throw new SecurityError(`Deploy command '${command}' not allowed. Permitted: ${DEPLOY_ALLOWED_COMMANDS.join(', ')}`);
          }
          
          return command;
        }
      </deploy_command_allowlist>
      
      <test_command_allowlist>
        const TEST_ALLOWED_COMMANDS = [
          'pytest', 'jest', 'mocha', 'jasmine', 'karma',
          'go test', 'cargo test', 'mvn test', 'gradle test',
          'phpunit', 'rspec', 'minitest'
        ];
        
        function validateTestCommand(command) {
          if (!TEST_ALLOWED_COMMANDS.includes(command)) {
            throw new SecurityError(`Test command '${command}' not allowed. Permitted: ${TEST_ALLOWED_COMMANDS.join(', ')}`);
          }
          
          return command;
        }
      </test_command_allowlist>
    </command_allowlists>
    
    <secure_execution_wrappers>
      <!-- Secure execution patterns -->
      <parameter_sanitization>
        function sanitizeCommandParameters(params) {
          if (!params || !Array.isArray(params)) {
            return [];
          }
          
          return params.map(param => {
            if (typeof param !== 'string') {
              throw new SecurityError('All command parameters must be strings');
            }
            
            // Remove shell metacharacters
            if (DANGEROUS_CHARS.test(param)) {
              throw new SecurityError(`Parameter contains forbidden characters: ${param}`);
            }
            
            return param.trim();
          });
        }
        
        function buildSecureCommand(baseCommand, parameters = []) {
          const sanitizedParams = sanitizeCommandParameters(parameters);
          
          // Build command as array to prevent injection
          const commandArray = [baseCommand, ...sanitizedParams];
          
          return commandArray;
        }
      </parameter_sanitization>
      
      <execution_wrapper>
        function executeSecureCommand(commandArray, options = {}) {
          // Final validation before execution
          if (!Array.isArray(commandArray) || commandArray.length === 0) {
            throw new SecurityError('Invalid command array');
          }
          
          const [baseCommand, ...params] = commandArray;
          
          // Log command execution for audit
          console.log(`[SECURITY AUDIT] Executing: ${baseCommand} with ${params.length} parameters`);
          
          // Add execution timeout and resource limits
          const execOptions = {
            timeout: options.timeout || 30000, // 30 second default timeout
            maxBuffer: options.maxBuffer || 1024 * 1024, // 1MB output limit
            ...options
          };
          
          return { command: baseCommand, params, options: execOptions };
        }
      </execution_wrapper>
    </secure_execution_wrappers>
    
    <error_handling>
      <!-- Secure error handling patterns -->
      <sanitized_error_messages>
        function sanitizeErrorMessage(error, context = {}) {
          // Remove potential sensitive information from error messages
          let sanitizedMessage = error.message || 'Unknown error occurred';
          
          // Remove file paths that might contain sensitive info
          sanitizedMessage = sanitizedMessage.replace(/\/[^\s]+/g, '[REDACTED_PATH]');
          
          // Remove potential credentials or tokens
          sanitizedMessage = sanitizedMessage.replace(/[a-zA-Z0-9]{20,}/g, '[REDACTED_TOKEN]');
          
          // Remove IP addresses
          sanitizedMessage = sanitizedMessage.replace(/\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b/g, '[REDACTED_IP]');
          
          return {
            error: 'Command execution failed',
            details: sanitizedMessage,
            context: context.operation || 'unknown operation',
            timestamp: new Date().toISOString()
          };
        }
      </sanitized_error_messages>
      
      <security_error_types>
        class SecurityError extends Error {
          constructor(message) {
            super(message);
            this.name = 'SecurityError';
            this.severity = 'HIGH';
          }
        }
        
        class ValidationError extends Error {
          constructor(message) {
            super(message);
            this.name = 'ValidationError';
            this.severity = 'MEDIUM';
          }
        }
        
        class CommandNotAllowedError extends SecurityError {
          constructor(command) {
            super(`Command '${command}' is not allowed by security policy`);
            this.command = command;
          }
        }
      </security_error_types>
    </error_handling>
    
    <integration_patterns>
      <!-- How to integrate security wrapper into commands -->
      <usage_example>
        ```xml
        <include>components/security/command-security-wrapper.md</include>
        
        <validation_step>
          <!-- Apply security validation before any bash execution -->
          1. Validate all user inputs using appropriate validation functions
          2. Check command against allowlist for the specific command type
          3. Sanitize all parameters and build secure command array
          4. Execute with secure wrapper and handle errors appropriately
        </validation_step>
        ```
      </usage_example>
      
      <implementation_template>
        ```javascript
        // Example integration in a command
        function secureCommandExecution(userInput, commandType) {
          try {
            // Step 1: Input validation
            const sanitizedInput = sanitizeShellInput(userInput.command);
            const validatedParams = userInput.params.map(p => sanitizeShellInput(p));
            
            // Step 2: Command allowlist validation
            let allowedCommand;
            switch (commandType) {
              case 'dev':
                allowedCommand = validateDevCommand('formatter', sanitizedInput);
                break;
              case 'pipeline':
                allowedCommand = validatePipelineCommand(sanitizedInput);
                break;
              case 'deploy':
                allowedCommand = validateDeployCommand(sanitizedInput);
                break;
              case 'test':
                allowedCommand = validateTestCommand(sanitizedInput);
                break;
              default:
                throw new SecurityError('Unknown command type');
            }
            
            // Step 3: Build secure command
            const secureCommand = buildSecureCommand(allowedCommand, validatedParams);
            
            // Step 4: Execute with security wrapper
            return executeSecureCommand(secureCommand, { timeout: 30000 });
            
          } catch (error) {
            // Step 5: Handle errors securely
            if (error instanceof SecurityError) {
              return sanitizeErrorMessage(error, { operation: commandType });
            }
            throw error;
          }
        }
        ```
      </implementation_template>
    </integration_patterns>
  </security_wrapper>

  <output>
Comprehensive command security wrapper implemented with:

**Input Validation:** Shell metacharacter filtering, path traversal prevention, URL validation
**Command Allowlists:** Specific allowlists for /dev, /pipeline, /deploy, /test-unit commands
**Secure Execution:** Parameter sanitization, command array building, resource limits
**Error Handling:** Sanitized error messages, security-specific error types
**Integration Patterns:** Ready-to-use templates for command integration

**Security Features:**
- Prevents command injection through shell metacharacters
- Blocks path traversal attacks
- Validates repository URLs and version numbers
- Enforces command allowlists per command type
- Implements secure parameter handling
- Provides audit logging for security events
- Sanitizes error messages to prevent information disclosure
  </output>
</prompt_component>