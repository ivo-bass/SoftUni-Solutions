total_tournaments = 0
total_fixtures = 0
total_wins = 0
total_lost = 0
while True:
    name_of_tournament = input()
    if name_of_tournament == 'End of tournaments':
        wins_percentage = total_wins / total_fixtures * 100
        lost_percentage = total_lost / total_fixtures * 100
        print(f"{wins_percentage:.2f}% matches win")
        print(f"{lost_percentage:.2f}% matches lost")
        break
    total_tournaments += 1
    fixtures = int(input())
    total_fixtures += fixtures
    for fixture in range(fixtures):
        home_points = int(input())
        away_points = int(input())
        difference = abs(home_points - away_points)
        if home_points > away_points:
            total_wins += 1
            print(f"Game {fixture + 1} of tournament {name_of_tournament}: win with {difference} points.")
        elif home_points < away_points:
            total_lost += 1
            print(f"Game {fixture + 1} of tournament {name_of_tournament}: lost with {difference} points.")
