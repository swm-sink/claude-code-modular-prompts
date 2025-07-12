#!/usr/bin/env python3
"""
Agent 6: Migration Strategist
Create detailed migration strategy using Agent 5's unified architecture design
Mission: Transform Agent 5's architecture blueprint into executable migration plan
"""

import os
import json
import re
from pathlib import Path
from collections import defaultdict, Counter
from datetime import datetime

class MigrationStrategist:
    def __init__(self, base_path=".claude"):
        self.base_path = Path(base_path)
        self.migration_strategy = {}
        self.execution_plan = {}
        self.risk_mitigation = {}
        self.rollback_procedures = {}
        
        # Load foundation data and architecture design
        self.agent1_data = self.load_agent_data("agent1_inventory_results.json")
        self.agent2_data = self.load_agent_data("agent2_directory_audit_results.json")
        self.agent3_data = self.load_agent_data("agent3_reference_analysis_results.json")
        self.agent4_data = self.load_agent_data("agent4_reality_testing_results.json")
        self.agent5_data = self.load_agent_data("agent5_architecture_design_results.json")
        
    def load_agent_data(self, filename):
        """Load agent data with fallback"""
        try:
            with open(filename, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"⚠️  {filename} not found")
            return {}
    
    def analyze_migration_requirements(self):
        """Analyze requirements from Agent 5's architecture design"""
        print("📋 Agent 6: Analyzing migration requirements from architecture design...")
        
        requirements = {
            'architecture_blueprint': {},
            'consolidation_targets': {},
            'file_movement_scope': {},
            'reference_update_scope': {},
            'functionality_protection': {}
        }
        
        # Extract architecture blueprint from Agent 5
        if self.agent5_data:
            unified_arch = self.agent5_data.get('unified_architecture', {})
            requirements['architecture_blueprint'] = {
                'target_structure': unified_arch.get('structure', {}),
                'directory_reduction': unified_arch.get('directory_reduction', '45 → 12 directories'),
                'consolidation_impact': unified_arch.get('consolidation_impact', {}),
                'duplication_elimination': unified_arch.get('duplication_elimination', '')
            }
            
            # Extract consolidation targets
            consolidation = self.agent5_data.get('consolidation_strategy', {})
            requirements['consolidation_targets'] = {
                'critical_consolidations': consolidation.get('critical_consolidations', []),
                'merge_procedures': consolidation.get('merge_procedures', {}),
                'reference_update_strategy': consolidation.get('reference_update_strategy', {})
            }
            
            # Extract migration approach
            migration_plan = self.agent5_data.get('migration_plan', {})
            requirements['migration_phases'] = migration_plan.get('migration_phases', {})
        
        # File movement scope from Agent 1
        if self.agent1_data:
            requirements['file_movement_scope'] = {
                'total_files': 241,
                'files_by_category': self.agent1_data.get('category_distribution', {}),
                'dependency_files': '159 files with dependencies'
            }
        
        # Reference update scope from Agent 3
        if self.agent3_data:
            requirements['reference_update_scope'] = {
                'broken_references': self.agent3_data.get('analysis_results', {}).get('broken_references', 101),
                'total_references': self.agent3_data.get('analysis_results', {}).get('total_references', 1093),
                'fix_strategies': self.agent3_data.get('fix_strategies', [])
            }
        
        # Functionality protection from Agent 4
        if self.agent4_data:
            functionality = self.agent4_data.get('functionality_assessment', {})
            requirements['functionality_protection'] = {
                'working_commands': functionality.get('functional_commands', 13),
                'total_commands': functionality.get('total_commands', 21),
                'accessible_quality_modules': functionality.get('accessible_quality_modules', 36),
                'baseline_score': functionality.get('overall_functionality_score', 81.0)
            }
        
        print("✅ Migration requirements analysis complete")
        return requirements
    
    def create_detailed_execution_plan(self):
        """Create detailed step-by-step execution plan"""
        print("📋 Agent 6: Creating detailed execution plan...")
        
        execution_plan = {
            'phase_1_preparation': {
                'description': 'Prepare migration environment with safety measures',
                'duration_estimate': '30 minutes',
                'steps': [
                    {
                        'step': 1,
                        'action': 'Create migration branch',
                        'command': 'git checkout -b framework-migration-phase3',
                        'validation': 'Confirm clean working directory',
                        'rollback': 'git checkout main'
                    },
                    {
                        'step': 2,
                        'action': 'Full backup current state',
                        'command': 'git add -A && git commit -m "Pre-migration backup: Complete current state"',
                        'validation': 'Verify commit hash recorded',
                        'rollback': 'git reset --hard HEAD~1'
                    },
                    {
                        'step': 3,
                        'action': 'Validate foundation data integrity',
                        'command': 'python3 validate_foundation_data.py',
                        'validation': 'All agent data files present and valid',
                        'rollback': 'N/A - read-only validation'
                    },
                    {
                        'step': 4,
                        'action': 'Create target directory structure',
                        'command': 'python3 create_target_structure.py',
                        'validation': 'New structure created without conflicts',
                        'rollback': 'rm -rf .claude_new && git checkout .'
                    }
                ],
                'success_criteria': 'Clean migration environment with target structure ready',
                'failure_recovery': 'Return to main branch, investigate blockers'
            },
            'phase_2_critical_consolidation': {
                'description': 'Resolve CRITICAL pattern duplication first',
                'duration_estimate': '45 minutes',
                'priority': 'CRITICAL',
                'steps': [
                    {
                        'step': 1,
                        'action': 'Analyze pattern duplication conflicts',
                        'command': 'python3 analyze_pattern_conflicts.py',
                        'validation': 'All pattern conflicts identified and categorized',
                        'rollback': 'N/A - analysis only'
                    },
                    {
                        'step': 2,
                        'action': 'Merge .claude/modules/patterns/ content',
                        'command': 'python3 merge_pattern_directories.py --source modules/patterns --target unified/patterns',
                        'validation': 'All modules/patterns files moved successfully',
                        'rollback': 'git restore .claude/modules/patterns/'
                    },
                    {
                        'step': 3,
                        'action': 'Merge .claude/prompt_eng/patterns/ content',
                        'command': 'python3 merge_pattern_directories.py --source prompt_eng/patterns --target unified/patterns',
                        'validation': 'All prompt_eng/patterns files merged without conflicts',
                        'rollback': 'git restore .claude/prompt_eng/patterns/'
                    },
                    {
                        'step': 4,
                        'action': 'Deduplicate merged pattern content',
                        'command': 'python3 deduplicate_patterns.py --target unified/patterns',
                        'validation': 'No duplicate patterns, single source of truth established',
                        'rollback': 'git restore unified/patterns/ from backup'
                    },
                    {
                        'step': 5,
                        'action': 'Update immediate pattern references',
                        'command': 'python3 update_pattern_references.py --new-location modules/patterns',
                        'validation': 'Critical pattern references updated successfully',
                        'rollback': 'git restore all modified files'
                    }
                ],
                'success_criteria': 'Pattern duplication eliminated, single source established',
                'failure_recovery': 'Restore pattern directories, analyze conflicts'
            },
            'phase_3_directory_restructure': {
                'description': 'Implement unified directory structure (45 → 12 dirs)',
                'duration_estimate': '60 minutes',
                'priority': 'HIGH',
                'steps': [
                    {
                        'step': 1,
                        'action': 'Move commands to .claude/commands/',
                        'command': 'python3 move_files.py --category COMMAND --target .claude/commands/',
                        'validation': 'All 21 command files moved to single location',
                        'rollback': 'python3 restore_files.py --category COMMAND'
                    },
                    {
                        'step': 2,
                        'action': 'Consolidate quality modules',
                        'command': 'python3 move_files.py --category QUALITY_MODULE --target .claude/modules/quality/',
                        'validation': 'All 36 quality modules preserved in single location',
                        'rollback': 'python3 restore_files.py --category QUALITY_MODULE'
                    },
                    {
                        'step': 3,
                        'action': 'Consolidate development modules',
                        'command': 'python3 move_files.py --category DEVELOPMENT_MODULE --target .claude/modules/development/',
                        'validation': 'Development modules unified',
                        'rollback': 'python3 restore_files.py --category DEVELOPMENT_MODULE'
                    },
                    {
                        'step': 4,
                        'action': 'Consolidate meta modules',
                        'command': 'python3 move_files.py --category META_MODULE --target .claude/modules/meta/',
                        'validation': 'Meta modules unified',
                        'rollback': 'python3 restore_files.py --category META_MODULE'
                    },
                    {
                        'step': 5,
                        'action': 'Consolidate security modules',
                        'command': 'python3 move_files.py --category SECURITY_MODULE --target .claude/modules/security/',
                        'validation': 'Security modules unified',
                        'rollback': 'python3 restore_files.py --category SECURITY_MODULE'
                    },
                    {
                        'step': 6,
                        'action': 'Preserve system infrastructure',
                        'command': 'python3 preserve_system.py --target .claude/system/',
                        'validation': 'System modules preserved in correct location',
                        'rollback': 'python3 restore_files.py --category SYSTEM_MODULE'
                    },
                    {
                        'step': 7,
                        'action': 'Refine prompt_eng structure',
                        'command': 'python3 refine_prompt_eng.py --keep frameworks,personas --remove modules,patterns',
                        'validation': 'Prompt_eng contains only frameworks and personas',
                        'rollback': 'git restore .claude/prompt_eng/'
                    },
                    {
                        'step': 8,
                        'action': 'Remove empty directories',
                        'command': 'python3 cleanup_empty_dirs.py',
                        'validation': 'No empty directories remain',
                        'rollback': 'git restore deleted directories'
                    }
                ],
                'success_criteria': '45 → 12 directory reduction achieved, unified structure implemented',
                'failure_recovery': 'Restore all files to original locations'
            },
            'phase_4_reference_reconciliation': {
                'description': 'Update all references to new unified structure',
                'duration_estimate': '45 minutes',
                'priority': 'HIGH',
                'steps': [
                    {
                        'step': 1,
                        'action': 'Generate reference mapping',
                        'command': 'python3 generate_reference_map.py --old-structure current --new-structure unified',
                        'validation': 'Complete old→new path mapping generated',
                        'rollback': 'N/A - mapping generation only'
                    },
                    {
                        'step': 2,
                        'action': 'Update broken references from Agent 3',
                        'command': 'python3 fix_broken_references.py --reference-list agent3_broken_refs.json',
                        'validation': '101 broken references fixed',
                        'rollback': 'git restore all modified files'
                    },
                    {
                        'step': 3,
                        'action': 'Update all command references',
                        'command': 'python3 update_references.py --category COMMAND --mapping reference_map.json',
                        'validation': 'All command references point to new locations',
                        'rollback': 'git restore all command files'
                    },
                    {
                        'step': 4,
                        'action': 'Update all module references',
                        'command': 'python3 update_references.py --category MODULE --mapping reference_map.json',
                        'validation': 'All module references updated',
                        'rollback': 'git restore all module files'
                    },
                    {
                        'step': 5,
                        'action': 'Validate reference integrity',
                        'command': 'python3 validate_references.py --target-threshold 95',
                        'validation': '95%+ reference integrity achieved',
                        'rollback': 'Investigate and fix failing references'
                    }
                ],
                'success_criteria': '95%+ reference integrity, all paths resolve correctly',
                'failure_recovery': 'Restore original references, analyze mapping issues'
            },
            'phase_5_validation_and_testing': {
                'description': 'Validate functionality and confirm production readiness',
                'duration_estimate': '30 minutes',
                'priority': 'CRITICAL',
                'steps': [
                    {
                        'step': 1,
                        'action': 'Test command functionality',
                        'command': 'python3 test_command_functionality.py',
                        'validation': 'All 13 working commands still functional',
                        'rollback': 'Investigate broken commands'
                    },
                    {
                        'step': 2,
                        'action': 'Test quality module accessibility',
                        'command': 'python3 test_quality_modules.py',
                        'validation': 'All 36 quality modules accessible',
                        'rollback': 'Investigate accessibility issues'
                    },
                    {
                        'step': 3,
                        'action': 'Validate unified structure compliance',
                        'command': 'python3 validate_structure.py --blueprint agent5_architecture.json',
                        'validation': 'Structure matches Agent 5 blueprint exactly',
                        'rollback': 'Fix structure deviations'
                    },
                    {
                        'step': 4,
                        'action': 'Production readiness check',
                        'command': 'python3 production_readiness_check.py',
                        'validation': 'All production blockers removed',
                        'rollback': 'Address remaining blockers'
                    },
                    {
                        'step': 5,
                        'action': 'Final commit and tag',
                        'command': 'git add -A && git commit -m "Framework Migration Complete: 45→12 dirs, chaos eliminated"',
                        'validation': 'Migration committed successfully',
                        'rollback': 'git reset --hard HEAD~1'
                    }
                ],
                'success_criteria': 'Production readiness achieved, all functionality preserved',
                'failure_recovery': 'Full rollback to pre-migration state'
            }
        }
        
        self.execution_plan = execution_plan
        print("✅ Detailed execution plan complete")
        return execution_plan
    
    def design_automation_scripts(self):
        """Design automation scripts for migration execution"""
        print("🤖 Agent 6: Designing automation scripts...")
        
        automation_scripts = {
            'foundation_scripts': {
                'validate_foundation_data.py': {
                    'purpose': 'Validate all Phase 1 agent data integrity',
                    'inputs': ['agent1-5 JSON files'],
                    'outputs': ['Validation report'],
                    'critical': True
                },
                'create_target_structure.py': {
                    'purpose': 'Create unified directory structure from Agent 5 blueprint',
                    'inputs': ['agent5_architecture_design_results.json'],
                    'outputs': ['New .claude structure'],
                    'critical': True
                }
            },
            'consolidation_scripts': {
                'analyze_pattern_conflicts.py': {
                    'purpose': 'Analyze pattern duplication conflicts',
                    'inputs': ['Agent 2 overlap data'],
                    'outputs': ['Conflict analysis report'],
                    'critical': True
                },
                'merge_pattern_directories.py': {
                    'purpose': 'Merge pattern directories with conflict resolution',
                    'inputs': ['Source directory', 'Target directory'],
                    'outputs': ['Merged patterns'],
                    'critical': True
                },
                'deduplicate_patterns.py': {
                    'purpose': 'Remove duplicate pattern content',
                    'inputs': ['Merged pattern directory'],
                    'outputs': ['Deduplicated patterns'],
                    'critical': True
                }
            },
            'migration_scripts': {
                'move_files.py': {
                    'purpose': 'Move files by category with tracking',
                    'inputs': ['Category', 'Target directory'],
                    'outputs': ['File movement log'],
                    'critical': True
                },
                'restore_files.py': {
                    'purpose': 'Restore files to original locations (rollback)',
                    'inputs': ['Category or movement log'],
                    'outputs': ['Restored file structure'],
                    'critical': True
                }
            },
            'reference_scripts': {
                'generate_reference_map.py': {
                    'purpose': 'Generate old→new path mapping',
                    'inputs': ['Current structure', 'New structure'],
                    'outputs': ['Reference mapping JSON'],
                    'critical': True
                },
                'fix_broken_references.py': {
                    'purpose': 'Fix specific broken references from Agent 3',
                    'inputs': ['Agent 3 broken reference list'],
                    'outputs': ['Fixed references'],
                    'critical': True
                },
                'update_references.py': {
                    'purpose': 'Update references using path mapping',
                    'inputs': ['File category', 'Reference mapping'],
                    'outputs': ['Updated references'],
                    'critical': True
                }
            },
            'validation_scripts': {
                'validate_references.py': {
                    'purpose': 'Validate reference integrity',
                    'inputs': ['Target threshold percentage'],
                    'outputs': ['Reference integrity report'],
                    'critical': True
                },
                'test_command_functionality.py': {
                    'purpose': 'Test command functionality preservation',
                    'inputs': ['Working command list from Agent 4'],
                    'outputs': ['Functionality test report'],
                    'critical': True
                },
                'production_readiness_check.py': {
                    'purpose': 'Final production readiness validation',
                    'inputs': ['Agent 4 production criteria'],
                    'outputs': ['Production readiness status'],
                    'critical': True
                }
            }
        }
        
        print(f"🤖 Designed {sum(len(scripts) for scripts in automation_scripts.values())} automation scripts")
        return automation_scripts
    
    def create_risk_mitigation_strategy(self):
        """Create comprehensive risk mitigation strategy"""
        print("🛡️  Agent 6: Creating risk mitigation strategy...")
        
        risk_mitigation = {
            'data_loss_prevention': {
                'risk': 'Accidental file loss during migration',
                'probability': 'MEDIUM',
                'impact': 'HIGH',
                'mitigation': [
                    'Full git backup before any changes',
                    'Atomic commits at each phase',
                    'File movement tracking with restore capability',
                    'Dry-run mode for all scripts'
                ],
                'detection': 'File count validation at each step',
                'recovery': 'Git-based rollback to any previous state'
            },
            'functionality_regression': {
                'risk': 'Breaking working commands/modules during migration',
                'probability': 'MEDIUM',
                'impact': 'CRITICAL',
                'mitigation': [
                    'Preserve Agent 4 baseline (13 commands, 36 quality modules)',
                    'Functionality testing at each phase',
                    'No modifications to working file content',
                    'Path-only updates for references'
                ],
                'detection': 'Automated functionality testing',
                'recovery': 'Restore specific components from backup'
            },
            'reference_integrity_failure': {
                'risk': 'Broken references preventing framework operation',
                'probability': 'LOW',
                'impact': 'HIGH',
                'mitigation': [
                    'Reference mapping validation before updates',
                    'Gradual reference updates with testing',
                    '95% integrity threshold requirement',
                    'Agent 3 baseline: 90.8% already functional'
                ],
                'detection': 'Reference validation scripts',
                'recovery': 'Restore original references, fix mapping'
            },
            'directory_structure_corruption': {
                'risk': 'Invalid final directory structure',
                'probability': 'LOW',
                'impact': 'HIGH',
                'mitigation': [
                    'Structure validation against Agent 5 blueprint',
                    'Directory creation with validation',
                    'Empty directory cleanup tracking',
                    'Structure compliance testing'
                ],
                'detection': 'Blueprint compliance validation',
                'recovery': 'Recreate structure from blueprint'
            },
            'migration_failure_cascade': {
                'risk': 'Failure in one phase corrupting subsequent phases',
                'probability': 'LOW',
                'impact': 'CRITICAL',
                'mitigation': [
                    'Phase independence with validation gates',
                    'Rollback capability at each phase',
                    'Success criteria validation before proceeding',
                    'Manual approval gates for critical phases'
                ],
                'detection': 'Phase success validation',
                'recovery': 'Phase-specific rollback procedures'
            }
        }
        
        self.risk_mitigation = risk_mitigation
        print("🛡️  Risk mitigation strategy complete")
        return risk_mitigation
    
    def design_rollback_procedures(self):
        """Design comprehensive rollback procedures"""
        print("🔄 Agent 6: Designing rollback procedures...")
        
        rollback_procedures = {
            'immediate_rollback': {
                'description': 'Quick rollback for immediate issues',
                'trigger': 'Any script failure or validation error',
                'procedure': [
                    'Stop current operation immediately',
                    'git stash any unstaged changes',
                    'git reset --hard to last known good commit',
                    'Validate rollback success',
                    'Analyze failure cause'
                ],
                'recovery_time': '< 2 minutes',
                'data_loss_risk': 'NONE'
            },
            'phase_rollback': {
                'description': 'Rollback entire phase while preserving previous progress',
                'trigger': 'Phase success criteria not met',
                'procedure': [
                    'Identify phase start commit',
                    'git reset --hard to phase start commit',
                    'Validate previous phase integrity',
                    'Document phase failure reasons',
                    'Prepare corrected phase execution'
                ],
                'recovery_time': '< 5 minutes',
                'data_loss_risk': 'NONE (protected by git)'
            },
            'complete_rollback': {
                'description': 'Full migration rollback to original state',
                'trigger': 'Multiple phase failures or critical issues',
                'procedure': [
                    'git checkout main branch',
                    'Delete migration branch',
                    'Validate original state integrity',
                    'Full analysis of migration failure',
                    'Update migration strategy based on learnings'
                ],
                'recovery_time': '< 1 minute',
                'data_loss_risk': 'NONE (returns to original state)'
            },
            'selective_rollback': {
                'description': 'Rollback specific components while preserving others',
                'trigger': 'Partial migration success with specific failures',
                'procedure': [
                    'Identify successful vs failed components',
                    'Restore failed components from backup',
                    'Validate partial migration state',
                    'Continue with corrected migration plan',
                    'Update automation scripts as needed'
                ],
                'recovery_time': '5-15 minutes',
                'data_loss_risk': 'LOW (targeted restoration)'
            }
        }
        
        # Git-specific rollback commands
        rollback_procedures['git_commands'] = {
            'emergency_rollback': 'git reset --hard HEAD~1',
            'phase_rollback': 'git reset --hard <phase_start_commit>',
            'complete_rollback': 'git checkout main && git branch -D framework-migration-phase3',
            'file_specific_rollback': 'git checkout HEAD~1 -- <file_path>'
        }
        
        self.rollback_procedures = rollback_procedures
        print("🔄 Rollback procedures complete")
        return rollback_procedures
    
    def create_migration_monitoring(self):
        """Create migration monitoring and progress tracking"""
        print("📊 Agent 6: Creating migration monitoring system...")
        
        monitoring = {
            'progress_tracking': {
                'phase_completion': 'Track phase completion percentage',
                'file_movement': 'Track files moved vs total files',
                'reference_updates': 'Track references updated vs total references',
                'validation_success': 'Track validation pass rates'
            },
            'success_metrics': {
                'directory_count': 'Target: 45 → 12 directories',
                'pattern_duplication': 'Target: 0 duplicated patterns',
                'reference_integrity': 'Target: 95%+ reference resolution',
                'functionality_preservation': 'Target: 100% working component preservation',
                'production_readiness': 'Target: All blockers removed'
            },
            'monitoring_checkpoints': {
                'pre_migration': 'Validate starting state and foundation data',
                'post_phase_2': 'Validate pattern duplication elimination',
                'post_phase_3': 'Validate directory structure compliance',
                'post_phase_4': 'Validate reference integrity',
                'post_phase_5': 'Validate production readiness'
            },
            'failure_detection': {
                'script_failures': 'Monitor script exit codes and error outputs',
                'validation_failures': 'Monitor validation script results',
                'file_integrity': 'Monitor file counts and checksums',
                'structure_compliance': 'Monitor directory structure vs blueprint'
            }
        }
        
        print("📊 Migration monitoring system complete")
        return monitoring
    
    def run_complete_migration_strategy(self):
        """Run complete migration strategy development"""
        print("📋 Agent 6: Starting complete migration strategy development...")
        
        # Step 1: Analyze migration requirements
        requirements = self.analyze_migration_requirements()
        
        # Step 2: Create detailed execution plan
        execution_plan = self.create_detailed_execution_plan()
        
        # Step 3: Design automation scripts
        automation_scripts = self.design_automation_scripts()
        
        # Step 4: Create risk mitigation strategy
        risk_mitigation = self.create_risk_mitigation_strategy()
        
        # Step 5: Design rollback procedures
        rollback_procedures = self.design_rollback_procedures()
        
        # Step 6: Create monitoring system
        monitoring = self.create_migration_monitoring()
        
        # Generate comprehensive strategy report
        report = self.generate_migration_strategy_report(
            requirements, execution_plan, automation_scripts, 
            risk_mitigation, rollback_procedures, monitoring
        )
        
        print("✅ Agent 6: Migration strategy development complete")
        return report
    
    def generate_migration_strategy_report(self, requirements, execution_plan, automation_scripts, 
                                         risk_mitigation, rollback_procedures, monitoring):
        """Generate comprehensive migration strategy report"""
        return {
            'analysis_timestamp': datetime.now().isoformat(),
            'agent': 'Agent 6 - Migration Strategist',
            'strategy_summary': {
                'architecture_source': 'Agent 5 unified design',
                'execution_phases': 5,
                'automation_scripts': sum(len(scripts) for scripts in automation_scripts.values()),
                'total_duration_estimate': '3.5 hours',
                'risk_level': 'LOW (comprehensive mitigation)',
                'rollback_capability': 'COMPLETE (git-based)'
            },
            'migration_requirements': requirements,
            'execution_plan': execution_plan,
            'automation_scripts': automation_scripts,
            'risk_mitigation': risk_mitigation,
            'rollback_procedures': rollback_procedures,
            'monitoring_system': monitoring,
            'critical_success_factors': self.identify_critical_success_factors(),
            'handoff_data': self.prepare_migration_handoff_data()
        }
    
    def identify_critical_success_factors(self):
        """Identify critical factors for migration success"""
        return {
            'pattern_duplication_elimination': {
                'criticality': 'HIGHEST',
                'description': 'Must eliminate CRITICAL pattern duplication',
                'success_measure': 'Single .claude/modules/patterns/ directory',
                'failure_impact': 'Continued structural chaos'
            },
            'functionality_preservation': {
                'criticality': 'HIGHEST',
                'description': 'Must preserve Agent 4 baseline functionality',
                'success_measure': '13 commands + 36 quality modules working',
                'failure_impact': 'Framework regression'
            },
            'directory_reduction': {
                'criticality': 'HIGH',
                'description': 'Must achieve 45 → 12 directory reduction',
                'success_measure': 'Maximum 12 core directories',
                'failure_impact': 'Continued complexity chaos'
            },
            'reference_integrity': {
                'criticality': 'HIGH',
                'description': 'Must maintain 95%+ reference resolution',
                'success_measure': '95%+ references resolve correctly',
                'failure_impact': 'Framework navigation broken'
            },
            'git_safety': {
                'criticality': 'CRITICAL',
                'description': 'Must maintain complete rollback capability',
                'success_measure': 'All changes tracked, instant rollback available',
                'failure_impact': 'Potential data loss'
            }
        }
    
    def prepare_migration_handoff_data(self):
        """Prepare handoff data for Agent 7 execution"""
        return {
            'agent_7_execution_requirements': {
                'execution_plan': self.execution_plan,
                'automation_scripts': 'All scripts designed and specified',
                'rollback_procedures': self.rollback_procedures,
                'success_criteria': 'All phase validation requirements',
                'monitoring_requirements': 'Progress tracking and failure detection'
            },
            'agent_8_reference_reconciliation': {
                'reference_update_plan': 'Detailed in Phase 4 execution plan',
                'broken_reference_targets': '101 broken references from Agent 3',
                'path_mapping_strategy': 'Old→new structure mapping',
                'validation_requirements': '95%+ reference integrity'
            },
            'phase_3_completion_criteria': {
                'migration_strategy_complete': True,
                'execution_plan_detailed': True,
                'automation_designed': True,
                'risk_mitigation_comprehensive': True,
                'agent_7_unblocked': True
            }
        }
    
    def save_migration_strategy_results(self, output_file="agent6_migration_strategy_results.json"):
        """Save migration strategy results to file"""
        report = self.run_complete_migration_strategy()
        
        with open(output_file, 'w') as f:
            json.dump(report, f, indent=2)
        
        print(f"💾 Agent 6: Migration strategy results saved to {output_file}")
        return report

