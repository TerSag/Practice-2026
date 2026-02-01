import tkinter as tk
from tkinter import filedialog, messagebox

class Notepad:
    def __init__(self, root):
        self.root = root
        self.root.title("Мій Блокнот")
        self.root.geometry("600x400")
        
        self.text_area = tk.Text(self.root, undo=True)
        self.text_area.pack(expand=True, fill="both")
        
        self.menu_bar = tk.Menu(self.root)
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        
        self.file_menu.add_command(label="Відкрити", command=self.open_file)
        self.file_menu.add_command(label="Зберегти", command=self.save_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Вийти", command=self.confirm_exit)
        
        self.menu_bar.add_cascade(label="Файл", menu=self.file_menu)
        self.root.config(menu=self.menu_bar)
        
        self.root.protocol("WM_DELETE_WINDOW", self.confirm_exit)
        self.last_saved_content = ""

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(1.0, content)
                self.last_saved_content = content

    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt")
        if file_path:
            content = self.text_area.get(1.0, tk.END)
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)
            self.last_saved_content = content

    def confirm_exit(self):
        current_content = self.text_area.get(1.0, tk.END)
        if current_content.strip() != self.last_saved_content.strip():
            if messagebox.askyesno("Вихід", "Ви маєте незбережені зміни. Бажаєте вийти?"):
                self.root.destroy()
        else:
            self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = Notepad(root)
    root.mainloop()