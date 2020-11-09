n = int(input())

left_sum = 0
right_sum = 0

for _ in range(n):
    num = int(input())
    left_sum += num
for _ in range(n):
    num = int(input())
    right_sum += num

# for index, _ in enumerate(range(2*n), 1):
#     number = int(input())
#     if index in range(1, n+1):
#         left_sum += number
#     else:
#         right_sum += number

difference = abs(left_sum - right_sum)
if difference == 0:
    print(f"Yes, sum = {left_sum}")
else:
    print(f"No, diff = {difference}")
