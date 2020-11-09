p1_name = input()
p2_name = input()

p1_points = 0
p2_points = 0

while True:
    p1_card = input()
    if p1_card == 'End of game':
        print(f"{p1_name} has {p1_points} points")
        print(f"{p2_name} has {p2_points} points")
        break
    elif p1_card == '':
        continue
    else:
        p1_card = int(p1_card)
        p2_card = int(input())
        difference = p1_card - p2_card
        if difference > 0:
            p1_points += difference
        elif difference < 0:
            p2_points += abs(difference)
        else:
            print('Number wars!')
            p1_card = int(input())
            p2_card = int(input())
            difference = p1_card - p2_card
            if difference > 0:
                print(f"{p1_name} is winner with {p1_points} points")
                break
            elif difference < 0:
                print(f"{p2_name} is winner with {p2_points} points")
                break
