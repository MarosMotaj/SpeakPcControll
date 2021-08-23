#!/usr/bin/python3
"""
linux terminal install:
pip install SpeechRecognition
sudo apt-get install python-pyaudio python3-pyaudio
"""
import speech_recognition as sr

class Microphone:
    """
    print(sr.Microphone.list_microphone_names())
    if you want to find external microphone,
    then you have to put it as parameter to sr.Microphone(microphone-name) method
    """

    def text_from_microphone(self):
        r = sr.Recognizer()
        mic = sr.Microphone()

        try:
            with mic as source:
                r.adjust_for_ambient_noise(source)  # method for filter strange noises from microphone
                audio = r.listen(source)
            speach_in_text = r.recognize_google(audio)

            return speach_in_text
        except:
            print("Strange noise detected")
