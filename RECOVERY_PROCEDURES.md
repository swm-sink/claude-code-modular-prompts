# Recovery Procedures Guide

*Version: 1.0.0*
*Purpose: Practical recovery patterns for when things go wrong*
*Philosophy: Fast recovery > Perfect recovery*

## 🎯 Recovery Principles

1. **Fail Fast** - Detect problems quickly
2. **Clear Communication** - Tell user what went wrong
3. **Actionable Recovery** - Provide specific steps
4. **Preserve Work** - Never lose user data
5. **Learn from Failures** - Log for improvement

## 🔄 Framework State Recovery

### Corrupted Module State
```python
import json
from pathlib import Path
from typing import Dict, Any

class FrameworkRecovery:
    """Handle framework state recovery scenarios."""
    
    def __init__(self):
        self.recovery_dir = Path(".claude/recovery")
        self.recovery_dir.mkdir(exist_ok=True)
    
    def recover_from_bad_module(self, module_path: str) -> bool:
        """
        Recover when a module fails to load.
        
        Args:
            module_path: Path to problematic module
            
        Returns:
            True if recovery successful
        """
        try:
            # Step 1: Backup the bad module
            bad_module = Path(module_path)
            if bad_module.exists():
                backup_path = self.recovery_dir / f"{bad_module.stem}_backup_{int(time.time())}.md"
                bad_module.rename(backup_path)
                print(f"✓ Backed up problematic module to: {backup_path}")
            
            # Step 2: Try to restore from git
            try:
                subprocess.run(
                    ["git", "checkout", "HEAD", "--", module_path],
                    check=True,
                    capture_output=True
                )
                print(f"✓ Restored module from git: {module_path}")
                return True
            except subprocess.CalledProcessError:
                print("✗ Could not restore from git")
            
            # Step 3: Create minimal working module
            self.create_minimal_module(module_path)
            print(f"✓ Created minimal module: {module_path}")
            return True
            
        except Exception as e:
            print(f"✗ Recovery failed: {e}")
            return False
    
    def create_minimal_module(self, module_path: str) -> None:
        """Create a minimal working module."""
        module_name = Path(module_path).stem
        minimal_content = f"""# {module_name}
Purpose: Minimal recovery module for {module_name}
Dependencies: []

## Interface
This is a recovery module with minimal functionality.

## Implementation
```python
def execute(input_data):
    return {{
        'status': 'recovery_mode',
        'message': 'Module in recovery mode. Original module was corrupted.',
        'recovery_hint': 'Restore from backup or recreate module functionality'
    }}
```

## Error Handling
Returns recovery mode status for all operations.

## Example Usage
This module is in recovery mode and provides minimal functionality.
"""
        Path(module_path).write_text(minimal_content)
```

### Command Execution Recovery
```python
class CommandRecovery:
    """Recover from command execution failures."""
    
    @staticmethod
    def recover_from_timeout(command: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Handle command timeout scenarios.
        
        Args:
            command: Command that timed out
            context: Execution context
            
        Returns:
            Recovery result
        """
        recovery_options = {
            'retry': 'Retry with longer timeout',
            'simplify': 'Break into smaller operations',
            'skip': 'Skip this operation',
            'debug': 'Run in debug mode'
        }
        
        print(f"\n⚠️  Command timed out: {command}")
        print("Recovery options:")
        for key, desc in recovery_options.items():
            print(f"  {key}: {desc}")
        
        choice = input("\nChoose recovery option (retry/simplify/skip/debug): ").lower()
        
        if choice == 'retry':
            # Retry with 2x timeout
            new_timeout = context.get('timeout', 30) * 2
            print(f"Retrying with {new_timeout}s timeout...")
            return {'action': 'retry', 'timeout': new_timeout}
        
        elif choice == 'simplify':
            # Provide guidance on breaking down
            print("Consider breaking this operation into:")
            print("1. Smaller, focused commands")
            print("2. Intermediate checkpoints")
            print("3. Progress indicators")
            return {'action': 'simplify', 'guidance': 'provided'}
        
        elif choice == 'skip':
            print("Skipping operation. You may need to complete it manually.")
            return {'action': 'skip', 'manual': True}
        
        else:  # debug
            print("Running in debug mode with verbose output...")
            return {'action': 'debug', 'verbose': True}
```

## 💾 Data Recovery

