import os 
import eel

eel.init("www")
os.system('open -a "Google Chrome" "http://127.0.0.1:5500/index.html"')

eel.start('index.html', mode=None, host='127.0.0.1', port=5500, block=True) 