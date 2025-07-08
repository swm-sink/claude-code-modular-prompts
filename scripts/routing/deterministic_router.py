#!/usr/bin/env python3
"""
Deterministic Router Implementation
Replaces fuzzy scoring with explicit component counting
"""

import json
import hashlib
from datetime import datetime, timezone, timedelta
from pathlib import Path
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass, asdict


@dataclass
class ComponentCounts:
    """Explicit component counts for routing decisions"""
    files_to_read: int = 0
    files_to_modify: int = 0
    files_to_create: int = 0
    files_to_delete: int = 0
    functions_affected: int = 0
    classes_affected: int = 0
    tests_to_write: int = 0
    tests_to_modify: int = 0
    cross_module_deps: int = 0
    external_deps: int = 0
    breaking_changes: int = 0
    architecture_decisions: int = 0
    
    @property
    def total_files(self) -> int:
        return (self.files_to_read + self.files_to_modify + 
                self.files_to_create + self.files_to_delete)
    
    @property
    def total_test_work(self) -> int:
        return self.tests_to_write + self.tests_to_modify


@dataclass
class RoutingDecision:
    """Routing decision with full transparency"""
    command: str
    confidence: float
    primary_reason: str
    counts: ComponentCounts
    alternatives: Dict[str, str]
    timestamp: str = ""
    artifact_id: str = ""
    
    def __post_init__(self):
        if not self.timestamp:
            self.timestamp = datetime.now(timezone.utc).isoformat()
        if not self.artifact_id:
            self.artifact_id = self._generate_id()
    
    def _generate_id(self) -> str:
        """Generate unique artifact ID"""
        content = f"{self.timestamp}-{self.command}-{self.primary_reason}"
        hash_obj = hashlib.sha256(content.encode())
        return f"{self.timestamp[:10]}-routing-{hash_obj.hexdigest()[:8]}"


