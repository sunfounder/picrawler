from .openai_helper import OpenAiHelper
from .keys import OPENAI_API_KEY, OPENAI_ASSISTANT_ID
from .preset_actions import *
from ..utils.utils import *
import threading  # Add this import for threading.Lock()
import os
import json  # Add json module for handling preset messages
import datetime  # Add datetime for time-based operations

# Suppress ALSA warnings
# Redirect stderr to /dev/null to suppress ALSA warnings
os.environ["ALSA_CARD"] = "Generic"
# This environment variable silences the ALSA error messages
os.environ["PYTHONWARNINGS"] = "ignore:ALSA lib"

# Initialize global variables
running = True
action_lock = threading.Lock()
action_status = "standby"  # Can be "standby", "actions", "think"
actions_to_be_done = []  # List to store actions that need to be performed
spider = None  # Initialize as None, will be set in init_robot
speech_lock = threading.Lock()
speech_loaded = False
tts_file = None
speech_is_playing = False  # Global variable to track speech status
has_greeted = False  # Track if initial greeting has been sent
audio_output = None  # Define global audio_output variable

# Default greeting and goodbye messages
DEFAULT_GREETING = {
    "actions": ["greeting", "wave_hand", "excited"],
    "answer": "Hello! I'm Arachne, your spider robot companion! I'm excited to talk with you and explore the world together. What would you like to do today?",
}

DEFAULT_GOODBYE = {
    "actions": ["sit", "wave_hand"],
    "answer": "Goodbye! It was nice spending time with you. I'll be here waiting when you want to chat again. Have a great day!",
}

# Paths for prerecorded messages
VOICE_PRESETS_DIR = "voice_presets"
GREETINGS_DIR = os.path.join(VOICE_PRESETS_DIR, "greetings")
GOODBYES_DIR = os.path.join(VOICE_PRESETS_DIR, "goodbyes")
RESPONSES_DIR = os.path.join(VOICE_PRESETS_DIR, "responses")


# Function to manage prerecorded voice messages
def ensure_voice_presets_exist():
    """Creates default voice presets if they don't exist"""
    global openai_helper

    print("Checking voice presets...")

    # Create directories if they don't exist
    for directory in [VOICE_PRESETS_DIR, GREETINGS_DIR, GOODBYES_DIR, RESPONSES_DIR]:
        if not os.path.exists(directory):
            try:
                os.makedirs(directory)
                print(f"Created directory: {directory}")
            except Exception as e:
                print(f"Error creating directory {directory}: {e}")

    # Force regeneration of all audio files that are invalid
    force_regenerate = True

    # Function to verify a preset is valid
    def verify_preset(preset_name, directory):
        meta_path = os.path.join(directory, f"{preset_name}.json")
        audio_path = os.path.join(directory, f"{preset_name}.wav")

        if not os.path.exists(meta_path) or not os.path.exists(audio_path):
            return False

        # Check JSON file integrity
        try:
            if os.path.getsize(meta_path) == 0:
                return False

            with open(meta_path, "r", encoding="utf-8") as f:
                json.load(f)

            # Verify audio file has proper WAV headers
            if force_regenerate:
                with open(audio_path, "rb") as f:
                    header = f.read(4)
                    if header != b"RIFF":
                        # Invalid WAV file
                        print(f"Invalid WAV file: {audio_path} - Regenerating")
                        return False

            return True
        except:
            return False

    # Generate default greetings if they don't exist
    greetings = [
        {
            "name": "morning_greeting",
            "text": "Dzień dobry! Jestem Arachne, twój przyjaciel robot pająk. Co będziemy dzisiaj robić?",
            "actions": ["greeting", "wave_hand", "excited"],
        },
        {
            "name": "afternoon_greeting",
            "text": "Witaj! Cieszę się, że mogę Cię zobaczyć! Jestem Arachne, twój pomocny robot pająk. Czym mogę Ci dzisiaj pomóc?",
            "actions": ["greeting", "wave_hand", "nod"],
        },
        {
            "name": "evening_greeting",
            "text": "Dobry wieczór! Jestem Arachne, twój robot pająk. Co planujesz robić dziś wieczorem?",
            "actions": ["greeting", "wave_hand", "look_around"],
        },
    ]

    # Also add a standard greeting as a fallback
    greetings.append(
        {
            "name": "standard_greeting",
            "text": "Witaj! Jestem Arachne, twój robot pająk. Jak mogę Ci pomóc dzisiaj?",
            "actions": ["greeting", "wave_hand"],
        }
    )

    for greeting in greetings:
        if not verify_preset(greeting["name"], GREETINGS_DIR):
            print(f"Creating or repairing greeting preset: {greeting['name']}")
            # Remove existing files if they exist but are invalid
            meta_path = os.path.join(GREETINGS_DIR, f"{greeting['name']}.json")
            audio_path = os.path.join(GREETINGS_DIR, f"{greeting['name']}.wav")

            try:
                if os.path.exists(meta_path):
                    os.remove(meta_path)
                if os.path.exists(audio_path):
                    os.remove(audio_path)
            except Exception as e:
                print(f"Error removing existing invalid files: {e}")

            # Now create the preset
            create_preset_message(
                greeting["text"], greeting["name"], GREETINGS_DIR, greeting["actions"]
            )
        else:
            print(f"Greeting preset '{greeting['name']}' is valid")

    # Generate default goodbyes if they don't exist
    goodbyes = [
        {
            "name": "standard_goodbye",
            "text": "Do widzenia! Dziękuję za rozmowę. Mam nadzieję, że wkrótce znów się zobaczymy!",
            "actions": ["wave_hand", "sit"],
        },
        {
            "name": "sleep_goodbye",
            "text": "Dobranoc! Idę odpocząć. Do zobaczenia następnym razem!",
            "actions": ["sit", "play_dead"],
        },
        {
            "name": "short_goodbye",
            "text": "Pa pa! Do zobaczenia wkrótce!",
            "actions": ["wave_hand", "excited", "sit"],
        },
    ]

    for goodbye in goodbyes:
        if not verify_preset(goodbye["name"], GOODBYES_DIR):
            print(f"Creating or repairing goodbye preset: {goodbye['name']}")
            # Remove existing files if they exist but are invalid
            meta_path = os.path.join(GOODBYES_DIR, f"{goodbye['name']}.json")
            audio_path = os.path.join(GOODBYES_DIR, f"{goodbye['name']}.wav")

            try:
                if os.path.exists(meta_path):
                    os.remove(meta_path)
                if os.path.exists(audio_path):
                    os.remove(audio_path)
            except Exception as e:
                print(f"Error removing existing invalid files: {e}")

            # Now create the preset
            create_preset_message(
                goodbye["text"], goodbye["name"], GOODBYES_DIR, goodbye["actions"]
            )
        else:
            print(f"Goodbye preset '{goodbye['name']}' is valid")

    # Generate default responses if they don't exist
    responses = [
        {
            "name": "error_response",
            "text": "Przepraszam, coś poszło nie tak. Spróbujmy ponownie.",
            "actions": ["shake_head", "look_down"],
        },
        {
            "name": "thinking_response",
            "text": "Hmm, muszę o tym pomyśleć...",
            "actions": ["look_up", "nod"],
        },
        {
            "name": "not_understood",
            "text": "Przepraszam, nie zrozumiałam. Czy możesz powtórzyć?",
            "actions": ["shake_head", "look_around"],
        },
    ]

    for response in responses:
        if not verify_preset(response["name"], RESPONSES_DIR):
            print(f"Creating or repairing response preset: {response['name']}")
            # Remove existing files if they exist but are invalid
            meta_path = os.path.join(RESPONSES_DIR, f"{response['name']}.json")
            audio_path = os.path.join(RESPONSES_DIR, f"{response['name']}.wav")

            try:
                if os.path.exists(meta_path):
                    os.remove(meta_path)
                if os.path.exists(audio_path):
                    os.remove(audio_path)
            except Exception as e:
                print(f"Error removing existing invalid files: {e}")

            # Now create the preset
            create_preset_message(
                response["text"], response["name"], RESPONSES_DIR, response["actions"]
            )
        else:
            print(f"Response preset '{response['name']}' is valid")

    print("Voice presets setup complete")


def create_preset_message(text, name, directory, actions=None):
    """Creates a preset voice message if it doesn't exist"""
    global openai_helper

    # Create metadata file path
    meta_path = os.path.join(directory, f"{name}.json")
    audio_path = os.path.join(directory, f"{name}.wav")

    # Check if the files exist and if the JSON file is valid
    json_valid = False
    if os.path.exists(meta_path) and os.path.getsize(meta_path) > 0:
        try:
            with open(meta_path, "r", encoding="utf-8") as f:
                json.load(f)  # Try to load the JSON to validate it
            json_valid = True
        except (json.JSONDecodeError, ValueError):
            print(
                f"JSON file for preset '{name}' exists but is invalid. Will recreate."
            )
            try:
                os.remove(meta_path)
            except:
                pass

    # Check if the audio file exists and is valid
    audio_valid = False
    if os.path.exists(audio_path) and os.path.getsize(audio_path) > 0:
        try:
            # Test if the audio file is valid by checking for RIFF header
            with open(audio_path, "rb") as f:
                header = f.read(4)
                if header == b"RIFF":
                    audio_valid = True
                else:
                    print(
                        f"Audio file for preset '{name}' exists but is invalid (no RIFF header). Will recreate."
                    )
                    try:
                        os.remove(audio_path)
                    except:
                        pass
        except Exception as e:
            print(f"Error checking audio file '{name}': {e}. Will recreate.")
            try:
                os.remove(audio_path)
            except:
                pass

    # Check if both files exist and are valid
    if json_valid and audio_valid:
        print(f"Preset '{name}' already exists and is valid")
        return (meta_path, audio_path)

    # Create the audio file if it doesn't exist or recreate if invalid
    try:
        print(f"Generating preset '{name}'...")

        # Generate the audio file
        if not os.path.exists(audio_path) or not audio_valid:
            try:
                # First try to generate using the OpenAI API
                success = openai_helper.text_to_speech(
                    text, audio_path, voice=TTS_VOICE
                )

                # Verify the generated file is valid
                if (
                    success
                    and os.path.exists(audio_path)
                    and os.path.getsize(audio_path) > 0
                ):
                    with open(audio_path, "rb") as f:
                        header = f.read(4)
                        if header != b"RIFF":
                            print(
                                f"Warning: Generated audio file for '{name}' is not a valid WAV file. Trying fallback method."
                            )
                            success = False

                if not success:
                    # Fallback: Generate a simple beep sound if TTS fails
                    print(f"Using fallback sound generation for '{name}'")
                    try:
                        import numpy as np
                        from scipy.io import wavfile

                        # Create a simple speaking-like sound
                        sample_rate = 22050
                        duration = 1.5  # 1.5 seconds
                        t = np.linspace(0, duration, int(sample_rate * duration))

                        # Create a complex tone that sounds like speech
                        frequencies = [400, 500, 600]
                        amplitudes = [0.3, 0.2, 0.1]
                        signal = np.zeros_like(t)

                        for freq, amp in zip(frequencies, amplitudes):
                            signal += amp * np.sin(2 * np.pi * freq * t)

                        # Add some variation to simulate speaking
                        envelope = np.ones_like(t)
                        envelope[: int(0.1 * len(t))] = np.linspace(
                            0, 1, int(0.1 * len(t))
                        )  # Fade in
                        envelope[-int(0.2 * len(t)) :] = np.linspace(
                            1, 0, int(0.2 * len(t))
                        )  # Fade out

                        # Apply envelope
                        signal = signal * envelope

                        # Add some "word breaks"
                        for i in range(3):
                            start = int((0.25 + i * 0.25) * len(t))
                            end = start + int(0.05 * len(t))
                            signal[start:end] *= 0.3

                        # Convert to 16-bit signed integers
                        audio_data = (signal * 32767).astype(np.int16)

                        # Save to WAV file
                        wavfile.write(audio_path, sample_rate, audio_data)

                        print(f"Created fallback audio file: {audio_path}")
                    except Exception as fallback_error:
                        print(f"Error creating fallback audio: {fallback_error}")
                        return (None, None)
                else:
                    print(f"Created audio file: {audio_path}")
            except Exception as tts_error:
                print(f"Error creating audio file: {tts_error}")
                return (None, None)

        # Create metadata
        metadata = {
            "text": text,
            "created": datetime.datetime.now().isoformat(),
            "actions": actions or [],
        }

        # Save metadata
        with open(meta_path, "w", encoding="utf-8") as f:
            json.dump(metadata, f, ensure_ascii=False, indent=2)

        print(f"Created preset metadata: {meta_path}")

        # Final verification
        if (
            os.path.exists(meta_path)
            and os.path.exists(audio_path)
            and os.path.getsize(audio_path) > 0
        ):
            return (meta_path, audio_path)
        else:
            print(f"Error: Failed to create complete preset for '{name}'")
            return (None, None)
    except Exception as e:
        print(f"Error creating preset '{name}': {e}")
        return (None, None)


