# SpeakPcControll
SpeakLinuxPcControll

This program uses microphone commands to open predefined programs in Linux PC 
(Tested on Linux Ubuntu 20.04, Python 3.8 version, Dell notebook PC). 
I have predefined to open (Google Chrome, Visual Studio Code, Calculator). 
You can define your own programs to be open in open_item.py. 

Voice commands:
"internet": opens Google Chrome
"programming": opens Visual Studio Code
"calculator": opens Calculator

Linux terminal commands to install libraries:
sudo apt-get update -y
pip install SpeechRecognition
sudo apt-get install python-pyaudio python3-pyaudio
pip install gTTS

Run program:
1. Go to program destination folder.
2. Open path in terminal.
3. Run command: python3 main.py
