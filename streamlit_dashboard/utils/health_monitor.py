"""
Health monitoring utilities for production deployment
Provides health checks, error tracking, and performance monitoring
"""

import time
import os
import json
import logging
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, Any, Optional
import streamlit as st
import psutil


class HealthMonitor:
    """Comprehensive health monitoring for production deployment"""
    
    def __init__(self, log_dir: Path = Path("logs")):
        self.log_dir = log_dir
        self.log_dir.mkdir(exist_ok=True)
        self.setup_logging()
        
    def setup_logging(self):
        """Configure production logging"""
        log_file = self.log_dir / f"health_{datetime.now().strftime('%Y%m%d')}.log"
        
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(log_file),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger(__name__)
    
    def get_health_status(self) -> Dict[str, Any]:
        """Get comprehensive health status"""
        start_time = time.time()
        
        health_data = {
            "timestamp": datetime.now().isoformat(),
            "status": "healthy",
            "checks": {},
            "performance": {},
            "environment": {}
        }
        
        try:
            # System health checks
            health_data["checks"]["memory"] = self._check_memory()
            health_data["checks"]["disk"] = self._check_disk_space()
            health_data["checks"]["environment"] = self._check_environment()
            health_data["checks"]["framework"] = self._check_framework_access()
            
            # Performance metrics
            health_data["performance"]["response_time"] = time.time() - start_time
            health_data["performance"]["memory_usage"] = psutil.Process().memory_info().rss / 1024 / 1024  # MB
            health_data["performance"]["cpu_percent"] = psutil.cpu_percent()
            
            # Environment info
            health_data["environment"]["python_version"] = f"{os.sys.version_info.major}.{os.sys.version_info.minor}"
            health_data["environment"]["deployment"] = os.getenv("RAILWAY_ENVIRONMENT", "local")
            health_data["environment"]["service"] = os.getenv("RAILWAY_SERVICE_NAME", "unknown")
            
            # Overall status
            failed_checks = [k for k, v in health_data["checks"].items() if not v.get("healthy", False)]
            if failed_checks:
                health_data["status"] = "degraded"
                health_data["failed_checks"] = failed_checks
                
        except Exception as e:
            health_data["status"] = "unhealthy"
            health_data["error"] = str(e)
            self.logger.error(f"Health check failed: {e}", exc_info=True)
        
        return health_data
    
    def _check_memory(self) -> Dict[str, Any]:
        """Check memory usage"""
        try:
            memory = psutil.virtual_memory()
            memory_check = {
                "healthy": memory.percent < 90,
                "usage_percent": memory.percent,
                "available_mb": memory.available / 1024 / 1024,
                "total_mb": memory.total / 1024 / 1024
            }
            return memory_check
        except Exception as e:
            return {"healthy": False, "error": str(e)}
    
    def _check_disk_space(self) -> Dict[str, Any]:
        """Check disk space"""
        try:
            disk = psutil.disk_usage('.')
            disk_check = {
                "healthy": disk.percent < 90,
                "usage_percent": disk.percent,
                "free_gb": disk.free / 1024 / 1024 / 1024,
                "total_gb": disk.total / 1024 / 1024 / 1024
            }
            return disk_check
        except Exception as e:
            return {"healthy": False, "error": str(e)}
    
    def _check_environment(self) -> Dict[str, Any]:
        """Check environment configuration"""
        try:
            env_check = {
                "healthy": True,
                "required_vars": {},
                "optional_vars": {}
            }
            
            # Check required environment variables
            required_vars = ["GEMINI_API_KEY"]
            for var in required_vars:
                value = os.getenv(var)
                env_check["required_vars"][var] = {
                    "present": value is not None,
                    "length": len(value) if value else 0
                }
                if not value:
                    env_check["healthy"] = False
            
            # Check optional environment variables
            optional_vars = ["CLAUDE_FRAMEWORK_PATH", "ENVIRONMENT"]
            for var in optional_vars:
                value = os.getenv(var)
                env_check["optional_vars"][var] = {
                    "present": value is not None,
                    "value": value if var != "GEMINI_API_KEY" else "***" if value else None
                }
            
            return env_check
        except Exception as e:
            return {"healthy": False, "error": str(e)}
    
    def _check_framework_access(self) -> Dict[str, Any]:
        """Check framework directory access"""
        try:
            # Try to access framework path using the same logic as the app
            from app import LocalDevelopmentConfig, RailwayProductionConfig, EnvironmentDetector
            
            env = EnvironmentDetector.detect_environment()
            if env == "railway":
                config = RailwayProductionConfig()
            else:
                config = LocalDevelopmentConfig()
            
            framework_path = config.get_framework_path()
            
            framework_check = {
                "healthy": framework_path is not None and framework_path.exists(),
                "path": str(framework_path) if framework_path else None,
                "exists": framework_path.exists() if framework_path else False,
                "environment": env
            }
            
            return framework_check
        except Exception as e:
            return {"healthy": False, "error": str(e)}
    
    def log_error(self, error: Exception, context: str = ""):
        """Log error with context for production debugging"""
        error_data = {
            "timestamp": datetime.now().isoformat(),
            "error_type": type(error).__name__,
            "error_message": str(error),
            "context": context,
            "environment": os.getenv("RAILWAY_ENVIRONMENT", "local")
        }
        
        self.logger.error(f"Application error: {json.dumps(error_data)}", exc_info=True)
        return error_data
    
    def log_performance(self, operation: str, duration: float, metadata: Dict[str, Any] = None):
        """Log performance metrics"""
        perf_data = {
            "timestamp": datetime.now().isoformat(),
            "operation": operation,
            "duration_seconds": duration,
            "metadata": metadata or {},
            "environment": os.getenv("RAILWAY_ENVIRONMENT", "local")
        }
        
        self.logger.info(f"Performance: {json.dumps(perf_data)}")
        return perf_data
    
    def render_health_dashboard(self):
        """Render health monitoring dashboard in Streamlit"""
        st.subheader("🏥 System Health Monitor")
        
        health = self.get_health_status()
        
        # Overall status
        if health["status"] == "healthy":
            st.success("✅ System Status: Healthy")
        elif health["status"] == "degraded":
            st.warning("⚠️ System Status: Degraded")
        else:
            st.error("❌ System Status: Unhealthy")
        
        # Health checks
        st.subheader("Health Checks")
        col1, col2 = st.columns(2)
        
        with col1:
            for check_name, check_data in health["checks"].items():
                if check_data.get("healthy", False):
                    st.success(f"✅ {check_name.title()}: OK")
                else:
                    st.error(f"❌ {check_name.title()}: Failed")
                    if "error" in check_data:
                        st.text(f"Error: {check_data['error']}")
        
        with col2:
            # Performance metrics
            st.subheader("Performance Metrics")
            perf = health["performance"]
            st.metric("Response Time", f"{perf.get('response_time', 0):.3f}s")
            st.metric("Memory Usage", f"{perf.get('memory_usage', 0):.1f} MB")
            st.metric("CPU Usage", f"{perf.get('cpu_percent', 0):.1f}%")
        
        # Environment info
        st.subheader("Environment Information")
        env_info = health["environment"]
        for key, value in env_info.items():
            st.text(f"{key.replace('_', ' ').title()}: {value}")
        
        # Raw health data (for debugging)
        with st.expander("Raw Health Data"):
            st.json(health)


# Global health monitor instance
health_monitor = HealthMonitor()