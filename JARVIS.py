import os

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

talk("Привіт, чим можу допомогти?")
