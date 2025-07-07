import SwiftUI

#if canImport(UIKit)
import UIKit
#endif

struct ContentView: View {
    @StateObject private var appCoordinator = AppCoordinator()
    @State private var showingProjectList = false
    @State private var animationScale: CGFloat = 1.0
    
    var body: some View {
        NavigationView {
            VStack(spacing: 30) {
                // Header
                headerView
                
                // Status Display
                statusView
                
                // Voice Button
                voiceButton
                
                // Real-time Feedback
                feedbackView
                
                // Recent Projects
                if !appCoordinator.recentProjects.isEmpty {
                    recentProjectsView
                }
                
                Spacer()
            }
            .padding()
            .navigationTitle("Voice iOS Builder")
            #if !os(macOS)
            .navigationBarTitleDisplayMode(.large)
            #endif
            .toolbar {
                ToolbarItem(placement: .primaryAction) {
                    Button("Projects") {
                        showingProjectList = true
                    }
                }
            }
            .sheet(isPresented: $showingProjectList) {
                ProjectListView(appCoordinator: appCoordinator)
            }
        }
    }
    
    // MARK: - Header View
    private var headerView: some View {
        VStack(spacing: 10) {
            Image(systemName: "mic.circle.fill")
                .font(.system(size: 60))
                .foregroundColor(.blue)
            
            Text("Speak to Create Apps")
                .font(.title2)
                .fontWeight(.medium)
                .multilineTextAlignment(.center)
        }
    }
    
    // MARK: - Status View
    private var statusView: some View {
        HStack {
            Circle()
                .fill(statusColor)
                .frame(width: 12, height: 12)
            
            Text(statusText)
                .font(.headline)
                .foregroundColor(.secondary)
        }
        .padding(.horizontal, 20)
        .padding(.vertical, 10)
        .background(Color.gray.opacity(0.1))
        .cornerRadius(20)
    }
    
    // MARK: - Voice Button
    private var voiceButton: some View {
        Button(action: handleVoiceButtonTap) {
            HStack {
                Image(systemName: voiceButtonIcon)
                    .font(.title2)
                
                Text(voiceButtonText)
                    .font(.headline)
                    .fontWeight(.semibold)
            }
            .foregroundColor(.white)
            .padding(.horizontal, 30)
            .padding(.vertical, 15)
            .background(voiceButtonColor)
            .cornerRadius(25)
            .scaleEffect(animationScale)
        }
        .disabled(appCoordinator.isProcessing)
        .animation(.easeInOut(duration: 0.1), value: animationScale)
    }
    
    // MARK: - Feedback View
    private var feedbackView: some View {
        Group {
            if !appCoordinator.feedbackMessage.isEmpty {
                VStack(spacing: 10) {
                    if appCoordinator.isProcessing {
                        ProgressView()
                            .scaleEffect(0.8)
                    }
                    
                    Text(appCoordinator.feedbackMessage)
                        .font(.body)
                        .multilineTextAlignment(.center)
                        .foregroundColor(.secondary)
                        .padding(.horizontal)
                }
                .padding()
                .background(Color.blue.opacity(0.1))
                .cornerRadius(15)
                .transition(.opacity.combined(with: .scale))
            }
        }
        .animation(.easeInOut, value: appCoordinator.feedbackMessage)
    }
    
    // MARK: - Recent Projects View
    private var recentProjectsView: some View {
        VStack(alignment: .leading, spacing: 15) {
            Text("Recent Projects")
                .font(.headline)
                .padding(.horizontal)
            
            ScrollView(.horizontal, showsIndicators: false) {
                LazyHStack(spacing: 15) {
                    ForEach(Array(appCoordinator.recentProjects.prefix(5)), id: \.id) { project in
                        ProjectCard(project: project, appCoordinator: appCoordinator)
                    }
                }
                .padding(.horizontal)
            }
        }
    }
    
    // MARK: - Computed Properties
    private var statusColor: Color {
        switch appCoordinator.currentState {
        case .idle:
            return .green
        case .recording:
            return .red
        case .processing, .generating:
            return .orange
        case .completed:
            return .blue
        case .error:
            return .red
        }
    }
    
