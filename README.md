# 🧠 neoBRAIN-Jetson

![neoBRAIN Logo](https://neo-shade.com/neoBRAIN.jpg)

**neoBRAIN v1.0** — Portable Edge AI Robotic Brain for **NeoLegacy**

A powerful, fully local AI brain built for **NVIDIA Jetson** platforms. Designed to preserve human legacy, power intelligent robots, and run advanced LLMs/VLMs on-device with zero cloud dependency.

---

### ✨ Key Features
- **Local LLM Inference** (llama.cpp + TensorRT)
- **Voice Interaction** (Whisper STT + Piper TTS)
- **Legacy Memory & Personality System**
- **ROS2 Robotics Ready**
- **Low Power Edge Computing**
- **Docker Support**

---

### 🎯 Recommended Hardware

![Jetson Orin Nano Super](https://neo-shade.com/jetson.jpg)

**Best Choice**: **[NVIDIA Jetson Orin Nano Super Developer Kit](https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/jetson-orin/nano-super-developer-kit/)**

---

### 🚀 Quick Start

```bash
git clone https://github.com/JokerJonny/neoBRAIN-Jetson.git
cd neoBRAIN-Jetson

chmod +x setup.sh
./setup.sh

chmod +x scripts/download_models.sh
./scripts/download_models.sh

python examples/simple_chat_robot.py
