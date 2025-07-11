# Mobile Development Domain Template

| version | last_updated | status |
|---------|--------------|--------|
| 1.0.0   | 2025-07-11   | stable |

## Domain Overview

Mobile Development domain template provides specialized framework configuration for iOS, Android, and cross-platform mobile application development. This template optimizes the Claude Code Framework for mobile-specific workflows, quality gates, and development patterns.

## Domain Configuration

```xml
<mobile_development_domain>
  <purpose>Specialized framework configuration for mobile application development</purpose>
  
  <target_platforms>
    <ios>Swift, Objective-C, Xcode, iOS SDK, SwiftUI, UIKit</ios>
    <android>Kotlin, Java, Android Studio, Android SDK, Jetpack Compose</android>
    <cross_platform>React Native, Flutter, Xamarin, Ionic</cross_platform>
  </target_platforms>
  
  <development_characteristics>
    <platform_specific>Native development for optimal performance</platform_specific>
    <cross_platform>Shared codebase for multiple platforms</cross_platform>
    <ui_focused>User interface and experience optimization</ui_focused>
    <device_constraints>Memory, battery, and network optimization</device_constraints>
    <app_store_deployment>Apple App Store and Google Play Store</app_store_deployment>
  </development_characteristics>
</mobile_development_domain>
```

## Template Variables

```xml
<template_variables>
  <platform_selection>
    <ios_enabled>{{IOS_ENABLED:boolean}}</ios_enabled>
    <android_enabled>{{ANDROID_ENABLED:boolean}}</android_enabled>
    <cross_platform_framework>{{CROSS_PLATFORM_FRAMEWORK:react_native|flutter|xamarin|ionic}}</cross_platform_framework>
  </platform_selection>
  
  <project_configuration>
    <project_name>{{PROJECT_NAME:string}}</project_name>
    <bundle_identifier>{{BUNDLE_IDENTIFIER:string}}</bundle_identifier>
    <target_os_versions>{{TARGET_OS_VERSIONS:object}}</target_os_versions>
    <app_store_ready>{{APP_STORE_READY:boolean}}</app_store_ready>
  </project_configuration>
  
  <development_settings>
    <ui_framework>{{UI_FRAMEWORK:swiftui|uikit|compose|react_native|flutter}}</ui_framework>
    <state_management>{{STATE_MANAGEMENT:redux|mobx|provider|bloc}}</state_management>
    <testing_framework>{{TESTING_FRAMEWORK:xctest|espresso|jest|flutter_test}}</testing_framework>
    <ci_cd_platform>{{CI_CD_PLATFORM:xcode_cloud|github_actions|bitrise|codemagic}}</ci_cd_platform>
  </development_settings>
</template_variables>
```

## Command Customizations

```xml
<command_customizations>
  <task_command>
    <mobile_specific_thinking>
      <platform_considerations>Consider platform-specific requirements and constraints</platform_considerations>
      <ui_ux_validation>Validate user interface and experience implications</ui_ux_validation>
      <device_compatibility>Ensure compatibility across target device range</device_compatibility>
      <performance_impact>Assess impact on app performance and resource usage</performance_impact>
    </mobile_specific_thinking>
    
    <quality_gates>
      <ui_testing>Automated UI testing for critical user flows</ui_testing>
      <performance_testing>Performance benchmarks for target devices</performance_testing>
      <accessibility_testing>Accessibility compliance validation</accessibility_testing>
      <device_testing>Testing on range of physical devices</device_testing>
    </quality_gates>
  </task_command>
  
  <feature_command>
    <mobile_feature_planning>
      <platform_parity>Ensure feature parity across target platforms</platform_parity>
      <native_integration>Leverage native platform capabilities</native_integration>
      <offline_capability>Design for offline functionality</offline_capability>
      <app_store_compliance>Ensure compliance with app store guidelines</app_store_compliance>
    </mobile_feature_planning>
    
    <development_workflow>
      <prototype_first>Create interactive prototypes before development</prototype_first>
      <design_system>Implement consistent design system</design_system>
      <responsive_design>Ensure responsive design across screen sizes</responsive_design>
      <platform_optimization>Optimize for each platform's conventions</platform_optimization>
    </development_workflow>
  </feature_command>
  
  <validate_command>
    <mobile_validation>
      <device_testing>Validate on physical devices and simulators</device_testing>
      <performance_profiling>Profile performance on target devices</performance_profiling>
      <app_store_validation>Validate against app store requirements</app_store_validation>
      <security_testing>Mobile-specific security testing</security_testing>
    </mobile_validation>
  </validate_command>
</command_customizations>
```

