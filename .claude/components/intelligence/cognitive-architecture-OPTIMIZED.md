# Cognitive Architecture

**Purpose**: Advanced cognitive framework implementing ACT-R, SOAR, CLARION architectures for human-like intelligent reasoning and adaptive learning.

**Usage**: 
- Implement hybrid cognitive systems with symbolic and connectionist reasoning
- Build memory systems (declarative, procedural, working memory) with learning
- Enable metacognitive monitoring and self-regulation capabilities
- Support analogical reasoning, case-based reasoning, and rule-based systems
- Integrate emotional and motivational components for human-like behavior

**Compatibility**: 
- **Works with**: multi-agent-coordination, agent-orchestration, agent-swarm, task-planning
- **Requires**: Complex reasoning tasks requiring human-like intelligence
- **Conflicts**: quick-command (complexity mismatch), file-reader (scope mismatch)

**Implementation**:
```python
# Initialize hybrid cognitive architecture
def create_cognitive_agent():
    memory = initialize_memory_systems(declarative=True, procedural=True, working=True)
    reasoning = setup_hybrid_reasoning(symbolic=True, connectionist=True)
    metacognition = enable_metacognitive_monitoring()
    learning = configure_adaptive_learning_mechanisms()
    return CognitiveAgent(memory, reasoning, metacognition, learning)

# Execute cognitive processing
def cognitive_process(problem, agent):
    working_memory = activate_relevant_knowledge(problem, agent.memory)
    solution_paths = generate_reasoning_strategies(working_memory)
    best_solution = evaluate_and_select_solution(solution_paths)
    agent.learn_from_experience(problem, best_solution)
    return best_solution
```

**Category**: intelligence | **Complexity**: very_high | **Time**: 2 weeks