import math

print("Програма для розв'язання квадратного рівняння ax^2 + bx + c = 0 ")

a = float(input("Введіть коефіцієнт a: "))
b = float(input("Введіть коефіцієнт b: "))
c = float(input("Введіть коефіцієнт c: "))

D = b**2 - 4*a*c
print("Дискримінант D =", D)

if D > 0:
    x1 = (-b + math.sqrt(D)) / (2 * a)
    x2 = (-b - math.sqrt(D)) / (2 * a)
    print("Рівняння має два корені:")
    print("x1 =", x1)
    print("x2 =", x2)

elif D == 0:
    x = -b / (2 * a)
    print("Рівняння має один корінь:")
    print("x =", x)

else:
    print("Дійсних коренів немає, оскільки D < 0")
    