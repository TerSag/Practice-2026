import math

# 1. ПРОЦЕДУРНИЙ ПІДХІД (Функції)

def calculate_rectangle_area(width, height):
    return width * height

def calculate_circle_area(radius):
    return math.pi * (radius ** 2)

rect_area = calculate_rectangle_area(10, 5)
circ_area = calculate_circle_area(7)

print(f"Процедурно: Прямокутник = {rect_area}, Коло = {circ_area:.2f}")

# 2. ОБ'ЄКТНО-ОРІЄНТОВАНИЙ ПІДХІД (Класи)

class Shape:
    """Базовий клас для всіх фігур"""
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

shapes = [Rectangle(10, 5), Circle(7)]

print("\nООП підхід:")
for shape in shapes:
    print(f"Площа фігури {type(shape).__name__}: {shape.area():.2f}")