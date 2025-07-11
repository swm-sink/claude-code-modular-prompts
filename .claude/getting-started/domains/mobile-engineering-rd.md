# Mobile Engineering R&D Domain Template

| version | last_updated | status |
|---------|--------------|--------|
| 1.0.0   | 2025-07-11   | stable |

## Domain Overview

Mobile Engineering R&D domain template provides specialized framework configuration for advanced mobile application development with focus on research, innovation, and cutting-edge mobile technologies. This template optimizes the Claude Code Framework for mobile R&D workflows, experimental features, and next-generation mobile development patterns.

## Domain Configuration

```xml
<mobile_engineering_rd_domain>
  <purpose>Advanced mobile R&D framework for iOS, Android, and emerging mobile platforms</purpose>
  
  <target_platforms>
    <ios>Swift, SwiftUI, iOS SDK, ARKit, CoreML, Metal, WidgetKit</ios>
    <android>Kotlin, Jetpack Compose, Android SDK, ARCore, ML Kit, CameraX</android>
    <cross_platform>React Native, Flutter, Kotlin Multiplatform, WebAssembly</cross_platform>
    <emerging>Wear OS, CarPlay, Android Auto, Foldables, AR/VR</emerging>
  </target_platforms>
  
  <rd_characteristics>
    <performance_optimization>Battery efficiency, memory optimization, CPU/GPU utilization</performance_optimization>
    <emerging_technologies>5G, Edge computing, AI/ML on-device, AR/VR integration</emerging_technologies>
    <hardware_integration>Sensors, cameras, biometrics, NFC, wireless charging</hardware_integration>
    <experimental_features>Beta APIs, cutting-edge frameworks, prototype development</experimental_features>
    <cross_platform_innovation>Shared business logic, platform-specific optimizations</cross_platform_innovation>
  </rd_characteristics>
</mobile_engineering_rd_domain>
```

## Template Variables

```xml
<template_variables>
  <platform_selection>
    <ios_enabled>{{IOS_ENABLED:boolean}}</ios_enabled>
    <android_enabled>{{ANDROID_ENABLED:boolean}}</android_enabled>
    <cross_platform_framework>{{CROSS_PLATFORM_FRAMEWORK:react_native|flutter|kotlin_multiplatform|xamarin}}</cross_platform_framework>
    <emerging_platforms>{{EMERGING_PLATFORMS:wear_os|carplay|android_auto|foldables|ar_vr}}</emerging_platforms>
  </platform_selection>
  
  <rd_configuration>
    <research_focus>{{RESEARCH_FOCUS:performance|ai_ml|ar_vr|iot|emerging_hardware}}</research_focus>
    <experimental_features>{{EXPERIMENTAL_FEATURES:boolean}}</experimental_features>
    <prototype_development>{{PROTOTYPE_DEVELOPMENT:boolean}}</prototype_development>
    <innovation_cycle>{{INNOVATION_CYCLE:rapid|structured|long_term}}</innovation_cycle>
  </rd_configuration>
  
  <advanced_features>
    <ai_ml_integration>{{AI_ML_INTEGRATION:coreml|mlkit|tensorflow_lite|custom}}</ai_ml_integration>
    <ar_vr_capabilities>{{AR_VR_CAPABILITIES:arkit|arcore|unity|unreal}}</ar_vr_capabilities>
    <performance_profiling>{{PERFORMANCE_PROFILING:instruments|systrace|custom_profilers}}</performance_profiling>
    <security_level>{{SECURITY_LEVEL:standard|enhanced|research_grade}}</security_level>
  </advanced_features>
</template_variables>
```

## Command Customizations

