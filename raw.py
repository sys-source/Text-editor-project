from tkinter import *
from pynput import keyboard

# Main variebles
dark_theme = ["#21201e", "#e3e0da", "#131414"]
light_theme = ["#e3e0da", "#000000", "#babfbf"]
Output = ""
size = 25

window = Tk()
window.geometry("900x600")
window.title("Goofy ahh text editor")
window.config(background=light_theme[0]) 

label = Label(window, text=Output+"|", font=("Ariel", size, "bold"), fg=light_theme[1], bg=light_theme[0])
label.place(x=0, y=0)

settings_button = Button()

# Function to handle key press events
def on_press(key):
    global Output
    try:
        # If a printable character is pressed
        if hasattr(key, 'char') and key.char is not None:
            Output += key.char
        elif key == keyboard.Key.space:
            Output += ' '
        elif key == keyboard.Key.enter:
            Output += '\n'
        elif key == keyboard.Key.backspace:
            Output = Output[:-1]  # Remove the last character
        
        # Update the label with new text
        label.config(text=Output+"|")
    except Exception as e:
        print(f"Error: {e}")

# Start the keyboard listener
listener = keyboard.Listener(on_press=on_press)
listener.start()

window.mainloop()
listener.stop()
