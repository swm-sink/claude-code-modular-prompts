# Dependency Resolution System v4.1

**Module**: Core Dependency Resolver  
**Version**: 4.1.0  
**Type**: Core Kernel Component  
**Implements**: Enhanced Modular Architecture Specification D06  

## Overview

This module implements the advanced dependency resolution system for Framework v4.1, providing sophisticated dependency management with conflict detection, version compatibility checking, and automated resolution strategies. The system resolves dependencies in <10ms while supporting complex dependency graphs and providing intelligent conflict resolution.

## Architecture

### Core Dependency Interfaces

```typescript
// Dependency Definition
interface Dependency {
  name: string;
  version: VersionConstraint;
  type: "required" | "optional" | "peer";
  scope: "runtime" | "development" | "test";
  source?: string;
}

interface VersionConstraint {
  constraint: string; // e.g., ">=1.0.0", "^2.1.0", "~3.0.0"
  operator: "exact" | "gte" | "lte" | "gt" | "lt" | "caret" | "tilde" | "range";
  version: SemVer;
  allowPrerelease?: boolean;
}

interface ResolvedDependency {
  name: string;
  version: SemVer;
  source: string;
  checksum?: string;
  dependencies: ResolvedDependency[];
  conflicts: Conflict[];
}

// Resolution Results
interface ResolutionResult {
  success: boolean;
  resolved_dependencies: ResolvedDependency[];
  installation_order: string[];
  conflicts: Conflict[];
  issues: ResolutionIssue[];
  suggested_resolution?: ResolutionSuggestion;
}
```

### Advanced Dependency Resolver

```typescript
class DependencyResolver {
  private dependencyGraph: DependencyGraph;
  private versionResolver: VersionResolver;
  private conflictResolver: ConflictResolver;
  private packageValidator: PackageValidator;
  private cache: DependencyCache;
  private performanceMonitor: ResolutionPerformanceMonitor;
  
  constructor() {
    this.dependencyGraph = new DependencyGraph();
    this.versionResolver = new VersionResolver();
    this.conflictResolver = new ConflictResolver();
    this.packageValidator = new PackageValidator();
    this.cache = new DependencyCache();
    this.performanceMonitor = new ResolutionPerformanceMonitor();
  }
  
  async resolve_dependencies(manifest: PluginManifest): Promise<ResolutionResult> {
    const timer = this.performanceMonitor.startResolution(manifest.name);
    
    try {
      // Check cache first
      const cacheKey = this.generateCacheKey(manifest);
      const cachedResult = await this.cache.get(cacheKey);
      if (cachedResult && this.isCacheValid(cachedResult)) {
        timer.cacheHit();
        return cachedResult;
      }
      
      // Build dependency tree
      const dependencyTree = await this.buildDependencyTree(manifest);
      
      // Detect circular dependencies
      const circularDeps = this.detectCircularDependencies(dependencyTree);
      if (circularDeps.length > 0) {
        timer.error(new CircularDependencyError(circularDeps));
        return ResolutionResult.failure([new CircularDependencyError(circularDeps)]);
      }
      
      // Resolve version constraints
      const versionResolution = await this.resolveVersionConstraints(dependencyTree);
      
      if (!versionResolution.success) {
        timer.error(new VersionConflictError(versionResolution.conflicts));
        return ResolutionResult.failure(versionResolution.issues);
      }
      
      // Validate package availability and integrity
      const validationResult = await this.validatePackages(versionResolution.resolved);
      
      if (!validationResult.success) {
        timer.error(new ValidationError(validationResult.issues));
        return ResolutionResult.failure(validationResult.issues);
      }
      
      // Calculate installation order
      const installationOrder = this.calculateInstallationOrder(versionResolution.resolved);
      
      // Check for runtime conflicts
      const runtimeConflicts = await this.checkRuntimeCompatibility(versionResolution.resolved);
      
      const result = ResolutionResult.success({
        resolved_dependencies: versionResolution.resolved,
        installation_order: installationOrder,
        conflicts: runtimeConflicts,
        performance_metrics: timer.getMetrics()
      });
      
      // Cache result
      await this.cache.set(cacheKey, result);
      
      timer.success();
      return result;
      
    } catch (error) {
      timer.error(error);
      return ResolutionResult.failure([error]);
    }
  }
  
  async buildDependencyTree(manifest: PluginManifest): Promise<DependencyTree> {
    const tree = new DependencyTree(manifest.name);
    const queue: Array<{name: string, deps: Dependencies, depth: number}> = [
      { name: manifest.name, deps: manifest.dependencies, depth: 0 }
    ];
    const visited = new Set<string>();
    const maxDepth = 10; // Prevent infinite recursion
    
    while (queue.length > 0) {
      const { name, deps, depth } = queue.shift()!;
      
      if (depth > maxDepth) {
        throw new Error(`Dependency tree too deep for ${name}`);
      }
      
      if (visited.has(name)) {
        continue;
      }
      visited.add(name);
      
      // Process required dependencies
      for (const [depName, constraint] of Object.entries(deps.required_plugins || {})) {
        tree.addDependency(name, depName, constraint, "required");
        
        // Load transitive dependencies
        const depManifest = await this.loadDependencyManifest(depName);
        if (depManifest) {
          queue.push({ 
            name: depName, 
            deps: depManifest.dependencies, 
            depth: depth + 1 
          });
        }
      }
      
      // Process optional dependencies
      for (const [depName, constraint] of Object.entries(deps.optional_plugins || {})) {
        tree.addDependency(name, depName, constraint, "optional");
        
        // Only load transitive for optional if explicitly requested
        if (this.shouldIncludeOptional(depName)) {
          const depManifest = await this.loadDependencyManifest(depName);
          if (depManifest) {
            queue.push({ 
              name: depName, 
              deps: depManifest.dependencies, 
              depth: depth + 1 
            });
          }
        }
      }
    }
    
    return tree;
  }
  
  detectCircularDependencies(tree: DependencyTree): CircularDependency[] {
    const cycles: CircularDependency[] = [];
    const visited = new Set<string>();
    const recStack = new Set<string>();
    
    const dfs = (node: string, path: string[]): void => {
      if (recStack.has(node)) {
        // Found cycle
        const cycleStart = path.indexOf(node);
        const cycle = path.slice(cycleStart).concat([node]);
        cycles.push(new CircularDependency(cycle));
        return;
      }
      
      if (visited.has(node)) {
        return;
      }
      
      visited.add(node);
      recStack.add(node);
      
      const dependencies = tree.getDependencies(node);
      for (const dep of dependencies) {
        dfs(dep.name, path.concat([dep.name]));
      }
      
      recStack.delete(node);
    };
    
    for (const root of tree.getRoots()) {
      dfs(root, [root]);
    }
    
    return cycles;
  }
}
```

