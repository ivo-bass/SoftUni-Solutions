clients_count = int(input())

prices = {'basket': 1.5, 'wreath': 3.8, 'chocolate bunny': 7}
income = 0
for _ in range(clients_count):
    items = 0
    total_costs = 0
    while True:
        purchase = input()
        if purchase == 'Finish':
            if items % 2 == 0:
                total_costs *= 0.8
            print(f"You purchased {items} items for {total_costs:.2f} leva.")
            income += total_costs
            break
        else:
            items += 1
            total_costs += prices[purchase]

avrg_bill = income / clients_count
print(f"Average bill per client is: {avrg_bill:.2f} leva.")
