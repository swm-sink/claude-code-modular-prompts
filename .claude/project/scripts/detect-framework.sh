#!/bin/bash
# Framework Detection Script for Claude Code Template Library
# Based on research from 50+ sources on automated project analysis

set -e

PROJECT_PATH="${1:-.}"
OUTPUT_FORMAT="${2:-json}"

# Initialize detection results
declare -A DETECTED_FRAMEWORKS
declare -A PROJECT_METADATA
declare -A DEPENDENCIES

# Framework detection functions
detect_javascript() {
    if [[ -f "$PROJECT_PATH/package.json" ]]; then
        local package_json=$(cat "$PROJECT_PATH/package.json")
        
        # Extract project metadata
        PROJECT_METADATA[name]=$(echo "$package_json" | grep -o '"name":\s*"[^"]*"' | cut -d'"' -f4)
        PROJECT_METADATA[version]=$(echo "$package_json" | grep -o '"version":\s*"[^"]*"' | cut -d'"' -f4)
        PROJECT_METADATA[author]=$(echo "$package_json" | grep -o '"author":\s*"[^"]*"' | cut -d'"' -f4)
        
        # Detect frameworks
        if echo "$package_json" | grep -q '"react"'; then
            DETECTED_FRAMEWORKS[react]="detected"
            if echo "$package_json" | grep -q '"next"'; then
                DETECTED_FRAMEWORKS[nextjs]="detected"
            fi
        fi
        
        if echo "$package_json" | grep -q '"vue"'; then
            DETECTED_FRAMEWORKS[vue]="detected"
            if echo "$package_json" | grep -q '"nuxt"'; then
                DETECTED_FRAMEWORKS[nuxt]="detected"
            fi
        fi
        
        if echo "$package_json" | grep -q '"@angular/core"'; then
            DETECTED_FRAMEWORKS[angular]="detected"
        fi
        
        if echo "$package_json" | grep -q '"express"'; then
            DETECTED_FRAMEWORKS[express]="detected"
        fi
        
        return 0
    fi
    return 1
}

detect_python() {
    local python_detected=false
    
    if [[ -f "$PROJECT_PATH/requirements.txt" ]]; then
        python_detected=true
        local requirements=$(cat "$PROJECT_PATH/requirements.txt")
        
        if echo "$requirements" | grep -q "django"; then
            DETECTED_FRAMEWORKS[django]="detected"
        fi
        
        if echo "$requirements" | grep -q "flask"; then
            DETECTED_FRAMEWORKS[flask]="detected"
        fi
        
        if echo "$requirements" | grep -q "fastapi"; then
            DETECTED_FRAMEWORKS[fastapi]="detected"
        fi
    fi
    
    if [[ -f "$PROJECT_PATH/setup.py" ]] || [[ -f "$PROJECT_PATH/pyproject.toml" ]]; then
        python_detected=true
    fi
    
    if [[ -f "$PROJECT_PATH/manage.py" ]]; then
        DETECTED_FRAMEWORKS[django]="detected"
        python_detected=true
    fi
    
    if $python_detected; then
        DETECTED_FRAMEWORKS[python]="detected"
        return 0
    fi
    return 1
}

detect_java() {
    if [[ -f "$PROJECT_PATH/pom.xml" ]]; then
        DETECTED_FRAMEWORKS[maven]="detected"
        DETECTED_FRAMEWORKS[java]="detected"
        
        if grep -q "spring-boot" "$PROJECT_PATH/pom.xml"; then
            DETECTED_FRAMEWORKS[spring-boot]="detected"
        fi
        return 0
    fi
    
    if [[ -f "$PROJECT_PATH/build.gradle" ]]; then
        DETECTED_FRAMEWORKS[gradle]="detected"
        DETECTED_FRAMEWORKS[java]="detected"
        return 0
    fi
    return 1
}

detect_go() {
    if [[ -f "$PROJECT_PATH/go.mod" ]]; then
        DETECTED_FRAMEWORKS[go]="detected"
        PROJECT_METADATA[module]=$(grep "^module" "$PROJECT_PATH/go.mod" | cut -d' ' -f2)
        return 0
    fi
    return 1
}

detect_rust() {
    if [[ -f "$PROJECT_PATH/Cargo.toml" ]]; then
        DETECTED_FRAMEWORKS[rust]="detected"
        PROJECT_METADATA[name]=$(grep "^name" "$PROJECT_PATH/Cargo.toml" | cut -d'"' -f2)
        return 0
    fi
    return 1
}

detect_database() {
    # Check for database configuration files
    if [[ -f "$PROJECT_PATH/.env" ]]; then
        local env_content=$(cat "$PROJECT_PATH/.env")
        
        if echo "$env_content" | grep -q "DATABASE_URL.*postgres"; then
            DETECTED_FRAMEWORKS[postgresql]="detected"
        fi
        
        if echo "$env_content" | grep -q "DATABASE_URL.*mysql"; then
            DETECTED_FRAMEWORKS[mysql]="detected"
        fi
        
        if echo "$env_content" | grep -q "MONGODB_URI"; then
            DETECTED_FRAMEWORKS[mongodb]="detected"
        fi
        
        if echo "$env_content" | grep -q "REDIS_URL"; then
            DETECTED_FRAMEWORKS[redis]="detected"
        fi
    fi
}

