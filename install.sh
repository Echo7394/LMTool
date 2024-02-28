#!/bin/bash

# Directory where lmtool.py is located
SCRIPT_DIR="$(pwd)"

# Create a desktop launcher file
echo "[Desktop Entry]
Type=Application
Name=LMTool
Exec=sudo python3 \"$SCRIPT_DIR/lmtool.py\"
Icon=linuxmint-logo-leaf-symbolic
Terminal=true" > ~/Desktop/lmtool_launcher.desktop

# Change permissions to make it executable
chmod +x ~/Desktop/lmtool_launcher.desktop

echo "Install complete. Launcher created on the desktop."

