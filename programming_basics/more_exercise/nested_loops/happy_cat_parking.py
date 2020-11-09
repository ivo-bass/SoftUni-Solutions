days_count = int(input())
hours_per_day = int(input())

total = 0
for day in range(1, days_count + 1):
    charge = 0
    for hour in range(1, hours_per_day + 1):
        if day % 2 == 0 and hour % 2 != 0:
            charge += 2.5
        elif day % 2 != 0 and hour % 2 == 0:
            charge += 1.25
        else:
            charge += 1
    total += charge
    print(f"Day: {day} - {charge:.2f} leva")

print(f"Total: {total:.2f} leva")