## Quality Gates Configuration

```xml
<quality_gates_configuration>
  <ui_ux_quality>
    <visual_consistency>
      <rule>Consistent design system implementation across all screens</rule>
      <validation>Automated screenshot comparison and design token validation</validation>
      <threshold>95% design system compliance</threshold>
    </visual_consistency>
    
    <accessibility_compliance>
      <rule>Full accessibility support for users with disabilities</rule>
      <validation>Automated accessibility testing and manual verification</validation>
      <threshold>100% critical accessibility requirements met</threshold>
    </accessibility_compliance>
    
    <responsive_design>
      <rule>Responsive design across all target screen sizes</rule>
      <validation>Automated responsive testing on device range</validation>
      <threshold>Perfect layout on all target devices</threshold>
    </responsive_design>
  </ui_ux_quality>
  
  <performance_quality>
    <launch_time>
      <rule>App launch time under 2 seconds on target devices</rule>
      <validation>Automated performance testing on device range</validation>
      <threshold>Cold start < 2s, warm start < 1s</threshold>
    </launch_time>
    
    <memory_usage>
      <rule>Memory usage within acceptable limits</rule>
      <validation>Memory profiling during typical usage scenarios</validation>
      <threshold>Memory usage < 150MB on low-end devices</threshold>
    </memory_usage>
    
    <battery_optimization>
      <rule>Minimal battery drain during normal usage</rule>
      <validation>Battery usage profiling over extended periods</validation>
      <threshold>Battery drain < 5% per hour during active use</threshold>
    </battery_optimization>
  </performance_quality>
  
  <platform_quality>
    <platform_guidelines>
      <rule>Adherence to platform-specific design guidelines</rule>
      <validation>Automated and manual platform guideline validation</validation>
      <threshold>100% compliance with platform UI guidelines</threshold>
    </platform_guidelines>
    
    <native_integration>
      <rule>Proper integration with native platform features</rule>
      <validation>Testing of native feature integration</validation>
      <threshold>All native features work correctly</threshold>
    </native_integration>
    
    <app_store_compliance>
      <rule>Full compliance with app store requirements</rule>
      <validation>App store validation and review simulation</validation>
      <threshold>Zero app store rejection risks</threshold>
    </app_store_compliance>
  </platform_quality>
</quality_gates_configuration>
```

## Module Selection

```xml
<module_selection>
  <core_modules>
    <mobile_development>
      <ui_component_library>Reusable UI components with platform optimization</ui_component_library>
      <device_integration>Native device feature integration patterns</device_integration>
      <performance_optimization>Mobile-specific performance optimization</performance_optimization>
      <testing_framework>Comprehensive mobile testing strategies</testing_framework>
    </mobile_development>
    
    <platform_specific>
      <ios_development condition="{{IOS_ENABLED}}">
        <swift_patterns>Swift-specific development patterns</swift_patterns>
        <xcode_integration>Xcode project management and automation</xcode_integration>
        <ios_deployment>iOS deployment and distribution</ios_deployment>
      </ios_development>
      
      <android_development condition="{{ANDROID_ENABLED}}">
        <kotlin_patterns>Kotlin-specific development patterns</kotlin_patterns>
        <android_studio_integration>Android Studio optimization</android_studio_integration>
        <android_deployment>Android deployment and distribution</android_deployment>
      </android_development>
      
      <cross_platform condition="{{CROSS_PLATFORM_FRAMEWORK}}">
        <shared_code_patterns>Cross-platform code sharing strategies</shared_code_patterns>
        <platform_bridging>Native platform bridging techniques</platform_bridging>
        <unified_testing>Cross-platform testing approaches</unified_testing>
      </cross_platform>
    </platform_specific>
  </core_modules>
  
  <quality_modules>
    <mobile_testing>
      <ui_testing>Automated UI testing with platform-specific tools</ui_testing>
      <device_testing>Physical device testing orchestration</device_testing>
      <performance_testing>Mobile performance benchmarking</performance_testing>
      <accessibility_testing>Accessibility compliance validation</accessibility_testing>
    </mobile_testing>
    
    <mobile_security>
      <secure_storage>Secure data storage and encryption</secure_storage>
      <authentication>Mobile authentication and biometrics</authentication>
      <network_security>Secure network communication</network_security>
      <code_obfuscation>Code protection and obfuscation</code_obfuscation>
    </mobile_security>
  </quality_modules>
  
  <development_modules>
    <ui_ux_development>
      <design_system>Consistent design system implementation</design_system>
      <animation_library>Smooth and performant animations</animation_library>
      <responsive_layout>Responsive design across devices</responsive_layout>
      <accessibility_framework>Accessibility implementation patterns</accessibility_framework>
    </ui_ux_development>
    
    <platform_integration>
      <native_modules>Native platform module integration</native_modules>
      <third_party_sdks>Third-party SDK integration patterns</third_party_sdks>
      <push_notifications>Push notification implementation</push_notifications>
      <offline_sync>Offline data synchronization</offline_sync>
    </platform_integration>
  </development_modules>
</module_selection>
```

