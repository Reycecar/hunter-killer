'''
Hunter Killer
@Author Reyce Salisbury
12/29/2023
'''
import pynput
mouse = pynput.mouse.Controller()

# If target hits enter, trigger hunter killer
def on_press(key):
    if key == pynput.keyboard.Key.enter:
        mouse.move(100000, -100000) # move mouse to top right corner once
        while True:
            mouse.click(pynput.mouse.Button.left, 10) # click infinite times lol
    

if __name__ == "__main__":
    with pynput.keyboard.Listener(on_press=on_press, on_release=None) as listener:
        while True:
            listener.run() # Start Listener