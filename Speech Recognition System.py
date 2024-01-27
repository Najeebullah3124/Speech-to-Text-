#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pyttsx3
import speech_recognition as sr
import subprocess

recognizer = sr.Recognizer()

while True:
    with sr.Microphone() as mic:
        recognizer.adjust_for_ambient_noise(mic, duration=0.2)
        print("Listening...")
        audio = recognizer.listen(mic)
        try:
            text = recognizer.recognize_google(audio).lower()
            print(f"Recognized: {text}")

            if "exit" in text or "stop" in text:
                print("Exiting the script.")
                break
                
        except sr.UnknownValueError:
            print("Sorry, could not understand audio.")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
print("Terminated.")


# In[ ]:




