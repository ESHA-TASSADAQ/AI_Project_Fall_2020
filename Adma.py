import pyttsx3
import datetime
import speech_recognition as sr 
import wikipedia
import webbrowser
from playsound import playsound
import os

print("Preparing Adma")
engine = pyttsx3.init('sapi5') #Microsoft Speech API (SAPI5) is the technology for voice recognition and synthesis provided by Microsoft.
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning User")
    elif hour>=12 and hour<4:
        speak("Good afternoon User")
    else:
        speak("Good Evening User")

    speak("I am your Assistant Admaa")
    