import math

count = int(input())
entr_fee = float(input())
bed_price = float(input())
umb_price = float(input())

beds_needed = math.ceil(75/100 * count)
umb_needed = math.ceil(count / 2)

entr_costs = entr_fee * count
beds_costs = beds_needed * bed_price
umb_costs = umb_needed * umb_price

total_costs = entr_costs + beds_costs + umb_costs

print(f"{total_costs:.2f} lv.")