def get_time_specific_greeting(time_of_day=None):
    """Get a time-appropriate greeting"""
    if time_of_day is None:
        current_hour = datetime.datetime.now().hour
        if 5 <= current_hour < 12:
            time_of_day = "morning"
        elif 12 <= current_hour < 18:
            time_of_day = "afternoon"
        else:
            time_of_day = "evening"

    greeting_name = f"{time_of_day}_greeting"
    greeting_path = os.path.join(GREETINGS_DIR, f"{greeting_name}.json")
    audio_path = os.path.join(GREETINGS_DIR, f"{greeting_name}.wav")

    # Check if the files exist and have content
    if (
        os.path.exists(greeting_path)
        and os.path.exists(audio_path)
        and os.path.getsize(greeting_path) > 0
    ):
        try:
            with open(greeting_path, "r", encoding="utf-8") as f:
                file_content = f.read().strip()
                if not file_content:  # Empty file
                    raise ValueError("Empty JSON file")

                metadata = json.loads(file_content)
            return {
                "text": metadata["text"],
                "audio_path": audio_path,
                "actions": metadata["actions"],
            }
        except (json.JSONDecodeError, ValueError) as e:
            print(f"Error reading greeting {greeting_name}: {e}")
            print(f"Recreating corrupt greeting: {greeting_name}")
            # The file exists but is corrupted/empty, delete it so we can recreate it
            try:
                os.remove(greeting_path)
            except:
                pass

            # Recreate the greeting
            if time_of_day == "morning":
                text = "Dzień dobry! Jestem Arachne, twój przyjaciel robot pająk. Co będziemy dzisiaj robić?"
                actions = ["greeting", "wave_hand", "excited"]
            elif time_of_day == "afternoon":
                text = "Witaj! Cieszę się, że mogę Cię zobaczyć! Jestem Arachne, twój pomocny robot pająk. Czym mogę Ci dzisiaj pomóc?"
                actions = ["greeting", "wave_hand", "nod"]
            else:  # evening
                text = "Dobry wieczór! Jestem Arachne, twój robot pająk. Co planujesz robić dziś wieczorem?"
                actions = ["greeting", "wave_hand", "look_around"]

            create_preset_message(text, greeting_name, GREETINGS_DIR, actions)

            # Try again with the new file
            try:
                with open(greeting_path, "r", encoding="utf-8") as f:
                    metadata = json.load(f)
                return {
                    "text": metadata["text"],
                    "audio_path": audio_path,
                    "actions": metadata["actions"],
                }
            except Exception as retry_error:
                print(f"Error reading recreated greeting: {retry_error}")

    # Fallback to default greeting
    fallback_greeting = os.path.join(GREETINGS_DIR, "standard_greeting.json")
    fallback_audio = os.path.join(GREETINGS_DIR, "standard_greeting.wav")

    if (
        os.path.exists(fallback_greeting)
        and os.path.exists(fallback_audio)
        and os.path.getsize(fallback_greeting) > 0
    ):
        try:
            with open(fallback_greeting, "r", encoding="utf-8") as f:
                file_content = f.read().strip()
                if not file_content:  # Empty file
                    raise ValueError("Empty JSON file")

                metadata = json.loads(file_content)
            return {
                "text": metadata["text"],
                "audio_path": fallback_audio,
                "actions": metadata["actions"],
            }
        except (json.JSONDecodeError, ValueError) as e:
            print(f"Error reading fallback greeting: {e}")

    # Ultimate fallback
    return {
        "text": "Witaj! Jestem Arachne, twój robot pająk!",
        "audio_path": None,
        "actions": ["greeting", "wave_hand"],
    }


def get_random_goodbye():
    """Get a random goodbye message"""
    goodbyes = []
    for file in os.listdir(GOODBYES_DIR):
        if file.endswith(".json"):
            goodbyes.append(os.path.splitext(file)[0])

    if not goodbyes:
        return {
            "text": "Do widzenia! Dziękuję za rozmowę.",
            "audio_path": None,
            "actions": ["wave_hand", "sit"],
        }

    goodbye_name = random.choice(goodbyes)
    goodbye_path = os.path.join(GOODBYES_DIR, f"{goodbye_name}.json")
    audio_path = os.path.join(GOODBYES_DIR, f"{goodbye_name}.wav")

    # Check if the files exist and have content
    if (
        os.path.exists(goodbye_path)
        and os.path.exists(audio_path)
        and os.path.getsize(goodbye_path) > 0
    ):
        try:
            with open(goodbye_path, "r", encoding="utf-8") as f:
                file_content = f.read().strip()
                if not file_content:  # Empty file
                    raise ValueError("Empty JSON file")

                metadata = json.loads(file_content)
            return {
                "text": metadata["text"],
                "audio_path": audio_path,
                "actions": metadata["actions"],
            }
        except (json.JSONDecodeError, ValueError) as e:
            print(f"Error reading goodbye {goodbye_name}: {e}")
            print(f"Recreating corrupt goodbye: {goodbye_name}")
            # The file exists but is corrupted/empty, delete it so we can recreate it
            try:
                os.remove(goodbye_path)
            except:
                pass

            # Recreate the goodbye based on its name
            if goodbye_name == "standard_goodbye":
                text = "Do widzenia! Dziękuję za rozmowę. Mam nadzieję, że wkrótce znów się zobaczymy!"
                actions = ["wave_hand", "sit"]
            elif goodbye_name == "sleep_goodbye":
                text = "Dobranoc! Idę odpocząć. Do zobaczenia następnym razem!"
                actions = ["sit", "play_dead"]
            elif goodbye_name == "short_goodbye":
                text = "Pa pa! Do zobaczenia wkrótce!"
                actions = ["wave_hand", "excited", "sit"]
            else:
                text = "Do widzenia! Dziękuję za rozmowę."
                actions = ["wave_hand", "sit"]

            create_preset_message(text, goodbye_name, GOODBYES_DIR, actions)

            # Try again with the new file
            try:
                with open(goodbye_path, "r", encoding="utf-8") as f:
                    metadata = json.load(f)
                return {
                    "text": metadata["text"],
                    "audio_path": audio_path,
                    "actions": metadata["actions"],
                }
            except Exception as retry_error:
                print(f"Error reading recreated goodbye: {retry_error}")

    # Fallback
    return {
        "text": "Do widzenia! Dziękuję za rozmowę.",
        "audio_path": None,
        "actions": ["wave_hand", "sit"],
    }


def play_preset_message(preset_type, name=None):
    """Play a preset message by type and name"""
    global LANGUAGE

    # Define language-specific fallback messages
    fallback_messages = {
        "greeting": {
            "en": "Hello! I'm PiCrawler, your friendly spider robot. Nice to meet you! How can I help you today?",
            "pl": "Witaj! Jestem PiCrawler, twój przyjazny robot-pająk. Miło mi cię poznać! Jak mogę ci dzisiaj pomóc?",
        },
        "goodbye": {
            "en": "Goodbye! It was nice talking to you. Have a great day!",
            "pl": "Do widzenia! Miło było z tobą rozmawiać. Miłego dnia!",
        },
        "error": {
            "en": "I'm sorry, I encountered an error. Please try again.",
            "pl": "Przepraszam, napotkałem błąd. Proszę spróbuj ponownie.",
        },
    }

    # Set language key for fallbacks
    lang_key = "pl" if LANGUAGE == "pl" else "en"

    if preset_type == "greeting":
        if name:
            path = os.path.join(GREETINGS_DIR, f"{name}.json")
            audio = os.path.join(GREETINGS_DIR, f"{name}.wav")
        else:
            greeting = get_time_specific_greeting()
            return play_message_with_actions(
                greeting["audio_path"], greeting["actions"]
            )
    elif preset_type == "goodbye":
        if name:
            path = os.path.join(GOODBYES_DIR, f"{name}.json")
            audio = os.path.join(GOODBYES_DIR, f"{name}.wav")
        else:
            goodbye = get_random_goodbye()
            return play_message_with_actions(goodbye["audio_path"], goodbye["actions"])
    elif preset_type == "response":
        if not name:
            name = "error_response"
        path = os.path.join(RESPONSES_DIR, f"{name}.json")
        audio = os.path.join(RESPONSES_DIR, f"{name}.wav")
    else:
        print(f"Unknown preset type: {preset_type}")
        return False

    if (
        name
        and os.path.exists(path)
        and os.path.exists(audio)
        and os.path.getsize(path) > 0
    ):
        try:
            # Safer JSON parsing with explicit error handling
            with open(path, "r", encoding="utf-8") as f:
                file_content = f.read().strip()
                if not file_content:  # Empty file
                    raise ValueError("Empty JSON file")

                metadata = json.loads(file_content)

            # Validate the required fields exist in the metadata
            if "actions" not in metadata:
                metadata["actions"] = []

            return play_message_with_actions(audio, metadata.get("actions", []))
        except (json.JSONDecodeError, ValueError) as e:
            print(f"Error playing preset {preset_type}/{name}: {e}")
            print(
                f"The preset file appears to be corrupted. Will recreate next time it's needed."
            )

            # Delete the corrupt JSON file so it will be recreated next time
            try:
                os.remove(path)
            except:
                pass

            # Attempt to play the audio file anyway, without actions
            return play_message_with_actions(audio, [])
        except Exception as e:
            print(f"Error playing preset {preset_type}/{name}: {e}")
            return False
    else:
        if name:
            print(f"Preset {preset_type}/{name} not found or is invalid")
        else:
            # Use TTS to generate a fallback message if preset not found
            if preset_type in fallback_messages:
                fallback_text = fallback_messages[preset_type][lang_key]
                print(f"Using fallback {preset_type} message: {fallback_text}")

                # Generate a temporary filename for the TTS
                _time = time.strftime("%y-%m-%d_%H-%M-%S", time.localtime())
                tts_file = f"./tts/fallback_{preset_type}_{_time}_{VOLUME_DB}dB.wav"

                # Try to generate TTS for the fallback
                try:
                    _tts_status = openai_helper.text_to_speech(
                        fallback_text, tts_file, TTS_VOICE, response_format="wav"
                    )

                    if _tts_status:
                        print(f"Generated fallback TTS: {tts_file}")
                        # Use appropriate actions for the message type
                        if preset_type == "greeting":
                            actions = ["greeting", "excited", "wave_hand"]
                        elif preset_type == "goodbye":
                            actions = ["wave_hand", "sit"]
                        else:
                            actions = ["shake_head"]

                        return play_message_with_actions(tts_file, actions)
                except Exception as tts_error:
                    print(f"Error generating fallback TTS: {tts_error}")

            return False


