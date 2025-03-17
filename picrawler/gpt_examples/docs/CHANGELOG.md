# Arachne PiCrawler Changelog

## Version 1.1.3 (March 2025)

### New Features (v1.1.3)

- Added comprehensive voice preset system for greetings, goodbyes and responses
- Implemented pre-generated voice messages with metadata and associated actions
- Added time-specific greetings (morning, afternoon, evening)
- Created structured folders for different types of audio messages

### Bug Fixes (v1.1.3)

- Fixed OpenAI image processing error by adding multiple fallback methods including base64 encoding
- Enhanced audio file processing to properly handle integer conversion and file existence
- Improved smile action implementation to eliminate 'servo' attribute error
- Added proper error handling for TTS file generation failures

### Improvements (v1.1.3)

- Added comprehensive audio playback error handling
- Enhanced greeting and goodbye message system with better error recovery
- Added Polish language support for preset voice messages

## Version 1.1.2 (March 2025)

### Bug Fixes (v1.1.2)

- Fixed OpenAI API image processing error with "file_ids" parameter by adding compatibility for both older and newer API versions
- Fixed audio playback issues in greeting and goodbye messages by properly initializing audio_output
- Fixed "smile" action implementation to use spider.do_action() instead of direct servo control

### Improvements (v1.1.2)

- Added audio playback verification to the testing script
- Enhanced error handling for audio output initialization and playback
- Added proper initialization checks for TTS file creation

## Version 1.1.1 (March 2025)

### New Features (v1.1.1)

- Added autonomous greeting and goodbye messages based on time of day
- Added 'smile' action to handle smile requests from the OpenAI assistant
- Improved shutdown process with proper goodbye message and actions

### Bug Fixes (v1.1.1)

- Fixed YouTube module check in verify_fixes.py by using direct import instead of importlib.util

## Version 1.1.0 (March 2025)

### Bug Fixes (v1.1.0)

- Fixed action handler to recognize all 28 movement functions by checking actions_dict dynamically
- Added missing `look_around` function to handle the previously invalid action
- Fixed SDN warning in camera initialization by applying tuning settings beforehand
- Improved YouTube video playing functionality with better error handling and debugging
- Enhanced thread management in OpenAI Assistant integration for better error recovery

### New Features (v1.1.0)

- Added YouTube video playback capability via OpenAI function calls
- Added custom tuning for libcamera to optimize image quality

### Improvements (v1.1.0)

- Updated dependency installation script to include YouTube-related packages
- Added comprehensive error handling and logging throughout the codebase
- Enhanced JSON parsing to better handle non-standard responses from OpenAI

## Version 1.0.0 (Initial Release)

### Features (v1.0.0)

- Basic movement functions with preset actions
- Speech-to-text and text-to-speech capabilities
- Camera integration with object detection
- Integration with OpenAI Assistant API for natural language understanding
- Web interface for robot control and monitoring
