---
name: research-report
description: Generate comprehensive research findings and pattern intelligence reports for consultation system integration
usage: "research-report [--scope=all|domain|batch] [--format=detailed|summary|executive] [--export=markdown|json|yaml]"
allowed-tools: [Read, Write, Edit, Bash, Grep, Glob, LS, TodoWrite]
category: research
version: "1.0"
---

# Research Report: Comprehensive Pattern Intelligence Analysis

## Purpose: Transform Research Data into Actionable Consultation Intelligence

The `/research-report` command synthesizes all research database findings into comprehensive, actionable intelligence reports that directly inform the 30-60 minute consultation system. This command transforms raw pattern data into strategic insights that enable evidence-based, project-specific recommendations.

**Reporting Philosophy**: Data without insight is just noise - transform evidence into actionable intelligence for superior consultation outcomes.

## Intelligence vs Information: Why Synthesis Matters

**❌ Failed Information Dump Approach**:
- Raw data export without analysis or synthesis
- Generic pattern lists without context or prioritization
- No cross-pattern relationships or trend identification
- Missing actionable recommendations for consultation
- No domain-specific insights or customization

**✅ Our Intelligence Synthesis Approach**:
- Comprehensive pattern analysis with trend identification
- Domain-specific insights with actionable recommendations
- Cross-pattern relationship mapping and dependency analysis
- Confidence-weighted recommendations with evidence trails
- Consultation-ready insights with specific usage scenarios
- Innovation spotlight and emerging pattern identification

## Report Types and Scope

### 1. Executive Intelligence Report
**Target Audience**: Decision makers, consultation system architects
**Focus**: High-level insights, strategic recommendations, ROI analysis

```
Executive Report Structure:
├── Strategic Intelligence Summary
│   ├── Pattern database quality metrics
│   ├── Consultation readiness assessment
│   ├── Domain coverage and capability gaps
│   └── Innovation and competitive insights
├── Evidence-Based Recommendations
│   ├── Priority patterns for consultation integration
│   ├── Domain expansion opportunities
│   ├── Quality improvement initiatives
│   └── Research investment priorities
└── Success Metrics and ROI Analysis
    ├── Consultation effectiveness predictions
    ├── Pattern confidence distribution
    └── Research database value assessment
```

### 2. Detailed Technical Analysis
**Target Audience**: Consultation system developers, agent builders
**Focus**: Technical implementation, pattern specifications, integration details

```
Technical Report Structure:
├── Pattern Categories Deep Dive
│   ├── Commands: Implementation patterns and variations
│   ├── Agents: Specialization strategies and orchestration
│   ├── Context: Engineering patterns and token optimization
│   └── Workflows: Automation and process patterns
├── Cross-Pattern Relationship Analysis
│   ├── Dependency chains and requirement mapping
│   ├── Complementary pattern clusters
│   ├── Conflict resolution and alternative approaches
│   └── Integration complexity assessment
├── Quality and Validation Analysis
│   ├── CRAAP score distribution and trends
│   ├── Evidence source diversity and authority
│   ├── Technical accuracy and compliance metrics
│   └── Continuous improvement recommendations
└── Implementation Specifications
    ├── Pattern integration requirements
    ├── Technical dependencies and prerequisites
    └── Testing and validation procedures
```

### 3. Domain-Specific Intelligence
**Target Audience**: Domain experts, consultation specialists
**Focus**: Domain expertise, use case scenarios, specialized recommendations

```
Domain Report Structure:
├── Domain Landscape Analysis
│   ├── Pattern coverage and capability assessment
│   ├── Technology stack representation
│   ├── Use case scenario mapping
│   └── Competitive landscape and innovation trends
├── Consultation Scenario Mapping
│   ├── Common project patterns and recommendations
│   ├── Anti-pattern warnings and alternatives
│   ├── Decision trees for pattern selection
│   └── Success stories and case studies
├── Domain-Specific Intelligence
│   ├── Emerging trends and technology adoption
│   ├── Best practices and proven approaches
│   ├── Common pitfalls and failure modes
│   └── Expert insights and community wisdom
└── Actionable Recommendations
    ├── Priority patterns for domain consultation
    ├── Customization strategies for domain needs
    └── Integration roadmap and implementation guide
```

