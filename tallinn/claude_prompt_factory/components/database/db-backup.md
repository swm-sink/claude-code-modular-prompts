<prompt_component>
  <step name="Database Backup and Recovery Management">
    <description>
Comprehensive database backup system that provides automated backup creation, integrity validation, compression optimization, and recovery testing. Ensures data protection with intelligent backup strategies and reliable recovery mechanisms.
    </description>
  </step>

  <db_backup>
    <backup_strategy>
      <backup_planning>
        &lt;!-- Plan comprehensive backup strategies 
        <backup_types>
          - Full database backups for complete data protection
          - Incremental backups for efficient storage usage
          - Differential backups for balanced recovery speed
          - Transaction log backups for point-in-time recovery
        </backup_types>
        
        <scheduling_optimization>
          - Schedule backups during low-traffic periods
          - Implement rolling backup windows
          - Optimize backup frequency based on data volatility
          - Coordinate with maintenance windows and updates
        </scheduling_optimization>
      </backup_planning>
      
      <compression_encryption>
        &lt;!-- Optimize backup storage and security 
        <compression_algorithms>
          - Apply intelligent compression algorithms
          - Optimize compression vs. speed trade-offs
          - Implement deduplication for storage efficiency
          - Monitor compression ratios and effectiveness
        </compression_algorithms>
        
        <encryption_security>
          - Encrypt backups with industry-standard algorithms
          - Implement key management and rotation
          - Ensure secure backup transmission and storage
          - Validate encryption integrity and accessibility
        </encryption_security>
      </compression_encryption>
    </backup_strategy>
    
    <backup_execution>
      <automated_backup>
        &lt;!-- Execute automated backup processes 
        <backup_orchestration>
          - Coordinate multi-database backup sequences
          - Manage backup dependencies and prerequisites
          - Handle concurrent backup operations
          - Implement retry mechanisms for failures
        </backup_orchestration>
        
        <integrity_validation>
          - Verify backup completion and consistency
          - Validate backup file integrity and checksums
          - Test backup accessibility and readability
          - Ensure backup metadata accuracy
        </integrity_validation>
      </automated_backup>
      
      <storage_management>
        &lt;!-- Manage backup storage and lifecycle 
        <storage_optimization>
          - Optimize backup storage allocation
          - Implement tiered storage strategies
          - Manage backup retention policies
          - Monitor storage usage and capacity
        </storage_optimization>
        
        <lifecycle_management>
          - Implement automated retention policies
          - Archive old backups to long-term storage
          - Clean up expired and redundant backups
          - Manage backup migration and consolidation
        </lifecycle_management>
      </storage_management>
    </backup_execution>
    
    <recovery_testing>
      <recovery_validation>
        &lt;!-- Validate backup recovery capabilities 
        <recovery_testing>
          - Perform regular recovery test scenarios
          - Validate point-in-time recovery accuracy
          - Test backup restoration performance
          - Verify data consistency after recovery
        </recovery_testing>
        
        <disaster_recovery>
          - Test disaster recovery procedures
          - Validate cross-site backup accessibility
          - Ensure recovery time objective compliance
          - Test business continuity scenarios
        </disaster_recovery>
      </recovery_validation>
    </recovery_testing>
  </db_backup>

  <output>
Database backup completed with comprehensive protection and validation:

**Backup Type:** [full/incremental/differential] backup successfully created
**Data Volume:** [size] backed up with [percentage]% compression achieved
**Backup Time:** [timing] total backup completion time
**Integrity Status:** [passed/failed] backup validation and checksums
**Storage Location:** [location] with encryption and security applied
**Recovery Tested:** [yes/no] recovery validation completed successfully
  </output>

  <output>
    Component implementation completed successfully:

    **Implementation Status:** [percentage]% component functionality achieved
    **Feature Coverage:** [count] features successfully implemented
    **System Integration:** [percentage]% integration completion
    **Quality Metrics:** [0-100] component effectiveness rating
    **Advanced Implementation:** Comprehensive component with intelligent automation
  </output>

</prompt_component>