import speech_recognition as sr
from win32com.client import Dispatch
import soundfile

speak = Dispatch("SAPI.SpVoice").Speak

def say(text) :
    speak(text)

def take_command():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold=1
        audio=r.listen(source)
        query=r.recognize_whisper(audio, language="english")
        print(f"User said -  {query}")

if __name__ == '__main__':
    print("PyCharm")
    print("Speaking...")
    say("Hello I am Jarvis A I")
    print("Listening...")
    take_command()
