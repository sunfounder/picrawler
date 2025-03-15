#!/usr/bin/env python3
"""
YouTube Video Player for Arachne PiCrawler

This script allows the robot to play YouTube videos with specified quality settings.
It uses yt-dlp (youtube-dl fork) to fetch video stream URLs and either mpv or omxplayer
to play the videos.

It can also add or update the 'play_youtube_video' function capability
to the Arachne PiCrawler's OpenAI Assistant.
"""

import subprocess
import os
import sys
import json
import time
import threading
import re
from urllib.parse import urlparse, parse_qs
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("youtube_player.log"), logging.StreamHandler()],
)
logger = logging.getLogger("youtube_player")

# Check if required libraries are installed
try:
    import yt_dlp
except ImportError:
    print("yt-dlp not found. Installing...")
    subprocess.run([sys.executable, "-m", "pip", "install", "yt-dlp"], check=True)
    import yt_dlp

# OpenAI integration imports (only imported when needed)
try:
    from openai import OpenAI
except ImportError:
    pass  # Will be handled when the update_assistant function is called

# Define player priority - try these players in order
PLAYERS = ["mpv", "omxplayer", "vlc"]

# Function definition for the YouTube player (for OpenAI Assistant)
YOUTUBE_FUNCTION = {
    "name": "play_youtube_video",
    "description": "Play a YouTube video on the robot's connected display",
    "parameters": {
        "type": "object",
        "properties": {
            "video_id": {
                "type": "string",
                "description": "The YouTube video ID or URL to play",
            },
            "quality": {
                "type": "string",
                "description": "The quality/resolution of the video",
                "enum": [
                    "144p",
                    "240p",
                    "360p",
                    "480p",
                    "720p",
                    "1080p",
                    "1440p",
                    "2160p",
                ],
            },
            "autoplay": {
                "type": "boolean",
                "description": "Whether to start playing the video automatically",
            },
        },
        "required": ["video_id", "quality", "autoplay"],
    },
}


def find_player():
    """Find an available video player from the PLAYERS list"""
    for player in PLAYERS:
        try:
            subprocess.run(["which", player], stdout=subprocess.PIPE, check=True)
            print(f"Using {player} for video playback")
            return player
        except subprocess.CalledProcessError:
            continue

    print(
        "No supported video player found. Please install one of: " + ", ".join(PLAYERS)
    )
    return None


def extract_video_id(video_id_or_url):
    """Extract YouTube video ID from either an ID or a full URL"""
    # If it's already just an ID (not a URL)
    if len(video_id_or_url) == 11 and re.match(r"^[A-Za-z0-9_-]{11}$", video_id_or_url):
        return video_id_or_url

    # Check if it's a YouTube URL
    url_patterns = [
        r"^https?://(?:www\.)?youtube\.com/watch\?v=([A-Za-z0-9_-]{11})",
        r"^https?://youtu\.be/([A-Za-z0-9_-]{11})",
        r"^https?://(?:www\.)?youtube\.com/embed/([A-Za-z0-9_-]{11})",
    ]

    for pattern in url_patterns:
        match = re.match(pattern, video_id_or_url)
        if match:
            return match.group(1)

    # If no patterns match, return the original string (it might be an ID)
    return video_id_or_url


def play_youtube_video(video_id, quality="medium", autoplay=True):
    """
    Play a YouTube video using mpv or vlc player.

    Args:
        video_id (str): YouTube video ID
        quality (str): Video quality (low, medium, high)
        autoplay (bool): Whether to autoplay the video

    Returns:
        bool: True if successful, False otherwise
    """
    try:
        logger.info(
            f"Playing YouTube video: {video_id}, quality: {quality}, autoplay: {autoplay}"
        )

        # Validate video_id
        if not video_id or not isinstance(video_id, str):
            logger.error(f"Invalid video_id: {video_id}")
            return False

        # Map quality to resolution
        quality_map = {"low": "240p", "medium": "480p", "high": "720p", "hd": "1080p"}

        # Get the resolution or use the provided quality directly
        resolution = quality_map.get(quality.lower(), quality)

        # Construct YouTube URL
        youtube_url = f"https://www.youtube.com/watch?v={video_id}"

        # Check for available players (mpv, vlc, or omxplayer)
        player_cmd = None

        # Try mpv first (best option for Raspberry Pi)
        try:
            subprocess.run(
                ["which", "mpv"],
                check=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )
            player_cmd = [
                "mpv",
                f"--ytdl-format=bestvideo[height<={resolution.rstrip('p')}]+bestaudio/best[height<={resolution.rstrip('p')}]",
                youtube_url,
                "--no-terminal",
            ]
            if not autoplay:
                player_cmd.append("--pause")

            logger.info("Using mpv player")
        except subprocess.CalledProcessError:
            logger.info("mpv not found")

        # Try VLC if mpv not available
        if player_cmd is None:
            try:
                subprocess.run(
                    ["which", "vlc"],
                    check=True,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                )
                player_cmd = ["vlc", youtube_url, "--no-video-title-show"]
                if not autoplay:
                    player_cmd.append("--pause")

                logger.info("Using vlc player")
            except subprocess.CalledProcessError:
                logger.info("vlc not found")

        # Try omxplayer as last resort (older Raspberry Pi)
        if player_cmd is None:
            try:
                subprocess.run(
                    ["which", "omxplayer"],
                    check=True,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                )
                player_cmd = ["omxplayer", youtube_url]
                logger.info("Using omxplayer")
            except subprocess.CalledProcessError:
                logger.info("omxplayer not found")

        # If no player found
        if player_cmd is None:
            logger.error("No suitable video player found")
            return False

        # Start the player in a separate process
        logger.info(f"Starting player with command: {' '.join(player_cmd)}")
        process = subprocess.Popen(
            player_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )

        # Don't wait for process to finish, return immediately
        logger.info(f"Player started with PID: {process.pid}")
        return True

    except Exception as e:
        logger.error(f"Error playing YouTube video: {e}")
        return False


