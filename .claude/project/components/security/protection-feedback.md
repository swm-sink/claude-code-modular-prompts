<!-- AI_METADATA_START -->
<ai_document_metadata>
  <document_type>component</document_type>
  <ai_consumption_priority>high</ai_consumption_priority>
  <content_structure>markdown_body</content_structure>
  <file_path>/Users/smenssink/conductor/repo/claude-code-modular-prompts/lusaka/.claude/components/security/protection-feedback.md</file_path>
  <last_modified>2025-07-31T12:00:00Z</last_modified>
  <ai_index_version>1.0</ai_index_version>
</ai_document_metadata>

<component_metadata>
  <component_id>protection-feedback</component_id>
  <component_count>91</component_count>
  <category>security</category>
  <subcategory>monitoring</subcategory>
  
  <complexity_metrics>
    <usage_complexity>moderate</usage_complexity>
    <implementation_effort>hours_1</implementation_effort>
    <prerequisite_knowledge>intermediate</prerequisite_knowledge>
  </complexity_metrics>
  
  <assembly_compatibility>
    <compatible_components>
      <component ref="credential-protection" strength="strong"/>
      <component ref="command-security-wrapper" strength="strong"/>
      <component ref="harm-prevention-framework" strength="medium"/>
      <component ref="progress-indicator" strength="medium"/>
      <component ref="task-summary" strength="medium"/>
    </compatible_components>
    <incompatible_components>
      <component ref="quick-command" reason="complexity_mismatch"/>
    </incompatible_components>
  </assembly_compatibility>
  
  <usage_patterns>
    <common_workflow>security_feedback</common_workflow>
    <typical_position>user_interface</typical_position>
  </usage_patterns>
</component_metadata>

<ai_navigation>
  <discovery_metadata>
    <primary_discovery_path>security_feedback</primary_discovery_path>
    <alternative_paths>
      <path>user_security_awareness</path>
      <path>protection_reporting</path>
      <path>security_metrics</path>
    </alternative_paths>
  </discovery_metadata>
  
  <relationship_map>
    <upstream_dependencies>
      <file type="component" ref="credential-protection" relation="protection_reporting"/>
      <file type="component" ref="command-security-wrapper" relation="security_events"/>
    </upstream_dependencies>
    <downstream_consumers>
      <file type="command" ref="secure-assess" relation="protection_feedback"/>
      <file type="command" ref="db-migrate" relation="protection_feedback"/>
      <file type="command" ref="deploy" relation="protection_feedback"/>
    </downstream_consumers>
    <peer_alternatives>
      <file type="component" ref="progress-indicator" similarity="0.60"/>
    </peer_alternatives>
  </relationship_map>
  
  <usage_context>
    <when_to_use>
      <scenario>Commands with active credential protection</scenario>
      <scenario>User needs visibility into security measures</scenario>
      <scenario>Security compliance reporting requirements</scenario>
      <scenario>Commands handling sensitive data processing</scenario>
    </when_to_use>
    <when_not_to_use>
      <scenario>Commands with no security implications</scenario>
      <scenario>Internal processing without user interaction</scenario>
      <scenario>Read-only documentation commands</scenario>
    </when_not_to_use>
  </usage_context>
  
  <ai_search_optimization>
    <keywords>security feedback protection notification user awareness credential masking security reporting</keywords>
    <semantic_tags>security_feedback protection_reporting user_awareness</semantic_tags>
    <functionality_vectors>security_notification protection_visibility user_feedback</functionality_vectors>
  </ai_search_optimization>
</ai_navigation>

