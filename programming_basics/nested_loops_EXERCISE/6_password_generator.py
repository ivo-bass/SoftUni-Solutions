n = int(input())
l = int(input())

passwords = []

for x1 in range(1, n):
    for x2 in range(1, n):
        for i1 in range(97, 97+l):
            x3 = chr(i1)
            for i2 in range(97, 97+l):
                x4 = chr(i2)
                for x5 in range(1, n+1):
                    if x5 > x1 and x5 > x2:
                        password = f'{x1}{x2}{x3}{x4}{x5}'
                        passwords.append(password)
print(*passwords)
