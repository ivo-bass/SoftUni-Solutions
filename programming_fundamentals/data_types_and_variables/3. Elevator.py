from math import ceil

persons_count = int(input())
elevator_capacity = int(input())

courses = ceil(persons_count / elevator_capacity)

print(courses)
