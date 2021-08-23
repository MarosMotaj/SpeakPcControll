#!/usr/bin/python3
# class for openning defined programs in linux PC
"""
in subprocess.call() method, you have to insert linux terminal command
for run defined program as parameter
"""
from microphone import Microphone
from text_to_speech import Speech
import subprocess
import time


class OpenProgram:

    def open_program(self):
        mic = Microphone()
        speech = Speech()

        microphone_text = mic.text_from_microphone()
        try:
            if microphone_text == "computer":
                speech.text_to_speech("Yes?")
                time.sleep(0.5)
                speech.text_to_speech("I am waiting on your commands")

            elif microphone_text == "internet":
                speech.text_to_speech("Starting internet")
                subprocess.call("google-chrome")

            elif microphone_text == "programming":
                speech.text_to_speech("Starting programming ide")
                subprocess.call("code")

            elif microphone_text == "calculator":
                speech.text_to_speech("Starting calculator")
                subprocess.call("gnome-calculator")

            else:
                print("Unknown command")
        except:
            print("Requesting programm not found")



