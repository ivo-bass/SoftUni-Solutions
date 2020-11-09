first_top = int(input())
second_top = int(input())
third_top = int(input())

for f in range(2, first_top+1, 2):
    first_num = f
    for s in range(2, second_top+1):
        if s in (2, 3, 5, 7):
            second_num = s
            for th in range(2, third_top+1, 2):
                third_num = th

                print(f"{first_num} {second_num} {third_num}")