```xml
<command_customizations>
  <task_command>
    <mobile_rd_thinking>
      <performance_first>Optimize for battery life, memory usage, and responsiveness</performance_first>
      <platform_native>Leverage platform-specific capabilities and best practices</platform_native>
      <device_compatibility>Ensure compatibility across device ecosystem</device_compatibility>
      <future_proofing>Design for upcoming OS versions and hardware capabilities</future_proofing>
      <research_validation>Validate research hypotheses through measurable outcomes</research_validation>
    </mobile_rd_thinking>
    
    <quality_gates>
      <performance_benchmarks>Battery usage, memory footprint, startup time, frame rates</performance_benchmarks>
      <device_testing>Physical device testing across target range</device_testing>
      <accessibility_compliance>WCAG 2.1 AA compliance, platform accessibility</accessibility_compliance>
      <security_validation>Security review, data protection, privacy compliance</security_validation>
      <app_store_readiness>App store guidelines compliance, metadata optimization</app_store_readiness>
    </quality_gates>
  </task_command>
  
  <feature_command>
    <mobile_rd_feature_planning>
      <research_hypothesis>Define measurable research objectives and success criteria</research_hypothesis>
      <platform_optimization>Optimize for each platform's unique characteristics</platform_optimization>
      <performance_impact>Assess and optimize performance implications</performance_impact>
      <hardware_utilization>Leverage device-specific hardware capabilities</hardware_utilization>
      <user_experience>Focus on intuitive, platform-native user experience</user_experience>
    </mobile_rd_feature_planning>
    
    <development_workflow>
      <prototype_validation>Rapid prototyping for concept validation</prototype_validation>
      <iterative_development>Continuous integration with user feedback</iterative_development>
      <cross_platform_sync>Maintain feature parity across platforms</cross_platform_sync>
      <performance_monitoring>Real-time performance monitoring and optimization</performance_monitoring>
    </development_workflow>
  </feature_command>
  
  <validate_command>
    <mobile_rd_validation>
      <device_lab_testing>Comprehensive testing across device ecosystem</device_lab_testing>
      <performance_profiling>CPU, memory, battery, network performance analysis</performance_profiling>
      <real_world_testing>Beta testing with target user groups</real_world_testing>
      <research_outcomes>Validation of research hypotheses and metrics</research_outcomes>
      <scalability_testing>Performance under scale and stress conditions</scalability_testing>
    </mobile_rd_validation>
  </validate_command>
</command_customizations>
```

## Quality Gates

```xml
<quality_gates>
  <performance_requirements>
    <startup_time>App launch time < 2 seconds on target devices</startup_time>
    <memory_usage>Memory footprint within platform recommendations</memory_usage>
    <battery_efficiency>Battery drain < 5% per hour of active use</battery_efficiency>
    <frame_rate>60 FPS for animations and interactions</frame_rate>
    <network_efficiency>Optimize for various network conditions</network_efficiency>
  </performance_requirements>
  
  <code_quality_standards>
    <architecture_patterns>Clean architecture, MVVM, dependency injection</architecture_patterns>
    <testing_coverage>Unit tests 80%+, UI tests for critical paths</testing_coverage>
    <code_style>Platform-specific style guides, automated formatting</code_style>
    <security_practices>Secure coding practices, vulnerability scanning</security_practices>
  </code_quality_standards>
  
  <platform_compliance>
    <ios_compliance>Apple Human Interface Guidelines, App Store Review Guidelines</ios_compliance>
    <android_compliance>Material Design, Google Play Policy, Android Quality Guidelines</android_compliance>
    <accessibility>Platform accessibility standards, screen reader compatibility</accessibility>
    <privacy_compliance>GDPR, CCPA, platform-specific privacy requirements</privacy_compliance>
  </platform_compliance>
</quality_gates>
```

## Research & Innovation Focus

```xml
<research_innovation>
  <emerging_technologies>
    <ai_ml_on_device>Core ML, ML Kit, TensorFlow Lite, custom inference engines</ai_ml_on_device>
    <ar_vr_integration>ARKit, ARCore, Unity, Unreal Engine, WebXR</ar_vr_integration>
    <edge_computing>5G capabilities, edge AI, real-time processing</edge_computing>
    <iot_integration>Bluetooth LE, WiFi Direct, NFC, sensor fusion</iot_integration>
  </emerging_technologies>
  
  <performance_research>
    <battery_optimization>Advanced power management, background processing</battery_optimization>
    <memory_efficiency>Memory pools, object reuse, garbage collection optimization</memory_efficiency>
    <rendering_optimization>Metal, Vulkan, custom rendering pipelines</rendering_optimization>
    <network_optimization>Protocol optimization, caching strategies, offline capabilities</network_optimization>
  </performance_research>
  
  <user_experience_innovation>
    <adaptive_interfaces>Context-aware UI, predictive interactions</adaptive_interfaces>
    <accessibility_innovation>Advanced accessibility features, inclusive design</accessibility_innovation>
    <cross_platform_ux>Consistent experience across diverse platforms</cross_platform_ux>
    <gesture_recognition>Advanced gesture recognition, haptic feedback</gesture_recognition>
  </user_experience_innovation>
</research_innovation>
```

