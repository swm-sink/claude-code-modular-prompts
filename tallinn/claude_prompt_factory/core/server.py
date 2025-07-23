#!/usr/bin/env python3
"""
Health Check System for Staging Deployment
"""

from flask import Flask, jsonify
import os
import json
import psutil
from datetime import datetime

app = Flask(__name__)

@app.route('/health')
def health_check():
    """Basic health check endpoint."""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'environment': os.getenv('ENVIRONMENT', 'unknown'),
        'version': os.getenv('FRAMEWORK_VERSION', 'unknown')
    })

@app.route('/health/detailed')
def detailed_health():
    """Detailed health check with system metrics."""
    cpu_percent = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    
    health_status = {
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'environment': os.getenv('ENVIRONMENT', 'unknown'),
        'version': os.getenv('FRAMEWORK_VERSION', 'unknown'),
        'system': {
            'cpu_usage': f'{cpu_percent}%',
            'memory_usage': f'{memory.percent}%',
            'memory_available': f'{memory.available / (1024**3):.1f}GB'
        },
        'components': {
            'cache': check_cache_health(),
            'performance': check_performance_health(),
            'security': check_security_health()
        }
    }
    
    # Determine overall health
    component_health = all(health_status['components'].values())
    system_healthy = cpu_percent < 90 and memory.percent < 90
    
    if not (component_health and system_healthy):
        health_status['status'] = 'degraded'
    
    return jsonify(health_status)

def check_cache_health():
    """Check cache system health."""
    try:
        cache_config = 'claude_prompt_factory/performance_config.json'
        if os.path.exists(cache_config):
            with open(cache_config, 'r') as f:
                config = json.load(f)
            return config.get('cache_enabled', False)
        return False
    except:
        return False

def check_performance_health():
    """Check performance optimization health."""
    try:
        perf_files = [
            'claude_prompt_factory/performance_config.json',
            'claude_prompt_factory/parallel_loading_config.json',
            'claude_prompt_factory/token_optimization_config.json'
        ]
        return all(os.path.exists(f) for f in perf_files)
    except:
        return False

def check_security_health():
    """Check security configuration health."""
    try:
        security_files = [
            'api_key_rotation.json',
            'settings.local.json'
        ]
        return all(os.path.exists(f) for f in security_files)
    except:
        return False

if __name__ == '__main__':
    port = int(os.getenv('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