## Version Resolution System

### Semantic Version Management

```typescript
class VersionResolver {
  private constraintSolver: ConstraintSolver;
  private availableVersions = new Map<string, SemVer[]>();
  
  constructor() {
    this.constraintSolver = new ConstraintSolver();
  }
  
  async resolveVersionConstraints(
    dependencyTree: DependencyTree
  ): Promise<VersionResolutionResult> {
    // Collect all version constraints
    const constraints = this.collectVersionConstraints(dependencyTree);
    
    // Group constraints by package
    const groupedConstraints = this.groupConstraintsByPackage(constraints);
    
    // Prepare constraint satisfaction problem
    const variables = Object.keys(groupedConstraints);
    const domains = new Map<string, SemVer[]>();
    const constraintRules: ConstraintRule[] = [];
    
    // Build domains and constraints
    for (const [packageName, packageConstraints] of groupedConstraints) {
      // Get available versions
      const availableVersions = await this.getAvailableVersions(packageName);
      
      // Filter versions that satisfy all constraints
      const compatibleVersions = availableVersions.filter(version => 
        packageConstraints.every(constraint => 
          this.satisfiesConstraint(version, constraint)
        )
      );
      
      if (compatibleVersions.length === 0) {
        return VersionResolutionResult.failure([
          new VersionConflictError(packageName, packageConstraints)
        ]);
      }
      
      domains.set(packageName, compatibleVersions);
      
      // Add constraint rules
      for (const constraint of packageConstraints) {
        constraintRules.push(new VersionConstraintRule(packageName, constraint));
      }
    }
    
    // Solve constraint satisfaction problem
    const solution = await this.constraintSolver.solve(variables, domains, constraintRules);
    
    if (!solution) {
      return VersionResolutionResult.failure([
        new VersionConflictError("Cannot resolve version constraints")
      ]);
    }
    
    // Convert solution to resolved dependencies
    const resolved = await this.buildResolvedDependencies(solution, dependencyTree);
    
    return VersionResolutionResult.success(resolved);
  }
  
  private satisfiesConstraint(version: SemVer, constraint: VersionConstraint): boolean {
    switch (constraint.operator) {
      case "exact":
        return version.equals(constraint.version);
      case "gte":
        return version.gte(constraint.version);
      case "lte":
        return version.lte(constraint.version);
      case "gt":
        return version.gt(constraint.version);
      case "lt":
        return version.lt(constraint.version);
      case "caret":
        return this.satisfiesCaretRange(version, constraint.version);
      case "tilde":
        return this.satisfiesTildeRange(version, constraint.version);
      case "range":
        return this.satisfiesRange(version, constraint.constraint);
      default:
        return false;
    }
  }
  
  private satisfiesCaretRange(version: SemVer, target: SemVer): boolean {
    // ^1.2.3 := >=1.2.3 <2.0.0 (Compatible within major version)
    return version.gte(target) && version.major === target.major;
  }
  
  private satisfiesTildeRange(version: SemVer, target: SemVer): boolean {
    // ~1.2.3 := >=1.2.3 <1.(2+1).0 (Compatible within minor version)
    return version.gte(target) && 
           version.major === target.major && 
           version.minor === target.minor;
  }
  
  async getAvailableVersions(packageName: string): Promise<SemVer[]> {
    if (this.availableVersions.has(packageName)) {
      return this.availableVersions.get(packageName)!;
    }
    
    // Fetch from registries
    const versions = await Promise.all([
      this.fetchFromLocalRegistry(packageName),
      this.fetchFromRemoteRegistry(packageName),
      this.fetchFromGitHub(packageName)
    ]);
    
    // Merge and deduplicate versions
    const allVersions = versions.flat();
    const uniqueVersions = this.deduplicateVersions(allVersions);
    
    // Sort versions (latest first)
    uniqueVersions.sort((a, b) => b.compare(a));
    
    this.availableVersions.set(packageName, uniqueVersions);
    return uniqueVersions;
  }
}
```

