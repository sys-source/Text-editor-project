from tkinter import *

# Main variebles
dark_theme = ["#21201e", "#e3e0da", "#131414"]
light_theme = ["#e3e0da", "#000000", "#babfbf"]
Output = ""
size = 25
LIGHT_THEME_SETTINGS_BUTTON_IMAGE = PhotoImage(file=...)    # Settings button light theme        
DARK_THEME_SETTINGS_BUTTON_IMAGE = PhotoImage(file=...)     # Settings button dark theme  

# Defining commands for buttons
def open_settings():
    settings_label = Label(window, bg=dark_theme[2], padx=300, pady=400)
    settings_label.place(relx=0.5, rely=0.5, anchor=CENTER)

# Creating window
window = Tk()
window.title("Goofy ahh text editor")

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

# Looooooop
window.mainloop()


# Note the code is not usable in this form in order to run the code you need to make setting button and it´s veriebles a comment !!!
