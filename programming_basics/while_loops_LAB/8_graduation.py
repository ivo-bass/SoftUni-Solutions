name = input()

class_count = 1
grades_sum = 0

while class_count <= 12:
    grade = float(input())
    if grade >= 4:
        grades_sum += grade
        class_count += 1

avrg_grade = grades_sum / 12
print(f"{name} graduated. Average grade: {avrg_grade:.2f}")
