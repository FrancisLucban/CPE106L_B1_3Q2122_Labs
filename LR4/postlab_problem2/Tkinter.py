import tkinter as tk
from tkinter import filedialog as fd 
from tkinter import *

def openfile():
    tf = fd.askopenfilename() 
    txtarea.insert(END, tf)

ws = Tk()
ws.title("Group 7 Problem 2")
ws.geometry("400x450")
ws['bg']='#40E0D0'

txtarea = Text(ws, width=40, height=20)
txtarea.pack(pady=20)


tk.Button(text='Click to Open File', 
       command=openfile).pack(fill=tk.X)
tk.mainloop()