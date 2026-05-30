# Hardware Guide - neoBRAIN-Jetson

## Recommended Setup

**Primary Target:**
- **NVIDIA Jetson Orin Nano Super (8GB)** — Best balance of performance, power, and price.

**Minimum:**
- Jetson Orin Nano 8GB

**Higher Performance:**
- Jetson Orin NX 16GB
- Jetson Thor series (future proof)

## Power Recommendations
- Use official NVIDIA power supply (or 65W+ USB-C PD)
- For portable use: 12V battery pack with good current rating

## Peripherals
- USB Camera or CSI camera
- USB Microphone + Speaker
- Motor controllers / ROS2 compatible hardware

## Setup Order
1. Flash latest JetPack 6
2. Run `./setup.sh`
3. Run `./scripts/download_models.sh`
4. Test with `python examples/simple_chat_robot.py`
