def analyze_students_data():

    raw_data = {
        "Іваненко": [90, 85, 90, 100],
        "Петренко": [75, 80, 70, 85],
        "Сидоренко": [90, 95, 100, 90]
    }

    processed_results = {}
    all_scores = []

    print("--- АНАЛІЗ УСПІШНОСТІ ---")
    
    for name, scores in raw_data.items():

        average = sum(scores) / len(scores)
        
        processed_results[name] = round(average, 2)
        
        all_scores.extend(scores)

    unique_scores = sorted(set(all_scores))

    print(f"Словник середніх балів: {processed_results}")
    print(f"Список унікальних оцінок у групі: {unique_scores}")
    
    for student, score in processed_results.items():
        print(f"Студент {student} має середній результат: {score}")

if __name__ == "__main__":
    analyze_students_data()