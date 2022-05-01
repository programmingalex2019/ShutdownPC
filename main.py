#OS library
import os
#UI libraries
from tkinter import *
from tkinter import ttk

#Frame instance
win = Tk()

#Set frame size
win.geometry("750x300")

def receive():
    global entry
    inp = entry.get()
    if not inp.isdigit():
        error_label.configure(text="Please input a number greater than 0")
    else:
        error_label.configure(text="Success")
        os.system(f"shutdown -s -t {inp}")

#Program Label
label=Label(win, text="Select Time in milliseconds:", font="Courier 16 bold")
label.pack(pady=15)

#User Input
entry = Entry(win, width= 40)
entry.focus_set()
entry.pack()

#Button to validate
ttk.Button(win, text="Set", width=5, command=receive).pack(pady=15)

#Error text
error_label=Label(win, text="", font="Courier 15 bold")
error_label.pack(pady=15)

win.mainloop()

