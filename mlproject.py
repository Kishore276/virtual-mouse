import tkinter as tk
from tkinter import *
from tkinter import ttk
import subprocess

win = tk.Tk()

win.title("Virtual Mouse")
win.geometry("300x220")

bg = PhotoImage(file='images.png')
label17 = Label(win, image=bg)
label17.place(x=40, y=0)

def hand():
    subprocess.Popen(["python", "hand.py"])  # Runs in a separate process

def handdetector():
    subprocess.Popen(["python", "eye.py"])  # Runs without stopping the main GUI

button = ttk.Button(win, text="Virtual Mouse Using Hand", command=hand)
button2 = ttk.Button(win, text="Virtual Mouse Using Eye", command=handdetector)
button.pack()
button2.pack()

win.mainloop()
