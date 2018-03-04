# Menu item for a GUI (menu, cascade, command)
import tkinter as tk

def clicked():
    print("Button was clicked")

w = tk.Tk()
m = tk.Menu(w)
w.config(menu=m)
submenu_file = tk.Menu(m)
submenu_edit = tk.Menu(m)
m.add_cascade(label="File", menu=submenu_file)
m.add_cascade(label="Edit", menu=submenu_edit)
submenu_file.add_command(label="New Project", command=clicked)
submenu_file.add_command(label="Open", command=clicked)
submenu_file.add_separator()
submenu_file.add_command(label="Settings", command=clicked)

submenu_edit.add_command(label="Copy", command=clicked)

w.mainloop()
