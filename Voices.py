import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty("voices")


# for voice in voices:
#     print('-----------''')
#     print(f'Name: {voice.name}')
#     print(f'ID: {voice.name}')
#     print(f'Language: {voice.name}')
#     print(f'Gender: {voice.name}')a
#     print(f'Age: {voice.name}')

engine.setProperty("voice", "eng")
for voice in voices:
    if voice.name == "Zira":
        engine.setProperty("voice", voice.id)
engine.say("Hello")
engine.runAndWait()