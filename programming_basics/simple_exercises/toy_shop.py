trip_price = float(input())
puzzles_count = int(input())
dolls_count = int(input())
bears_count = int(input())
minions_count = int(input())
trucks_count = int(input())

puzzles_income = puzzles_count * 2.60
dolls_income = dolls_count * 3.00
bears_income = bears_count * 4.10
minions_income = minions_count * 8.20
trucks_income = trucks_count * 2.00

total_income = puzzles_income + dolls_income + \
               bears_income + minions_income + trucks_income

toys_count = puzzles_count + dolls_count + \
             bears_count + minions_count + trucks_count

if toys_count >= 50:
    discount = 0.25
else:
    discount = 0

final_price = total_income - discount * total_income
rent = final_price * 0.10
profit = final_price - rent

if profit >= trip_price:
    money_left = profit - trip_price
    print(f"Yes! {money_left:.2f} lv left.")
else:
    money_needed = trip_price - profit
    print(f"Not enough money! {money_needed:.2f} lv needed.")