def play_message_with_actions(audio_path, actions):
    """
    Queue an audio message for playback and execute associated actions.
    The audio will actually be played by the speak_handler thread.

    Args:
        audio_path: Path to the audio file
        actions: List of action names to execute while playing

    Returns:
        bool: True if successfully queued, False otherwise
    """
    global actions_dict

    # Verify we have valid inputs
    if not audio_path:
        print("Warning: No audio path provided for message with actions")
        return False

    if not os.path.exists(audio_path):
        print(f"Warning: Audio file does not exist: {audio_path}")
        return False

    success = True

    # Process and queue the audio file for playback by the speak_handler thread
    try:
        if not process_audio_for_playback(audio_path):
            print(f"Error processing audio message: {audio_path}")
            success = False
    except Exception as e:
        print(f"Exception processing audio message: {e}")
        success = False

    # Execute actions if available
    if actions and isinstance(actions, list):
        try:
            for action_name in actions:
                if action_name in actions_dict:
                    print(f"Executing action from preset: {action_name}")
                    try:
                        # Execute the action
                        actions_dict[action_name](spider)
                    except Exception as action_error:
                        print(f"Error executing action '{action_name}': {action_error}")
                        success = False
                else:
                    print(f"Warning: Action '{action_name}' not found in actions_dict")
        except Exception as e:
            print(f"Error executing actions: {e}")
            success = False

    return success


# Override the stand function to handle the speed parameter properly
def stand(spider, speed=40):
    """Custom stand function that accepts a speed parameter"""
    spider.do_action("stand", speed=speed)


# Override the sit function to handle the speed parameter properly
def sit(spider, speed=40):
    """Custom sit function that accepts a speed parameter"""
    spider.do_action("sit", speed=speed)


"""
GPT-SPIDER - Voice-controlled spider robot with ChatGPT integration

Usage:
    sudo ~/my_venv/bin/python3 gpt_spider.py [options]
    
Options:
    --keyboard          Use keyboard input instead of voice
    --no-img            Disable camera functionality
    --debug             Show debugging information (audio levels, etc.)
    --threshold=XXX     Set initial microphone sensitivity (200-400 recommended)
                        Higher values require louder speech
                        Lower values are more sensitive but may trigger falsely
    --lang=XX           Set speech recognition language (en, zh, etc.)
                        Default auto-detects between multiple languages
    --pl                Set speech recognition language to Polish (pl)
    --low-threshold     Force very low microphone sensitivity (100) for testing
                        
Microphone Troubleshooting:
    - If it doesn't hear you: Try --threshold=250 (more sensitive)
    - If it hears things you didn't say: Try --threshold=350 (less sensitive)
    - If it detects wrong language: Try --lang=en (or your language code)
    - If nothing works: Try --low-threshold to test with extreme sensitivity
    - Use --debug to see audio levels while you speak
    
Controls:
    - Ctrl+C to exit
"""

import readline  # optimize keyboard input, only need to import

import speech_recognition as sr
import audioop

from picrawler import Picrawler
from robot_hat import Music, Pin

import time
import threading
import random
import signal  # Add signal module for handling keyboard interrupts

import sys
import subprocess
import datetime
import hashlib

# Define global variables for clean shutdown
interrupt_count = 0
MAX_INTERRUPTS = 2  # Force exit after this many interrupts
force_low_threshold = False  # Flag for forcing very low thresholds for testing
beep_enabled = True  # Flag to enable/disable beep sounds
SOUND_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "sounds")
PROMPT_SOUND = os.path.join(SOUND_DIR, "prompt.wav")
FINISH_SOUND = os.path.join(SOUND_DIR, "finish.wav")

# Define file paths for audio cues
START_SOUND = os.path.join("sounds", "listen_start.wav")
FINISH_SOUND = os.path.join("sounds", "listen_end.wav")
TIMEOUT_SOUND = os.path.join("sounds", "listen_again.wav")

# Create sounds directory if it doesn't exist
if not os.path.exists(SOUND_DIR):
    os.makedirs(SOUND_DIR)


# Create sound files if they don't exist
def create_beep_sound(filename, freq=1000, duration=0.2):
    if not os.path.exists(filename):
        try:
            import numpy as np
            from scipy.io import wavfile

            # Create a simple beep sound
            sample_rate = 44100
            t = np.linspace(0, duration, int(sample_rate * duration), False)
            wave = np.sin(2 * np.pi * freq * t) * 0.5

            # Convert to 16-bit PCM
            wave = (wave * 32767).astype(np.int16)

            # Save to file
            wavfile.write(filename, sample_rate, wave)
            print(f"Created sound file: {filename}")
            return True
        except Exception as e:
            print(f"Failed to create sound file: {e}")
            return False
    return True


# Create beep sounds if they don't exist
try:
    if not os.path.exists(PROMPT_SOUND):
        create_beep_sound(PROMPT_SOUND, freq=1200, duration=0.1)
    if not os.path.exists(FINISH_SOUND):
        create_beep_sound(FINISH_SOUND, freq=800, duration=0.1)
    if (
        not os.path.exists(START_SOUND)
        or not os.path.exists(FINISH_SOUND)
        or not os.path.exists(TIMEOUT_SOUND)
    ):
        try:
            import wave
            import array
            import math

            # Function to create a simple beep sound
            def create_beep_sound(filename, freq=1000, duration=0.2, volume=0.5):
                # Parameters
                sample_rate = 44100
                num_samples = int(duration * sample_rate)

                # Generate samples
                samples = array.array(
                    "h",
                    [
                        int(
                            32767.0
                            * volume
                            * math.sin(2 * math.pi * freq * i / sample_rate)
                        )
                        for i in range(num_samples)
                    ],
                )

                # Save to file
                with wave.open(filename, "w") as wave_file:
                    wave_file.setparams(
                        (1, 2, sample_rate, num_samples, "NONE", "not compressed")
                    )
                    wave_file.writeframes(samples.tobytes())

                print(f"Created sound file: {filename}")

            # Create different beep sounds
            if not os.path.exists(START_SOUND):
                create_beep_sound(
                    START_SOUND, freq=880, duration=0.1
                )  # Higher pitch for start
            if not os.path.exists(FINISH_SOUND):
                create_beep_sound(
                    FINISH_SOUND, freq=660, duration=0.1
                )  # Medium pitch for end
            if not os.path.exists(TIMEOUT_SOUND):
                create_beep_sound(
                    TIMEOUT_SOUND, freq=440, duration=0.2
                )  # Lower pitch for timeout
        except Exception as e:
            print(f"Could not create sound files: {e}")
            # Set beep_enabled to False if we couldn't create the sound files
            beep_enabled = False
except Exception as e:
    print(f"Failed to create sound files: {e}")
    beep_enabled = False


# Define a signal handler for SIGINT (Ctrl+C)
def signal_handler(sig, frame):
    """Handle graceful shutdown on CTRL+C"""
    global running, audio_output, openai_helper, LANGUAGE, interrupt_count

    # Increment interrupt count to allow forcing exit with multiple Ctrl+C
    interrupt_count += 1

    # Force exit if this is the second or third interrupt
    if interrupt_count >= MAX_INTERRUPTS:
        print(f"\nForced exit after {interrupt_count} interrupts. Exiting immediately.")
        os._exit(1)  # Force immediate exit

    print("\nShutting down gracefully...")

    # Set running to False to stop all threads
    running = False

    try:
        # Say goodbye before shutting down
        if spider is not None and "sit" in actions_dict:
            # Return robot to sit position
            sit(spider)
            print("Robot returned to sit position.")

            # Use a direct goodbye with no API calls to avoid getting stuck
            try:
                print("Playing goodbye message...")
                # Directly play a preset goodbye without making API calls
                play_preset_message("goodbye")
                # Give a small delay for audio to start playing
                time.sleep(0.5)
            except Exception as e:
                print(f"Error playing goodbye: {e}")
    except Exception as e:
        print(f"Error during shutdown: {e}")

    print("Cleaning up...")

    # Release picamera resources if initialized
    if "camera" in globals() and camera is not None:
        try:
            camera.stop()
            camera.close()
            print("Picamera2 resources released.")
        except:
            pass

    print("Shutdown complete.")
    # Use a small delay to allow messages to be printed, then force exit
    time.sleep(1)
    sys.exit(0)


# Register the signal handler
signal.signal(signal.SIGINT, signal_handler)

os.popen("pinctrl set 20 op dh")  # enable robot_hat speake switch
current_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_path)  # change working directory

# Ensure the tts directory exists
if not os.path.exists("./tts"):
    os.makedirs("./tts")
    print("Created 'tts' directory for storing voice files")

# Parse command line arguments
with_img = True
debug_mode = False
LANGUAGE = None  # Default language is None (auto-detect/English)
args = sys.argv[1:]
if "--keyboard" in args:
    input_mode = "keyboard"
else:
    input_mode = "voice"

if "--no-img" in args:
    with_img = False
else:
    with_img = True

if "--debug" in args:
    debug_mode = True
    print("Debug mode enabled - will show additional diagnostics")

if "--low-threshold" in args:
    force_low_threshold = True
    recognizer.energy_threshold = 100
    recognizer.minimum_energy_threshold = 100
    recognizer.dynamic_energy_threshold = False
    print(
        "WARNING: Forced very low threshold (100). This may cause false triggers but helps diagnose mic issues."
    )

# Check for energy threshold parameter
for arg in args:
    if arg.startswith("--threshold="):
        try:
            threshold_value = float(arg.split("=")[1])
            recognizer.energy_threshold = threshold_value
            print(f"Setting initial energy threshold to: {threshold_value}")
        except:
            print("Invalid threshold value. Using default.")

# Define available robot actions and their keywords for auto-detection
ROBOT_ACTIONS = {
    "dance": ["dance", "dancing", "twirl", "spinning", "bouncing", "wiggling"],
    "wave_hand": ["wave", "waving", "greeting", "hello", "hi"],
    "beckon": ["beckon", "come here", "beckoning", "calling over"],
    "shake_hand": ["shake hand", "handshake", "high five"],
    "fighting": ["fight", "fighting", "boxing", "punch", "karate"],
    "excited": ["excited", "excitement", "jumping", "jumps", "bouncing"],
    "nod": ["nod", "nodding", "yes", "agree", "agreeing"],
    "shake_head": ["shake head", "disagreeing", "no", "disagree"],
    "look_left": ["look left", "turning left", "glance left"],
    "look_right": ["look right", "turning right", "glance right"],
    "sit": ["sit", "sitting", "rest", "resting"],
    "stand": ["stand", "standing", "get up", "rise"],
}

# openai assistant init
# =================================================================
if len(OPENAI_API_KEY) < 10 or len(OPENAI_ASSISTANT_ID) < 10:
    raise ValueError(
        "\n\nInvalid OPENAI_API_KEY and OPENAI_ASSISTANT_ID in `keys.py`.\n"
    )

# Define API_KEY_SET to identify if the API key is valid and set
API_KEY_SET = True if len(OPENAI_API_KEY) >= 10 else False

# Log the API key status
if API_KEY_SET:
    print("OpenAI API key is properly configured.")
else:
    print(
        "WARNING: OpenAI API key is NOT properly configured. Speech recognition will use Google's API instead."
    )

openai_helper = OpenAiHelper(OPENAI_API_KEY, OPENAI_ASSISTANT_ID, "picrawler")

