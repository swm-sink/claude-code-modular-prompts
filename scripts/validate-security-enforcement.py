#!/usr/bin/env python3
"""
Agent V33: Security Standards Validation Script
Tests threat modeling enforcement and security gate implementation
"""

import json
import os
import re
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Tuple

class SecurityStandardsValidator:
    def __init__(self):
        self.base_path = Path(".")
        self.results = {
            'agent': 'V33',
            'timestamp': datetime.now().isoformat(),
            'security_score': 0,
            'threat_modeling': {
                'enforcement': False,
                'coverage': 0,
                'blocking_verified': False
            },
            'security_gates': {
                'quality_gates': False,
                'command_integration': {},
                'module_coverage': 0
            },
            'security_standards': {
                'secure_coding': False,
                'input_sanitization': False,
                'secrets_management': False,
                'vulnerability_scanning': False
            },
            'findings': [],
            'recommendations': []
        }
    
    def analyze_threat_modeling_enforcement(self):
        """Verify threat modeling is enforced as mandatory gate"""
        print("\n🔍 Analyzing Threat Modeling Enforcement...")
        
        # Check CLAUDE.md for threat modeling requirement
        claude_path = self.base_path / "CLAUDE.md"
        if claude_path.exists():
            with open(claude_path, 'r') as f:
                content = f.read()
                
            # Look for threat modeling in quality gates
            if re.search(r'Security:\s*Threat\s*model\s*first', content, re.IGNORECASE):
                self.results['threat_modeling']['enforcement'] = True
                print("✅ Threat modeling found in quality gates")
            else:
                self.results['findings'].append({
                    'severity': 'HIGH',
                    'issue': 'Threat modeling not enforced in quality gates',
                    'location': 'CLAUDE.md'
                })
        
        # Check threat-modeling.md module
        threat_model_path = self.base_path / ".claude/system/security/threat-modeling.md"
        if threat_model_path.exists():
            with open(threat_model_path, 'r') as f:
                content = f.read()
                
            # Verify STRIDE and DREAD methodologies
            if 'STRIDE' in content and 'DREAD' in content:
                self.results['threat_modeling']['coverage'] += 40
                print("✅ STRIDE and DREAD methodologies implemented")
            
            # Check for blocking enforcement
            if re.search(r'enforcement\s*=\s*["\'](BLOCKING|MANDATORY)', content, re.IGNORECASE):
                self.results['threat_modeling']['blocking_verified'] = True
                self.results['threat_modeling']['coverage'] += 30
                print("✅ Blocking enforcement verified")
        
        # Check integration with commands
        protocol_cmd = self.base_path / ".claude/commands/protocol.md"
        if protocol_cmd.exists():
            with open(protocol_cmd, 'r') as f:
                content = f.read()
                
            if 'threat' in content.lower():
                self.results['threat_modeling']['coverage'] += 30
                print("✅ Threat modeling integrated in /protocol command")
    
    def analyze_security_gates(self):
        """Verify security gates across framework"""
        print("\n🔍 Analyzing Security Gates...")
        
        # Check quality gates integration
        quality_gates_path = self.base_path / ".claude/system/quality/universal-quality-gates.md"
        if quality_gates_path.exists():
            with open(quality_gates_path, 'r') as f:
                content = f.read()
                
            if 'security' in content.lower():
                self.results['security_gates']['quality_gates'] = True
                print("✅ Security integrated in universal quality gates")
        
        # Check command integration
        commands_to_check = ['protocol', 'feature', 'swarm']
        for cmd in commands_to_check:
            cmd_path = self.base_path / f".claude/commands/{cmd}.md"
            if cmd_path.exists():
                with open(cmd_path, 'r') as f:
                    content = f.read()
                    
                security_mentions = len(re.findall(r'security|threat|vulnerability', content, re.IGNORECASE))
                self.results['security_gates']['command_integration'][cmd] = security_mentions > 0
                
                if security_mentions > 0:
                    print(f"✅ Security gates in /{cmd} command ({security_mentions} references)")
                else:
                    self.results['findings'].append({
                        'severity': 'MEDIUM',
                        'issue': f'No security gates in /{cmd} command',
                        'location': f'{cmd}.md'
                    })
    
    def analyze_security_standards(self):
        """Verify security standards implementation"""
        print("\n🔍 Analyzing Security Standards...")
        
        # Check audit module for security scanning
        audit_path = self.base_path / ".claude/system/security/audit.md"
        if audit_path.exists():
            with open(audit_path, 'r') as f:
                content = f.read()
                
            # Check for scanning tools
            if 'bandit' in content or 'semgrep' in content:
                self.results['security_standards']['vulnerability_scanning'] = True
                print("✅ Security scanning tools configured")
            
            # Check for input validation
            if 'input validation' in content.lower():
                self.results['security_standards']['input_sanitization'] = True
                print("✅ Input validation standards found")
            
            # Check for secrets detection
            if 'trufflehog' in content.lower() or 'detect-secrets' in content.lower():
                self.results['security_standards']['secrets_management'] = True
                print("✅ Secrets detection configured")
        
        # Check for secure coding practices
        if self.results['security_standards']['input_sanitization'] and \
           self.results['security_standards']['vulnerability_scanning']:
            self.results['security_standards']['secure_coding'] = True
            print("✅ Secure coding practices implemented")
    
    def calculate_security_score(self):
        """Calculate overall security posture score"""
        score = 0
        
        # Threat modeling enforcement (35 points)
        if self.results['threat_modeling']['enforcement']:
            score += 10
        score += int(self.results['threat_modeling']['coverage'] * 0.25)
        
        # Security gates (30 points)
        if self.results['security_gates']['quality_gates']:
            score += 10
        
        cmd_integration = sum(1 for v in self.results['security_gates']['command_integration'].values() if v)
        score += cmd_integration * 6  # 6 points per command
        
        # Security standards (35 points)
        standards_implemented = sum(1 for v in self.results['security_standards'].values() if v)
        score += standards_implemented * 8  # 8 points per standard
        
        self.results['security_score'] = min(score, 100)
    
    def generate_recommendations(self):
        """Generate security improvement recommendations"""
        if self.results['security_score'] < 90:
            if not self.results['threat_modeling']['blocking_verified']:
                self.results['recommendations'].append(
                    "Implement blocking enforcement for threat modeling in all security-sensitive operations"
                )
            
            missing_cmds = [cmd for cmd, integrated in self.results['security_gates']['command_integration'].items() if not integrated]
            if missing_cmds:
                self.results['recommendations'].append(
                    f"Add security gates to commands: {', '.join(missing_cmds)}"
                )
            
            if not self.results['security_standards']['vulnerability_scanning']:
                self.results['recommendations'].append(
                    "Configure automated vulnerability scanning in CI/CD pipeline"
                )
    
    def run_validation(self):
        """Execute complete security validation"""
        print("=" * 60)
        print("Agent V33: Security Standards Validation")
        print("=" * 60)
        
        self.analyze_threat_modeling_enforcement()
        self.analyze_security_gates()
        self.analyze_security_standards()
        self.calculate_security_score()
        self.generate_recommendations()
        
        # Print summary
        print("\n" + "=" * 60)
        print("SECURITY VALIDATION SUMMARY")
        print("=" * 60)
        print(f"\n🛡️ Security Score: {self.results['security_score']}/100")
        print(f"📋 Threat Modeling Enforcement: {'✅' if self.results['threat_modeling']['enforcement'] else '❌'}")
        print(f"🚪 Security Gates Active: {'✅' if self.results['security_gates']['quality_gates'] else '❌'}")
        print(f"🔐 Vulnerability Scanning: {'✅' if self.results['security_standards']['vulnerability_scanning'] else '❌'}")
        
        if self.results['findings']:
            print(f"\n⚠️ Issues Found: {len(self.results['findings'])}")
            for finding in self.results['findings']:
                print(f"  - [{finding['severity']}] {finding['issue']} in {finding['location']}")
        
        if self.results['recommendations']:
            print(f"\n💡 Recommendations:")
            for rec in self.results['recommendations']:
                print(f"  - {rec}")
        
        # Save results
        output_path = self.base_path / "internal/validation/v33-security-validation.json"
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, 'w') as f:
            json.dump(self.results, f, indent=2)
        
        print(f"\n✅ Validation complete. Results saved to {output_path}")
        
        return self.results['security_score'] >= 85

if __name__ == "__main__":
    validator = SecurityStandardsValidator()
    success = validator.run_validation()
    exit(0 if success else 1)