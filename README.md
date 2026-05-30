# neoBRAIN-Jetson

**neoBRAIN v1.0** — Portable Edge AI Robotic Brain for NeoLegacy

A modular, on-device AI brain designed to run on **NVIDIA Jetson Orin Nano Super** and higher. Combines local LLMs, Vision, Speech, Memory, and Robotics control — all running locally with no cloud dependency.

### Goals
- Preserve legacy voices, stories, and personalities on edge devices
- Enable intelligent real-time robotic behavior
- Low power, portable, and fully open source

### Key Features
- Local LLM & VLM inference (llama.cpp + TensorRT)
- Voice interaction (Whisper STT + Piper TTS)
- Persistent memory system
- ROS2 robotics integration
- Legacy personality core

### Recommended Hardware
- **Jetson Orin Nano Super 8GB** (best starting point)

### Quick Start

```bash
git clone https://github.com/JokerJonny/neoBRAIN-Jetson.git
cd neoBRAIN-Jetson
chmod +x setup.sh
./setup.sh
python src/core/brain.py
