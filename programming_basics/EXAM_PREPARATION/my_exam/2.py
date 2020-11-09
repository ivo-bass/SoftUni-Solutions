starting_overall = 9.2
start_reviews_count = 405

reviews_count = start_reviews_count
overall = starting_overall
points = starting_overall * start_reviews_count

while True:
    command = input()
    if command == "End":
        break
    grade = float(command)
    reviews_count += 1
    points += grade
    current_overall = points / reviews_count
    print(f"Нова средна оценка: {current_overall}")