### Session Recovery
```python
import pickle
import json
from datetime import datetime

class SessionRecovery:
    """Recover lost session data."""
    
    def __init__(self, session_dir: str = ".claude/sessions"):
        self.session_dir = Path(session_dir)
        self.session_dir.mkdir(exist_ok=True)
    
    def create_checkpoint(self, session_id: str, data: Dict[str, Any]) -> str:
        """
        Create session checkpoint for recovery.
        
        Args:
            session_id: Current session ID
            data: Session data to checkpoint
            
        Returns:
            Checkpoint ID
        """
        checkpoint_id = f"{session_id}_{int(time.time())}"
        checkpoint_file = self.session_dir / f"{checkpoint_id}.checkpoint"
        
        # Save in multiple formats for redundancy
        checkpoint_data = {
            'session_id': session_id,
            'timestamp': datetime.now().isoformat(),
            'data': data
        }
        
        # Primary: JSON (human readable)
        try:
            with open(checkpoint_file, 'w') as f:
                json.dump(checkpoint_data, f, indent=2)
        except:
            # Fallback: Pickle (handles more types)
            with open(checkpoint_file.with_suffix('.pkl'), 'wb') as f:
                pickle.dump(checkpoint_data, f)
        
        return checkpoint_id
    
    def recover_session(self, session_id: str) -> Dict[str, Any]:
        """
        Recover most recent session data.
        
        Args:
            session_id: Session to recover
            
        Returns:
            Recovered session data
        """
        # Find all checkpoints for session
        checkpoints = list(self.session_dir.glob(f"{session_id}_*.checkpoint"))
        checkpoints.extend(self.session_dir.glob(f"{session_id}_*.pkl"))
        
        if not checkpoints:
            print(f"No checkpoints found for session: {session_id}")
            return {}
        
        # Sort by timestamp (newest first)
        checkpoints.sort(key=lambda p: p.stat().st_mtime, reverse=True)
        
        # Try to recover from newest checkpoint
        for checkpoint in checkpoints:
            try:
                if checkpoint.suffix == '.checkpoint':
                    with open(checkpoint, 'r') as f:
                        data = json.load(f)
                else:  # .pkl
                    with open(checkpoint, 'rb') as f:
                        data = pickle.load(f)
                
                print(f"✓ Recovered session from: {checkpoint.name}")
                print(f"  Timestamp: {data['timestamp']}")
                return data['data']
                
            except Exception as e:
                print(f"✗ Failed to recover from {checkpoint.name}: {e}")
                continue
        
        print("✗ All recovery attempts failed")
        return {}
```

### Work Recovery
```python
class WorkRecovery:
    """Recover unsaved work and changes."""
    
    def __init__(self):
        self.work_dir = Path(".claude/recovery/work")
        self.work_dir.mkdir(parents=True, exist_ok=True)
    
    def auto_save(self, file_path: str, content: str) -> None:
        """
        Auto-save work for recovery.
        
        Args:
            file_path: Original file path
            content: Content to save
        """
        # Create recovery file name
        original = Path(file_path)
        recovery_name = f"{original.stem}_autosave_{int(time.time())}{original.suffix}"
        recovery_path = self.work_dir / recovery_name
        
        # Save with metadata
        metadata = {
            'original_path': str(file_path),
            'saved_at': datetime.now().isoformat(),
            'size': len(content)
        }
        
        # Save content
        recovery_path.write_text(content)
        
        # Save metadata
        meta_path = recovery_path.with_suffix('.meta')
        meta_path.write_text(json.dumps(metadata, indent=2))
        
        # Clean old autosaves (keep last 10)
        self._cleanup_old_autosaves(original.stem)
    
    def recover_unsaved_work(self, file_path: str) -> Optional[str]:
        """
        Recover most recent unsaved work.
        
        Args:
            file_path: Original file path
            
        Returns:
            Recovered content or None
        """
        original = Path(file_path)
        pattern = f"{original.stem}_autosave_*{original.suffix}"
        
        autosaves = list(self.work_dir.glob(pattern))
        if not autosaves:
            return None
        
        # Get most recent
        latest = max(autosaves, key=lambda p: p.stat().st_mtime)
        
        # Check if newer than original
        if original.exists() and latest.stat().st_mtime < original.stat().st_mtime:
            return None  # Original is newer
        
        content = latest.read_text()
        
        # Show recovery info
        meta_path = latest.with_suffix('.meta')
        if meta_path.exists():
            metadata = json.loads(meta_path.read_text())
            print(f"✓ Found autosave from: {metadata['saved_at']}")
            print(f"  Size: {metadata['size']} characters")
        
        return content
```

## 🔧 Operation Recovery

