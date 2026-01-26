students = [
    {"prizv": "Петренко", "imya": "Олег", "marks": [5, 4, 5, 3, 4]},
    {"prizv": "Сидоренко", "imya": "Анна", "marks": [4, 5, 5, 5, 4]},
    {"prizv": "Іванова", "imya": "Марія", "marks": [3, 3, 4, 4, 5]},
    {"prizv": "Коваль", "imya": "Ігор", "marks": [5, 5, 4, 3, 3]}
]

print("Таблиця результатів:")
print("Прізвище\tІм'я\tСередній бал")
print("-" * 40)

for s in students:
    avg_student = sum(s["marks"]) / len(s["marks"])
    print(f"{s['prizv']}\t{s['imya']}\t{avg_student}")

print("-" * 40)

num_subjects = 5
num_students = len(students)

print("Середній бал групи по предметах:")
for i in range(num_subjects):
    total_subject_marks = 0
    for s in students:
        total_subject_marks += s["marks"][i]
    
    avg_subject = total_subject_marks / num_students
    print(f"Предмет {i+1}: {avg_subject}")