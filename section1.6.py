def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

number = int(input("Введіть ціле число для обчислення факторіала: "))

if number < 0:
    print("Факторіал не визначений для від'ємних чисел.")
else:
    result = factorial(number)
    print("Факторіал числа", number, "дорівнює", result)