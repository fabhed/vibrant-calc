import tkinter as tk

class Button:
    def __init__(self, text, color, command):
        self.widget = tk.Button(text=text, bg=color, command=lambda: command(text))
