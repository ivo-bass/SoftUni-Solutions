sum = float(input())

coins = 0

while sum > 0:
    sum = round(sum, 2)
    if sum >= 2:
        sum -= 2
        coins += 1
    elif sum >= 1:
        sum -= 1
        coins += 1
    elif sum >= 0.5:
        sum -= 0.5
        coins += 1
    elif sum >= 0.2:
        sum -= 0.2
        coins += 1
    elif sum >= 0.1:
        sum -= 0.1
        coins += 1
    elif sum >= 0.05:
        sum -= 0.05
        coins += 1
    elif sum >= 0.02:
        sum -= 0.02
        coins += 1
    elif sum >= 0.01:
        sum -= 0.01
        coins += 1
    else:
        sum = 0

print(f"{coins}")