## Comprehensive Analysis Engine

### Pattern Intelligence Analysis
```bash
# Comprehensive pattern analysis pipeline
generate_pattern_intelligence() {
  local scope=$1
  local report_type=$2
  
  echo "Generating pattern intelligence for scope: $scope"
  
  # Load pattern data from research database
  pattern_data=$(load_pattern_database "$scope")
  
  # Analyze pattern distribution and quality metrics
  quality_metrics=$(analyze_pattern_quality "$pattern_data")
  
  # Identify pattern relationships and dependencies
  relationship_analysis=$(analyze_pattern_relationships "$pattern_data")
  
  # Generate confidence-weighted recommendations
  recommendations=$(generate_weighted_recommendations "$pattern_data" "$quality_metrics")
  
  # Identify innovation and emerging patterns
  innovation_analysis=$(identify_innovation_patterns "$pattern_data")
  
  # Create domain-specific insights
  domain_insights=$(generate_domain_insights "$pattern_data" "$scope")
  
  # Synthesize comprehensive intelligence report
  synthesize_intelligence_report "$report_type" "$quality_metrics" "$relationship_analysis" "$recommendations" "$innovation_analysis" "$domain_insights"
}
```

### Cross-Repository Trend Analysis
```bash
# Analyze trends across repository collection
analyze_cross_repository_trends() {
  local repository_list=$1
  
  echo "Analyzing trends across repositories: $repository_list"
  
  # Pattern evolution tracking
  evolution_trends=$(track_pattern_evolution "$repository_list")
  
  # Technology adoption patterns
  adoption_patterns=$(analyze_technology_adoption "$repository_list")
  
  # Community consensus identification
  consensus_patterns=$(identify_community_consensus "$repository_list")
  
  # Innovation diffusion analysis
  diffusion_analysis=$(analyze_innovation_diffusion "$repository_list")
  
  # Generate trend intelligence report
  generate_trend_report "$evolution_trends" "$adoption_patterns" "$consensus_patterns" "$diffusion_analysis"
}
```

### Confidence-Weighted Recommendation Engine
```bash
# Generate recommendations weighted by confidence and evidence
generate_weighted_recommendations() {
  local pattern_data=$1
  local quality_metrics=$2
  
  echo "Generating confidence-weighted recommendations"
  
  # High-confidence patterns (0.8+)
  high_confidence_patterns=$(filter_patterns_by_confidence "$pattern_data" 0.8 1.0)
  high_conf_recommendations=$(generate_recommendations "$high_confidence_patterns" "immediate_use")
  
  # Medium-confidence patterns (0.7-0.8)
  medium_confidence_patterns=$(filter_patterns_by_confidence "$pattern_data" 0.7 0.8)
  medium_conf_recommendations=$(generate_recommendations "$medium_confidence_patterns" "validation_required")
  
  # Emerging patterns (0.6-0.7 but innovative)
  emerging_patterns=$(filter_emerging_patterns "$pattern_data" 0.6 0.7)
  emerging_recommendations=$(generate_recommendations "$emerging_patterns" "experimental_use")
  
  # Synthesize weighted recommendation matrix
  create_recommendation_matrix "$high_conf_recommendations" "$medium_conf_recommendations" "$emerging_recommendations"
}
```

## Report Generation Workflow

### Phase 1: Data Collection and Aggregation (5-10 minutes)
```
Data Intelligence Gathering:
├── Load complete research database
├── Aggregate pattern metadata and validation results
├── Collect cross-reference relationship data
├── Gather repository analysis summaries
├── Load domain and technology mapping data
└── Prepare trend analysis datasets
```

### Phase 2: Pattern Analysis and Synthesis (15-25 minutes)
```
Intelligence Analysis:
├── Calculate pattern quality distributions and trends
├── Identify high-value patterns for consultation
├── Analyze cross-pattern relationships and dependencies
├── Map patterns to consultation scenarios
├── Generate confidence-weighted recommendations
├── Identify innovation and emerging pattern opportunities
└── Create domain-specific insight analysis
```

