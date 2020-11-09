wrong_count = int(input())
wrong_ans = 0
total_count = 0
grades_sum = 0

while wrong_ans < wrong_count:
    name = input()
    if name == 'Enough':
        avrg = grades_sum / total_count
        print(f"Average score: {avrg:.2f}")
        print(f"Number of problems: {total_count}")
        print(f"Last problem: {last_name}")
        break
    last_name = name
    grade = int(input())
    total_count += 1
    if grade <= 4:
        wrong_ans += 1
    grades_sum += grade
else:
    print(f"You need a break, {wrong_count} poor grades.")
