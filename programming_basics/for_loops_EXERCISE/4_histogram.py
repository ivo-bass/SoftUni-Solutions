n = int(input())

p1, p2, p3, p4, p5 = 0, 0, 0, 0, 0

for _ in range(n):
    num = int(input())
    if num < 200:
        p1 += 1
    elif 200 <= num <= 399:
        p2 += 1
    elif 400 <= num <= 599:
        p3 += 1
    elif 600 <= num <= 799:
        p4 += 1
    elif num >= 800:
        p5 += 1

print(f"{(p1 / n):.2%}")
print(f"{(p2 / n):.2%}")
print(f"{(p3 / n):.2%}")
print(f"{(p4 / n):.2%}")
print(f"{(p5 / n):.2%}")
