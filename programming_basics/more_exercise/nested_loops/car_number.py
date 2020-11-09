start = int(input())
stop = int(input())

digit_range = range(start, stop+1)
numbers = []

for dig1 in digit_range:
    for dig2 in digit_range:
        for dig3 in digit_range:
            for dig4 in digit_range:
                if dig1 > dig4 and (dig2 + dig3) % 2 == 0:
                    if (dig1 % 2 == 0 and dig4 % 2 != 0) or (dig4 % 2 == 0 and dig1 % 2 != 0):
                        number = f"{dig1}{dig2}{dig3}{dig4}"
                        numbers.append(number)

print(*numbers)
