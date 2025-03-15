# Arachne PiCrawler with GPT-4o Integration

A Raspberry Pi-powered robot spider with advanced AI capabilities, powered by GPT-4o for natural language interaction and vision capabilities.

## Project Structure

```directory
gpt_examples/
├── src/                 # Source code
│   ├── core/           # Core functionality
│   │   ├── gpt_spider.py       # Main robot control
│   │   ├── openai_helper.py    # OpenAI API integration
│   │   ├── preset_actions.py   # Robot actions
│   │   └── keys.py            # API configuration
│   ├── vision/         # Vision-related code
│   │   ├── enable_vision.py    # Vision capabilities
│   │   └── flask_camera_server.py # Camera server
│   └── utils/          # Utilities
│       ├── utils.py           # Common utilities
│       └── youtube_player.py  # YouTube integration
├── scripts/            # Shell scripts
│   ├── setup_dependencies.sh  # Installation script
│   └── run_with_keyboard.sh  # Keyboard control mode
├── tests/              # Test utilities
│   ├── test_actions.py       # Action testing
│   ├── test_openai.py       # OpenAI integration testing
│   └── simple_mic_test.py   # Microphone testing
├── docs/               # Documentation
│   └── CHANGELOG.md         # Version history
└── config/             # Configuration files
    └── libcamera_tuning.json # Camera configuration
```

## Prerequisites

1. A Raspberry Pi with the PiCrawler robot assembled
2. OpenAI API key (requires payment)
3. OpenAI Assistant ID configured for the PiCrawler
4. Optional: USB microphone for voice interaction

## Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/Xza85hrf/Arachne-Picrawler.git
   cd Arachne_PiCrawler
   ```

2. **Install Dependencies**:
   First, install PiCrawler dependencies:

   ```bash
   # Follow SunFounder's guide for basic setup
   https://docs.sunfounder.com/projects/pi-crawler/en/latest/python/python_start/download_and_run_code.html
   ```

   Then install additional dependencies:

   ```bash
   cd picrawler/gpt_examples/scripts
   ./setup_dependencies.sh
   ```

3. **Configure OpenAI Integration**:
   - Get your API key from: <https://platform.openai.com/api-keys>
   - Create an Assistant at: <https://platform.openai.com/assistants>
   - Copy `src/core/keys.template.py` to `src/core/keys.py`
   - Add your keys to `keys.py`:

     ```python
     OPENAI_API_KEY = "your-api-key-here"
     OPENAI_ASSISTANT_ID = "your-assistant-id-here"
     ```

## Usage

### Voice Control Mode

```bash
cd src/core
python3 gpt_spider.py
```

### Keyboard Control Mode

```bash
cd scripts
./run_with_keyboard.sh
```

### Command Line Options

- `--keyboard`: Use keyboard input instead of voice
- `--no-img`: Disable camera functionality
- `--debug`: Show debugging information

## Features

- Natural language interaction through GPT-4o
- Voice and keyboard control options
- Advanced movement capabilities
- Vision system with camera integration
- YouTube video playback capability
- Autonomous greeting and goodbye messages

## Vision Capabilities

### Enabling Vision

1. **Automatic Setup**:

   ```bash
   python picrawler/gpt_examples/enable_vision.py
   ```

2. **Manual Configuration**:
   - Ensure your Assistant uses a vision-capable model (GPT-4o recommended)
   - The robot will automatically attach camera images to conversations

### Supported Vision Models

- GPT-4o (recommended)
- GPT-4o-mini (recommended)
- GPT-4-vision
- GPT-4-turbo

### Testing Vision

Ask the robot questions about its environment:

- "What can you see?"
- "Describe the room you're in"
- "How many people are in front of you?"

## Testing

The `tests` directory contains utilities for testing different components:

```bash
cd tests
# Test robot actions
python3 test_actions.py [action_name]
# Test OpenAI integration
python3 test_openai.py
# Test microphone setup
python3 simple_mic_test.py
```

## Configuration Options

### Speech Recognition

- Set STT language in `gpt_spider.py`:

  ```python
  LANGUAGE = []  # Empty for all languages
  LANGUAGE = ['en']  # English only
  LANGUAGE = ['zh', 'en']  # Chinese and English
  ```

### Text-to-Speech

- Adjust volume gain (max 5dB):

  ```python
  VOLUME_DB = 3
  ```

- Select voice:

  ```python
  TTS_VOICE = 'shimmer'  # Options: alloy, echo, fable, onyx, nova, shimmer
  ```

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Future Development Plans

The following improvements are planned for future versions:

1. **Smoother Action Transitions**
   - Improve transitions between actions for more fluid and natural movements
   - Implement motion interpolation for smoother joint movements

2. **Action Memory System**
   - Track recently performed actions to avoid repetitive behaviors
   - Implement action history and preference learning

3. **Context-Aware Actions**
   - Enhance AI decision-making based on conversation context
   - Better environmental awareness for action selection

4. **Energy Management**
   - Monitor battery levels in real-time
   - Adapt movements to conserve energy when needed
   - Implement power-saving modes

5. **Enhanced Logging**
   - More detailed action execution logging
   - Improved troubleshooting capabilities
   - Performance metrics tracking

## Acknowledgments

- SunFounder for the PiCrawler robot platform
- OpenAI for the GPT-4o API
  