import speech_recognition as sr
import os
from win32com.client import Dispatch

speak = Dispatch("SAPI.SpVoice").Speak

def say(text) :
    speak(text)

if __name__ == '__main__':
    print('PyCharm')
    say("Hello I am Jarvis A I")
