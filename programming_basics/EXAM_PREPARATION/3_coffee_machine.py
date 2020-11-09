drink_type = input()
sugar_choice = input()
drink_count = int(input())

espresso_prices = {"Without": 0.90, "Normal": 1.00, "Extra": 1.20}
cappuccino_prices = {"Without": 1.00, "Normal": 1.20, "Extra": 1.60}
tea_prices = {"Without": 0.50, "Normal": 0.60, "Extra": 0.70}
drink_price = 0.00

if drink_type == "Espresso":
    drink_price = espresso_prices[sugar_choice]
elif drink_type == "Cappuccino":
    drink_price = cappuccino_prices[sugar_choice]
elif drink_type == "Tea":
    drink_price = tea_prices[sugar_choice]

total_price = drink_price * drink_count

if sugar_choice == "Without":
    total_price -= total_price * 0.35

if drink_type == "Espresso" and drink_count >= 5:
    total_price -= total_price * 0.25

if total_price > 15.00:
    total_price -= total_price * 0.20

print(f"You bought {drink_count} cups of {drink_type} for {total_price:.2f} lv.")
