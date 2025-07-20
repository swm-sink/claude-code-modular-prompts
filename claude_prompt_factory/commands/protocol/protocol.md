# /protocol - EPICCC Development & Deployment Protocol

**Purpose**: Execute a production-grade development and deployment workflow using the EPICCC (Evaluate, Plan, Implement, Check, Commit, Continue) cycle, an iterative, safety-focused methodology for achieving high-quality results.

## Usage
```bash
/protocol "[development goal]"
```

## The EPICCC Cycle

The `/protocol` command follows a rigorous, cyclical, six-phase process to ensure safe and successful outcomes.

```xml
<epiccc_cycle>
  <phase name="Evaluate">
    <description>Perform a comprehensive pre-work risk and impact assessment. I will analyze the development goal, map its dependencies, and assess the potential impact on the system and users. I will then present a summary of my findings and ask for your confirmation before proceeding.</description>
  </phase>
  
  <phase name="Plan">
    <description>Develop a strategic implementation plan, including a detailed rollout strategy and a comprehensive rollback plan. I will present this plan to you for your approval, and I will not proceed until you have confirmed that you are comfortable with the plan.</description>
  </phase>
  
  <phase name="Implement">
    <description>Execute the implementation plan in a controlled and monitored manner. I will provide a real-time dashboard of the progress, including health scores, performance metrics, and any active alerts. You will have the ability to pause the implementation or trigger a rollback at any time.</description>
  </phase>
  
  <phase name="Check">
    <description>Perform a thorough validation of the implementation, including functional, performance, and security testing. I will present a detailed report of the validation results and ask for your confirmation before committing the changes.</description>
  </phase>
  
  <phase name="Commit">
    <description>Commit the validated changes to the codebase in a safe, atomic transaction. This step ensures that the work is integrated into the main branch only after it has been thoroughly checked and confirmed.</description>
  </phase>
  
  <phase name="Continue">
    <description>After a successful commit, I will assess if the overall goal has been met to a high quality standard. If not, I will continue the cycle by spawning a new set of agents to address the remaining gaps or refine the solution further. The process concludes only when the quality bar is fully met.</description>
  </phase>
</epiccc_cycle>
```

## Use Cases

*   **High-Stakes Feature Development**: Develop and deploy critical features with a rigorous, quality-driven, and iterative process.
*   **Complex System Refactoring**: Safely refactor complex systems by breaking the work into manageable, verifiable, and iterative cycles.
*   **Autonomous Problem Solving**: Tackle complex problems by allowing the protocol to iteratively spawn agents until the desired quality standard is achieved. 