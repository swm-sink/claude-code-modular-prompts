# Troubleshooting Guide - Claude Code Framework Dashboard

## 🔧 Quick Fix Index

### 🚨 Critical Issues
- [Dashboard Won't Start](#dashboard-wont-start)
- [Complete System Failure](#complete-system-failure)
- [Data Loss or Corruption](#data-loss-or-corruption)

### ⚠️ Common Issues
- [Modules Not Loading](#modules-not-loading)
- [Performance Issues](#performance-issues)
- [Export/Import Problems](#exportimport-problems)
- [Session Management Issues](#session-management-issues)

### 💡 User Experience Issues
- [Navigation Problems](#navigation-problems)
- [Visual Display Issues](#visual-display-issues)
- [Feature Not Working](#feature-not-working)

---

## 🚨 Critical Issues

### Dashboard Won't Start

#### Symptoms
- Application fails to launch
- Error messages on startup
- Browser shows "connection refused"
- Terminal shows Python errors

#### Diagnosis Steps
1. **Check Python Version**
   ```bash
   python --version
   # Should be 3.8 or higher
   ```

2. **Verify Dependencies**
   ```bash
   pip check
   pip list | grep streamlit
   ```

3. **Check Port Availability**
   ```bash
   lsof -i :8501
   # Port should be free
   ```

4. **Test Basic Installation**
   ```bash
   streamlit hello
   ```

#### Solutions

**Solution 1: Python Version Issue**
```bash
# Install Python 3.8+
# On macOS with Homebrew
brew install python@3.9

# On Ubuntu/Debian
sudo apt update
sudo apt install python3.9

# Create virtual environment
python3.9 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

**Solution 2: Dependencies Issue**
```bash
# Clean install
pip uninstall streamlit
pip install --no-cache-dir -r requirements.txt

# Or use conda
conda create -n claude-dashboard python=3.9
conda activate claude-dashboard
pip install -r requirements.txt
```

**Solution 3: Port Conflict**
```bash
# Kill process using port 8501
lsof -ti:8501 | xargs kill -9

# Or use different port
streamlit run app.py --server.port 8502
```

**Solution 4: Permissions Issue**
```bash
# Check file permissions
ls -la app.py

# Fix permissions
chmod +x app.py
chmod -R 755 streamlit_dashboard/
```

### Complete System Failure

#### Symptoms
- Dashboard crashes frequently
- Memory errors
- System becomes unresponsive
- Browser crashes

#### Diagnosis Steps
1. **Check System Resources**
   ```bash
   htop
   # Monitor CPU and memory usage
   ```

2. **Check Error Logs**
   ```bash
   tail -f ~/.streamlit/logs/streamlit.log
   ```

3. **Memory Profile**
   ```bash
   # Run with memory profiling
   python -m memory_profiler app.py
   ```

#### Solutions

**Solution 1: Memory Issue**
```bash
# Increase system memory or use swap
sudo fallocate -l 2G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile

# Or run with memory limits
streamlit run app.py --server.maxUploadSize=50
```

**Solution 2: Clear Cache**
```bash
# Clear Streamlit cache
streamlit cache clear

# Clear browser cache
# In browser: Ctrl+Shift+Del
```

**Solution 3: Reset Installation**
```bash
# Complete reset
rm -rf ~/.streamlit/
pip uninstall streamlit
pip install streamlit
```

---

## ⚠️ Common Issues

### Modules Not Loading

#### Symptoms
- Empty module library
- "No modules found" message
- Modules appear but have no content
- Search returns no results

#### Diagnosis Steps
1. **Check Framework Structure**
   ```bash
   ls -la .claude/
   find .claude -name "*.md" | head -10
   ```

2. **Verify Module Content**
   ```bash
   head -20 .claude/modules/patterns/thinking-pattern-template.md
   ```

3. **Check Permissions**
   ```bash
   ls -la .claude/modules/
   ```

#### Solutions

**Solution 1: Missing Framework Files**
```bash
# Clone or copy framework files
git clone https://github.com/swm-sink/claude-code-modular-prompts.git
cp -r claude-code-modular-prompts/.claude ./
```

**Solution 2: File Permissions**
```bash
# Fix permissions
chmod -R 755 .claude/
chmod -R 644 .claude/**/*.md
```

**Solution 3: Module Parser Issues**
```bash
# Test module parsing
python -c "
from data.framework_parser import FrameworkParser
parser = FrameworkParser()
modules = parser.parse_modules()
print(f'Found {len(modules)} modules')
"
```

**Solution 4: Path Configuration**
```bash
# Set correct framework path
export FRAMEWORK_PATH=/path/to/your/.claude
streamlit run app.py
```

### Performance Issues

#### Symptoms
- Slow page loading
- Unresponsive interface
- High memory usage
- Browser freezing

#### Diagnosis Steps
1. **Performance Profiling**
   ```python
   from utils.performance_profiler import PerformanceProfiler
   profiler = PerformanceProfiler()
   results = profiler.profile_complete_workflow()
   ```

2. **Check Resource Usage**
   ```bash
   # Monitor real-time usage
   watch -n 1 'ps aux | grep streamlit'
   ```

3. **Browser Debug**
   ```
   F12 → Network → Monitor loading times
   F12 → Performance → Record page interactions
   ```

#### Solutions

**Solution 1: Browser Cache**
```bash
# Clear browser cache
# Chrome: Ctrl+Shift+Del
# Firefox: Ctrl+Shift+Del
# Safari: Develop → Empty Caches
```

**Solution 2: Reduce Dataset Size**
```python
# Limit modules loaded
MAX_MODULES = 20  # Reduce from 64+
```

**Solution 3: Memory Optimization**
```python
# Add to app.py
import gc
gc.collect()  # Force garbage collection
```

**Solution 4: Streamlit Configuration**
```bash
# Create .streamlit/config.toml
mkdir -p ~/.streamlit/
cat > ~/.streamlit/config.toml << EOF
[server]
maxUploadSize = 50
maxMessageSize = 50
enableCORS = false
enableXsrfProtection = false

[browser]
gatherUsageStats = false
EOF
```

### Export/Import Problems

#### Symptoms
- Download buttons not working
- Export files are empty
- Import fails with errors
- Corrupted export data

#### Diagnosis Steps
1. **Check Browser Console**
   ```
   F12 → Console → Look for JavaScript errors
   ```

2. **Verify Export Data**
   ```python
   # Test export functionality
   import json
   test_data = {"test": "data"}
   json.dumps(test_data)
   ```

3. **Check File Permissions**
   ```bash
   ls -la downloads/
   ```

#### Solutions

**Solution 1: Browser Download Settings**
```
1. Check browser download permissions
2. Disable popup blockers
3. Allow downloads from localhost
4. Check download directory permissions
```

**Solution 2: Export Data Validation**
```python
# Add validation to export functions
def validate_export_data(data):
    try:
        json.dumps(data)
        return True
    except:
        return False
```

**Solution 3: File Size Limits**
```python
# Check export file size
import os
max_size = 10 * 1024 * 1024  # 10MB
if os.path.getsize(export_file) > max_size:
    print("Export file too large")
```

---

## 💡 User Experience Issues

### Navigation Problems

#### Symptoms
- Sidebar not responding
- Pages not loading
- Navigation buttons not working
- URL routing issues

#### Solutions

**Solution 1: Session State Reset**
```python
# Clear session state
if st.button("Reset Session"):
    for key in st.session_state.keys():
        del st.session_state[key]
    st.rerun()
```

**Solution 2: Browser Refresh**
```
# Hard refresh
Ctrl+Shift+R (Windows/Linux)
Cmd+Shift+R (Mac)
```

**Solution 3: Check Network**
```bash
# Test network connectivity
ping localhost
curl http://localhost:8501
```

### Visual Display Issues

#### Symptoms
- Elements not rendering
- CSS styling broken
- Charts not displaying
- Layout problems

#### Solutions

**Solution 1: CSS Cache**
```bash
# Clear CSS cache
# Browser: Ctrl+Shift+R
# Or disable cache in DevTools
```

**Solution 2: Plotly Issues**
```python
# Update Plotly
pip install --upgrade plotly
```

**Solution 3: Streamlit Version**
```bash
# Update Streamlit
pip install --upgrade streamlit
```

---

## 🔧 Diagnostic Tools

### Built-in Diagnostics

#### Health Check
```python
def run_health_check():
    """Run comprehensive health check"""
    checks = {
        'python_version': check_python_version(),
        'dependencies': check_dependencies(),
        'framework_files': check_framework_files(),
        'permissions': check_permissions(),
        'memory': check_memory_usage(),
        'performance': check_performance()
    }
    return checks
```

#### Performance Monitor
```python
from utils.performance_profiler import PerformanceProfiler

profiler = PerformanceProfiler()
results = profiler.profile_complete_workflow()
print(f"Overall Grade: {results['overall_grade']}")
```

### External Diagnostic Tools

#### System Monitoring
```bash
# CPU and Memory
htop
# Or
top -p $(pgrep -f streamlit)

# Network
netstat -tlnp | grep :8501

# Disk Space
df -h
```

#### Application Logs
```bash
# Streamlit logs
tail -f ~/.streamlit/logs/streamlit.log

# Application logs
tail -f debug.log
```

---

## 📋 Common Error Messages

### Error: "ModuleNotFoundError"
```
Solution: pip install -r requirements.txt
```

### Error: "Port 8501 is already in use"
```
Solution: lsof -ti:8501 | xargs kill -9
```

### Error: "Permission denied"
```
Solution: chmod -R 755 streamlit_dashboard/
```

### Error: "No module named 'streamlit'"
```
Solution: pip install streamlit
```

### Error: "JSON decode error"
```
Solution: Check for corrupted configuration files
```

---

## 🆘 Emergency Recovery

### Complete System Reset
```bash
# 1. Stop all processes
pkill -f streamlit

# 2. Clear all cache
rm -rf ~/.streamlit/
rm -rf __pycache__/
rm -rf .pytest_cache/

# 3. Clean install
pip uninstall streamlit
pip install --no-cache-dir -r requirements.txt

# 4. Reset permissions
chmod -R 755 .
chmod -R 644 **/*.md

# 5. Start fresh
streamlit run app.py
```

### Data Recovery
```bash
# Recover from session backups
ls -la data/sessions/
# Copy latest working session
cp data/sessions/latest.json data/sessions/recovery.json
```

---

## 📞 Getting Help

### Self-Service Resources
1. **Check Documentation**: Complete guides and tutorials
2. **Search Issues**: GitHub issues for similar problems
3. **Community Forums**: Connect with other users
4. **FAQ**: Frequently asked questions

### Support Channels
1. **GitHub Issues**: Report bugs and get help
2. **Community Discord**: Real-time community support
3. **Email Support**: Direct support for complex issues
4. **Documentation**: Comprehensive troubleshooting guides

### Before Contacting Support
Please include:
- **Operating System**: Version and type
- **Python Version**: `python --version`
- **Streamlit Version**: `streamlit version`
- **Error Messages**: Complete error logs
- **Steps to Reproduce**: Detailed reproduction steps
- **Expected vs Actual**: What you expected vs what happened

---

## 🔄 Maintenance and Prevention

### Regular Maintenance
```bash
# Weekly maintenance script
#!/bin/bash
echo "Running weekly maintenance..."

# Update dependencies
pip install --upgrade streamlit

# Clear old cache
streamlit cache clear

# Check for updates
git fetch origin
git status

# Clean up logs
find . -name "*.log" -mtime +7 -delete

echo "Maintenance complete!"
```

### Monitoring Setup
```python
# Set up basic monitoring
import logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()
    ]
)
```

### Best Practices
1. **Keep Dependencies Updated**: Regular updates prevent issues
2. **Monitor Performance**: Track metrics and usage
3. **Backup Regularly**: Save important configurations
4. **Test After Changes**: Always test after modifications
5. **Document Issues**: Keep track of problems and solutions

---

*Last Updated: 2025-07-18*
*Troubleshooting Guide Version: 1.0.0*
*Framework Version: 3.0.0*

**Need more help? Contact support at support@claude-code-framework.com**