# Check for language parameter
for arg in args:
    if arg.startswith("--lang="):
        LANGUAGE = arg.split("=")[1]
        print(f"Setting speech recognition language to: {LANGUAGE}")
        # The following message is just for user feedback
        if LANGUAGE == "pl":
            print("Using Polish for both speech recognition and responses")
        else:
            print(f"Setting OpenAI to respond in language: {LANGUAGE}")

VOLUME_DB = 3  # tts voloume gain, preferably less than 5db

# select tts voice role, counld be "alloy, echo, fable, onyx, nova, and shimmer"
# https://platform.openai.com/docs/guides/text-to-speech/supported-languages
TTS_VOICE = "shimmer"

SOUND_EFFECT_ACTIONS = []

# car init
# =================================================================
try:
    time.sleep(1)
except Exception as e:
    raise RuntimeError(e)

# action_flow = ActionFlow(my_spider)


# Initialize the pygame mixer with better error handling and fallbacks
def init_pygame_mixer():
    """Initialize pygame mixer for audio output"""
    global audio_output

    print("Initializing audio output...")

    try:
        # Try pygame mixer first (most compatible)
        import pygame

        pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=2048)
        pygame.init()

        # Create a wrapper class for pygame.mixer.music
        class PygameMusicWrapper:
            def __init__(self):
                self.pygame = pygame

            def play(self, file_path):
                try:
                    pygame.mixer.music.load(file_path)
                    pygame.mixer.music.play()
                    return True
                except Exception as e:
                    print(f"Pygame mixer error: {e}")
                    return False

        audio_output = PygameMusicWrapper()
        print("Using pygame.mixer.music wrapper for audio output")
        return True

    except (ImportError, pygame.error) as e:
        print(f"Failed to initialize pygame mixer: {e}")

        try:
            # Try alternative minimal audio player
            class MinimalMusicPlayer:
                def __init__(self):
                    self.pygame = True  # Just a flag so we know it's this class

                def play(self, file_path):
                    try:
                        # Try using system command to play audio
                        subprocess.run(
                            ["aplay", file_path],
                            check=False,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                        )
                        return True
                    except Exception as e:
                        print(f"Minimal player error: {e}")
                        return False

            audio_output = MinimalMusicPlayer()
            print("Using MinimalMusicPlayer for audio output")
            return True

        except Exception as minimal_error:
            print(f"Failed to initialize minimal audio player: {minimal_error}")

            # Last resort: dummy player that does nothing
            class DummyMusic:
                def play(self, file_path):
                    print(f"[DUMMY] Would play {file_path}")
                    return True

            audio_output = DummyMusic()
            print("Warning: Using DummyMusic (no audio will play)")
            return True

    except Exception as e:
        print(f"Unexpected error initializing audio: {e}")
        audio_output = None
        return False


# Replace direct Music() initialization with our new function
try:
    # Initialize audio with fallback options
    audio_available = init_pygame_mixer()
    if not audio_available:
        print(
            "WARNING: Audio system couldn't be initialized. Speech output will be disabled."
        )

        # Create dummy music object to prevent crashes
        class DummyMusic:
            def play(self, file_path):
                print(f"[AUDIO DISABLED] Would play: {file_path}")

        music = DummyMusic()
except Exception as e:
    print(f"Error initializing audio: {e}")

    # Dummy music object as last resort
    class DummyMusic:
        def play(self, file_path):
            print(f"[AUDIO DISABLED] Would play: {file_path}")

    music = DummyMusic()

# Vilib start
# =================================================================
vilib_enabled = False  # Initialize to False by default
picamera2_enabled = False  # Track if we're using picamera2 instead

if with_img:
    try:
        # Set up libcamera tuning to fix SDN warning
        try:
            sdn_tuning_dir = "/etc/libcamera/tuning"
            sdn_tuning_file = os.path.join(sdn_tuning_dir, "rpi_sdn_fix.json")

            # Check if tuning file exists, if not create it
            if not os.path.exists(sdn_tuning_file):
                print("Creating SDN tuning fix...")
                if not os.path.exists(sdn_tuning_dir):
                    subprocess.run(["sudo", "mkdir", "-p", sdn_tuning_dir], check=False)

                # Define the tuning content
                sdn_tuning_content = """{
                    "version": 1.0,
                    "target": "rpi/pisp",
                    "algorithms": {
                        "rpi.denoise": {
                            "parameters": {
                                "use_sdn": true,
                                "sdn_mode": "auto"
                            }
                        },
                        "rpi.sdn": null
                    }"""

                # Create a temporary file and copy it to the system location
                with open("temp_sdn_fix.json", "w") as f:
                    f.write(sdn_tuning_content)

                subprocess.run(
                    ["sudo", "cp", "temp_sdn_fix.json", sdn_tuning_file], check=False
                )
                subprocess.run(["sudo", "chmod", "644", sdn_tuning_file], check=False)
                os.remove("temp_sdn_fix.json")
                print("SDN tuning fix created.")
            else:
                print("SDN tuning fix already exists.")
        except Exception as sdn_error:
            print(f"Warning: Failed to apply SDN tuning fix: {sdn_error}")

        # First check if vilib is installed
        import importlib.util

        vilib_spec = importlib.util.find_spec("vilib")

        if vilib_spec is None:
            print("Warning: vilib package not found. Trying picamera2 instead...")
            # Try to use picamera2 as fallback
            try:
                from picamera2 import Picamera2
                from picamera2.encoders import JpegEncoder
                from picamera2.outputs import FileOutput
                import io
                import cv2
                import numpy as np

                print("Successfully loaded picamera2. Setting up camera...")

                try:
                    # Check if we have the right version of libcamera
                    libcamera_check = subprocess.run(
                        ["ldconfig", "-p"],
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                        text=True,
                    )

                    if "libcamera.so.0.3" in libcamera_check.stdout:
                        print(
                            "Detected libcamera.so.0.3, which might have compatibility issues"
                        )
                        print("Trying to initialize camera anyway...")
                except Exception as lib_check_error:
                    print(f"Could not check libcamera version: {lib_check_error}")

                # Initialize the camera with better error handling
                try:
                    camera = Picamera2()
                    camera_config = camera.create_preview_configuration(
                        main={"size": (640, 480)}
                    )
                    camera.configure(camera_config)
                    camera.start()

                    # Create a function to capture images
                    def capture_still():
                        return camera.capture_array()

                    print("Camera initialized with picamera2 successfully")

                    # Add basic ROI visualization for picamera2
                    import cv2
                    import numpy as np
                    from threading import Thread

                    # Create a simple face detector using OpenCV's built-in cascade classifier
                    try:
                        face_cascade = cv2.CascadeClassifier(
                            cv2.data.haarcascades
                            + "haarcascade_frontalface_default.xml"
                        )
                        print("OpenCV face detection initialized for camera feed")

                        # Frame processing function to add ROI visualization
                        def process_frame_with_roi(frame):
                            """Add ROI visualization to the camera frame"""
                            # Make a copy of the frame to avoid modifying the original
                            processed = frame.copy()

                            # Convert to grayscale for face detection
                            gray = cv2.cvtColor(processed, cv2.COLOR_BGR2RGB)
                            gray = cv2.cvtColor(gray, cv2.COLOR_RGB2GRAY)

                            # Detect faces
                            faces = face_cascade.detectMultiScale(gray, 1.1, 4)

                            # Draw rectangles around faces
                            for x, y, w, h in faces:
                                cv2.rectangle(
                                    processed, (x, y), (x + w, y + h), (0, 255, 0), 2
                                )
                                # Add "Face" label
                                cv2.putText(
                                    processed,
                                    "Face",
                                    (x, y - 10),
                                    cv2.FONT_HERSHEY_SIMPLEX,
                                    0.5,
                                    (0, 255, 0),
                                    2,
                                )

                            # Return the processed frame with ROI visualization
                            return processed

                        # Override the flask_camera_server's frame processor
                        flask_camera_server.frame_processor = process_frame_with_roi
                        print("ROI visualization enabled for camera feed")
                    except Exception as roi_e:
                        print(
                            f"Warning: Could not initialize ROI visualization: {roi_e}"
                        )
                        print("Camera will show normal feed without ROI boxes")

                    # Try to start the camera web server
                    try:
                        import flask_camera_server

                        # Set the camera in the server module
                        flask_camera_server.set_camera(camera)

                        # Start the web server in a separate thread
                        web_server_thread = threading.Thread(
                            target=flask_camera_server.start_server,
                            kwargs={"port": 9001, "host": "0.0.0.0"},
                        )
                        web_server_thread.daemon = True
                        web_server_thread.start()

                        # Get hostname or IP for display
                        try:
                            import socket

                            hostname = socket.gethostname()
                            ip_addr = socket.gethostbyname(hostname)
                            print(f"Web display available at: http://{ip_addr}:9001/")
                        except:
                            print(
                                "Web display available at: http://raspberrypi.local:9001/"
                            )
                    except Exception as server_error:
                        print(f"Could not start camera web server: {server_error}")
                        print("Will continue without web display")
                        print("Make sure Flask is installed: pip install flask")

                    picamera2_enabled = True
                    with_img = True
                except Exception as cam_init_error:
                    print(f"Failed to initialize picamera2: {cam_init_error}")

                    # Detailed diagnostic information
                    if "undefined symbol" in str(cam_init_error):
                        print("This appears to be a library compatibility issue.")
                        print(
                            "Your system has mismatching versions of libcamera and/or libpisp."
                        )
                        print("Try running: sudo apt update && sudo apt upgrade")
                        print(
                            "Or reinstall picamera2: sudo apt reinstall python3-picamera2"
                        )

                    print("Camera functionality will be disabled.")
                    with_img = False
                    picamera2_enabled = False

            except ImportError as e:
                print(f"Failed to import picamera2: {e}")
                print("Camera functionality will be disabled.")
                with_img = False
        else:
            # Try to import the Vilib class specifically
            try:
                from vilib import Vilib
                import cv2

                Vilib.camera_start(vflip=False, hflip=False)
                Vilib.show_fps()
                Vilib.display(local=False, web=True)

                # Enable object detection with ROI boxes
                try:
                    print("Enabling face detection and object tracking...")
                    Vilib.face_detect_switch(True)  # Enable face detection with ROI
                    print("Face detection enabled")

                    # Also enable color detection for better visual feedback
                    print("Enabling color detection...")
                    color_to_detect = (
                        "red"  # Can be: red, orange, yellow, green, blue, purple
                    )
                    Vilib.color_detect(color_to_detect)
                    print(f"Color detection enabled for {color_to_detect}")

                    # Enable object detection status display
                    def object_detection_thread():
                        """Thread to periodically display object detection status"""
                        while vilib_enabled and running:
                            try:
                                # Show face detection status
                                if Vilib.detect_obj_parameter["human_n"] > 0:
                                    face_pos = (
                                        Vilib.detect_obj_parameter["human_x"],
                                        Vilib.detect_obj_parameter["human_y"],
                                    )
                                    face_size = (
                                        Vilib.detect_obj_parameter["human_w"],
                                        Vilib.detect_obj_parameter["human_h"],
                                    )
                                    if (
                                        debug
                                    ):  # Use the debug flag passed to the main function
                                        print(
                                            f"[Face detected] Position: {face_pos}, Size: {face_size}"
                                        )

                                # Show color detection status
                                if Vilib.detect_obj_parameter["color_n"] > 0:
                                    color_pos = (
                                        Vilib.detect_obj_parameter["color_x"],
                                        Vilib.detect_obj_parameter["color_y"],
                                    )
                                    color_size = (
                                        Vilib.detect_obj_parameter["color_w"],
                                        Vilib.detect_obj_parameter["color_h"],
                                    )
                                    if (
                                        debug
                                    ):  # Use the debug flag passed to the main function
                                        print(
                                            f"[Color detected] Position: {color_pos}, Size: {color_size}"
                                        )
                            except Exception as detect_e:
                                if (
                                    debug
                                ):  # Use the debug flag passed to the main function
                                    print(
                                        f"Error in object detection display: {detect_e}"
                                    )
                            time.sleep(1)  # Update every second

                    # Start object detection thread
                    detection_thread = threading.Thread(target=object_detection_thread)
                    detection_thread.daemon = True
                    detection_thread.start()

                except Exception as roi_e:
                    print(f"Warning: Unable to enable object detection: {roi_e}")

                while True:
                    if Vilib.flask_start:
                        break
                    time.sleep(0.01)

                time.sleep(0.5)
                print("\n")
                vilib_enabled = True
            except (ImportError, AttributeError) as e:
                print(f"Warning: Unable to import or use Vilib class: {e}")
                print("Trying to use picamera2 instead...")

                # Try to use picamera2 as fallback
                try:
                    from picamera2 import Picamera2
                    from picamera2.encoders import JpegEncoder
                    from picamera2.outputs import FileOutput
                    import io
                    import cv2
                    import numpy as np

                    print("Successfully loaded picamera2. Setting up camera...")

                    try:
                        # Check if we have the right version of libcamera
                        libcamera_check = subprocess.run(
                            ["ldconfig", "-p"],
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            text=True,
                        )

                        if "libcamera.so.0.3" in libcamera_check.stdout:
                            print(
                                "Detected libcamera.so.0.3, which might have compatibility issues"
                            )
                            print("Trying to initialize camera anyway...")
                    except Exception as lib_check_error:
                        print(f"Could not check libcamera version: {lib_check_error}")

                    # Initialize the camera with better error handling
                    try:
                        camera = Picamera2()
                        camera_config = camera.create_preview_configuration(
                            main={"size": (640, 480)}
                        )
                        camera.configure(camera_config)
                        camera.start()

                        # Create a function to capture images
                        def capture_still():
                            return camera.capture_array()

                        print("Camera initialized with picamera2 successfully")

                        # Try to start the camera web server
                        try:
                            import flask_camera_server

                            # Set the camera in the server module
                            flask_camera_server.set_camera(camera)

                            # Start the web server in a separate thread
                            web_server_thread = threading.Thread(
                                target=flask_camera_server.start_server,
                                kwargs={"port": 9001, "host": "0.0.0.0"},
                            )
                            web_server_thread.daemon = True
                            web_server_thread.start()

                            # Get hostname or IP for display
                            try:
                                import socket

                                hostname = socket.gethostname()
                                ip_addr = socket.gethostbyname(hostname)
                                print(
                                    f"Web display available at: http://{ip_addr}:9001/"
                                )
                            except:
                                print(
                                    "Web display available at: http://raspberrypi.local:9001/"
                                )
                        except Exception as server_error:
                            print(f"Could not start camera web server: {server_error}")
                            print("Will continue without web display")
                            print("Make sure Flask is installed: pip install flask")

                        picamera2_enabled = True
                        with_img = True
                    except Exception as cam_init_error:
                        print(f"Failed to initialize picamera2: {cam_init_error}")

                        # Detailed diagnostic information
                        if "undefined symbol" in str(cam_init_error):
                            print("This appears to be a library compatibility issue.")
                            print(
                                "Your system has mismatching versions of libcamera and/or libpisp."
                            )
                            print("Try running: sudo apt update && sudo apt upgrade")
                            print(
                                "Or reinstall picamera2: sudo apt reinstall python3-picamera2"
                            )

                        print("Camera functionality will be disabled.")
                        with_img = False
                        picamera2_enabled = False
                except ImportError as e:
                    print(f"Failed to import picamera2: {e}")
                    print("Camera functionality will be disabled.")
                    with_img = False
                    picamera2_enabled = False
    except Exception as e:
        print(f"Warning: Camera initialization failed: {e}")
        print("Continuing without camera functionality...")
        with_img = False
        vilib_enabled = False
        picamera2_enabled = False

