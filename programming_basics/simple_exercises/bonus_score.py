entry_points = int(input())
bonus_points = 0

if entry_points <= 100:
    bonus_points = 5
elif entry_points > 1000:
    bonus_points = entry_points * 0.1
else:
    bonus_points = entry_points * 0.2

if bonus_points - int(bonus_points) == 0:
    bonus_points = int(bonus_points)

if entry_points % 2 == 0:
    bonus_points += 1
elif entry_points % 10 == 5:
    bonus_points += 2

total_points = entry_points + bonus_points

print(bonus_points)
print(total_points)
