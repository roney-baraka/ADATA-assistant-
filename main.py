import os 
import eel

from engine.features import *
from engine.command import *

eel.init("www")

def launch_app():
    try:
        eel.start ('index.html', mode ="chrome", host= '127.0.0.1', port=5500, block=True)
    except Exception as e:
        print(f"Error launching app: {e}")

if __name__ == "__main__":
    print("Starting A DATA Assistant...")

    try:
        playAssistantSound()
    except Exception as e:
        print(f"Error playing startup sound: {e}")
    launch_app()