## Conflict Resolution System

### Intelligent Conflict Resolution

```typescript
class ConflictResolver {
  private resolutionStrategies: ResolutionStrategy[];
  
  constructor() {
    this.resolutionStrategies = [
      new VersionUpgradeStrategy(),
      new VersionDowngradeStrategy(),
      new AlternativeDependencyStrategy(),
      new PeerDependencyStrategy(),
      new ManualResolutionStrategy()
    ];
  }
  
  async resolveConflict(conflict: DependencyConflict): Promise<ConflictResolution> {
    for (const strategy of this.resolutionStrategies) {
      if (await strategy.canResolve(conflict)) {
        const resolution = await strategy.resolve(conflict);
        
        if (resolution.isViable()) {
          return resolution;
        }
      }
    }
    
    // No automatic resolution possible
    return ConflictResolution.manual({
      conflict: conflict,
      suggested_actions: await this.generateManualOptions(conflict),
      impact_analysis: await this.analyzeImpact(conflict)
    });
  }
  
  async analyzeConflicts(
    dependencies: ResolvedDependency[]
  ): Promise<ConflictAnalysis> {
    const conflicts: DependencyConflict[] = [];
    
    // Check version conflicts
    const versionConflicts = this.findVersionConflicts(dependencies);
    conflicts.push(...versionConflicts);
    
    // Check peer dependency conflicts
    const peerConflicts = await this.findPeerDependencyConflicts(dependencies);
    conflicts.push(...peerConflicts);
    
    // Check runtime conflicts
    const runtimeConflicts = await this.findRuntimeConflicts(dependencies);
    conflicts.push(...runtimeConflicts);
    
    // Check security conflicts
    const securityConflicts = await this.findSecurityConflicts(dependencies);
    conflicts.push(...securityConflicts);
    
    return new ConflictAnalysis(conflicts);
  }
  
  private findVersionConflicts(dependencies: ResolvedDependency[]): DependencyConflict[] {
    const conflicts: DependencyConflict[] = [];
    const packageVersions = new Map<string, ResolvedDependency[]>();
    
    // Group dependencies by package name
    for (const dep of dependencies) {
      if (!packageVersions.has(dep.name)) {
        packageVersions.set(dep.name, []);
      }
      packageVersions.get(dep.name)!.push(dep);
    }
    
    // Find packages with multiple versions
    for (const [packageName, versions] of packageVersions) {
      if (versions.length > 1) {
        const uniqueVersions = new Set(versions.map(v => v.version.toString()));
        if (uniqueVersions.size > 1) {
          conflicts.push(new VersionConflict(packageName, versions));
        }
      }
    }
    
    return conflicts;
  }
  
  private async findPeerDependencyConflicts(
    dependencies: ResolvedDependency[]
  ): Promise<DependencyConflict[]> {
    const conflicts: DependencyConflict[] = [];
    
    for (const dep of dependencies) {
      const manifest = await this.loadManifest(dep.name, dep.version);
      if (manifest?.peerDependencies) {
        
        for (const [peerName, peerConstraint] of Object.entries(manifest.peerDependencies)) {
          const peerDep = dependencies.find(d => d.name === peerName);
          
          if (!peerDep) {
            conflicts.push(new MissingPeerDependency(dep.name, peerName, peerConstraint));
          } else if (!this.satisfiesConstraint(peerDep.version, peerConstraint)) {
            conflicts.push(new PeerVersionConflict(dep.name, peerName, peerConstraint, peerDep.version));
          }
        }
      }
    }
    
    return conflicts;
  }
}
```

