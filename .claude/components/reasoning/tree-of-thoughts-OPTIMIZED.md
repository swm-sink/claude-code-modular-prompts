# Tree of Thoughts Reasoning

**Purpose**: Advanced Tree of Thoughts reasoning framework enabling multi-path exploration, thought tree construction, branch evaluation, and path synthesis for comprehensive problem-solving.

**Usage**: 
- Explores multiple reasoning paths simultaneously from root problem statement
- Evaluates branch quality and potential through systematic analysis
- Expands most promising branches for deeper exploration
- Synthesizes best elements from all paths into optimal solution
- Supports customizable exploration style (depth-first, breadth-first, balanced)

**Compatibility**: 
- **Works with**: react-reasoning, pattern-extraction, cognitive-architecture, prompt-optimization
- **Requires**: problem_statement, branching_factor, evaluation_criteria
- **Conflicts**: None (enhances other reasoning approaches)

**Implementation**:
```xml
<tot_structure>
  <root>Initial problem statement</root>
  <branches>[branch_1, branch_2, branch_3]</branches>
  <evaluation>Compare branch quality and potential</evaluation>
  <expansion>Develop most promising branches</expansion>
  <synthesis>Combine best elements into solution</synthesis>
</tot_structure>
```

**Category**: reasoning | **Complexity**: moderate | **Time**: 1-2 hours