## Framework Integration

```xml
<framework_integration>
  <optimal_frameworks>
    <primary_framework>CRISP - Creative, role-based development with personality</primary_framework>
    <secondary_framework>CARE - Context-aware development with evaluation</secondary_framework>
    <specialized_framework>FOCUS - User-focused development with scope clarity</specialized_framework>
  </optimal_frameworks>
  
  <framework_customization>
    <crisp_mobile_optimization>
      <capacity>Mobile development expertise with platform-specific knowledge</capacity>
      <role>Mobile developer with UX/UI focus and performance awareness</role>
      <insight>Mobile platform constraints, user behavior, and app store dynamics</insight>
      <statement>Clear mobile development tasks with platform-specific requirements</statement>
      <personality>User-focused, performance-conscious, platform-aware development approach</personality>
    </crisp_mobile_optimization>
    
    <care_mobile_optimization>
      <context>Mobile development context with platform, device, and user considerations</context>
      <action>Mobile-specific development actions with platform optimization</action>
      <result>Mobile app features with performance and UX validation</result>
      <evaluation>Mobile app quality assessment with device and platform testing</evaluation>
    </care_mobile_optimization>
  </framework_customization>
</framework_integration>
```

## Development Workflows

```xml
<development_workflows>
  <mobile_development_cycle>
    <design_phase>
      <step>Create user experience wireframes and prototypes</step>
      <step>Design visual interface with platform-specific guidelines</step>
      <step>Validate design with target user group</step>
      <step>Create design system and component library</step>
    </design_phase>
    
    <development_phase>
      <step>Implement UI components with responsive design</step>
      <step>Integrate native platform features and APIs</step>
      <step>Implement business logic with performance optimization</step>
      <step>Add offline functionality and data synchronization</step>
    </development_phase>
    
    <testing_phase>
      <step>Unit testing for business logic and utilities</step>
      <step>UI testing for user interface and interactions</step>
      <step>Integration testing for platform feature integration</step>
      <step>Performance testing on target device range</step>
    </testing_phase>
    
    <deployment_phase>
      <step>App store optimization and compliance validation</step>
      <step>Beta testing with TestFlight or Google Play Console</step>
      <step>App store submission and review process</step>
      <step>Production deployment and monitoring</step>
    </deployment_phase>
  </mobile_development_cycle>
  
  <platform_specific_workflows>
    <ios_workflow condition="{{IOS_ENABLED}}">
      <xcode_setup>Configure Xcode project with proper settings</xcode_setup>
      <cocoapods_setup>Set up dependency management with CocoaPods or SPM</cocoapods_setup>
      <simulator_testing>Test on iOS Simulator with various device configurations</simulator_testing>
      <device_testing>Test on physical iOS devices</device_testing>
      <app_store_preparation>Prepare app for App Store submission</app_store_preparation>
    </ios_workflow>
    
    <android_workflow condition="{{ANDROID_ENABLED}}">
      <gradle_setup>Configure Gradle build system and dependencies</gradle_setup>
      <emulator_testing>Test on Android Emulator with various API levels</emulator_testing>
      <device_testing>Test on physical Android devices</device_testing>
      <play_store_preparation>Prepare app for Google Play Store submission</play_store_preparation>
    </android_workflow>
  </platform_specific_workflows>
</development_workflows>
```

## Performance Optimization

