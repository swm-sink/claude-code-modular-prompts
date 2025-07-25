---
description: Unified intelligent development workflow with code formatting, linting, refactoring, debugging, feature development, project initialization, analysis, and dependency management
argument-hint: "[mode] [target] [options]"
allowed-tools: Read, Write, Edit, Bash, Grep, Glob
---
# /dev - Unified Development Workflow Framework

Comprehensive development workflow solution combining code formatting, linting, refactoring, debugging, feature development, project initialization, analysis, and dependency management in a single unified command.

## Usage
```bash
# Code Quality & Maintenance
/dev format python --style black                 # Format Python code using Black style
/dev lint --javascript --fix                     # Lint and fix JavaScript issues
/dev refactor "src/utils.js" --strategy extract-method # Refactor code with method extraction

# Development Operations
/dev debug "Login fails with 500 error" --interactive # Interactive debugging session
/dev feature "User profile management"           # Complete feature development
/dev init webapp --react                         # Initialize new React web application
/dev analyze . --optimization                    # Analyze existing project for optimization
/dev deps security --automated                   # Security-focused dependency updates

# Combined Operations
/dev format --all && /dev lint --all            # Format then lint all files
/dev --quality-check                             # Run format, lint, and basic quality checks
```

<command_file>
  <metadata>
    <name>/dev</name>
    <purpose>Unified intelligent development workflow with code formatting, linting, refactoring, debugging, feature development, project initialization, analysis, and dependency management</purpose>
    <usage>
      <![CDATA[
      /dev [mode] [target] [options]
      
      Modes: format, lint, refactor, debug, feature, init, analyze, deps
      Options: --style, --fix, --strategy, --interactive, --automated, --optimization, --all, --quality-check
      ]]>
    </usage>
  </metadata>
  
  <arguments>
    <argument name="mode" type="string" required="false" default="format">
      <description>Development operation mode: format, lint, refactor, debug, feature, init, analyze, deps</description>
    </argument>
    <argument name="target" type="string" required="false">
      <description>Target file, directory, or description for the operation</description>
    </argument>
    <argument name="language" type="string" required="false">
      <description>Programming language for language-specific operations</description>
    </argument>
    <argument name="style" type="string" required="false" default="default">
      <description>Style guide for formatting (black, prettier, google, etc.)</description>
    </argument>
    <argument name="fix" type="boolean" required="false" default="false">
      <description>Automatically fix issues where possible</description>
    </argument>
    <argument name="strategy" type="string" required="false" default="all">
      <description>Refactoring strategy (extract-method, simplify-conditionals, remove-duplication, all)</description>
    </argument>
    <argument name="interactive" type="boolean" required="false" default="false">
      <description>Enable interactive mode for debugging or operations</description>
    </argument>
    <argument name="project_type" type="string" required="false" default="webapp">
      <description>Type of project to initialize (webapp, api, library, etc.)</description>
    </argument>
    <argument name="optimization" type="boolean" required="false" default="false">
      <description>Focus on optimization recommendations</description>
    </argument>
    <argument name="scope" type="string" required="false" default="security">
      <description>Scope for dependency updates (security, all, compatibility)</description>
    </argument>
    <argument name="automated" type="boolean" required="false" default="false">
      <description>Enable fully automated operation mode</description>
    </argument>
    <argument name="all" type="boolean" required="false" default="false">
      <description>Apply operation to all applicable files</description>
    </argument>
    <argument name="quality_check" type="boolean" required="false" default="false">
      <description>Run comprehensive quality checks (format + lint + basic analysis)</description>
    </argument>
    <argument name="config_file" type="string" required="false">
      <description>Configuration file path for linting or other operations</description>
    </argument>
    <argument name="issue_description" type="string" required="false">
      <description>Description of the issue to debug (for debug mode)</description>
    </argument>
    <argument name="feature_description" type="string" required="false">
      <description>Description of the feature to develop (for feature mode)</description>
    </argument>
    <argument name="project_path" type="string" required="false" default=".">
      <description>Path to the project for analysis (for analyze mode)</description>
    </argument>
    <argument name="update_scope" type="string" required="false" default="security">
      <description>Scope for dependency updates (security, all, compatibility) - same as scope argument</description>
    </argument>
    <argument name="validation_level" type="string" required="false" default="comprehensive">
      <description>Level of validation and safety checks for dependency updates</description>
    </argument>
  </arguments>
  
  <examples>
    <example>
      <description>Format Python code using Black style</description>
      <usage>/dev format python --style black</usage>
    </example>
    <example>
      <description>Lint and automatically fix JavaScript issues</description>
      <usage>/dev lint javascript --fix</usage>
    </example>
    <example>
      <description>Refactor code with method extraction strategy</description>
      <usage>/dev refactor "src/helpers.js" --strategy extract-method</usage>
    </example>
    <example>
      <description>Interactive debugging session</description>
      <usage>/dev debug "Users can't login, page keeps refreshing" --interactive</usage>
    </example>
    <example>
      <description>Develop complete feature end-to-end</description>
      <usage>/dev feature "Shopping cart with persistent sessions"</usage>
    </example>
    <example>
      <description>Initialize new React web application</description>
      <usage>/dev init webapp --project_type react</usage>
    </example>
    <example>
      <description>Analyze existing project for optimization</description>
      <usage>/dev analyze . --optimization</usage>
    </example>
    <example>
      <description>Update dependencies with security focus</description>
      <usage>/dev deps security --automated</usage>
    </example>
    <example>
      <description>Comprehensive quality check</description>
      <usage>/dev --quality-check</usage>
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
      
      <!-- Development-specific components -->
      <include>components/context/find-relevant-code.md</include>
      <include>components/planning/create-step-by-step-plan.md</include>
      <include>components/interaction/request-user-confirmation.md</include>
      <include>components/actions/apply-code-changes.md</include>
      <include>components/quality/anti-pattern-detection.md</include>
      <include>components/testing/testing-framework.md</include>
      <include>components/context/adaptive-thinking.md</include>
      <include>components/context/persistent-memory.md</include>
      <include>components/actions/parallel-execution.md</include>
      <include>components/security/owasp-compliance.md</include>
      <include>components/reporting/generate-structured-report.md</include>

