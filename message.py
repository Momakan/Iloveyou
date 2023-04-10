import tkinter as tk
from tkinter import messagebox

def show_message():
    messagebox.showinfo("Message", "I love you!")

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    show_message()
    root.mainloop()
