money_target = float(input())
fantasy_books = int(input())
horror_books = int(input())
romance_books = int(input())

prices = {'fantasy': 14.9, 'horror': 9.8, 'romance': 4.3}

income = fantasy_books * prices['fantasy'] + \
         horror_books * prices['horror'] + \
         romance_books * prices['romance']
profit = 0.8 * income

money_left = profit - money_target
if profit >= money_target:
    sellers_money = int(0.1 * money_left)
    donation = profit - sellers_money
    print(f"{donation:.2f} leva donated.")
    print(f"Sellers will receive {sellers_money} leva.")
else:
    print(f"{abs(money_left):.2f} money needed.")
