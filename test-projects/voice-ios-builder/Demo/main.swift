import Foundation
@preconcurrency import VoiceIOSBuilder

@main
struct VoiceIOSBuilderDemo {
    static func main() async {
        print("🎙️ Voice iOS Builder Demo")
        print("========================")
        
        // Initialize the main coordinator
        let coordinator = AppCoordinator()
        
        print("✅ AppCoordinator initialized")
        print("✅ All modules integrated and ready")
        
        // Test voice recording
        print("\n🎤 Testing voice recording...")
        await withCheckedContinuation { (continuation: CheckedContinuation<Void, Never>) in
            coordinator.startVoiceRecording { success in
                print(success ? "✅ Voice recording started" : "❌ Voice recording failed")
                continuation.resume()
            }
        }
        
        // Test voice processing
        print("\n🧠 Testing voice processing...")
        await withCheckedContinuation { (continuation: CheckedContinuation<Void, Never>) in
            coordinator.processVoiceInput("Create a calculator app with buttons") { result in
                switch result {
                case .success(let processedText):
                    print("✅ Voice processing successful: \(processedText)")
                case .failure(let error):
                    print("❌ Voice processing failed: \(error)")
                }
                continuation.resume()
            }
        }
        
        // Test code generation
        print("\n⚙️ Testing code generation...")
        let testRequest = VoiceRequest(
            originalText: "Create a calculator app",
            processedText: "Create a calculator app with buttons",
            intent: .createApp
        )
        
        await withCheckedContinuation { (continuation: CheckedContinuation<Void, Never>) in
            coordinator.triggerCodeGeneration(for: testRequest) { result in
                switch result {
                case .success(let code):
                    print("✅ Code generation successful!")
                    print("Generated \(code.components(separatedBy: .newlines).count) lines of SwiftUI code")
                case .failure(let error):
                    print("❌ Code generation failed: \(error)")
                }
                continuation.resume()
            }
        }
        
        print("\n🎉 Demo completed!")
    }
}