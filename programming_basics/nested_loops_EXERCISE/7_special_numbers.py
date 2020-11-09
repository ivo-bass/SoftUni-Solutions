n = int(input())

special_numbers = []
for number in range(1111, 10000):
    number_string = str(number)
    if '0' not in number_string:
        for i in number_string:
            if n % int(i) == 0:
                pass
            else:
                break
        else:
            special_numbers.append(number)

print(*special_numbers)
