budget = float(input())
gpu_count = int(input())
cpu_count = int(input())
ram_count = int(input())

gpu_price = 250.00
gpu_costs = gpu_count * gpu_price

cpu_price = 0.35 * gpu_costs
cpu_costs = cpu_count * cpu_price

ram_price = 0.10 * gpu_costs
ram_costs = ram_count * ram_price

expenses = gpu_costs + cpu_costs + ram_costs

if gpu_count > cpu_count:
    expenses -= 0.15 * expenses

if budget >= expenses:
    money_left = budget - expenses
    print(f"You have {money_left:.2f} leva left!")
else:
    money_needed = expenses - budget
    print(f"Not enough money! You need {money_needed:.2f} leva more!")
