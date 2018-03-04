# Binding function for action
import tkinter as tk

w = tk.Tk()

def clicked(event):
    print("Button was clicked")

b = tk.Button(w, text="Click")

b.bind("<Button-3>", clicked)

b.pack()
w.mainloop()


m = tk.Menu(w)
w.config(menu=m)

submenu = tk.Menu(m)
m.add_cascade(label="File", menu=submenu)
submenu.add_command(label="New Project", command=clicked)
submenu.add_command(label="Files", command=clicked)
submenu.add_separator()
submenu.add_command(label="Exit", command=clicked)

submenu2 = tk.Menu(m)
m.add_cascade(label="File", menu=submenu2)
