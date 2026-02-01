import tkinter as tk

def save_data():
    name = entry_name.get()
    gender = gender_var.get()
    agreement = "Погоджуюсь" if agree_var.get() else "Не погоджуюсь"
    
    info = f"Ім'я: {name}\nСтать: {gender}\nУмови: {agreement}"
    label_result.config(text=info)


root = tk.Tk()
root.title("Анкета користувача")
root.geometry("400x350")

gender_var = tk.StringVar(value="Чоловіча")
agree_var = tk.BooleanVar()

tk.Label(root, text="Ім'я:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Стать:").grid(row=1, column=0, padx=10, pady=10, sticky="e")
tk.Radiobutton(root, text="Чоловіча", variable=gender_var, value="Чоловіча").grid(row=1, column=1, sticky="w")
tk.Radiobutton(root, text="Жіноча", variable=gender_var, value="Жіноча").grid(row=2, column=1, sticky="w")

check_agree = tk.Checkbutton(root, text="Погоджуюсь із умовами", variable=agree_var)
check_agree.grid(row=3, column=0, columnspan=2, pady=10)

btn_save = tk.Button(root, text="Зберегти", command=save_data, width=15)
btn_save.grid(row=4, column=0, columnspan=2, pady=10)

label_result = tk.Label(root, text="", font=("Arial", 10, "italic"), justify="left")
label_result.grid(row=5, column=0, columnspan=2, pady=10)

root.mainloop()