# speech_recognition init
# =================================================================
recognizer = sr.Recognizer()
# Re-enable dynamic threshold but with minimum limits
recognizer.dynamic_energy_threshold = True
# Adjust thresholds based on successful detection parameters from logs
recognizer.energy_threshold = 80  # Set close to the value (79.1) that worked in logs
# More responsive parameters
recognizer.dynamic_energy_adjustment_damping = 0.1  # Even more responsive to changes
recognizer.dynamic_energy_ratio = 1.1  # Very sensitive (lower value)
recognizer.pause_threshold = 1.2  # Give more time between phrases
recognizer.phrase_threshold = 0.15  # More sensitive to detect shorter phrases
# Add a minimum threshold it won't drop below regardless of ambient noise
recognizer.minimum_energy_threshold = 75  # Set slightly below our target threshold

# Check available microphones
microphone_found = False
available_mics = []
selected_mic_index = 0  # Default to first microphone

try:
    # List all available microphones
    from speech_recognition import Microphone

    available_mics = Microphone.list_microphone_names()
    print("Available microphones:")
    for i, mic in enumerate(available_mics):
        print(f"  {i}: {mic}")
        # Look for the USB microphone
        if "USB" in mic:
            selected_mic_index = i
            print(f"Found USB microphone at index {i}")

    # Safety check for Raspberry Pi - sometimes indices are offset in ALSA
    if selected_mic_index == 1 and "USB" in available_mics[selected_mic_index]:
        # This is common on Raspberry Pi with USB mics
        print(f"Using microphone: {available_mics[selected_mic_index]}")
        microphone_found = True
    elif selected_mic_index >= 0 and selected_mic_index < len(available_mics):
        print(f"Using microphone: {available_mics[selected_mic_index]}")
        microphone_found = True
    else:
        print("No suitable microphones found. Switching to keyboard input mode.")
        input_mode = "keyboard"

    # On Linux/Raspberry Pi, sometimes we need to create a test recording to initialize the mic
    print("Testing microphone connection...")
    with sr.Microphone(device_index=selected_mic_index) as source:
        # Record a short sample to initialize the mic
        audio = recognizer.record(source, duration=0.1)
    print("Microphone test complete")

except Exception as e:
    print(f"Error detecting microphones: {e}")
    print("Switching to keyboard input mode.")
    input_mode = "keyboard"

# speak_handler
# =================================================================
speech_loaded = False
# speech_lock is already declared globally
tts_file = None
speech_is_playing = False  # Global variable to track speech status


def speak_handler():
    global running, speech_loaded, tts_file, speech_is_playing, audio_output

    print("Speak handler started with speech_is_playing=", speech_is_playing)

    while running:  # Only run while the program is running
        with speech_lock:
            _isloaded = speech_loaded
            _tts_file = tts_file  # Make a local copy inside the lock

        if _isloaded:
            if _tts_file and os.path.exists(_tts_file):
                print(f"Playing audio: {_tts_file}")
                with speech_lock:
                    speech_is_playing = True  # Mark that speech is now playing
                    print("speech_is_playing set to True")

                try:
                    # Use audio_output directly instead of music
                    if audio_output is not None and hasattr(audio_output, "play"):
                        audio_output.play(_tts_file)
                        print("Audio playback completed")
                    else:
                        print("Error: audio_output is not properly initialized")
                        # Try pygame directly as a last resort
                        try:
                            import pygame

                            pygame.mixer.music.load(_tts_file)
                            pygame.mixer.music.play()
                            # Wait for playback to complete
                            while pygame.mixer.music.get_busy():
                                time.sleep(0.1)
                            print("Audio playback completed via direct pygame call")
                        except Exception as pygame_error:
                            print(f"Direct pygame playback error: {pygame_error}")
                except Exception as e:
                    print(f"Error playing audio: {e}")

                # Ensure we reset the status flags after audio completes or fails
                with speech_lock:
                    speech_loaded = False
                    speech_is_playing = False  # Mark that speech has completed
                    print("Speech flags reset: loaded=False, playing=False")
            else:
                print(f"Warning: Audio file not found: {_tts_file}")
                # Reset flags even if file not found
                with speech_lock:
                    speech_loaded = False
                    speech_is_playing = False

        time.sleep(0.05)


speak_thread = threading.Thread(target=speak_handler)
speak_thread.daemon = True


# actions thread
# =================================================================
action_status = "standby"  # 'standby', 'think', 'actions', 'actions_done'
led_status = "standby"  # 'standby', 'think' or 'actions', 'actions_done'
last_action_status = "standby"
last_led_status = "standby"

LED_DOUBLE_BLINK_INTERVAL = 0.8  # seconds
LED_BLINK_INTERVAL = 0.1  # seconds

actions_to_be_done = []
action_lock = threading.Lock()


def action_handler():
    global running, action_lock, action_status, spider, actions_to_be_done, speech_lock, speech_loaded, tts_file, speech_is_playing

    # Initialize the status tracking variables
    last_led_status = None
    last_action_status = None
    led_status = "off"

    print("Action handler thread started")

    while running:
        # Get the current action status and actions safely
        current_actions = []
        current_status = "standby"

        with action_lock:
            current_status = action_status
            if action_status == "actions" and actions_to_be_done:
                current_actions = list(actions_to_be_done)  # Create a copy
                actions_to_be_done.clear()  # Clear the list so we don't repeat actions

        # Handle actions if needed
        if current_status == "actions" and current_actions:
            try:
                print(
                    f"Action handler processing {len(current_actions)} actions: {current_actions}"
                )

                # Get valid actions from the actions_dict in preset_actions.py
                valid_actions = list(actions_dict.keys())

                # Check for invalid actions
                invalid_actions = [a for a in current_actions if a not in valid_actions]
                if invalid_actions:
                    print(f"Ignoring invalid actions: {invalid_actions}")
                    print(f"Valid actions are: {valid_actions}")

                # Filter out invalid actions
                current_actions = [a for a in current_actions if a in valid_actions]

                # Check if robot needs to be standing before some actions
                actions_requiring_standing = [
                    "wave_hand",
                    "beckon",
                    "shake_hand",
                    "fighting",
                    "excited",
                    "warm_up",
                    "push_up",
                    "look_up",
                    "look_down",
                    "walk_forward",
                    "walk_backward",
                    "move_closer",
                    "explore",
                    "turn_left",
                    "turn_right",
                    "zigzag",
                    "circle",
                    "patrol",
                    "random_explore",
                    "curious",
                    "search_around",
                    "greeting",
                ]

                if any(a in actions_requiring_standing for a in current_actions):
                    try:
                        print("Making sure robot is standing...")
                        stand(spider, speed=40)
                        time.sleep(1)  # Give it time to stand
                    except Exception as e:
                        print(f"Error ensuring standing position: {e}")

                # Check speech status to avoid playing the audio twice
                should_wait_for_speech = False
                with speech_lock:
                    # If speech is already playing or loaded, wait for it instead of playing again
                    should_wait_for_speech = speech_is_playing or speech_loaded

                # Wait for any ongoing speech to finish before continuing with actions
                if should_wait_for_speech:
                    print("Waiting for speech to complete...")
                    wait_start = time.time()
                    while running:
                        with speech_lock:
                            if not speech_loaded and not speech_is_playing:
                                break
                        # Timeout after 30 seconds to prevent hanging
                        if time.time() - wait_start > 30:
                            print("Speech wait timeout, continuing with actions...")
                            break
                        time.sleep(0.1)
                    print("Speech has completed, continuing...")

                # Process each action
                for action in current_actions:
                    try:
                        # Make sure to use the global spider here
                        if action in actions_dict:
                            action_func = actions_dict[action]
                            if callable(action_func):
                                # Use the global spider
                                action_func(spider)
                                print(f"Successfully performed action: {action}")
                            else:
                                print(f"Error: Action {action} is not callable")
                        else:
                            print(f"Error: Action {action} not found in actions_dict")
                    except Exception as e:
                        print(f"Error processing action {action}: {e}")

                    # Small delay between actions
                    time.sleep(0.5)

                # Set the action status back to standby when done
                with action_lock:
                    action_status = "standby"
                    print("Action status set back to standby")

            except Exception as e:
                print(f"Error processing actions: {e}")
                with action_lock:
                    action_status = "standby"

        # Handle LED status changes if needed
        if led_status != last_led_status:
            # LED handling code would go here
            last_led_status = led_status

        # Sleep to prevent CPU hogging
        time.sleep(0.1)


