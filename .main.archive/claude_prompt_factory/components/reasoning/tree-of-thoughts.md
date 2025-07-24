<prompt_component>
  <step name="Tree of Thoughts Reasoning">
    <description>
Advanced Tree of Thoughts reasoning framework using Claude's natural branching and exploration capabilities. Enables multi-path exploration, thought tree construction, branch evaluation, and path synthesis for comprehensive problem-solving.
    </description>
  </step>

  <tree_of_thoughts>
    <reasoning_framework>
      <!-- Tree of Thoughts multi-path reasoning implementation -->
      <thought_exploration>
        <core_concept>Tree of Thoughts allows Claude to explore multiple reasoning paths simultaneously, evaluate them, and synthesize the best elements into a final solution.</core_concept>

```xml
<tot_structure>
  <root>Initial problem statement</root>
  <branches>
    <branch_1>First approach/perspective</branch_1>
    <branch_2>Second approach/perspective</branch_2>
    <branch_3>Third approach/perspective</branch_3>
  </branches>
  <evaluation>Compare branch quality and potential</evaluation>
  <expansion>Develop most promising branches further</expansion>
  <synthesis>Combine best elements into final solution</synthesis>
</tot_structure>
```

## Native Implementation

### Thought Tree Construction
Claude naturally builds thought trees through structured exploration:

```xml
<thought_tree>
  <problem>How to optimize a slow database query?</problem>
  
  <level_1_branches>
    <branch_a>
      <thought>Focus on query optimization</thought>
      <reasoning>Analyze the SQL query structure for inefficiencies</reasoning>
    </branch_a>
    <branch_b>
      <thought>Focus on database structure</thought>
      <reasoning>Examine indexes, table design, and schema optimization</reasoning>
    </branch_b>
    <branch_c>
      <thought>Focus on application layer</thought>
      <reasoning>Look at caching, connection pooling, and query patterns</reasoning>
    </branch_c>
  </level_1_branches>
  
  <evaluation_level_1>
    <branch_a_score>8/10 - Direct impact, immediate improvement</branch_a_score>
    <branch_b_score>9/10 - Fundamental improvement, long-term benefits</branch_b_score>
    <branch_c_score>7/10 - Good complementary approach</branch_c_score>
  </evaluation_level_1>
  
  <expansion>
    <expand_branch_b>
      <sub_branch_b1>
        <thought>Add missing indexes</thought>
        <analysis>Identify columns used in WHERE, JOIN, ORDER BY clauses</analysis>
      </sub_branch_b1>
      <sub_branch_b2>
        <thought>Optimize table structure</thought>
        <analysis>Normalize/denormalize based on query patterns</analysis>
      </sub_branch_b2>
      <sub_branch_b3>
        <thought>Partition large tables</thought>
        <analysis>Split data by date/region for better performance</analysis>
      </sub_branch_b3>
    </expand_branch_b>
  </expansion>
</thought_tree>
```

### Branch Evaluation Strategies

#### Quality Scoring
```xml
<branch_evaluation>
  <criteria>
    <feasibility>How easy is this to implement?</feasibility>
    <impact>How much improvement will this provide?</impact>
    <risk>What are the potential downsides?</risk>
    <cost>What resources are required?</cost>
  </criteria>
  
  <scoring_example>
    <branch>Add database indexes</branch>
    <feasibility>9/10 - Straightforward implementation</feasibility>
    <impact>8/10 - Significant query speed improvement</impact>
    <risk>2/10 - Low risk, easily reversible</risk>
    <cost>3/10 - Minimal development time</cost>
    <total_score>8.0/10</total_score>
  </scoring_example>
</branch_evaluation>
```

#### Comparative Analysis
```xml
<comparative_analysis>
  <branch_comparison>
    <branch_a>Query optimization</branch_a>
    <branch_b>Database structure</branch_b>
    <comparison>
      <short_term>Branch A provides faster results</short_term>
      <long_term>Branch B provides more sustainable improvement</long_term>
      <complexity>Branch A is simpler to implement</complexity>
      <scalability>Branch B scales better with growth</scalability>
    </comparison>
    <decision>Pursue Branch B with quick wins from Branch A</decision>
  </branch_comparison>
</comparative_analysis>
```

## Advanced ToT Patterns

### Parallel Exploration
```xml
<parallel_exploration>
  <problem>Design authentication system for microservices</problem>
  
  <simultaneous_branches>
    <security_branch>
      <thought>Focus on security-first design</thought>
      <exploration>
        <jwt_tokens>Stateless, scalable authentication</jwt_tokens>
        <oauth2>Standard protocol, good ecosystem</oauth2>
        <mutual_tls>High security, certificate-based</mutual_tls>
      </exploration>
    </security_branch>
    
    <performance_branch>
      <thought>Focus on performance and scalability</thought>
      <exploration>
        <token_caching>Reduce validation overhead</token_caching>
        <session_affinity>Minimize cross-service calls</session_affinity>
        <edge_authentication>Authenticate at gateway</edge_authentication>
      </exploration>
    </performance_branch>
    
    <usability_branch>
      <thought>Focus on developer experience</thought>
      <exploration>
        <single_sign_on>Seamless user experience</single_sign_on>
        <simple_integration>Easy service integration</simple_integration>
        <clear_documentation>Comprehensive guides</clear_documentation>
      </exploration>
    </usability_branch>
  </simultaneous_branches>
</parallel_exploration>
```