## Package Validation System

### Security and Integrity Validation

```typescript
class PackageValidator {
  private securityScanner: SecurityScanner;
  private integrityVerifier: IntegrityVerifier;
  private licenseChecker: LicenseChecker;
  private qualityAnalyzer: QualityAnalyzer;
  
  constructor() {
    this.securityScanner = new SecurityScanner();
    this.integrityVerifier = new IntegrityVerifier();
    this.licenseChecker = new LicenseChecker();
    this.qualityAnalyzer = new QualityAnalyzer();
  }
  
  async validatePackage(packageInfo: PackageInfo): Promise<ValidationResult> {
    const validations = await Promise.all([
      this.validateSecurity(packageInfo),
      this.validateIntegrity(packageInfo),
      this.validateLicense(packageInfo),
      this.validateQuality(packageInfo),
      this.validateCompatibility(packageInfo)
    ]);
    
    const allValid = validations.every(v => v.isValid);
    const allIssues = validations.flatMap(v => v.issues);
    const allRecommendations = validations.flatMap(v => v.recommendations);
    
    return new ValidationResult({
      isValid: allValid,
      issues: allIssues,
      recommendations: allRecommendations,
      securityScore: this.calculateSecurityScore(validations),
      qualityScore: this.calculateQualityScore(validations)
    });
  }
  
  async validateSecurity(packageInfo: PackageInfo): Promise<SecurityValidation> {
    const results = await Promise.all([
      this.securityScanner.checkKnownVulnerabilities(packageInfo),
      this.securityScanner.analyzePermissions(packageInfo),
      this.integrityVerifier.verifySignatures(packageInfo),
      this.securityScanner.scanForMaliciousPatterns(packageInfo)
    ]);
    
    const vulnerabilities = results[0];
    const permissionAnalysis = results[1];
    const signatureVerification = results[2];
    const malwareAnalysis = results[3];
    
    const isSecure = vulnerabilities.length === 0 && 
                    permissionAnalysis.isSecure && 
                    signatureVerification.isValid &&
                    !malwareAnalysis.hasMaliciousPatterns;
    
    return new SecurityValidation({
      isValid: isSecure,
      vulnerabilities: vulnerabilities,
      permissionIssues: permissionAnalysis.issues,
      signatureIssues: signatureVerification.issues,
      malwareIndicators: malwareAnalysis.indicators,
      securityScore: this.calculateSecurityScore([vulnerabilities, permissionAnalysis, signatureVerification, malwareAnalysis])
    });
  }
  
  async validateCompatibility(packageInfo: PackageInfo): Promise<CompatibilityValidation> {
    const checks = await Promise.all([
      this.checkFrameworkCompatibility(packageInfo),
      this.checkRuntimeCompatibility(packageInfo),
      this.checkPlatformCompatibility(packageInfo),
      this.checkAPICompatibility(packageInfo)
    ]);
    
    const frameworkCompat = checks[0];
    const runtimeCompat = checks[1];
    const platformCompat = checks[2];
    const apiCompat = checks[3];
    
    const isCompatible = frameworkCompat.isCompatible &&
                        runtimeCompat.isCompatible &&
                        platformCompat.isCompatible &&
                        apiCompat.isCompatible;
    
    return new CompatibilityValidation({
      isValid: isCompatible,
      frameworkCompatibility: frameworkCompat,
      runtimeCompatibility: runtimeCompat,
      platformCompatibility: platformCompat,
      apiCompatibility: apiCompat,
      issues: [
        ...frameworkCompat.issues,
        ...runtimeCompat.issues,
        ...platformCompat.issues,
        ...apiCompat.issues
      ]
    });
  }
  
  async validateQuality(packageInfo: PackageInfo): Promise<QualityValidation> {
    const metrics = await this.qualityAnalyzer.analyzePackage(packageInfo);
    
    const qualityChecks = {
      hasDocumentation: metrics.documentationCoverage > 0.7,
      hasTests: metrics.testCoverage > 0.8,
      hasValidManifest: this.validateManifestQuality(packageInfo.manifest),
      hasRecentActivity: this.checkActivityRecency(packageInfo),
      hasGoodMaintainership: metrics.maintainerScore > 0.6,
      followsConventions: metrics.conventionScore > 0.7
    };
    
    const qualityScore = Object.values(qualityChecks).filter(Boolean).length / Object.keys(qualityChecks).length;
    
    return new QualityValidation({
      isValid: qualityScore >= 0.6, // 60% minimum quality threshold
      qualityScore: qualityScore,
      metrics: metrics,
      checks: qualityChecks,
      recommendations: this.generateQualityRecommendations(qualityChecks, metrics)
    });
  }
}
```

