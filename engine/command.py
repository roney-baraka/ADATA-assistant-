import pyttsx3
import speech_recognition as sr
import eel
import time 


def speak(text):
    engine = pyttsx3.init('nsss')
    engine.setProperty('rate', 174)
    engine.say(text)
    engine.runAndWait()    


def takecommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('listening....')
        eel.DisplayMessage('listening....')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source, 10, 6)

    try:
        print('recognizing')
        eel.DisplayMessage('recognizing....')
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")
        eel.DisplayMessage(query) 
        eel.ShowHood()
        time.sleep(2)

    except Exception as e:
        print("Error in recognition")
        eel.DisplayMessage("Error in recognition")
        return ""
    
    return query.lower()

@eel.expose
def allCommands():

    query = takecommand()
    print(f"Command received: {query}")

    if "open" in query:
        print("running open command")
        speak("Opening...")
        eel.DisplayMessage("Opening...")

    else:
        print("Command not recognized ")
        speak("command not recognized")
        eel.DisplayMessage("Command not recognized")    