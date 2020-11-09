number_str = input()

for n in reversed(number_str):
    num = int(n)
    for i in range(num):
        if num != 0:
            char = chr(num+33)
            print(char, end='')
    if num == 0:
        print('ZERO')
    else:
        print()
