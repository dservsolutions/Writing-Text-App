from tkinter import *
import tkinter as tk
from tkinter import messagebox

# Windows Configuration
window = tk.Tk()
window.title("Writing Text App")

# Functions
def greeting():
    if  name_entry != " ":
        messagebox.showinfo("Info", f"Welcome {name_entry.get()}")
        name_entry.delete(0,tk.END)
        name_entry.focus()
    else:
        messagebox.showwarning("Error", f"Please enter your name.")
        pass


# Setting the windows size to 500x300
window.geometry("800x600")

# Settings
name_label = tk.Label(window, text="Enter your name: ", wraplength=400, justify="left")
name_label.pack(pady=10)
name_entry = tk.Entry(window, width=25)
name_entry.pack(pady=10)
name_button = tk.Button(window, text="OK", command=functions.greeting)
name_button.pack(pady=10)





if __name__ == '__main__':
    window.mainloop()

