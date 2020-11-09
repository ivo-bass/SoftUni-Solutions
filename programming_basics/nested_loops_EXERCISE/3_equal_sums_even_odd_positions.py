x = int(input())
y = int(input())

for number in range(x, y + 1):
    even_sum = 0
    odd_sum = 0
    counter = 1
    num = number

    while num > 0:
        last = num % 10
        if counter % 2 == 0:
            even_sum += last
        else:
            odd_sum += last
        num = num // 10
        counter += 1

    if even_sum == odd_sum:
        print(number, end=" ")
