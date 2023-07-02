import os
import sys
import webbrowser

import speech_recognition as sr

#
import pyttsx3
engine = pyttsx3.init()
#engine.say("Шота")
#engine.runAndWait()

#
def talk(words):
    # os.system("say" + words)
    engine.say(words)
    engine.runAndWait()

talk("Hello")


def command():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Say")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        task = r.recognize_google(audio, language="en-US").lower()
        print("You: " + task)
    except:
        talk("I dont understand you")
        task = command()


    return task

def make_something(ar_task):
    if ("open" and "site") in ar_task:
        talk("ok")
        url = "https://ituniver.com"
        webbrowser.open(url)

    elif "Stop" in ar_task:
        talk("Good bye")
        sys.exit()

    elif "name" in ar_task:
        talk("My name is JARVIS")

make_something(command())

command()