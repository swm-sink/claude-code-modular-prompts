#!/usr/bin/env swift

import Foundation

/**
 * XML Framework Validation Tool (Swift)
 * Validates Claude Code XML framework structure and performance
 */

struct ValidationResult {
    var isValid: Bool
    var issues: [String]
    var metrics: [String: Any]
    var fileName: String
}

struct ValidationSummary {
    var totalFiles: Int
    var validFiles: Int
    var totalIssues: Int
    var averageOptimizationScore: Double
    var tddComplianceAverage: Double
    var recommendations: [String]
}

class XMLFrameworkValidator {
    private let projectRoot: URL
    private let claudeDir: URL
    private var validationResults: [String: ValidationResult] = [:]
    
    init(projectRoot: String) {
        self.projectRoot = URL(fileURLWithPath: projectRoot)
        self.claudeDir = self.projectRoot.appendingPathComponent(".claude")
    }
    
    func validateXMLStructure(file: URL) -> ValidationResult {
        var result = ValidationResult(
            isValid: false,
            issues: [],
            metrics: [:],
            fileName: file.lastPathComponent
        )
        
        do {
            // Read file content
            let content = try String(contentsOf: file, encoding: .utf8)
            
            // Extract XML content from markdown
            let xmlPattern = "```xml\\s*\\n(.*?)\\n```"
            let regex = try NSRegularExpression(pattern: xmlPattern, options: [.dotMatchesLineSeparators])
            let range = NSRange(location: 0, length: content.utf16.count)
            
            guard let match = regex.firstMatch(in: content, options: [], range: range) else {
                result.issues.append("No XML content found in markdown")
                return result
            }
            
            let xmlRange = Range(match.range(at: 1), in: content)!
            let xmlContent = String(content[xmlRange])
            
            // Parse XML
            guard let xmlData = xmlContent.data(using: .utf8) else {
                result.issues.append("Unable to convert XML to data")
                return result
            }
            
            let parser = XMLParser(data: xmlData)
            let delegate = XMLValidationDelegate()
            parser.delegate = delegate
            
            if parser.parse() {
                result.isValid = true
                result.metrics = delegate.metrics
                result.issues = delegate.issues
                
                // Additional validation based on content
                validateCommandStructure(xmlContent: xmlContent, result: &result)
                calculatePerformanceMetrics(xmlContent: xmlContent, result: &result)
                validateTDDCompliance(xmlContent: xmlContent, result: &result)
                
            } else {
                result.issues.append("XML parsing failed")
                if let error = parser.parserError {
                    result.issues.append("Parser error: \\(error.localizedDescription)")
                }
            }
            
        } catch {
            result.issues.append("File reading error: \\(error.localizedDescription)")
        }
        
        return result
    }
    
    private func validateCommandStructure(xmlContent: String, result: inout ValidationResult) {
        var commandStructure: [String: Any] = [:]
        
        // Check for required elements
        commandStructure["has_delegation"] = xmlContent.contains("delegation")
        commandStructure["has_pattern_integration"] = xmlContent.contains("pattern_integration")
        commandStructure["has_thinking_pattern"] = xmlContent.contains("thinking_pattern")
        commandStructure["has_tdd_integration"] = xmlContent.contains("tdd_integration")
        
        // Count checkpoints
        let checkpointPattern = "checkpoint\\s+id="
        let checkpointRegex = try? NSRegularExpression(pattern: checkpointPattern, options: [])
        let checkpointRange = NSRange(location: 0, length: xmlContent.utf16.count)
        let checkpointCount = checkpointRegex?.numberOfMatches(in: xmlContent, options: [], range: checkpointRange) ?? 0
        commandStructure["checkpoint_count"] = checkpointCount
        
        // Count patterns
        let patternPattern = "uses_pattern\\s+from="
        let patternRegex = try? NSRegularExpression(pattern: patternPattern, options: [])
        let patternRange = NSRange(location: 0, length: xmlContent.utf16.count)
        let patternCount = patternRegex?.numberOfMatches(in: xmlContent, options: [], range: patternRange) ?? 0
        commandStructure["pattern_count"] = patternCount
        
        result.metrics["command_structure"] = commandStructure
        
        // Validate required elements
        if !xmlContent.contains("delegation") {
            result.issues.append("Missing delegation element")
        }
        if !xmlContent.contains("thinking_pattern") {
            result.issues.append("Missing thinking_pattern element")
        }
        if checkpointCount == 0 {
            result.issues.append("No checkpoints found")
        }
    }
    
