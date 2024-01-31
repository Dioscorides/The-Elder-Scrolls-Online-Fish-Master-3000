# Welcome to The Elder Scrolls Online Fish Master 3000 documentation

This documentation aims to help you understand how to use the addon and become a successful fisherman.

!!! warning
    The Elder Scrolls Online EULA prohibits the use of third-party programs to automate gameplay:

    > use cheats, automation software (bots), hacks, mods or any other unauthorized third-party software designed to modify the Game or adversely impact any other persons playing of the Game or his/her experience of playing the Game;

    While you are not "modifying the game" or "adversely impacting" other players by automating the fishing process, you might still be considered in violation the EULA by using this program. Use this program at your own risk.

## Concept

The **The Elder Scrolls Online Fish Master 3000** uses the following concept to automate the fishing process in the game "The Elder Scrolls Online":

1. Thanks to [Votan's Fisherman](https://www.esoui.com/downloads/info918-VotansFisherman.html) plugin, the game plays a sound effect when a fish bites the hook.
2. The sound effect is recorded by the computer's audio input device.
3. The recorded audio data is analyzed in real-time to detect the sound effect.
4. When the sound effect is detected, a keyboard key is simulated to reel in the fish.
5. The process is repeated until all fish are caught and the fishing hole is depleted.

## Prerequisites

The **The Elder Scrolls Online Fish Master 3000** requires the following software to be installed:

1. [Python 3.8.5](https://www.python.org/downloads/release/python-385/) or newer
2. The Elder Scrolls Online
3. [Votan's Fisherman](https://www.esoui.com/downloads/info918-VotansFisherman.html) add-on for The Elder Scrolls Online
4. A sound file of the fishing sound effect from the _Votan's Fisherman_ plugin (one is included in the repository)
5. Patience

## Dependencies

The sound_detector.py script requires the following Python libraries to be installed:

- numpy: A library for working with arrays and numerical operations.
- soundfile: A library for reading and writing sound files.
- pyaudio: A library for working with audio streams.
- scipy: A library for scientific computing and signal processing.
- pyautogui: A library for GUI automation.

## Usage

To use the sound_detector.py script, follow these steps:

1. Install the required Python libraries.
2. Define the path to the sound file to detect in the `sound_file_path` variable.
3. Adjust the threshold variable `DETECTION_THRESHOLD` to set the minimum correlation value required for the sound file to be detected. The lower, the more sensitive.
4. Adjust the `MINIMUM_INTERVAL_BETWEEN_DETECTIONS` variable to set the minimum time between sound file detections.
5. Adjust the key variable `KEY_TO_PRESS` to set the keyboard key to simulate.
6. Adjust the `MINIMUM_INTERVAL_BETWEEN_KEY_PRESSES` variable to set the minimum time between keyboard key presses.
7. Adjust the `DELAY_TIME_LOWER_BOUND` and `DELAY_TIME_UPPER_BOUND` variables to set the pause time after the first keyboard key press.
8. Run the sound_detector.py script.

The script will start recording audio data from the default audio input device. When the selected sound file is detected in the audio data, the script will simulate a keyboard key press using pyautogui.press(key).

Carefully read the `sound_detector.py` script and adjust the variables to match your system and requirements.

## Code Structure

The sound_detector.py script is structured as follows:

1. Import the required Python libraries.
2. Define the path to the sound file to detect.
3. Load the sound file.
4. Define the length of the audio data to record.
5. Define the threshold for sound detection.
6. Define the minimum time between detections.
7. Define the keyboard key to simulate.
8. Define the minimum time between key presses.
9. Define the pause time after the first key press.
10. Resample the sound file to match the length of the audio data.
11. Define the callback function for recording audio.
12. Initialize the audio stream.
13. Start recording audio.
14. Wait for user input to stop recording.
15. Stop recording audio and close the audio stream.

The callback function is the main function that is called by the audio stream to process the audio data. The callback function performs the following steps:

- Convert the audio data to a numpy array.
- Reshape the sound file to match the shape of the audio data.
- Cross-correlate the audio data with the sound file.
- Calculate the maximum correlation value.
- Check if the sound file is detected and enough time has passed since the last detection and key press.
- Simulate a keyboard key press using pyautogui.press(key).
- Update the time of the last detection and key press.
- Wait for the pause time.
- Add a random delay time between 0.3 and 1.2 seconds.
- Simulate a keyboard key press again using pyautogui.press(key).

## Limitations

The sound_detector.py script has the following limitations:

- The script can only detect sound files that match the length and format of the resampled sound file.
- The script may produce false positives if the audio data contains noise or other sounds that match the sound file.