def update_assistant(api_key=None, assistant_id=None):
    """
    Update the OpenAI assistant with the YouTube function capability

    Args:
        api_key (str, optional): OpenAI API key. If None, attempts to import from keys.py
        assistant_id (str, optional): OpenAI Assistant ID. If None, attempts to import from keys.py

    Returns:
        bool: True if the update was successful, False otherwise
    """
    try:
        # Try to import API keys if not provided
        if api_key is None or assistant_id is None:
            try:
                from ..core.keys import OPENAI_API_KEY, OPENAI_ASSISTANT_ID

                if api_key is None:
                    api_key = OPENAI_API_KEY
                if assistant_id is None:
                    assistant_id = OPENAI_ASSISTANT_ID
            except ImportError:
                print("Error: Could not import API keys from keys.py")
                return False

        if not api_key or not assistant_id:
            print(
                "Error: OPENAI_API_KEY and OPENAI_ASSISTANT_ID must be provided or set in keys.py"
            )
            return False

        # Check for OpenAI library
        try:
            from openai import OpenAI
        except ImportError:
            print("OpenAI library not found. Installing...")
            subprocess.run(
                [sys.executable, "-m", "pip", "install", "openai"], check=True
            )
            from openai import OpenAI

        # Initialize the OpenAI client
        client = OpenAI(api_key=api_key)

        # Retrieve the current assistant
        assistant = client.beta.assistants.retrieve(assistant_id)
        print(f"Found assistant: {assistant.name}")

        # Get existing tools
        existing_tools = assistant.tools

        # Check if the YouTube function already exists
        youtube_function_exists = False
        for tool in existing_tools:
            if tool.type == "function" and tool.function.name == "play_youtube_video":
                youtube_function_exists = True
                print("YouTube function already exists, updating it...")
                break

        # Update the assistant with the YouTube function
        updated_tools = [
            tool
            for tool in existing_tools
            if not (
                tool.type == "function" and tool.function.name == "play_youtube_video"
            )
        ]
        updated_tools.append({"type": "function", "function": YOUTUBE_FUNCTION})

        # Update the assistant
        updated_assistant = client.beta.assistants.update(
            assistant_id=assistant_id, tools=updated_tools
        )

        print(
            f"Successfully {'updated' if youtube_function_exists else 'added'} the YouTube function!"
        )
        print(f"Assistant now has {len(updated_assistant.tools)} tools")

        return True

    except Exception as e:
        print(f"Error updating assistant: {e}")
        return False


def play_from_command_line():
    """Handle command line arguments when script is run directly"""
    if len(sys.argv) < 2:
        print("Usage:")
        print(
            "  To play a video: python youtube_player.py play <video_id_or_url> [quality] [autoplay]"
        )
        print("  To update assistant: python youtube_player.py update")
        sys.exit(1)

    command = sys.argv[1]

    if command == "play":
        if len(sys.argv) < 3:
            print(
                "Usage: python youtube_player.py play <video_id_or_url> [quality] [autoplay]"
            )
            sys.exit(1)

        video_id = sys.argv[2]
        quality = sys.argv[3] if len(sys.argv) > 3 else "medium"
        autoplay = True
        if len(sys.argv) > 4:
            autoplay = sys.argv[4].lower() in ["true", "yes", "1", "y"]

        result = play_youtube_video(video_id, quality, autoplay)
        print(json.dumps(result, indent=2))

    elif command == "update":
        success = update_assistant()

        if success:
            print("\nSuccess! The Arachne PiCrawler can now play YouTube videos.")
            print("Example usage (you can say to the robot):")
            print("- 'Can you show me a video about spiders?'")
            print("- 'Play a relaxing music video in the background'")
            print("- 'Find and play a tutorial on how to build robots'")
        else:
            print("\nFailed to update the assistant. See error details above.")
            sys.exit(1)

    else:
        # For backwards compatibility
        video_id = sys.argv[1]
        quality = sys.argv[2] if len(sys.argv) > 2 else "medium"
        autoplay = True
        if len(sys.argv) > 3:
            autoplay = sys.argv[3].lower() in ["true", "yes", "1", "y"]

        result = play_youtube_video(video_id, quality, autoplay)
        print(json.dumps(result, indent=2))


if __name__ == "__main__":
    play_from_command_line()
