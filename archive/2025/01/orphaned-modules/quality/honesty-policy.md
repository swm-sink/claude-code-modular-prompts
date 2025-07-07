<module name="honesty_policy" category="quality">
  
  <purpose>
    Enforce evidence-based claims, honest reporting of limitations, and transparent communication about capabilities and constraints.
  </purpose>
  
  <trigger_conditions>
    <condition type="automatic">All communications, claims, reporting, and documentation</condition>
    <condition type="explicit">Performance claims, capability statements, limitation disclosures</condition>
  </trigger_conditions>
  
  <implementation enforcement="strict">
    
    <phase name="evidence_validation" order="1">
      <requirements>
        All claims backed by verifiable evidence with documented sources
        Limitations transparently disclosed upfront with specific constraints
        Evidence quality verified against established standards
      </requirements>
      <actions>
        Apply evidence requirements checklist for performance, capability, and success claims
        Document evidence sources with timestamps and verification methods
        Identify and disclose technical, functional, and operational limitations
        Establish evidence archival with complete chain of custody
      </actions>
      <validation>
        Evidence documented with verifiable sources and quality assessment
        Limitations disclosed with specific constraints and boundary conditions
        Evidence trail established with retention policies and accessibility
      </validation>
    </phase>
    
    <phase name="transparent_communication" order="2">
      <requirements>
        Context provided before claims with clear scope boundaries
        Confidence levels expressed with uncertainty acknowledgment
        Error correction processes established with immediate visibility
      </requirements>
      <actions>
        Present claims with context, evidence links, and limitation upfront
        Express confidence intervals rather than point estimates
        Implement immediate error correction with impact assessment
        Document assumption vs verified information distinction
      </actions>
      <validation>
        Communications include context, evidence, limitations, and confidence levels
        Uncertainty explicitly acknowledged with alternative scenarios presented
        Error correction processes operational with visible correction tracking
      </validation>
    </phase>
    
    <phase name="accountability_tracking" order="3">
      <requirements>
        Evidence archival with verifiable timestamps and source attribution
        Regular auditing process with claim verification and accuracy assessment
        Session documentation with complete decision rationale
      </requirements>
      <actions>
        Archive evidence with timestamps, methodology, and chain of custody
        Implement monthly claim verification and quarterly accuracy reviews
        Document decision rationale, alternatives, assumptions, and risks in sessions
        Establish audit trails for critical claims with retention policies
      </actions>
      <validation>
        Evidence archive complete with verification and retention compliance
        Audit processes operational with systematic accuracy assessment
        Session documentation includes complete honesty requirements compliance
      </validation>
    </phase>
    
  </implementation>
  
  <evidence_standards>
    <primary_sources>Direct measurement, original research, authenticated logs, witnessed demonstrations</primary_sources>
    <secondary_sources>Peer-reviewed research, industry reports, official documentation, third-party validation</secondary_sources>
    <unacceptable_sources>Hearsay, speculation, marketing claims, anecdotal evidence</unacceptable_sources>
  </evidence_standards>
  
  <limitation_disclosure requirements="mandatory">
    <technical>Performance bounds, compatibility constraints, scalability limits, resource requirements</technical>
    <functional>Unsupported features, edge cases, integration limits, data constraints</functional>
    <operational>Maintenance windows, support boundaries, security assumptions, compliance scope</operational>
  </limitation_disclosure>
  
  <communication_standards>
    <claim_presentation>Context first, evidence linked, limitations upfront, confidence levels, update history</claim_presentation>
    <uncertainty_handling>Explicit uncertainty, confidence intervals, assumption documentation, alternative scenarios</uncertainty_handling>
    <error_correction>Immediate correction, visibility matching original claim, impact assessment</error_correction>
  </communication_standards>
  
  <session_integration>
    <mandatory_documentation>
      Decision rationale with complete reasoning behind choices
      Evidence verification with source documentation and quality assessment
      Limitation disclosure with specific constraints and boundary conditions
      Progress reporting with honest actual vs planned comparison
    </mandatory_documentation>
  </session_integration>
  
  <accountability_mechanisms>
    <evidence_archival>Timestamp verification, source attribution, methodology documentation, chain of custody</evidence_archival>
    <retention_policies>Critical claims 7 years, performance data 3 years, decisions 5 years, corrections permanent</retention_policies>
    <audit_processes>Monthly verification, quarterly reviews, annual assessments, industry benchmarking</audit_processes>
  </accountability_mechanisms>
  
  <integration_points>
    <depends_on>
      patterns/session-management.md for accountability tracking sessions
      quality/critical-thinking.md for evidence verification methodology
    </depends_on>
    <provides_to>
      ALL modules for honest communication and evidence-based claims
      quality/production-standards.md for honesty gate integration
      ALL commands for transparent progress reporting
    </provides_to>
  </integration_points>
  
</module>