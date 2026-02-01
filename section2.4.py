import tkinter as tk

def calculate(operation):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        
        if operation == "+":
            res = num1 + num2
        elif operation == "-":
            res = num1 - num2
        elif operation == "*":
            res = num1 * num2
        elif operation == "/":
            if num2 == 0:
                raise ZeroDivisionError 
            res = num1 / num2
            
        label_result.config(text=f"Результат: {res}", fg="black")
        
    except ValueError:
        label_result.config(text="Помилка: введіть числа!", fg="red")
    except ZeroDivisionError:
        label_result.config(text="Помилка: ділення на нуль!", fg="red")

root = tk.Tk()
root.title("Калькулятор")
root.geometry("300x350")

tk.Label(root, text="Число 1:").pack(pady=5)
entry1 = tk.Entry(root, justify="center")
entry1.pack()

tk.Label(root, text="Число 2:").pack(pady=5)
entry2 = tk.Entry(root, justify="center")
entry2.pack()

frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=20)

tk.Button(frame_buttons, text="+", width=5, command=lambda: calculate("+")).grid(row=0, column=0, padx=5)
tk.Button(frame_buttons, text="-", width=5, command=lambda: calculate("-")).grid(row=0, column=1, padx=5)
tk.Button(frame_buttons, text="*", width=5, command=lambda: calculate("*")).grid(row=1, column=0, padx=5, pady=5)
tk.Button(frame_buttons, text="/", width=5, command=lambda: calculate("/")).grid(row=1, column=1, padx=5, pady=5)

label_result = tk.Label(root, text="Результат: ", font=("Arial", 12, "bold"))
label_result.pack(pady=20)

root.mainloop()