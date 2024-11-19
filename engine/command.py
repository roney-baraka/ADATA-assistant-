import pyttsx3
import speech_recognition as sr
import eel
import time 
import platform 
import logging 

#Configure logging 
logging.basicConfig(filename="assistant.log", level=logging.DEBUG)


def speak(text):
    try:
        engine =pyttsx3.init()
        system = platform.system()

        if system == "Darwin":
            engine.setProperty('voice', 'com.apple.speech.synthesis.voice.samantha')    
        elif system == "Windows":
            engine.setProperty('rate', 150)
        elif system == 'Linux':
            engine.setProperty('rate', 174)


        engine.setProperty('rate', 174)
        engine.say(text)
        engine.runAndWait()  
    except Exception as e:
        logging.error(f"Error in TTS: {e}")
        eel.DisplayMessage("Text-to-speech failed.")


def takecommand():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        eel.DisplayMessage('listening....')
        logging.info("Listening for command...")
        recognizer.pause_threshold = 1
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source, timeout=10, phrase_time_limit=6)
            eel.DisplayMessage('Recognizing...')
            query = recognizer.recognize_google(audio, language= "en-in")
            eel.DisplayMessage(query)
            logging.info(f"Recognized command: {query} ")
            return query.lower()
        except sr.RequestError as e:
            eel.DisplayMessage("API unavailable. Check your connection. ")
            logging.error(f"API Error: {e}")
        except sr.UnknownValueError:
            eel.DisplayMessage("Sorry, I didn't catch that.")
            logging.warning("Speech not understood.")
        except Exception as e:
            eel.DisplayMessage("An unexpected error occured.")
            logging.error(f"Error: {e}")
        return ""

@eel.expose 
def allCommands():
    query = takecommand()  
    if query:
        speak(query)
        if "open" in query:
            if "YouTube" in query:
                eel.DisplayMessage("Opening Youtube.")
                speak ("Opening Youtube")
            elif "Google" in query:
                eel.DisplayMessage("Opening Google.")
                speak("Opening Google")
            else:
                eel.DisplayMessage("Specify what to open.")
                speak("Specify what to open")
        elif "exit" in query or "quit" in query:
            eel.DisplayMessage("Goodbye!")
            speak("Goodbye!")
            return
        else:
            eel.DisplayMessage("Command not recognized.")
            speak("Command not recognized.")
        eel.ShowHood()
    else :
        eel.DisplayMessage("No command detected. Try again.")