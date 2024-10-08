import os
from datetime import datetime
import speech_recognition as sr
from win32com.client import Dispatch
import soundfile
import webbrowser

speak = Dispatch("SAPI.SpVoice").Speak

def say(text) :
    speak(text)

def take_command():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold=0.6
        audio=r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_whisper(audio, language="en")
            print(f"User said -  {query}")
            return query
        except Exception as e:
            return "Please try again"

if __name__ == '__main__':
    print("PyCharm")
    print("Speaking...")
    say("Hello I am Jarvis A I")
    while True:
        print("Listening...")
        query=take_command()
        sites=[["youtube", "https://www.youtube.com"], ["google", "https://www.google.com"], ["instagram", "https://www.instagram.com"]]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]}")
                webbrowser.open(site[1])

        if "open music".lower() in query.lower():
            musicPath="C:/Users/ashut/PycharmProjects/JarvisAI/vinee-heights-126947.mp3"
            os.startfile(musicPath)

        if "the time".lower() in query.lower():
            strfTime=datetime.now().strftime("%H:%M:%S")
            say(f"the time is {strfTime}")

        if "open notepad".lower() in query.lower():
            file="C:/ProgramData/Microsoft/Windows/Start Menu/Programs/Accessories/Notepad"
            os.startfile(file)




        # say(query)
