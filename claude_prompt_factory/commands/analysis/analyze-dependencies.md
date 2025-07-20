# /analyze dependencies - Dependency Analysis Command

## Purpose
Comprehensive dependency analysis to map relationships, identify issues, and optimize project dependencies for security, performance, and maintainability.

## Command Usage
```bash
/analyze dependencies [optional: --scope=package.json|requirements.txt|go.mod|Cargo.toml]
```

## Analysis Scope

### 1. Dependency Mapping
- **Direct Dependencies**: First-level project dependencies
- **Transitive Dependencies**: Complete dependency tree
- **Peer Dependencies**: Required peer packages
- **Development Dependencies**: Build/test-only dependencies

### 2. Security Analysis
- **Vulnerability Scanning**: Known CVEs and security issues
- **License Compliance**: License compatibility checks
- **Supply Chain Risks**: Package maintenance and trust scoring
- **Outdated Packages**: Security patches available

### 3. Circular Dependency Detection
- **Module Cycles**: Internal circular references
- **Package Cycles**: Cross-package circular dependencies
- **Import Analysis**: Static import cycle detection
- **Runtime Dependencies**: Dynamic loading cycles

### 4. Optimization Opportunities
- **Bundle Size**: Package size impact analysis
- **Duplicate Dependencies**: Multiple versions detection
- **Unused Dependencies**: Dead dependency identification
- **Version Conflicts**: Dependency resolution issues

## Framework Output Structure

```
🔍 DEPENDENCY ANALYSIS REPORT

📦 PROJECT DEPENDENCIES:
- Total packages: 127 (production: 89, dev: 38)
- Dependency depth: 4 levels
- Bundle size impact: 2.3MB

🚨 SECURITY FINDINGS:
- High severity: 2 vulnerabilities
- Medium severity: 5 vulnerabilities
- Outdated packages: 12

🔄 CIRCULAR DEPENDENCIES:
- Module cycles detected: 3
- Affected components: auth.service ↔ user.service

⚡ OPTIMIZATION OPPORTUNITIES:
- Unused dependencies: 7 packages
- Duplicate versions: lodash (3.10.1, 4.17.21)
- Bundle size reduction: ~400KB possible

📋 ACTION ITEMS:
1. Update vulnerable packages
2. Resolve circular dependencies
3. Remove unused dependencies
4. Consolidate duplicate versions
```

## Integration Benefits
- **Security Hardening**: Proactive vulnerability management
- **Performance Optimization**: Bundle size and load time improvements  
- **Maintenance Efficiency**: Simplified dependency management
- **Supply Chain Security**: Trusted dependency verification