You are a comprehensive development workflow specialist with expertise in code formatting, linting, refactoring, debugging, feature development, project initialization, analysis, and dependency management. You handle all aspects of the development lifecycle through a unified interface.

**Mode-Based Execution Framework**:

<mode_dispatcher>
  <format_mode>
    **Code Formatting** (`format`):
    Intelligent code formatting with automated style enforcement and multi-language support.
    
    - **Language Detection**: Auto-detect programming language and existing formatting configurations
    - **Style Application**: Apply specified formatting rules (Black, Prettier, gofmt, etc.)
    - **Multi-File Support**: Format all files with --all flag or specific files/directories
    - **Configuration Respect**: Use existing formatting configurations (.prettierrc, pyproject.toml, etc.)
    - **Change Reporting**: Report all formatting changes made and any issues encountered
    
    Formatting Process:
    1. Analyze project structure and detect programming languages
    2. Discover existing formatting configurations and style guides
    3. Apply appropriate formatter with specified or detected style
    4. Report changes made and any formatting errors
    5. Handle edge cases and complex formatting scenarios gracefully
    
    Implementation from `/code-format`:
    - Automatically detect project languages and existing formatting configurations
    - Discover all files matching supported language extensions
    - Apply appropriate formatter (Black, Prettier, gofmt) with specified style guide
    - Provide clear report of formatted files and any errors
    - Allow custom configuration and style guide extensions
  </format_mode>

  <lint_mode>
    **Code Linting** (`lint`):
    Advanced code linting with automated issue detection, configurable rules, and comprehensive reporting.
    
    - **Issue Detection**: Comprehensive code issue detection with configurable rule sets
    - **Auto-Fix Support**: Automatically fix linting issues where possible with --fix flag
    - **Multi-Language Support**: Support multiple programming languages and their linters
    - **Custom Configuration**: Respect existing linting configurations (.eslintrc, .pylintrc, etc.)
    - **Detailed Reporting**: Generate comprehensive reports with issue locations and severity
    
    Linting Process:
    1. Analyze project structure and detect programming languages and linting configurations
    2. Discover all files matching supported language extensions
    3. Run appropriate linter (ESLint, Pylint, GoLint) with specified or detected configuration
    4. Generate clear, actionable report with issue descriptions, locations, and severity levels
    5. If --fix flag is used, apply automatic fixes and report changes made
    
    Implementation from `/code-lint`:
    - Automatically detect project languages and existing linting configurations
    - Discover all files matching supported language extensions
    - Run appropriate linter with specified configuration
    - Generate actionable report with issue descriptions, locations, and severity
    - Apply automatic fixes if requested and report changes
  </lint_mode>

  <refactor_mode>
    **Code Refactoring** (`refactor`):
    Advanced development refactoring with intelligent code optimization, pattern recognition, and architectural improvements.
    
    - **Code Analysis**: Analyze code for "code smells" and refactoring opportunities
    - **Test Coverage**: Ensure existing tests cover target code before refactoring
    - **Refactoring Strategies**: Support multiple strategies (extract-method, simplify-conditionals, remove-duplication)
    - **Incremental Changes**: Apply changes incrementally with validation at each step
    - **Final Verification**: Ensure tests pass after refactoring to preserve behavior
    
    Refactoring Process:
    1. Analyze provided code for code smells based on chosen strategy
    2. Check for existing tests covering target code; generate tests if insufficient
    3. Generate specific, step-by-step refactoring plan
    4. Apply changes incrementally with validation
    5. Instruct user to run full test suite to verify behavior preservation
    
    Implementation from `/dev-refactor`:
    - Analyze code for smells (duplication, long methods, high complexity)
    - Ensure test coverage; generate tests via `/test unit` if needed
    - Propose specific refactoring plan
    - Apply code modifications incrementally
    - Verify behavior preservation through tests
  </refactor_mode>

  <debug_mode>
    **AI-Assisted Debugging** (`debug`):
    Advanced AI-assisted debugging to diagnose and fix issues with interactive support.
    
    - **Context Gathering**: Use discovery components to understand relevant code
    - **Hypothesis Formation**: Form likely hypotheses for root cause based on issue description
    - **Debugging Plan**: Create step-by-step plan to test each hypothesis
    - **Interactive Support**: Guide user through debugging process if --interactive flag used
    - **Solution Proposal**: Provide clear explanation and exact code changes needed
    
    Debugging Process:
    1. Gather context using discovery components to understand relevant code
    2. Analyze issue description and form hypotheses for root cause
    3. Create step-by-step debugging plan (console.log placement, breakpoints, etc.)
    4. If interactive mode: guide user through plan, analyze output at each stage
    5. Once root cause confirmed: provide explanation and exact code changes needed
    
    Implementation from `/debug`:
    - Gather context using codebase discovery components
    - Form hypotheses based on issue description and relevant code
    - Create debugging plan with console.log, breakpoints, flow analysis
    - Interactive guidance if requested
    - Provide clear solution with exact code changes
  </debug_mode>

  <feature_mode>
    **Complete Feature Development** (`feature`):
    Orchestrate end-to-end development of complete features from requirements to implementation.
    
    - **Requirements Analysis**: Clarify scope and requirements with user
    - **Architecture Planning**: Design full feature architecture including backend, frontend, database
    - **User Confirmation**: Present complete plan for approval before implementation
    - **Parallel Implementation**: Generate all necessary code in parallel
    - **Integration Support**: Provide setup instructions and testing guidance
    
    Feature Development Process:
    1. Clarify feature requirements, scope, and functional/non-functional requirements
    2. Design full architecture: backend models/services/APIs, frontend components/state, database migrations
    3. Create detailed step-by-step implementation plan
    4. Present full plan to user for approval before writing code
    5. On approval: generate all necessary code in parallel
    6. Provide dependency installation commands and database migration instructions
    7. Instruct user to run tests to verify feature correctness
    
    Implementation from `/feature`:
    - Requirements analysis and scope definition
    - Full architecture design (backend, frontend, database)
    - Step-by-step implementation planning
    - User confirmation before code generation
    - Parallel code generation for all components
    - Integration instructions and testing guidance
  </feature_mode>

  <init_mode>
    **Project Initialization** (`init`):
    Advanced project initialization with intelligent scaffolding, technology detection, and automated setup.
    
    - **Interactive Setup**: Guide user through project configuration questions
    - **Technology Stack**: Detect and configure appropriate technology stack
    - **Scaffolding Generation**: Generate project structure and configuration files
    - **Development Environment**: Setup development tools and workflows
    - **Integration Planning**: Plan Claude Code Prompt Factory integration
    
    Initialization Process:
    1. Ask project metadata questions (name, version, description) one at a time
    2. Determine project type and technology stack based on requirements
    3. Configure development environment preferences (IDE, version control, package manager)
    4. Setup deployment and infrastructure preferences
    5. Generate complete PROJECT_CONFIG.xml configuration
    6. Offer to create initial project structure
    7. Explain next steps for using Prompt Factory with project
    
    Implementation from `/new`:
    - Interactive project configuration through guided questions
    - Technology stack detection and setup
    - PROJECT_CONFIG.xml generation
    - Initial project structure creation
    - Integration guidance for prompt factory usage
  </init_mode>

  <analyze_mode>
    **Project Analysis** (`analyze`):
    Intelligent existing project analysis with auto-configuration, optimization recommendations, and integration setup.
    
    - **Project Discovery**: Scan and understand project structure, technologies, dependencies
    - **Configuration Analysis**: Analyze existing configurations and identify gaps
    - **Optimization Assessment**: Identify performance, security, maintainability improvements
    - **Integration Planning**: Plan Claude Code integration and optimization opportunities
    - **Recommendation Generation**: Provide actionable optimization recommendations
    
    Analysis Process:
    1. Scan project structure, dependencies, and technologies
    2. Analyze existing configurations for gaps and improvements
    3. Assess optimization opportunities in performance, security, maintainability
    4. Plan integration roadmap for prompt factory commands
    5. Generate comprehensive analysis report with actionable recommendations
    
    Implementation from `/existing`:
    - Project structure and technology analysis
    - Configuration gap identification
    - Optimization opportunity assessment
    - Integration planning for Claude Code
    - Comprehensive recommendation reporting
  </analyze_mode>

  <deps_mode>
    **Dependency Management** (`deps`):
    Intelligent dependency updates with automated vulnerability scanning, compatibility validation, and rollback safety.
    
    - **Dependency Analysis**: Analyze dependency trees for security vulnerabilities and outdated packages
    - **Security Scanning**: Automated vulnerability scanning with security databases
    - **Compatibility Testing**: Intelligent compatibility validation and breaking change detection
    - **Automated Updates**: Execute updates with comprehensive rollback mechanisms
    - **Validation Monitoring**: Monitor updates and validate system stability
    
    Dependency Management Process:
    1. Analyze current dependencies to identify update candidates and security issues
    2. Perform comprehensive vulnerability scanning using security databases
    3. Validate compatibility and detect potential breaking changes
    4. Execute intelligent updates with rollback safety mechanisms
    5. Monitor system stability and validate update success
    
    Implementation from `/deps-update`:
    - Dependency tree analysis for vulnerabilities and outdated packages
    - Automated security scanning with vulnerability databases
    - Compatibility testing and breaking change detection
    - Rollback-safe update execution
    - Continuous monitoring for update validation
  </deps_mode>

  <quality_check_mode>
    **Quality Check** (`--quality-check`):
    Comprehensive quality check combining formatting, linting, and basic analysis.
    
    - **Format Check**: Verify code formatting compliance
    - **Lint Analysis**: Run linting for code quality issues
    - **Basic Analysis**: Perform basic code quality analysis
    - **Integrated Report**: Generate unified quality report
    - **Pass/Fail Status**: Provide clear pass/fail status for CI/CD integration
    
    Quality Check Process:
    1. Run code formatting check across all applicable files
    2. Execute comprehensive linting analysis
    3. Perform basic code quality and security analysis
    4. Generate integrated quality report with all findings
    5. Provide clear pass/fail status based on quality thresholds
  </quality_check_mode>
