import os 
import eel

from engine.features import *
from engine.command import *

eel.init("www")

def launch_app():
    try:
        print("Playing startup sound...")
        playAssistantSound()

        print ("Launching A DATA Assistant web app... ")
        eel.start ('index.html', mode ="chrome", host= '127.0.0.1', port=5500, block=True)
    except Exception as e:
        print(f"Error launching app: {e}")
        fallback_launch()

def fallback_launch():
    try:
        print("Fallback: Launching in non-GUI mode.")
        eel.start('index.html', block = True)
    except Exception as e:
        print(f"Error launching fallback mode : {e}")

def is_port_available(port):
    import socket 
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(('127.0.0.1', port)) != 0

if __name__ == "__main__":
    print("Starting A DATA Assistant...")

    port =5500
    if not is_port_available(port):
        print(f"Port {port} is unavailable. Please choose a different port ")
    else:
        launch_app()