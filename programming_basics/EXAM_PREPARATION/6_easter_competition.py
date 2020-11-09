cakes_count = int(input())
best_baker = ''
best_points = 0
for _ in range(cakes_count):
    baker_name = input()
    total_points = 0
    while True:
        points = input()
        if points == 'Stop':
            print(f"{baker_name} has {total_points} points.")
            if total_points > best_points:
                best_baker = baker_name
                best_points = total_points
                print(f"{baker_name} is the new number 1!")
            break
        else:
            points = int(points)
            total_points += points

print(f"{best_baker} won competition with {best_points} points!")
