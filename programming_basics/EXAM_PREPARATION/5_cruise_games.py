player = input()
games_count = int(input())

games_perc = {"volleyball": 0.07, "tennis": 0.05, "badminton": 0.02}
games_count_dict = {"volleyball": 0, "tennis": 0, "badminton": 0}
games_points_dict = {"volleyball": 0.0, "tennis": 0.0, "badminton": 0.0}
total_points = 0.00

for _ in range(games_count):
    game_name = input()
    points = int(input())
    add_points = points + games_perc[game_name] * points
    total_points += add_points
    games_points_dict[game_name] += add_points
    games_count_dict[game_name] += 1

for name, count in games_count_dict.items():
    avrg_per_game = games_points_dict[name] / count
    if avrg_per_game < 75:
        print(f"Sorry, {player}, you lost. Your points are only {int(total_points)}.")
        break
else:
    print(f"Congratulations, {player}! You won the cruise games with {int(total_points)} points.")