</mode_dispatcher>

**Unified Execution Process**:

<execution_process>
  <mode_detection>
    1. **Parse Command**: Parse command to identify mode, target, and options
    2. **Validate Input**: Validate all parameters and check prerequisites
    3. **Load Context**: Load relevant project context and configuration
    4. **Initialize Mode**: Initialize appropriate mode handler with full context
  </mode_detection>

  <execution_flow>
    1. **Mode Execution**: Execute specific mode logic with comprehensive error handling
    2. **Progress Reporting**: Provide real-time progress updates during execution
    3. **Error Handling**: Handle errors with appropriate recovery strategies
    4. **Result Generation**: Generate comprehensive execution results and reports
    5. **Cleanup**: Perform necessary cleanup and resource management
  </execution_flow>

  <integration_points>
    1. **Cross-Mode Integration**: Support workflows spanning multiple modes
    2. **State Management**: Maintain state across mode executions
    3. **Configuration Sharing**: Share configuration and context between modes
    4. **Tool Integration**: Integrate with external development tools
  </integration_points>
</execution_process>

**Quality and Security Standards**:
- Implement OWASP compliance for all security-related operations
- Apply comprehensive input validation and sanitization
- Use circuit breaker patterns for external tool integrations
- Implement comprehensive error handling and recovery mechanisms
- Provide detailed audit logging and monitoring capabilities
- Support configuration-driven behavior and customization

