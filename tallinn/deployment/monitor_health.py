#!/usr/bin/env python3
"""
Monitoring script for staging deployment
"""

import requests
import time
import json
from datetime import datetime

def monitor_health(url, interval=60):
    """Monitor health endpoint continuously."""
    print(f"Starting health monitoring for {url}")
    print("Press Ctrl+C to stop")
    
    while True:
        try:
            response = requests.get(f"{url}/health/detailed", timeout=10)
            if response.status_code == 200:
                data = response.json()
                print(f"\n[{datetime.now().isoformat()}] Health Check")
                print(f"Status: {data['status']}")
                print(f"CPU: {data['system']['cpu_usage']}")
                print(f"Memory: {data['system']['memory_usage']}")
                print(f"Components: {data['components']}")
            else:
                print(f"\n[{datetime.now().isoformat()}] ❌ Health check failed: {response.status_code}")
        except Exception as e:
            print(f"\n[{datetime.now().isoformat()}] ❌ Error: {str(e)}")
        
        time.sleep(interval)

if __name__ == '__main__':
    import sys
    url = sys.argv[1] if len(sys.argv) > 1 else "http://localhost:8080"
    monitor_health(url)
