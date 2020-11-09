budget = float(input())
costs = 0
count = 0
while True:
    product = input()
    if product == "Stop":
        print(f"You bought {count} products for {costs:.2f} leva.")
        break
    price = float(input())
    count += 1
    if count % 3 == 0:
        price *= 0.5

    costs += price
    if costs > budget:
        print("You don't have enough money!")
        print(f"You need {(costs - budget):.2f} leva!")
        break
