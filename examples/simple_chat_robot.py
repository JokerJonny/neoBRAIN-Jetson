from src.core.brain import NeoBrain
from src.legacy.personality_core import LegacyPersonality

def main():
    print("🚀 Starting NeoLegacy Simple Chat Robot Demo\n")
    
    brain = NeoBrain()
    personality = LegacyPersonality()
    
    print("You can now talk to the NeoBrain. Type 'exit' to quit.\n")
    
    while True:
        try:
            user_input = input("You: ")
            if user_input.lower() in ["exit", "quit"]:
                print("🧠 Session ended. Legacy preserved.")
                break
            
            # Add to legacy memory
            personality.add_memory(f"User said: {user_input}")
            
            response = brain.think(user_input)
            print(f"NeoBrain: {response}\n")
            
        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    main()
