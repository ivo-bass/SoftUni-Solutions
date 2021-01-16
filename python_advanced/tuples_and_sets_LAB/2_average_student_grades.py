def get_for_input(count):
    """Takes input with for loop in given range.
    Returns list of the inputs."""
    the_input = []
    for _ in range(count):
        text = input()
        the_input.append(text)
    return the_input


def print_output(dictionary):
    for name, grades in dictionary.items():
        avrg = sum(grades) / len(grades)
        grades = ' '.join(map(lambda grade: f'{grade:.2f}', grades))
        print(f'{name} -> {grades} (avg: {avrg:.2f})')


n = int(input())
student_list = get_for_input(n)

student_db = {}
for student in student_list:
    name, grade = student.split(' ')
    if not name in student_db:
        student_db[name] = []
    student_db[name].append(float(grade))

print_output(student_db)