### Phase 3: Intelligence Report Generation (10-15 minutes)
```
Report Synthesis:
├── Structure findings by report type and audience
├── Generate executive summaries with key insights
├── Create detailed technical documentation
├── Produce domain-specific consultation guides
├── Format for multiple export options
└── Validate report completeness and accuracy
```

### Phase 4: Consultation Integration Preparation (5-10 minutes)
```
Consultation Readiness:
├── Create consultation scenario mapping
├── Generate pattern recommendation decision trees
├── Prepare anti-pattern warnings and alternatives
├── Create implementation guidance and prerequisites
├── Format for agent integration and context engineering
└── Validate consultation scenario completeness
```

## Intelligence Report Templates

### Executive Intelligence Summary Template
```markdown
# Research Intelligence Executive Summary

## Strategic Overview
**Research Database Status**: [Quality Assessment]
- **Total Patterns Analyzed**: [Count] across [Domain Count] domains
- **High-Confidence Patterns**: [Count] ([Percentage]%) ready for consultation
- **Domain Coverage**: [Assessment] with [Gap Analysis]
- **Innovation Index**: [Score] based on emerging pattern analysis

## Consultation Readiness Assessment
**Overall Readiness**: [Grade] ([Percentage]%)
- **Web Development**: [Grade] - [Pattern Count] validated patterns
- **Data Science**: [Grade] - [Pattern Count] validated patterns  
- **DevOps**: [Grade] - [Pattern Count] validated patterns
- **Enterprise**: [Grade] - [Pattern Count] validated patterns

## Key Strategic Insights
### High-Impact Patterns Identified
1. **[Pattern Name]** - [Confidence Score] - [Impact Assessment]
2. **[Pattern Name]** - [Confidence Score] - [Impact Assessment]
3. **[Pattern Name]** - [Confidence Score] - [Impact Assessment]

### Innovation Opportunities
- **[Innovation Area]**: [Description] - [Adoption Potential]
- **[Innovation Area]**: [Description] - [Adoption Potential]

### Risk Assessment
- **Coverage Gaps**: [Domain Areas] requiring additional research
- **Quality Concerns**: [Pattern Count] patterns requiring improvement
- **Dependencies**: [Critical Dependencies] for consultation effectiveness

## Strategic Recommendations
### Immediate Actions (0-30 days)
1. **Integrate High-Confidence Patterns**: [Pattern Count] patterns ready for consultation
2. **Address Quality Gaps**: Focus on [Specific Areas] requiring improvement
3. **Expand Domain Coverage**: Prioritize [Domain Areas] for additional research

### Medium-Term Initiatives (30-90 days)
1. **Innovation Integration**: Evaluate [Emerging Patterns] for adoption
2. **Quality Enhancement**: Implement [Improvement Strategies] for medium-confidence patterns
3. **Community Engagement**: Leverage [Community Resources] for pattern validation

### Long-Term Strategy (90+ days)
1. **Ecosystem Leadership**: Position as [Strategic Advantage] in consultation market
2. **Research Expansion**: Scale to [Target Pattern Count] across [Domain Count] domains
3. **Intelligence Platform**: Develop [Advanced Capabilities] for ongoing analysis

## ROI Analysis
**Research Investment**: [Total Time/Resources]
**Expected Consultation Impact**: [Quantified Benefits]
**Pattern Database Value**: [Strategic Value Assessment]
**Competitive Advantage**: [Market Position Analysis]
```

