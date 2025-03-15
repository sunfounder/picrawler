#!/usr/bin/env python3
"""
OpenAI Integration Test for PiCrawler

This script tests the OpenAI assistant integration to ensure
it returns actions in the correct format.

Usage:
    sudo ~/my_venv/bin/python3 test_openai.py
"""

import time
import json
import os
import sys

# Add the parent directory to the Python path to allow imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.core.openai_helper import OpenAiHelper
from src.core.keys import OPENAI_API_KEY, OPENAI_ASSISTANT_ID


def main():
    print("Initializing OpenAI helper...")
    helper = OpenAiHelper(OPENAI_API_KEY, OPENAI_ASSISTANT_ID, "test_assistant")

    # Test prompts to check if actions are included in responses
    test_prompts = [
        "Can you wave your hand?",
        "Please nod your head if you understand me",
        "Can you do a little dance?",
        "Show me how excited you are about being a robot!",
        "Can you look up at the ceiling?",
    ]

    print("\n===== BEGINNING TESTS =====")

    for i, prompt in enumerate(test_prompts):
        print(f"\nTEST {i+1}: '{prompt}'")
        try:
            response = helper.dialogue(prompt)

            # Check if response is in the right format
            print(f"Response type: {type(response)}")

            if isinstance(response, dict):
                print(f"Response keys: {response.keys()}")

                if "actions" in response:
                    actions = response["actions"]
                    print(f"Actions: {actions}")

                    if isinstance(actions, list) and len(actions) > 0:
                        print("✓ SUCCESS: Response contains actions array with items")
                    else:
                        print("✗ FAIL: Actions array is empty or not a list")
                else:
                    print("✗ FAIL: Response doesn't contain an 'actions' key")

                if "answer" in response:
                    print(f"Answer: {response['answer'][:100]}...")
                else:
                    print("✗ FAIL: Response doesn't contain an 'answer' key")
            else:
                print("✗ FAIL: Response is not a dictionary")
                print(f"Raw response: {response}")

            # Try to parse as JSON to see if it might work with proper extraction
            try:
                if isinstance(response, str):
                    json_response = json.loads(response)
                    print("INFO: Response could be parsed as JSON")
                    if "actions" in json_response:
                        print(f"JSON parsed actions: {json_response['actions']}")
            except:
                pass

        except Exception as e:
            print(f"ERROR: Exception occurred: {e}")

        print("-" * 40)
        time.sleep(2)  # Don't overload the API

    print("\n===== TESTS COMPLETE =====")


if __name__ == "__main__":
    main()
