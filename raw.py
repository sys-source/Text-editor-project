from tkinter import *

theme = {"Dark theme": "#21201e", "Light theme": "#e3e0da"}
Output = "Text"
size = 25

window = Tk()     
window.geometry("900x600")                      
window.title("Goofy text editor")  
window.config(background=theme["Light theme"])

label = Label(window, text=Output, font=("Ariel", size, "bold"))
label.place(x=0, y=0)

window.mainloop()         