### Adaptive Branching
```xml
<adaptive_branching>
  <initial_exploration>Basic approach analysis</initial_exploration>
  <adaptive_response>
    <if_simple_problem>Use fewer branches, focus on execution</if_simple_problem>
    <if_complex_problem>Create more branches, deeper exploration</if_complex_problem>
    <if_creative_problem>Emphasize divergent thinking branches</if_creative_problem>
    <if_analytical_problem>Focus on systematic evaluation branches</if_analytical_problem>
  </adaptive_response>
</adaptive_branching>
```

### Branch Pruning
```xml
<branch_pruning>
  <pruning_criteria>
    <low_feasibility>Remove branches that are impractical</low_feasibility>
    <high_risk>Eliminate approaches with unacceptable risk</high_risk>
    <resource_constraints>Cut branches that exceed available resources</resource_constraints>
    <redundancy>Merge similar branches</redundancy>
  </pruning_criteria>
  
  <pruning_example>
    <original_branches>8</original_branches>
    <after_feasibility_filter>6</after_feasibility_filter>
    <after_risk_assessment>4</after_risk_assessment>
    <after_resource_check>3</after_resource_check>
    <final_branches>3 high-quality, diverse approaches</final_branches>
  </pruning_example>
</branch_pruning>
```

## Synthesis Strategies

### Best-of-Breed Combination
```xml
<synthesis_pattern>
  <approach>Combine the best elements from multiple branches</approach>
  
  <example>
    <branch_a_contribution>Efficient caching strategy</branch_a_contribution>
    <branch_b_contribution>Robust error handling</branch_b_contribution>
    <branch_c_contribution>Scalable architecture pattern</branch_c_contribution>
    
    <synthesized_solution>
      A scalable architecture (from C) that implements efficient caching (from A) 
      with robust error handling (from B), creating a solution better than any 
      single branch.
    </synthesized_solution>
  </example>
</synthesis_pattern>
```

### Hierarchical Integration
```xml
<hierarchical_integration>
  <strategy>Layer solutions from different branches</strategy>
  
  <layers>
    <foundation>Core architecture from most robust branch</foundation>
    <optimization>Performance improvements from efficiency branch</optimization>
    <features>User experience enhancements from usability branch</features>
    <safety>Security measures from security-focused branch</safety>
  </layers>
</hierarchical_integration>
```

## Integration with Other Components

### With ReAct Reasoning
```xml
<tot_react_integration>
  <thought>I need to explore multiple approaches to this problem</thought>
  <action>Generate Tree of Thoughts with 4 main branches</action>
  <observation>Each branch reveals different aspects of the solution space</observation>
  <thought>Now I'll evaluate and synthesize the most promising elements</thought>
  <action>Apply ToT evaluation criteria and synthesis strategies</action>
  <observation>Combined solution is more comprehensive than any single approach</observation>
</tot_react_integration>
```

### With Optimization Components
```xml
<tot_optimization>
  <branch_optimization>Each branch can be optimized independently</branch_optimization>
  <synthesis_optimization>The final synthesis can be further optimized</synthesis_optimization>
  <meta_optimization>The ToT process itself can be optimized based on results</meta_optimization>
</tot_optimization>
```

## Usage Patterns

### Activation
```xml
<activate_tot>
  <mode>tree_of_thoughts</mode>
  <branches>auto|3|5|7</branches>
  <depth>shallow|medium|deep</depth>
  <synthesis>best_of_breed|hierarchical|weighted_combination</synthesis>
</activate_tot>
```

### Customization
```xml
<tot_customization>
  <exploration_style>
    <breadth_first>Explore many options at each level</breadth_first>
    <depth_first>Dive deep into promising branches</depth_first>
    <balanced>Mix of breadth and depth</balanced>
  </exploration_style>
  
  <evaluation_focus>
    <practical>Emphasize feasibility and implementation</practical>
    <innovative>Prioritize creativity and novel approaches</innovative>
    <conservative>Focus on low-risk, proven strategies</conservative>
  </evaluation_focus>
</tot_customization>
```

## Performance Characteristics

### Strengths
- **Comprehensive exploration** of solution space
- **Systematic evaluation** of alternatives
- **Creative synthesis** of best elements
- **Reduced bias** through multiple perspectives

### Optimization
- **Adaptive branching** based on problem complexity
- **Intelligent pruning** to focus on promising paths
- **Efficient synthesis** to combine insights
- **Context-aware** depth and breadth control

      </exploration_capabilities>
    </reasoning_framework>
  </tree_of_thoughts>

  <o>
Tree of Thoughts reasoning completed with multi-path exploration:

**Thought Branches:** [count] reasoning paths explored and evaluated
**Path Synthesis:** [count] optimal solution elements combined
**Exploration Depth:** [level] systematic reasoning depth achieved
**Solution Quality:** [percentage]% improvement through multi-path analysis
**Branch Evaluation:** [0-100] thought tree construction effectiveness rating
**Systematic Exploration:** Advanced Tree of Thoughts with comprehensive problem-solving
  </o>
</prompt_component> 