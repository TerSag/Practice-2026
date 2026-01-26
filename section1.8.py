import pandas as pd
df = pd.read_csv('students.csv')

subjects = df.columns[2:]
df['Середній бал'] = df[subjects].mean(axis=1)

print("Дані студентів із середнім балом:")
print(df[['Прізвище', 'Ім\'я', 'Середній бал']])

print("\n Середній бал групи по дисциплінах:")
group_avg = df[subjects].mean()
print(group_avg)