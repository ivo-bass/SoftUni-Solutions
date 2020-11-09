end_100 = int(input())
end_10 = int(input())
end_1 = int(input())

for x in range(2, end_100 + 1):
    if x % 2 == 0:
        dig1 = x
        for y in range(2, end_10 + 1):
            if y in (2, 3, 5, 7):
                dig2 = y
                for z in range(2, end_1 + 1):
                    if z % 2 == 0:
                        dig3 = z
                        password = f"{dig1} {dig2} {dig3}"
                        print(password)
