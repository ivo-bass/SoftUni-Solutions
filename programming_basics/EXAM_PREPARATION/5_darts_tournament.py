starting_points = int(input())

sectors_q = {"number section": 1, "double ring": 2, "triple ring": 3}
current_points = starting_points
moves = 0
while True:
    sector = input()
    moves += 1
    if sector == "bullseye":
        print(f"Congratulations! You won the game with a bullseye in {moves} moves!")
        break

    points = int(input())
    points *= sectors_q[sector]

    if points < current_points:
        current_points -= points
    elif points == current_points:
        print(f"Congratulations! You won the game in {moves} moves!")
        break
    else:
        print(f"Sorry, you lost. Score difference: {abs(current_points - points)}.")
        break
