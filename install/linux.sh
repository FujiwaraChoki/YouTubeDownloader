#!/bin/bash

# Install ffmpeg, needed for convertion
sudo apt-get install ffmpeg -y
# Install python requirements
pip3 install -r requirements.txt
# Update the system
sudo apt-get upgrade -y
sudo apt-get update -y
pyinstaller --onefile --noconsole ../src/gui.py
# Move the executable to the bin folder
mv dist/gui /bin

# Comfortably use the program
# Test
gui