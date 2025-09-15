# Infrastructure Scripts Setup Guide

## 🎯 Script Categories

### **✅ Standalone Scripts** (Work anywhere)
- `setup_email.sh` - Email configuration setup
- `push.sh` - Git commit and push automation
- `setup-github-runner.sh` - GitHub Actions runner setup

### **⚠️ Project-Dependent Scripts** (Need project-specific setup)
- `loc.sh` - Requires `scripts/analyze_git_stats.py`
- `run_tests_with_coverage.sh` - Requires `vpython` and venv setup

### **🔧 Support Files**
- `infrastructure_common.sh` - Shared functions and auto-detection
- `.infrastructure.conf.example` - Configuration template

## 📋 Setup Instructions

### 1. **Copy to Project Root**
All infrastructure scripts should be placed in your project root directory:
```bash
cp infrastructure-scripts/* .
```

### 2. **Configure Project Settings**
```bash
# Copy and customize configuration
cp .infrastructure.conf.example .infrastructure.conf
# Edit .infrastructure.conf with your project settings
```

### 3. **Dependencies for Advanced Scripts**

#### For `loc.sh`:
Create the missing dependency or use a simplified version:
```bash
mkdir -p scripts
# Either copy analyze_git_stats.py from source project
# OR use the simplified version provided below
```

#### For `run_tests_with_coverage.sh`:
```bash
# Create vpython wrapper if using Python virtual environment
echo '#!/bin/bash' > vpython
echo 'exec python "$@"' >> vpython
chmod +x vpython

# OR install actual virtual environment
python -m venv venv
```

## 🚀 Quick Test
```bash
# Test basic functionality
./test_portability.sh

# Test individual scripts
./setup_email.sh
./push.sh "test commit"
```

## 🔧 Troubleshooting

### Missing Dependencies
- **vpython**: Create simple wrapper or install virtual environment
- **analyze_git_stats.py**: Use simplified version or copy from source project
- **test_server_manager.sh**: Optional - only for branch-specific server startup

### Configuration Issues
- Check `.infrastructure.conf` for project-specific settings
- Verify git repository is properly initialized
- Ensure git user.email is configured

## 📊 Script Portability Matrix

| Script | Standalone | Needs Deps | Project Root |
|--------|------------|------------|--------------|
| setup_email.sh | ✅ | ❌ | ✅ |
| push.sh | ✅ | ❌ | ✅ |
| setup-github-runner.sh | ✅ | ❌ | ✅ |
| loc.sh | ❌ | ⚠️ | ✅ |
| run_tests_with_coverage.sh | ❌ | ⚠️ | ✅ |