action_thread = threading.Thread(target=action_handler)
action_thread.daemon = True


# main
# =================================================================
def main():
    global current_feeling, last_feeling
    global speech_loaded, speech_is_playing, speech_lock, tts_file
    global action_status, actions_to_be_done
    global running
    global input_mode  # Add global input_mode reference
    global LANGUAGE  # Add global LANGUAGE reference
    global with_img  # Add global with_img reference
    global openai_helper  # Add global reference to openai_helper

    # Set a timeout for waiting for speech to complete
    SPEECH_WAIT_TIMEOUT = 30  # seconds

    # Parse command line arguments
    LANGUAGE = None
    debug_mode = False
    threshold_value = 300  # Default threshold

    # Check for command line arguments
    for arg in sys.argv[1:]:
        if arg == "--keyboard":
            input_mode = "keyboard"
            print("Using keyboard input mode")
        elif arg == "--no-img":
            with_img = False
            print("Camera functionality disabled")
        elif arg == "--debug":
            debug_mode = True
            print("Debug mode enabled")
        elif arg == "--low-threshold":
            threshold_value = 100
            print(f"Using very low threshold: {threshold_value}")
        elif arg == "--pl":
            LANGUAGE = "pl"
            print("Using Polish language for speech recognition")
        elif arg.startswith("--lang="):
            LANGUAGE = arg.split("=")[1]
            print(f"Setting speech recognition language to: {LANGUAGE}")
            # The following message is just for user feedback
            if LANGUAGE == "pl":
                print("Using Polish for both speech recognition and responses")
        elif arg.startswith("--threshold="):
            try:
                threshold_value = int(arg.split("=")[1])
                print(f"Using custom threshold: {threshold_value}")
            except ValueError:
                print(f"Invalid threshold value: {arg.split('=')[1]}")
                print("Using default threshold: 300")
                threshold_value = 300

    # Set the language for the OpenAI helper if specified
    if LANGUAGE:
        openai_helper.set_language(LANGUAGE)
        if LANGUAGE == "pl":
            print("Setting OpenAI to respond in Polish")
        else:
            print(f"Setting OpenAI to respond in language: {LANGUAGE}")

    # Tracking consecutive listen failures for auto-adjusting sensitivity
    listen_failures = 0

    # Initialize variables for audio, conversation, etc.
    global running, action_lock, action_status, beep_enabled, gpio_enabled, spider, actions_to_be_done

    # Initialize action variables to default values
    with action_lock:
        action_status = "standby"
        actions_to_be_done = []

    # Use the global spider variable
    init_robot()
    if spider is None:
        print("ERROR: Failed to initialize robot. Exiting.")
        exit(1)

    # Set the spider to stand initially
    try:
        stand(spider, speed=40)  # Reduced speed from 60 to 40
        print("Robot standing successfully")
    except Exception as stand_e:
        print(f"Warning: Failed to set robot to standing position: {stand_e}")

    speak_thread.start()
    action_thread.start()

    # Initialize audio_output if not already initialized
    global audio_output

    if audio_output is None:
        # Call the init_pygame_mixer function to initialize audio
        init_pygame_mixer()

    # Setup voice presets
    ensure_voice_presets_exist()

    # After all initialization is complete
    global has_greeted

    if not has_greeted and not input_mode == "keyboard":
        try:
            # First play audio greeting from presets
            print("Playing initial greeting sound...")
            play_preset_message("greeting")

            # Then get a personalized greeting from the Assistant
            try:
                print("Getting personalized greeting from the Assistant...")

                # Use language-specific greeting prompt
                if LANGUAGE == "pl":
                    greeting_prompt = "Witaj! Właśnie się uruchomiłem. Proszę, powitaj użytkownika w języku polskim! Odpowiedź MUSI być w języku polskim."
                else:
                    greeting_prompt = "Hello! I just started up. Please provide a friendly greeting to start our conversation!"

                # Define fallback greetings upfront
                if LANGUAGE == "pl":
                    fallback_greeting = {
                        "actions": ["greeting", "excited", "wave_hand"],
                        "answer": "Witaj! Jestem PiCrawler, twój przyjazny robot-pająk. Miło mi cię poznać! Jak mogę ci dzisiaj pomóc?",
                    }
                else:
                    fallback_greeting = {
                        "actions": ["greeting", "excited", "wave_hand"],
                        "answer": "Hello! I'm PiCrawler, your friendly spider robot. Nice to meet you! How can I help you today?",
                    }

                # Try to get greeting from Assistant with retry limit
                max_retries = 3
                retry_count = 0
                greeting_response = None

                while retry_count < max_retries:
                    try:
                        print(
                            f"Attempt {retry_count + 1}/{max_retries} to get greeting"
                        )
                        greeting_response = openai_helper.dialogue(greeting_prompt)
                        # If we got here without exception, we have a response
                        break
                    except Exception as api_error:
                        print(f"Error getting greeting from API: {api_error}")
                        retry_count += 1
                        if retry_count < max_retries:
                            print(f"Retrying in 2 seconds...")
                            time.sleep(2)
                        else:
                            print("Maximum retries reached, using fallback greeting")

                # If we still don't have a greeting, use fallback
                if greeting_response is None:
                    print("Using fallback greeting due to API failures")
                    greeting_response = fallback_greeting

                # Check if the greeting is in the expected language
                if LANGUAGE == "pl" and greeting_response is not None:
                    # Quick check for common English phrases in the greeting
                    eng_phrases = ["hello", "i am", "i'm", "thank you", "nice to meet"]
                    greeting_text = greeting_response["answer"].lower()

                    # Look for Polish indicators
                    polish_words = ["witaj", "cześć", "dzień dobry", "jestem", "miło"]
                    has_polish = any(word in greeting_text for word in polish_words)

                    # Check for English only if no Polish detected
                    has_english = False
                    if not has_polish:
                        has_english = any(
                            phrase in greeting_text for phrase in eng_phrases
                        )

                    if has_english:
                        print(
                            "Greeting detected as English instead of Polish, using fallback"
                        )
                        greeting_response = fallback_greeting

                # Create TTS for the Assistant's greeting
                try:
                    print("Creating TTS for Assistant greeting...")
                    _time = time.strftime("%y-%m-%d_%H-%M-%S", time.localtime())
                    tts_file = f"./tts/{_time}_{VOLUME_DB}dB.wav"

                    _tts_status = openai_helper.text_to_speech(
                        greeting_response["answer"],
                        tts_file,
                        TTS_VOICE,
                        response_format="wav",
                    )

                    if _tts_status:
                        print(f"Assistant greeting TTS created: {tts_file}")

                        # Queue the speech
                        with speech_lock:
                            speech_loaded = True

                        # Execute greeting action
                        if greeting_response["actions"]:
                            for action_name in greeting_response["actions"]:
                                if action_name in actions_dict:
                                    try:
                                        print(
                                            f"Executing greeting action: {action_name}"
                                        )
                                        actions_dict[action_name](spider)
                                    except Exception as action_error:
                                        print(
                                            f"Error executing greeting action: {action_error}"
                                        )

                    else:
                        print("Failed to generate greeting TTS")
                        # Use preset greeting as fallback
                        play_preset_message("greeting")
                except Exception as tts_error:
                    print(f"Error generating greeting TTS: {tts_error}")
                    # Use preset greeting as fallback
                    play_preset_message("greeting")
            except Exception as assistant_error:
                print(f"Error getting greeting from Assistant: {assistant_error}")
                # Preset greeting already played, so continue

            has_greeted = True
            print("Initial greeting completed.")
            time.sleep(1)  # Give a moment after greeting
        except Exception as e:
            print(f"Error during initial greeting: {e}")

    while running:  # Check the running flag
        if input_mode == "voice":
            spider.do_action("stand", speed=40)  # Reduced speed from 60 to 40

            # listen
            # ----------------------------------------------------------------
            gray_print("listening ... (Press Ctrl+C to exit)")

            with action_lock:
                action_status = "standby"

            try:
                if not microphone_found:
                    print("No microphone detected. Switching to keyboard input.")
                    input_mode = "keyboard"
                    continue
            except Exception as e:
                print(f"Error checking microphone: {e}")
                input_mode = "keyboard"
                continue

            _stderr_back = (
                redirect_error_2_null()
            )  # ignore error print to ignore ALSA errors

            # Initialize the speech recognizer with a fixed threshold
            recognizer.energy_threshold = (
                80  # Fixed threshold based on known working value
            )
            recognizer.dynamic_energy_threshold = False  # Disable dynamic adjustment

            # Use a larger chunk size to prevent freezing
            try:
                with sr.Microphone(
                    device_index=selected_mic_index, chunk_size=8192
                ) as source:
                    cancel_redirect_error(_stderr_back)  # restore error print

                    try:
                        # We'll adjust for ambient noise only for diagnostics
                        print("Adjusting for ambient noise... Please be quiet.")
                        # We don't actually use this value, just measuring for logging
                        # We already set the fixed threshold above
                        ambient_energy = audioop.rms(
                            source.stream.read(source.CHUNK), source.SAMPLE_WIDTH
                        )
                        print(f"Ambient energy level: {ambient_energy:.1f}")
                        print(f"Using fixed threshold: 80")

                        print("Testing audio levels - speak to see levels...")

                        # Variable to store the audio outside the loop
                        captured_audio = None

                        # Counter for timeout messages
                        timeout_counter = 0

                        while running:
                            # Play the start sound to signal we're listening
                            if beep_enabled:
                                try:
                                    if os.path.exists(START_SOUND):
                                        os.system(f"aplay -q {START_SOUND} &")
                                        # Small pause to make sure the sound plays
                                        time.sleep(0.3)
                                    else:
                                        print("Warning: Start sound file not found")
                                except Exception as beep_e:
                                    print(f"Unable to play start sound: {beep_e}")

                            print("Speak now...")

                            # Increase the timeout for better chance to capture speech
                            try:
                                # Capture audio with a generous timeout
                                captured_audio = recognizer.listen(
                                    source, timeout=8.0, phrase_time_limit=15.0
                                )

                                # Once audio is captured, play a sound to indicate we're processing
                                if beep_enabled:
                                    try:
                                        if os.path.exists(FINISH_SOUND):
                                            os.system(f"aplay -q {FINISH_SOUND} &")
                                            # Small pause to make sure the sound plays
                                            time.sleep(0.3)
                                        else:
                                            print(
                                                "Warning: Finish sound file not found"
                                            )
                                    except Exception as beep_e:
                                        print(f"Unable to play finish sound: {beep_e}")

                                # Get language settings
                                recognize_language = LANGUAGE if LANGUAGE else None

                                # Process the audio
                                text = speech_to_text(
                                    captured_audio,
                                    language=recognize_language,
                                    debug=debug_mode,
                                )

                                if not text or text.strip() == "":
                                    print("No speech detected")
                                    timeout_counter += 1

                                    # Play timeout sound every few tries
                                    if timeout_counter % 2 == 0 and beep_enabled:
                                        try:
                                            if os.path.exists(TIMEOUT_SOUND):
                                                os.system(f"aplay -q {TIMEOUT_SOUND} &")
                                                # Small pause to make sure the sound plays
                                                time.sleep(0.3)
                                            else:
                                                print(
                                                    "Warning: Timeout sound file not found"
                                                )
                                        except Exception as beep_e:
                                            print(
                                                f"Unable to play timeout sound: {beep_e}"
                                            )

                                    continue

                                # We have valid speech, break out of the listening loop
                                break

                            except sr.WaitTimeoutError:
                                print("Listening timed out. No speech detected.")
                                timeout_counter += 1
                                # Reset the captured_audio variable to prevent errors during shutdown
                                captured_audio = None

                                # Play timeout sound every few tries
                                if timeout_counter % 2 == 0 and beep_enabled:
                                    try:
                                        if os.path.exists(TIMEOUT_SOUND):
                                            os.system(f"aplay -q {TIMEOUT_SOUND} &")
                                            # Small pause to make sure the sound plays
                                            time.sleep(0.3)
                                        else:
                                            print(
                                                "Warning: Timeout sound file not found"
                                            )
                                    except Exception as beep_e:
                                        print(f"Unable to play timeout sound: {beep_e}")

                                listen_failures += 1
                                continue
                            except Exception as e:
                                print(f"Error recognizing speech: {e}")
                                # Reset the captured_audio variable to prevent errors during shutdown
                                captured_audio = None
                                listen_failures += 1
                                timeout_counter += 1
                                continue

                    except sr.WaitTimeoutError:
                        print("Listening timed out. No speech detected.")
                        listen_failures += 1
                        continue

                    except Exception as inner_error:
                        print(f"Error during speech processing: {inner_error}")
                        print("Trying again...")
                        listen_failures += 1
                        continue

            except Exception as mic_error:
                print(f"Error during listening: {mic_error}")
                print("Switching to keyboard input mode due to microphone issues.")
                input_mode = "keyboard"
                continue

            # Reset failure counter on successful listen
            listen_failures = 0

            # Check if we should exit before proceeding
            if not running:
                break

            # chat-gpt
            # ----------------------------------------------------------------
            response = {}
            st = time.time()

            with action_lock:
                action_status = "think"

            if with_img:
                # Including image data with dialogue
                img_path = "./img_input.jpg"

                # Capture image based on which camera system is enabled
                if vilib_enabled:
                    # Using vilib camera
                    try:
                        cv2.imwrite(img_path, Vilib.img)
                        print("Image captured with vilib")
                        response = openai_helper.dialogue_with_img(text, img_path)
                    except Exception as e:
                        print(f"Error capturing image with vilib: {e}")
                        # Fallback to dialogue without image
                        response = openai_helper.dialogue(text)
                elif picamera2_enabled:
                    # Using picamera2
                    try:
                        # Capture frame and ensure it's properly saved
                        frame = capture_still()

                        # Convert to RGB format to ensure compatibility
                        if frame is not None:
                            # Save as JPEG with high quality
                            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                            cv2.imwrite(
                                img_path, frame_rgb, [int(cv2.IMWRITE_JPEG_QUALITY), 95]
                            )

                            # Verify the image file exists and has content
                            if (
                                os.path.exists(img_path)
                                and os.path.getsize(img_path) > 0
                            ):
                                print("Image captured with picamera2")

                                # Send the image to OpenAI with the dialogue
                                response = openai_helper.dialogue_with_img(
                                    text, img_path
                                )
                            else:
                                print(
                                    f"Error: Image file is empty or missing: {img_path}"
                                )
                                response = openai_helper.dialogue(text)
                        else:
                            print("Error: No frame captured from camera")
                            response = openai_helper.dialogue(text)
                    except Exception as e:
                        print(f"Error processing camera image: {e}")
                        response = openai_helper.dialogue(text)
                else:
                    # No camera is available, use text-only
                    print("No camera system available, using text-only dialogue")
                    response = openai_helper.dialogue(text)
            else:
                response = openai_helper.dialogue(text)

            gray_print(f"chat takes: {time.time() - st:.3f} s")

            # actions & TTS
            # ----------------------------------------------------------------
            try:
                # Initialize _sound_actions before using it
                _sound_actions = []

                if isinstance(response, dict):
                    if "actions" in response:
                        actions = list(response["actions"])
                    else:
                        actions = ["stop"]

                    if "answer" in response:
                        answer = response["answer"]
                    else:
                        answer = ""

                    if len(answer) > 0:
                        _actions = list.copy(actions)
                        for _action in _actions:
                            if _action in SOUND_EFFECT_ACTIONS:
                                _sound_actions.append(_action)
                                actions.remove(_action)

                        # Auto-detect actions from the response text
                        detected_actions = []
                        lower_answer = answer.lower()

                        # Check for action keywords in the response
                        for action_name, keywords in ROBOT_ACTIONS.items():
                            for keyword in keywords:
                                if keyword.lower() in lower_answer:
                                    detected_actions.append(action_name)
                                    print(f"Detected action from text: {action_name}")
                                    break  # Found one keyword for this action, no need to check others

                        # Add unique detected actions to the actions list
                        for action in detected_actions:
                            if action not in actions and action in actions_dict:
                                actions.append(action)
                                print(f"Added implied action: {action}")
                else:
                    response = str(response)
                    if len(response) > 0:
                        actions = []
                        answer = response

            except Exception as e:
                print(f"Error parsing response: {e}")
                actions = []
                answer = ""
                _sound_actions = []

            try:
                # ---- tts ----
                _tts_status = False
                if answer != "":
                    try:
                        st = time.time()
                        _time = time.strftime("%y-%m-%d_%H-%M-%S", time.localtime())
                        _tts_f = f"./tts/{_time}_raw.wav"
                        try:
                            _tts_status = openai_helper.text_to_speech(
                                answer, _tts_f, TTS_VOICE, response_format="wav"
                            )
                            if os.path.exists(_tts_f) and os.path.getsize(_tts_f) > 0:
                                _tts_status = True
                        except Exception as tts_e:
                            print(f"tts err: {tts_e}")
                            _tts_status = False

                        if _tts_status:
                            tts_file = f"./tts/{_time}_{VOLUME_DB}dB.wav"
                            try:
                                _tts_status = sox_volume(_tts_f, tts_file, VOLUME_DB)
                                print(f"TTS file created: {tts_file}")
                                with speech_lock:
                                    speech_loaded = True
                            except Exception as sox_e:
                                print(f"Error applying volume: {sox_e}")
                                # If volume adjustment fails, try to use the original file
                                tts_file = _tts_f
                                with speech_lock:
                                    speech_loaded = True
                        else:
                            print("Failed to generate TTS audio")
                        gray_print(f"tts takes: {time.time() - st:.3f} s")
                    except Exception as e:
                        print(f"TTS generation error: {e}")
                        _tts_status = False

                # ---- actions ----
                with action_lock:
                    actions_to_be_done = actions
                    gray_print(f"actions: {actions_to_be_done}")
                    action_status = "actions"

                # --- sound effects and voice ---
                try:
                    for _sound in _sound_actions:
                        try:
                            sounds_dict[_sound](music)
                        except Exception as e:
                            print(f"Sound effect error: {e}")
                except Exception as e:
                    print(f"Sound effects processing error: {e}")

                # --- If we have TTS output, queue it for playback by the speak_handler thread ---
                if tts_file and os.path.exists(tts_file):
                    # Only queue the speech, don't play it here
                    # The speak_handler thread will detect and play it
                    with speech_lock:
                        if not speech_is_playing:  # Only set if not currently playing
                            speech_loaded = True
                    # DO NOT play audio here, let the speak_handler thread do it
                    _tts_status = True
                else:
                    _tts_status = False

                # ---- wait speak done ----
                if _tts_status:
                    print("Waiting for speech to complete...")
                    wait_start = time.time()
                    last_speech_status_print = 0  # Track when we last printed status
                    while running:  # Exit if shutdown is requested
                        try:
                            # Check speech status
                            with speech_lock:
                                speech_status = (speech_loaded, speech_is_playing)

                            # Only print status every 2 seconds to reduce spam
                            current_time = time.time()
                            if (
                                debug_mode
                                and current_time - last_speech_status_print >= 2.0
                            ):
                                print(
                                    f"Speech status: loaded={speech_status[0]}, playing={speech_status[1]}"
                                )
                                last_speech_status_print = current_time

                            # Break out if speech is not loaded and not playing
                            if not speech_status[0] and not speech_status[1]:
                                print("Speech has completed, continuing...")
                                break

                            # Check for timeout
                            if current_time - wait_start > 30:  # 30-second timeout
                                print("Speech wait timeout, continuing...")
                                break

                            time.sleep(0.1)  # Small delay to prevent CPU thrashing
                        except Exception as e:
                            print(f"Error monitoring speech: {e}")
                            break

                    print("Speech completed. Waiting for user to speak...")

                # ---- wait actions done ----
                print("Waiting for actions to complete...")
                wait_start = time.time()
                last_status_print_time = 0  # Track when we last printed status
                while running:  # Exit if shutdown is requested
                    with action_lock:
                        current_status = action_status

                    # Only print status every 1 second to reduce spam
                    current_time = time.time()
                    if debug_mode and current_time - last_status_print_time >= 1.0:
                        print(f"Action status: {current_status}")
                        last_status_print_time = current_time

                    if current_status != "actions":
                        print("Actions completed, continuing...")
                        break

                    time.sleep(0.1)
                    # Don't wait more than 10 seconds
                    if time.time() - wait_start > 10:
                        print("Actions wait timeout, continuing...")
                        with action_lock:
                            action_status = "standby"
                        break

                # Give some time for the user to prepare their next input
                print("Ready for next interaction")
                time.sleep(2.0)  # Wait 2 seconds before asking for new input

                # Main loop audio feedback for speak now
                if beep_enabled:
                    try:
                        # Play a short beep to indicate ready to listen
                        if os.path.exists(START_SOUND):
                            os.system(f"aplay -q {START_SOUND} &")
                        else:
                            print("Warning: Start sound file not found")
                    except Exception as beep_e:
                        print(f"Unable to play start beep sound: {beep_e}")

                print("Speak now...")

                # Play a beep to indicate listening has stopped and processing is starting
                if beep_enabled:
                    try:
                        # Play a short beep to indicate listening has ended
                        if os.path.exists(FINISH_SOUND):
                            os.system(f"aplay -q {FINISH_SOUND} &")
                        else:
                            print("Warning: Finish sound file not found")
                    except Exception as beep_e:
                        print(f"Unable to play end beep sound: {beep_e}")

            except Exception as e:
                print(f"actions or TTS error: {e}")

        elif input_mode == "keyboard":
            spider.do_action("stand", speed=60)

            with action_lock:
                action_status = "standby"

            # Check if we should exit before proceeding
            if not running:
                break

            _result = (
                input(f'\033[1;30m{"input (Ctrl+C to exit): "}\033[0m')
                .encode(sys.stdin.encoding)
                .decode("utf-8")
            )

            if _result == False or _result == "":
                print()  # new line
                continue

        else:
            raise ValueError("Invalid input mode")


