# Package Security Validation (I19)

| version | last_updated | status | agent |
|---------|--------------|---------|-------|
| 1.0.0   | 2025-07-20   | active | I19 |

## Purpose
Comprehensive package security validation system that integrates vulnerability scanning, license compliance checking, supply chain validation, and security scoring to ensure safe package usage in code generation and development workflows.

## Core Security Validation Framework

### Vulnerability Scanning Integration

```python
class VulnerabilityScanner:
    def __init__(self):
        self.vulnerability_databases = {
            "osv": OSVDatabase("https://osv.dev/v1/"),
            "snyk": SnykDatabase(api_key=os.getenv("SNYK_API_KEY")),
            "github": GitHubAdvisoryDatabase(),
            "npm_audit": NPMAuditDatabase(),
            "safety": SafetyDatabase(),
            "cargo_audit": CargoAuditDatabase()
        }
        
        self.severity_levels = {
            "critical": {"score": 10, "threshold": 9.0},
            "high": {"score": 8, "threshold": 7.0},
            "medium": {"score": 5, "threshold": 4.0},
            "low": {"score": 2, "threshold": 1.0},
            "info": {"score": 1, "threshold": 0.0}
        }
        
        self.scan_cache = TTLCache(maxsize=10000, ttl=3600)  # 1 hour cache
    
    def scan_package_vulnerabilities(self, package_name: str, version: str, 
                                   language: str) -> VulnerabilityReport:
        """Comprehensive vulnerability scan across multiple databases"""
        cache_key = f"{language}:{package_name}:{version}"
        
        if cache_key in self.scan_cache:
            return self.scan_cache[cache_key]
        
        vulnerabilities = []
        scan_sources = self._get_scan_sources_for_language(language)
        
        for source_name in scan_sources:
            source = self.vulnerability_databases[source_name]
            try:
                source_vulns = source.scan_package(package_name, version)
                for vuln in source_vulns:
                    vuln.source = source_name
                    vulnerabilities.append(vuln)
            except Exception as e:
                logging.warning(f"Vulnerability scan failed for {source_name}: {e}")
        
        # Deduplicate vulnerabilities by CVE ID
        unique_vulns = self._deduplicate_vulnerabilities(vulnerabilities)
        
        # Calculate overall security score
        security_score = self._calculate_security_score(unique_vulns)
        
        report = VulnerabilityReport(
            package_name=package_name,
            version=version,
            language=language,
            vulnerabilities=unique_vulns,
            security_score=security_score,
            scan_timestamp=datetime.now(),
            recommendation=self._generate_security_recommendation(unique_vulns, security_score)
        )
        
        self.scan_cache[cache_key] = report
        return report
    
    def _get_scan_sources_for_language(self, language: str) -> List[str]:
        """Get appropriate vulnerability sources for language"""
        language_sources = {
            "python": ["osv", "safety", "snyk"],
            "javascript": ["osv", "npm_audit", "snyk", "github"],
            "go": ["osv", "snyk", "github"],
            "rust": ["osv", "cargo_audit", "github"],
            "java": ["osv", "snyk", "github"],
            "php": ["osv", "snyk"],
            "ruby": ["osv", "github", "snyk"],
            "c_sharp": ["osv", "snyk", "github"]
        }
        
        return language_sources.get(language, ["osv", "snyk"])
    
    def _calculate_security_score(self, vulnerabilities: List[Vulnerability]) -> float:
        """Calculate overall security score (0-10, higher is more secure)"""
        if not vulnerabilities:
            return 10.0
        
        total_impact = 0
        for vuln in vulnerabilities:
            severity_impact = self.severity_levels[vuln.severity]["score"]
            
            # Apply recency penalty (recent vulns are more concerning)
            days_old = (datetime.now() - vuln.published_date).days
            recency_multiplier = max(0.5, 1.0 - (days_old / 365))  # Full impact for recent, 50% for old
            
            # Apply patch availability bonus
            patch_multiplier = 0.7 if vuln.has_fix else 1.0
            
            total_impact += severity_impact * recency_multiplier * patch_multiplier
        
        # Normalize to 0-10 scale
        max_possible_impact = len(vulnerabilities) * 10
        security_score = max(0, 10 - (total_impact / max_possible_impact * 10))
        
        return round(security_score, 2)
    
    def scan_dependency_tree(self, dependency_tree: DependencyTree) -> TreeScanResult:
        """Scan entire dependency tree for vulnerabilities"""
        scan_results = {}
        critical_paths = []
        
        for package in dependency_tree.get_all_packages():
            scan_result = self.scan_package_vulnerabilities(
                package.name, package.version, package.language
            )
            scan_results[f"{package.name}@{package.version}"] = scan_result
            
            # Track critical vulnerability paths
            if scan_result.has_critical_vulnerabilities():
                critical_paths.append(dependency_tree.get_path_to_package(package))
        
        return TreeScanResult(
            total_packages=len(scan_results),
            vulnerable_packages=len([r for r in scan_results.values() if r.vulnerabilities]),
            critical_vulnerabilities=sum(len([v for v in r.vulnerabilities if v.severity == "critical"]) 
                                       for r in scan_results.values()),
            overall_score=self._calculate_tree_security_score(scan_results),
            critical_paths=critical_paths,
            detailed_results=scan_results
        )
```

