import tkinter as tk

root = tk.Tk()

root.title("Перша програма")
root.geometry("1024x768")

root.resizable(False, False)

label = tk.Label(root, text="Hello, world!", font=("Arial", 24))
label.pack(expand=True)

exit_button = tk.Button(root, text="Закрити", command=root.destroy, width=20, height=2)
exit_button.pack(pady=50)

root.mainloop()