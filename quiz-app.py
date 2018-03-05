# Simple Quiz GUI app
# Create a question and multiple choice options of which one is correct
# When correct option is clicked a message displays that option is correct!

from tkinter import *
import tkinter.messagebox

# keep the question in a separate json file
q = [
    "Capital of India",
    "South most city in India",
]

options = [
    ["Delhi", "Mumbai", "Kolkata", "Chennai"],
    ["Delhi", "Mumbai", "Chennai", "Kanyakumari"],
]

a = [1, 4]

class Quiz:
    def __init__(self, master):
        self.opt_selected = IntVar()
        self.qn = 0
        self.correct = 0
        self.ques = self.create_q(master, self.qn)
        self.opts = self.create_options(master, 4)
        self.display_q(self.qn)
        self.status_bar = self.create_status_bar(master)
        self.create_nav(master)

    def create_status_bar(self, master):
        status_bar = Label(master, text="Click an answer...", bd=1, relief=SUNKEN, anchor=W)
        status_bar.pack(side=BOTTOM, fill=X)
        return status_bar

    def create_nav(self, master):
        button = Button(master, text="Back", command=self.back_btn)
        button.pack(side=BOTTOM)
        button = Button(master, text="Next", command=self.next_btn)
        button.pack(side=BOTTOM)
        quit_button = Button(master, text="Quit", command=master.quit)
        quit_button.pack(side=BOTTOM)


    def create_q(self, master, qn):
        w = Label(master, text=q[qn])
        w.pack(side=TOP)
        return w

    def create_options(self, master, n):
        b_val = 0
        b = []
        while b_val < n:
            btn = Radiobutton(master, text="foo", variable=self.opt_selected, value=b_val+1)
            b.append(btn)
            btn.pack(side=TOP, anchor="w")
            b_val = b_val + 1
        return b

    def display_q(self, qn):
        b_val = 0
        self.opt_selected.set(0)
        self.ques['text'] = q[qn]
        for op in options[qn]:
            self.opts[b_val]['text'] = op
            b_val = b_val + 1

    def check_q(self, qn):
        if self.opt_selected.get() == a[qn]:
            return True
        return False

    def print_results(self):
        result = "Score: " + str(self.correct) + "/" + str(len(q))
        tkinter.messagebox.showinfo("Final Result", result)
        print("Score: ", self.correct, "/", len(q))

    def back_btn(self):
        print("go back")

    def next_btn(self):
        if self.check_q(self.qn):
            self.status_bar['text'] = "Correct"
            self.correct += 1
        else:
            self.status_bar['text'] = "Wrong"
        self.qn = self.qn + 1
        if self.qn >= len(q):
            self.print_results()
        else:
            self.display_q(self.qn)


root = Tk()
root.geometry("500x300")
app = Quiz(root)
root.mainloop()

# TODO: Shuffle answers (Random shuffle of a list)
# TODO: Display the answer on the GUI
