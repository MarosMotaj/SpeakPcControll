#!/usr/bin/python3
# class for recording microphone audio
"""
Linux terminal install:
pip install gTTS
"""
import gtts
from playsound import playsound

class Speech:

    def text_to_speech(self, text):
        tts = gtts.gTTS(text)
        tts.save("speech_audio/speech.mp3")
        playsound("speech_audio/speech.mp3")