    private func calculatePerformanceMetrics(xmlContent: String, result: inout ValidationResult) {
        var metrics: [String: Any] = [:]
        
        // Estimate tokens (rough: 1 token ≈ 4 characters)
        let estimatedTokens = xmlContent.count / 4
        metrics["estimated_tokens"] = estimatedTokens
        
        // Calculate nesting depth
        let depth = calculateXMLDepth(xmlContent: xmlContent)
        metrics["nesting_depth"] = depth
        
        // Parsing complexity
        let complexity: String
        if depth <= 3 {
            complexity = "low"
        } else if depth <= 6 {
            complexity = "medium"
        } else {
            complexity = "high"
        }
        metrics["parsing_complexity"] = complexity
        
        // Count parallel opportunities
        let parallelHints = countOccurrences(in: xmlContent, pattern: "parallel")
        let batchHints = countOccurrences(in: xmlContent, pattern: "batch")
        metrics["parallel_opportunities"] = parallelHints + batchHints
        
        // Calculate optimization score (0-100)
        var optimizationScore = 100.0
        if depth > 6 {
            optimizationScore -= 20
        }
        if estimatedTokens > 15000 {
            optimizationScore -= 20
        }
        if parallelHints + batchHints == 0 {
            optimizationScore -= 30
        }
        let mandatoryCount = countOccurrences(in: xmlContent, pattern: "enforcement=\"MANDATORY\"")
        if mandatoryCount < 3 {
            optimizationScore -= 10
        }
        
        metrics["optimization_score"] = max(0, optimizationScore)
        
        result.metrics["performance"] = metrics
    }
    
    private func validateTDDCompliance(xmlContent: String, result: inout ValidationResult) {
        var compliance: [String: Any] = [:]
        
        // Check for TDD elements
        compliance["has_tdd_integration"] = xmlContent.contains("tdd_integration")
        compliance["has_red_phase"] = xmlContent.contains("red_phase")
        compliance["has_green_phase"] = xmlContent.contains("green_phase")
        compliance["has_refactor_phase"] = xmlContent.contains("refactor_phase")
        compliance["has_blocking_conditions"] = xmlContent.contains("blocking_conditions")
        
        // Count quality gates
        let qualityGateCount = countOccurrences(in: xmlContent, pattern: "quality_gate")
        compliance["quality_gates_count"] = qualityGateCount
        
        // Calculate compliance score
        var score = 0.0
        if xmlContent.contains("tdd_integration") { score += 20 }
        if xmlContent.contains("red_phase") { score += 20 }
        if xmlContent.contains("green_phase") { score += 20 }
        if xmlContent.contains("refactor_phase") { score += 20 }
        if xmlContent.contains("blocking_conditions") { score += 10 }
        if qualityGateCount > 0 { score += min(10, Double(qualityGateCount) * 2) }
        
        compliance["compliance_score"] = score
        
        result.metrics["tdd_compliance"] = compliance
        
        // Check for issues
        if !xmlContent.contains("tdd_integration") {
            result.issues.append("Missing TDD integration")
        }
        if !(xmlContent.contains("red_phase") && xmlContent.contains("green_phase") && xmlContent.contains("refactor_phase")) {
            result.issues.append("Incomplete TDD cycle phases")
        }
    }
    
    private func calculateXMLDepth(xmlContent: String) -> Int {
        var maxDepth = 0
        var currentDepth = 0
        
        let lines = xmlContent.components(separatedBy: .newlines)
        for line in lines {
            let trimmed = line.trimmingCharacters(in: .whitespaces)
            if trimmed.hasPrefix("<") && !trimmed.hasPrefix("</") && !trimmed.contains("/>") {
                currentDepth += 1
                maxDepth = max(maxDepth, currentDepth)
            } else if trimmed.hasPrefix("</") {
                currentDepth -= 1
            }
        }
        
        return maxDepth
    }
    
    private func countOccurrences(in text: String, pattern: String) -> Int {
        let regex = try? NSRegularExpression(pattern: pattern, options: [.caseInsensitive])
        let range = NSRange(location: 0, length: text.utf16.count)
        return regex?.numberOfMatches(in: text, options: [], range: range) ?? 0
    }
    
    func runValidation() -> ValidationSummary {
        print("Starting XML Framework Validation (Swift)...")
        
        // Find all XML files
        let commandsDir = claudeDir.appendingPathComponent("commands")
        let modulesDir = claudeDir.appendingPathComponent("modules")
        
        var allFiles: [URL] = []
        
        // Get command files
        if let commandFiles = try? FileManager.default.contentsOfDirectory(at: commandsDir, includingPropertiesForKeys: nil, options: []) {
            allFiles.append(contentsOf: commandFiles.filter { $0.pathExtension == "md" })
        }
        
        // Get module files
        if let enumerator = FileManager.default.enumerator(at: modulesDir, includingPropertiesForKeys: nil) {
            for case let fileURL as URL in enumerator {
                if fileURL.pathExtension == "md" {
                    allFiles.append(fileURL)
                }
            }
        }
        
        print("Found \\(allFiles.count) files to validate")
        
        // Validate each file
        for file in allFiles {
            print("Validating \\(file.lastPathComponent)...")
            let result = validateXMLStructure(file: file)
            validationResults[file.lastPathComponent] = result
        }
        
        // Generate summary
        return generateSummary()
    }
    
