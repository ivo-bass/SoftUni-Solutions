player_name = input()
starting_points = 301

sectors = {"Single": 1, "Double": 2, "Triple": 3}
bad_shots = 0
good_shots = 0

while True:
    sector_hit = input()
    if sector_hit == 'Retire':
        print(f"{player_name} retired after {bad_shots} unsuccessful shots.")
        break
    else:
        points_hit = int(input())
        points_hit *= sectors[sector_hit]

    if points_hit > starting_points:
        bad_shots += 1
        continue
    else:
        good_shots += 1
        starting_points -= points_hit
        if starting_points == 0:
            print(f"{player_name} won the leg with {good_shots} shots.")
            break
