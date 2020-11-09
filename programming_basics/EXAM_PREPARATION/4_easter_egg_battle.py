count1 = int(input())
count2 = int(input())

while True:
    winner = input()
    if winner == 'one':
        count2 -= 1
        if count2 == 0:
            print(f"Player two is out of eggs. Player one has {count1} eggs left.")
            break
    elif winner == 'two':
        count1 -= 1
        if count1 == 0:
            print(f"Player one is out of eggs. Player two has {count2} eggs left.")
            break
    else:
        print(f"Player one has {count1} eggs left.")
        print(f"Player two has {count2} eggs left.")
        break
