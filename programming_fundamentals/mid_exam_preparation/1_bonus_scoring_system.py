from math import ceil

count_of_students = int(input())
count_of_lectures = int(input())
initial_bonus = int(input())

all_bonuses = []
best_student = {"bonus": 0, "attendances": 0}

for student in range(count_of_students):
	attendances = int(input())
	bonus = attendances / count_of_lectures * (5 + initial_bonus)
	if bonus > best_student["bonus"]:
		best_student["bonus"] = bonus
		best_student["attendances"] = attendances

max_bonus = ceil(best_student["bonus"])
max_attendances = best_student["attendances"]

print(f'Max Bonus: {max_bonus}.')
print(f'The student has attended {max_attendances} lectures.')