# Create ALSA configuration file to fix audio errors if it doesn't exist
def setup_alsa_config():
    """Setup ALSA configuration to fix common audio errors"""
    alsa_conf_path = "/etc/asound.conf"
    try:
        # Check if file already exists
        if not os.path.exists(alsa_conf_path) or os.path.getsize(alsa_conf_path) == 0:
            print("Creating ALSA configuration file to fix audio errors...")

            # Use a simpler configuration that's less likely to cause errors
            alsa_config = """# Simple ALSA configuration for PiCrawler
# This minimal configuration avoids the 'front is not a compound' errors

pcm.!default {
    type hw
    card 0
    device 0
}

ctl.!default {
    type hw
    card 0
}

# Basic software mixer
pcm.dmixer {
    type dmix
    ipc_key 1024
    slave {
        pcm "hw:0,0"
        period_time 0
        period_size 1024
        buffer_size 4096
        rate 48000
        channels 2
    }
}

# Simple default device using the mixer
pcm.!default {
    type plug
    slave.pcm "dmixer"
}
"""

            # Try to create the file with sudo
            try:
                # Using subprocess to run sudo command
                with open("temp_asound.conf", "w") as f:
                    f.write(alsa_config)

                # Copy to system location with sudo
                subprocess.run(["sudo", "cp", "temp_asound.conf", alsa_conf_path])
                subprocess.run(["sudo", "chmod", "644", alsa_conf_path])
                os.remove("temp_asound.conf")
                print(f"Created ALSA configuration file at {alsa_conf_path}")

                # Try to restart ALSA
                try:
                    subprocess.run(
                        ["sudo", "alsactl", "restore"], stderr=subprocess.PIPE
                    )
                    print("ALSA configuration reloaded")
                except Exception as alsa_e:
                    print(f"Note: Could not restart ALSA (not critical): {alsa_e}")

            except Exception as e:
                print(f"Could not create system-wide ALSA config: {e}")

                # Create user-specific config as fallback
                user_alsa_path = os.path.expanduser("~/.asoundrc")
                try:
                    with open(user_alsa_path, "w") as f:
                        f.write(alsa_config)
                    print(f"Created user ALSA configuration at {user_alsa_path}")
                except Exception as user_e:
                    print(f"Failed to create user ALSA config: {user_e}")
        else:
            print("ALSA configuration file already exists.")
    except Exception as e:
        print(f"Error setting up ALSA configuration: {e}")


