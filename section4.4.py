class Car:

    def __init__(self, brand, year, mileage=0):
        self.brand = brand
        self.year = year
        self.mileage = mileage

    def drive(self, km):
        if km > 0:
            self.mileage += km
            print(f"Поїздка на {km} км завершена.")
        else:
            print("Помилка: відстань має бути додатною!")

    def info(self):
        print(f"Автомобіль: {self.brand}")
        print(f"Рік випуску: {self.year}")
        print(f"Поточний пробіг: {self.mileage} км")

    def __str__(self):
        return f"{self.brand} ({self.year}), пробіг: {self.mileage} км"

print("--- Створення та тестування об'єкта Car ---")

my_car = Car("Audi", 2026, 100)

print(f"Статус через __str__: {my_car}")

my_car.drive(150)
my_car.drive(45)

my_car.info()