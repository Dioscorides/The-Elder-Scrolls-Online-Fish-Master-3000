"""
sound_detector.py

This script houses the SoundDetector class, designed to identify a specific sound within real-time audio data and
simulate a keyboard key press upon detection. The primary application of this script is to automate the
fishing process in the game "The Elder Scrolls Online". The script listens for a specific sound file (representing a
fish biting the hook in the game). Upon detection of this sound, it simulates a keyboard key press to reel in the
fish.

The SoundDetector class comprises methods to load the sound file, initiate recording of audio data from a specified input
device, process the audio data in real-time, detect the sound file in the audio data, and manage the detection of the
sound file.

This script necessitates the numpy, pyaudio, pyautogui, soundfile, and scipy Python libraries.

Usage: 1. Launch the game "The Elder Scrolls Online" and navigate to a fishing spot. 2. Execute this script. 3. Press
'e' to cast the line into the water. 4. The script automates the process from here, reeling in the fish when the bite
sound is detected and starting fishing again after a short pause.
"""

import random
import time

import numpy as np
import pyaudio
import pyautogui
import soundfile as sf
from scipy.signal import correlate, resample


class SoundDetector:
    """
    A class that detects a specific sound within real-time audio data and triggers a simulated keyboard key press
    upon detection.

    The SoundDetector class is designed to listen for a specific sound within a continuous audio stream. When the
    specified sound is identified, the class simulates a keyboard key press. This functionality can be used in
    various applications, such as automating certain tasks in response to specific audio cues.
    """

    def __init__(self, sound_file_path):
        """
        Initializes the SoundDetector instance.

        This method sets up the SoundDetector instance by taking the path to the sound file as an argument. The sound
        file is expected to be in a format that is readable by the soundfile library. The path is stored in the
        instance, and the sound file is loaded for further processing.

        Parameters:
        sound_file_path (str): The path to the sound file to be detected in the audio stream.
        """
        self.sound_file_path = sound_file_path
        self.sound_data, self.sound_sample_rate = self.load_sound_file()
        self.audio_data_duration = self.AUDIO_DATA_DURATION_MULTIPLIER * self.AUDIO_DATA_DURATION_SECONDS
        self.time_of_last_detection = 0
        self.time_of_last_key_press = 0
        self.resampled_sound_data = resample(self.sound_data, self.audio_data_duration)

    # Constants
    AUDIO_DATA_DURATION_MULTIPLIER = 288
    AUDIO_DATA_DURATION_SECONDS = 1
    DETECTION_THRESHOLD = 0.02
    KEY_TO_PRESS = 'e'
    MINIMUM_INTERVAL_BETWEEN_DETECTIONS = 5  # in seconds
    MINIMUM_INTERVAL_BETWEEN_KEY_PRESSES = 5  # in seconds
    DELAY_TIME_LOWER_BOUND = 0.15  # in seconds
    DELAY_TIME_UPPER_BOUND = 0.25  # in seconds
    LONG_DELAY_TIME_LOWER_BOUND = 3.4  # in seconds
    LONG_DELAY_TIME_UPPER_BOUND = 3.7  # in seconds

    def load_sound_file(self):
        """
        Load the sound file from the specified path.

        This method attempts to read the sound file from the path provided during the initialization of the SoundDetector
        instance. It uses the soundfile library's read function to load the file.

        Returns:
        tuple: A tuple containing the sound data and the sample rate of the sound file.

        Raises:
        FileNotFoundError: If the sound file is not found at the specified path.
        """
        try:
            return sf.read(self.sound_file_path)
        except FileNotFoundError:
            print(f"Error: Sound file '{self.sound_file_path}' not found")
            exit()

    def callback(self, incoming_audio_data, frame_count, time_info, status):
        """
        Callback function that processes the incoming audio data in real-time.

        This function is called by the audio stream each time a new frame of audio data is available. It converts the
        incoming audio data into a numpy array, reshapes the resampled sound data to match the shape of the audio
        data, and performs a cross-correlation between the audio data and the resampled sound data. If the maximum
        correlation value exceeds a predefined threshold and enough time has passed since the last detection and key
        press, it simulates a keyboard key press, updates the time of the last detection and key press,
        and then sleeps for a predefined pause time before simulating another key press.

        Parameters:
        incoming_audio_data (bytes): The incoming audio data as a byte string.
        frame_count (int): The number of frames in the incoming audio data.
        time_info (dict): A dictionary containing timing information for the audio stream.
        status (int): The status of the audio stream.

        Returns: tuple: A tuple containing the incoming audio data and a flag indicating whether the audio stream
        should continue or stop.
        """
        audio_data_array = np.frombuffer(incoming_audio_data, dtype=np.float32)
        reshaped_sound_data = np.reshape(self.resampled_sound_data, (len(audio_data_array), ))
        correlation = correlate(audio_data_array, reshaped_sound_data, mode='valid')
        max_correlation = np.max(correlation)
        if max_correlation > self.DETECTION_THRESHOLD and time.time() - self.time_of_last_detection > self.MINIMUM_INTERVAL_BETWEEN_DETECTIONS and time.time() - self.time_of_last_key_press > self.MINIMUM_INTERVAL_BETWEEN_KEY_PRESSES:
            print("Fish on, fish on!")
            delay_time = random.uniform(self.DELAY_TIME_LOWER_BOUND, self.DELAY_TIME_UPPER_BOUND)
            long_delay_time = random.uniform(self.LONG_DELAY_TIME_LOWER_BOUND, self.LONG_DELAY_TIME_UPPER_BOUND)
            time.sleep(delay_time)
            pyautogui.press(self.KEY_TO_PRESS)
            print(f"Reeled in fish after {delay_time} seconds")
            self.time_of_last_detection = time.time()
            self.time_of_last_key_press = time.time()
            time.sleep(long_delay_time)
            print(f"Paused for {long_delay_time} seconds")
            pyautogui.press(self.KEY_TO_PRESS)
            print(f"Fishing again!")
        return incoming_audio_data, pyaudio.paContinue

    def start(self):
        """
        Starts recording audio data from a specified input device.

        This method initializes an audio stream with the PyAudio library and starts recording audio data from the
        input device specified by the 'input_device_index' parameter. The audio data is processed in real-time by the
        'callback' method.

        Note: The 'input_device_index' should be set to the index of the desired input device. To get a list of all
        available audio devices on your system, run the 'list_audio_devices.py' script.

        Raises:
            IOError: If the specified input device is not available or if there's an error starting the audio stream.
        """
        audio_stream = pyaudio.PyAudio()
        stream = audio_stream.open(
            format=pyaudio.paFloat32, 
            channels=1, 
            rate=44100,
            input=True, 
            output=False, 
            stream_callback=self.callback, 
            input_device_index=6
        )
        stream.start_stream()
        input("Gone fishing!")
        stream.stop_stream()
        stream.close()
        audio_stream.terminate()


if __name__ == "__main__":
    detector = SoundDetector('hooked.wav')
    detector.start()