# Ensure the Raspberry Pi audio module is loaded
def setup_audio_module():
    """Check and load the Raspberry Pi audio module if needed"""
    try:
        # Check if snd_bcm2835 module is loaded
        lsmod_result = subprocess.run(
            ["lsmod"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
        )

        if "snd_bcm2835" not in lsmod_result.stdout:
            print("Raspberry Pi audio module not loaded. Attempting to load it...")
            try:
                # Attempt to load the module
                subprocess.run(
                    ["sudo", "modprobe", "snd_bcm2835"],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                )
                print("Successfully loaded snd_bcm2835 audio module")

                # Verify it loaded
                lsmod_check = subprocess.run(
                    ["lsmod"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
                )
                if "snd_bcm2835" in lsmod_check.stdout:
                    print("Verified audio module is now loaded")
                else:
                    print(
                        "Audio module load command appeared to succeed but module is not showing as loaded"
                    )
            except Exception as e:
                print(f"Failed to load audio module: {e}")
        else:
            print("Raspberry Pi audio module (snd_bcm2835) is already loaded")
    except Exception as e:
        print(f"Error checking audio module: {e}")


# Call both functions early in the program
setup_audio_module()
setup_alsa_config()

# Try to check if GPIO is available using a more robust approach
try:
    # First try checking if GPIO is accessible directly through Pin
    try:
        led = Pin("LED")
        led_enabled = True
        print("LED initialized successfully")
    except Exception as pin_error:
        # If direct Pin initialization fails, check if the 'gpio' command exists
        try:
            # Check if gpio command exists
            gpio_exists = subprocess.run(
                ["which", "gpio"],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
            )

            if gpio_exists.returncode == 0:
                # gpio command exists, try readall
                gpio_check = subprocess.run(
                    ["gpio", "readall"],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True,
                )

                if "GPIO busy" in gpio_check.stderr:
                    print("Warning: GPIO is busy, LED functionality will be disabled")
                    led_enabled = False
                else:
                    led = Pin("LED")
                    led_enabled = True
            else:
                print(
                    "Warning: gpio command not found. LED functionality will be disabled."
                )
                led_enabled = False
        except Exception as gpio_error:
            print(f"Warning: Unable to check GPIO: {gpio_error}")
            led_enabled = False
except Exception as e:
    print(f"Warning: Unable to initialize LED: {e}")
    print("Continuing without LED functionality...")
    led_enabled = False


# Function to handle speech recognition
def speech_to_text(audio, language=None, debug=False):
    """
    Convert speech audio to text using the appropriate speech recognition service

    Args:
        audio: Audio data from the speech recognizer
        language: Optional language code or list of language codes
        debug: Whether to output debug information

    Returns:
        Recognized text or empty string if recognition failed
    """
    lang_str = language if language else "auto-detect"
    print(f"Using speech recognition language: {lang_str}")

    st = time.time()
    text = ""

    if API_KEY_SET:
        try:
            # Use the openai_helper.stt method which uses OpenAI's Whisper service
            print("Using OpenAI's Whisper service directly")

            # Use the language setting if specified - ensure it's properly formatted
            # Whisper requires languages in ISO-639-1 format (e.g. "en", "pl")
            if language:
                # If it's a string, use it directly
                if isinstance(language, str):
                    lang = language
                # If it's a list or tuple, use the first element
                elif isinstance(language, (list, tuple)) and len(language) > 0:
                    lang = language[0]
                else:
                    lang = "en"
            else:
                lang = "en"

            try:
                text = openai_helper.stt(audio, language=lang)
            except Exception as e:
                print(f"stt err:{e}")
                return ""

            if not text:
                print("Whisper could not understand audio or returned empty result")
        except Exception as e:
            print(f"Error during speech processing: {e}")
            return ""
    else:
        # Fallback to built-in speech recognition
        try:
            text = recognizer.recognize_google(audio, language=language)
        except sr.UnknownValueError:
            print("Could not understand audio")
            return ""
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            return ""

    if text:
        print(f"stt takes: {time.time() - st:.3f} s")
        text = text.strip()
        if debug:
            print(f"Processing input: '{text}'")
        return text

    return ""


# Initialize robot with servo zeroing
def init_robot():
    global spider  # Declare as global
    try:
        print("Initializing PiCrawler and zeroing servos...")
        spider = Picrawler()

        # Zero all servos at startup for proper calibration
        for i in range(12):
            print(f"Servo {i} set to zero")
            spider.servo_list[i].angle(10)  # Small movement to ensure servo responds
            time.sleep(0.1)
            spider.servo_list[i].angle(0)
            time.sleep(0.1)

        print("Servo zeroing completed")
        return spider
    except Exception as e:
        print(f"Error initializing robot: {e}")
        return None


def generate_greeting():
    """Generate a greeting message based on time of day"""
    import datetime

    current_hour = datetime.datetime.now().hour

    if 5 <= current_hour < 12:
        time_greeting = "Good morning"
    elif 12 <= current_hour < 18:
        time_greeting = "Good afternoon"
    else:
        time_greeting = "Good evening"

    greeting_messages = [
        f"{time_greeting}! I'm Arachne, your friendly spider robot. I just woke up and I'm ready to explore!",
        f"{time_greeting}! Arachne here! I've been waiting to chat with you. What shall we do today?",
        f"{time_greeting}! It's me, Arachne! *beep boop* I'm so excited to see what we'll discover today!",
    ]

    import random

    greeting_text = random.choice(greeting_messages)

    return {"actions": ["greeting", "wave_hand", "excited"], "answer": greeting_text}


def process_audio_for_playback(audio_file, volume_gain=3):
    """
    Process an audio file for playback with optional volume adjustment.
    This function ONLY processes the audio and queues it - it does NOT play it directly.
    The speak_handler thread will handle actual playback.

    Args:
        audio_file: Path to the audio file
        volume_gain: Volume gain in dB to apply

    Returns:
        bool: True if successfully processed and queued for playback, False otherwise
    """
    global speech_lock, tts_file, speech_loaded, audio_output

    try:
        # Initialize audio if needed
        if audio_output is None:
            try:
                print("Audio output not initialized. Initializing now...")
                init_pygame_mixer()

                # If audio_output is still None, create a fallback
                if audio_output is None:
                    print("Using fallback audio player")

                    class FallbackAudioPlayer:
                        def play(self, file_path):
                            print(f"Playing audio with fallback player: {file_path}")
                            # Try using system command to play audio
                            try:
                                subprocess.run(
                                    ["aplay", file_path],
                                    check=False,
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE,
                                )
                                return True
                            except Exception as e:
                                print(f"Fallback player error: {e}")
                                return False

                    audio_output = FallbackAudioPlayer()
            except Exception as e:
                print(f"Error initializing audio: {e}")
                return False

        # Check if audio file exists and is valid
        if not audio_file or not os.path.exists(audio_file):
            print(f"Warning: Audio file not found: {audio_file}")
            return False

        # Verify if the file is a valid WAV file
        try:
            with open(audio_file, "rb") as f:
                header = f.read(4)
                if header != b"RIFF":
                    print(f"Warning: Not a valid WAV file: {audio_file}")
                    return False
        except Exception as e:
            print(f"Error checking audio file header: {e}")
            return False

        # Apply volume gain if needed
        if volume_gain != 0:
            # Create processed filename based on volume level
            processed_file = audio_file.replace(".wav", f"_{volume_gain}dB.wav")

            # Skip processing if processed file already exists
            if not os.path.exists(processed_file):
                # Apply gain using sox
                try:
                    subprocess.run(
                        ["sox", audio_file, processed_file, "gain", str(volume_gain)],
                        check=True,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                    )
                    print(f"Applied {volume_gain}dB gain to {audio_file}")
                except Exception as e:
                    print(f"Error applying gain: {e}")
                    processed_file = audio_file  # Use original file as fallback

            audio_file = processed_file

        # Make sure we're not setting speech_loaded if speech is already playing
        # to avoid duplicate playback
        with speech_lock:
            # Don't queue new audio if the current one is still being played
            if not speech_is_playing:
                tts_file = audio_file
                speech_loaded = True
            else:
                print(
                    "Speech already in progress, waiting for it to complete before queueing new audio"
                )

        return True

    except Exception as e:
        print(f"Error in process_audio_for_playback: {e}")
        with speech_lock:
            speech_loaded = False
        return False


# Keep an alias for backward compatibility
process_and_play_audio = process_audio_for_playback


if __name__ == "__main__":
    try:
        # Use a safer way to check if we should switch to keyboard mode
        if not microphone_found:
            print("No microphone detected, starting in keyboard mode.")
            input_mode = "keyboard"

        main()
    except KeyboardInterrupt:
        print("\nKeyboard interrupt detected. Shutting down...")
    except Exception as e:
        print(f"\033[31mERROR: {e}\033[m")
        import traceback

        traceback.print_exc()  # Print the full stack trace for better debugging
    finally:
        # Ensure we set running to False for clean thread exit
        running = False
        print("Cleaning up...")
        # Allow threads time to exit
        time.sleep(0.5)
        if with_img:
            if vilib_enabled:
                try:
                    Vilib.camera_close()
                    print("Vilib camera resources released.")
                except Exception as e:
                    print(f"Error during vilib camera cleanup: {e}")
            elif picamera2_enabled:
                try:
                    camera.close()
                    print("Picamera2 resources released.")
                except Exception as e:
                    print(f"Error during picamera2 cleanup: {e}")
        try:
            if spider:
                spider.do_action("sit", speed=40)  # Reduced speed from 60 to 40
                print("Robot returned to sit position.")
            else:
                print("Robot instance not available for cleanup")
        except Exception as e:
            print(f"Error during robot cleanup: {e}")
        print("Shutdown complete.")
