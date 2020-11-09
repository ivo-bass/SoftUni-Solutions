empl1 = int(input())
empl2 = int(input())
empl3 = int(input())
total_students = int(input())

per_hour = empl1 + empl2 + empl3
time = 0

while total_students > 0:
    total_students -= per_hour
    time += 1
    if time % 4 == 0:
        time += 1

print(f"Time needed: {time}h.")
