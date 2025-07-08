| version | last_updated | status |
|---------|--------------|--------|
| 1.0.0   | 2025-07-08   | stable |

# Performance Gates Module

────────────────────────────────────────────────────────────────────────────────

```xml
<module name="performance_gates" category="quality">
  
  <purpose>
    Performance benchmark verification system with p95 <200ms requirement, automated measurement methodology, and regression prevention.
  </purpose>
  
  <thinking_pattern enforcement="MANDATORY">
    <step>1. Establish performance baseline for current system</step>
    <step>2. Define performance targets and SLA requirements</step>
    <step>3. Create comprehensive performance test suite</step>
    <step>4. Execute performance benchmarks with load simulation</step>
    <step>5. Analyze results against established thresholds</step>
    <step>6. Detect performance regressions automatically</step>
    <step>7. Generate performance compliance certificate</step>
    <step>8. Block deployment if performance gates fail</step>
  </thinking_pattern>
  
  <trigger_conditions>
    <condition type="automatic">Pre-merge hooks, deployment gates, performance testing</condition>
    <condition type="explicit">Performance verification requests, SLA validation</condition>
  </trigger_conditions>
  
  <implementation>
    
    <performance_benchmarking_engine>
      
      <benchmark_categories>
        <category name="API_PERFORMANCE" priority="CRITICAL">
          <metrics>
            <metric name="response_time_p50" target="<100ms" threshold="150ms" />
            <metric name="response_time_p95" target="<200ms" threshold="300ms" />
            <metric name="response_time_p99" target="<500ms" threshold="1000ms" />
            <metric name="requests_per_second" target=">1000" threshold="500" />
            <metric name="error_rate" target="<1%" threshold="5%" />
          </metrics>
          <test_scenarios>
            <scenario name="normal_load">Sustained load at 70% capacity for 10 minutes</scenario>
            <scenario name="peak_load">Burst load at 150% capacity for 2 minutes</scenario>
            <scenario name="stress_test">Gradual load increase to failure point</scenario>
          </test_scenarios>
        </category>
        
        <category name="DATABASE_PERFORMANCE" priority="HIGH">
          <metrics>
            <metric name="query_response_time" target="<10ms" threshold="50ms" />
            <metric name="transaction_completion" target="<50ms" threshold="100ms" />
            <metric name="connection_pool_efficiency" target=">95%" threshold="80%" />
            <metric name="deadlock_rate" target="<0.1%" threshold="1%" />
          </metrics>
          <test_scenarios>
            <scenario name="concurrent_reads">1000 concurrent read operations</scenario>
            <scenario name="write_intensive">100 concurrent write operations</scenario>
            <scenario name="mixed_workload">70% reads, 30% writes sustained</scenario>
          </test_scenarios>
        </category>
        
        <category name="MEMORY_PERFORMANCE" priority="HIGH">
          <metrics>
            <metric name="memory_usage" target="<512MB" threshold="1GB" />
            <metric name="garbage_collection_time" target="<10ms" threshold="50ms" />
            <metric name="memory_leak_rate" target="0MB/hour" threshold="10MB/hour" />
            <metric name="allocation_rate" target="stable" threshold="10x_baseline" />
          </metrics>
          <test_scenarios>
            <scenario name="memory_stress">Process large datasets over 1 hour</scenario>
            <scenario name="gc_pressure">Rapid object allocation and deallocation</scenario>
            <scenario name="long_running">24-hour stability test</scenario>
          </test_scenarios>
        </category>
        
        <category name="FRONTEND_PERFORMANCE" priority="MEDIUM">
          <metrics>
            <metric name="first_contentful_paint" target="<1s" threshold="2s" />
            <metric name="largest_contentful_paint" target="<2.5s" threshold="4s" />
            <metric name="cumulative_layout_shift" target="<0.1" threshold="0.25" />
            <metric name="time_to_interactive" target="<3s" threshold="5s" />
          </metrics>
          <test_scenarios>
            <scenario name="lighthouse_audit">Full lighthouse performance audit</scenario>
            <scenario name="real_user_monitoring">Synthetic user interaction tests</scenario>
            <scenario name="network_throttling">3G and slow connection simulation</scenario>
          </test_scenarios>
        </category>
      </benchmark_categories>
      
      <measurement_infrastructure>
        <load_testing_tools>
          <tool name="apache_bench" use_case="Quick API response time testing">
            <configuration>
              <concurrent_users>100</concurrent_users>
              <test_duration>60s</test_duration>
              <endpoints>All critical API endpoints</endpoints>
            </configuration>
            <command_template>ab -c 100 -t 60 -g results.tsv {endpoint}</command_template>
          </tool>
          
          <tool name="wrk" use_case="High-performance HTTP benchmarking">
            <configuration>
              <threads>12</threads>
              <connections>400</connections>
              <duration>120s</duration>
            </configuration>
            <command_template>wrk -t12 -c400 -d120s --script script.lua {endpoint}</command_template>
          </tool>
          
          <tool name="k6" use_case="Modern load testing with JavaScript">
            <configuration>
              <virtual_users>1000</virtual_users>
              <test_stages>Ramp up, sustain, ramp down</test_stages>
              <scenario_files>Custom test scenarios</scenario_files>
            </configuration>
            <command_template>k6 run --vus 1000 --duration 5m scenario.js</command_template>
          </tool>
          
          <tool name="artillery" use_case="Real-world load simulation">
            <configuration>
              <phases>Multiple load phases</phases>
              <arrival_rate>Dynamic request rates</arrival_rate>
              <payload_files>Realistic data payloads</payload_files>
            </configuration>
            <command_template>artillery run performance-test.yml</command_template>
          </tool>
        </load_testing_tools>
        
        <monitoring_and_profiling>
          <application_monitoring>
            <tool name="prometheus">Metrics collection and alerting</tool>
            <tool name="grafana">Performance visualization dashboards</tool>
            <tool name="jaeger">Distributed tracing for latency analysis</tool>
            <tool name="newrelic">Application performance monitoring</tool>
          </application_monitoring>
          
          <system_monitoring>
            <tool name="htop">Real-time system resource monitoring</tool>
            <tool name="iotop">Disk I/O performance analysis</tool>
            <tool name="netstat">Network connection monitoring</tool>
            <tool name="perf">Linux performance analysis toolkit</tool>
          </system_monitoring>
          
          <database_monitoring>
            <tool name="pg_stat_statements">PostgreSQL query performance</tool>
            <tool name="mysql_slow_log">MySQL slow query analysis</tool>
            <tool name="redis_info">Redis performance metrics</tool>
            <tool name="mongodb_profiler">MongoDB operation profiling</tool>
          </database_monitoring>
        </monitoring_and_profiling>
        
        <automated_testing_framework>
          <baseline_establishment>
            <step>1. Execute performance tests on known-good version</step>
            <step>2. Collect metrics across all categories</step>
            <step>3. Calculate statistical baselines (mean, p95, p99)</step>
            <step>4. Store baseline data with version metadata</step>
            <step>5. Define acceptable variance ranges</step>
          </baseline_establishment>
          
          <regression_detection>
            <algorithm name="statistical_comparison">
              <description>Compare current results to baseline using statistical significance</description>
              <threshold>95% confidence interval for regression detection</threshold>
              <minimum_samples>50 measurements for reliable comparison</minimum_samples>
            </algorithm>
            
            <algorithm name="trend_analysis">
              <description>Analyze performance trends over multiple builds</description>
              <window>Rolling 30-day performance history</window>
              <alert_threshold>3 consecutive degradations</alert_threshold>
            </algorithm>
            
            <algorithm name="percentile_shift">
              <description>Monitor shifts in performance percentile distributions</description>
              <sensitivity>Alert on p95 increase >20% or p99 increase >50%</sensitivity>
              <validation>Require multiple test runs to confirm regression</validation>
            </algorithm>
          </regression_detection>
          
          <automated_test_execution>
            <pre_commit_tests>
              <scope>Fast performance smoke tests</scope>
              <duration>Under 5 minutes</duration>
              <coverage>Critical path performance validation</coverage>
            </pre_commit_tests>
            
            <pre_merge_tests>
              <scope>Comprehensive performance test suite</scope>
              <duration>15-30 minutes</duration>
              <coverage>All performance categories and scenarios</coverage>
            </pre_merge_tests>
            
            <scheduled_tests>
              <frequency>Nightly comprehensive performance runs</frequency>
              <scope>Full regression testing against historical data</scope>
              <reporting>Daily performance health reports</reporting>
            </scheduled_tests>
          </automated_test_execution>
        </automated_testing_framework>
      </measurement_infrastructure>
      
      <performance_gate_enforcement>
        <gate_definitions>
          <gate name="API_RESPONSE_TIME" blocking="true" priority="CRITICAL">
            <requirement>p95 response time under 200ms for all critical endpoints</requirement>
            <measurement>Load test with 100 concurrent users for 2 minutes</measurement>
            <failure_action>Block merge, require optimization</failure_action>
            <evidence_required>Load test results, response time distribution</evidence_required>
          </gate>
          
          <gate name="THROUGHPUT_CAPACITY" blocking="true" priority="HIGH">
            <requirement>Minimum 1000 requests per second sustained</requirement>
            <measurement>Sustained load test at target RPS for 10 minutes</measurement>
            <failure_action>Block deployment, require capacity planning</failure_action>
            <evidence_required>Throughput graphs, resource utilization</evidence_required>
          </gate>
          
          <gate name="MEMORY_EFFICIENCY" blocking="true" priority="HIGH">
            <requirement>Memory usage under 512MB, no memory leaks</requirement>
            <measurement>Extended runtime test with memory profiling</measurement>
            <failure_action>Block deployment, require memory optimization</failure_action>
            <evidence_required>Memory profiling reports, heap dumps</evidence_required>
          </gate>
          
          <gate name="DATABASE_PERFORMANCE" blocking="true" priority="HIGH">
            <requirement>Database queries under 10ms p95, transactions under 50ms</requirement>
            <measurement>Database stress test with concurrent operations</measurement>
            <failure_action>Block merge, require query optimization</failure_action>
            <evidence_required>Query performance logs, execution plans</evidence_required>
          </gate>
          
          <gate name="REGRESSION_PREVENTION" blocking="true" priority="CRITICAL">
            <requirement>No performance regression >20% from baseline</requirement>
            <measurement>Statistical comparison with historical performance data</measurement>
            <failure_action>Block deployment, require performance investigation</failure_action>
            <evidence_required>Regression analysis report, root cause analysis</evidence_required>
          </gate>
        </gate_definitions>
        
        <enforcement_levels>
          <level name="BLOCKING" severity="CRITICAL">
            <condition>Performance gate failure prevents progression</condition>
            <override>Requires architecture team approval with justification</override>
            <escalation>Immediate notification to performance team</escalation>
          </level>
          
          <level name="WARNING" severity="HIGH">
            <condition>Performance degradation detected but within acceptable range</condition>
            <override>Automatic with documentation requirement</override>
            <escalation>Flag for performance team review</escalation>
          </level>
          
          <level name="ADVISORY" severity="MEDIUM">
            <condition>Performance trends suggest future issues</condition>
            <override>No override required</override>
            <escalation>Performance optimization recommendations generated</escalation>
          </level>
        </enforcement_levels>
      </performance_gate_enforcement>
      
    </performance_benchmarking_engine>
    
    <performance_optimization_guidance>
      
      <common_performance_patterns>
        <pattern name="API_OPTIMIZATION">
          <issue>Slow API response times</issue>
          <solutions>
            <solution priority="HIGH">Implement response caching (Redis, Memcached)</solution>
            <solution priority="HIGH">Optimize database queries (indexing, query optimization)</solution>
            <solution priority="MEDIUM">Add request/response compression</solution>
            <solution priority="MEDIUM">Implement connection pooling</solution>
            <solution priority="LOW">Add CDN for static content</solution>
          </solutions>
          <verification>Re-run load tests, confirm p95 improvement</verification>
        </pattern>
        
        <pattern name="DATABASE_OPTIMIZATION">
          <issue>Slow database operations</issue>
          <solutions>
            <solution priority="HIGH">Add missing database indexes</solution>
            <solution priority="HIGH">Optimize N+1 query problems</solution>
            <solution priority="MEDIUM">Implement read replicas for read-heavy workloads</solution>
            <solution priority="MEDIUM">Add database connection pooling</solution>
            <solution priority="LOW">Consider database sharding for scale</solution>
          </solutions>
          <verification>Monitor query execution times, check execution plans</verification>
        </pattern>
        
        <pattern name="MEMORY_OPTIMIZATION">
          <issue>High memory usage or memory leaks</issue>
          <solutions>
            <solution priority="HIGH">Fix memory leaks (object references, event listeners)</solution>
            <solution priority="HIGH">Implement object pooling for frequently created objects</solution>
            <solution priority="MEDIUM">Optimize data structures for memory efficiency</solution>
            <solution priority="MEDIUM">Add garbage collection tuning</solution>
            <solution priority="LOW">Implement lazy loading for large datasets</solution>
          </solutions>
          <verification>Run memory profiling, verify leak absence over time</verification>
        </pattern>
        
        <pattern name="FRONTEND_OPTIMIZATION">
          <issue>Slow page load times or poor user experience</issue>
          <solutions>
            <solution priority="HIGH">Implement code splitting and lazy loading</solution>
            <solution priority="HIGH">Optimize images (WebP, compression, responsive)</solution>
            <solution priority="MEDIUM">Add service worker for caching</solution>
            <solution priority="MEDIUM">Minimize and compress JavaScript/CSS</solution>
            <solution priority="LOW">Implement progressive web app features</solution>
          </solutions>
          <verification>Run Lighthouse audits, measure Core Web Vitals</verification>
        </pattern>
      </common_performance_patterns>
      
      <automated_optimization_suggestions>
        <analysis_engine>
          <profiling_data_analysis>
            <input>Performance profiling results, monitoring data</input>
            <processing>Pattern matching against known optimization opportunities</processing>
            <output>Ranked list of optimization recommendations</output>
          </profiling_data_analysis>
          
          <bottleneck_identification>
            <methodology>Critical path analysis, resource utilization correlation</methodology>
            <hotspot_detection>Identify top 20% of code responsible for 80% of performance issues</hotspot_detection>
            <root_cause_analysis>Trace performance issues to specific code sections</root_cause_analysis>
          </bottleneck_identification>
          
          <optimization_prioritization>
            <impact_assessment>Estimate performance improvement potential</impact_assessment>
            <effort_estimation>Evaluate implementation complexity and time</effort_estimation>
            <risk_analysis>Assess risk of regression or system instability</risk_analysis>
            <roi_calculation>Calculate return on investment for optimization efforts</roi_calculation>
          </optimization_prioritization>
        </analysis_engine>
        
        <recommendation_system>
          <intelligent_suggestions>
            <code_level>Specific code changes for performance improvement</code_level>
            <architecture_level>System design modifications for better performance</architecture_level>
            <infrastructure_level>Deployment and configuration optimizations</infrastructure_level>
            <monitoring_level>Additional monitoring and alerting recommendations</monitoring_level>
          </intelligent_suggestions>
          
          <implementation_guidance>
            <step_by_step>Detailed implementation instructions</step_by_step>
            <code_examples>Working code samples for common optimizations</code_examples>
            <testing_procedures>How to validate optimization effectiveness</testing_procedures>
            <rollback_plans>Safe rollback procedures if optimizations fail</rollback_plans>
          </implementation_guidance>
        </recommendation_system>
      </automated_optimization_guidance>
      
    </performance_optimization_guidance>
    
  </implementation>
  
  <integration_points>
    <depends_on>
      quality/gate-verification.md for quality gate integration
      quality/production-standards.md for performance standards
      development/task-management.md for development workflow integration
      patterns/enforcement-verification.md for checkpoint templates
    </depends_on>
    <provides_to>
      quality/gate-verification.md for performance gate results
      development/task-management.md for performance-aware development
      planning/feature-workflow.md for performance planning
      All commands for performance gate enforcement
    </provides_to>
  </integration_points>
  
</module>
```

