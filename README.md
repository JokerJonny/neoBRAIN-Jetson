# neoBRAIN-Jetson

**neoBRAIN v1.0** — Portable Edge AI Robotic Brain for NeoLegacy

A modular, fully local AI brain built for **NVIDIA Jetson** platforms. Designed to preserve legacy, enable intelligent robotics, and run powerful LLMs/VLMs on-device.

### Features
- Local LLM inference (llama.cpp)
- Voice interaction (STT + TTS)
- Legacy memory & personality system
- ROS2-ready robotics support
- Docker support

### Quick Start

```bash
# 1. Clone
git clone https://github.com/JokerJonny/neoBRAIN-Jetson.git
cd neoBRAIN-Jetson

# 2. Setup
chmod +x setup.sh
./setup.sh

# 3. Download models
chmod +x scripts/download_models.sh
./scripts/download_models.sh

# 4. Run demo
python examples/simple_chat_robot.py
