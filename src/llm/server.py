import subprocess
import time
from pathlib import Path

class LLM_Server:
    def __init__(self):
        self.model_path = Path("models/Qwen2.5-7B-Instruct-Q4_K_M.gguf")
        self.server_process = None

    def start_server(self, port=8080):
        """Start llama.cpp server"""
        if not self.model_path.exists():
            print("⚠️ Model not found. Run ./scripts/download_models.sh first.")
            return False

        cmd = [
            "llama-server",
            "-m", str(self.model_path),
            "--port", str(port),
            "-c", "8192",
            "--n-gpu-layers", "999"
        ]

        print(f"🚀 Starting LLM server on port {port}...")
        self.server_process = subprocess.Popen(cmd)
        time.sleep(5)  # Wait for server to start
        print("✅ LLM Server is running!")
        return True

    def stop_server(self):
        if self.server_process:
            self.server_process.terminate()
            print("🛑 LLM Server stopped.")

if __name__ == "__main__":
    server = LLM_Server()
    server.start_server()