class DeterministicRouter:
    """Routes requests based on deterministic component counting"""
    
    def __init__(self, artifact_dir: Path = None):
        self.artifact_dir = artifact_dir or Path(".claude/context/artifacts")
        self.thresholds = self._load_thresholds()
        
    def _load_thresholds(self) -> dict:
        """Load command thresholds"""
        return {
            '/task': {
                'max_files_total': 3,
                'max_cross_module_deps': 0,
                'max_breaking_changes': 0,
                'max_architecture_decisions': 0
            },
            '/feature': {
                'min_files_total': 2,
                'max_files_total': 10,
                'max_cross_module_deps': 2,
                'min_architecture_decisions': 1,
                'requires_tests': True
            },
            '/swarm': {
                'min_files_total': 10,
                'min_cross_module_deps': 3,
                'allows_breaking_changes': True,
                'parallel_possible': True
            },
            '/query': {
                'max_files_modify': 0,
                'max_files_create': 0,
                'research_only': True
            }
        }
    
    def route_request(self, request: str, counts: ComponentCounts) -> RoutingDecision:
        """Route request based on component counts"""
        # Check each command in order
        alternatives = {}
        
        # Check /query first (read-only)
        if self._can_use_query(counts):
            return RoutingDecision(
                command='/query',
                confidence=1.0,
                primary_reason='Read-only research request',
                counts=counts,
                alternatives=alternatives
            )
        
        # Check /task (simplest)
        if self._can_use_task(counts):
            return RoutingDecision(
                command='/task',
                confidence=0.95,
                primary_reason=f'Simple task affecting {counts.total_files} files',
                counts=counts,
                alternatives=alternatives
            )
        else:
            alternatives['/task'] = self._why_not_task(counts)
        
        # Check /feature (design-driven)
        if self._can_use_feature(counts):
            return RoutingDecision(
                command='/feature',
                confidence=0.95,
                primary_reason='Feature requiring design and tests',
                counts=counts,
                alternatives=alternatives
            )
        else:
            alternatives['/feature'] = self._why_not_feature(counts)
        
        # Check /swarm (complex)
        if self._should_use_swarm(counts):
            return RoutingDecision(
                command='/swarm',
                confidence=0.90,
                primary_reason='Complex multi-component task',
                counts=counts,
                alternatives=alternatives
            )
        else:
            alternatives['/swarm'] = self._why_not_swarm(counts)
        
        # Default to /auto
        return RoutingDecision(
            command='/auto',
            confidence=0.70,
            primary_reason='Requirements need clarification',
            counts=counts,
            alternatives=alternatives
        )
    
    def _can_use_query(self, counts: ComponentCounts) -> bool:
        """Check if request is query-only"""
        return (counts.files_to_modify == 0 and 
                counts.files_to_create == 0 and
                counts.files_to_read > 0)
    
    def _can_use_task(self, counts: ComponentCounts) -> bool:
        """Check if request fits /task thresholds"""
        t = self.thresholds['/task']
        return (counts.total_files <= t['max_files_total'] and
                counts.cross_module_deps <= t['max_cross_module_deps'] and
                counts.breaking_changes <= t['max_breaking_changes'] and
                counts.architecture_decisions <= t['max_architecture_decisions'])
    
    def _can_use_feature(self, counts: ComponentCounts) -> bool:
        """Check if request fits /feature thresholds"""
        t = self.thresholds['/feature']
        return (t['min_files_total'] <= counts.total_files <= t['max_files_total'] and
                counts.cross_module_deps <= t['max_cross_module_deps'] and
                counts.architecture_decisions >= t['min_architecture_decisions'] and
                counts.total_test_work > 0)
    
    def _should_use_swarm(self, counts: ComponentCounts) -> bool:
        """Check if request requires /swarm"""
        t = self.thresholds['/swarm']
        return (counts.total_files >= t['min_files_total'] or
                counts.cross_module_deps >= t['min_cross_module_deps'] or
                counts.breaking_changes > 0)
    
    def _why_not_task(self, counts: ComponentCounts) -> str:
        """Explain why /task cannot be used"""
        t = self.thresholds['/task']
        if counts.total_files > t['max_files_total']:
            return f"Too many files ({counts.total_files} > {t['max_files_total']})"
        if counts.cross_module_deps > t['max_cross_module_deps']:
            return f"Cross-module dependencies ({counts.cross_module_deps} > 0)"
        if counts.breaking_changes > 0:
            return "Contains breaking changes"
        if counts.architecture_decisions > 0:
            return "Requires architecture decisions"
        return "Does not meet /task criteria"
    
    def _why_not_feature(self, counts: ComponentCounts) -> str:
        """Explain why /feature cannot be used"""
        t = self.thresholds['/feature']
        if counts.total_files < t['min_files_total']:
            return f"Too few files ({counts.total_files} < {t['min_files_total']})"
        if counts.total_files > t['max_files_total']:
            return f"Too many files ({counts.total_files} > {t['max_files_total']})"
        if counts.architecture_decisions < t['min_architecture_decisions']:
            return "No architecture decisions needed"
        if counts.total_test_work == 0:
            return "No tests required"
        return "Does not meet /feature criteria"
    
    def _why_not_swarm(self, counts: ComponentCounts) -> str:
        """Explain why /swarm is not needed"""
        if counts.total_files < 10 and counts.cross_module_deps < 3:
            return "Not complex enough for parallel work"
        return "Does not require /swarm complexity"
    
    def save_decision_artifact(self, decision: RoutingDecision, request: str) -> str:
        """Save routing decision as artifact"""
        artifact = {
            'id': decision.artifact_id,
            'version': '1.0.0',
            'type': 'routing',
            'timestamp': decision.timestamp,
            'metadata': {
                'priority': 'high',
                'preserve_until': (datetime.now(timezone.utc) + 
                                 timedelta(days=30)).isoformat(),
                'compression_safe': True
            },
            'context': {
                'user_request': request,
                'framework_version': '2.3.0'
            },
            'decision': {
                'type': 'command_selection',
                'counts': asdict(decision.counts),
                'chosen_command': decision.command,
                'confidence': decision.confidence,
                'primary_reason': decision.primary_reason,
                'alternatives': decision.alternatives
            }
        }
        
        # Save artifact
        date_dir = self.artifact_dir / decision.timestamp[:10] / 'routing'
        date_dir.mkdir(parents=True, exist_ok=True)
        
        artifact_path = date_dir / f"{decision.artifact_id}.json"
        with open(artifact_path, 'w') as f:
            json.dump(artifact, f, indent=2)
        
        return str(artifact_path)
    
    def explain_decision(self, decision: RoutingDecision) -> str:
        """Generate user-friendly explanation"""
        explanation = f"""
🎯 Routing Decision: {decision.command}

📊 Component Analysis:
- Files affected: {decision.counts.total_files}
  - To read: {decision.counts.files_to_read}
  - To modify: {decision.counts.files_to_modify}
  - To create: {decision.counts.files_to_create}
- Tests needed: {decision.counts.total_test_work}
- Cross-module dependencies: {decision.counts.cross_module_deps}
- Architecture decisions: {decision.counts.architecture_decisions}

✅ Selected {decision.command} because: {decision.primary_reason}

❌ Alternatives considered:
"""
        for cmd, reason in decision.alternatives.items():
            explanation += f"- {cmd}: {reason}\n"
        
        explanation += f"\n🔍 Decision ID: {decision.artifact_id}"
        return explanation


# Example usage
if __name__ == "__main__":
    router = DeterministicRouter()
    
    # Example: Simple bug fix
    simple_counts = ComponentCounts(
        files_to_modify=1,
        functions_affected=2,
        tests_to_modify=1
    )
    
    decision = router.route_request("Fix authentication bug", simple_counts)
    print("Simple fix routing:")
    print(router.explain_decision(decision))
    print("-" * 60)
    
    # Example: Feature implementation
    feature_counts = ComponentCounts(
        files_to_create=3,
        files_to_modify=2,
        functions_affected=8,
        tests_to_write=5,
        architecture_decisions=2,
        cross_module_deps=1
    )
    
    decision = router.route_request("Add user authentication", feature_counts)
    print("\nFeature routing:")
    print(router.explain_decision(decision))
    print("-" * 60)
    
    # Example: Complex refactor
    complex_counts = ComponentCounts(
        files_to_modify=15,
        functions_affected=40,
        tests_to_modify=20,
        cross_module_deps=5,
        breaking_changes=2,
        architecture_decisions=3
    )
    
    decision = router.route_request("Refactor database layer", complex_counts)
    print("\nComplex routing:")
    print(router.explain_decision(decision))
    
    # Save artifacts
    for d in [decision]:
        path = router.save_decision_artifact(d, "Example request")
        print(f"\nArtifact saved: {path}")