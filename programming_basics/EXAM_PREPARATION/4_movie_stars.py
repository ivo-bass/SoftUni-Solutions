budget = float(input())

while True:
    name = input()
    if name == "ACTION":
        print(f"We are left with {budget:.2f} leva.")
        break
    if len(name) > 15:
        wage = 0.2 * budget
    else:
        wage = float(input())
    budget -= wage
    if budget <= 0:
        print(f"We need {abs(budget):.2f} leva for our actors.")
        break
