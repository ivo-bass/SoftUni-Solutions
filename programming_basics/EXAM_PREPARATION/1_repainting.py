nylon_needed = int(input()) + 2
paint_needed = int(input()) * 1.1
diluent_needed = int(input())
hours_needed = int(input())

nylon_price = 1.50    # per m2
paint_price = 14.50   # per litre
diluent_price = 5.00  # per litre
bags = 0.40

items_expenses = nylon_needed * nylon_price + \
                 paint_needed * paint_price + \
                 diluent_needed * diluent_price + \
                 bags

workers_expenses = items_expenses * 0.3 * hours_needed

total_expenses = items_expenses + workers_expenses

print(f"Total expenses: {total_expenses:.2f} lv.")
