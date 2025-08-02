# Progress Tracking

**Purpose**: Monitor and track workflow execution progress across orchestrated systems with real-time updates, performance metrics, and completion analysis.

**Usage**: 
- Track task execution progress across complex orchestrated workflows
- Monitor real-time performance metrics and completion percentages
- Provide detailed progress reports for DAG orchestrators and agent systems
- Generate milestone notifications and completion alerts
- Analyze workflow bottlenecks and performance optimization opportunities

**Compatibility**: 
- **Works with**: dag-orchestrator, agent-orchestration, task-execution, progress-indicator
- **Requires**: Workflow execution data and task completion events
- **Conflicts**: quick-command (monitoring overhead not needed for simple tasks)

**Implementation**:
```python
# Orchestration progress tracking system
class ProgressTracker:
    def __init__(self):
        self.active_workflows = {}
        self.progress_listeners = []
        self.performance_metrics = PerformanceMetrics()
        
    def track_workflow(self, workflow_id, total_tasks, milestones=None):
        workflow_progress = WorkflowProgress(
            workflow_id=workflow_id,
            total_tasks=total_tasks,
            completed_tasks=0,
            milestones=milestones or [],
            start_time=time.time()
        )
        
        self.active_workflows[workflow_id] = workflow_progress
        self.notify_listeners("workflow_started", workflow_progress)
        
        return workflow_progress
    
    def update_task_progress(self, workflow_id, task_id, status, completion_percentage=None):
        if workflow_id not in self.active_workflows:
            raise ValueError(f"Workflow {workflow_id} not being tracked")
            
        workflow = self.active_workflows[workflow_id]
        
        # Update task status
        task_update = TaskUpdate(
            task_id=task_id,
            status=status,
            completion_percentage=completion_percentage,
            timestamp=time.time()
        )
        
        workflow.update_task(task_update)
        
        # Check for milestone completion
        if status == "completed":
            self.check_milestone_completion(workflow)
        
        # Update performance metrics
        self.performance_metrics.record_task_update(workflow_id, task_update)
        
        # Notify listeners of progress update
        self.notify_listeners("task_updated", workflow, task_update)
        
        return workflow.get_overall_progress()
    
    def get_workflow_status(self, workflow_id):
        if workflow_id not in self.active_workflows:
            return None
            
        workflow = self.active_workflows[workflow_id]
        
        return WorkflowStatus(
            workflow_id=workflow_id,
            overall_progress=workflow.get_overall_progress(),
            completed_tasks=workflow.completed_tasks,
            total_tasks=workflow.total_tasks,
            current_milestone=workflow.get_current_milestone(),
            estimated_completion=self.estimate_completion_time(workflow),
            performance_metrics=self.performance_metrics.get_workflow_metrics(workflow_id)
        )
    
    def check_milestone_completion(self, workflow):
        current_progress = workflow.get_overall_progress()
        
        for milestone in workflow.milestones:
            if not milestone.completed and current_progress >= milestone.threshold:
                milestone.completed = True
                milestone.completion_time = time.time()
                
                self.notify_listeners("milestone_reached", workflow, milestone)
    
    def estimate_completion_time(self, workflow):
        if workflow.completed_tasks == 0:
            return None
            
        elapsed_time = time.time() - workflow.start_time
        avg_time_per_task = elapsed_time / workflow.completed_tasks
        remaining_tasks = workflow.total_tasks - workflow.completed_tasks
        
        estimated_remaining_time = avg_time_per_task * remaining_tasks
        estimated_completion = time.time() + estimated_remaining_time
        
        return estimated_completion
    
    def generate_progress_report(self, workflow_id):
        workflow = self.active_workflows.get(workflow_id)
        if not workflow:
            return None
            
        performance_data = self.performance_metrics.get_workflow_metrics(workflow_id)
        
        return ProgressReport(
            workflow_id=workflow_id,
            summary=self.generate_summary(workflow),
            detailed_progress=workflow.get_detailed_progress(),
            milestones=workflow.milestones,
            performance_analysis=performance_data,
            bottlenecks=self.identify_bottlenecks(workflow, performance_data),
            recommendations=self.generate_optimization_recommendations(workflow, performance_data)
        )

# Real-time progress monitoring
class ProgressListener:
    def on_workflow_started(self, workflow):
        print(f"Workflow {workflow.workflow_id} started with {workflow.total_tasks} tasks")
    
    def on_task_updated(self, workflow, task_update):
        progress = workflow.get_overall_progress()
        print(f"Task {task_update.task_id}: {task_update.status} - Overall progress: {progress:.1f}%")
    
    def on_milestone_reached(self, workflow, milestone):
        print(f"Milestone reached: {milestone.name} at {workflow.get_overall_progress():.1f}% completion")

# Performance metrics tracking
class PerformanceMetrics:
    def __init__(self):
        self.task_durations = {}
        self.workflow_metrics = {}
    
    def record_task_update(self, workflow_id, task_update):
        if workflow_id not in self.workflow_metrics:
            self.workflow_metrics[workflow_id] = {
                'task_count': 0,
                'total_duration': 0,
                'bottlenecks': [],
                'throughput': []
            }
        
        metrics = self.workflow_metrics[workflow_id]
        
        if task_update.status == "completed":
            metrics['task_count'] += 1
            # Calculate throughput
            current_throughput = metrics['task_count'] / (time.time() - task_update.timestamp)
            metrics['throughput'].append(current_throughput)
    
    def get_workflow_metrics(self, workflow_id):
        return self.workflow_metrics.get(workflow_id, {})
```

**Category**: orchestration | **Complexity**: moderate | **Time**: 2 hours