import sys

n = int(input())
max_num = -sys.maxsize

while n > 0:
    n -= 1
    num = int(input())
    if num > max_num:
        max_num = num

print(max_num)