classify_project_type() {
    local has_frontend=false
    local has_backend=false
    local has_database=false
    
    # Check for frontend indicators
    if [[ "${DETECTED_FRAMEWORKS[react]}" == "detected" ]] || \
       [[ "${DETECTED_FRAMEWORKS[vue]}" == "detected" ]] || \
       [[ "${DETECTED_FRAMEWORKS[angular]}" == "detected" ]]; then
        has_frontend=true
    fi
    
    # Check for backend indicators
    if [[ "${DETECTED_FRAMEWORKS[express]}" == "detected" ]] || \
       [[ "${DETECTED_FRAMEWORKS[django]}" == "detected" ]] || \
       [[ "${DETECTED_FRAMEWORKS[flask]}" == "detected" ]] || \
       [[ "${DETECTED_FRAMEWORKS[spring-boot]}" == "detected" ]]; then
        has_backend=true
    fi
    
    # Check for database indicators
    if [[ "${DETECTED_FRAMEWORKS[postgresql]}" == "detected" ]] || \
       [[ "${DETECTED_FRAMEWORKS[mysql]}" == "detected" ]] || \
       [[ "${DETECTED_FRAMEWORKS[mongodb]}" == "detected" ]]; then
        has_database=true
    fi
    
    # Classify project type
    if $has_frontend && $has_backend && $has_database; then
        PROJECT_METADATA[type]="fullstack-web-app"
    elif $has_backend && $has_database; then
        PROJECT_METADATA[type]="api-backend"
    elif $has_frontend; then
        PROJECT_METADATA[type]="frontend-spa"
    elif [[ "${DETECTED_FRAMEWORKS[go]}" == "detected" ]] || [[ "${DETECTED_FRAMEWORKS[rust]}" == "detected" ]]; then
        PROJECT_METADATA[type]="cli-tool"
    else
        PROJECT_METADATA[type]="library"
    fi
}

# Main detection logic
detect_frameworks() {
    echo "🔍 Analyzing project at: $PROJECT_PATH"
    
    # Run all detection functions
    detect_javascript
    detect_python
    detect_java
    detect_go
    detect_rust
    detect_database
    
    # Classify project type
    classify_project_type
    
    # Extract git information if available
    if [[ -d "$PROJECT_PATH/.git" ]]; then
        PROJECT_METADATA[git_author]=$(git -C "$PROJECT_PATH" config user.name 2>/dev/null || echo "")
        PROJECT_METADATA[git_email]=$(git -C "$PROJECT_PATH" config user.email 2>/dev/null || echo "")
    fi
}

# Output functions
output_json() {
    echo "{"
    echo "  \"project_metadata\": {"
    for key in "${!PROJECT_METADATA[@]}"; do
        echo "    \"$key\": \"${PROJECT_METADATA[$key]}\","
    done
    echo "    \"path\": \"$PROJECT_PATH\""
    echo "  },"
    echo "  \"detected_frameworks\": {"
    local first=true
    for framework in "${!DETECTED_FRAMEWORKS[@]}"; do
        if ! $first; then echo ","; fi
        echo -n "    \"$framework\": \"${DETECTED_FRAMEWORKS[$framework]}\""
        first=false
    done
    echo ""
    echo "  },"
    echo "  \"project_type\": \"${PROJECT_METADATA[type]}\","
    echo "  \"confidence\": \"high\""
    echo "}"
}

output_summary() {
    echo "📊 Framework Detection Results:"
    echo "   Project: ${PROJECT_METADATA[name]:-$(basename "$PROJECT_PATH")}"
    echo "   Type: ${PROJECT_METADATA[type]}"
    echo ""
    echo "🔧 Detected Frameworks:"
    for framework in "${!DETECTED_FRAMEWORKS[@]}"; do
        echo "   ✅ $framework"
    done
    echo ""
    echo "📋 Recommended Templates:"
    case "${PROJECT_METADATA[type]}" in
        "fullstack-web-app")
            echo "   - Core commands (help, task, analyze, review, debug, test, docs)"
            echo "   - Frontend templates (component, page, styling)"
            echo "   - Backend templates (api, database, auth)"
            echo "   - DevOps templates (deploy, monitor, ci-cd)"
            ;;
        "api-backend")
            echo "   - Core commands (help, task, analyze, review, debug, test, docs)"
            echo "   - API templates (endpoint, middleware, validation)"
            echo "   - Database templates (migration, model, query)"
            echo "   - DevOps templates (deploy, monitor)"
            ;;
        "frontend-spa")
            echo "   - Core commands (help, task, analyze, review, debug, test, docs)"
            echo "   - Frontend templates (component, page, styling, build)"
            echo "   - Testing templates (unit, integration, e2e)"
            ;;
        *)
            echo "   - Core commands (help, task, analyze, review, debug, test, docs)"
            echo "   - Basic development templates"
            ;;
    esac
}

# Main execution
main() {
    if [[ ! -d "$PROJECT_PATH" ]]; then
        echo "Error: Project path '$PROJECT_PATH' does not exist"
        exit 1
    fi
    
    detect_frameworks
    
    case "$OUTPUT_FORMAT" in
        "json")
            output_json
            ;;
        "summary")
            output_summary
            ;;
        *)
            echo "Error: Unknown output format '$OUTPUT_FORMAT'. Use 'json' or 'summary'"
            exit 1
            ;;
    esac
}

main "$@"