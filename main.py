from tkinter import *
import tkinter as tk

# Windows Configuration
window = tk.Tk()
window.title("Writing Text App")

# Setting the windows size to 500x300
window.geometry("800x600")

name_label = tk.Label(window, text="Enter your name: ", wraplength=400, justify="left")
name_label.pack(pady=5)

if __name__ == '__main__':
    window.mainloop()