### Technical Implementation Report Template
```markdown
# Technical Pattern Analysis Report

## Pattern Database Analysis

### Commands Category Analysis
**Total Command Patterns**: [Count]
**Quality Distribution**:
- High Confidence (0.8+): [Count] ([Percentage]%)
- Medium Confidence (0.7-0.8): [Count] ([Percentage]%)
- Improvement Needed (<0.7): [Count] ([Percentage]%)

**Implementation Patterns Identified**:
1. **Generation Commands**: [Count] patterns
   - Component generators: [Count] ([Average Confidence])
   - File scaffolders: [Count] ([Average Confidence])
   - Configuration creators: [Count] ([Average Confidence])
   
2. **Analysis Commands**: [Count] patterns
   - Code reviewers: [Count] ([Average Confidence])
   - Metrics analyzers: [Count] ([Average Confidence])
   - Quality assessors: [Count] ([Average Confidence])

### Agents Category Analysis  
**Total Agent Patterns**: [Count]
**Specialization Strategies**:
1. **Domain Experts**: [Count] patterns
   - Technology specialists: [Count]
   - Business domain experts: [Count]
   - Architecture advisors: [Count]
   
2. **Orchestration Agents**: [Count] patterns
   - Task coordinators: [Count]
   - Workflow managers: [Count]
   - Quality supervisors: [Count]

### Cross-Pattern Relationship Analysis
**Total Relationships Mapped**: [Count]
**Relationship Types**:
- Extends: [Count] ([Average Strength])
- Complements: [Count] ([Average Strength])
- Requires: [Count] ([Average Strength])
- Conflicts: [Count] ([Resolution Status])

**Critical Dependency Chains**:
1. **[Chain Name]**: [Pattern A] → [Pattern B] → [Pattern C]
   - Strength: [Assessment]
   - Consultation Impact: [Description]
   
### Integration Requirements
**Technical Prerequisites**:
- Claude Code version: [Requirements]
- Tool dependencies: [List]
- Configuration requirements: [Specifications]

**Implementation Complexity**:
- Simple Integration: [Pattern Count] patterns
- Moderate Integration: [Pattern Count] patterns  
- Complex Integration: [Pattern Count] patterns

## Quality Assurance Analysis

### CRAAP Validation Results
**Overall Validation Success Rate**: [Percentage]%
**Score Distribution**:
- Currency (avg: [Score]): [Distribution Analysis]
- Relevance (avg: [Score]): [Distribution Analysis]
- Authority (avg: [Score]): [Distribution Analysis]
- Accuracy (avg: [Score]): [Distribution Analysis]
- Purpose (avg: [Score]): [Distribution Analysis]

### Evidence Source Analysis
**Source Diversity**: [Assessment]
- Repository types: [Distribution]
- Authority levels: [Distribution]
- Geographic/community distribution: [Analysis]

**Evidence Quality Metrics**:
- Average sources per pattern: [Count]
- Working example coverage: [Percentage]%
- Technical validation rate: [Percentage]%
```

## Domain-Specific Intelligence Reports

### Web Development Domain Intelligence
```yaml
web_development_intelligence:
  landscape_analysis:
    framework_coverage:
      react: 
        patterns: 23
        confidence: 0.82
        innovation_index: 0.78
        key_insights: ["Component generation highly mature", "Testing integration excellent"]
      vue:
        patterns: 12
        confidence: 0.75
        innovation_index: 0.65
        key_insights: ["Composition API patterns emerging", "State management evolving"]
      angular:
        patterns: 8
        confidence: 0.70
        innovation_index: 0.55
        key_insights: ["Enterprise patterns strong", "Modern Angular adoption growing"]
        
  consultation_scenarios:
    new_project_setup:
      priority_patterns:
        - component-architecture-generator (0.89 confidence)
        - testing-framework-integration (0.85 confidence)
        - state-management-setup (0.78 confidence)
      success_probability: 0.87
      time_savings: "40-60% faster setup"
      
    legacy_migration:
      priority_patterns:
        - migration-assessment-tool (0.81 confidence)
        - incremental-modernization (0.74 confidence)
        - compatibility-checker (0.72 confidence)
      success_probability: 0.73
      complexity_factors: ["Legacy code quality", "Team expertise", "Timeline constraints"]
      
  innovation_spotlight:
    ai_assisted_development:
      patterns: 5
      adoption_stage: "early"
      potential_impact: "high"
      evidence_strength: "medium"
      consultation_readiness: "experimental"
      
  recommendations:
    immediate_integration:
      - "React component generation patterns (23 patterns, 0.82 avg confidence)"
      - "TypeScript integration workflows (18 patterns, 0.79 avg confidence)"
      - "Testing automation strategies (15 patterns, 0.83 avg confidence)"
      
    quality_improvement:
      - "Vue 3 Composition API patterns need additional validation"
      - "Angular modern patterns require more enterprise evidence"
      - "Next.js app router patterns need performance validation"
```

