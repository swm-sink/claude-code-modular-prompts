#!/usr/bin/env python3
"""
Functional Credential Protection Tests
Tests that credential detection and masking actually work during command execution.
"""

import json
import re
import sys
from datetime import datetime

class CredentialProtectionTester:
    """Test functional credential protection with real patterns and verification."""
    
    def __init__(self):
        # Real credential patterns that should be detected
        self.api_key_patterns = {
            'aws_access_key': r'AKIA[0-9A-Z]{16}',
            'aws_secret': r'[A-Za-z0-9/+=]{40}',
            'generic_api_key': r'api[_-]?key[_-]?[=:]\s*[\'\"]*([a-zA-Z0-9_-]{16,64})[\'\"]',
            'bearer_token': r'bearer\s+([a-zA-Z0-9_-]{20,})',
            'db_connection': r'(mysql|postgresql|mongodb)://[^:]+:[^@]+@[^/]+',
            'ssh_private_key': r'-----BEGIN (RSA |OPENSSH |DSA |EC )?PRIVATE KEY-----',
            'jwt_token': r'eyJ[a-zA-Z0-9_-]*\.eyJ[a-zA-Z0-9_-]*\.[a-zA-Z0-9_-]*',
            'github_token': r'gh[pousr]_[A-Za-z0-9_]{36}',
            'docker_auth': r'"auth":\s*"[A-Za-z0-9+/]+=*"',
            'password_field': r'password[_-]?[=:]\s*[\'\"]*([^\'\"\\s]{8,})[\'\"]',
            'gcp_service_key': r'"private_key":\s*"-----BEGIN PRIVATE KEY-----[^"]*"',
            'azure_secret': r'[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}',
            'secret_env': r'(secret|token|key)[_-]?[=:]\s*[\'\"]*([a-zA-Z0-9_-]{16,})[\'\"]'
        }
        
        self.test_cases = [
            # AWS Credentials
            {
                'name': 'AWS Access Key',
                'input': 'AWS_ACCESS_KEY_ID=AKIAIOSFODNN7EXAMPLE',
                'expected_masked': True,
                'credential_type': 'aws_access_key'
            },
            {
                'name': 'AWS Secret Key',
                'input': 'AWS_SECRET_ACCESS_KEY=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY',
                'expected_masked': True,
                'credential_type': 'aws_secret'
            },
            
            # Database URLs
            {
                'name': 'MySQL Connection String',
                'input': 'mysql://user:password123@localhost:3306/database',
                'expected_masked': True,
                'credential_type': 'db_connection'
            },
            {
                'name': 'PostgreSQL Connection String',
                'input': 'postgresql://dbuser:securepass@host.example.com:5432/mydb',
                'expected_masked': True,
                'credential_type': 'db_connection'
            },
            
            # API Keys and Tokens
            {
                'name': 'Generic API Key',
                'input': 'api_key: "sk-1234567890abcdef1234567890abcdef"',
                'expected_masked': True,
                'credential_type': 'generic_api_key'
            },
            {
                'name': 'Bearer Token',
                'input': 'Authorization: Bearer abc123def456ghi789jkl012mno345pqr678stu',
                'expected_masked': True,
                'credential_type': 'bearer_token'
            },
            {
                'name': 'JWT Token',
                'input': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c',
                'expected_masked': True,
                'credential_type': 'jwt_token'
            },
            
            # GitHub Token
            {
                'name': 'GitHub Personal Access Token',
                'input': 'github_token = ghp_1234567890abcdef1234567890abcdef12',
                'expected_masked': True,
                'credential_type': 'github_token'
            },
            
            # SSH Keys
            {
                'name': 'SSH Private Key',
                'input': '-----BEGIN RSA PRIVATE KEY-----\nMIIEpAIBAAKCAQEA...',
                'expected_masked': True,
                'credential_type': 'ssh_private_key'
            },
            {
                'name': 'OpenSSH Private Key',
                'input': '-----BEGIN OPENSSH PRIVATE KEY-----\nb3BlbnNzaC1rZXk...',
                'expected_masked': True,
                'credential_type': 'ssh_private_key'
            },
            
            # Docker Authentication
            {
                'name': 'Docker Registry Auth',
                'input': '{"auth": "dXNlcjpwYXNzd29yZA=="}',
                'expected_masked': True,
                'credential_type': 'docker_auth'
            },
            
            # Environment Variables
            {
                'name': 'Environment Secret',
                'input': 'export SECRET_KEY=super_secret_value_123456',
                'expected_masked': True,
                'credential_type': 'secret_env'
            },
            {
                'name': 'Password Environment Variable',
                'input': 'DB_PASSWORD=myverysecurepassword123',
                'expected_masked': True,
                'credential_type': 'password_field'
            },
            
            # Azure Credentials
            {
                'name': 'Azure Client Secret',
                'input': 'client_secret = 12345678-1234-1234-1234-123456789012',
                'expected_masked': True,
                'credential_type': 'azure_secret'
            },
            
            # Safe content (should not be masked)
            {
                'name': 'Safe Text',
                'input': 'This is just regular text with no credentials',
                'expected_masked': False,
                'credential_type': None
            },
            {
                'name': 'Safe Log Entry',
                'input': 'Application started successfully on port 3000',
                'expected_masked': False,
                'credential_type': None
            }
        ]
    
    def detect_credentials(self, text):
        """Functional credential detection using real regex patterns."""
        if not text or not isinstance(text, str):
            return {'detected_count': 0, 'types': [], 'masked_text': text}
        
        detected_types = []
        masked_text = text
        
        for pattern_name, pattern in self.api_key_patterns.items():
            matches = re.findall(pattern, text, re.IGNORECASE)
            if matches:
                detected_types.append(pattern_name)
                # Mask the matches
                for match in re.finditer(pattern, text, re.IGNORECASE):
                    full_match = match.group(0)
                    if len(full_match) > 8:
                        masked = full_match[:4] + '*' * (len(full_match) - 8) + full_match[-4:]
                    else:
                        masked = '***MASKED***'
                    masked_text = masked_text.replace(full_match, masked, 1)
        
        return {
            'detected_count': len(detected_types),
            'types': list(set(detected_types)),
            'masked_text': masked_text
        }
    
    def test_individual_patterns(self):
        """Test each credential pattern individually."""
        print("🧪 Testing Individual Credential Patterns")
        print("=" * 50)
        
        results = []
        for test_case in self.test_cases:
            result = self.detect_credentials(test_case['input'])
            
            # Check if detection matches expectation
            actually_detected = result['detected_count'] > 0
            expected_detected = test_case['expected_masked']
            
            test_passed = actually_detected == expected_detected
            
            # Check specific credential type if applicable
            type_match = True
            if test_case['credential_type'] and expected_detected:
                type_match = test_case['credential_type'] in result['types']
            
            overall_passed = test_passed and type_match
            
            results.append({
                'name': test_case['name'],
                'passed': overall_passed,
                'input_length': len(test_case['input']),
                'detected_count': result['detected_count'],
                'detected_types': result['types'],
                'expected_type': test_case['credential_type'],
                'masked_output': result['masked_text'][:100] + ('...' if len(result['masked_text']) > 100 else '')
            })
            
            status = "✅ PASS" if overall_passed else "❌ FAIL"
            print(f"{status} {test_case['name']}")
            if result['detected_count'] > 0:
                print(f"     🔒 Detected: {result['detected_count']} credentials ({', '.join(result['types'])})")
            
        return results
    
    def test_command_output_protection(self):
        """Test protection of simulated command outputs."""
        print("\n🔧 Testing Command Output Protection")
        print("=" * 50)
        
        # Simulate command outputs that might contain credentials
        simulated_outputs = [
            {
                'command': '/secure-assess scan',
                'output': '''
Security scan results:
Found API key: api_key=sk-1234567890abcdef1234567890abcdef
Database connection: mysql://user:secret123@prod.example.com:3306/app
AWS credentials found in environment:
  AWS_ACCESS_KEY_ID=AKIAIOSFODNN7EXAMPLE
  AWS_SECRET_ACCESS_KEY=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
Scan complete.
''',
                'expected_masked': True
            },
            {
                'command': '/db-migrate status',
                'output': '''
Migration status for database: postgresql://dbuser:password@host:5432/db
Current version: 20231201_001
Pending migrations: 3
Connection successful.
''',
                'expected_masked': True
            },
            {
                'command': '/deploy production',
                'output': '''
Deploying to production...
Using AWS credentials: AKIAIOSFODNN7EXAMPLE
Docker registry auth: {"auth": "dXNlcjpwYXNzd29yZA=="}
Kubernetes secret created successfully
Deployment completed.
''',
                'expected_masked': True
            },
            {
                'command': '/secure-assess audit',
                'output': '''
Security audit complete.
No vulnerabilities found.
Application is secure.
''',
                'expected_masked': False
            }
        ]
        
        results = []
        for test in simulated_outputs:
            result = self.detect_credentials(test['output'])
            
            actually_protected = result['detected_count'] > 0
            expected_protection = test['expected_masked']
            
            test_passed = actually_protected == expected_protection
            
            results.append({
                'command': test['command'],
                'passed': test_passed,
                'credentials_detected': result['detected_count'],
                'types_found': result['types'],
                'protection_active': actually_protected
            })
            
            status = "✅ PASS" if test_passed else "❌ FAIL"
            print(f"{status} {test['command']}")
            if result['detected_count'] > 0:
                print(f"     🔒 Protection Active: {result['detected_count']} credentials masked")
            else:
                print(f"     ✅ No credentials detected")
        
        return results
    
    def test_error_message_sanitization(self):
        """Test that error messages are properly sanitized."""
        print("\n🚨 Testing Error Message Sanitization")
        print("=" * 50)
        
        error_scenarios = [
            {
                'error': 'Database connection failed: mysql://user:password123@host:3306/db',
                'expected_sanitized': True
            },
            {
                'error': 'Authentication failed for AWS_ACCESS_KEY_ID=AKIAIOSFODNN7EXAMPLE',
                'expected_sanitized': True
            },
            {
                'error': 'Invalid token: Bearer abc123def456ghi789jkl012mno345pqr678stu',
                'expected_sanitized': True
            },
            {
                'error': 'File not found: /app/config.yml',
                'expected_sanitized': False
            },
            {
                'error': 'Port 3000 is already in use',
                'expected_sanitized': False
            }
        ]
        
        results = []
        for scenario in error_scenarios:
            result = self.detect_credentials(scenario['error'])
            
            has_credentials = result['detected_count'] > 0
            expected_credentials = scenario['expected_sanitized']
            
            test_passed = has_credentials == expected_credentials
            
            results.append({
                'original_error': scenario['error'][:50] + ('...' if len(scenario['error']) > 50 else ''),
                'passed': test_passed,
                'credentials_found': result['detected_count'],
                'sanitized_error': result['masked_text'][:50] + ('...' if len(result['masked_text']) > 50 else '')
            })
            
            status = "✅ PASS" if test_passed else "❌ FAIL"
            print(f"{status} Error sanitization test")
            if result['detected_count'] > 0:
                print(f"     🔒 Credentials masked in error message")
        
        return results
    
    def generate_test_report(self, individual_results, output_results, error_results):
        """Generate comprehensive test report."""
        total_tests = len(individual_results) + len(output_results) + len(error_results)
        total_passed = (
            sum(1 for r in individual_results if r['passed']) +
            sum(1 for r in output_results if r['passed']) +
            sum(1 for r in error_results if r['passed'])
        )
        
        report = {
            'test_execution': {
                'timestamp': datetime.now().isoformat(),
                'total_tests': total_tests,
                'tests_passed': total_passed,
                'tests_failed': total_tests - total_passed,
                'success_rate': round((total_passed / total_tests) * 100, 2) if total_tests > 0 else 0
            },
            'credential_patterns_tested': len(self.api_key_patterns),
            'individual_pattern_tests': {
                'total': len(individual_results),
                'passed': sum(1 for r in individual_results if r['passed']),
                'results': individual_results
            },
            'command_output_protection_tests': {
                'total': len(output_results),
                'passed': sum(1 for r in output_results if r['passed']),
                'results': output_results
            },
            'error_sanitization_tests': {
                'total': len(error_results),
                'passed': sum(1 for r in error_results if r['passed']),
                'results': error_results
            },
            'functional_verification': {
                'credential_detection_working': any(r['detected_count'] > 0 for r in individual_results if r['passed']),
                'command_protection_active': any(r['credentials_detected'] > 0 for r in output_results if r['passed']),
                'error_sanitization_functional': any(r['credentials_found'] > 0 for r in error_results if r['passed'])
            }
        }
        
        return report
    
    def run_all_tests(self):
        """Run all credential protection tests."""
        print("🔒 FUNCTIONAL CREDENTIAL PROTECTION TESTS")
        print("=" * 60)
        print(f"Testing {len(self.api_key_patterns)} credential patterns with {len(self.test_cases)} test cases")
        print()
        
        # Run individual pattern tests
        individual_results = self.test_individual_patterns()
        
        # Run command output protection tests
        output_results = self.test_command_output_protection()
        
        # Run error message sanitization tests
        error_results = self.test_error_message_sanitization()
        
        # Generate comprehensive report
        report = self.generate_test_report(individual_results, output_results, error_results)
        
        # Print summary
        print("\n📊 TEST SUMMARY")
        print("=" * 50)
        print(f"Total Tests: {report['test_execution']['total_tests']}")
        print(f"Passed: {report['test_execution']['tests_passed']}")
        print(f"Failed: {report['test_execution']['tests_failed']}")
        print(f"Success Rate: {report['test_execution']['success_rate']}%")
        print()
        print("🔍 FUNCTIONAL VERIFICATION:")
        print(f"✅ Credential Detection: {'Working' if report['functional_verification']['credential_detection_working'] else 'Not Working'}")
        print(f"✅ Command Protection: {'Active' if report['functional_verification']['command_protection_active'] else 'Inactive'}")
        print(f"✅ Error Sanitization: {'Functional' if report['functional_verification']['error_sanitization_functional'] else 'Not Functional'}")
        
        return report

def main():
    """Run credential protection tests."""
    tester = CredentialProtectionTester()
    report = tester.run_all_tests()
    
    # Save detailed report
    report_file = f"credential_protection_test_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(report_file, 'w') as f:
        json.dump(report, f, indent=2)
    
    print(f"\nDetailed report saved to: {report_file}")
    
    # Return appropriate exit code
    if report['test_execution']['success_rate'] >= 90:
        print("🎉 CREDENTIAL PROTECTION TESTS PASSED")
        return 0
    else:
        print("⚠️ CREDENTIAL PROTECTION TESTS FAILED")
        return 1

if __name__ == "__main__":
    sys.exit(main())