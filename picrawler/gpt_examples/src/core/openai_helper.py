from openai import OpenAI
import time
import shutil
import os
import base64
import json
import sys

# Add import for YouTube player functionality
from ..utils.youtube_player import play_youtube_video as youtube_player


# utils
# =================================================================
def chat_print(label, message):
    width = shutil.get_terminal_size().columns
    msg_len = len(message)
    line_len = width - 27

    # --- normal print ---
    print(f"{time.time():.3f} {label:>6} >>> {message}")
    return

    # --- table mode ---
    if width < 38 or msg_len <= line_len:
        print(f"{time.time():.3f} {label:>6} >>> {message}")
    else:
        texts = []

        # words = message.split()
        # print(words)
        # current_line = ""
        # for word in words:
        #     if len(current_line) + len(word) + 1 <= line_len:
        #         current_line += word + " "
        #     else:
        #         texts.append(current_line)
        #         current_line = ""

        # if current_line:
        #     texts.append(current_line)

        for i in range(0, len(message), line_len):
            texts.append(message[i : i + line_len])

        for i, text in enumerate(texts):
            if i == 0:
                print(f"{time.time():.3f} {label:>6} >>> {text}")
            else:
                print(f'{"":>26} {text}')


# OpenAiHelper
# =================================================================
class OpenAiHelper:
    STT_OUT = "stt_output.wav"
    TTS_OUTPUT_FILE = "tts_output.mp3"
    TIMEOUT = 30  # seconds

    def __init__(self, api_key, assistant_id, assistant_name, timeout=TIMEOUT) -> None:
        self.api_key = api_key
        self.assistant_id = assistant_id
        self.assistant_name = assistant_name
        self.client = OpenAI(api_key=api_key, timeout=timeout)
        self.current_language = "en"  # Default language

        # Store API version-specific formats for later use
        self.api_version = self._detect_api_version()

        # Ensure assistant has vision capabilities
        try:
            # Retrieve the assistant to check its capabilities
            assistant = self.client.beta.assistants.retrieve(assistant_id)

            # Check if vision model is being used (gpt-4-vision or similar)
            if "gpt-4" in assistant.model:
                print(f"Using vision-capable model: {assistant.model}")
            else:
                # Update to use a vision-capable model if needed
                print(
                    f"Warning: Assistant model {assistant.model} may not have vision capabilities."
                )
                # We don't update automatically as it might change pricing/behavior
        except Exception as e:
            print(f"Error checking assistant capabilities: {e}")

        # Create an initial thread - will be recreated for each conversation
        self.create_new_thread()

    def _detect_api_version(self):
        """Detect which version of the OpenAI API is being used based on available methods"""
        try:
            # Try to make a simple API call to determine capabilities
            print("Detecting OpenAI API version and capabilities...")
            return "latest"  # Assume latest version - we'll handle different formats
        except Exception as e:
            print(f"Error detecting API version: {e}")
            return "unknown"

    def set_language(self, language_code):
        """Set the language for assistant responses"""
        if language_code:
            self.current_language = language_code
            print(f"OpenAI Helper language set to: {language_code}")

            # Use the appropriate language label for messages
            if language_code == "pl":
                print("Setting OpenAI to respond in Polish")
            elif language_code == "en":
                print("Setting OpenAI to respond in English")
            else:
                print(f"Setting OpenAI to respond in {language_code}")

            # Create a new thread with updated language settings
            self.create_new_thread()

    def get_mime_type(self, file_path):
        """Get the MIME type based on file extension"""
        extension = os.path.splitext(file_path)[1].lower()
        mime_types = {
            ".jpg": "image/jpeg",
            ".jpeg": "image/jpeg",
            ".png": "image/png",
            ".gif": "image/gif",
            ".bmp": "image/bmp",
            ".webp": "image/webp",
        }
        return mime_types.get(extension, "image/jpeg")  # Default to JPEG

    def create_new_thread(self):
        """Create a new thread for the conversation to avoid conflicts with active runs"""
        self.thread = self.client.beta.threads.create()
        self.thread_id = self.thread.id
        print(f"Created new conversation thread: {self.thread_id}")

        # Prepare additional instructions for the assistant
        instructions = []

        # If the language is set to something other than English, add language instructions
        if hasattr(self, "current_language") and self.current_language != "en":
            if self.current_language == "pl":
                language_instruction = """ZAWSZE ODPOWIADAJ W JĘZYKU POLSKIM. 
Twój język odpowiedzi to WYŁĄCZNIE POLSKI.
Nawet jeśli użytkownik pisze po angielsku, TY odpowiadasz TYLKO PO POLSKU.
Nie używaj angielskich słów ani zwrotów.
Format JSON musi zawierać odpowiedź w języku polskim w polu "answer".
Przykład: {"actions": ["greeting"], "answer": "Witaj! Jak mogę pomóc?"}"""
            else:
                language_instruction = f"Please respond in {self.current_language} language for all future interactions."
            instructions.append(language_instruction)

        # Add instructions about the robot's movement capabilities
        movement_instruction = """
When the user interacts with the robot, use a variety of physical actions to make the robot more lively and autonomous. Include one or more of these actions in your response:

Basic Movements:
- "stand" - stand upright
- "sit" - sit down
- "walk_forward" - to move the robot forward
- "walk_backward" - to move the robot backward
- "turn_left" - turn the robot left
- "turn_right" - turn the robot right
- "look_up" - look upward
- "look_down" - look downward

Complex Movements:
- "move_closer" - to approach what's in front of the robot
- "explore" - to perform a basic exploration pattern
- "zigzag" - to move in a zigzag pattern
- "circle" - to move in a circular pattern
- "patrol" - to patrol an area methodically
- "random_explore" - to explore the environment randomly

Expressive Behaviors:
- "wave_hand" - wave hello with one leg
- "beckon" - motion to come closer
- "shake_hand" - extend a leg for a handshake
- "fighting" - perform fighting stance
- "excited" - show excitement
- "play_dead" - play dead
- "nod" - nod in agreement
- "shake_head" - shake head in disagreement
- "warm_up" - stretch and warm up
- "push_up" - do push-ups

Combined Behaviors:
- "curious" - act curious by looking around and moving closer
- "search_around" - systematically search the area
- "idle_motion" - subtle movements to look more alive
- "greeting" - perform a friendly greeting sequence

These are ACTUAL commands the robot can execute, so include them in your "actions" list.
The robot is a physical spider robot that can move around and interact with its environment.
"""
        instructions.append(movement_instruction)

        # Add instructions about the JSON response format
        format_instruction = """
ALWAYS respond in valid JSON format with the following structure:
{
  "actions": ["action1", "action2", "action3"],
  "answer": "Your detailed response here"
}

The "actions" field MUST be an array of strings from the available actions listed earlier.
The "answer" field MUST contain your conversational response.

This JSON structure is MANDATORY for every response.
"""
        instructions.append(format_instruction)

        # Send all instructions to the thread
        if instructions:
            full_instruction = "\n\n".join(instructions)
            try:
                # Create the initial instructions message
                self.client.beta.threads.messages.create(
                    thread_id=self.thread_id, role="user", content=full_instruction
                )

                # Run the assistant to process the instruction
                run = self.client.beta.threads.runs.create(
                    thread_id=self.thread_id,
                    assistant_id=self.assistant_id,
                )

                # Poll for completion
                start_time = time.time()
                timeout = 30  # 30 seconds timeout
                print("Initializing assistant with instructions...")

                while time.time() - start_time < timeout:
                    run_status = self.client.beta.threads.runs.retrieve(
                        thread_id=self.thread_id, run_id=run.id
                    )
                    if run_status.status == "completed":
                        print("Assistant initialized successfully")
                        break
                    elif run_status.status in ["failed", "cancelled", "expired"]:
                        print(f"Assistant initialization {run_status.status}")
                        break
                    time.sleep(1)
            except Exception as e:
                print(f"Error setting up thread with instructions: {e}")

    def stt(self, audio, language="en"):
        try:
            import wave
            from io import BytesIO

            wav_data = BytesIO(audio.get_wav_data())
            wav_data.name = self.STT_OUT

            transcript = self.client.audio.transcriptions.create(
                model="whisper-1",
                file=wav_data,
                language=language,
                prompt="this is the conversation between me and a robot",
            )

            # file = "./stt_output.wav"
            # with wave.open(file, "wb") as wf:
            #     wf.write(audio.get_wav_data())

            # with open(file, 'rb') as f:
            #     transcript = client.audio.transcriptions.create(
            #         model="whisper-1",
            #         file=f
            #     )
            return transcript.text
        except Exception as e:
            print(f"stt err:{e}")
            return False

    def speech_recognition_stt(self, recognizer, audio):
        import speech_recognition as sr

        # # recognize speech using Sphinx
        # try:
        #     print("Sphinx thinks you said: " + r.recognize_sphinx(audio, language="en-US"))
        # except sr.UnknownValueError:
        #     print("Sphinx could not understand audio")
        # except sr.RequestError as e:
        #     print("Sphinx error; {0}".format(e))

        # recognize speech using whisper
        # try:
        #     print("Whisper thinks you said: " + r.recognize_whisper(audio, language="english"))
        # except sr.UnknownValueError:
        #     print("Whisper could not understand audio")
        # except sr.RequestError as e:
        #     print(f"Could not request results from Whisper; {e}")

        # recognize speech using Whisper API
        try:
            return recognizer.recognize_whisper_api(audio, api_key=self.api_key)
        except sr.RequestError as e:
            print(f"Could not request results from Whisper API; {e}")
            return False

    def dialogue(self, text, with_img=False, img_path=None, user_id="user"):
        """Add user's message to the thread and get a response"""
        # Add logging for debugging
        print(f"Processing request: '{text}'")

        try:
            # Check if there's an active run on the thread
            try:
                runs = self.client.beta.threads.runs.list(thread_id=self.thread_id)
                active_runs = [
                    run for run in runs.data if run.status in ["queued", "in_progress"]
                ]

                # If there's an active run, wait for it to complete
                if active_runs:
                    print(f"Waiting for {len(active_runs)} active runs to complete...")
                    for run in active_runs:
                        run_id = run.id
                        while True:
                            run = self.client.beta.threads.runs.retrieve(
                                thread_id=self.thread_id, run_id=run_id
                            )
                            if run.status not in ["queued", "in_progress"]:
                                print(
                                    f"Run {run_id} completed with status: {run.status}"
                                )
                                break
                            print(
                                f"Waiting for run {run_id}, current status: {run.status}"
                            )
                            time.sleep(1)
            except Exception as run_check_error:
                print(f"Error checking for active runs: {run_check_error}")
                # If there's an error checking runs, create a new thread to be safe
                self.create_new_thread()

            # Enhance the message with language instructions if needed
            enhanced_text = text
            if self.current_language and self.current_language.lower() != "english":
                if self.current_language == "pl":
                    enhanced_text += "\n\nOdpowiedz mi w języku polskim. To jest bardzo ważne, żebyś odpowiadał po polsku."
                else:
                    enhanced_text += f"\n\nPlease respond in {self.current_language} language. It is very important."

            # Create a message
            self.client.beta.threads.messages.create(
                thread_id=self.thread_id, role="user", content=enhanced_text
            )

            # Create a run
            run = self.client.beta.threads.runs.create(
                thread_id=self.thread_id,
                assistant_id=self.assistant_id,
            )

            # Wait for run to complete or require action
            while True:
                try:
                    run = self.client.beta.threads.runs.retrieve(
                        thread_id=self.thread_id, run_id=run.id
                    )

                    if run.status == "completed":
                        print("Run completed successfully")
                        break
                    elif run.status == "requires_action":
                        print("Run requires action: function calling")
                        # Handle tool calls if present
                        if (
                            run.required_action
                            and run.required_action.type == "submit_tool_outputs"
                        ):
                            print("Processing tool calls...")
                            tool_calls = (
                                run.required_action.submit_tool_outputs.tool_calls
                            )
                            tool_outputs = self.handle_tool_calls(
                                self.thread_id, run.id, tool_calls
                            )

                            # Submit the outputs back to the assistant
                            run = self.client.beta.threads.runs.submit_tool_outputs(
                                thread_id=self.thread_id,
                                run_id=run.id,
                                tool_outputs=tool_outputs,
                            )
                            print(
                                f"Submitted tool outputs, new run status: {run.status}"
                            )
                    elif run.status in ["failed", "cancelled", "expired"]:
                        print(f"Run ended with status: {run.status}")
                        if hasattr(run, "last_error"):
                            print(f"Error details: {run.last_error}")

                        # Return a fallback response
                        if self.current_language == "pl":
                            return {
                                "actions": ["shake_head"],
                                "answer": "Przepraszam, ale coś poszło nie tak. Spróbujmy ponownie.",
                            }
                        else:
                            return {
                                "actions": ["shake_head"],
                                "answer": "I'm sorry, but something went wrong. Let's try again.",
                            }

                    # Wait before checking status again
                    time.sleep(0.5)

                except Exception as status_error:
                    print(f"Error checking run status: {status_error}")
                    # In case of error, try to recreate thread and continue
                    self.create_new_thread()
                    if self.current_language == "pl":
                        return {
                            "actions": ["shake_head"],
                            "answer": "Przepraszam, napotkałem problem techniczny. Spróbujmy ponownie.",
                        }
                    else:
                        return {
                            "actions": ["shake_head"],
                            "answer": "Sorry, I encountered a technical problem. Let's try again.",
                        }

            # Retrieve messages
            try:
                messages = self.client.beta.threads.messages.list(
                    thread_id=self.thread_id, order="desc", limit=1
                )

                # Extract the assistant's response
                if len(messages.data) > 0:
                    latest_message = messages.data[0]
                    if latest_message.role == "assistant":
                        # Get the message content - checking for various content types
                        content_parts = []
                        for content in latest_message.content:
                            if content.type == "text":
                                content_parts.append(content.text.value)

                        # Join the content parts
                        response_text = " ".join(content_parts)

                        # Debug output
                        print(f"Raw response: {response_text[:100]}...")

                        # Try to parse JSON response
                        try:
                            json_response = json.loads(response_text)
                            # Verify language if needed
                            if (
                                self.current_language == "pl"
                                and "answer" in json_response
                            ):
                                # Check if the answer appears to be in English (more robust check)
                                # Use word boundaries to avoid matching substrings
                                eng_words = [
                                    "I am ",
                                    " am ",
                                    " the ",
                                    " is ",
                                    " are ",
                                    "Hello,",
                                    "Hello!",
                                    "Sorry,",
                                    "Sorry.",
                                ]

                                # Check if response starts with English phrases (case insensitive)
                                response_lower = json_response["answer"].lower()

                                # First check for common Polish words to avoid false positives
                                polish_words = [
                                    "witaj",
                                    "cześć",
                                    "dzień dobry",
                                    "przepraszam",
                                    "dziękuję",
                                ]
                                has_polish = any(
                                    word in response_lower for word in polish_words
                                )

                                # Only check for English if no Polish detected
                                is_english = False
                                if not has_polish:
                                    is_english = any(
                                        word.lower() in response_lower
                                        for word in eng_words
                                    )

                                if is_english:
                                    # Force a retry with stronger language instruction
                                    print(
                                        "Response detected as English instead of Polish, retrying..."
                                    )

                                    # Check if there's a retry_count in the text to limit retries
                                    retry_count = 1
                                    if "\n\nPROSZĘ ODPOWIADAJ" in text:
                                        # Count the number of retry instructions already in the text
                                        retry_count = text.count("PROSZĘ ODPOWIADAJ")

                                    # Limit to 3 retries to avoid infinite loops
                                    if retry_count >= 3:
                                        print(
                                            "Reached maximum retry attempts. Using response as-is."
                                        )
                                        return json_response

                                    # Otherwise, try again with stronger instruction
                                    return self.dialogue(
                                        text
                                        + "\n\nPROSZĘ ODPOWIADAJ TYLKO W JĘZYKU POLSKIM. NIE UŻYWAJ ANGIELSKIEGO.",
                                        with_img,
                                        img_path,
                                        user_id,
                                    )
                            return json_response
                        except json.JSONDecodeError:
                            # If not JSON, look for JSON-like content in the text
                            import re

                            json_pattern = r"\{.*\}"
                            matches = re.findall(json_pattern, response_text, re.DOTALL)

                            if matches:
                                for potential_json in matches:
                                    try:
                                        return json.loads(potential_json)
                                    except:
                                        continue

                            # If no valid JSON found, return a formatted response
                            return {"actions": ["nod"], "answer": response_text}

                # If no valid response found
                if self.current_language == "pl":
                    return {
                        "actions": [],
                        "answer": "Przepraszam, nie udało mi się wygenerować odpowiedzi.",
                    }
                else:
                    return {
                        "actions": [],
                        "answer": "I'm sorry, I couldn't generate a response.",
                    }

            except Exception as message_error:
                print(f"Error retrieving messages: {message_error}")
                if self.current_language == "pl":
                    return {
                        "actions": ["shake_head"],
                        "answer": "Przepraszam, wystąpił problem z komunikacją.",
                    }
                else:
                    return {
                        "actions": ["shake_head"],
                        "answer": "Sorry, there was a communication problem.",
                    }

        except Exception as e:
            print(f"Error in dialogue method: {e}")
            if self.current_language == "pl":
                return {
                    "actions": ["shake_head"],
                    "answer": f"Przepraszam, wystąpił błąd: {str(e)}",
                }
            else:
                return {
                    "actions": ["shake_head"],
                    "answer": f"Sorry, an error occurred: {str(e)}",
                }

    def dialogue_with_img(
        self,
        prompt,
        img_path,
        thread_id=None,
        add_language_instruction=True,
        fallback_response=None,
    ):
        """
        Process an image using the Assistant API with modern attachment methods.

        :param prompt: The prompt to send
        :param img_path: Path to the image
        :param thread_id: Thread ID to use (or None to use the instance's thread)
        :param add_language_instruction: Whether to add language instructions
        :param fallback_response: A fallback response to return if processing fails
        :return: The response from the AI
        """
        try:
            print(f"Processing request with image: {img_path}")

            # Add wait_for_run_completion method if it doesn't exist
            if not hasattr(self, "wait_for_run_completion"):

                def wait_for_run_completion(thread_id, run_id, timeout=30):
                    """Temporary inline implementation of wait_for_run_completion"""
                    start_time = time.time()
                    while time.time() - start_time < timeout:
                        try:
                            run = self.client.beta.threads.runs.retrieve(
                                thread_id=thread_id, run_id=run_id
                            )
                            if run.status == "completed":
                                print(f"Run {run_id} completed successfully")
                                return True
                            elif run.status in ["failed", "cancelled", "expired"]:
                                print(f"Run {run_id} ended with status: {run.status}")
                                return False
                            time.sleep(1)
                        except Exception as e:
                            print(f"Error checking run status: {e}")
                            return False
                    print(f"Run {run_id} timed out after {timeout} seconds")
                    return False

                # Dynamically add the method to the instance
                self.wait_for_run_completion = wait_for_run_completion

            # Add get_latest_message method if it doesn't exist
            if not hasattr(self, "get_latest_message"):

                def get_latest_message(thread_id):
                    """Temporary inline implementation of get_latest_message"""
                    try:
                        messages = self.client.beta.threads.messages.list(
                            thread_id=thread_id, order="desc", limit=1
                        )
                        if messages.data and len(messages.data) > 0:
                            return messages.data[0]
                        else:
                            print("No messages found in thread")
                            return None
                    except Exception as e:
                        print(f"Error retrieving latest message: {e}")
                        return None

                # Dynamically add the method to the instance
                self.get_latest_message = get_latest_message

            # Add process_message_response method if it doesn't exist
            if not hasattr(self, "process_message_response"):

                def process_message_response(message, with_img=False):
                    """Temporary inline implementation of process_message_response"""
                    try:
                        if message.role == "assistant":
                            content_parts = []
                            for content in message.content:
                                if content.type == "text":
                                    content_parts.append(content.text.value)

                            response_text = " ".join(content_parts)

                            try:
                                json_response = json.loads(response_text)
                                return json_response
                            except json.JSONDecodeError:
                                import re

                                json_pattern = r"\{.*\}"
                                matches = re.findall(
                                    json_pattern, response_text, re.DOTALL
                                )

                                for potential_json in matches:
                                    try:
                                        return json.loads(potential_json)
                                    except:
                                        continue

                                return {
                                    "actions": ["nod"] if with_img else [],
                                    "answer": response_text,
                                }

                        if self.current_language == "pl":
                            return {
                                "actions": [],
                                "answer": "Przepraszam, nie mogę odczytać odpowiedzi.",
                            }
                        else:
                            return {
                                "actions": [],
                                "answer": "Sorry, I couldn't read the response.",
                            }
                    except Exception as e:
                        print(f"Error processing message response: {e}")
                        if self.current_language == "pl":
                            return {
                                "actions": ["shake_head"],
                                "answer": "Przepraszam, wystąpił błąd podczas przetwarzania odpowiedzi.",
                            }
                        else:
                            return {
                                "actions": ["shake_head"],
                                "answer": "Sorry, there was an error processing the response.",
                            }

                # Dynamically add the method to the instance
                self.process_message_response = process_message_response

            # Use the instance thread_id if none provided
            if thread_id is None:
                thread_id = self.thread_id

            # Set fallback response with language awareness
            if fallback_response is None:
                if self.current_language == "pl":
                    fallback_response = "Przepraszam, mam problem z przetworzeniem obrazu. Spróbuj ponownie później."
                else:
                    fallback_response = "I'm sorry, I'm having trouble processing your request with the image. Please try again later."

            # Try to process the image
            try:
                if os.path.exists(img_path):
                    # Check if there's an active run on the thread
                    try:
                        # Get current runs on the thread (just use a simple try-except)
                        try:
                            runs = self.client.beta.threads.runs.list(
                                thread_id=thread_id, limit=1
                            )
                            if runs.data and runs.data[0].status in [
                                "queued",
                                "in_progress",
                                "requires_action",
                            ]:
                                run_id = runs.data[0].id
                                print(
                                    f"Active run {run_id} found. Waiting for completion..."
                                )
                                # Wait a few seconds
                                time.sleep(5)
                        except Exception as runs_error:
                            print(f"Error checking for active runs: {runs_error}")
                    except Exception:
                        pass  # Ignore any errors here

                    # Enhance the prompt with language instructions if needed
                    enhanced_prompt = prompt
                    if add_language_instruction and self.current_language:
                        language_name = self.current_language
                        enhanced_prompt += f"\n\nPlease respond in {language_name} language. It is very important that you respond in {language_name}."

                    # Try a completely different approach to attaching the image
                    try:
                        # Create a message with the image attached
                        file_object = None
                        try:
                            # First, create a file attachment
                            file_object = self.client.files.create(
                                file=open(img_path, "rb"), purpose="assistants"
                            )

                            # Create content list with text and image
                            content_parts = [
                                {"type": "text", "text": enhanced_prompt},
                                {
                                    "type": "image_file",
                                    "image_file": {"file_id": file_object.id},
                                },
                            ]

                            # Now create the message with both text and image
                            message = self.client.beta.threads.messages.create(
                                thread_id=thread_id, role="user", content=content_parts
                            )
                            print(f"Successfully attached image {img_path} to message")
                        except Exception as img_error:
                            print(f"Error attaching image: {img_error}")
                            # Fall back to text-only if image attachment fails
                            message = self.client.beta.threads.messages.create(
                                thread_id=thread_id,
                                role="user",
                                content=enhanced_prompt
                                + " (I've captured an image but couldn't attach it.)",
                            )
                            print(
                                "Using text-only mode due to image attachment failure"
                            )
                    except Exception as img_error:
                        print(f"Error: {img_error}")
                        # Emergency fallback
                        message = self.client.beta.threads.messages.create(
                            thread_id=thread_id, role="user", content=enhanced_prompt
                        )

                    # Run the assistant
                    try:
                        run = self.client.beta.threads.runs.create(
                            thread_id=thread_id,
                            assistant_id=self.assistant_id,
                        )
                        run_id = run.id
                        print(f"Created run with ID: {run_id}")
                    except Exception as run_error:
                        print(f"Error creating run: {run_error}")
                        return self._create_fallback_response(
                            fallback_response, "error"
                        )

                    # Wait for the run to complete - simple approach
                    try:
                        # Simple wait loop
                        timeout = 30  # 30 seconds
                        start_time = time.time()
                        completed = False

                        while time.time() - start_time < timeout:
                            try:
                                run_status = self.client.beta.threads.runs.retrieve(
                                    thread_id=thread_id, run_id=run_id
                                )
                                if run_status.status == "completed":
                                    print("Run completed successfully")
                                    completed = True
                                    break
                                elif run_status.status in [
                                    "failed",
                                    "cancelled",
                                    "expired",
                                ]:
                                    print(f"Run ended with status: {run_status.status}")
                                    break
                                time.sleep(1)
                            except Exception as e:
                                print(f"Error checking run status: {e}")
                                break

                        if not completed:
                            print("Run did not complete within the timeout period")
                            return self._create_fallback_response(
                                fallback_response, "timeout"
                            )
                    except Exception as wait_error:
                        print(f"Error waiting for run completion: {wait_error}")
                        # If we can't wait properly, try to continue anyway
                        time.sleep(5)  # Simple delay

                    # Retrieve and process messages
                    try:
                        messages = self.client.beta.threads.messages.list(
                            thread_id=thread_id, order="desc", limit=1
                        )

                        if messages.data and len(messages.data) > 0:
                            latest_message = messages.data[0]
                            if latest_message.role == "assistant":
                                # Extract content
                                content_parts = []
                                for content in latest_message.content:
                                    if content.type == "text":
                                        content_parts.append(content.text.value)

                                response_text = " ".join(content_parts)

                                # Parse JSON response
                                try:
                                    json_response = json.loads(response_text)
                                    return json_response
                                except json.JSONDecodeError:
                                    # Try to find JSON-like content
                                    import re

                                    json_pattern = r"\{.*\}"
                                    matches = re.findall(
                                        json_pattern, response_text, re.DOTALL
                                    )

                                    for potential_json in matches:
                                        try:
                                            return json.loads(potential_json)
                                        except:
                                            continue

                                    # If no valid JSON found, return a formatted response
                                    return {"actions": ["nod"], "answer": response_text}

                        # If we get here, no valid response was found
                        return self._create_fallback_response(
                            fallback_response, "no_response"
                        )
                    except Exception as msg_error:
                        print(f"Error retrieving messages: {msg_error}")
                        return self._create_fallback_response(
                            fallback_response, "message_retrieval_error"
                        )
                else:
                    print(f"Image file not found: {img_path}")
                    return self._create_fallback_response(
                        fallback_response, "file_not_found"
                    )
            except Exception as inner_e:
                print(f"Inner error processing image: {inner_e}")
                return self._create_fallback_response(fallback_response, str(inner_e))
        except Exception as e:
            print(f"Error in dialogue_with_img: {e}")
            return self._create_fallback_response(fallback_response, str(e))

    def _create_fallback_response(self, message, error_type="unknown"):
        """Create a fallback response with the given message and error type"""
        if self.current_language == "pl":
            if message is None:
                message = f"Przepraszam, wystąpił błąd typu '{error_type}'. Spróbuj ponownie później."
            return {
                "actions": ["shake_head"],
                "answer": message,
            }
        else:
            if message is None:
                message = (
                    f"Sorry, an error occurred: {error_type}. Please try again later."
                )
            return {
                "actions": ["shake_head"],
                "answer": message,
            }

    def text_to_speech(
        self, text, output_file, voice="alloy", response_format="mp3", speed=1
    ):
        """
        voice: alloy, echo, fable, onyx, nova, and shimmer
        """
        try:
            # Select a voice appropriate for the language if possible
            # For Polish, Nova or Alloy might work better with European languages
            if self.current_language == "pl" and voice == "alloy":
                voice = "nova"  # Nova tends to work better with European languages
                print(f"Using '{voice}' voice for Polish TTS")

            # check dir
            dir = os.path.dirname(output_file)
            if dir and not os.path.exists(dir):
                os.makedirs(dir)

            # tts
            with self.client.audio.speech.with_streaming_response.create(
                model="tts-1",
                voice=voice,
                input=text,
                response_format=response_format,
                speed=speed,
            ) as response:
                response.stream_to_file(output_file)

            return True
        except Exception as e:
            print(f"tts err: {e}")
            return False

    def handle_tool_calls(self, thread_id, run_id, tool_calls):
        """Handle tool calls from the assistant"""
        try:
            print(f"Handling {len(tool_calls)} tool calls")
            tool_outputs = []

            for tool_call in tool_calls:
                function_name = tool_call.function.name
                function_args = json.loads(tool_call.function.arguments)

                print(f"Function call: {function_name}")
                print(f"Arguments: {function_args}")

                if function_name == "play_youtube_video":
                    # Extract parameters
                    video_id = function_args.get("video_id")
                    quality = function_args.get("quality", "medium")
                    autoplay = function_args.get("autoplay", True)

                    # Call YouTube player function
                    try:
                        # First, try relative import
                        try:
                            from .youtube_player import play_youtube_video
                        except ImportError:
                            # If that fails, try direct import
                            from youtube_player import play_youtube_video

                        result = play_youtube_video(video_id, quality, autoplay)
                    except Exception as e:
                        print(f"Error importing or calling youtube_player: {e}")
                        result = False

                    # Add result to tool outputs
                    tool_outputs.append(
                        {
                            "tool_call_id": tool_call.id,
                            "output": json.dumps({"success": result}),
                        }
                    )
                else:
                    # Unknown function
                    tool_outputs.append(
                        {
                            "tool_call_id": tool_call.id,
                            "output": json.dumps({"error": "Function not implemented"}),
                        }
                    )

            # Submit tool outputs back to the assistant
            if tool_outputs:
                run = self.client.beta.threads.runs.submit_tool_outputs(
                    thread_id=thread_id, run_id=run_id, tool_outputs=tool_outputs
                )

                # Wait for completion after submitting tool outputs
                while run.status in ["queued", "in_progress"]:
                    print(f"Run status after tool submission: {run.status}")
                    time.sleep(1)
                    run = self.client.beta.threads.runs.retrieve(
                        thread_id=thread_id, run_id=run.id
                    )

                # Get the final response
                if run.status == "completed":
                    messages = self.client.beta.threads.messages.list(
                        thread_id=thread_id
                    )

                    # Extract the assistant's latest response
                    for message in messages.data:
                        if message.role == "assistant":
                            for content_item in message.content:
                                if content_item.type == "text":
                                    return content_item.text

            return "I've processed your request to play a YouTube video."

        except Exception as e:
            print(f"Error handling tool calls: {e}")
            return "I encountered an error while trying to process your request."

    def wait_for_run_completion(self, thread_id, run_id, timeout=30):
        """
        Wait for a run to complete within the specified timeout period.

        :param thread_id: The thread ID
        :param run_id: The run ID to wait for
        :param timeout: Timeout in seconds (default 30)
        :return: Boolean indicating if the run completed successfully
        """
        start_time = time.time()
        while time.time() - start_time < timeout:
            try:
                run = self.client.beta.threads.runs.retrieve(
                    thread_id=thread_id, run_id=run_id
                )

                if run.status == "completed":
                    print(f"Run {run_id} completed successfully")
                    return True
                elif run.status in ["failed", "cancelled", "expired"]:
                    print(f"Run {run_id} ended with status: {run.status}")
                    return False

                # Wait before checking again
                time.sleep(1)
            except Exception as e:
                print(f"Error checking run status: {e}")
                return False

        print(f"Run {run_id} timed out after {timeout} seconds")
        return False

    def get_latest_message(self, thread_id):
        """
        Retrieve the latest message from a thread.

        :param thread_id: The thread ID to get messages from
        :return: The latest message or None if not found
        """
        try:
            messages = self.client.beta.threads.messages.list(
                thread_id=thread_id, order="desc", limit=1
            )

            if messages.data and len(messages.data) > 0:
                return messages.data[0]
            else:
                print("No messages found in thread")
                return None
        except Exception as e:
            print(f"Error retrieving latest message: {e}")
            return None

    def process_message_response(self, message, with_img=False):
        """
        Process a message response from the assistant.

        :param message: The message to process
        :param with_img: Whether the message was in response to an image
        :return: Processed response as a dictionary
        """
        try:
            if message.role == "assistant":
                # Get the message content
                content_parts = []
                for content in message.content:
                    if content.type == "text":
                        content_parts.append(content.text.value)

                # Join the content parts
                response_text = " ".join(content_parts)

                # Try to parse as JSON
                try:
                    json_response = json.loads(response_text)
                    return json_response
                except json.JSONDecodeError:
                    # Look for JSON-like content
                    import re

                    json_pattern = r"\{.*\}"
                    matches = re.findall(json_pattern, response_text, re.DOTALL)

                    for potential_json in matches:
                        try:
                            return json.loads(potential_json)
                        except:
                            continue

                    # If we can't find valid JSON, create a formatted response
                    return {
                        "actions": ["nod"] if with_img else [],
                        "answer": response_text,
                    }

            # Default fallback
            if self.current_language == "pl":
                return {
                    "actions": [],
                    "answer": "Przepraszam, nie mogę odczytać odpowiedzi.",
                }
            else:
                return {"actions": [], "answer": "Sorry, I couldn't read the response."}
        except Exception as e:
            print(f"Error processing message response: {e}")
            if self.current_language == "pl":
                return {
                    "actions": ["shake_head"],
                    "answer": "Przepraszam, wystąpił błąd podczas przetwarzania odpowiedzi.",
                }
            else:
                return {
                    "actions": ["shake_head"],
                    "answer": "Sorry, there was an error processing the response.",
                }

    def process_image_with_vision_model(self, img_path, prompt):
        """
        This method is deprecated.
        We should use the Assistant API for image processing rather than direct vision model access.

        The PiCrawler application is designed to work with the Assistant API which has vision
        capabilities through the thread-based conversation model.
        """
        print(
            "WARNING: Direct vision model processing is disabled in favor of Assistant API"
        )
        return None