## Usage Examples and Scenarios

### Generate Comprehensive Intelligence Report
```bash
# Full intelligence analysis across all domains
/research-report --scope=all --format=detailed --export=markdown

# Executive summary for stakeholders
/research-report --scope=all --format=executive --export=markdown

# Technical implementation guide
/research-report --scope=all --format=detailed --export=json
```

### Domain-Specific Intelligence
```bash
# Web development consultation preparation
/research-report --scope=web-development --format=detailed

# Data science domain analysis
/research-report --scope=data-science --format=summary --export=yaml

# Enterprise patterns intelligence
/research-report --scope=enterprise --format=executive
```

### Batch and Project-Specific Reports
```bash
# Analysis of specific research batch
/research-report --scope=priority-web-dev --format=detailed

# Innovation and emerging patterns focus
/research-report --scope=innovation-research --format=summary

# Quality improvement analysis
/research-report --scope=improvement-needed --format=detailed
```

### Export Format Examples
```bash
# Markdown for documentation
/research-report --format=executive --export=markdown

# JSON for programmatic consumption
/research-report --format=detailed --export=json

# YAML for configuration and agent integration
/research-report --format=summary --export=yaml
```

## Advanced Analytics and Insights

### Pattern Network Analysis
```python
# Network analysis of pattern relationships
def analyze_pattern_network(patterns, relationships):
    """
    Analyze pattern relationships as network graph
    Identify central patterns, clusters, and isolated nodes
    """
    import networkx as nx
    
    # Create network graph
    G = nx.Graph()
    
    # Add pattern nodes with attributes
    for pattern in patterns:
        G.add_node(pattern['id'], 
                  confidence=pattern['confidence'],
                  category=pattern['category'],
                  domain=pattern['domain'])
    
    # Add relationship edges
    for rel in relationships:
        G.add_edge(rel['pattern_1'], rel['pattern_2'], 
                  type=rel['type'], strength=rel['strength'])
    
    # Calculate network metrics
    centrality = nx.centrality.betweenness_centrality(G)
    clusters = nx.community.greedy_modularity_communities(G)
    
    return {
        'centrality_analysis': centrality,
        'pattern_clusters': clusters,
        'network_density': nx.density(G),
        'key_connectors': sorted(centrality.items(), key=lambda x: x[1], reverse=True)[:10]
    }
```

### Trend Prediction and Evolution Analysis
```python
# Analyze pattern evolution and predict trends
def analyze_pattern_evolution(historical_data):
    """
    Track pattern evolution over time
    Predict emerging trends and technology adoption
    """
    evolution_trends = []
    
    for pattern_category in ['commands', 'agents', 'context', 'workflows']:
        category_data = filter_by_category(historical_data, pattern_category)
        
        # Analyze confidence score trends
        confidence_trend = calculate_trend(category_data, 'confidence')
        
        # Analyze adoption rate trends
        adoption_trend = calculate_adoption_trend(category_data)
        
        # Predict future evolution
        prediction = predict_evolution(confidence_trend, adoption_trend)
        
        evolution_trends.append({
            'category': pattern_category,
            'confidence_trend': confidence_trend,
            'adoption_trend': adoption_trend,
            'prediction': prediction,
            'emerging_patterns': identify_emerging(category_data)
        })
    
    return evolution_trends
```

