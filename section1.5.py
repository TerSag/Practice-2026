print("Програма: Бульбашкове сортування ")

raw_input = input("Введіть числа через пробіл: ")
data = []
for x in raw_input.split():
    data.append(int(x))

n = len(data)
print("Початковий масив:", data)

for i in range(n):

    for j in range(0, n - i - 1):
        if data[j] > data[j + 1]:
            temp = data[j]
            data[j] = data[j + 1]
            data[j + 1] = temp

print("Відсортований масив:", data)