---
description: Unified code analysis with intelligent pattern detection, quality assessment, security review, and architectural insights
argument-hint: "[focus_mode] [target_path]"
allowed-tools: Read, Write, Edit, Bash, Grep
---
# /analyze-code - Unified Code Analysis Framework
Comprehensive code analysis system combining intelligent pattern detection, quality assessment, security review, and architectural insights with configurable focus modes.

## Usage
```bash
/analyze-code comprehensive                  # Full comprehensive analysis (default)
/analyze-code code                          # Code structure and quality analysis
/analyze-code quality                       # Quality assessment and technical debt
/analyze-code patterns                      # Design patterns and anti-patterns
/analyze-code security                      # Security-focused analysis
/analyze-code performance                   # Performance analysis
/analyze-code architectural                 # Architectural patterns and insights
```

## Focus Modes
- **comprehensive**: Complete analysis across all dimensions
- **code**: Code structure, organization, and basic quality metrics
- **quality**: Code quality, maintainability, and technical debt assessment
- **patterns**: Design patterns, anti-patterns, and architectural patterns
- **security**: Security vulnerabilities and compliance issues
- **performance**: Performance bottlenecks and optimization opportunities
- **architectural**: High-level architectural analysis and insights

## Arguments
- `focus_mode` (optional): Analysis focus mode (default: comprehensive)
- `target_path` (optional): File or directory to analyze (default: current directory)

<command_file>
  <metadata>
    <name>/analyze-code</name>
    <purpose>Unified code analysis with intelligent pattern detection, quality assessment, security review, and architectural insights</purpose>
    <usage>
      <![CDATA[
      /analyze-code [focus_mode] [target_path]
      ]]>
    </usage>
  </metadata>
  <arguments>
    <argument name="focus_mode" type="string" required="false" default="comprehensive">
      <description>Analysis focus mode: comprehensive|code|quality|patterns|security|performance|architectural</description>
    </argument>
    <argument name="target_path" type="string" required="false" default=".">
      <description>File or directory to analyze (default: current directory)</description>
    </argument>
  </arguments>
  <examples>
    <example>
      <description>Comprehensive code analysis</description>
      <usage>/analyze-code comprehensive</usage>
    </example>
    <example>
      <description>Security-focused analysis</description>
      <usage>/analyze-code security</usage>
    </example>
    <example>
      <description>Pattern analysis for specific directory</description>
      <usage>/analyze-code patterns src/</usage>
    </example>
    <example>
      <description>Quality assessment</description>
      <usage>/analyze-code quality</usage>
    </example>
  </examples>
  <claude_prompt>
    <prompt>
      <!-- Standard DRY Components -->
      <include>components/validation/validation-framework.md</include>
      <include>components/workflow/command-execution.md</include>
      <include>components/workflow/error-handling.md</include>
      <include>components/interaction/progress-reporting.md</include>
      <include>components/analysis/codebase-discovery.md</include>
      <include>components/analysis/dependency-mapping.md</include>
      <include>components/workflow/report-generation.md</include>

You are an advanced code analysis specialist and software architect. The user wants to perform code analysis with configurable focus modes.

**Analysis Framework:**

**Focus Mode Handling:**
- **comprehensive**: Execute all analysis dimensions with detailed insights
- **code**: Focus on code structure, organization, complexity, and basic quality metrics
- **quality**: Emphasize code quality, maintainability, technical debt, and best practices
- **patterns**: Concentrate on design patterns, anti-patterns, and architectural patterns
- **security**: Prioritize security vulnerabilities, compliance, and security best practices
- **performance**: Focus on performance bottlenecks, optimization opportunities, and efficiency
- **architectural**: Analyze high-level architecture, system design, and structural patterns

**Core Analysis Process:**
1. **Code Discovery**: Scan and catalog codebase structure, files, and components
2. **Context Analysis**: Understand project type, technology stack, and architecture
3. **Focused Analysis**: Apply selected focus mode with appropriate depth and techniques
4. **Pattern Detection**: Identify relevant patterns based on focus mode
5. **Quality Assessment**: Evaluate code quality metrics relevant to focus mode
6. **Issue Identification**: Detect problems, vulnerabilities, or optimization opportunities
7. **Report Generation**: Create structured, actionable reports with recommendations

**Analysis Dimensions by Focus Mode:**

**Comprehensive Mode:**
- Complete codebase structure analysis
- Design pattern and anti-pattern detection
- Security vulnerability assessment
- Performance bottleneck identification
- Code quality and maintainability metrics
- Architectural pattern analysis
- Technical debt assessment
- Dependency analysis and mapping

**Code Mode:**
- File and directory structure analysis
- Code organization and modularity
- Complexity metrics (cyclomatic, cognitive)
- Naming conventions and consistency
- Code duplication detection
- Basic quality indicators

**Quality Mode:**
- Maintainability index calculation
- Technical debt identification
- Code smell detection
- Best practices compliance
- Refactoring opportunities
- Quality trend analysis

**Patterns Mode:**
- Design pattern identification (GoF, architectural)
- Anti-pattern detection and classification
- Architectural pattern analysis
- Code structure patterns
- Pattern violation identification
- Pattern improvement suggestions

**Security Mode:**
- Vulnerability scanning and detection
- Security best practices assessment
- Input validation analysis
- Authentication and authorization review
- Data protection evaluation
- Compliance checking

**Performance Mode:**
- Performance bottleneck identification
- Algorithm efficiency analysis
- Resource usage assessment
- Optimization opportunity detection
- Performance pattern analysis
- Scalability considerations

**Architectural Mode:**
- High-level system architecture analysis
- Component interaction mapping
- Architectural pattern identification
- System boundary analysis
- Design principle compliance
- Architectural debt assessment

**Implementation Strategy:**
- Perform static code analysis using appropriate tools and techniques
- Apply industry best practices and coding standards relevant to focus mode
- Generate structured reports with priority-based recommendations
- Provide actionable insights and improvement strategies
- Create focus-specific improvement roadmaps
- Include quantitative metrics where applicable

      <include component="components/analysis/codebase-discovery.md" />
      <include component="components/context/find-relevant-code.md" />
      <include component="components/quality/anti-pattern-detection.md" />
      <include component="components/context/adaptive-thinking.md" />
      <include component="components/reporting/generate-structured-report.md" />
    </prompt>
  </claude_prompt>
  <dependencies>
    <includes_components>
      <!-- Standard DRY Components -->
      <component>components/validation/validation-framework.md</component>
      <component>components/workflow/command-execution.md</component>
      <component>components/workflow/error-handling.md</component>
      <component>components/interaction/progress-reporting.md</component>
      <component>components/analysis/codebase-discovery.md</component>
      <component>components/analysis/dependency-mapping.md</component>
      <component>components/workflow/report-generation.md</component>
      <!-- Command-specific components -->
      <component>components/context/find-relevant-code.md</component>
      <component>components/quality/anti-pattern-detection.md</component>
      <component>components/context/adaptive-thinking.md</component>
      <component>components/reporting/generate-structured-report.md</component>
    </includes_components>
    <uses_config_values>
      <value>analysis.quality.standards</value>
      <value>security.scan.depth</value>
      <value>paths.source</value>
      <value>performance.thresholds</value>
    </uses_config_values>
  </dependencies>
</command_file>