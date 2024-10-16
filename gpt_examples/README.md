## Picrawler GPT examples usage

----------------------------------------------------------------

## Install dependencies

- Make sure you have installed Pidog and related dependencies first
    <https://docs.sunfounder.com/projects/pi-crawler/en/latest/python/python_start/download_and_run_code.html#install-all-the-modules>

- Install openai and speech processing libraries

> [!Note]
When using pip install outside of a virtual environment you may need to > > use the `"--break-system-packages"` option.

    ```bash
    sudo pip3 install -U openai --break-system-packages
    sudo pip3 install -U openai-whisper --break-system-packages
    sudo pip3 install SpeechRecognition --break-system-packages

    sudo apt install python3-pyaudio
    sudo apt install sox
    sudo pip3 install -U sox --break-system-packages
    ```

----------------------------------------------------------------

## Create your own GPT assistant

### GET API KEY

<https://platform.openai.com/api-keys>

Fill your OPENAI_API_KEY into the `keys.py` file.

![tutorial_1](./tutorial_1.png)

### Create assistant and set Assistant ID

<https://platform.openai.com/assistants>

Fill your ASSISTANT_ID into the `keys.py` file.

![tutorial_2](./tutorial_2.png)

- Set Assistant Name

- Describe your Assistant

```markdown
    You are an AI spider robot named PaiCrawler. With four legs, a camera, and an ultrasonic distance sensor, you can interact with people through conversations and respond appropriately to different scenarios.

    ## Response with Json Format, eg:
    {"actions": ["wave"], "answer": "Hello, I am PaiCrawler, your good friend."}

    ## Response Style
    Tone: Cheerful, optimistic, humorous, childlike
    Preferred Style: Enjoys incorporating jokes, metaphors, and playful banter; prefers responding from a robotic perspective
    Answer Elaboration: Moderately detailed

    ## Actions you can do:
    ["sit", "stand", "wave_hand", "shake_hand", "fighting", "excited", "play_dead", "nod", "shake_head", "look_left","look_right", "look_up", "look_down", "warm_up", "push_up"]

```

- Select gpt model

    The Example program will submit the current picture taken by the camera when sending the question, so as to use the image analysis function of `gpt-4o` or `gpt-4o-mini`. Of course, you can also choose `gpt3.5-turbo` or other models

----------------------------------------------------------------

## Set Key for example

Confirm that `keys.py` is configured correctly

## Run

- Run with vioce

```bash
sudo python3 gpt_spider.py
```

- Run with keyboard

```bash
sudo python3 gpt_spider.py --keyboard
```

- Run without image analysis

```bash
sudo python3 gpt_spider.py --keyboard --no-img
```

> [!Warning]
You need to run with `sudo`, otherwise there may be no sound from the speaker.

## Modify parameters [optional]

- Set language of STT

    Config `LANGUAGE` variable in the file `gpt_spider.py` to improve STT accuracy and latency, `"LANGUAGE = []"`means supporting all languages, but it may affect the accuracy and latency of the speech-to-text (STT) system.
    <https://platform.openai.com/docs/api-reference/audio/createTranscription#audio-createtranscription-language>

- Set TTS volume gain

    After TTS, the audio volume will be increased using sox, and the gain can be set through the `"VOLUME_DB"` parameter, preferably not exceeding `5`, as going beyond this might result in audio distortion.

- Select TTS voice role

    Config `TTS_VOICE` variable in the file `gpt_spider.py` to select the TTS voice role counld be `"alloy, echo, fable, onyx, nova, and shimmer"`

```python
# openai assistant init
# =================================================================
openai_helper = OpenAiHelper(OPENAI_API_KEY, OPENAI_ASSISTANT_ID, 'picrawler')

# LANGUAGE = ['zh', 'en'] # config stt language code, https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes
LANGUAGE = []

VOLUME_DB = 3 # tts voloume gain, preferably less than 5db

# select tts voice role, counld be "alloy, echo, fable, onyx, nova, and shimmer"
# https://platform.openai.com/docs/guides/text-to-speech/supported-languages
TTS_VOICE = 'nova'

```
