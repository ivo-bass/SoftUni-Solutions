n = int(input())

special_numbers = []
for number in range(1111, 10000):
    number_string = str(number)
    if '0' not in number_string:
        if (int(number_string[0]) + int(number_string[1])) == (int(number_string[2]) + int(number_string[3])):
            if n % (int(number_string[0]) + int(number_string[1])) == 0:
                special_numbers.append(number)

print(*special_numbers)
