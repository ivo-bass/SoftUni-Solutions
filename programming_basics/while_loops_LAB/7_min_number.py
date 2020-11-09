import sys

n = int(input())
min_num = sys.maxsize

while n > 0:
    n -= 1
    num = int(input())
    if num < min_num:
        min_num = num

print(min_num)