### Git Operation Recovery
```python
class GitRecovery:
    """Recover from git operation failures."""
    
    @staticmethod
    def recover_from_merge_conflict() -> bool:
        """
        Guide through merge conflict resolution.
        
        Returns:
            True if resolved successfully
        """
        print("\n⚠️  Merge conflict detected!")
        print("\nRecovery options:")
        print("1. Accept current changes (--ours)")
        print("2. Accept incoming changes (--theirs)")
        print("3. Manual resolution")
        print("4. Abort merge")
        
        choice = input("\nChoose option (1-4): ")
        
        try:
            if choice == '1':
                subprocess.run(["git", "checkout", "--ours", "."], check=True)
                subprocess.run(["git", "add", "."], check=True)
                print("✓ Accepted current changes")
                return True
                
            elif choice == '2':
                subprocess.run(["git", "checkout", "--theirs", "."], check=True)
                subprocess.run(["git", "add", "."], check=True)
                print("✓ Accepted incoming changes")
                return True
                
            elif choice == '3':
                print("\nFiles with conflicts:")
                result = subprocess.run(
                    ["git", "diff", "--name-only", "--diff-filter=U"],
                    capture_output=True, text=True
                )
                print(result.stdout)
                print("\nResolve conflicts manually, then run:")
                print("  git add .")
                print("  git commit")
                return False
                
            else:  # abort
                subprocess.run(["git", "merge", "--abort"], check=True)
                print("✓ Merge aborted")
                return True
                
        except subprocess.CalledProcessError as e:
            print(f"✗ Recovery failed: {e}")
            return False
    
    @staticmethod  
    def create_safety_branch() -> str:
        """
        Create safety branch before risky operations.
        
        Returns:
            Branch name created
        """
        branch_name = f"safety-backup-{int(time.time())}"
        
        try:
            # Create branch at current HEAD
            subprocess.run(
                ["git", "branch", branch_name],
                check=True,
                capture_output=True
            )
            print(f"✓ Created safety branch: {branch_name}")
            print(f"  To recover: git checkout {branch_name}")
            return branch_name
            
        except subprocess.CalledProcessError:
            print("✗ Could not create safety branch")
            return ""
```

## 🚨 Emergency Recovery

### Panic Recovery
```python
def emergency_recovery():
    """
    Emergency recovery when framework is broken.
    
    This function can be run standalone without framework dependencies.
    """
    print("\n🚨 EMERGENCY RECOVERY MODE 🚨\n")
    
    print("Checking framework integrity...")
    
    issues = []
    
    # Check critical files
    critical_files = [
        'CLAUDE.md',
        'PROJECT_CONFIG.xml',
        '.claude/modules',
        '.claude/system'
    ]
    
    for file_path in critical_files:
        if not Path(file_path).exists():
            issues.append(f"Missing: {file_path}")
    
    if not issues:
        print("✓ All critical files present")
    else:
        print("✗ Found issues:")
        for issue in issues:
            print(f"  - {issue}")
    
    print("\nRecovery options:")
    print("1. Restore from git")
    print("2. Download fresh framework")
    print("3. Minimal mode")
    print("4. Exit")
    
    choice = input("\nChoose option (1-4): ")
    
    if choice == '1':
        # Git restore
        try:
            subprocess.run(["git", "status"], check=True, capture_output=True)
            subprocess.run(["git", "checkout", "HEAD", "--", ".claude", "CLAUDE.md"], check=True)
            print("✓ Restored framework from git")
        except:
            print("✗ Git restore failed")
    
    elif choice == '2':
        # Download fresh
        print("\nTo download fresh framework:")
        print("1. Visit: https://github.com/your-framework-repo")
        print("2. Download .claude directory and CLAUDE.md")
        print("3. Extract to project root")
    
    elif choice == '3':
        # Minimal mode
        print("\nEntering minimal mode...")
        print("Basic operations available:")
        print("- File reading/writing")
        print("- Git operations")
        print("- Command execution")
        print("\nFramework features disabled")
    
    else:
        print("Exiting recovery mode")

# Run if called directly
if __name__ == "__main__":
    emergency_recovery()
```

## 📋 Recovery Patterns Quick Reference

### Pattern: Command Failed
```python
try:
    result = execute_command(cmd)
except CommandError as e:
    # 1. Log failure
    logger.error(f"Command failed: {e}")
    
    # 2. Attempt recovery
    recovery = CommandRecovery.recover_from_timeout(cmd, context)
    
    # 3. Retry if appropriate
    if recovery['action'] == 'retry':
        result = execute_command(cmd, timeout=recovery['timeout'])
```

### Pattern: File Operation Failed
```python
try:
    write_file(path, content)
except IOError as e:
    # 1. Auto-save content
    WorkRecovery().auto_save(path, content)
    
    # 2. Inform user
    print(f"✗ Could not write file: {e}")
    print(f"✓ Content saved to recovery")
    
    # 3. Provide options
    print("Options:")
    print(f"1. Try different location")
    print(f"2. Fix permissions and retry")
```

### Pattern: State Corruption
```python
try:
    state = load_state()
except StateError:
    # 1. Try recovery
    state = SessionRecovery().recover_session(session_id)
    
    # 2. Fall back to defaults
    if not state:
        state = get_default_state()
        print("✓ Using default state")
```

## 🎯 Recovery Best Practices

1. **Always Create Checkpoints**
   - Before risky operations
   - At logical boundaries
   - Periodically during long operations

2. **Make Recovery Visible**
   - Clear error messages
   - Show recovery progress
   - Confirm successful recovery

3. **Preserve User Work**
   - Auto-save frequently
   - Never lose user input
   - Keep multiple backups

4. **Test Recovery Paths**
   - Simulate failures
   - Verify recovery works
   - Document procedures

5. **Learn from Failures**
   - Log all failures
   - Analyze patterns
   - Improve prevention

---

Remember: The best recovery is prevention, but when things fail, fail gracefully and recover quickly.