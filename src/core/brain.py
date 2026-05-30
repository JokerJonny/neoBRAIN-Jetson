import yaml
import sys
from pathlib import Path
from datetime import datetime

class NeoBrain:
    def __init__(self):
        self.config = self.load_config()
        self.name = self.config['brain']['name']
        print(f"🧠 {self.name} v{self.config['brain']['version']} initialized on {self.config['brain']['hardware']}")
        print("NeoLegacy Edge Brain is now online.\n")

    def load_config(self):
        config_path = Path("config/config.yaml")
        if not config_path.exists():
            print("⚠️ Config file not found! Using defaults.")
            return {"brain": {"name": "NeoLegacy Brain", "version": "1.0"}}
        with open(config_path, "r") as f:
            return yaml.safe_load(f)

    def think(self, prompt: str):
        """Core reasoning function - will connect to LLM later"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        print(f"[{timestamp}] Thinking about: {prompt[:80]}...")
        
        # Placeholder response (we'll replace with real LLM call soon)
        response = f"I am {self.name}. I have received your message and am processing it with full NeoLegacy awareness."
        
        return response

    def run(self):
        print("Type 'exit' to quit.\n")
        while True:
            try:
                user_input = input("You: ")
                if user_input.lower() in ["exit", "quit", "bye"]:
                    print("🧠 NeoBrain shutting down. Legacy preserved.")
                    break
                response = self.think(user_input)
                print(f"NeoBrain: {response}\n")
            except KeyboardInterrupt:
                print("\n🧠 Shutdown signal received.")
                break

if __name__ == "__main__":
    brain = NeoBrain()
    brain.run()
