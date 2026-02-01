import tkinter as tk
from tkinter import ttk, colorchooser
import os

CONFIG_FILE = "settings.txt"

def save_color(color):
    with open(CONFIG_FILE, "w") as f:
        f.write(color)

def load_color():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as f:
            return f.read().strip()
    return "#f0f0f0" 

def choose_color():

    color = colorchooser.askcolor(title="Оберіть колір фону")[1]
    if color:
        apply_color(color)
        save_color(color)

def apply_color(color):

    style.configure("TFrame", background=color)
    tab1.configure(bg=color)
    tab2.configure(bg=color)
    tab3.configure(bg=color)

root = tk.Tk()
root.title("Розширений інтерфейс")
root.geometry("500x400")

style = ttk.Style()
style.theme_use('clam')

notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill="both")

tab1 = tk.Frame(notebook)
tab2 = tk.Frame(notebook)
tab3 = tk.Frame(notebook)

notebook.add(tab1, text="Головна")
notebook.add(tab2, text="Налаштування")
notebook.add(tab3, text="Про програму")

tk.Label(tab1, text="Введіть дані:", font=("Arial", 12)).pack(pady=10)
tk.Entry(tab1, width=30).pack(pady=5)
tk.Button(tab1, text="Надіслати", width=15).pack(pady=10)

tk.Label(tab2, text="Персоналізація інтерфейсу", font=("Arial", 12)).pack(pady=20)
tk.Button(tab2, text="Змінити колір фону", command=choose_color).pack(pady=10)

about_text = "Автор: Студент групи ІПЗ-33\nВерсія: 1.0\nДата: 2026 рік"
tk.Label(tab3, text=about_text, font=("Arial", 10), justify="center").pack(expand=True)

saved_color = load_color()
apply_color(saved_color)

root.mainloop()