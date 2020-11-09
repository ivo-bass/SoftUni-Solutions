money_vacation = float(input())
money_available = float(input())

total_days = 0
spend_days = 0

while money_available < money_vacation:
    total_days += 1
    action = input()
    action_money = float(input())

    if action == 'save':
        money_available += action_money
        spend_days = 0
    elif action == 'spend':
        money_available -= action_money
        spend_days += 1
        if money_available < 0:
            money_available = 0

        if spend_days == 5:
            print("You can't save the money.")
            print(f"{total_days}")
            break
else:
    print(f"You saved the money for {total_days} days.")
