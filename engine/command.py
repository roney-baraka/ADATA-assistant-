import pyttsx3


def speak(text):
    engine = pyttsx3.init('nsss')
    engine.setProperty('rate', 174)
    engine.say(text)
    engine.runAndWait()    


speak("Hi! Am ADATA")