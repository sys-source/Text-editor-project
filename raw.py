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


LIGHT_THEME_SETTINGS_BUTTON_IMAGE = PhotoImage(file=r"Screenshot 2024-11-01 185621.png")    # Settings button (light theme)        
DARK_THEME_SETTINGS_BUTTON_IMAGE = PhotoImage(file=r"Screenshot 2024-11-01 191922.png")     # Settings button (dark theme)  

# Defining commands for buttons
def open_settings():
    # Creating the settings window 
    settings_label = Label(window, bg=dark_theme[2], width=90, height=55)
    settings_label.place(relx=0.5, rely=0.5, anchor=CENTER)

    # creating the settings heading
    settings_label_for_settings = Label(window, bg=dark_theme[2], fg=dark_theme[1], text="Settings", font=("Ink free", 33), width=10, height=2)
    settings_label_for_settings.place(relx=0.5, rely=0.15, anchor=CENTER)

    # creating the texts next to the buttons
    settings_label_for_font = Label(window, bg=dark_theme[2], fg=dark_theme[1], text="Font:", font=("Ink free", 23), width=10, height=1)
    settings_label_for_font.place(relx=0.38, rely=0.22)

    settings_label_for_font_size = Label(window, bg=dark_theme[2], fg=dark_theme[1], text="Font size:", font=("Ink free", 23), width=10, height=1)
    settings_label_for_font_size.place(relx=0.38, rely=0.45)

    settings_label_for_theme = Label(window, bg=dark_theme[2], fg=dark_theme[1], text="Theme:", font=("Ink free", 23), width=10, height=1)
    settings_label_for_theme.place(relx=0.38, rely=0.68)

    #Creating the buttons
    settings_button_for_font = Button(window, bg=dark_theme[0], text=size, fg=dark_theme[1], font=(30), height=2, width=20)
    settings_button_for_font.place(relx=0.56, rely=0.24, anchor=CENTER)

# Getting input (text on the screen)
def save_file():
    input = text.get("1.0", END)
    print(input)
    with open(os.getcwd() + '\ '+entry.get() + '.' + entry2.get() ,'a') as f:
                f.write(input)
                print(os.getcwd())
                print(input)

#ayo lock in this is the place where you insert file name \(-_-)/
entry = Entry()
entry.insert(0,'filename')
entry.config(width=20)
entry.pack()
entry2 = Entry()
entry2.insert(0,'ext')
entry2.config(width=8)
entry2.pack()


# Creating text area and showing it
text = Text(window, fg=dark_theme[1], bg=dark_theme[0],font=("Calibri", 25), padx=200, pady=100)
text.pack(expand=True, fill=BOTH)

# Creating a label at the bottom of the screen
bottom_label = Label(window, bg=dark_theme[2],padx=1000, pady=25)
bottom_label.place(relx=0, rely=0.958)

# Creating the settings button
settings_button = Button(window, command=open_settings, image=DARK_THEME_SETTINGS_BUTTON_IMAGE, width=70, height=36)
settings_button.place(relx=0, rely=0.959)

saving_files_button = Button(window, fg="black", text="save me!", command=save_file)
saving_files_button.place(x=0, y=0)

input = text.get("1.0", END)
print(input)

def on_press(key):
    global Output
    try:
        # If a printable character is pressed
        if hasattr(key, 'char') and key.char is not None:
            Output += key.char
        elif key == keyboard.Key.f5:
            save_file()
    except Exception as e:
        print(f"Error: {e}")
listener = keyboard.Listener(on_press=on_press)
listener.start()
# Looooooop
window.mainloop()