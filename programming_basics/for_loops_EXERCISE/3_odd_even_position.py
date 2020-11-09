import sys

n = int(input())

odd_sum = 0
odd_min = sys.maxsize
odd_max = -sys.maxsize
even_sum = 0
even_min = sys.maxsize
even_max = -sys.maxsize

for i in range(1, n + 1):
    num = float(input())
    if i % 2 == 0:
        even_sum += num
        if num > even_max:
            even_max = num
        if num < even_min:
            even_min = num
    else:
        odd_sum += num
        if num > odd_max:
            odd_max = num
        if num < odd_min:
            odd_min = num

if odd_min == sys.maxsize:
    odd_min = "No"
else:
    odd_min = f"{odd_min:.2f}"

if odd_max == -sys.maxsize:
    odd_max = "No"
else:
    odd_max = f"{odd_max:.2f}"

if even_min == sys.maxsize:
    even_min = "No"
else:
    even_min = f"{even_min:.2f}"

if even_max == -sys.maxsize:
    even_max = "No"
else:
    even_max = f"{even_max:.2f}"

print(f"OddSum={odd_sum:.2f},")
print(f"OddMin={odd_min},")
print(f"OddMax={odd_max},")
print(f"EvenSum={even_sum:.2f},")
print(f"EvenMin={even_min},")
print(f"EvenMax={even_max}")
