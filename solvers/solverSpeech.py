import speech_recognition as sr
import pyttsx3

def SpeakText(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

def CollectText(x, gram):
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.3)
        audio = recognizer.listen(source)
        x = recognizer.recognize_sphinx(audio, grammar=gram)
        x = x.lower()
        return x
        