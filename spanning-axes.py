# Controlling layout of widgets using pack
import tkinter as tk

w = tk.Tk()
b1 = tk.Button(w, text="button1", bg="red")
b1.pack()
b2 = tk.Button(w, text="button2", bg="white")
b2.pack(fill=tk.X)
b3 = tk.Button(w, text="button3", bg="green")
b3.pack(fill=tk.Y, side=tk.RIGHT)

w.mainloop()
