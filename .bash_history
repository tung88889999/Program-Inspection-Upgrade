#!/bin/bash
# Real APK build process using Buildozer
echo "Updating system and installing dependencies..."
sudo apt update
sudo apt install -y python3-pip build-essential git python3 python3-dev     ffmpeg libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev     libportmidi-dev libswscale-dev libavformat-dev libavcodec-dev zlib1g-dev     cython libgstreamer1.0-dev gstreamer1.0-plugins-base gstreamer1.0-plugins-good
echo "Installing Buildozer..."
pip install --upgrade buildozer
echo "Initializing Buildozer project..."
if [ ! -f "buildozer.spec" ]; then     buildozer init;     echo "Buildozer spec file created. Please configure buildozer.spec before proceeding.";     exit 1; fi
