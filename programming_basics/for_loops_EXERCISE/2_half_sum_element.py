import sys

n = int(input())

max_num = -sys.maxsize
sum_numbers = 0
for _ in range(n):
    num = int(input())

    if num > max_num:
        max_num = num

    sum_numbers += num

sum_numbers -= max_num

if sum_numbers == max_num:
    print("Yes")
    print(f"Sum = {sum_numbers}")
else:
    print("No")
    print(f"Diff = {abs(sum_numbers - max_num)}")
