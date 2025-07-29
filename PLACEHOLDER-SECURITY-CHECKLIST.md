# Placeholder Security Checklist

**Critical Security Protocol for Safe Placeholder Replacement**

## Pre-Replacement Security Setup

### 🔒 Environment Preparation

**Data Protection**
```markdown
□ Create complete backup of .claude/ directory
□ Initialize or commit current state to version control
□ Work in isolated environment (not production)
□ Document all planned replacement values
□ Prepare rollback plan in case of issues
```

**Security Tools Setup**
```markdown
□ Install validation script (if available)
□ Set up secure text editor with find/replace
□ Configure file monitoring for change tracking  
□ Prepare security scanning tools
□ Enable file system snapshots/backups
```

### 🛡️ Value Preparation Security

**Input Value Validation**
```markdown
□ Validate each replacement value against input guidelines
□ Check maximum length limits (100 characters per value)  
□ Verify character whitelist compliance (alphanumeric + -_. only)
□ Scan for dangerous patterns (commands, scripts, HTML)
□ Test values with validation script if available
□ Document validation results for each placeholder
```

**Security Pattern Checking**
```markdown
□ No quotes: ', ", `
□ No command separators: ;, &, |, &&, ||
□ No path traversal: ../, ..\, \\
□ No HTML/script tags: <script>, <iframe>, etc.
□ No system commands: cmd, bash, sh, eval, exec  
□ No variable expansion: ${}, $(), %%, ``
□ No special characters: @, #, $, %, ^, *, +, =
□ No brackets or parens: (), [], {}
```

## During Replacement Security Protocol

### 🔍 File-by-File Security Process

**Before Opening Each File**
```markdown
□ Verify file is in expected location (.claude/commands/)
□ Check file hasn't been tampered with externally
□ Confirm file size is reasonable (not corrupted)
□ Review file last modified timestamp
```

**During Find/Replace Operations**
```markdown
□ Use "Match Case" option to ensure exact matching
□ Review each match before confirming replacement
□ Replace one placeholder type at a time systematically
□ Avoid "Replace All" without reviewing matches first
□ Save file after each placeholder type completion
□ Test file syntax/structure after major changes
```

**After Each File Modification**
```markdown
□ Verify file still has proper markdown structure
□ Check YAML front matter is intact
□ Confirm no unintended text was replaced
□ Search for any remaining [INSERT_ patterns in file
□ Save and close file before moving to next
```

### 🚨 Security Violation Response

**If Dangerous Pattern Detected**
```markdown
□ STOP replacement process immediately
□ Document the dangerous pattern found
□ Revert to backup version of affected file
□ Re-validate the problematic replacement value
□ Update replacement value to safe alternative
□ Re-run validation before attempting replacement again
```

**If Unexpected File Changes Detected**
```markdown
□ Compare current file to backup version
□ Identify all unintended changes
□ Revert file to last known good state
□ Review replacement process for errors
□ Fix process and restart replacement for that file
```

## Post-Replacement Security Verification

### 🔬 Comprehensive Security Audit

**Pattern Verification**
```markdown
□ Search entire .claude/ directory for "[INSERT_" patterns
□ Verify no placeholders remain unreplaced
□ Check for malformed replacement patterns
□ Scan for any doubled or nested replacements
□ Confirm all replacements use expected values
```

**Content Security Scan**
```markdown
□ Scan all modified files for dangerous patterns
□ Check for script injection signatures
□ Verify no command execution patterns introduced
□ Confirm no path traversal patterns exist
□ Validate no HTML/XML injection occurred
□ Check for quote escaping issues
```

**Structural Integrity Check**
```markdown
□ Verify all markdown files have valid syntax
□ Check YAML front matter is properly formatted
□ Confirm code blocks and formatting intact
□ Validate internal links still work
□ Test command structure compliance
```

### 🧪 Functional Security Testing

**Command Execution Safety**
```markdown
□ Test 3-5 sample commands in safe environment
□ Verify commands execute without errors
□ Check command outputs for unexpected content
□ Confirm no system information leakage
□ Validate commands behave as expected
□ Test both simple and complex commands
```

**Context Loading Security**
```markdown
□ Verify Claude Code loads commands correctly
□ Check for any error messages during loading
□ Confirm context files load without issues
□ Test command discovery works properly
□ Validate help system still functions
```

## Security Incident Response

### 🚨 If Security Issue Discovered

**Immediate Response**
```markdown
□ STOP using the affected commands immediately
□ Document the security issue in detail
□ Revert to backup version immediately
□ Identify root cause of security issue
□ Update security procedures to prevent recurrence
```

**Investigation Protocol**
```markdown
□ Review all replacement values for similar issues
□ Check validation process for gaps
□ Scan all files for similar security problems
□ Document lessons learned
□ Update security checklist with new requirements
```

**Remediation Steps**
```markdown
□ Fix all identified security issues
□ Re-validate all replacement values
□ Re-test entire replacement process
□ Update documentation with security fixes
□ Commit secure version to version control
```

## Long-term Security Maintenance

### 🔄 Ongoing Security Practices

**Regular Security Audits**
```markdown
□ Monthly scan for dangerous patterns
□ Quarterly validation of all replacement values
□ Annual review of security procedures
□ Update validation rules based on new threats
□ Monitor for changes to template library
```

**Security Updates**
```markdown
□ Subscribe to security updates for template library
□ Review security advisories for Claude Code
□ Update validation scripts when new threats identified
□ Participate in security discussions with community
□ Report security issues to template maintainers
```

## Emergency Procedures

### 🚨 Security Breach Response

**If Malicious Content Detected**
```
1. IMMEDIATELY stop all command usage
2. Disconnect from network if commands have network access
3. Revert ALL files to last known secure backup
4. Report incident to security team/maintainers
5. Do not attempt to "fix" compromised commands
6. Start replacement process from scratch with enhanced validation
```

**Recovery Checklist**
```markdown
□ Restore from secure backup
□ Re-validate entire security process
□ Test all commands before resuming use
□ Document incident for future prevention
□ Update security procedures based on lessons learned
```

## Validation Tools

### 🛠️ Security Validation Commands

**Pre-replacement Validation**
```bash
# Validate replacement values (if script available)
./scripts/validate_placeholder_inputs.py values.txt

# Check for dangerous patterns in input
grep -E '[\'"`;|&<>]' replacement-values.txt
```

**Post-replacement Security Scan**
```bash
# Check for remaining placeholders
find .claude/ -name "*.md" -exec grep -l "\[INSERT_" {} \;

# Scan for dangerous patterns
find .claude/ -name "*.md" -exec grep -l -E '[\'"`;|&]' {} \;

# Validate file integrity
find .claude/ -name "*.md" -exec head -3 {} \; | grep -E "^name:|^description:"
```

**Emergency Security Scan**
```bash
# Comprehensive security audit
grep -r -E "(cmd|bash|sh|eval|exec)" .claude/
grep -r -E "<script|javascript:|onclick" .claude/
grep -r -E "\.\./|\\\\|%2e%2e" .claude/
```

---

## Security Contact Information

**If Security Issue Discovered:**
1. Stop using affected commands immediately
2. Document issue with screenshots/details
3. Report to template library maintainers
4. Follow emergency procedures above

**Security Updates:**
- Monitor project repository for security advisories
- Subscribe to security notifications if available
- Review this checklist monthly for updates

---

**⚠️ CRITICAL REMINDER**: This security checklist must be followed completely for every placeholder replacement operation. Skipping steps may result in security vulnerabilities.

**Security Level**: Production-grade protection against injection, traversal, and execution attacks

**Last Updated**: 2025-07-29  
**Review Schedule**: Monthly security audit required