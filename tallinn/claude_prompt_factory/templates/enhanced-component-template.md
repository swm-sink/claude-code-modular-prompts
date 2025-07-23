<prompt_component>
  <step name="[COMPONENT_NAME]">
    <description>
      [COMPREHENSIVE_DESCRIPTION] - Clear, detailed explanation of purpose, integration points, and expected outcomes. Must be 2-4 sentences providing complete context.
    </description>
    
    <metadata>
      <template_version>2.0</template_version>
      <component_type>[TYPE]</component_type>
      <complexity_level>[low|medium|high]</complexity_level>
      <dependencies>[COMPONENT_COUNT]</dependencies>
    </metadata>
    
    <[PROCESS_SECTION_NAME]>
      1. **[Phase 1 Name]**:
         - [Specific action with clear deliverable]
         - [Validation criteria for this phase]
         - [Integration point or handoff]

      2. **[Phase 2 Name]**:
         - [Specific action with clear deliverable]
         - [Validation criteria for this phase]
         - [Integration point or handoff]

      3. **[Phase 3 Name]**:
         - [Specific action with clear deliverable]
         - [Validation criteria for this phase]
         - [Integration point or handoff]

      4. **[Phase 4 Name]**:
         - [Specific action with clear deliverable]
         - [Validation criteria for this phase]
         - [Final validation step]
    </[PROCESS_SECTION_NAME]>
    
    <configuration>
      [CONFIGURATION_DETAILS] - Specific settings, parameters, or environmental requirements:
      - **[Setting 1]**: [Description and default value]
      - **[Setting 2]**: [Description and constraints]
      - **[Setting 3]**: [Description and validation rules]
    </configuration>
    
    <integration_points>
      - **Input Requirements**: [What this component expects]
      - **Output Guarantees**: [What this component provides]
      - **Side Effects**: [Any system changes or state modifications]
      - **Error Conditions**: [When this component might fail]
    </integration_points>
    
    <output>
      [STANDARDIZED_OUTPUT_FORMAT] - Clear, structured specification:
      
      **[Primary Output Category]**:
      - Format: [Specific format pattern/template]
      - Content: [What information is included]
      - Validation: [How to verify output quality]
      
      **[Secondary Output Category]**:
      - Format: [Specific format pattern/template] 
      - Content: [What information is included]
      - Status Indicators: [Success/warning/error patterns]
      
      **[Metadata Output]**:
      - Performance Metrics: [Timing, resource usage]
      - Quality Scores: [Accuracy, completeness measures]
      - Integration Status: [Handoff confirmation]
      
      **Behavioral Guidelines**:
      - Always provide structured output matching the specified format
      - Include validation metadata for downstream processing
      - Maintain consistent error handling and reporting patterns
      - When [specific_condition], execute [specific_action]
    </output>

    <validation>
      <xml_well_formed>true</xml_well_formed>
      <required_sections>
        <section>description</section>
        <section>output</section>
      </required_sections>
      <output_format_compliance>strict</output_format_compliance>
    </validation>
  </step>
</prompt_component>