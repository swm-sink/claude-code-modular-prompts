#!/bin/bash
# WORKING Configuration Monitor
# Demonstrates FUNCTIONAL health monitoring

monitor_config_health() {
    local config_file="$1"
    local health_score=100
    
    echo "=== CONFIGURATION HEALTH CHECK: $config_file ==="
    
    # Track parameter usage
    echo "Analyzing parameter usage..."
    if [ -f "$config_file" ]; then
        # Count parameters with actual values vs placeholders/auto-detect
        used_params=$(grep -v "auto-detect\|TODO\|\[.*\]" "$config_file" | grep -c "<[^/].*>.*<")
        total_params=$(grep -c "<[^/].*>" "$config_file")
        
        if [ $total_params -gt 0 ]; then
            usage_rate=$((used_params * 100 / total_params))
            echo "✅ Parameter Usage: $usage_rate% ($used_params/$total_params)"
            
            if [ $usage_rate -lt 70 ]; then
                echo "⚠️  LOW USAGE: Consider switching to simpler tier"
                health_score=$((health_score - 20))
            fi
        fi
    fi
    
    # Analyze complexity
    echo "Analyzing complexity..."
    if [ -f "$config_file" ]; then
        complexity=$(wc -l < "$config_file")
        echo "✅ Configuration Size: $complexity lines"
        
        if [ $complexity -gt 150 ]; then
            echo "⚠️  HIGH COMPLEXITY: $complexity lines (optimal: <100)"
            health_score=$((health_score - 15))
        elif [ $complexity -gt 100 ]; then
            echo "⚠️  MODERATE COMPLEXITY: $complexity lines (consider optimization)"
            health_score=$((health_score - 5))
        else
            echo "✅ OPTIMAL COMPLEXITY: Configuration size is manageable"
        fi
    fi
    
    # Check for common issues
    echo "Checking for common issues..."
    if grep -q "auto-detect" "$config_file" 2>/dev/null; then
        auto_detect_count=$(grep -c "auto-detect" "$config_file")
        echo "⚠️  AUTO-DETECT REMAINING: $auto_detect_count parameters need configuration"
        health_score=$((health_score - 5))
    else
        echo "✅ FULLY CONFIGURED: No auto-detect placeholders remaining"
    fi
    
    # Generate recommendations
    echo ""
    echo "=== OPTIMIZATION RECOMMENDATIONS ==="
    if [ $health_score -lt 70 ]; then
        echo "🎯 CRITICAL: Switch to MINIMAL tier (reduce complexity by 60%)"
    elif [ $health_score -lt 85 ]; then
        echo "🎯 RECOMMENDED: Optimize current configuration (remove unused parameters)"
    else
        echo "✅ EXCELLENT: Configuration is optimal for your needs"
    fi
    
    echo ""
    echo "🏥 Overall Health Score: $health_score/100"
    
    # Performance recommendations
    if [ $complexity -lt 50 ]; then
        echo "⚡ PERFORMANCE: Excellent (< 50ms validation time)"
    elif [ $complexity -lt 100 ]; then
        echo "⚡ PERFORMANCE: Good (< 100ms validation time)"
    else
        echo "⚡ PERFORMANCE: Consider optimization for faster startup"
    fi
}

# Test monitoring on different configs
echo "Monitoring minimal configuration:"
monitor_config_health "test_minimal_config.xml"

echo ""
echo "Monitoring broken configuration:"
monitor_config_health "broken_config.xml"