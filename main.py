import speech_recognition as sr
import gtts
from playsound import playsound
import os
from datetime import datetime
from notion import NotionClient



r = sr.Recognizer()

token = "secret_HwsHYl6EX7WUJMTTXZOj3aUEa0MMCtu76sdqfpMwxXg"
database_id = "5401e5efc6dd41b88e69b738d267844e"
client = NotionClient(token, database_id)



ACTIVATION_COMMAND = "Hi"

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


def play_sound(text):
    try:
        tts = gtts.gTTS(text)
        tempfile = "./temp.mp3"
        tts.save(tempfile)
        playsound (tempfile)
        os.remove (tempfile)
    except AssertionError:
        print("Could Not Play Sound")


if __name__ == "__main__":
    while True:
        a = get_audio ()
        command = audio_to_text(a)
        

        if ACTIVATION_COMMAND in command.lower():
            print("Activate")
            playsound ("What can I do for you?")


            note = get_audio()
            note = audio_to_text(note)


            if note:
                playsound (note)

                now = datetime.now().astimezone().isoformat()
                res = client.create_page(note, now, status="Active")

                if res.status_code == 200:
                    play_sound = "Start New Item"




                