### License Compliance Checking

```python
class LicenseComplianceChecker:
    def __init__(self):
        self.license_database = LicenseDatabase()
        self.compatibility_matrix = self._load_license_compatibility_matrix()
        self.policy_engine = LicensePolicyEngine()
        
        # Standard license categories
        self.license_categories = {
            "permissive": ["MIT", "BSD-2-Clause", "BSD-3-Clause", "Apache-2.0", "ISC"],
            "copyleft_weak": ["LGPL-2.1", "LGPL-3.0", "MPL-2.0"],
            "copyleft_strong": ["GPL-2.0", "GPL-3.0", "AGPL-3.0"],
            "proprietary": ["Commercial", "Proprietary"],
            "public_domain": ["Unlicense", "CC0-1.0"],
            "unknown": ["UNKNOWN", "NOASSERTION", ""]
        }
    
    def check_package_license(self, package_name: str, version: str, 
                            language: str) -> LicenseReport:
        """Check package license compliance"""
        # Get license information from package metadata
        license_info = self._extract_license_info(package_name, version, language)
        
        if not license_info:
            return LicenseReport(
                package_name=package_name,
                version=version,
                license="UNKNOWN",
                category="unknown",
                compliance_status="requires_review",
                risk_level="medium",
                issues=["License information not available"]
            )
        
        # Normalize license identifier
        normalized_license = self._normalize_license_identifier(license_info.identifier)
        
        # Categorize license
        category = self._categorize_license(normalized_license)
        
        # Check against policy
        policy_result = self.policy_engine.evaluate_license(normalized_license, category)
        
        # Identify potential issues
        issues = self._identify_license_issues(normalized_license, license_info)
        
        return LicenseReport(
            package_name=package_name,
            version=version,
            license=normalized_license,
            category=category,
            compliance_status=policy_result.status,
            risk_level=policy_result.risk_level,
            issues=issues,
            obligations=self._get_license_obligations(normalized_license),
            attribution_required=self._requires_attribution(normalized_license)
        )
    
    def check_license_compatibility(self, licenses: List[str], 
                                  project_license: str) -> CompatibilityReport:
        """Check compatibility between multiple licenses"""
        compatibility_issues = []
        
        for license_id in licenses:
            compatibility = self._check_license_pair_compatibility(project_license, license_id)
            if not compatibility.compatible:
                compatibility_issues.append(CompatibilityIssue(
                    project_license=project_license,
                    dependency_license=license_id,
                    conflict_type=compatibility.conflict_type,
                    severity=compatibility.severity,
                    resolution_options=compatibility.resolution_options
                ))
        
        overall_compatible = len(compatibility_issues) == 0
        
        return CompatibilityReport(
            project_license=project_license,
            dependency_licenses=licenses,
            compatible=overall_compatible,
            issues=compatibility_issues,
            recommendations=self._generate_compatibility_recommendations(compatibility_issues)
        )
    
    def _load_license_compatibility_matrix(self) -> Dict[Tuple[str, str], CompatibilityResult]:
        """Load license compatibility matrix"""
        # Simplified compatibility matrix
        # In production, this would be loaded from a comprehensive database
        matrix = {}
        
        # Permissive licenses are generally compatible with everything
        permissive = self.license_categories["permissive"]
        for p1 in permissive:
            for p2 in permissive + self.license_categories["copyleft_weak"] + self.license_categories["copyleft_strong"]:
                matrix[(p1, p2)] = CompatibilityResult(compatible=True, reason="Permissive license")
        
        # GPL compatibility rules
        gpl_licenses = ["GPL-2.0", "GPL-3.0"]
        for gpl in gpl_licenses:
            # GPL is incompatible with many other licenses
            matrix[(gpl, "Apache-2.0")] = CompatibilityResult(
                compatible=False, 
                conflict_type="patent_clause_conflict",
                severity="high"
            )
            matrix[("Apache-2.0", gpl)] = matrix[(gpl, "Apache-2.0")]
        
        return matrix
    
    def generate_license_summary(self, dependency_tree: DependencyTree) -> LicenseSummary:
        """Generate comprehensive license summary for project"""
        license_reports = {}
        license_distribution = {}
        compliance_issues = []
        
        for package in dependency_tree.get_all_packages():
            report = self.check_package_license(package.name, package.version, package.language)
            license_reports[f"{package.name}@{package.version}"] = report
            
            # Count license distribution
            license_key = report.license
            license_distribution[license_key] = license_distribution.get(license_key, 0) + 1
            
            # Collect compliance issues
            if report.compliance_status != "approved":
                compliance_issues.append(report)
        
        return LicenseSummary(
            total_packages=len(license_reports),
            license_distribution=license_distribution,
            compliance_issues=compliance_issues,
            requires_attribution=len([r for r in license_reports.values() if r.attribution_required]),
            unknown_licenses=len([r for r in license_reports.values() if r.license == "UNKNOWN"]),
            detailed_reports=license_reports
        )
```

