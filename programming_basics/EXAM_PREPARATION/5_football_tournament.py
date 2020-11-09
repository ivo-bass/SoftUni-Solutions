team_name = input()
games_played = int(input())

points = 0
total_w = 0
total_d = 0
total_l = 0

if games_played == 0:
    print(f"{team_name} hasn't played any games during this season.")
else:
    for game in range(games_played):
        result = input()
        if result == "W":
            points += 3
            total_w += 1
        elif result == "D":
            points += 1
            total_d += 1
        elif result == "L":
            total_l += 1

    wins_percentage = total_w / games_played
    print(f"{team_name} has won {points} points during this season.")
    print("Total stats:")
    print(f"## W: {total_w}")
    print(f"## D: {total_d}")
    print(f"## L: {total_l}")
    print(f"Win rate: {wins_percentage:.2%}")
