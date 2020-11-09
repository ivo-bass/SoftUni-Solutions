tax = int(input())

sneakers = 0.6 * tax
jersey = 0.8 * sneakers
ball = 0.25 * jersey
accessories = 0.2 * ball

total = sneakers + jersey + ball + accessories + tax

print(f"{total:.2f}")
