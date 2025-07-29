---
name: /notebook-run
description: "Execute Jupyter notebooks for [INSERT_PROJECT_NAME] with parameter injection and monitoring"
usage: /notebook-run [notebook-path] [--params key=value] [--kernel python3|R|julia] [--output-dir path]
category: data-science
tools: Bash, Read, Write
security: [path-validation]
risk_level: high
---

# Notebook Execution for [INSERT_PROJECT_NAME]

## 🔒 Security Validation

Before executing any notebook, I'll validate all paths for security:

**Path Security Check:**
- **Notebook path**: `{notebook_path_input}`
- **Sanitized**: Removing any `../` traversal sequences
- **Canonical path**: Resolving to absolute path within project boundaries  
- **Directory allowlist**: Checking against allowed directories: `notebooks/`, `data/`, `experiments/`, `analysis/`
- **Output directory**: Validating `--output-dir` parameter if provided
- **Config files**: Ensuring `--config` paths are within project scope

**Validation Process:**
1. **Sanitize input**: Remove path traversal sequences (`../`, `..\\`, URL-encoded variants)
2. **Canonicalize path**: Resolve to absolute path and check project boundaries
3. **Enforce allowlist**: Ensure path is within approved directories for notebook execution
4. **Validate permissions**: Check file exists and is readable

**Security Result:**
✅ **VALIDATED** - All paths are secure, proceeding with notebook execution  
❌ **BLOCKED** - Security violation detected, operation cancelled

---

I'll help you run Jupyter notebooks for **[INSERT_PROJECT_NAME]** with proper parameterization, monitoring, and output management for your **[INSERT_DOMAIN]** data science workflows.

## Execution Modes

### Interactive Execution
Run with live output:
```bash
# SECURITY: Path 'analysis.ipynb' validated → 'notebooks/analysis.ipynb' ✅
/notebook-run analysis.ipynb
```

### Batch Execution
Run multiple notebooks:
```bash
/notebook-run experiments/*.ipynb --parallel
```

### Scheduled Execution
For [INSERT_WORKFLOW_TYPE] workflows:
```bash
/notebook-run daily_report.ipynb --schedule "0 9 * * *"
```

## Parameter Injection

### Basic Parameters
Pass variables to notebooks:
```bash
/notebook-run model_training.ipynb \
  --params dataset=train_2025 \
  --params epochs=100 \
  --params learning_rate=0.001
```

### Environment-Based
For different environments:
```bash
/notebook-run analysis.ipynb \
  --params env=[INSERT_DEPLOYMENT_TARGET] \
  --params db=[INSERT_DATABASE_TYPE]
```

### Configuration Files
Load from config:
```bash
/notebook-run experiment.ipynb \
  --config experiments/config.yaml
```

## Kernel Management

### Python Kernels
For [INSERT_PRIMARY_LANGUAGE] projects:
```bash
/notebook-run ml_pipeline.ipynb --kernel python3
```

### R Kernels
Statistical analysis:
```bash
/notebook-run stats_analysis.ipynb --kernel ir
```

### Custom Kernels
Domain-specific:
```bash
/notebook-run [INSERT_DOMAIN]_analysis.ipynb \
  --kernel custom_kernel
```

## Output Management

### Save Outputs
Preserve results:
```bash
# SECURITY: All paths validated before execution
# - notebook: 'experiment.ipynb' → '/project/notebooks/experiment.ipynb' ✅
# - output-dir: 'results/20250729' → '/project/results/20250729' ✅
/notebook-run experiment.ipynb \
  --output-dir results/$(date +%Y%m%d) \
  --save-html \
  --save-pdf
```

### Clean Outputs
For version control:
```bash
/notebook-run *.ipynb --clear-outputs
```

### Export Formats
Multiple formats:
- HTML reports
- PDF documents
- Markdown files
- Python scripts

## Error Handling

### Cell-Level Errors
Continue on error:
```bash
/notebook-run exploration.ipynb \
  --continue-on-error \
  --log-errors errors.log
```

### Timeout Protection
For long-running cells:
```bash
/notebook-run training.ipynb \
  --timeout-per-cell 3600 \
  --total-timeout 7200
```

## Integration Features

### With [INSERT_CI_CD_PLATFORM]
CI/CD pipeline integration:
```bash
/notebook-run tests/notebook_tests.ipynb \
  --junit-xml results.xml
```

### With MLflow
Experiment tracking:
```bash
/notebook-run model_experiment.ipynb \
  --mlflow-tracking \
  --experiment-name "[INSERT_PROJECT_NAME]_exp"
```

### With [INSERT_DATABASE_TYPE]
Database connections:
```bash
/notebook-run data_analysis.ipynb \
  --params db_conn=$DATABASE_URL
```

## Performance Options

For [INSERT_PERFORMANCE_PRIORITY]:
- GPU acceleration
- Memory limits
- CPU allocation
- Parallel execution

## Monitoring

### Progress Tracking
Real-time monitoring:
```bash
/notebook-run long_training.ipynb \
  --progress \
  --notify-on-complete
```

### Resource Usage
Monitor consumption:
```bash
/notebook-run resource_heavy.ipynb \
  --monitor-resources \
  --max-memory 16GB
```

## Team Collaboration

For [INSERT_TEAM_SIZE] teams:
- Shared parameter sets
- Result distribution
- Execution logs
- Reproducibility

## Templates

### Data Analysis
```bash
/notebook-run templates/eda_template.ipynb \
  --params data_path=new_dataset.csv \
  --output-dir analysis/
```

### Model Training
```bash
/notebook-run templates/train_template.ipynb \
  --params model_type=xgboost \
  --params target_metric=accuracy
```

### Reporting
```bash
/notebook-run templates/report_template.ipynb \
  --params period=weekly \
  --output-format pdf
```

## 🚨 Security Protection Examples

The following malicious patterns are **automatically blocked**:

### Path Traversal Attacks (BLOCKED)
```bash
# ❌ BLOCKED: Attempt to access system files
/notebook-run ../../../etc/passwd

# ❌ BLOCKED: Directory traversal with output redirect
/notebook-run analysis.ipynb --output-dir ../../../tmp/

# ❌ BLOCKED: URL-encoded traversal
/notebook-run analysis.ipynb --config ..%2F..%2F..%2Fetc%2Fpasswd
```

### Legitimate Operations (ALLOWED)
```bash
# ✅ ALLOWED: Notebook in approved directory
/notebook-run notebooks/data_analysis.ipynb

# ✅ ALLOWED: Output to project results
/notebook-run notebooks/experiment.ipynb --output-dir results/today/

# ✅ ALLOWED: Config in project directory  
/notebook-run notebooks/model.ipynb --config configs/training.yaml
```

**Protection Active**: All paths are validated before execution. Malicious patterns trigger immediate blocking with security alerts.

---

Which notebook would you like to run for [INSERT_PROJECT_NAME]?