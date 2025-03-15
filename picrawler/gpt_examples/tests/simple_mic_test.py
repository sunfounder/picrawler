#!/usr/bin/env python3
"""
Simple Microphone Test Script for PiCrawler

This script tests the microphone using arecord directly,
which may avoid some of the PortAudio/PyAudio issues.

Usage:
    sudo ~/my_venv/bin/python3 simple_mic_test.py
"""

import os
import subprocess
import time


def test_mic_with_arecord():
    """Test microphone using arecord command"""
    print("Testing microphone with arecord...")

    # First, list all available audio capture devices
    print("\nListing audio capture devices:")
    os.system("arecord -l")

    # Record a short audio sample (3 seconds)
    print("\nRecording 3 seconds of audio to test.wav...")
    print("Please speak into the microphone now.")

    # The -D option specifies the device, hw:4,0 should be your USB mic based on the logs
    cmd = "arecord -D hw:4,0 -f cd -d 3 -r 44100 test.wav"

    try:
        subprocess.run(cmd, shell=True)
        print("Recording completed. Saved to test.wav")

        # Now play it back to verify
        print("\nPlaying back the recording...")
        os.system("aplay test.wav")

        print("\nIf you heard your voice, the microphone is working!")
        print("If not, let's try a different device...")

        # Try with default device
        print("\nTrying with default device...")
        subprocess.run("arecord -f cd -d 3 -r 44100 test2.wav", shell=True)
        print("Playing back recording from default device...")
        os.system("aplay test2.wav")

    except Exception as e:
        print(f"Error during recording: {e}")

    print("\nMicrophone test complete.")
    print("If none of the recordings worked, try:")
    print("1. Reconnecting your USB microphone")
    print("2. Checking if it's recognized with 'lsusb'")
    print("3. Checking if it's the right device with 'arecord -l'")


if __name__ == "__main__":
    test_mic_with_arecord()
