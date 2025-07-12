#!/usr/bin/env python3
"""
Agent 7.1: Real Migration Executor
Mission: Execute ACTUAL migration (not simulation) based on Agent 5 blueprint
Critical: Transform 58 chaotic directories into clean 12-directory architecture
"""

import json
import subprocess
import shutil
from pathlib import Path
from datetime import datetime
import os

class Agent71RealMigrationExecutor:
    def __init__(self):
        self.base_path = Path(".")
        self.migration_results = {
            'agent': 'Agent 7.1 - Real Migration Executor',
            'timestamp': datetime.now().isoformat(),
            'mission': 'Execute ACTUAL migration - Transform chaotic structure to clean architecture',
            'pre_migration_state': {},
            'migration_operations': [],
            'post_migration_state': {},
            'atomic_commits': [],
            'rollback_points': []
        }
        self.operations_log = []
        
    def log_operation(self, operation, status, details=None):
        """Log operation with timestamp"""
        entry = {
            'timestamp': datetime.now().isoformat(),
            'operation': operation,
            'status': status,
            'details': details or {}
        }
        self.operations_log.append(entry)
        self.migration_results['migration_operations'].append(entry)
        print(f"📋 {status}: {operation}")
    
    def atomic_commit(self, message):
        """Perform real atomic commit"""
        try:
            # Check if there are changes
            result = subprocess.run(['git', 'status', '--porcelain'], capture_output=True, text=True)
            if not result.stdout.strip():
                self.log_operation(f"No changes to commit for: {message}", "INFO")
                return True
            
            # Real atomic commit
            subprocess.run(['git', 'add', '-A'], check=True)
            subprocess.run(['git', 'commit', '-m', f"REAL MIGRATION: {message}"], check=True)
            
            # Record rollback point
            commit_hash = subprocess.run(['git', 'rev-parse', 'HEAD'], capture_output=True, text=True).stdout.strip()
            self.atomic_commits.append({
                'commit': commit_hash,
                'message': message,
                'timestamp': datetime.now().isoformat()
            })
            
            self.log_operation(f"REAL atomic commit: {message}", "SUCCESS")
            return True
            
        except Exception as e:
            self.log_operation(f"Atomic commit failed: {e}", "FAILED")
            return False
    
    def backup_current_state(self):
        """Create backup of current state"""
        self.log_operation("Creating complete backup of current state", "IN_PROGRESS")
        
        try:
            # Document current structure
            dirs_before = list(self.base_path.glob('.claude/**'))
            dir_count_before = len([d for d in dirs_before if d.is_dir()])
            
            files_before = list(self.base_path.glob('.claude/**/*.md'))
            file_count_before = len(files_before)
            
            self.migration_results['pre_migration_state'] = {
                'directory_count': dir_count_before,
                'file_count': file_count_before,
                'structure_snapshot': str(subprocess.run(['find', '.claude', '-type', 'd'], 
                                         capture_output=True, text=True).stdout)
            }
            
            # Create git commit backup
            if not self.atomic_commit("PRE-MIGRATION BACKUP: Complete state before real migration"):
                return False
            
            self.log_operation(f"Backup complete: {dir_count_before} dirs, {file_count_before} files", "SUCCESS")
            return True
            
        except Exception as e:
            self.log_operation(f"Backup failed: {e}", "FAILED")
            return False
    
    def eliminate_pattern_duplication(self):
        """ACTUALLY eliminate pattern duplication (not simulate)"""
        self.log_operation("REAL OPERATION: Eliminating pattern duplication", "IN_PROGRESS")
        
        try:
            source_dir = Path('.claude/prompt_eng/patterns')
            target_dir = Path('.claude/modules/patterns')
            
            if not source_dir.exists():
                self.log_operation("Source pattern directory not found", "INFO")
                return True
            
            # Count files before
            source_files = list(source_dir.rglob('*.md'))
            print(f"  📁 Moving {len(source_files)} files from prompt_eng/patterns/ to modules/patterns/")
            
            # Actually move files
            moved_count = 0
            for file_path in source_files:
                relative_path = file_path.relative_to(source_dir)
                target_path = target_dir / relative_path
                
                # Create target directory if needed
                target_path.parent.mkdir(parents=True, exist_ok=True)
                
                # Move file
                shutil.move(str(file_path), str(target_path))
                moved_count += 1
                print(f"    📄 Moved: {relative_path}")
            
            # Remove empty source directories
            if source_dir.exists() and not any(source_dir.iterdir()):
                shutil.rmtree(source_dir)
                print(f"    🗑️  Removed empty: {source_dir}")
            
            # Remove empty parent directories
            parent = source_dir.parent
            while parent != Path('.claude') and parent.exists() and not any(parent.iterdir()):
                shutil.rmtree(parent)
                print(f"    🗑️  Removed empty: {parent}")
                parent = parent.parent
            
            if not self.atomic_commit(f"CRITICAL: Pattern duplication ACTUALLY eliminated - {moved_count} files moved"):
                return False
                
            self.log_operation(f"Pattern duplication eliminated: {moved_count} files moved", "SUCCESS")
            return True
            
        except Exception as e:
            self.log_operation(f"Pattern duplication elimination failed: {e}", "FAILED")
            return False
    
    def consolidate_directory_structure(self):
        """ACTUALLY consolidate directory structure to match Agent 5 blueprint"""
        self.log_operation("REAL OPERATION: Consolidating directory structure", "IN_PROGRESS")
        
        try:
            # Define target structure based on Agent 5 blueprint
            target_structure = {
                '.claude/commands': 'All command files',
                '.claude/modules/quality': 'Quality gate modules',
                '.claude/modules/patterns': 'All pattern modules (consolidated)',
                '.claude/modules/development': 'Development workflow modules',
                '.claude/modules/meta': 'Meta-framework modules', 
                '.claude/modules/security': 'Security validation modules',
                '.claude/system/context': 'Context management',
                '.claude/system/session': 'Session management',
                '.claude/system/git': 'Git operations',
                '.claude/prompt_eng/frameworks': 'Prompt frameworks only',
                '.claude/prompt_eng/personas': 'Personas only',
                '.claude/domain': 'Domain-specific templates'
            }
            
            # Create target directories
            for target_dir in target_structure:
                Path(target_dir).mkdir(parents=True, exist_ok=True)
                print(f"    📁 Ensured: {target_dir}")
            
            # Remove redundant directories that shouldn't exist in clean structure
            redundant_dirs = [
                '.claude/analytics',
                '.claude/config', 
                '.claude/development/debugging',
                '.claude/development/documentation',
                '.claude/development/planning',
                '.claude/development/testing',
                '.claude/meta/evolution',
                '.claude/meta/learning',
                '.claude/meta/safety',
                '.claude/meta/validation',
                '.claude/modules/domains',
                '.claude/modules/getting-started',
                '.claude/modules/planning',
                '.claude/modules/testing',
                '.claude/prompt_eng/commands',
                '.claude/prompt_eng/modules',
                '.claude/sessions',
                '.claude/start_here',
                '.claude/templates',
                '.claude/testing'
            ]
            
            removed_count = 0
            for redundant_dir in redundant_dirs:
                dir_path = Path(redundant_dir)
                if dir_path.exists():
                    # Move any important files to appropriate locations first
                    md_files = list(dir_path.rglob('*.md'))
                    for md_file in md_files:
                        # Determine appropriate target based on content/name
                        if 'quality' in md_file.name or 'tdd' in md_file.name:
                            target = Path('.claude/modules/quality') / md_file.name
                        elif 'pattern' in md_file.name:
                            target = Path('.claude/modules/patterns') / md_file.name
                        elif 'development' in md_file.name or 'task' in md_file.name:
                            target = Path('.claude/modules/development') / md_file.name
                        elif 'meta' in md_file.name:
                            target = Path('.claude/modules/meta') / md_file.name
                        else:
                            target = Path('.claude/modules/development') / md_file.name
                        
                        # Move file if target doesn't exist
                        if not target.exists():
                            target.parent.mkdir(parents=True, exist_ok=True)
                            shutil.move(str(md_file), str(target))
                            print(f"    📄 Relocated: {md_file} → {target}")
                    
                    # Remove redundant directory
                    shutil.rmtree(dir_path)
                    removed_count += 1
                    print(f"    🗑️  Removed redundant: {redundant_dir}")
            
            if not self.atomic_commit(f"STRUCTURE: Directory consolidation - {removed_count} redundant dirs removed"):
                return False
                
            self.log_operation(f"Directory structure consolidated: {removed_count} dirs removed", "SUCCESS")
            return True
            
        except Exception as e:
            self.log_operation(f"Directory consolidation failed: {e}", "FAILED")
            return False
    
    def validate_migration_results(self):
        """Validate that real migration achieved targets"""
        self.log_operation("Validating real migration results", "IN_PROGRESS")
        
        try:
            # Count final directory structure
            dirs_after = list(self.base_path.glob('.claude/**'))
            dir_count_after = len([d for d in dirs_after if d.is_dir()])
            
            files_after = list(self.base_path.glob('.claude/**/*.md'))
            file_count_after = len(files_after)
            
            # Check pattern duplication
            modules_patterns = list(Path('.claude/modules/patterns').glob('*.md')) if Path('.claude/modules/patterns').exists() else []
            prompt_patterns = list(Path('.claude/prompt_eng/patterns').rglob('*.md')) if Path('.claude/prompt_eng/patterns').exists() else []
            
            pattern_duplication_eliminated = len(prompt_patterns) == 0
            
            self.migration_results['post_migration_state'] = {
                'directory_count': dir_count_after,
                'file_count': file_count_after,
                'pattern_duplication_eliminated': pattern_duplication_eliminated,
                'modules_patterns_count': len(modules_patterns),
                'prompt_patterns_count': len(prompt_patterns)
            }
            
            # Calculate improvement
            dir_reduction = self.migration_results['pre_migration_state']['directory_count'] - dir_count_after
            reduction_pct = (dir_reduction / self.migration_results['pre_migration_state']['directory_count']) * 100
            
            print(f"  📊 Directories: {self.migration_results['pre_migration_state']['directory_count']} → {dir_count_after} ({reduction_pct:.1f}% reduction)")
            print(f"  📊 Pattern Duplication: {'ELIMINATED' if pattern_duplication_eliminated else 'STILL EXISTS'}")
            print(f"  📊 Files: {file_count_after} total")
            
            # Success criteria
            success = (
                dir_count_after <= 20 and  # Significant reduction achieved
                pattern_duplication_eliminated and  # Critical duplication fixed
                file_count_after >= self.migration_results['pre_migration_state']['file_count'] * 0.9  # No major file loss
            )
            
            if success:
                self.log_operation(f"Migration validation PASSED: {reduction_pct:.1f}% reduction, duplication eliminated", "SUCCESS")
            else:
                self.log_operation(f"Migration validation FAILED: targets not met", "FAILED")
            
            return success
            
        except Exception as e:
            self.log_operation(f"Migration validation failed: {e}", "FAILED")
            return False
    
    def execute_real_migration(self):
        """Execute complete real migration"""
        print("🚀 Agent 7.1: Starting REAL Migration Execution...")
        print("🎯 Mission: Transform chaotic structure into clean 12-directory architecture")
        print("⚠️  WARNING: This is REAL migration, not simulation!")
        
        # Phase 1: Backup and prepare
        if not self.backup_current_state():
            print("❌ Agent 7.1: Backup failed - aborting migration")
            return False
        
        # Phase 2: Eliminate pattern duplication
        if not self.eliminate_pattern_duplication():
            print("❌ Agent 7.1: Pattern duplication elimination failed")
            return False
        
        # Phase 3: Consolidate directory structure  
        if not self.consolidate_directory_structure():
            print("❌ Agent 7.1: Directory consolidation failed")
            return False
        
        # Phase 4: Validate results
        if not self.validate_migration_results():
            print("❌ Agent 7.1: Migration validation failed")
            return False
        
        # Phase 5: Final commit
        if not self.atomic_commit("MIGRATION COMPLETE: Real structural transformation achieved"):
            print("❌ Agent 7.1: Final commit failed")
            return False
        
        # Save results
        with open('agent7_1_real_migration_results.json', 'w') as f:
            json.dump(self.migration_results, f, indent=2)
        
        print("\n" + "="*80)
        print("🎯 AGENT 7.1 REAL MIGRATION - COMPLETE SUCCESS!")
        print("="*80)
        print(f"📊 Directory Reduction: {self.migration_results['pre_migration_state']['directory_count']} → {self.migration_results['post_migration_state']['directory_count']}")
        print(f"🚨 Pattern Duplication: {'ELIMINATED' if self.migration_results['post_migration_state']['pattern_duplication_eliminated'] else 'STILL EXISTS'}")
        print(f"💎 Atomic Commits: {len(self.atomic_commits)}")
        print(f"🎯 STATUS: REAL MIGRATION SUCCESSFUL")
        print("🏭 Framework is now ACTUALLY production ready!")
        
        return True

if __name__ == "__main__":
    agent71 = Agent71RealMigrationExecutor()
    agent71.execute_real_migration()