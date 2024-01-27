"""
Voice Recognition Script

This script allows users to perform basic voice-controlled actions using speech recognition.
It uses the pyttsx3 library for text-to-speech and the speech_recognition library for voice recognition.

Requirements:
- Install required libraries using: pip install pyttsx3 SpeechRecognition

Usage:
1. Run the script.
2. Speak commands such as "exit" or "stop" to terminate the script.
3. Customize additional commands as needed.

Note: This script currently recognizes the "exit" or "stop" command to terminate the loop.

"""

import pyttsx3
import speech_recognition as sr
import subprocess

# Initialize the speech engine
engine = pyttsx3.init()

# Function to speak the provided text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Initialize the speech recognizer
recognizer = sr.Recognizer()

# Main loop for voice recognition
while True:
    with sr.Microphone() as mic:
        recognizer.adjust_for_ambient_noise(mic, duration=0.2)
        print("Listening...")
        audio = recognizer.listen(mic)

        try:
            # Recognize the speech and convert to lowercase
            text = recognizer.recognize_google(audio).lower()
            print(f"Recognized: {text}")

            # Check for specific commands
            if "exit" in text or "stop" in text:
                print("Exiting the script.")
                break

        except sr.UnknownValueError:
            print("Sorry, could not understand audio.")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")

# Terminate the script
print("Terminated.")
