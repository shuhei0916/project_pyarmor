# import pyarmor_runtime
import tkinter as tk
from tkinter import messagebox
from dist import common
from dist import tom
from common import *

# tom.hi()

def hehe():
    try:
        check_expiration()
    except:
        messagebox.showerror("Error", error_message)

root = tk.Tk()
root.title("Hello World App")
label = tk.Label(root, text="Hello, World!")
label.pack(padx=20, pady=20)

button = tk.Button(root, text="push", command=hehe)
button.pack()

root.mainloop()