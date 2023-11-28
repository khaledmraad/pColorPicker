import tkinter as tk
from tkinter import colorchooser

import pyautogui as pg

def pick_color():
    color = colorchooser.askcolor()[1]  
    if color:
        color_label.config(foreground=color)  
        

window = tk.Tk()
window.title("Python Color Picker")

color_label = tk.Label(window, text="this is your color", font=("Helvetica", 18))
color_label.pack(pady=20)

color_picker = tk.Button(window, text="Pick a Color", command=pick_color)
color_picker.pack()


window.mainloop()