────────────────────────────────────────────────────────────────────────────────

## Performance Testing Commands

```bash
#!/bin/bash
# Performance Gates Engine

# Global configuration
PERFORMANCE_EVIDENCE_DIR="evidence/performance"
PERFORMANCE_CONFIG_FILE=".performance_gates.json"
PERFORMANCE_BASELINE_DIR="baselines/performance"

# Initialize performance testing for a task
init_performance_testing() {
    local task_id=$1
    local test_environment=${2:-"local"}
    
    echo "⚡ Initializing Performance Testing for task: $task_id"
    
    # Create evidence directory
    local evidence_dir="$PERFORMANCE_EVIDENCE_DIR/$task_id"
    mkdir -p "$evidence_dir"
    mkdir -p "$PERFORMANCE_BASELINE_DIR"
    
    # Initialize performance configuration
    cat > "$PERFORMANCE_CONFIG_FILE" << EOF
{
  "task_id": "$task_id",
  "test_environment": "$test_environment",
  "evidence_dir": "$evidence_dir",
  "baseline_version": "$(git rev-parse HEAD)",
  "performance_targets": {
    "api_response_p95": 200,
    "api_response_p99": 500,
    "requests_per_second": 1000,
    "memory_usage_mb": 512,
    "database_query_p95": 10
  },
  "test_configuration": {
    "load_test_duration": 120,
    "concurrent_users": 100,
    "ramp_up_time": 30
  },
  "initialized_at": "$(date -u +%Y-%m-%dT%H:%M:%S.000Z)"
}
EOF
    
    echo "✅ Performance testing initialized"
    echo "📁 Evidence directory: $evidence_dir"
    echo "🎯 Performance targets loaded"
}

# Execute comprehensive performance gate verification
execute_performance_gates() {
    local task_id=$1
    local gate_profile=${2:-"standard"}  # minimal, standard, comprehensive
    
    echo "🚦 Executing Performance Gates for task: $task_id"
    
    local evidence_dir="$PERFORMANCE_EVIDENCE_DIR/$task_id"
    local timestamp=$(date +%Y%m%d-%H%M%S)
    local overall_status="PASS"
    
    # Load configuration
    if [[ ! -f "$PERFORMANCE_CONFIG_FILE" ]]; then
        echo "❌ Performance configuration not found. Run init_performance_testing first."
        return 1
    fi
    
    local config=$(cat "$PERFORMANCE_CONFIG_FILE")
    local api_response_target=$(echo "$config" | jq -r '.performance_targets.api_response_p95')
    local rps_target=$(echo "$config" | jq -r '.performance_targets.requests_per_second')
    local memory_target=$(echo "$config" | jq -r '.performance_targets.memory_usage_mb')
    
    # Execute performance test gates
    echo "🔍 Running API Performance Gate..."
    if execute_api_performance_gate "$task_id" "$evidence_dir" "$api_response_target"; then
        echo "✅ API Performance Gate: PASSED"
    else
        echo "❌ API Performance Gate: FAILED"
        overall_status="FAIL"
    fi
    
    echo "🔍 Running Throughput Performance Gate..."
    if execute_throughput_gate "$task_id" "$evidence_dir" "$rps_target"; then
        echo "✅ Throughput Gate: PASSED"
    else
        echo "❌ Throughput Gate: FAILED"
        overall_status="FAIL"
    fi
    
    echo "🔍 Running Memory Performance Gate..."
    if execute_memory_gate "$task_id" "$evidence_dir" "$memory_target"; then
        echo "✅ Memory Gate: PASSED"
    else
        echo "❌ Memory Gate: FAILED"
        overall_status="FAIL"
    fi
    
    if [[ "$gate_profile" != "minimal" ]]; then
        echo "🔍 Running Database Performance Gate..."
        if execute_database_gate "$task_id" "$evidence_dir"; then
            echo "✅ Database Gate: PASSED"
        else
            echo "❌ Database Gate: FAILED"
            overall_status="FAIL"
        fi
        
        echo "🔍 Running Regression Detection Gate..."
        if execute_regression_gate "$task_id" "$evidence_dir"; then
            echo "✅ Regression Gate: PASSED"
        else
            echo "❌ Regression Gate: FAILED"
            overall_status="FAIL"
        fi
    fi
    
    # Generate comprehensive performance report
    generate_performance_report "$task_id" "$evidence_dir" "$overall_status" "$timestamp"
    
    if [[ "$overall_status" == "PASS" ]]; then
        echo "🎉 All performance gates PASSED"
        update_performance_baseline "$task_id"
        return 0
    else
        echo "🚨 Performance gates FAILED"
        generate_optimization_recommendations "$task_id" "$evidence_dir"
        return 1
    fi
}

# Execute API performance gate
execute_api_performance_gate() {
    local task_id=$1
    local evidence_dir=$2
    local response_time_target=$3
    
    echo "📊 Testing API performance..."
    
    # Detect API endpoints to test
    local endpoints=$(discover_api_endpoints)
    if [[ -z "$endpoints" ]]; then
        echo "⚠️  No API endpoints detected, skipping API performance test"
        return 0
    fi
    
    local results_file="$evidence_dir/api-performance-results.json"
    local load_test_output="$evidence_dir/load-test-output.txt"
    
    # Start application if needed
    ensure_application_running
    
    # Execute load test using wrk
    echo "🔧 Running load test with wrk..."
    wrk -t12 -c100 -d120s --script scripts/performance/api-test.lua \
        --latency "$endpoints" > "$load_test_output" 2>&1
    
    # Parse results
    local p95_latency=$(grep "99.00%" "$load_test_output" | awk '{print $2}' | sed 's/ms//')
    local requests_per_sec=$(grep "Requests/sec:" "$load_test_output" | awk '{print $2}')
    local error_rate=$(calculate_error_rate "$load_test_output")
    
    # Store results
    cat > "$results_file" << EOF
{
  "test_type": "api_performance",
  "timestamp": "$(date -u +%Y-%m-%dT%H:%M:%S.000Z)",
  "configuration": {
    "duration": 120,
    "threads": 12,
    "connections": 100,
    "endpoints_tested": $(echo "$endpoints" | wc -l)
  },
  "results": {
    "p95_latency_ms": $p95_latency,
    "requests_per_second": $requests_per_sec,
    "error_rate_percent": $error_rate,
    "total_requests": $(grep "requests in" "$load_test_output" | awk '{print $1}')
  },
  "targets": {
    "p95_latency_target": $response_time_target,
    "passed": $(echo "$p95_latency < $response_time_target" | bc -l)
  }
}
EOF
    
    # Check if gate passed
    if (( $(echo "$p95_latency < $response_time_target" | bc -l) )); then
        echo "✅ API p95 latency: ${p95_latency}ms (target: <${response_time_target}ms)"
        return 0
    else
        echo "❌ API p95 latency: ${p95_latency}ms exceeds target: ${response_time_target}ms"
        return 1
    fi
}

# Execute throughput gate
execute_throughput_gate() {
    local task_id=$1
    local evidence_dir=$2
    local rps_target=$3
    
    echo "📊 Testing throughput capacity..."
    
    local results_file="$evidence_dir/throughput-results.json"
    local benchmark_output="$evidence_dir/throughput-benchmark.txt"
    
    # Use Apache Bench for throughput testing
    echo "🔧 Running throughput test with Apache Bench..."
    ab -n 10000 -c 200 -g "$evidence_dir/throughput-graph.tsv" \
       "$(get_primary_endpoint)" > "$benchmark_output" 2>&1
    
    # Parse throughput results
    local actual_rps=$(grep "Requests per second:" "$benchmark_output" | awk '{print $4}')
    local mean_time=$(grep "Time per request:" "$benchmark_output" | head -1 | awk '{print $4}')
    local failed_requests=$(grep "Failed requests:" "$benchmark_output" | awk '{print $3}')
    
    # Store results
    cat > "$results_file" << EOF
{
  "test_type": "throughput_capacity",
  "timestamp": "$(date -u +%Y-%m-%dT%H:%M:%S.000Z)",
  "configuration": {
    "total_requests": 10000,
    "concurrency_level": 200,
    "endpoint": "$(get_primary_endpoint)"
  },
  "results": {
    "requests_per_second": $actual_rps,
    "mean_response_time_ms": $mean_time,
    "failed_requests": $failed_requests,
    "success_rate_percent": $(echo "scale=2; (10000 - $failed_requests) / 100" | bc)
  },
  "targets": {
    "rps_target": $rps_target,
    "passed": $(echo "$actual_rps > $rps_target" | bc -l)
  }
}
EOF
    
    # Check if gate passed
    if (( $(echo "$actual_rps > $rps_target" | bc -l) )); then
        echo "✅ Throughput: ${actual_rps} RPS (target: >${rps_target} RPS)"
        return 0
    else
        echo "❌ Throughput: ${actual_rps} RPS below target: ${rps_target} RPS"
        return 1
    fi
}

# Execute memory performance gate
execute_memory_gate() {
    local task_id=$1
    local evidence_dir=$2
    local memory_target_mb=$3
    
    echo "📊 Testing memory performance..."
    
    local results_file="$evidence_dir/memory-results.json"
    local memory_profile="$evidence_dir/memory-profile.txt"
    
    # Start memory monitoring
    echo "🔧 Starting memory monitoring..."
    monitor_memory_usage "$memory_profile" &
    local monitor_pid=$!
    
    # Run memory stress test
    execute_memory_stress_test "$evidence_dir"
    
    # Stop monitoring
    sleep 5
    kill $monitor_pid 2>/dev/null
    
    # Analyze memory usage
    local max_memory=$(awk 'BEGIN{max=0} {if($1>max) max=$1} END{print max}' "$memory_profile")
    local avg_memory=$(awk '{sum+=$1; count++} END{print sum/count}' "$memory_profile")
    local memory_leak_rate=$(calculate_memory_leak_rate "$memory_profile")
    
    # Store results
    cat > "$results_file" << EOF
{
  "test_type": "memory_performance",
  "timestamp": "$(date -u +%Y-%m-%dT%H:%M:%S.000Z)",
  "results": {
    "max_memory_mb": $max_memory,
    "average_memory_mb": $avg_memory,
    "memory_leak_rate_mb_per_hour": $memory_leak_rate,
    "test_duration_minutes": 10
  },
  "targets": {
    "memory_target_mb": $memory_target_mb,
    "leak_rate_target": 0,
    "passed": $(echo "$max_memory < $memory_target_mb && $memory_leak_rate == 0" | bc -l)
  }
}
EOF
    
    # Check if gate passed
    if (( $(echo "$max_memory < $memory_target_mb" | bc -l) )) && [[ "$memory_leak_rate" == "0" ]]; then
        echo "✅ Memory usage: ${max_memory}MB (target: <${memory_target_mb}MB)"
        return 0
    else
        echo "❌ Memory usage: ${max_memory}MB exceeds target: ${memory_target_mb}MB"
        return 1
    fi
}

# Execute database performance gate
execute_database_gate() {
    local task_id=$1
    local evidence_dir=$2
    
    echo "📊 Testing database performance..."
    
    local results_file="$evidence_dir/database-results.json"
    
    # Run database performance tests
    if command -v pgbench >/dev/null 2>&1; then
        test_postgresql_performance "$evidence_dir"
    elif command -v mysql >/dev/null 2>&1; then
        test_mysql_performance "$evidence_dir"
    else
        echo "⚠️  No supported database found for performance testing"
        return 0
    fi
    
    # Analyze database performance results
    local query_p95=$(get_database_query_p95 "$evidence_dir")
    local transaction_rate=$(get_database_transaction_rate "$evidence_dir")
    
    # Check if database performance meets targets
    if (( $(echo "$query_p95 < 10" | bc -l) )); then
        echo "✅ Database query p95: ${query_p95}ms (target: <10ms)"
        return 0
    else
        echo "❌ Database query p95: ${query_p95}ms exceeds target: 10ms"
        return 1
    fi
}

# Execute regression detection gate
execute_regression_gate() {
    local task_id=$1
    local evidence_dir=$2
    
    echo "📊 Testing for performance regressions..."
    
    local current_baseline="$evidence_dir/current-performance-baseline.json"
    local historical_baseline="$PERFORMANCE_BASELINE_DIR/latest-baseline.json"
    
    # Create current baseline
    create_performance_baseline "$task_id" "$current_baseline"
    
    if [[ ! -f "$historical_baseline" ]]; then
        echo "⚠️  No historical baseline found, creating new baseline"
        cp "$current_baseline" "$historical_baseline"
        return 0
    fi
    
    # Compare baselines
    local regression_report="$evidence_dir/regression-analysis.json"
    compare_performance_baselines "$current_baseline" "$historical_baseline" "$regression_report"
    
    # Check for significant regressions
    local regression_detected=$(jq -r '.significant_regression' "$regression_report")
    
    if [[ "$regression_detected" == "false" ]]; then
        echo "✅ No significant performance regression detected"
        return 0
    else
        echo "❌ Performance regression detected"
        jq -r '.regressions[]' "$regression_report"
        return 1
    fi
}

# Generate performance optimization recommendations
generate_optimization_recommendations() {
    local task_id=$1
    local evidence_dir=$2
    
    echo "🔍 Generating optimization recommendations..."
    
    local recommendations_file="$evidence_dir/optimization-recommendations.json"
    
    # Analyze performance bottlenecks
    local api_bottlenecks=$(analyze_api_bottlenecks "$evidence_dir")
    local memory_issues=$(analyze_memory_issues "$evidence_dir")
    local database_issues=$(analyze_database_issues "$evidence_dir")
    
    # Generate recommendations
    cat > "$recommendations_file" << EOF
{
  "task_id": "$task_id",
  "analysis_timestamp": "$(date -u +%Y-%m-%dT%H:%M:%S.000Z)",
  "performance_issues": {
    "api_bottlenecks": $api_bottlenecks,
    "memory_issues": $memory_issues,
    "database_issues": $database_issues
  },
  "recommendations": [
    {
      "category": "API_OPTIMIZATION",
      "priority": "HIGH",
      "issue": "High response time",
      "solution": "Implement response caching with Redis",
      "expected_improvement": "40-60% response time reduction",
      "implementation_effort": "Medium",
      "resources": ["Redis setup guide", "Caching patterns documentation"]
    },
    {
      "category": "DATABASE_OPTIMIZATION",
      "priority": "HIGH",
      "issue": "Slow database queries",
      "solution": "Add database indexes for frequently queried columns",
      "expected_improvement": "70-90% query time reduction",
      "implementation_effort": "Low",
      "resources": ["Database indexing guide", "Query optimization checklist"]
    },
    {
      "category": "MEMORY_OPTIMIZATION",
      "priority": "MEDIUM",
      "issue": "High memory usage",
      "solution": "Implement object pooling for frequently created objects",
      "expected_improvement": "30-50% memory usage reduction",
      "implementation_effort": "Medium",
      "resources": ["Object pooling patterns", "Memory optimization guide"]
    }
  ],
  "next_steps": [
    "Implement high-priority optimizations",
    "Re-run performance tests to validate improvements",
    "Monitor production performance for sustained improvement"
  ]
}
EOF
    
    echo "📋 Optimization recommendations generated: $recommendations_file"
    echo "🔧 Recommended next steps:"
    jq -r '.next_steps[]' "$recommendations_file" | sed 's/^/  • /'
}

# Utility functions
discover_api_endpoints() {
    # Auto-discover API endpoints from routing files
    if [[ -f "routes.py" ]]; then
        grep -E "app\.(get|post|put|delete)" routes.py | sed 's/.*["'\'']\([^"'\'']*\)["'\''].*/\1/'
    elif [[ -f "server.js" ]]; then
        grep -E "app\.(get|post|put|delete)" server.js | sed 's/.*["'\'']\([^"'\'']*\)["'\''].*/\1/'
    else
        echo "http://localhost:8080/health"  # Default health endpoint
    fi
}

ensure_application_running() {
    # Check if application is running and start if needed
    if ! curl -s "$(get_primary_endpoint)" >/dev/null 2>&1; then
        echo "🚀 Starting application for performance testing..."
        start_application_for_testing
        sleep 10  # Wait for startup
    fi
}

get_primary_endpoint() {
    echo "http://localhost:8080/api/v1/health"
}

monitor_memory_usage() {
    local output_file=$1
    while true; do
        # Get memory usage in MB
        local memory_mb=$(ps aux | grep -v grep | grep "$(get_application_process)" | awk '{sum+=$6} END {print sum/1024}')
        echo "$memory_mb" >> "$output_file"
        sleep 1
    done
}

# Export functions
export -f init_performance_testing
export -f execute_performance_gates
export -f execute_api_performance_gate
export -f execute_throughput_gate
export -f execute_memory_gate
export -f execute_database_gate
export -f execute_regression_gate
export -f generate_optimization_recommendations
```

