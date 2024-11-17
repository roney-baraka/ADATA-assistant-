from playsound import playsound
import eel
import os 

# Playing assistant sound function

@eel.expose
def playAssistantSound():
    try:
        music_dir = os.path.join("www", "assets", "audio", "www_assets_audio_start_sound.mp3")
        if os.path.exists(music_dir):
            playsound(music_dir)
        else:
            print("Sound file not found.")
            eel.DisplayMessage("Sound file not found.")
    except Exception as e:
        print (f"Error playing sound: {e}")
        eel.DisplayMessage("Error playing sound.")