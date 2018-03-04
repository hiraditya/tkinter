# Getting started with tkinter (tcl/tk)
# GUI = graphical user interface

import tkinter as tk

#widget is like canvas
w = tk.Tk()
l = tk.Label(w, text="Hello world")
l.pack()

# event loop
w.mainloop()
