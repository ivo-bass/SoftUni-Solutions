show_costs = int(input())
command = input()

total_income = 0
total_guests = 0
while command != 'The restaurant is full':
    guests_count = int(command)
    if guests_count < 5:
        price = 100
    else:
        price = 70
    group_price = price * guests_count
    total_income += group_price
    total_guests += guests_count
    command = input()

money_difference = total_income - show_costs
if money_difference < 0:
    print(f"You have {total_guests} guests and {total_income} leva income, but no singer.")
else:
    print(f"You have {total_guests} guests and {money_difference} leva left.")
