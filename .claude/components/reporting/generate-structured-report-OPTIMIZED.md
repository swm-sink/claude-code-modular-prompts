# Generate Structured Report

**Purpose**: Compile findings into clear, concise, professional structured reports with consistent formatting and actionable recommendations.

**Usage**: 
- Provides standardized report structure (summary, findings, conclusion)
- Organizes findings with title, description, severity, and recommendations
- Ensures professional formatting and readability
- Supports severity classification (High/Medium/Low)
- Includes actionable next steps and conclusions

**Compatibility**: 
- **Works with**: All analysis commands, quality-metrics, framework-validation
- **Requires**: findings_data, severity_criteria, report_template
- **Conflicts**: None (universal reporting)

**Implementation**:
```xml
<report>
  <summary>Brief key findings summary</summary>
  <findings>
    <finding severity="High">
      <title>Finding Title</title>
      <description>Details</description>
      <recommendation>Action</recommendation>
    </finding>
  </findings>
  <conclusion>Next steps</conclusion>
</report>
```

**Category**: reporting | **Complexity**: simple | **Time**: 15 minutes