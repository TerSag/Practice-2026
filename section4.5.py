class BankAccount:

    def __init__(self, owner, initial_balance=0):
        self.owner = owner
        self.__balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Рахунок успішно поповнено на {amount} грн.")
        else:
            print("Помилка: сума поповнення має бути більшою за нуль.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Знято {amount} грн. Залишок: {self.__balance} грн.")
        else:
            print("Помилка: недостатньо коштів або невірна сума.")

    def get_balance(self):
        return self.__balance

my_account = BankAccount("ФОП Користувач", 1000)

print(f"Власник рахунку: {my_account.owner}")
print(f"Початковий баланс: {my_account.get_balance()} грн.")

my_account.deposit(500)
my_account.withdraw(200)

try:
    print(my_account.__balance) 
except AttributeError:
    print("\n[ЗАХИСТ ПРАЦЮЄ]: Прямий доступ до '__balance' заборонено.")

my_account.__balance = 999999 
print(f"Баланс після спроби прямого злому: {my_account.get_balance()} грн. (Змін не відбулося)")