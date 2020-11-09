judges_count = int(input())
presentation_name = input()

all_grades = 0
presentations_count = 0
while presentation_name != 'Finish':
    presentation_grades = 0
    presentations_count += 1
    for judge in range(judges_count):
        grade = float(input())
        presentation_grades += grade
        all_grades += grade
    presentation_avrg_grade = presentation_grades / judges_count
    print(f"{presentation_name} - {presentation_avrg_grade:.2f}.")
    presentation_name = input()

final_grade = all_grades / (presentations_count * judges_count)
print(f"Student's final assessment is {final_grade:.2f}.")
