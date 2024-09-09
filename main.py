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
        r.pause_threshold=0.8
        audio=r.listen(source)
        try:
            query = r.recognize_whisper(audio, language="english")
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
        sites=[["youtube", "https://www.youtube.com"], ["google", "https://www.google.com"], ["wikipedia", "https://www.wikipedia.com"]]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]}")
                webbrowser.open(site[1])

        # say(query)
