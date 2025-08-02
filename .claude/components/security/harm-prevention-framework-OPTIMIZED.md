# Harm Prevention Framework

**Purpose**: Comprehensive AI safety system implementing Constitutional AI principles, input validation, privilege enforcement, and approval workflows for secure Claude Code command execution.

**Usage**: 
- Implement Constitutional AI safety constraints with harm prevention validation
- Enforce least privilege access control and command scope limitations
- Require explicit approval for risky operations (file modifications, system commands)
- Provide comprehensive input sanitization and prompt injection prevention
- Monitor and log all security events with audit trail capabilities

**Compatibility**: 
- **Works with**: prompt-injection-prevention, command-security-wrapper, input-validation-framework, owasp-compliance
- **Requires**: Security policy configuration and approval workflow integration
- **Conflicts**: quick-command (safety complexity exceeds simple command scope)

**Implementation**:
```python
# Comprehensive harm prevention framework
class HarmPreventionFramework:
    def __init__(self):
        self.input_validator = InputValidator()
        self.privilege_enforcer = PrivilegeEnforcer()
        self.approval_manager = ApprovalManager()
        self.security_monitor = SecurityMonitor()
        
    def validate_and_execute(self, command, user_input, context=None):
        # 1. Constitutional AI safety validation
        safety_check = self.validate_constitutional_ai_constraints(command, user_input)
        if not safety_check.is_safe:
            return SecurityViolation(
                type="constitutional_ai_violation",
                reason=safety_check.violation_reason,
                blocked_content=safety_check.flagged_content
            )
        
        # 2. Input sanitization and validation
        sanitized_input = self.input_validator.sanitize_and_validate(user_input)
        if sanitized_input.has_violations:
            return SecurityViolation(
                type="input_validation_failure",
                reason="Dangerous input patterns detected",
                violations=sanitized_input.violations
            )
        
        # 3. Privilege enforcement and scope checking
        privilege_check = self.privilege_enforcer.check_command_privileges(command, context)
        if not privilege_check.is_authorized:
            return SecurityViolation(
                type="privilege_violation",
                reason=privilege_check.denial_reason,
                required_privileges=privilege_check.required_privileges
            )
        
        # 4. Risk assessment and approval workflow
        risk_assessment = self.assess_operation_risk(command, sanitized_input, context)
        if risk_assessment.requires_approval:
            approval_result = self.approval_manager.request_approval(
                operation=command,
                risk_level=risk_assessment.risk_level,
                justification=risk_assessment.risk_explanation
            )
            
            if not approval_result.approved:
                return SecurityViolation(
                    type="approval_required",
                    reason="Operation requires explicit user approval",
                    risk_factors=risk_assessment.risk_factors
                )
        
        # 5. Execute with monitoring
        try:
            self.security_monitor.log_operation_start(command, sanitized_input, risk_assessment)
            
            result = self.execute_with_safety_wrapper(command, sanitized_input, context)
            
            self.security_monitor.log_operation_success(command, result)
            return result
            
        except Exception as e:
            self.security_monitor.log_security_incident(command, sanitized_input, e)
            raise SecurityException(f"Secure execution failed: {e}")
    
    def validate_constitutional_ai_constraints(self, command, user_input):
        violations = []
        
        # Block harmful content categories
        harmful_patterns = [
            ("illegal_activities", self.detect_illegal_activity_requests),
            ("violence", self.detect_violence_content),
            ("harassment", self.detect_harassment_content),
            ("private_info", self.detect_private_info_requests),
            ("misinformation", self.detect_misinformation_creation)
        ]
        
        for category, detector_func in harmful_patterns:
            if detector_func(user_input):
                violations.append(ConstitutionalViolation(
                    category=category,
                    severity="critical",
                    content_sample=user_input[:100]
                ))
        
        return SafetyValidation(
            is_safe=len(violations) == 0,
            violations=violations,
            risk_level=self.calculate_constitutional_risk_level(violations)
        )
    
    def assess_operation_risk(self, command, input_data, context):
        risk_factors = []
        
        # File system risk assessment
        if self.involves_file_operations(command):
            risk_factors.append(RiskFactor(
                type="file_system_access",
                severity="medium",
                description="Command involves file system modifications"
            ))
        
        # System command risk assessment  
        if self.involves_system_commands(command):
            risk_factors.append(RiskFactor(
                type="system_command",
                severity="high", 
                description="Command executes system-level operations"
            ))
        
        # External access risk assessment
        if self.involves_external_access(command):
            risk_factors.append(RiskFactor(
                type="external_access",
                severity="high",
                description="Command accesses external systems or networks"
            ))
        
        # Calculate overall risk level
        overall_risk = self.calculate_overall_risk_level(risk_factors)
        
        return RiskAssessment(
            risk_level=overall_risk,
            risk_factors=risk_factors,
            requires_approval=overall_risk >= RiskLevel.MEDIUM,
            risk_explanation=self.generate_risk_explanation(risk_factors)
        )

# Input validation with prompt injection prevention
class InputValidator:
    def __init__(self):
        self.dangerous_patterns = [
            r"ignore\s+previous\s+instructions",
            r"system\s+prompt",
            r"override\s+safety",
            r"jailbreak",
            r"roleplay\s+as",
            r"rm\s+-rf",
            r"sudo\s+",
            r"chmod\s+777",
            r"curl.*\|.*wget"
        ]
        
    def sanitize_and_validate(self, user_input):
        violations = []
        
        # Length validation
        if len(user_input) > 1000:
            violations.append(ValidationViolation(
                type="excessive_length",
                severity="medium",
                description="Input exceeds maximum allowed length"
            ))
        
        # Pattern matching for dangerous content
        for pattern in self.dangerous_patterns:
            if re.search(pattern, user_input, re.IGNORECASE):
                violations.append(ValidationViolation(
                    type="dangerous_pattern",
                    severity="high",
                    pattern=pattern,
                    description=f"Input contains potentially dangerous pattern: {pattern}"
                ))
        
        # Character validation
        allowed_chars = re.compile(r'^[a-zA-Z0-9\s\-_/\.]+$')
        if not allowed_chars.match(user_input):
            violations.append(ValidationViolation(
                type="invalid_characters",
                severity="medium", 
                description="Input contains characters outside allowed set"
            ))
        
        return ValidationResult(
            sanitized_input=self.sanitize_input(user_input),
            has_violations=len(violations) > 0,
            violations=violations
        )

# Privilege enforcement system
class PrivilegeEnforcer:
    def __init__(self):
        self.allowed_directories = {'.claude/', 'tests/', 'docs/', 'src/'}
        self.blocked_directories = {'/etc/', '/bin/', '/usr/', '~/.ssh/'}
        self.operation_limits = {
            'max_file_operations': 10,
            'max_bash_commands': 3,
            'max_external_requests': 2
        }
        
    def check_command_privileges(self, command, context):
        authorization_checks = []
        
        # Directory access validation
        if self.accesses_blocked_directory(command):
            authorization_checks.append(AuthorizationFailure(
                type="directory_access_denied",
                reason="Command attempts to access restricted directory",
                required_privilege="admin_directory_access"
            ))
        
        # Operation limit validation
        limits_exceeded = self.check_operation_limits(command, context)
        if limits_exceeded:
            authorization_checks.append(AuthorizationFailure(
                type="operation_limits_exceeded",
                reason="Command exceeds allowed operation limits",
                limits_exceeded=limits_exceeded
            ))
        
        return AuthorizationResult(
            is_authorized=len(authorization_checks) == 0,
            authorization_failures=authorization_checks
        )
```

**Category**: security | **Complexity**: high | **Time**: 1 hour