tournaments_count = int(input())
starting_points = int(input())

points = {"W": 2000, "F": 1200, "SF": 720}

final_points = 0
won_tournaments = 0

for _ in range(tournaments_count):
    stage_reached = input()
    final_points += points[stage_reached]
    if stage_reached == "W":
        won_tournaments += 1

avrg_points = int(final_points / tournaments_count)
won_perc = won_tournaments / tournaments_count
final_points += starting_points

print(f"Final points: {final_points}")
print(f"Average points: {avrg_points}")
print(f"{won_perc:.2%}")
