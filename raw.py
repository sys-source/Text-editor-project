from tkinter import *
from tkinter import font
from tkinter import filedialog
from pynput import keyboard
import os

# Main variebles
dark_theme = ["#21201e", "#e3e0da", "#131414", "Dark theme"]
light_theme = ["#e3e0da", "#000000", "#626664", "Light theme"]
current_theme = dark_theme
Output = ""
size = 25
file_path = os.getcwd()
current_font = "Default font"
allowed = True


window = Tk()
window.title("Goofy ahh text editor")

available_fonts = list(font.families())


LIGHT_THEME_SETTINGS_BUTTON_IMAGE = PhotoImage(file=r"C:\Users\anmar\Downloads\Screenshot 2024-11-01 185621.png")    # Settings button (light theme)              
DARK_THEME_SETTINGS_BUTTON_IMAGE = PhotoImage(file=r"C:\Users\anmar\Downloads\Screenshot 2024-11-01 191922.png")     # Settings button (dark theme)

# Defining commands for buttons

def close_settings():
    global allowed
    settings_label.destroy()
    settings_label_for_settings.destroy()
    settings_label_for_font_size.destroy()
    settings_label_for_font.destroy()
    settings_label_for_theme.destroy()
    settings_button_for_closing.destroy()
    settings_button_for_font.destroy()
    settings_button_for_font_size.destroy()
    settings_button_for_theme.destroy()
    settings_button.config(state=ACTIVE)

    allowed = True
    

def select_font():
    def update_font(event):
        global current_font
        global text
        current_font = font_box.get(font_box.curselection())
        font_box.destroy()
        close_settings()
        open_settings()
        text.config(font=(current_font))

    index = 0
    font_box = Listbox(window, width=37, bg=current_theme[0], fg=current_theme[1])
    for i in available_fonts:
        font_box.insert(index, i)
        index += 1
    font_box.place(relx=0.491, rely=0.27)
    font_box.bind("<<ListboxSelect>>", update_font)

def select_font_size():
    def update_font_size(event):
        global size
        global text
        size = font_size_box.get(font_size_box.curselection())
        font_size_box.destroy()
        close_settings()
        open_settings()
        text.config(font=(current_font, size))
    
    index = 0
    font_size_box = Listbox(window, width=37, bg=current_theme[0], fg=current_theme[1])
    for i in range(1,50):
        font_size_box.insert(index, i)
        index += 1
    font_size_box.place(relx=0.491, rely=0.50)
    font_size_box.bind("<<ListboxSelect>>", update_font_size)

def select_theme():
    def update_theme(event):
        global settings_button
        global bottom_label
        global current_theme
        global text
        theme = font_theme_box.get(font_theme_box.curselection())
        if theme == "Dark theme":
            theme = dark_theme
            settings_button.config(image=DARK_THEME_SETTINGS_BUTTON_IMAGE)
        else:
            theme = light_theme
            settings_button.config(image=LIGHT_THEME_SETTINGS_BUTTON_IMAGE)
        font_theme_box.destroy()
        current_theme = theme
        close_settings()
        open_settings()
        text.config(bg=current_theme[0], fg=current_theme[1])
        bottom_label.config(bg=current_theme[2])
    
    font_theme_box = Listbox(window, width=37, bg=current_theme[0], fg=current_theme[1])
    font_theme_box.config(height=font_theme_box.size())
    font_theme_box.insert(0, "Dark theme")
    font_theme_box.insert(1, "Light theme")
    font_theme_box.place(relx=0.491, rely=0.73)
    font_theme_box.bind("<<ListboxSelect>>", update_theme)

