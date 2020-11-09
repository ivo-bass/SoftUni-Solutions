a1 = int(input())
a2 = int(input())
n = int(input())

for x in range(a1, a2):
    for y in range(1, n):
        for z in range(1, int(n / 2)):
            if x % 2 != 0 and (y + z + x) % 2 != 0:
                print(f"{chr(x)}-{y}{z}{x}")
