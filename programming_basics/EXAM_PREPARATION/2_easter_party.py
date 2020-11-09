guests_count = int(input())
price_per_guest = float(input())
budget = float(input())

discount = {10 <= guests_count <= 15: 0.15 * price_per_guest * guests_count,
            15 < guests_count <= 20: 0.2 * price_per_guest * guests_count,
            guests_count > 20: 0.25 * price_per_guest * guests_count,
            guests_count < 10: 0}

cake_price = 0.1 * budget
total = guests_count * price_per_guest - discount[True] + cake_price
money_difference = budget - total
if money_difference < 0:
    print(f"No party! {abs(money_difference):.2f} leva needed.")
else:
    print(f"It is party time! {money_difference:.2f} leva left.")
