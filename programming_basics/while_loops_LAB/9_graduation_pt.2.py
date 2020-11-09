name = input()

class_counter = 1
class_failed = 0
grades_sum = 0
is_excluded = False
while class_counter <= 12:
    grade = float(input())
    if grade >= 4:
        class_counter += 1
        grades_sum += grade
    else:
        class_failed += 1
        if class_failed == 2:
            print(f"{name} has been excluded at {class_counter} grade")
            is_excluded = True
            break

if not is_excluded:
    avrg_grade = grades_sum / 12
    print(f"{name} graduated. Average grade: {avrg_grade:.2f}")
