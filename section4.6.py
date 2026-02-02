class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        raise NotImplementedError("Похідний клас повинен реалізувати цей метод")

class Dog(Animal):
    def sound(self):
        return f"{self.name} каже: Гав-гав!"

class Cat(Animal):
    def sound(self):
        return f"{self.name} каже: Мяу!"

class Cow(Animal):
    def sound(self):
        return f"{self.name} каже: Му-у-у!"


animals = [
    Dog("Сірко"),
    Cat("Мурчик"),
    Cow("Зірка")
]

print("--- Демонстрація звуків тварин ---")
for animal in animals:
    print(animal.sound())