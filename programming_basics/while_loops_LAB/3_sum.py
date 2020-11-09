sum = 0

while True:
    num = input()
    if num == 'Stop':
        break
    else:
        num = int(num)
    sum += num

print(sum)