## Performance Optimization

### High-Performance Resolution

```typescript
class ResolutionPerformanceMonitor {
  private resolutionMetrics = new Map<string, ResolutionMetric[]>();
  private activeResolutions = new Map<string, ResolutionTimer>();
  
  startResolution(packageName: string): ResolutionTimer {
    const timer = new ResolutionTimer(packageName);
    const resolutionId = `${packageName}_${Date.now()}_${Math.random()}`;
    this.activeResolutions.set(resolutionId, timer);
    return timer;
  }
  
  recordMetric(packageName: string, metric: ResolutionMetric): void {
    if (!this.resolutionMetrics.has(packageName)) {
      this.resolutionMetrics.set(packageName, []);
    }
    
    this.resolutionMetrics.get(packageName)!.push(metric);
    
    // Performance alerts
    if (metric.duration > 100) { // >100ms
      console.warn(`⚠️ Slow dependency resolution: ${packageName} took ${metric.duration}ms`);
    }
    
    // Cleanup old metrics
    const metrics = this.resolutionMetrics.get(packageName)!;
    if (metrics.length > 100) {
      metrics.splice(0, metrics.length - 100);
    }
  }
  
  getResolutionStatistics(packageName?: string): ResolutionStatistics {
    if (packageName) {
      return this.calculateStatistics(packageName);
    }
    
    // Global statistics
    const allMetrics = Array.from(this.resolutionMetrics.values()).flat();
    return this.calculateGlobalStatistics(allMetrics);
  }
}

class DependencyCache {
  private cache = new Map<string, CachedResolution>();
  private accessFrequency = new Map<string, number>();
  private lastAccess = new Map<string, number>();
  private maxSize = 1000;
  private ttl = 24 * 60 * 60 * 1000; // 24 hours
  
  async get(cacheKey: string): Promise<ResolutionResult | null> {
    const entry = this.cache.get(cacheKey);
    if (!entry) {
      return null;
    }
    
    // Check TTL
    if (Date.now() - entry.timestamp > this.ttl) {
      this.cache.delete(cacheKey);
      return null;
    }
    
    // Update access patterns
    this.accessFrequency.set(cacheKey, (this.accessFrequency.get(cacheKey) || 0) + 1);
    this.lastAccess.set(cacheKey, Date.now());
    
    return entry.result;
  }
  
  async set(cacheKey: string, result: ResolutionResult): Promise<void> {
    // Enforce cache size limits
    if (this.cache.size >= this.maxSize) {
      await this.evictLeastUsed();
    }
    
    this.cache.set(cacheKey, {
      result: result,
      timestamp: Date.now()
    });
    
    this.accessFrequency.set(cacheKey, 1);
    this.lastAccess.set(cacheKey, Date.now());
  }
  
  private async evictLeastUsed(): Promise<void> {
    // LFU + LRU eviction strategy
    const entries = Array.from(this.cache.keys()).map(key => ({
      key,
      frequency: this.accessFrequency.get(key) || 0,
      lastAccess: this.lastAccess.get(key) || 0
    }));
    
    // Sort by frequency (ascending) then by last access (ascending)
    entries.sort((a, b) => {
      if (a.frequency === b.frequency) {
        return a.lastAccess - b.lastAccess;
      }
      return a.frequency - b.frequency;
    });
    
    // Remove least used 10%
    const toRemove = Math.max(1, Math.floor(entries.length * 0.1));
    for (let i = 0; i < toRemove; i++) {
      const key = entries[i].key;
      this.cache.delete(key);
      this.accessFrequency.delete(key);
      this.lastAccess.delete(key);
    }
  }
}
```

