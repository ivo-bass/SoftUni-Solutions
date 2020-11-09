count1 = int(input())
count2 = int(input())
count5 = int(input())
total = int(input())

for ones in range(0, count1 + 1):
    for twos in range(0, count2 + 1):
        for fives in range(0, count5 + 1):
            if ones + twos * 2 + fives * 5 == total:
                print(f"{ones} * 1 lv. + {twos} * 2 lv. + {fives} * 5 lv. = {total} lv.")
