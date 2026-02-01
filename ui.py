import tkinter as tk
from logic import process_text, calculate_length

class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Модульна програма")
        self.root.geometry("400x300")
        
        tk.Label(root, text="Введіть текст для обробки:", font=("Arial", 10)).pack(pady=10)
        
        self.entry = tk.Entry(root, width=40)
        self.entry.pack(pady=5)
        
        self.btn = tk.Button(root, text="Обробити", command=self.on_click)
        self.btn.pack(pady=10)
        
        self.result_label = tk.Label(root, text="", font=("Courier", 11, "bold"), fg="darkblue")
        self.result_label.pack(pady=20)

    def on_click(self):
        user_input = self.entry.get()
        result = process_text(user_input)
        length = calculate_length(user_input)
        
        self.result_label.config(text=f"Результат: {result}\nДовжина: {length}")