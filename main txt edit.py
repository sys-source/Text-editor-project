from tkinter import *
from tkinter import font
from tkinter import filedialog
import os

dark_theme = ["#21201e", "#e3e0da", "#131414"]
light_theme = ["#e3e0da", "#000000", "#babfbf"]
Output = ""
size = 25
file_path = os.getcwd()
current_font = "Default font"
available_fonts = list(font.families())
    
window = Tk()
window.geometry("900x600")                     
window.mainloop()       
LIGHT_THEME_SETTINGS_BUTTON_IMAGE = PhotoImage(file=r"Screenshot 2024-11-01 185621.png")    # Settings button (light theme)              
DARK_THEME_SETTINGS_BUTTON_IMAGE = PhotoImage(file=r"Screenshot 2024-11-01 191922.png")





class Settings:
    class Buttons:
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
        def close_settings():
            settings_label.destroy()
            settings_label_for_settings.destroy()
            settings_label_for_font_size.destroy()
            settings_label_for_font.destroy()
            settings_label_for_theme.destroy()
            settings_button_for_closing.destroy()
            settings_button_for_font.destroy()
            settings_button_for_font_size.destroy()
        global settings_label, settings_label_for_settings
        global settings_label_for_font_size, settings_label_for_font
        global settings_label_for_theme, settings_button_for_closing
        global settings_button_for_font, settings_button_for_font_size
        settings_label = Label(window, bg=dark_theme[2], width=90, height=55)
        settings_label_for_settings = Label(window, bg=dark_theme[2], fg=dark_theme[1], text="Settings", font=("Ink free", 33), width=10, height=2)
        settings_label_for_font = Label(window, bg=dark_theme[2], fg=dark_theme[1], text="Font:", font=("Ink free", 23), width=10, height=1)
        settings_label_for_font_size = Label(window, bg=dark_theme[2], fg=dark_theme[1], text="Font size:", font=("Ink free", 23), width=10, height=1)
        settings_label_for_theme = Label(window, bg=dark_theme[2], fg=dark_theme[1], text="Theme:", font=("Ink free", 23), width=10, height=1)
        settings_button_for_closing = Button(window, bg=dark_theme[2], text="×", font=("Ink free", 20), fg=dark_theme[1], width=5, height=2, borderwidth=0, activebackground=dark_theme[2], activeforeground=dark_theme[1], command=close_settings)
        settings_button_for_font = Button(window, bg=dark_theme[0], text=current_font, fg=dark_theme[1], font=(current_font, 15), height=2, width=20, activebackground=dark_theme[0], activeforeground=dark_theme[1], command=select_font)
        settings_button_for_font_size = Button(window, bg=dark_theme[0], text=size, fg=dark_theme[1], font=(current_font, 15), height=2, width=20, activebackground=dark_theme[0], activeforeground=dark_theme[1], command=change_font_size)
        def open_settings():
            settings_label.place(relx=0.5, rely=0.5, anchor=CENTER)
            settings_label_for_settings.place(relx=0.5, rely=0.15, anchor=CENTER)
            settings_label_for_font.place(relx=0.38, rely=0.22)
            settings_label_for_font_size.place(relx=0.38, rely=0.45)
            settings_label_for_theme.place(relx=0.38, rely=0.68)
            settings_button_for_closing.place(relx=0.624, rely=0.09)
            settings_button_for_font.place(relx=0.55, rely=0.24, anchor=CENTER)
            settings_button_for_font_size.place(relx=0.55, rely=0.47, anchor=CENTER)

            

class Window_Widgets:
    ...                        

class Input:
    ... # While looooop waits for input

class Output:
    ... # Takes Input or File I/O  and prints it out 

class Saver:
    ... # when programm gets closed reads all the stuff on the screen and takes all the settings and saves them File I/O
    
    