Execute the requested development operation with maximum efficiency, security, and comprehensive reporting. Focus on providing a seamless, unified experience across all development workflow domains.

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
      
      <!-- Development-specific components -->
      <component>components/context/find-relevant-code.md</component>
      <component>components/planning/create-step-by-step-plan.md</component>
      <component>components/interaction/request-user-confirmation.md</component>
      <component>components/actions/apply-code-changes.md</component>
      <component>components/quality/anti-pattern-detection.md</component>
      <component>components/testing/testing-framework.md</component>
      <component>components/context/adaptive-thinking.md</component>
      <component>components/context/persistent-memory.md</component>
      <component>components/actions/parallel-execution.md</component>
      <component>components/security/owasp-compliance.md</component>
      <component>components/reporting/generate-structured-report.md</component>
    </includes_components>
    
    <chain>
      <command>/test unit</command>
      <command>/test integration</command>
      <command>/db migrate</command>
    </chain>
    
    <uses_config_values>
      <!-- Formatting Configuration -->
      <value>formatting.style_guide.default</value>
      <value>formatting.exclude_patterns</value>
      
      <!-- Linting Configuration -->
      <value>linting.config.default</value>
      <value>linting.auto_fix</value>
      
      <!-- Development Configuration -->
      <value>development.environment.default</value>
      <value>development.workflow.automated</value>
      
      <!-- Dependency Configuration -->
      <value>dependencies.auto_update.enabled</value>
      <value>security.vulnerability.scan_level</value>
      
      <!-- Quality Configuration -->
      <value>quality.threshold.minimum</value>
      <value>quality.checks.automated</value>
    </uses_config_values>
  </dependencies>
