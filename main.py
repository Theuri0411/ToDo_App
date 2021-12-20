import speech_recognition as sr
import gtts
from playsound import playsound


r = sr.Recognizer

def get_audio():
    with sr.Microphone() as source:
        print ("Say Something")
        audio = r.listen(source)
    return audio