## Technology Stack

```xml
<technology_stack>
  <ios_technologies>
    <languages>Swift, Objective-C, SwiftUI, UIKit</languages>
    <frameworks>Combine, CoreData, CloudKit, WidgetKit, App Clips</frameworks>
    <tools>Xcode, Instruments, TestFlight, Xcode Cloud</tools>
    <advanced>Metal, CoreML, ARKit, RealityKit, CreateML</advanced>
  </ios_technologies>
  
  <android_technologies>
    <languages>Kotlin, Java, Jetpack Compose, Android Views</languages>
    <frameworks>Android Architecture Components, Dagger/Hilt, Retrofit</frameworks>
    <tools>Android Studio, Gradle, Firebase, Play Console</tools>
    <advanced>CameraX, ML Kit, ARCore, Android NDK</advanced>
  </android_technologies>
  
  <cross_platform_technologies>
    <react_native>React Native, Expo, Flipper, CodePush</react_native>
    <flutter>Flutter, Dart, Firebase, Platform Channels</flutter>
    <kotlin_multiplatform>Kotlin Multiplatform Mobile, Ktor, SQLDelight</kotlin_multiplatform>
  </cross_platform_technologies>
  
  <testing_automation>
    <ios_testing>XCTest, XCUITest, Earl Grey, Appium</ios_testing>
    <android_testing>JUnit, Espresso, UI Automator, Robolectric</android_testing>
    <cross_platform_testing>Detox, Maestro, Appium, Selenium</cross_platform_testing>
  </testing_automation>
</technology_stack>
```

## Best Practices

```xml
<best_practices>
  <architecture_principles>
    <separation_of_concerns>Clear separation between UI, business logic, and data layers</separation_of_concerns>
    <dependency_injection>Modular architecture with dependency injection</dependency_injection>
    <reactive_programming>Reactive patterns for data flow and state management</reactive_programming>
    <clean_architecture>Clean architecture principles for maintainability</clean_architecture>
  </architecture_principles>
  
  <performance_optimization>
    <lazy_loading>Implement lazy loading for images and content</lazy_loading>
    <memory_management>Proper memory management and leak prevention</memory_management>
    <background_processing>Efficient background task handling</background_processing>
    <network_optimization>Caching, compression, and efficient API usage</network_optimization>
  </performance_optimization>
  
  <security_practices>
    <data_protection>Encrypt sensitive data, secure storage</data_protection>
    <network_security>Certificate pinning, secure communication</network_security>
    <authentication>Secure authentication and authorization</authentication>
    <privacy_compliance>Privacy-first design, data minimization</privacy_compliance>
  </security_practices>
</best_practices>
```

## Usage Instructions

```xml
<usage_instructions>
  <initialization>
    <setup_command>Use `/init` command with mobile-engineering-rd template</setup_command>
    <configuration>Configure platform targets and R&D focus areas</configuration>
    <validation>Validate setup with `/validate` command</validation>
  </initialization>
  
  <development_workflow>
    <research_phase>Define research objectives and success metrics</research_phase>
    <prototype_phase>Rapid prototyping and concept validation</prototype_phase>
    <development_phase>Iterative development with continuous validation</development_phase>
    <optimization_phase>Performance optimization and platform-specific tuning</optimization_phase>
  </development_workflow>
  
  <quality_assurance>
    <continuous_testing>Automated testing throughout development cycle</continuous_testing>
    <performance_monitoring>Real-time performance monitoring and alerts</performance_monitoring>
    <user_feedback>Continuous user feedback integration</user_feedback>
    <research_validation>Regular validation of research hypotheses</research_validation>
  </quality_assurance>
</usage_instructions>
```

**Usage**: Apply this template when working on mobile R&D projects requiring advanced performance optimization, emerging technology integration, or innovative mobile experiences. Optimized for research-driven mobile development with focus on measurable outcomes and cutting-edge capabilities.