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

   
def takeCommand():
    # takes my command from microphone and gives text
    r =sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("recognizing...")
        query = r.recognize_google(audio, language ='en-in')
        print("user said : ", query)
    except Exception as e:
        print(e)
        speak("Sorry User, can you repeat that again?")
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
        speak("How can i help you?")
        query = takeCommand().lower()
        if 'wikipedia' in query:
                speak("searching in wikipedia")
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences = 2)
                speak("According to wikipedia")
                print(results)
                speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            speak("youtube is opened")
        elif 'open google' in query:
            webbrowser.open("google.com")
            speak("google is opened")
        
        elif 'teacher name' in query:
            speak("Our teacher name is Sir Rehaan. He is the best AI teacher I ever met.")

        elif 'open gmail' in query:
            webbrowser.open("gmail.com")
            speak("gmail is opened")
        elif 'play music' in query:
            while True:
                playsound('song.mp3')
            if 'pause' in query:
                break
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")

        elif 'open gender and age detection with image 1' in query:
            speak("Sure! Opening gender and age detection project")
            os.system('genderage.py --image imranKhan.jpg')

        elif 'open gender and age detection with image 2' in query:
            speak("Sure! Opening gender and age detection project")  
            os.system('genderage.py --image sir.jpg')

        elif 'open colour detection' in query:
            speak("Sure! Opening  detection project")
            os.system('color_detection.py')
            
        elif 'open object detection' in query:
            speak("Sure! Opening object detection project")
            os.system('RTV.py --model Model.caffemodel --prototxt ModelDeploy.prototxt.txt')
            
        elif 'motion detection' in query:
            speak("Sure! Opening motion detection project")
            os.system('plot.py')
            
        elif 'stop' in query:
            speak("see you soon user")
            exit()
        else :
            speak("Sorry can u repeat")
      