### Consultation Impact Modeling
```python
# Model expected consultation impact from pattern integration
def model_consultation_impact(patterns, consultation_scenarios):
    """
    Predict consultation effectiveness based on pattern integration
    Calculate expected time savings and success rates
    """
    impact_model = {}
    
    for scenario in consultation_scenarios:
        # Map patterns to scenario requirements
        relevant_patterns = map_patterns_to_scenario(patterns, scenario)
        
        # Calculate weighted effectiveness
        effectiveness = 0
        total_weight = 0
        
        for pattern in relevant_patterns:
            weight = pattern['relevance_to_scenario']
            effectiveness += pattern['confidence'] * weight
            total_weight += weight
        
        if total_weight > 0:
            scenario_effectiveness = effectiveness / total_weight
        else:
            scenario_effectiveness = 0
        
        # Estimate time savings and success probability
        time_savings = calculate_time_savings(relevant_patterns, scenario)
        success_probability = calculate_success_probability(scenario_effectiveness)
        
        impact_model[scenario['name']] = {
            'effectiveness': scenario_effectiveness,
            'time_savings': time_savings,
            'success_probability': success_probability,
            'pattern_count': len(relevant_patterns),
            'confidence_distribution': get_confidence_distribution(relevant_patterns)
        }
    
    return impact_model
```

## Integration with Consultation System

### Agent-Ready Intelligence Packages
```yaml
# Intelligence package for consultation agents
agent_intelligence_package:
  high_confidence_patterns:
    web_development:
      component_generation:
        - pattern: "react-component-generator"
          confidence: 0.89
          usage_scenarios: ["new_project", "feature_development"]
          prerequisites: ["typescript", "testing_framework"]
          
  domain_expertise:
    web_development:
      common_patterns:
        - "Component-based architecture dominant (87% adoption)"
        - "TypeScript adoption accelerating (78% of new projects)"
        - "Testing automation critical success factor (95% correlation)"
      
      anti_patterns:
        - "Avoid premature micro-frontend adoption (62% failure rate)"
        - "Don't skip accessibility integration (compliance risk)"
        - "Prevent state management over-engineering (performance impact)"
      
      decision_trees:
        component_architecture:
          - condition: "team_size < 5 AND complexity = simple"
            recommendation: "simple-component-patterns"
            confidence: 0.84
          - condition: "team_size >= 5 OR complexity = complex"
            recommendation: "enterprise-component-patterns"
            confidence: 0.78
```

### Context Engineering Intelligence
```yaml
# Context engineering recommendations from research
context_intelligence:
  hierarchical_patterns:
    optimal_structure:
      - "Master CLAUDE.md with cross-references (confidence: 0.86)"
      - "Domain-specific context files (confidence: 0.81)"
      - "Technical architecture documentation (confidence: 0.79)"
      - "Decision logs and rationale (confidence: 0.74)"
    
    token_optimization:
      - "Navigation-first structure reduces token waste by 23%"
      - "Hierarchical referencing improves comprehension by 31%"
      - "Cross-file context increases retention by 18%"
    
  navigation_strategies:
    most_effective:
      - pattern: "hub-and-spoke-navigation"
        effectiveness: 0.83
        evidence_sources: 7
        token_efficiency: "+24%"
```

## Quality Metrics and Success Indicators

### Report Quality Assessment
- **Comprehensiveness**: Coverage of all pattern categories and domains
- **Accuracy**: Alignment between predictions and consultation outcomes
- **Actionability**: Clear, implementable recommendations with success criteria
- **Timeliness**: Intelligence reflects current ecosystem state and trends
- **Relevance**: Direct applicability to consultation system enhancement

### Intelligence Value Metrics
- **Consultation Improvement**: Measurable enhancement in consultation outcomes
- **Decision Support**: Faster, more accurate pattern selection and recommendations
- **Risk Mitigation**: Early identification of problematic patterns and approaches
- **Innovation Adoption**: Successful integration of emerging patterns and techniques
- **Competitive Advantage**: Unique insights driving superior consultation experiences

## Output Deliverables

### Research Intelligence Dashboard
- Interactive pattern database exploration
- Real-time confidence score tracking
- Domain coverage visualization
- Relationship network mapping
- Trend analysis and predictions

### Consultation Integration Packages
- Agent-ready pattern intelligence
- Context engineering recommendations
- Decision support frameworks
- Anti-pattern warning systems
- Success probability models

### Strategic Planning Documents
- Executive intelligence summaries
- Research investment recommendations
- Domain expansion strategies
- Quality improvement roadmaps
- Competitive landscape analysis

---

**Remember**: Intelligence without action is academic exercise. These reports exist to transform research data into consultation superiority - every insight must contribute to delivering better, faster, more valuable consultation experiences.