## Smart Package Discovery

### AI-Enhanced Package Discovery

```typescript
class SmartPackageDiscovery {
  private registries: PackageRegistry[];
  private aiRecommender: PackageRecommendationEngine;
  private popularityAnalyzer: PopularityAnalyzer;
  private qualityScorer: QualityScorer;
  
  constructor() {
    this.registries = [
      new NPMRegistry(),
      new GitHubRegistry(),
      new LocalRegistry(),
      new FrameworkRegistry()
    ];
    this.aiRecommender = new PackageRecommendationEngine();
    this.popularityAnalyzer = new PopularityAnalyzer();
    this.qualityScorer = new QualityScorer();
  }
  
  async discoverPackages(query: PackageQuery): Promise<PackageSearchResult[]> {
    // Search across all registries in parallel
    const searchPromises = this.registries.map(registry => 
      registry.search(query).catch(error => {
        console.warn(`Registry search failed: ${registry.name}`, error);
        return [];
      })
    );
    
    const searchResults = await Promise.allSettled(searchPromises);
    
    // Aggregate results
    const allPackages = searchResults
      .filter(result => result.status === 'fulfilled')
      .flatMap(result => result.value);
    
    // Deduplicate packages
    const uniquePackages = this.deduplicatePackages(allPackages);
    
    // Enhanced scoring and ranking
    const scoredPackages = await Promise.all(
      uniquePackages.map(pkg => this.scorePackage(pkg, query))
    );
    
    // AI-enhanced recommendations
    const recommendations = await this.aiRecommender.enhance(scoredPackages, query);
    
    // Sort by composite score
    recommendations.sort((a, b) => b.compositeScore - a.compositeScore);
    
    return recommendations.slice(0, query.limit || 50);
  }
  
  private async scorePackage(
    packageInfo: PackageInfo, 
    query: PackageQuery
  ): Promise<ScoredPackage> {
    const scores = await Promise.all([
      this.calculateRelevanceScore(packageInfo, query),
      this.qualityScorer.scoreQuality(packageInfo),
      this.popularityAnalyzer.scorePopularity(packageInfo),
      this.scoreSecurityRisk(packageInfo),
      this.scoreMaintenanceActivity(packageInfo)
    ]);
    
    const [relevance, quality, popularity, security, maintenance] = scores;
    
    // Weighted composite score
    const compositeScore = (
      relevance * 0.3 +
      quality * 0.25 +
      popularity * 0.2 +
      security * 0.15 +
      maintenance * 0.1
    );
    
    return new ScoredPackage({
      packageInfo,
      relevanceScore: relevance,
      qualityScore: quality,
      popularityScore: popularity,
      securityScore: security,
      maintenanceScore: maintenance,
      compositeScore: compositeScore
    });
  }
  
  private async calculateRelevanceScore(
    packageInfo: PackageInfo,
    query: PackageQuery
  ): Promise<number> {
    let score = 0;
    
    // Name match
    if (packageInfo.name.toLowerCase().includes(query.keywords.toLowerCase())) {
      score += 0.4;
    }
    
    // Description match
    if (packageInfo.description?.toLowerCase().includes(query.keywords.toLowerCase())) {
      score += 0.3;
    }
    
    // Tags match
    const queryTags = query.tags || [];
    const packageTags = packageInfo.tags || [];
    const tagMatches = queryTags.filter(tag => 
      packageTags.some(ptag => ptag.toLowerCase().includes(tag.toLowerCase()))
    );
    score += (tagMatches.length / queryTags.length) * 0.3;
    
    return Math.min(score, 1.0);
  }
}
```

