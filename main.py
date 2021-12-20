import speech_recognition as sr
import gtts
from playsound import playsound


r = sr.Recognizer()

def get_audio():
    with sr.Microphone() as source:
        print ("Say Something")
        audio = r.listen(source)
    return audio

def audio_to_text (audio):
    text = ""
    try:
        text= r.recognize_google(audio)
    except sr.UnknownValueError:
        print("Speech Could Not Understand Audio")
    except sr.RequestError:
        print("Could Not Process Results from API")
    return text


    if __name__ == "__main__":
        a = get_audio ()
        command = audio_to_text(a)
        print(command)
