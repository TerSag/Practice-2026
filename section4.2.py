class Student:
    
    def __init__(self, name, group, average_score):
        self.name = name
        self.group = group
        self.average_score = average_score

    def show_info(self):
        print(f"--- Картка студента ---")
        print(f"Прізвище та ім'я: {self.name}")
        print(f"Навчальна група: {self.group}")
        print(f"Середній бал:    {self.average_score}")
        print("-" * 23)

student1 = Student("Іваненко Максим", "ІПЗ-33", 92.5)
student2 = Student("Петренко Олена", "ІПЗ-33", 88.0)
student3 = Student("Сидоренко Денис", "ІПЗ-33", 75.4)

print("Результати роботи програми:\n")
student1.show_info()
student2.show_info()
student3.show_info()