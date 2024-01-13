"""
list_audio_devices.py

This script is designed to list all available audio devices on the system. It uses the sounddevice Python library to
query the system for audio devices and prints out a list of these devices along with their respective number of input
and output channels.

The primary use of this script is to assist users in identifying the correct audio device index when configuring audio
input for other scripts or applications.

Usage:
1. Execute this script.
2. The script will print a list of all available audio devices on the system, along with their respective number of
   input and output channels.
3. Use the printed information to identify the correct audio device index in sound_detector.py.
"""

import sounddevice as sd

DEVICE_LIST_HEADER = "Available audio devices:"


def get_audio_devices():
    """
    Query the system for available audio devices using the sounddevice library.
    Returns a list of available audio devices.
    """
    return sd.query_devices()


def print_audio_device_info(device_info, index):
    """
    Prints the information of a single audio device.
    """
    print(
        f"{index}: {device_info['name']} (input channels: {device_info['max_input_channels']}, output channels: {device_info['max_output_channels']})")


def print_all_audio_devices(devices):
    """
    Prints the information of all available audio devices.
    """
    print(DEVICE_LIST_HEADER)
    for i, device in enumerate(devices):
        print_audio_device_info(device, i)


def main():
    """
    Main function to list all available audio devices on the system.
    """
    devices = get_audio_devices()
    print_all_audio_devices(devices)


if __name__ == "__main__":
    main()
