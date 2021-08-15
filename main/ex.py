import keyboard 

def tru():
    return 1
keyboard.add_hotkey("z",tru)

history=open('history.txt','w')

def save_pressed_keys(e):
    history.write(f"{e.name},{e.time}\n")

keyboard.hook(save_pressed_keys)
keyboard.wait(hotkey="z")
history.close()