    private var statusText: String {
        switch appCoordinator.currentState {
        case .idle:
            return "Ready"
        case .recording:
            return "Listening"
        case .processing:
            return "Processing"
        case .generating:
            return "Generating"
        case .completed:
            return "Completed"
        case .error(let message):
            return "Error: \(message)"
        }
    }
    
    private var voiceButtonIcon: String {
        switch appCoordinator.currentState {
        case .recording:
            return "stop.circle.fill"
        default:
            return "mic.circle.fill"
        }
    }
    
    private var voiceButtonText: String {
        switch appCoordinator.currentState {
        case .recording:
            return "Stop Recording"
        case .processing, .generating:
            return "Processing..."
        default:
            return "Start Recording"
        }
    }
    
    private var voiceButtonColor: Color {
        switch appCoordinator.currentState {
        case .recording:
            return .red
        case .processing, .generating:
            return .gray
        default:
            return .blue
        }
    }
    
    // MARK: - Actions
    private func handleVoiceButtonTap() {
        // Add haptic feedback (iOS only)
        #if canImport(UIKit) && !os(macOS)
        let impactFeedback = UIImpactFeedbackGenerator(style: .medium)
        impactFeedback.impactOccurred()
        #endif
        
        // Animate button press
        animationScale = 0.95
        DispatchQueue.main.asyncAfter(deadline: .now() + 0.1) {
            animationScale = 1.0
        }
        
        switch appCoordinator.currentState {
        case .idle:
            startVoiceRecording()
        case .recording:
            appCoordinator.stopVoiceRecording()
        default:
            break
        }
    }
    
    private func startVoiceRecording() {
        appCoordinator.startVoiceRecording { success in
            if !success {
                // Handle recording failure
                print("Failed to start voice recording")
            }
        }
    }
}

// MARK: - Project Card View
struct ProjectCard: View {
    let project: Project
    let appCoordinator: AppCoordinator
    
    var body: some View {
        VStack(alignment: .leading, spacing: 10) {
            HStack {
                Image(systemName: "app.fill")
                    .foregroundColor(.blue)
                
                Spacer()
                
                Button(action: {
                    openInSimulator()
                }) {
                    Image(systemName: "play.circle.fill")
                        .foregroundColor(.green)
                }
            }
            
            Text(project.name)
                .font(.headline)
                .lineLimit(1)
            
            Text(project.description)
                .font(.caption)
                .foregroundColor(.secondary)
                .lineLimit(2)
        }
        .padding()
        .frame(width: 180, height: 100)
        .background(Color.gray.opacity(0.1))
        .cornerRadius(15)
    }
    
    private func openInSimulator() {
        // In a real implementation, this would trigger the simulator
        print("Opening \(project.name) in simulator")
    }
}

// MARK: - Project List View
struct ProjectListView: View {
    @ObservedObject var appCoordinator: AppCoordinator
    @Environment(\.dismiss) private var dismiss
    
    var body: some View {
        NavigationView {
            List {
                ForEach(appCoordinator.recentProjects, id: \.id) { project in
                    ProjectRow(project: project)
                }
                .onDelete(perform: deleteProjects)
            }
            .navigationTitle("All Projects")
            #if !os(macOS)
            .navigationBarTitleDisplayMode(.large)
            #endif
            .toolbar {
                ToolbarItem(placement: .primaryAction) {
                    Button("Done") {
                        dismiss()
                    }
                }
            }
        }
    }
    
    private func deleteProjects(offsets: IndexSet) {
        // In a real implementation, this would delete projects
        for index in offsets {
            let project = appCoordinator.recentProjects[index]
            print("Deleting project: \(project.name)")
        }
    }
}

// MARK: - Project Row View
struct ProjectRow: View {
    let project: Project
    
    var body: some View {
        VStack(alignment: .leading, spacing: 5) {
            Text(project.name)
                .font(.headline)
            
            Text(project.description)
                .font(.subheadline)
                .foregroundColor(.secondary)
                .lineLimit(2)
            
            Text("Created: \(project.createdAt, style: .date)")
                .font(.caption)
                .foregroundColor(.secondary)
        }
        .padding(.vertical, 5)
    }
}

// MARK: - Preview
struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}