<context_engineering>
  <ai_understanding_scope>
    <scope_level>local</scope_level>
    <context_retention>session</context_retention>
    <memory_priority>7</memory_priority>
  </ai_understanding_scope>
  
  <knowledge_dependencies>
    <required_context>
      <context_file ref="../security/credential-protection.md" importance="critical"/>
    </required_context>
    <helpful_context>
      <context_file ref="../security/command-security-wrapper.md" importance="high"/>
      <context_file ref="../atomic/progress-indicator.md" importance="medium"/>
    </helpful_context>
  </knowledge_dependencies>
  
  <workflow_integration>
    <workflow_stage>user_feedback</workflow_stage>
    <integration_patterns>
      <pattern>security_notification</pattern>
      <pattern>protection_reporting</pattern>
      <pattern>user_awareness</pattern>
    </integration_patterns>
  </workflow_integration>
  
  <ai_learning_markers>
    <concept_introduction>security_feedback_systems</concept_introduction>
    <skill_progression>intermediate</skill_progression>
    <mastery_indicators>
      <indicator>Real-time security protection notifications</indicator>
      <indicator>Command-specific protection feedback and reporting</indicator>
      <indicator>Security metrics and user awareness systems</indicator>
    </mastery_indicators>
  </ai_learning_markers>
</context_engineering>
<!-- AI_METADATA_END -->

<prompt_component>
  <step name="Security Protection User Feedback">
    <description>
