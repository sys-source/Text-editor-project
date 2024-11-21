from tkinter import *
from tkinter import font
from tkinter import filedialog
from pynput import keyboard
import os

# Main variebles
dark_theme = ["#21201e", "#e3e0da", "#131414"]
light_theme = ["#e3e0da", "#000000", "#babfbf"]
Output = ""
size = 25
file_path = os.getcwd()
current_font = "Default font"


window = Tk()
window.title("Goofy ahh text editor")

available_fonts = list(font.families())


LIGHT_THEME_SETTINGS_BUTTON_IMAGE = PhotoImage(file=r"C:\Users\anmar\Downloads\Screenshot 2024-11-01 185621.png")    # Settings button (light theme)              
DARK_THEME_SETTINGS_BUTTON_IMAGE = PhotoImage(file=r"C:\Users\anmar\Downloads\Screenshot 2024-11-01 191922.png")     # Settings button (dark theme)
# Defining commands for buttons

def close_settings():
    # Destroy each widget created in the open_settings function
    settings_label.destroy()
    settings_label_for_settings.destroy()
    settings_label_for_font_size.destroy()
    settings_label_for_font.destroy()
    settings_label_for_theme.destroy()
    settings_button_for_closing.destroy()
    settings_button_for_font.destroy()

def select_font():
    def update_font(event):
        global current_font
        global text
        current_font = font_box.get(font_box.curselection())
        font_box.destroy()
        close_settings()
        open_settings()
        print(current_font)
        text.config(font=(current_font, 25))

    index = 0
    font_box = Listbox(window, width=37, bg=dark_theme[0], fg=dark_theme[1])
    for i in available_fonts:
        font_box.insert(index, i)
        index += 1
    font_box.place(relx=0.491, rely=0.27)
    font_box.bind("<<ListboxSelect>>", update_font)

def change_font_size():
    pass

def open_settings():
    global settings_label, settings_label_for_settings
    global settings_label_for_font_size, settings_label_for_font
    global settings_label_for_theme, settings_button_for_closing
    global settings_button_for_font

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
    settings_button_for_closing = Button(window, bg=dark_theme[2], text="×", font=("Ink free", 20), fg=dark_theme[1], width=5, height=2, borderwidth=0, activebackground=dark_theme[2], activeforeground=dark_theme[1], command=close_settings)
    settings_button_for_closing.place(relx=0.624, rely=0.09)

    settings_button_for_font = Button(window, bg=dark_theme[0], text=current_font, fg=dark_theme[1], font=(current_font, 15), height=2, width=20, activebackground=dark_theme[0], activeforeground=dark_theme[1], command=select_font)
    settings_button_for_font.place(relx=0.55, rely=0.24, anchor=CENTER)

    settings_button_for_font_size = Button(window, bg=dark_theme[0], text=size, fg=dark_theme[1], font=(current_font, 15), height=2, width=20, activebackground=dark_theme[0], activeforeground=dark_theme[1], command=change_font_size)
    settings_button_for_font_size.place(relx=0.55, rely=0.47, anchor=CENTER)



# Getting input (text on the screen)
def save_file():
    input = text.get("1.0", END)
    print(input)
    if file_path == os.getcwd():
        with open(file_path + '\ '+entry.get() + '.' + entry2.get() ,'a') as f:
                    f.write(input)
                    print(os.getcwd())
                    print(input)
    if file_path != os.getcwd():
                with open(file_path,'w') as f:
                    f.write(input)
                    print(os.getcwd())
                    print(input)
#ligma check this out
def ask_open_file():
    file_path = filedialog.askopenfilename(title="Select a File")
    with open(file_path,'r') as f:
            text.delete("1.0", END)
            text.insert(END, ''.join(f.readlines()))


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
text = Text(window, fg=dark_theme[1], bg=dark_theme[0], font=(current_font, 25), padx=200, pady=100)
text.pack(expand=True, fill=BOTH)

# Creating a label at the bottom of the screen
bottom_label = Label(window, bg=dark_theme[2],padx=1000, pady=25)
bottom_label.place(relx=0, rely=0.958)

# Creating the settings button
settings_button = Button(window, command=open_settings, image=DARK_THEME_SETTINGS_BUTTON_IMAGE, width=70, height=36)
settings_button.place(relx=0, rely=0.959)

saving_files_button = Button(window, fg="black", text="save me!", command=save_file)
saving_files_button.place(x=0, y=0)

opening_files_button = Button(window, fg="black", text="open a file", command=ask_open_file)
opening_files_button.place(x=60, y=0)
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




# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⣤⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⠿⠿⠿⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣶⣿⣿⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⡟⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣶⣾⣿⣶⣶⣤⡀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⠘⢿⣿⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀
# ⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠈⠻⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀
# ⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⣀⣤⣶⣶⣌⠻⣿⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀
# ⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⠁⣰⣿⣿⣿⣿⣿⣦⡙⢿⣿⣿⣿⠄⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⠀⣿⣿⣿⣿⣿⣿⣿⣿⣦⣙⣛⣋⣼⣿⣿⣶⣿⣿⣿⣿⣿⣿⣯⡉⠉⠉⠁⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⡆⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⡇⠀⢻⣿⣿⣿⣿⣿⡇⠀⠀⠈⠉⠉⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀
# ⠀⣠⣴⣶⣶⣶⣶⣶⣶⣾⣿⣿⣿⣿⣿⡇⠀⠸⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠹⢿⣿⣿⢿⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀
# ⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢰⣶⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣧⣄⣀⣀⣀⣀⣀⣀⡀
# ⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢸⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿

