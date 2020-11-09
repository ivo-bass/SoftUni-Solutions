sweets_prices = {"cookies": 1.50, "cakes": 7.80, "waffles": 2.30}
sweets_count_total = {"cookies": 0, "cakes": 0, "waffles": 0}

participants_count = int(input())

for _ in range(participants_count):
    sweets_per_participant = {"cookies": 0, "cakes": 0, "waffles": 0}
    baker = input()

    sweets_type = input()
    while sweets_type != "Stop baking!":
        sweets_count = int(input())
        sweets_per_participant[sweets_type] += sweets_count
        sweets_count_total[sweets_type] += sweets_count
        sweets_type = input()

    print(f'{baker} baked '
          f'{sweets_per_participant["cookies"]} cookies, '
          f'{sweets_per_participant["cakes"]} cakes and '
          f'{sweets_per_participant["waffles"]} waffles.')

total_sold = sweets_count_total["cookies"] + \
             sweets_count_total["cakes"] + \
             sweets_count_total["waffles"]

total_sum = sweets_count_total["cookies"] * sweets_prices["cookies"] + \
            sweets_count_total["cakes"] * sweets_prices["cakes"] + \
            sweets_count_total["waffles"] * sweets_prices["waffles"]

print(f"All bakery sold: {total_sold}")
print(f"Total sum for charity: {total_sum:.2f} lv.")