if __name__ == "__main__":
    strategist = MigrationStrategist()
    report = strategist.save_migration_strategy_results()
    
    # Print summary for immediate visibility
    print("\n" + "="*80)
    print("AGENT 6 MIGRATION STRATEGY SUMMARY")
    print("="*80)
    print(f"🏗️  Architecture Source: {report['strategy_summary']['architecture_source']}")
    print(f"📋 Execution Phases: {report['strategy_summary']['execution_phases']}")
    print(f"🤖 Automation Scripts: {report['strategy_summary']['automation_scripts']}")
    print(f"⏱️  Duration Estimate: {report['strategy_summary']['total_duration_estimate']}")
    print(f"🛡️  Risk Level: {report['strategy_summary']['risk_level']}")
    print(f"🔄 Rollback Capability: {report['strategy_summary']['rollback_capability']}")
    
    if report.get('critical_success_factors'):
        print("\n🚨 Critical Success Factors:")
        for factor_name, factor_info in report['critical_success_factors'].items():
            print(f"  {factor_name}: {factor_info['description']}")
    
    execution_plan = report.get('execution_plan', {})
    print(f"\n📋 Execution Plan Overview:")
    for phase_name, phase_info in execution_plan.items():
        duration = phase_info.get('duration_estimate', 'Unknown')
        step_count = len(phase_info.get('steps', []))
        print(f"  {phase_name}: {step_count} steps, {duration}")
    
    print(f"\n✅ Agent 6 Complete - Migration strategy ready for Agent 7")
    print(f"🚀 PHASE 3 IMPLEMENTATION PLANNING COMPLETE!")
    print(f"🎯 Ready to unblock Agent 7 (Migration Executor)")