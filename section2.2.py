import tkinter as tk

def say_hello():
    main_label.config(text="Вітаю, користувач!")

def clear_text():
    main_label.config(text="")


root = tk.Tk()
root.title("Керування подіями")
root.geometry("400x300")

main_label = tk.Label(root, text="", font=("Verdana", 14), fg="blue")
main_label.pack(pady=30)

btn_greet = tk.Button(root, text="Привітати", command=say_hello, width=15)
btn_greet.pack(pady=5)

btn_clear = tk.Button(root, text="Очистити", command=clear_text, width=15)
btn_clear.pack(pady=5)

btn_exit = tk.Button(root, text="Вийти", command=root.destroy, width=15)
btn_exit.pack(pady=5)

root.mainloop()