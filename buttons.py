# Controlling the layout using frames
import tkinter as tk

w = tk.Tk()
f1 = tk.Frame(w)
f2 = tk.Frame(w)

f1.pack(side=tk.TOP)
f2.pack(side=tk.BOTTOM)


b1 = tk.Button(f1, text="b1", fg="blue")
b2 = tk.Button(f1, text="b2", bg="red")
b3 = tk.Button(f1, text="b3")
b4 = tk.Button(f2, text="b4")


b2.pack(side=tk.LEFT)
b1.pack(side=tk.LEFT)
b3.pack(side=tk.LEFT)
b4.pack()

w.mainloop()