### Supply Chain Validation

```python
class SupplyChainValidator:
    def __init__(self):
        self.reputation_checker = PackageReputationChecker()
        self.integrity_verifier = PackageIntegrityVerifier()
        self.maintainer_analyzer = MaintainerAnalyzer()
        self.typosquatting_detector = TyposquattingDetector()
        
    def validate_package_supply_chain(self, package_name: str, version: str, 
                                    language: str) -> SupplyChainReport:
        """Comprehensive supply chain validation"""
        
        # Check package reputation
        reputation_score = self.reputation_checker.analyze_package_reputation(
            package_name, language
        )
        
        # Verify package integrity
        integrity_result = self.integrity_verifier.verify_package_integrity(
            package_name, version, language
        )
        
        # Analyze maintainers
        maintainer_analysis = self.maintainer_analyzer.analyze_maintainers(
            package_name, language
        )
        
        # Check for typosquatting
        typosquatting_risk = self.typosquatting_detector.assess_typosquatting_risk(
            package_name, language
        )
        
        # Calculate overall supply chain score
        supply_chain_score = self._calculate_supply_chain_score(
            reputation_score, integrity_result, maintainer_analysis, typosquatting_risk
        )
        
        return SupplyChainReport(
            package_name=package_name,
            version=version,
            language=language,
            reputation_score=reputation_score,
            integrity_verified=integrity_result.verified,
            maintainer_trust_score=maintainer_analysis.trust_score,
            typosquatting_risk=typosquatting_risk.risk_level,
            supply_chain_score=supply_chain_score,
            recommendations=self._generate_supply_chain_recommendations(
                reputation_score, integrity_result, maintainer_analysis, typosquatting_risk
            )
        )
    
    def _calculate_supply_chain_score(self, reputation: ReputationScore, 
                                    integrity: IntegrityResult,
                                    maintainer: MaintainerAnalysis,
                                    typosquatting: TyposquattingRisk) -> float:
        """Calculate weighted supply chain security score"""
        weights = {
            "reputation": 0.3,
            "integrity": 0.25,
            "maintainer": 0.25,
            "typosquatting": 0.2
        }
        
        scores = {
            "reputation": reputation.overall_score,
            "integrity": 10.0 if integrity.verified else 0.0,
            "maintainer": maintainer.trust_score,
            "typosquatting": 10.0 - typosquatting.risk_score
        }
        
        weighted_score = sum(scores[factor] * weights[factor] for factor in weights)
        return round(weighted_score, 2)

class PackageReputationChecker:
    def __init__(self):
        self.metrics_weights = {
            "download_count": 0.25,
            "github_stars": 0.20,
            "community_adoption": 0.20,
            "maintenance_activity": 0.15,
            "age_stability": 0.10,
            "documentation_quality": 0.10
        }
    
    def analyze_package_reputation(self, package_name: str, language: str) -> ReputationScore:
        """Analyze package reputation across multiple metrics"""
        
        metrics = {}
        
        # Download/usage metrics
        metrics["download_count"] = self._get_download_metrics(package_name, language)
        
        # GitHub metrics (if available)
        github_data = self._get_github_metrics(package_name, language)
        metrics["github_stars"] = github_data.get("stars", 0)
        metrics["github_forks"] = github_data.get("forks", 0)
        metrics["github_issues"] = github_data.get("open_issues", 0)
        
        # Community adoption
        metrics["community_adoption"] = self._assess_community_adoption(package_name, language)
        
        # Maintenance activity
        metrics["maintenance_activity"] = self._assess_maintenance_activity(package_name, language)
        
        # Package age and stability
        metrics["age_stability"] = self._assess_age_stability(package_name, language)
        
        # Documentation quality
        metrics["documentation_quality"] = self._assess_documentation_quality(package_name, language)
        
        # Calculate weighted score
        overall_score = self._calculate_weighted_reputation_score(metrics)
        
        return ReputationScore(
            package_name=package_name,
            language=language,
            overall_score=overall_score,
            metrics=metrics,
            recommendation=self._generate_reputation_recommendation(overall_score, metrics)
        )

class TyposquattingDetector:
    def __init__(self):
        self.popular_packages = self._load_popular_packages()
        self.similarity_threshold = 0.8
        
    def assess_typosquatting_risk(self, package_name: str, language: str) -> TyposquattingRisk:
        """Assess risk of package being a typosquatting attack"""
        
        if language not in self.popular_packages:
            return TyposquattingRisk(risk_level="unknown", risk_score=5.0)
        
        popular_names = self.popular_packages[language]
        
        # Check for suspicious similarities
        suspicious_matches = []
        for popular_name in popular_names:
            similarity = self._calculate_similarity(package_name, popular_name)
            if 0.7 <= similarity < 1.0:  # Suspiciously similar but not identical
                suspicious_matches.append({
                    "target": popular_name,
                    "similarity": similarity,
                    "edit_distance": self._edit_distance(package_name, popular_name)
                })
        
        # Assess risk level
        if not suspicious_matches:
            risk_level = "low"
            risk_score = 1.0
        elif len(suspicious_matches) == 1 and suspicious_matches[0]["similarity"] < 0.85:
            risk_level = "medium"
            risk_score = 5.0
        else:
            risk_level = "high"
            risk_score = 8.0
        
        return TyposquattingRisk(
            package_name=package_name,
            language=language,
            risk_level=risk_level,
            risk_score=risk_score,
            suspicious_matches=suspicious_matches
        )
```

