days = int(input())
hours_per_day = int(input())

day = 0
total = 0
for d in range(days):
    day += 1
    price_for_today = 0

    hour = 0
    for h in range(hours_per_day):
        hour += 1
        if day % 2 == 0 and hour % 2 != 0:
            price_per_hour = 2.5
        elif day % 2 != 0 and hour % 2 == 0:
            price_per_hour = 1.25
        else:
            price_per_hour = 1
        price_for_today += price_per_hour

    print(f"Day: {day} - {price_for_today:.2f} leva")
    total += price_for_today

print(f"Total: {total:.2f} leva")
