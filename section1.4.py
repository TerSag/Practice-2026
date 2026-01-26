import math

g = 9.81

print(" Розрахунок польоту снаряда (ідеальні умови) ")

v0 = float(input("Введіть початкову швидкість (м/с): "))
angle_deg = float(input("Введіть кут вильоту (у градусах): "))

angle_rad = math.radians(angle_deg)

t_total = (2 * v0 * math.sin(angle_rad)) / g

dist = (v0**2 * math.sin(2 * angle_rad)) / g

h_max = (v0 * math.sin(angle_rad))**2 / (2 * g)

print("Результати ")
print("Загальний час польоту:", t_total, "сек.")
print("Максимальна дальність:", dist, "м.")
print("Максимальна висота:", h_max, "м.")

print("\n Висота снаряда на кожну секунду польоту ")
t = 0
while t <= t_total:
    h = v0 * t * math.sin(angle_rad) - (g * t**2) / 2
    
    if h < 0:
        h = 0
        
    print("Секунда", t, ": висота =", h, "м.")
    t = t + 1


if (t - 1) < t_total:
    print("Момент приземлення (", t_total, "сек ): висота = 0 м.")