### Security Scoring System

```python
class SecurityScoringSystem:
    def __init__(self):
        self.score_weights = {
            "vulnerability_score": 0.35,
            "license_compliance": 0.20,
            "supply_chain_score": 0.25,
            "maintenance_score": 0.20
        }
        
        self.risk_thresholds = {
            "critical": (0.0, 3.0),
            "high": (3.0, 5.0),
            "medium": (5.0, 7.0),
            "low": (7.0, 9.0),
            "minimal": (9.0, 10.0)
        }
    
    def calculate_package_security_score(self, package_name: str, version: str, 
                                       language: str) -> SecurityScore:
        """Calculate comprehensive security score for package"""
        
        # Get component scores
        vulnerability_report = self.vulnerability_scanner.scan_package_vulnerabilities(
            package_name, version, language
        )
        
        license_report = self.license_checker.check_package_license(
            package_name, version, language
        )
        
        supply_chain_report = self.supply_chain_validator.validate_package_supply_chain(
            package_name, version, language
        )
        
        maintenance_score = self._calculate_maintenance_score(package_name, language)
        
        # Calculate weighted overall score
        component_scores = {
            "vulnerability_score": vulnerability_report.security_score,
            "license_compliance": self._convert_license_compliance_to_score(license_report),
            "supply_chain_score": supply_chain_report.supply_chain_score,
            "maintenance_score": maintenance_score
        }
        
        overall_score = sum(
            component_scores[component] * self.score_weights[component]
            for component in component_scores
        )
        
        # Determine risk level
        risk_level = self._determine_risk_level(overall_score)
        
        # Generate recommendations
        recommendations = self._generate_security_recommendations(
            vulnerability_report, license_report, supply_chain_report, component_scores
        )
        
        return SecurityScore(
            package_name=package_name,
            version=version,
            language=language,
            overall_score=round(overall_score, 2),
            risk_level=risk_level,
            component_scores=component_scores,
            recommendations=recommendations,
            detailed_reports={
                "vulnerabilities": vulnerability_report,
                "license": license_report,
                "supply_chain": supply_chain_report
            }
        )
    
    def batch_security_assessment(self, packages: List[PackageSpec]) -> BatchSecurityReport:
        """Perform security assessment on multiple packages"""
        security_scores = []
        high_risk_packages = []
        critical_issues = []
        
        # Process packages in parallel for efficiency
        with ThreadPoolExecutor(max_workers=10) as executor:
            future_to_package = {
                executor.submit(
                    self.calculate_package_security_score,
                    pkg.name, pkg.version, pkg.language
                ): pkg for pkg in packages
            }
            
            for future in as_completed(future_to_package):
                package = future_to_package[future]
                try:
                    score = future.result()
                    security_scores.append(score)
                    
                    if score.risk_level in ["critical", "high"]:
                        high_risk_packages.append(score)
                    
                    # Collect critical issues
                    if score.detailed_reports["vulnerabilities"].vulnerabilities:
                        critical_vulns = [
                            v for v in score.detailed_reports["vulnerabilities"].vulnerabilities
                            if v.severity == "critical"
                        ]
                        critical_issues.extend(critical_vulns)
                        
                except Exception as e:
                    logging.error(f"Security assessment failed for {package.name}: {e}")
        
        return BatchSecurityReport(
            total_packages=len(packages),
            assessed_packages=len(security_scores),
            high_risk_count=len(high_risk_packages),
            critical_vulnerabilities=len(critical_issues),
            average_score=sum(s.overall_score for s in security_scores) / len(security_scores),
            security_distribution=self._calculate_risk_distribution(security_scores),
            detailed_scores=security_scores,
            prioritized_actions=self._prioritize_security_actions(security_scores)
        )
```

