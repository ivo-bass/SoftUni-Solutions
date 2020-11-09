budget = float(input())
overnight_count = int(input())
overnight_price = float(input())
additional_expenses = int(input()) / 100 * budget

if overnight_count > 7:
    overnight_price -= 5/100 * overnight_price

expenses = overnight_count * overnight_price + additional_expenses

if expenses <= budget:
    money_left = budget - expenses
    print(f"Ivanovi will be left with {money_left:.2f} leva after vacation.")
else:
    money_needed = expenses - budget
    print(f"{money_needed:.2f} leva needed.")
