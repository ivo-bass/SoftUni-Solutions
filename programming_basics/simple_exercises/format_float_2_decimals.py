dog_price = 2.50
other_price = 4.00

dogs_count = int(input())
other_count = int(input())

costs = (dogs_count * dog_price + other_count * other_price)
coasts_format = format(costs, '7.2f')

print(coasts_format, "lv.")