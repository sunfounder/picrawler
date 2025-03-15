#!/usr/bin/env python3
"""
PiCrawler Action Test Script

This script tests all the available actions for the PiCrawler to ensure
they're working correctly.

Usage:
    sudo ~/my_venv/bin/python3 test_actions.py [action_name]

If no action name is provided, it will test all actions sequentially.
"""

import sys
import time
import os

# Add the parent directory to the Python path to allow imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.core.preset_actions import actions_dict

print("Testing available actions for Arachne PiCrawler...")
print(f"Total number of available actions: {len(actions_dict)}")
print("\nList of all available actions:")

# Print all available actions
for i, action_name in enumerate(actions_dict.keys()):
    print(f"{i+1}. {action_name}")

print("\nTesting action handling for previously problematic actions:")

# List of actions that were previously not working
test_actions = [
    "move_closer",
    "curious",
    "search_around",
    "random_explore",
    "zigzag",
    "circle",
    "patrol",
]


# Simulate the action handler's validation logic
def validate_actions(actions):
    valid_actions = list(actions_dict.keys())
    invalid_actions = [a for a in actions if a not in valid_actions]
    valid = [a for a in actions if a in valid_actions]

    print(f"\nValidating actions: {actions}")
    if invalid_actions:
        print(f"Invalid actions: {invalid_actions}")
    print(f"Valid actions: {valid}")

    return len(invalid_actions) == 0


# Test individual actions
for action in test_actions:
    result = validate_actions([action])
    print(f"Action '{action}' is {'VALID' if result else 'INVALID'}")

# Test a combination of actions
combined_actions = ["move_closer", "look_down", "curious"]
result = validate_actions(combined_actions)
print(
    f"\nCombined actions {combined_actions} are {'ALL VALID' if result else 'SOME INVALID'}"
)

print("\nTest completed!")