```xml
<performance_optimization>
  <mobile_specific_optimizations>
    <startup_optimization>
      <lazy_loading>Implement lazy loading for non-critical components</lazy_loading>
      <preloading>Preload critical resources for faster startup</preloading>
      <splash_screen>Optimize splash screen for perceived performance</splash_screen>
      <cold_start>Minimize cold start time through optimization</cold_start>
    </startup_optimization>
    
    <memory_optimization>
      <image_optimization>Optimize images for different screen densities</image_optimization>
      <memory_management>Implement proper memory management patterns</memory_management>
      <cache_management>Efficient caching strategies for mobile</cache_management>
      <garbage_collection>Optimize for platform-specific garbage collection</garbage_collection>
    </memory_optimization>
    
    <battery_optimization>
      <background_processing>Optimize background processing for battery life</background_processing>
      <network_efficiency>Implement efficient network usage patterns</network_efficiency>
      <location_services>Optimize location services usage</location_services>
      <push_notifications>Efficient push notification handling</push_notifications>
    </battery_optimization>
  </mobile_specific_optimizations>
  
  <platform_optimizations>
    <ios_optimizations condition="{{IOS_ENABLED}}">
      <swift_optimization>Swift-specific performance optimizations</swift_optimization>
      <ios_lifecycle>Optimize for iOS app lifecycle events</ios_lifecycle>
      <core_data>Efficient Core Data usage patterns</core_data>
      <metal_graphics>Leverage Metal for graphics-intensive operations</metal_graphics>
    </ios_optimizations>
    
    <android_optimizations condition="{{ANDROID_ENABLED}}">
      <kotlin_optimization>Kotlin-specific performance optimizations</kotlin_optimization>
      <android_lifecycle>Optimize for Android activity/fragment lifecycle</android_lifecycle>
      <room_database>Efficient Room database operations</room_database>
      <renderscript>Leverage RenderScript for computation-intensive tasks</renderscript>
    </android_optimizations>
  </platform_optimizations>
</performance_optimization>
```

## Testing Strategy

```xml
<testing_strategy>
  <mobile_testing_pyramid>
    <unit_tests>
      <business_logic>Test business logic and utility functions</business_logic>
      <data_layer>Test data access and manipulation</data_layer>
      <view_models>Test view models and presentation logic</view_models>
      <coverage_target>80% code coverage for unit tests</coverage_target>
    </unit_tests>
    
    <integration_tests>
      <api_integration>Test API integration and data flow</api_integration>
      <database_integration>Test database operations and queries</database_integration>
      <native_integration>Test native platform feature integration</native_integration>
      <coverage_target>60% coverage for integration scenarios</coverage_target>
    </integration_tests>
    
    <ui_tests>
      <user_flows>Test critical user flows and navigation</user_flows>
      <ui_components>Test UI component behavior and rendering</ui_components>
      <accessibility>Test accessibility features and compliance</accessibility>
      <coverage_target>100% coverage for critical user flows</coverage_target>
    </ui_tests>
    
    <performance_tests>
      <load_testing>Test app performance under various loads</load_testing>
      <memory_testing>Test memory usage and leak detection</memory_testing>
      <battery_testing>Test battery usage during typical scenarios</battery_testing>
      <network_testing>Test app behavior under poor network conditions</network_testing>
    </performance_tests>
  </mobile_testing_pyramid>
  
  <device_testing_strategy>
    <simulator_testing>
      <ios_simulator>Test on iOS Simulator with various configurations</ios_simulator>
      <android_emulator>Test on Android Emulator with different API levels</android_emulator>
      <configuration_matrix>Test across screen sizes, OS versions, and orientations</configuration_matrix>
    </simulator_testing>
    
    <device_testing>
      <physical_devices>Test on range of physical devices</physical_devices>
      <cloud_testing>Use cloud testing services for device coverage</cloud_testing>
      <real_world_scenarios>Test in real-world usage scenarios</real_world_scenarios>
    </device_testing>
  </device_testing_strategy>
</testing_strategy>
```

## Deployment Configuration

