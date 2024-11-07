from tkinter import *
from pynput import keyboard

theme = {"Dark theme": "#21201e", "Light theme": "#e3e0da"}
Output = ""
size = 25

window = Tk()
window.geometry("900x600")
window.title("Goofy ahh text editor")
window.config(background=theme["Light theme"])

label = Label(window, text=Output, font=("Ariel", size, "bold"))
label.place(x=0, y=0)

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
        label.config(text=Output)
    except Exception as e:
        print(f"Error: {e}")

# Start the keyboard listener
listener = keyboard.Listener(on_press=on_press)
listener.start()

window.mainloop()
listener.stop()
