# SpeakPcControll
SpeakLinuxPcControll

This program uses microphone commands to open predefined programs in Linux PC 
(Tested on Linux Ubuntu 20.04, Python 3.8 version, Dell notebook PC). 
I have predefined to open (Google Chrome, Visual Studio Code, Calculator). 
You can define your own programs to be open in open_item.py. 

Voice commands:
1. "internet": opens Google Chrome
2. "programming": opens Visual Studio Code
3. "calculator": opens Calculator

Linux terminal commands to install libraries:
1. sudo apt-get update -y
2. pip install SpeechRecognition
3. sudo apt-get install python-pyaudio python3-pyaudio 
4. pip install gTTS

Run program:
1. Go to program destination folder.
2. Open path in terminal.
3. Run command: python3 main.py
