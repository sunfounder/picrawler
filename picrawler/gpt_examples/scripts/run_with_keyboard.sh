#!/bin/bash
# Run the PiCrawler in keyboard mode with debug output

echo "Running PiCrawler with keyboard input and debug output..."
echo "This bypasses the microphone and will let you type commands instead"
echo ""
echo "Press Ctrl+C to exit"
echo ""

# Run with keyboard mode and debug output
sudo ~/my_venv/bin/python3 gpt_spider.py --keyboard --debug 