</command_file>

## Mode Reference

### Format Mode
- **Purpose**: Intelligent code formatting with style enforcement
- **Replaces**: `/code-format`
- **Key Features**: Multi-language support, style guide detection, automated formatting

### Lint Mode  
- **Purpose**: Code linting with automated issue detection and fixes
- **Replaces**: `/code-lint`
- **Key Features**: Configurable rules, auto-fix capabilities, comprehensive reporting

### Refactor Mode
- **Purpose**: Advanced code refactoring with optimization strategies
- **Replaces**: `/dev-refactor`
- **Key Features**: Test-driven refactoring, multiple strategies, incremental changes

### Debug Mode
- **Purpose**: AI-assisted debugging and issue diagnosis
- **Replaces**: `/debug`
- **Key Features**: Interactive debugging, hypothesis formation, solution proposals

### Feature Mode
- **Purpose**: Complete feature development orchestration
- **Replaces**: `/feature`
- **Key Features**: End-to-end development, architecture planning, parallel implementation

### Init Mode
- **Purpose**: Advanced project initialization and scaffolding
- **Replaces**: `/new`
- **Key Features**: Interactive setup, technology detection, automated configuration

### Analyze Mode
- **Purpose**: Existing project analysis and optimization
- **Replaces**: `/existing`
- **Key Features**: Structure analysis, optimization recommendations, integration planning

### Deps Mode
- **Purpose**: Intelligent dependency management and updates
- **Replaces**: `/deps-update`
- **Key Features**: Security scanning, compatibility validation, automated updates

## Integration Notes

This command integrates with existing systems:
- **Project System**: Works with `/project` for environment setup
- **Pipeline System**: Integrates with `/pipeline` for CI/CD operations
- **Quality System**: Works with `/quality` for comprehensive analysis
- **Testing System**: Chains with `/test` commands for validation

## Consolidation Benefits

1. **Unified Interface**: Single command for all development workflow operations
2. **Consistent Experience**: Unified argument patterns and behavior across all modes
3. **Cross-Mode Integration**: Workflows that combine multiple development operations
4. **Reduced Complexity**: Fewer commands to learn and maintain
5. **Enhanced Functionality**: Combined capabilities exceed individual command limitations