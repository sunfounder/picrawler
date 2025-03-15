#!/usr/bin/env python3
"""
Enable Vision Capabilities for OpenAI Assistant

This script checks and updates the OpenAI assistant to ensure it has vision capabilities
by setting its model to GPT-4o or another vision-capable model.

Usage:
    python enable_vision.py
"""

import os
import sys
import json
import time

try:
    from openai import OpenAI
except ImportError:
    print("OpenAI package not found. Installing...")
    import subprocess

    subprocess.check_call([sys.executable, "-m", "pip", "install", "openai"])
    from openai import OpenAI

# Import API credentials
try:
    from ..core.keys import OPENAI_API_KEY, OPENAI_ASSISTANT_ID
except ImportError:
    print(
        "Error: Could not import API keys. Please check the keys.py file exists in the core directory."
    )
    sys.exit(1)

# Vision-capable models (in order of preference)
VISION_MODELS = [
    "gpt-4o",  # Best option - vision + high capability
    "gpt-4-vision",  # Good alternative
    "gpt-4-turbo",  # Another alternative that supports vision
]


def main():
    print("Checking OpenAI Assistant Vision Capabilities...")
    print(f"Assistant ID: {OPENAI_ASSISTANT_ID}")

    # Initialize the OpenAI client
    client = OpenAI(api_key=OPENAI_API_KEY)

    # Check current assistant configuration
    try:
        assistant = client.beta.assistants.retrieve(assistant_id=OPENAI_ASSISTANT_ID)

        print(f"\nCurrent assistant configuration:")
        print(f"- Name: {assistant.name}")
        print(f"- Model: {assistant.model}")

        # Check if the current model is vision-capable
        has_vision = any(model in assistant.model for model in VISION_MODELS)

        if has_vision:
            print(
                f"✅ Great! Assistant is already using vision-capable model: {assistant.model}"
            )
            print("No changes needed.")
            return

        # Ask for confirmation before updating
        print(
            f"\n⚠️ The current model '{assistant.model}' may not support vision capabilities."
        )
        change_model = input(
            "Would you like to update to GPT-4o for vision support? (y/n): "
        )

        if change_model.lower() != "y":
            print("No changes made to the assistant.")
            return

        # Get instructions from the existing assistant
        instructions = assistant.instructions

        # Update the assistant with a vision-capable model
        print(f"\nUpdating assistant to use {VISION_MODELS[0]}...")
        updated_assistant = client.beta.assistants.update(
            assistant_id=OPENAI_ASSISTANT_ID,
            model=VISION_MODELS[0],
            instructions=instructions,
        )

        print(f"✅ Assistant successfully updated!")
        print(f"- New model: {updated_assistant.model}")
        print("\nYour PiCrawler robot should now be able to see and analyze images!")

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
