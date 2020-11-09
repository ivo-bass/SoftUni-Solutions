first_result = input()
second_result = input()
third_result = input()

results = [first_result, second_result, third_result]
games_won = 0
games_lost = 0
games_drawn = 0

for result in results:
    home_goals = result[0]
    away_goals = result[2]
    if home_goals > away_goals:
        games_won += 1
    elif home_goals < away_goals:
        games_lost += 1
    else:
        games_drawn += 1

print(f"Team won {games_won} games.")
print(f"Team lost {games_lost} games.")
print(f"Drawn games: {games_drawn}")
