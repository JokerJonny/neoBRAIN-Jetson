import json
from pathlib import Path
from datetime import datetime

class LegacyPersonality:
    def __init__(self):
        self.memory_file = Path("data/legacy_memory.json")
        self.memory_file.parent.mkdir(exist_ok=True)
        self.load_memory()

    def load_memory(self):
        if self.memory_file.exists():
            with open(self.memory_file, "r") as f:
                self.memory = json.load(f)
        else:
            self.memory = {
                "name": "NeoLegacy",
                "core_traits": ["wise", "protective", "curious", "respectful_of_history"],
                "memories": []
            }

    def save_memory(self):
        with open(self.memory_file, "w") as f:
            json.dump(self.memory, f, indent=2)

    def add_memory(self, text: str):
        entry = {
            "timestamp": datetime.now().isoformat(),
            "content": text
        }
        self.memory["memories"].append(entry)
        self.save_memory()
        print(f"💾 Legacy memory preserved: {text[:60]}...")

    def get_personality_prompt(self):
        return f"""You are {self.memory['name']}, a wise guardian AI preserving human legacy.
Core traits: {', '.join(self.memory['core_traits'])}
Stay respectful, thoughtful, and helpful."""

if __name__ == "__main__":
    lp = LegacyPersonality()
    lp.add_memory("First activation of NeoLegacy Brain.")
    print("Legacy Personality Core initialized.")
