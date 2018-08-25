'''
Create simple canvas using Tkinter gui
'''
import tkinter
from tkinter import Canvas

top = tkinter.Tk()

c = Canvas(bg="#80deea", cursor='circle',
           highlightcolor="#ff5722", height=300, width=500)

c.pack()
top.mainloop()
