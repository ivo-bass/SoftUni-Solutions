income_per_month = float(input())
months = int(input())
costs_per_month = float(input())

unpredicted_costs = 30/100 * income_per_month
savings_per_month = income_per_month - costs_per_month - unpredicted_costs
savings_percentage = savings_per_month / income_per_month
savings = f"{months * savings_per_month:.2f}"

print(f"She can save {savings_percentage:.2%}")
print(savings)
