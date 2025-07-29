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