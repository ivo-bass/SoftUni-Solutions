years_lily = int(input())
washing_machine_price = float(input())
toy_price = int(input())

additional_sum = 10
total_sum = 0
toys_count = 0
for year in range(1, years_lily + 1):
    if year % 2 == 0:
        total_sum += additional_sum
        additional_sum += 10
        total_sum -= 1
    else:
        toys_count += 1

toy_sum = toys_count * toy_price
total_sum += toy_sum
difference = total_sum - washing_machine_price

if difference < 0:
    print(f"No! {abs(difference):.2f}")
else:
    print(f"Yes! {difference:.2f}")
