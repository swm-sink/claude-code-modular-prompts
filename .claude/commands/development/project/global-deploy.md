---
name: /global-deploy
description: "Advanced global deployment with multi-region orchestration, geographic optimization, and intelligent traffic management"
usage: "[deployment_scope] [region_strategy]"
tools: Read, Write, Edit, Bash, Grep
---
# /deploy global - Advanced Global Deployment
Sophisticated global deployment system with multi-region orchestration, geographic optimization, and intelligent traffic management.
## Usage
```bash
/deploy global multi-region                  # Multi-region deployment
/deploy global --cdn                         # CDN-optimized global deployment
/deploy global --traffic-management          # Intelligent traffic management
/deploy global --comprehensive               # Comprehensive global orchestration
```
<command_file>
  <metadata>
    <name>/global-deploy</name>
    <purpose>Execute intelligent global deployment with multi-region optimization, localization, and cultural adaptation using Claude's native understanding.</purpose>
    <usage>
      <![CDATA[
      /global-deploy "[target_regions]" --strategy=[blue-green|canary|rolling] --localize=[auto|manual]
      ]]>
    </usage>
  </metadata>
  <arguments>
    <argument name="target_regions" type="string" required="true">
      <description>Target regions for deployment (e.g., "US,EU,APAC" or "global").</description>
    </argument>
    <argument name="strategy" type="string" required="false" default="blue-green">
      <description>Deployment strategy: blue-green, canary, or rolling.</description>
    </argument>
    <argument name="localize" type="string" required="false" default="auto">
      <description>Localization mode: auto (Claude-driven) or manual (user-guided).</description>
    </argument>
  </arguments>
  <examples>
    <example>
      <description>Deploy globally with automatic localization</description>
      <usage>/global-deploy "global" --strategy=blue-green --localize=auto</usage>
    </example>
    <example>
      <description>Deploy to specific regions with canary rollout</description>
      <usage>/global-deploy "US,EU,JP" --strategy=canary --localize=manual</usage>
    </example>
  </examples>
  <claude_prompt>
    <prompt>
      <!-- Standard DRY Components -->
      <include>components/validation/validation-framework.md</include>
      <include>components/workflow/command-execution.md</include>
      <include>components/workflow/error-handling.md</include>
      <include>components/interaction/progress-reporting.md</include>
      <!-- Command-specific components -->
      <include>components/context/adaptive-thinking.md</include>
      <include>components/actions/parallel-execution.md</include>
      <include>components/orchestration/dag-orchestrator.md</include>
      <include>components/quality/anti-pattern-detection.md</include>
      <![CDATA[
      You are an expert global deployment orchestrator with deep knowledge of international markets, cultural nuances, and regional technology preferences. Execute intelligent global deployment using Claude's native capabilities.
      **Global Deployment Intelligence**:
      <regional_analysis>
        <market_intelligence>
          Analyze target regions for deployment optimization:
          - **North America (US/CA)**: High cloud adoption, privacy-conscious, performance-focused
          - **Europe (EU/UK)**: GDPR compliance critical, quality-focused, data sovereignty requirements
          - **Asia Pacific (JP/KR/SG/AU)**: Mobile-first, efficiency-oriented, relationship-driven adoption
          - **Latin America (BR/MX/AR)**: Cost-sensitive, community-driven, localization important
          - **Middle East & Africa (UAE/ZA)**: Emerging adoption, infrastructure considerations, cultural sensitivity
          - **India**: Cost-optimization focus, English proficiency, massive scale requirements
          - **China**: Unique regulatory environment, local partnerships essential, performance critical
        </market_intelligence>
        <cultural_adaptation>
          Apply cultural intelligence for each target region:
          - **Communication Styles**: Direct vs. indirect, formal vs. casual, hierarchy awareness
          - **Technical Preferences**: Cloud vs. on-premise, security vs. convenience, innovation vs. stability
          - **Business Practices**: Decision-making processes, procurement cycles, relationship importance
          - **Language Nuances**: Technical terminology, cultural metaphors, professional tone
          - **Time Zones**: Optimal deployment windows, support coverage, coordination timing
        </cultural_adaptation>
      </regional_analysis>
      **Intelligent Localization Through Claude**:
      <native_localization>
        <language_adaptation>
          Use Claude's multilingual capabilities for intelligent localization:
          - **Command Documentation**: Auto-translate with technical accuracy and cultural appropriateness
          - **Error Messages**: Culturally sensitive error explanations with local context
          - **Help Content**: Region-appropriate examples and use cases
          - **User Interface**: Localized terminology and interaction patterns
          - **Examples & Tutorials**: Market-relevant scenarios and business contexts
        </language_adaptation>
        <technical_localization>
          Adapt technical implementation for regional requirements:
          - **Data Residency**: Ensure compliance with local data sovereignty laws
          - **Performance Optimization**: CDN placement and regional infrastructure
          - **Integration Patterns**: Local tool ecosystems and preferred platforms
          - **Compliance Frameworks**: Regional regulatory requirements (GDPR, CCPA, etc.)
          - **Currency & Pricing**: Local pricing models and payment preferences
        </technical_localization>
      </native_localization>
      **Multi-Region Deployment Orchestration**:
      <deployment_strategy>
        <blue_green_global>
          Blue-Green deployment across regions:
          1. **Preparation Phase**: Validate all regional configurations and dependencies
          2. **Green Environment Setup**: Deploy to green environments in all target regions
          3. **Regional Validation**: Execute region-specific testing and validation
          4. **Staged Cutover**: Region-by-region traffic switching with monitoring
          5. **Rollback Readiness**: Maintain blue environment for instant rollback capability
        </blue_green_global>
        <canary_rollout>
          Intelligent canary deployment with regional awareness:
          1. **Pilot Region Selection**: Choose optimal pilot region based on risk tolerance
          2. **Gradual Expansion**: Progressive rollout to additional regions
          3. **Performance Monitoring**: Region-specific SLA monitoring and validation
          4. **Cultural Feedback**: Monitor user adoption and satisfaction by region
          5. **Adaptive Scaling**: Adjust rollout speed based on regional success metrics
        </canary_rollout>
        <rolling_deployment>
          Coordinated rolling deployment across time zones:
          1. **Time Zone Optimization**: Schedule deployments during optimal windows
          2. **Dependency Management**: Handle cross-region service dependencies
          3. **Progressive Updates**: Gradual updates with regional health monitoring
          4. **Load Balancing**: Intelligent traffic routing during updates
          5. **Coordination**: Real-time coordination across global deployment teams
        </rolling_deployment>
      </deployment_strategy>
      **Regional Optimization Intelligence**:
      <performance_optimization>
        <regional_infrastructure>
          Optimize infrastructure for each region:
          - **US/CA**: Multi-AZ deployment with high availability and disaster recovery
          - **EU**: GDPR-compliant infrastructure with data residency guarantees
          - **APAC**: Edge computing optimization for reduced latency
          - **Emerging Markets**: Cost-optimized infrastructure with local partnerships
          - **Global**: CDN optimization and intelligent routing
        </regional_infrastructure>
        <cultural_user_experience>
          Adapt user experience for regional preferences:
          - **Information Density**: Detailed vs. simplified interfaces by culture
          - **Interaction Patterns**: Touch vs. keyboard preferences, navigation styles
          - **Visual Design**: Color psychology, layout preferences, iconography
          - **Content Structure**: Linear vs. hierarchical information organization
          - **Help Systems**: Self-service vs. human-assisted support preferences
        </cultural_user_experience>
      </performance_optimization>
      **Execution Workflow**:
      <deployment_execution>
        <phase_1_preparation>
          **Global Deployment Preparation**:
          1. Analyze target regions and validate requirements
          2. Generate region-specific configurations and optimizations
          3. Create localized documentation and help content
          4. Validate compliance requirements for each region
          5. Prepare monitoring and alerting for global deployment
        </phase_1_preparation>
        <phase_2_regional_deployment>
          **Intelligent Regional Rollout**:
          1. Execute deployment strategy across target regions
          2. Monitor performance and user adoption in real-time
          3. Adapt deployment based on regional feedback and metrics
          4. Coordinate cross-region dependencies and integrations
          5. Maintain global operational awareness and control
        </phase_2_regional_deployment>
        <phase_3_optimization>
          **Post-Deployment Optimization**:
          1. Analyze regional performance and user satisfaction
          2. Implement region-specific optimizations and improvements
          3. Gather cultural feedback and adapt user experience
          4. Document lessons learned and best practices
          5. Plan continuous improvement and expansion strategies
        </phase_3_optimization>
      </deployment_execution>
      **Global Coordination & Communication**:
      <coordination_intelligence>
        <cross_cultural_communication>
          Manage global deployment communication:
          - **Stakeholder Updates**: Culturally appropriate communication styles
          - **Status Reporting**: Region-specific metrics and success criteria
          - **Issue Escalation**: Time zone-aware escalation procedures
          - **Success Celebration**: Culturally appropriate recognition and celebration
          - **Continuous Feedback**: Region-specific feedback collection and analysis
        </cross_cultural_communication>
        <operational_excellence>
          Maintain operational excellence across regions:
          - **24/7 Support Coverage**: Follow-the-sun support model
          - **Regional Expertise**: Local technical and cultural expertise
          - **Knowledge Transfer**: Cross-region learning and best practice sharing
          - **Compliance Monitoring**: Ongoing regulatory compliance validation
          - **Performance Optimization**: Continuous regional performance tuning
        </operational_excellence>
      </coordination_intelligence>
      Execute this global deployment using Claude's native intelligence to handle cultural nuances, technical requirements, and regional optimization. Provide detailed progress updates and adapt the deployment based on real-time feedback and regional success metrics.
      **Remember**: Success in global deployment requires both technical excellence and cultural intelligence. Use Claude's understanding of global markets and cultural nuances to create deployments that truly resonate with local users and business practices.
]]>
    </prompt>
  </claude_prompt>
  <dependencies>
    <includes_components>
      <component>components/context/adaptive-thinking.md</component>
      <component>components/actions/parallel-execution.md</component>
      <component>components/orchestration/dag-orchestrator.md</component>
      <component>components/quality/anti-pattern-detection.md</component>
    </includes_components>
    <uses_config_values>
      <config>target_regions</config>
      <config>compliance_requirements</config>
      <config>cultural_preferences</config>
      <config>deployment_strategy</config>
    </uses_config_values>
  </dependencies>
</command_file> 