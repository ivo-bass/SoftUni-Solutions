fruit = input()
day = input()
quantity = float(input())

fruits = ('banana', 'apple', 'orange', 'grapefruit', 'kiwi', 'pineapple', 'grapes')
weekdays_prices = (2.50, 1.20, 0.85, 1.45, 2.70, 5.50, 3.85)
weekend_prices = (2.70, 1.25, 0.90, 1.60, 3.00, 5.60, 4.20)
weekdays = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday')
weekend = ('Saturday', 'Sunday')
price = 'error'

if day in weekdays and fruit in fruits:
    price = f"{weekdays_prices[fruits.index(fruit)] * quantity:.2f}"
elif day in weekend and fruit in fruits:
    price = f"{weekend_prices[fruits.index(fruit)] * quantity:.2f}"

print(price)
