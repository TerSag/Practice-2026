# Використав класи, створені у попередньому завданні (4.6)
class Animal:
    def __init__(self, name):
        self.name = name
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return f"{self.name} (Собака): Гав!"

class Cat(Animal):
    def sound(self):
        return f"{self.name} (Кіт): Мяу!"

class Cow(Animal):
    def sound(self):
        return f"{self.name} (Корова): Му-у!"

zoo = [
    Dog("Барон"),
    Cat("Мурка"),
    Cow("Лиска"),
    Dog("Рекс")
]

print("--- ДЕМОНСТРАЦІЯ ПОЛІМОРФІЗМУ ---")

for animal in zoo:
    print(animal.sound())