    private func generateSummary() -> ValidationSummary {
        let totalFiles = validationResults.count
        let validFiles = validationResults.values.filter { $0.isValid }.count
        let totalIssues = validationResults.values.reduce(0) { $0 + $1.issues.count }
        
        // Calculate average optimization score
        let optimizationScores = validationResults.values.compactMap { result in
            (result.metrics["performance"] as? [String: Any])?["optimization_score"] as? Double
        }
        let avgOptimization = optimizationScores.isEmpty ? 0 : optimizationScores.reduce(0, +) / Double(optimizationScores.count)
        
        // Calculate average TDD compliance
        let tddScores = validationResults.values.compactMap { result in
            (result.metrics["tdd_compliance"] as? [String: Any])?["compliance_score"] as? Double
        }
        let avgTDD = tddScores.isEmpty ? 0 : tddScores.reduce(0, +) / Double(tddScores.count)
        
        // Generate recommendations
        var recommendations: [String] = []
        if avgOptimization < 80 {
            recommendations.append("Consider XML structure optimization for better performance")
        }
        if avgTDD < 80 {
            recommendations.append("Improve TDD compliance in command structures")
        }
        if totalIssues > 0 {
            recommendations.append("Address XML structure issues identified")
        }
        
        return ValidationSummary(
            totalFiles: totalFiles,
            validFiles: validFiles,
            totalIssues: totalIssues,
            averageOptimizationScore: avgOptimization,
            tddComplianceAverage: avgTDD,
            recommendations: recommendations
        )
    }
    
    func saveResults(to outputFile: String) {
        // Convert results to JSON
        var jsonResults: [String: Any] = [:]
        
        for (fileName, result) in validationResults {
            jsonResults[fileName] = [
                "isValid": result.isValid,
                "issues": result.issues,
                "metrics": result.metrics
            ]
        }
        
        do {
            let jsonData = try JSONSerialization.data(withJSONObject: jsonResults, options: [.prettyPrinted])
            try jsonData.write(to: URL(fileURLWithPath: outputFile))
            print("Validation results saved to \\(outputFile)")
        } catch {
            print("Error saving results: \\(error.localizedDescription)")
        }
    }
}

class XMLValidationDelegate: NSObject, XMLParserDelegate {
    var metrics: [String: Any] = [:]
    var issues: [String] = []
    var elementCount = 0
    var maxDepth = 0
    var currentDepth = 0
    var attributeCount = 0
    
    func parser(_ parser: XMLParser, didStartElement elementName: String, namespaceURI: String?, qualifiedName qName: String?, attributes attributeDict: [String : String] = [:]) {
        elementCount += 1
        currentDepth += 1
        maxDepth = max(maxDepth, currentDepth)
        attributeCount += attributeDict.count
        
        // Update metrics
        metrics["element_count"] = elementCount
        metrics["max_depth"] = maxDepth
        metrics["attribute_count"] = attributeCount
    }
    
    func parser(_ parser: XMLParser, didEndElement elementName: String, namespaceURI: String?, qualifiedName qName: String?) {
        currentDepth -= 1
    }
    
    func parser(_ parser: XMLParser, parseErrorOccurred parseError: Error) {
        issues.append("XML parsing error: \\(parseError.localizedDescription)")
    }
}

// Main execution
func main() {
    guard CommandLine.argc >= 2 else {
        print("Usage: swift XMLValidator.swift <project_root>")
        exit(1)
    }
    
    let projectRoot = CommandLine.arguments[1]
    let validator = XMLFrameworkValidator(projectRoot: projectRoot)
    
    let startTime = CFAbsoluteTimeGetCurrent()
    let summary = validator.runValidation()
    let endTime = CFAbsoluteTimeGetCurrent()
    
    // Print summary
    print("\\n=== XML Framework Validation Summary (Swift) ===")
    print("Validation completed in \\(String(format: "%.2f", endTime - startTime)) seconds")
    print("Total files validated: \\(summary.totalFiles)")
    print("Valid XML files: \\(summary.validFiles)")
    print("Total issues found: \\(summary.totalIssues)")
    print("Average optimization score: \\(String(format: "%.1f", summary.averageOptimizationScore))/100")
    print("Average TDD compliance: \\(String(format: "%.1f", summary.tddComplianceAverage))/100")
    
    if !summary.recommendations.isEmpty {
        print("\\nRecommendations:")
        for rec in summary.recommendations {
            print("  - \\(rec)")
        }
    }
    
    // Save results
    validator.saveResults(to: "xml_validation_results_swift.json")
    
    // Exit with appropriate code
    let exitCode = (summary.validFiles == summary.totalFiles && summary.totalIssues == 0) ? 0 : 1
    exit(Int32(exitCode))
}

main()