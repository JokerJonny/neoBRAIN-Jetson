#!/bin/bash
echo "====================================="
echo "   Downloading Models for neoBRAIN"
echo "====================================="

mkdir -p models

echo "Downloading recommended models (this may take time)..."

# Qwen2.5 7B (good balance for Jetson)
wget -O models/Qwen2.5-7B-Instruct-Q4_K_M.gguf https://huggingface.co/Qwen/Qwen2.5-7B-Instruct-GGUF/resolve/main/Qwen2.5-7B-Instruct-Q4_K_M.gguf

# Smaller VLM for vision
echo "Note: For VLM, use Hugging Face or Ollama separately for now."

echo ""
echo "✅ Models downloaded to /models folder"
echo "You can add more models later."
echo "====================================="