────────────────────────────────────────────────────────────────────────────────

## Performance Test Scenarios

```javascript
// K6 Performance Test Script
import http from 'k6/http';
import { check, sleep } from 'k6';
import { Rate } from 'k6/metrics';

export let errorRate = new Rate('errors');

export let options = {
  stages: [
    { duration: '30s', target: 50 },   // Ramp-up to 50 users
    { duration: '1m', target: 100 },   // Stay at 100 users
    { duration: '2m', target: 200 },   // Ramp-up to 200 users
    { duration: '2m', target: 200 },   // Stay at 200 users
    { duration: '30s', target: 0 },    // Ramp-down to 0 users
  ],
  thresholds: {
    http_req_duration: ['p(95)<200'],  // 95% of requests must complete below 200ms
    http_req_failed: ['rate<0.01'],    // Error rate must be below 1%
    errors: ['rate<0.01'],
  },
};

export default function() {
  let response = http.get('http://localhost:8080/api/v1/users');
  
  check(response, {
    'status is 200': (r) => r.status === 200,
    'response time < 200ms': (r) => r.timings.duration < 200,
    'content type is JSON': (r) => r.headers['Content-Type'] === 'application/json',
  }) || errorRate.add(1);
  
  // Simulate user think time
  sleep(1);
}
```

```yaml
# Artillery Performance Test Configuration
config:
  target: 'http://localhost:8080'
  phases:
    - duration: 60
      arrivalRate: 10
      name: "Warm up"
    - duration: 120
      arrivalRate: 50
      name: "Normal load"
    - duration: 60
      arrivalRate: 100
      name: "Peak load"
  defaults:
    headers:
      Content-Type: 'application/json'
  
scenarios:
  - name: "API Performance Test"
    weight: 100
    flow:
      - get:
          url: "/api/v1/health"
          expect:
            - statusCode: 200
            - contentType: json
      - post:
          url: "/api/v1/users"
          json:
            name: "Test User"
            email: "test@example.com"
          expect:
            - statusCode: 201
      - get:
          url: "/api/v1/users/{{ id }}"
          expect:
            - statusCode: 200
            - hasProperty: name
      - think: 1

  - name: "Database Heavy Operations"
    weight: 20
    flow:
      - get:
          url: "/api/v1/reports/heavy"
          expect:
            - statusCode: 200
            - maxResponseTime: 500
```