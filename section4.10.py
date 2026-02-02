class Car:
    def __init__(self, brand, mileage=0):
        self.brand = brand
        self.mileage = mileage 

    @property
    def mileage(self):
        return self._mileage

    @mileage.setter
    def mileage(self, value):
        if value < 0:
            print(f"[Помилка]: Пробіг для {self.brand} не може бути від’ємним!")
            self._mileage = 0
        else:
            self._mileage = value

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Баланс не може бути меншим за нуль!")
        self._balance = value


print("--- Тестування класу Car ---")
my_car = Car("Toyota", 5000)
print(f"Поточний пробіг: {my_car.mileage}")

my_car.mileage = -100 
print(f"Пробіг після спроби зміни: {my_car.mileage}")

print("\n--- Тестування класу BankAccount ---")
account = BankAccount("Іван", 1000)
try:
    account.balance = -500
except ValueError as e:
    print(f"[Валідація]: {e}")