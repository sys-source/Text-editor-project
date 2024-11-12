from tkinter import *
from pynput import keyboard
import os
# Main variebles
dark_theme = ["#21201e", "#e3e0da", "#131414"]
light_theme = ["#e3e0da", "#000000", "#babfbf"]
Output = ""
size = 25

window = Tk()
window.title("Goofy ahh text editor")


LIGHT_THEME_SETTINGS_BUTTON_IMAGE = PhotoImage(file="Screenshot 2024-11-01 191922.png")    # Settings button (light theme)        
DARK_THEME_SETTINGS_BUTTON_IMAGE = PhotoImage(file="Screenshot 2024-11-01 185621.png")     # Settings button (dark theme)  

# Defining commands for buttons
def open_settings():
    settings_label = Label(window, bg=dark_theme[2], padx=300, pady=400)
    settings_label.place(relx=0.5, rely=0.5, anchor=CENTER)




        
        
        
# Start the keyboard listener

# Creating text area and showing it
text = Text(window, fg=dark_theme[1], bg=dark_theme[0],font=("Calibri", 25), padx=200, pady=100)
text.pack(expand=True, fill=BOTH)

# Creating a label at the bottom of the screen
bottom_label = Label(window, bg=dark_theme[2],padx=1000, pady=25)
bottom_label.place(x=0, y=975)

# Creating settings button
settings_button = Button(window, command=open_settings, image=DARK_THEME_SETTINGS_BUTTON_IMAGE)

# Getting input (text on the screen)
input = text.get("1.0", END)


def on_press(key):
    global Output
    try:
        # If a printable character is pressed
        if hasattr(key, 'char') and key.char is not None:
            Output += key.char
        elif key == keyboard.Key.f5:
            with open(os.getcwd() + '\ luanonna.txt' ,'a') as f:
                f.write(input)
                print(os.getcwd())
                print(input)

    except Exception as e:
        print(f"Error: {e}")
listener = keyboard.Listener(on_press=on_press)
listener.start()
# Looooooop
window.mainloop()