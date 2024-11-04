import pyttsx3
import speech_recognition as sr
import eel
import time 


def speak(text):
    engine = pyttsx3.init('nsss')
    engine.setProperty('rate', 174)
    engine.say(text)
    engine.runAndWait()    

@eel.expose
def takecommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('listening....')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source, 10, 6)

    try:
        print('recognizing')
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")
        speak(query)
        time.sleep(2)

    except Exception as e:
        return ""
    
    return query.lower()


