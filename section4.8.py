from abc import ABC, abstractmethod
import math

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


shapes = [
    Circle(10),
    Rectangle(5, 8),
    Circle(5)
]

print("--- ОБЧИСЛЕННЯ ПЛОЩ ЧЕРЕЗ АБСТРАКЦІЮ ---")
for shape in shapes:
    print(f"Площа фігури {type(shape).__name__}: {shape.area():.2f}")