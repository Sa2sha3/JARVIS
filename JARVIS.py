import os
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

command()