```xml
<deployment_configuration>
  <app_store_optimization>
    <ios_app_store>
      <app_store_connect>Configure App Store Connect for iOS distribution</app_store_connect>
      <testflight>Set up TestFlight for beta testing</testflight>
      <app_review>Optimize app for App Store review process</app_review>
      <metadata_optimization>Optimize app metadata for discoverability</metadata_optimization>
    </ios_app_store>
    
    <google_play_store>
      <play_console>Configure Google Play Console for Android distribution</play_console>
      <internal_testing>Set up internal testing tracks</internal_testing>
      <play_review>Optimize app for Google Play review process</play_review>
      <store_listing>Optimize store listing for visibility</store_listing>
    </google_play_store>
  </app_store_optimization>
  
  <ci_cd_integration>
    <automated_builds>
      <build_triggers>Automated builds on code commits</build_triggers>
      <build_variants>Configure build variants for different environments</build_variants>
      <code_signing>Automated code signing and provisioning</code_signing>
      <artifact_management>Manage build artifacts and distributions</artifact_management>
    </automated_builds>
    
    <automated_testing>
      <test_execution>Automated test execution on builds</test_execution>
      <device_testing>Automated device testing integration</device_testing>
      <performance_testing>Automated performance benchmark execution</performance_testing>
      <security_scanning>Automated security vulnerability scanning</security_scanning>
    </automated_testing>
  </ci_cd_integration>
</deployment_configuration>
```

## Documentation Templates

```xml
<documentation_templates>
  <mobile_documentation>
    <architecture_docs>
      <app_architecture>Document app architecture and design patterns</app_architecture>
      <platform_integration>Document native platform integration approaches</platform_integration>
      <performance_architecture>Document performance optimization strategies</performance_architecture>
      <security_architecture>Document security implementation and best practices</security_architecture>
    </architecture_docs>
    
    <user_guides>
      <setup_guide>Mobile development environment setup</setup_guide>
      <development_guide>Mobile development workflow and best practices</development_guide>
      <testing_guide>Mobile testing strategies and implementation</testing_guide>
      <deployment_guide>Mobile app deployment and distribution</deployment_guide>
    </user_guides>
    
    <api_documentation>
      <native_apis>Document native platform API usage</native_apis>
      <third_party_apis>Document third-party service integrations</third_party_apis>
      <internal_apis>Document internal API design and usage</internal_apis>
      <sdk_documentation>Document custom SDK development and usage</sdk_documentation>
    </api_documentation>
  </mobile_documentation>
  
  <platform_specific_docs>
    <ios_documentation condition="{{IOS_ENABLED}}">
      <swift_guidelines>Swift coding standards and best practices</swift_guidelines>
      <xcode_configuration>Xcode project configuration and management</xcode_configuration>
      <ios_deployment>iOS deployment and distribution procedures</ios_deployment>
      <app_store_guidelines>App Store submission and optimization</app_store_guidelines>
    </ios_documentation>
    
    <android_documentation condition="{{ANDROID_ENABLED}}">
      <kotlin_guidelines>Kotlin coding standards and best practices</kotlin_guidelines>
      <gradle_configuration>Gradle build configuration and optimization</gradle_configuration>
      <android_deployment>Android deployment and distribution procedures</android_deployment>
      <play_store_guidelines>Google Play Store submission and optimization</play_store_guidelines>
    </android_documentation>
  </platform_specific_docs>
</documentation_templates>
```

## Success Metrics

```xml
<success_metrics>
  <development_metrics>
    <development_velocity>Feature delivery speed and consistency</development_velocity>
    <code_quality>Code quality scores and technical debt metrics</code_quality>
    <testing_coverage>Test coverage and quality metrics</testing_coverage>
    <performance_benchmarks>App performance against established benchmarks</performance_benchmarks>
  </development_metrics>
  
  <user_experience_metrics>
    <app_performance>App launch time, responsiveness, and stability</app_performance>
    <user_satisfaction>User ratings and feedback scores</user_satisfaction>
    <accessibility_compliance>Accessibility audit scores and user feedback</accessibility_compliance>
    <platform_consistency>Consistency with platform design guidelines</platform_consistency>
  </user_experience_metrics>
  
  <deployment_metrics>
    <app_store_approval>App store approval rates and time to approval</app_store_approval>
    <deployment_success>Deployment success rates and rollback frequency</deployment_success>
    <crash_rates>App crash rates and stability metrics</crash_rates>
    <adoption_rates>Feature adoption and user engagement metrics</adoption_rates>
  </deployment_metrics>
</success_metrics>
```

---

**Reference**: This template provides comprehensive mobile development domain configuration, enabling specialized framework adaptation for iOS, Android, and cross-platform mobile application development with optimized workflows, quality gates, and deployment strategies.