## Real-Time Security Monitoring

```yaml
real_time_monitoring:
  triggers:
    - new_package_installation
    - dependency_updates
    - vulnerability_database_updates
    - license_policy_changes
    
  continuous_scanning:
    - vulnerability_check_frequency: "daily"
    - license_compliance_recheck: "weekly"
    - supply_chain_monitoring: "continuous"
    - score_recalculation: "on_change"
    
  alert_conditions:
    critical:
      - new_critical_vulnerability_discovered
      - license_policy_violation
      - supply_chain_compromise_detected
    high:
      - security_score_drops_below_threshold
      - new_high_severity_vulnerability
      - maintainer_trust_score_degradation
    medium:
      - dependency_update_available_with_security_fix
      - license_compatibility_issue_detected

integration_points:
  ci_cd_pipeline:
    - pre_commit_hooks: "security_score_validation"
    - build_gates: "block_on_critical_vulnerabilities"
    - deployment_checks: "comprehensive_security_assessment"
    
  ide_integration:
    - real_time_security_indicators
    - vulnerability_highlighting
    - license_compliance_warnings
    
  package_managers:
    - custom_security_advisories
    - automated_security_updates
    - dependency_pinning_recommendations
```

## Usage Examples

```python
# Example: Comprehensive security validation
security_system = PackageSecurityValidation()

# Assess single package security
score = security_system.calculate_package_security_score("requests", "2.28.1", "python")
print(f"Security Score: {score.overall_score}/10 ({score.risk_level})")

# Batch assessment for project
packages = [
    PackageSpec("django", "4.2.0", "python"),
    PackageSpec("react", "18.2.0", "javascript"),
    PackageSpec("axios", "1.4.0", "javascript")
]

batch_report = security_system.batch_security_assessment(packages)
print(f"High-risk packages: {batch_report.high_risk_count}/{batch_report.total_packages}")

# Monitor dependency tree
dependency_tree = DependencyTree.from_project("./")
tree_scan = security_system.scan_dependency_tree(dependency_tree)
print(f"Tree security score: {tree_scan.overall_score}")
```

This security validation system provides comprehensive protection against vulnerable packages, ensures license compliance, validates supply chain integrity, and provides actionable security scoring to guide safe package selection in development workflows.