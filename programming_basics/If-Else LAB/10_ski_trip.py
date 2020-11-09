days = int(input())
room = input()
opinion = input()

nights = days - 1
prices = {'room for one person': {'price': 18, 'discount': {True: 0}},
          'apartment': {'price': 25, 'discount': {days < 10: 0.3, 10 <= days <= 15: 0.35, days > 15: 0.5}},
          'president apartment': {'price': 35, 'discount': {days < 10: 0.1, 10 <= days <= 15: 0.15, days > 15: 0.2}}}

price = prices[room]['price'] - prices[room]['discount'][True] * prices[room]['price']
total = nights * price
if opinion == 'positive':
    total *= 1.25
elif opinion == 'negative':
    total *= 0.9

print(f"{total:.2f}")