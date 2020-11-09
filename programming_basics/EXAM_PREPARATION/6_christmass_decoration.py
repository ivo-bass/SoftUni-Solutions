budget = int(input())

money_left = budget
while True:
    item_name = input()
    if item_name == 'Stop':
        print(f"Money left: {money_left}")
        break
    price = 0
    for char in item_name:
        price += ord(char)
    money_left -= price
    if money_left < 0:
        print("Not enough money!")
        break
    else:
        print("Item successfully purchased!")

