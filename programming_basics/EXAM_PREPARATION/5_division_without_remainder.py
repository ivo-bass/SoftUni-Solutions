n = int(input())
p1 = 0
p2 = 0
p3 = 0
for _ in range(n):
    number = int(input())
    if number % 2 == 0:
        p1 += 1
    if number % 3 == 0:
        p2 += 1
    if number % 4 == 0:
        p3 += 1

p1 = p1 / n * 100
p2 = p2 / n * 100
p3 = p3 / n * 100
print(f'{p1:.2f}%')
print(f'{p2:.2f}%')
print(f'{p3:.2f}%')
