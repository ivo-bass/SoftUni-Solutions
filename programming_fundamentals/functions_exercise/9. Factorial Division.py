from math import factorial

n1 = int(input())
n2 = int(input())

factorial_1 = factorial(n1)
factorial_2 = factorial(n2)

result = factorial_1 / factorial_2

print(f"{result:.2f}")
