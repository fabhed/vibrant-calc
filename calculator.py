import tkinter as tk
from button import Button

class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Calculator")
        self.display = tk.Entry(self.window, width=20)
        self.display.grid(row=0, column=0, columnspan=4)
        self.buttons = [
            Button("7", "red", self.append_to_display),
            Button("8", "orange", self.append_to_display),
            Button("9", "yellow", self.append_to_display),
            Button("4", "green", self.append_to_display),
            Button("5", "blue", self.append_to_display),
            Button("6", "indigo", self.append_to_display),
            Button("1", "violet", self.append_to_display),
            Button("2", "red", self.append_to_display),
            Button("3", "orange", self.append_to_display),
            Button("0", "yellow", self.append_to_display),
            Button("+", "green", self.append_to_display),
            Button("-", "blue", self.append_to_display),
            Button("*", "indigo", self.append_to_display),
            Button("/", "violet", self.append_to_display),
            Button("=", "red", self.calculate),
            Button("C", "orange", self.clear_display),
        ]
        for i, button in enumerate(self.buttons):
            button.widget.grid(row=i//4+1, column=i%4)

    def run(self):
        self.window.mainloop()

    def append_to_display(self, text):
        self.display.insert(tk.END, text)

    def clear_display(self):
        self.display.delete(0, tk.END)

    def calculate(self):
        try:
            result = eval(self.display.get())
            self.clear_display()
            self.append_to_display(str(result))
        except Exception:
            self.clear_display()
            self.append_to_display("Error")
