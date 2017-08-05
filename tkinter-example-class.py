import tkinter as tk


class MyWindow(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Hello, world")
        label.pack()

root = tk.Tk()
MyWindow(root).pack()
root.mainloop()


import tkinter as tk

root = tk.Tk()
topFrame = tk.Frame(root)
label = tk.Label(root, text="Hello, world")
label.pack()
topFrame.pack()

root.mainloop()