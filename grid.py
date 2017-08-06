# Controlling layout of widgets using grid
import tkinter as tk

w = tk.Tk()
l1 = tk.Label(w, text="Enter your Username:")
l2 = tk.Label(w, text="Password:")
e1 = tk.Entry(w)
e2 = tk.Entry(w)

l1.grid(row=0, column=0)
l2.grid(row=1, column=0, sticky=tk.E)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

w.mainloop()
