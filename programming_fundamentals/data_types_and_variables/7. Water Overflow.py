number_of_inputs = int(input())

capacity = 255
litters_in = 0

for _ in range(number_of_inputs):
    quantity = int(input())
    if quantity > capacity:
        print("Insufficient capacity!")
        continue
    capacity -= quantity
    litters_in += quantity

print(litters_in)