def open_settings():
    global allowed
    if allowed == True:
        allowed = False

        global settings_label, settings_label_for_settings
        global settings_label_for_font_size, settings_label_for_font
        global settings_label_for_theme, settings_button_for_closing
        global settings_button_for_font, settings_button_for_font_size
        global settings_button_for_theme
        global settings_button


        # Creating the settings window 
        settings_label = Label(window, bg=current_theme[2], width=90, height=55)
        settings_label.place(relx=0.5, rely=0.5, anchor=CENTER)

        # creating the settings heading
        settings_label_for_settings = Label(window, bg=current_theme[2], fg=current_theme[1], text="Settings", font=("Ink free", 33), width=10, height=2)
        settings_label_for_settings.place(relx=0.5, rely=0.15, anchor=CENTER)

        # creating the texts next to the buttons
        settings_label_for_font = Label(window, bg=current_theme[2], fg=current_theme[1], text="Font:", font=("Ink free", 23), width=10, height=1)
        settings_label_for_font.place(relx=0.38, rely=0.22)

        settings_label_for_font_size = Label(window, bg=current_theme[2], fg=current_theme[1], text="Font size:", font=("Ink free", 23), width=10, height=1)
        settings_label_for_font_size.place(relx=0.38, rely=0.45)

        settings_label_for_theme = Label(window, bg=current_theme[2], fg=current_theme[1], text="Theme:", font=("Ink free", 23), width=10, height=1)
        settings_label_for_theme.place(relx=0.38, rely=0.68)


        #Creating the buttons
        settings_button_for_closing = Button(window, bg=current_theme[2], text="×", font=("Ink free", 20), fg=current_theme[1], width=5, height=2, borderwidth=0, activebackground=current_theme[2], activeforeground=current_theme[1], command=close_settings)
        settings_button_for_closing.place(relx=0.624, rely=0.09)

        settings_button_for_font = Button(window, bg=current_theme[0], text=current_font, fg=current_theme[1], font=(current_font, 15), height=2, width=20, activebackground=current_theme[0], activeforeground=current_theme[1], command=select_font)
        settings_button_for_font.place(relx=0.55, rely=0.24, anchor=CENTER)

        settings_button_for_font_size = Button(window, bg=current_theme[0], text=size, fg=current_theme[1], font=(current_font, 15), height=2, width=20, activebackground=current_theme[0], activeforeground=current_theme[1], command=select_font_size)
        settings_button_for_font_size.place(relx=0.55, rely=0.47, anchor=CENTER)

        settings_button_for_theme = Button(window, bg=current_theme[0], text=current_theme[3], fg=current_theme[1], font=(current_font, 15), height=2, width=20, activebackground=current_theme[0], activeforeground=current_theme[1], command=select_theme)
        settings_button_for_theme.place(relx=0.55, rely=0.70, anchor=CENTER)



# Getting input (text on the screen)
def save_file():
    def save_filee(entry, entry2):
        global file_path  # Use the global variable to ensure changes persist
        input_text = text.get("1.0", END).strip()  # Get the text and strip trailing newlines
        if not input_text:
            print("No text to save!")
            return
        
        # Ensure file_path is valid
        if not file_path:
            file_path = os.getcwd()  # Default to current working directory
        
        # Get filename and extension from entries
        filename = entry.get().strip()
        extension = entry2.get().strip()
        
        if not filename or not extension:
            print("Filename or extension is missing!")
            return
        
        # Construct the full file path
        full_path = os.path.join(file_path, f"{filename}.{extension}")
        
        try:
            with open(full_path, 'w') as file:
                file.write(input_text)
            print(f"File saved successfully at {full_path}")
            saving_files_window.destroy()
        except Exception as e:
            print(f"Error saving file: {e}")

    saving_files_window = Toplevel()
    entry = Entry(saving_files_window, width=30)
    entry.insert(0,'filename')
    entry.pack()
    entry2 = Entry(saving_files_window, width=18)
    entry2.insert(0,'ext')
    entry2.pack()
    def save_fileee():
        save_filee(entry, entry2)
    saving_button = Button(saving_files_window, text="Save", height=2, width=12, command=save_fileee)
    saving_button.pack()

#ligma check this out
def ask_open_file():
    global file_path
    file_path = filedialog.askopenfilename(title="Select a File")
    with open(file_path,'r') as f:
            text.delete("1.0", END)
            text.insert(END, ''.join(f.readlines()))




# Creating text area and showing it
text = Text(window, fg=current_theme[1], bg=current_theme[0], font=(current_font, 25), padx=200, pady=100)
text.pack(expand=True, fill=BOTH)

# Creating a label at the bottom of the screen
bottom_label = Label(window, bg=current_theme[2],padx=1000, pady=25)
bottom_label.place(relx=0, rely=0.958)

# Creating the settings button
settings_button = Button(window, command=open_settings, image=DARK_THEME_SETTINGS_BUTTON_IMAGE, width=70, height=36)
settings_button.place(relx=0, rely=0.959)

saving_files_button = Button(window, fg="black", text="save me!", command=save_file)
saving_files_button.place(x=0, y=0)

opening_files_button = Button(window, fg="black", text="open a file", command=ask_open_file)
opening_files_button.place(x=60, y=0)
input = text.get("1.0", END)

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

