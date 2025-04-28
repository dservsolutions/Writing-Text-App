import tkinter as tk

class KeepTypingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Keep Typing or Restart!")

        self.text = tk.Text(root, width=50, height=20, font=("Arial", 14))
        self.text.pack(padx=10, pady=10)

        # Bind any key press to reset the timer
        self.text.bind("<Key>", self.reset_timer)

        self.timeout = 2000  # 2 seconds
        self.timer = None
        self.start_timer()

    def start_timer(self):
        self.timer = self.root.after(self.timeout, self.clear_text)

    def reset_timer(self, event=None):
        if self.timer:
            self.root.after_cancel(self.timer)
        self.start_timer()

    def clear_text(self):
        self.text.delete("1.0", tk.END)
        self.start_timer()  # Restart timer after clearing

if __name__ == "__main__":
    root = tk.Tk()
    app = KeepTypingApp(root)
    root.mainloop()