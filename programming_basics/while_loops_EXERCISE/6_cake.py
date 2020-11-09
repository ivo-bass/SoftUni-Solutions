l_cake = int(input())
w_cake = int(input())

vol_cake = l_cake * w_cake

while vol_cake > 0:
    pieces_taken = input()
    if pieces_taken == 'STOP':
        print(f"{vol_cake} pieces are left.")
        break
    pieces_taken = int(pieces_taken)
    vol_cake -= pieces_taken
    if vol_cake < 0:
        print(f"No more cake left! You need {abs(vol_cake)} pieces more.")