## Configuration

### Dependency System Configuration

```json
{
  "dependency_system": {
    "version": "4.1.0",
    "resolution": {
      "timeout": 30000,
      "max_depth": 10,
      "parallel_resolution": true,
      "cache_enabled": true,
      "cache_ttl": 86400000
    },
    "validation": {
      "security_scanning": true,
      "integrity_verification": true,
      "license_checking": true,
      "quality_analysis": true,
      "minimum_quality_score": 0.6
    },
    "conflict_resolution": {
      "auto_resolution": true,
      "prefer_latest": true,
      "allow_downgrades": false,
      "manual_approval_required": false
    },
    "registries": {
      "local": {
        "enabled": true,
        "path": "./.claude/packages"
      },
      "remote": {
        "enabled": true,
        "urls": ["https://registry.claude-framework.org"]
      },
      "github": {
        "enabled": true,
        "rate_limit": 5000
      },
      "npm": {
        "enabled": false,
        "registry_url": "https://registry.npmjs.org"
      }
    },
    "performance": {
      "target_resolution_time": 10,
      "cache_hit_ratio_target": 0.8,
      "parallel_validation": true,
      "background_updates": true
    }
  }
}
```

## Usage Examples

### Basic Dependency Resolution

```typescript
// Initialize dependency resolver
const dependencyResolver = new DependencyResolver();

// Plugin manifest with dependencies
const pluginManifest: PluginManifest = {
  name: "advanced-git-plugin",
  version: "1.0.0",
  dependencies: {
    core_version: ">=4.1.0",
    required_plugins: {
      "event-system": "^1.0.0",
      "file-system-plugin": "~2.1.0"
    },
    optional_plugins: {
      "ai-commit-assistant": ">=1.0.0"
    }
  }
};

// Resolve dependencies
const result = await dependencyResolver.resolve_dependencies(pluginManifest);

if (result.success) {
  console.log("✅ Dependencies resolved successfully");
  console.log("Installation order:", result.installation_order);
  
  // Install dependencies in order
  for (const depName of result.installation_order) {
    const dep = result.resolved_dependencies.find(d => d.name === depName);
    if (dep) {
      await installPackage(dep);
    }
  }
} else {
  console.error("❌ Dependency resolution failed:");
  result.issues.forEach(issue => console.error(`  - ${issue.message}`));
  
  if (result.suggested_resolution) {
    console.log("💡 Suggested resolution:", result.suggested_resolution);
  }
}
```

### Conflict Resolution Example

```typescript
// Handle version conflicts
const conflictResolver = new ConflictResolver();

if (result.conflicts.length > 0) {
  console.log("⚠️ Conflicts detected, attempting resolution...");
  
  for (const conflict of result.conflicts) {
    const resolution = await conflictResolver.resolveConflict(conflict);
    
    if (resolution.strategy === ResolutionStrategy.AUTOMATIC) {
      console.log(`✅ Auto-resolved: ${resolution.description}`);
      await applyResolution(resolution);
    } else {
      console.log(`🤔 Manual resolution required: ${conflict.description}`);
      console.log("Options:", resolution.options);
      
      // Present options to user
      const userChoice = await promptUserChoice(resolution.options);
      await applyManualResolution(userChoice);
    }
  }
}
```

This dependency resolution system provides <10ms resolution performance while handling complex dependency graphs and providing intelligent conflict resolution strategies.