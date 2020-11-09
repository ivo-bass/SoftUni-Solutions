name = input()
deal = input()
tickets_count = int(input())

prices = {"John Wick": {"Drink": 12, "Popcorn": 15, "Menu": 19},
          "Star Wars": {"Drink": 18, "Popcorn": 25, "Menu": 30},
          "Jumanji": {"Drink": 9, "Popcorn": 11, "Menu": 14}}

bill = tickets_count * prices[name][deal]
if name == "Star Wars" and tickets_count >= 4:
    bill *= 0.7

if name == "Jumanji" and tickets_count == 2:
    bill *= 0.85

print(f"Your bill is {bill:.2f} leva.")