Real-time user feedback system that shows when credential protection is active during command execution.
Provides visible confirmation that sensitive data is being masked.
    </description>
  </step>

  <protection_feedback>
    <real_time_notifications>
      <!-- Functions to show protection status during command execution -->
      <protection_status_display>
        function showProtectionStatus(detectionResult) {
          if (!detectionResult || typeof detectionResult !== 'object') {
            return '';
          }
          
          if (detectionResult.detectedCredentials > 0) {
            const credentialText = detectionResult.detectedCredentials === 1 ? 'credential' : 'credentials';
            const typesList = detectionResult.credentialTypes.join(', ');
            
            return `🔒 SECURITY PROTECTION ACTIVE: ${detectionResult.detectedCredentials} ${credentialText} masked (${typesList})`;
          } else {
            return '✅ No sensitive data detected in output';
          }
        }
        
        function showCommandProtectionBanner(commandName) {
          const securityNotice = [
            `🛡️ CREDENTIAL PROTECTION ENABLED FOR ${commandName.toUpperCase()}`,
            ``,
            `✅ 13 credential patterns monitored (AWS, API keys, database URLs, tokens)`,
            `✅ Real-time output scanning and masking active`,
            `✅ Error message sanitization enabled`,
            ``,
            `Command output will be automatically protected...`
          ].join('\n');
          
          return securityNotice;
        }
      </protection_status_display>
      
      <progress_indicators>
        function showProtectionProgress(phase, details = {}) {
          const phases = {
            'scanning_input': {
              icon: '🔍',
              message: 'Scanning command input for credentials...',
              details: details.inputLength ? `(${details.inputLength} characters scanned)` : ''
            },
            'executing_protected': {
              icon: '⚡',
              message: 'Executing command with credential protection...',
              details: details.command ? `Running: ${details.command}` : ''
            },
            'sanitizing_output': {
              icon: '🧹',
              message: 'Sanitizing command output...',
              details: details.outputLength ? `(${details.outputLength} characters processed)` : ''
            },
            'protection_complete': {
              icon: '✅',
              message: 'Command execution complete with protection active',
              details: details.maskedCount ? `${details.maskedCount} items masked` : 'No sensitive data found'
            }
          };
          
          const phaseInfo = phases[phase] || { icon: 'ℹ️', message: 'Processing...', details: '' };
          
          return `${phaseInfo.icon} ${phaseInfo.message} ${phaseInfo.details}`.trim();
        }
      </progress_indicators>
    </real_time_notifications>
    
    <command_specific_feedback>
      <!-- Feedback tailored to specific commands -->
      <secure_assess_feedback>
        function getSecureAssessFeedback(scanResults) {
          const feedback = [
            showCommandProtectionBanner('/secure-assess'),
            ''
          ];
          
          if (scanResults.toolOutputs) {
            scanResults.toolOutputs.forEach(output => {
              if (output.credentialsMasked) {
                feedback.push(`🔒 ${output.toolName}: ${output.maskingInfo.credentialCount} credentials masked (${output.maskingInfo.types.join(', ')})`);
              } else {
                feedback.push(`✅ ${output.toolName}: No credentials detected`);
              }
            });
          }
          
          if (scanResults.totalCredentialsMasked > 0) {
            feedback.push('');
            feedback.push(`🛡️ TOTAL PROTECTION: ${scanResults.totalCredentialsMasked} credentials masked across all security tools`);
          }
          
          return feedback.join('\n');
        }
      </secure_assess_feedback>
      
      <db_migrate_feedback>
        function getDbMigrateFeedback(migrationResults) {
          const feedback = [
            showCommandProtectionBanner('/db-migrate'),
            ''
          ];
          
          if (migrationResults.connectionStringMasked) {
            feedback.push('🔒 Database connection string detected and masked for security');
          }
          
          if (migrationResults.errorsMasked > 0) {
            feedback.push(`🔒 ${migrationResults.errorsMasked} error messages sanitized to prevent credential exposure`);
          }
          
          if (migrationResults.migrationStatus) {
            feedback.push(`📊 Migration Status: ${migrationResults.migrationStatus} (credentials protected)`);
          }
          
          return feedback.join('\n');
        }
      </db_migrate_feedback>
      
      <deploy_feedback>
        function getDeployFeedback(deploymentResults) {
          const feedback = [
            showCommandProtectionBanner('/deploy'),
            ''
          ];
          
          const protectedServices = [];
          
          if (deploymentResults.awsCredentialsMasked) {
            protectedServices.push('AWS credentials');
          }
          
          if (deploymentResults.kubernetesSecretsMasked) {
            protectedServices.push('Kubernetes secrets');
          }
          
          if (deploymentResults.dockerAuthMasked) {
            protectedServices.push('Docker registry authentication');
          }
          
          if (deploymentResults.gcpCredentialsMasked) {
            protectedServices.push('GCP service account keys');
          }
          
          if (deploymentResults.azureCredentialsMasked) {
            protectedServices.push('Azure client secrets');
          }
          
          if (protectedServices.length > 0) {
            feedback.push('🔒 PROTECTED SERVICES:');
            protectedServices.forEach(service => {
              feedback.push(`   ✓ ${service}`);
            });
          } else {
            feedback.push('✅ No cloud provider credentials detected in deployment output');
          }
          
          if (deploymentResults.deploymentSuccessful) {
            feedback.push('');
            feedback.push('🚀 Deployment completed successfully with full credential protection');
          }
          
          return feedback.join('\n');
        }
      </deploy_feedback>
    </command_specific_feedback>
    
    <security_summary_reporting>
      <!-- End-of-command security summary -->
      <generate_security_summary>
        function generateSecuritySummary(protectionResults) {
          const summary = {
            timestamp: new Date().toISOString(),
            protectionActive: protectionResults.credentialsDetected > 0,
            credentialsProtected: protectionResults.credentialsDetected || 0,
            credentialTypes: protectionResults.credentialTypes || [],
            commandsProtected: protectionResults.commandsExecuted || 0,
            errorsSanitized: protectionResults.errorsSanitized || 0
          };
          
          const report = [
            '🔒 SECURITY PROTECTION SUMMARY',
            '━'.repeat(40),
            `Timestamp: ${summary.timestamp}`,
            `Protection Status: ${summary.protectionActive ? '🟢 ACTIVE' : '🟡 MONITORING'}`,
            `Credentials Protected: ${summary.credentialsProtected}`,
            `Credential Types: ${summary.credentialTypes.length > 0 ? summary.credentialTypes.join(', ') : 'None detected'}`,
            `Commands Protected: ${summary.commandsProtected}`,
            `Errors Sanitized: ${summary.errorsSanitized}`,
            '━'.repeat(40)
          ];
          
          if (summary.protectionActive) {
            report.push('✅ Sensitive data successfully protected from exposure');
          } else {
            report.push('✅ No sensitive data detected - command executed safely');
          }
          
          return report.join('\n');
        }
      </generate_security_summary>
      
      <protection_metrics>
        function trackProtectionMetrics(sessionResults) {
          return {
            session_start: sessionResults.startTime,
            total_commands_protected: sessionResults.commandsExecuted,
            total_credentials_masked: sessionResults.credentialsMasked,
            protection_effectiveness: sessionResults.credentialsMasked > 0 ? 'HIGH' : 'MONITORING',
            most_common_credential_types: sessionResults.topCredentialTypes || [],
            commands_with_protection: sessionResults.protectedCommands || [],
            user_security_score: calculateSecurityScore(sessionResults)
          };
        }
        
        function calculateSecurityScore(results) {
          // Higher score for successful protection without false positives
          let score = 100; // Base score
          
          if (results.credentialsMasked > 0) {
            score += 20; // Bonus for active protection
          }
          
          if (results.falsePositives > 0) {
            score -= results.falsePositives * 5; // Penalty for false positives
          }
          
          if (results.missedCredentials > 0) {
            score -= results.missedCredentials * 10; // Penalty for missed credentials
          }
          
          return Math.max(0, Math.min(100, score));
        }
      </protection_metrics>
    </security_summary_reporting>
    
    <integration_examples>
      <!-- How to integrate feedback into commands -->
      <usage_patterns>
        ```markdown
        <!-- In command execution -->
        
        ## Step 1: Show protection banner
        ${showCommandProtectionBanner('/secure-assess')}
        
        ## Step 2: Execute with progress updates
        ${showProtectionProgress('scanning_input', { inputLength: userInput.length })}
        
        <!-- Execute actual command with protection -->
        ${showProtectionProgress('executing_protected', { command: actualCommand })}
        
        ## Step 3: Show results with protection status
        ${showProtectionStatus(detectionResult)}
        
        ## Step 4: Provide command-specific feedback
        ${getSecureAssessFeedback(scanResults)}
        
        ## Step 5: Generate security summary
        ${generateSecuritySummary(protectionResults)}
        ```
      </usage_patterns>
      
      <real_world_example>
        ```markdown
        🛡️ CREDENTIAL PROTECTION ENABLED FOR /SECURE-ASSESS

        ✅ 13 credential patterns monitored (AWS, API keys, database URLs, tokens)
        ✅ Real-time output scanning and masking active
        ✅ Error message sanitization enabled

        Command output will be automatically protected...

        🔍 Scanning command input for credentials... (245 characters scanned)
        ⚡ Executing command with credential protection... Running: snyk test
        🧹 Sanitizing command output... (1,245 characters processed)
        
        🔒 SECURITY PROTECTION ACTIVE: 3 credentials masked (aws_access_key, api_key, db_connection)
        
        🔒 Snyk Security Scanner: 2 credentials masked (aws_access_key, api_key)
        ✅ Dependency Checker: No credentials detected
        🔒 Secret Scanner: 1 credentials masked (db_connection)
        
        🛡️ TOTAL PROTECTION: 3 credentials masked across all security tools
        
        🔒 SECURITY PROTECTION SUMMARY
        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
        Timestamp: 2025-07-29T01:15:30.123Z
        Protection Status: 🟢 ACTIVE
        Credentials Protected: 3
        Credential Types: aws_access_key, api_key, db_connection
        Commands Protected: 3
        Errors Sanitized: 0
        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
        ✅ Sensitive data successfully protected from exposure
        ```
      </real_world_example>
    </integration_examples>
  </protection_feedback>

  <output>
User feedback system for credential protection implemented with:

**Real-time Notifications:**
- Protection status display showing masked credential count and types
- Command protection banners for enhanced security awareness
- Progress indicators during command execution phases

**Command-specific Feedback:**
- /secure-assess: Tool-by-tool protection reporting
- /db-migrate: Database credential masking status
- /deploy: Cloud provider credential protection status

**Security Summary Reporting:**
- End-of-command protection summary with metrics
- Session-level protection tracking
- User security score calculation

**Integration Ready:**
- Functions ready for immediate use in commands
- Real-world examples showing complete protection flow
- Measurable feedback that users can verify

**User Experience:**
- Clear visual indicators when protection is active
- Detailed reporting of what was protected
- Confidence that sensitive data is masked
  </output>
</prompt_component>