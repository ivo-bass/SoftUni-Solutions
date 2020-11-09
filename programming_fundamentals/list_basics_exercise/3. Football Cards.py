string = input()

cards_list = list(string.split())
team_a = [str(number) for number in range(1, 12)]
team_b = [str(number) for number in range(1, 12)]
game_still_going = True

for card in cards_list:
    card_split = card.split(sep='-')
    if card_split[0] == 'A':
        if card_split[1] in team_a:
            team_a.remove(card_split[1])
    elif card_split[0] == 'B':
        if card_split[1] in team_b:
            team_b.remove(card_split[1])
    if len(team_a) < 7 or len(team_b) < 7:
        game_still_going = False
        break

print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")
if not game_still_going:
    print("Game was terminated")
