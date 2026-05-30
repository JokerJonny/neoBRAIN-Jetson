#!/bin/bash
echo "====================================="
echo "   neoBRAIN-Jetson Setup Script"
echo "====================================="

echo "Updating system packages..."
sudo apt update && sudo apt upgrade -y

echo "Installing essential packages..."
sudo apt install -y python3-pip python3-venv git curl wget nano htop portaudio19-dev

echo "Creating Python virtual environment..."
python3 -m venv venv
source venv/bin/activate

echo "Installing Python dependencies..."
pip install --upgrade pip
pip install pyyaml numpy pillow opencv-python-headless sounddevice pyaudio faster-whisper piper-tts langchain langchain-community chromadb

echo ""
echo "✅ Setup completed successfully!"
echo "To activate environment: source venv/bin/activate"
echo "Next step: ./scripts/download_models.sh"
echo "====================================="
