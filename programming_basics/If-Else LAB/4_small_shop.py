sofia_prices = {'coffee': 0.50, 'water': 0.80, 'beer': 1.20,
                'sweets': 1.45, 'peanuts': 1.60}
plovdiv_prices = {'coffee': 0.40, 'water': 0.70, 'beer': 1.15,
                  'sweets': 1.30, 'peanuts': 1.50}
varna_prices = {'coffee': 0.45, 'water': 0.70, 'beer': 1.10,
                'sweets': 1.35, 'peanuts': 1.55}

product = input()
city = input()
count = float(input())
price = 0.0

if city == 'Sofia':
    price = count * sofia_prices[product]
elif city == 'Plovdiv':
    price = count * plovdiv_prices[product]
elif city == 'Varna':
    price = count * varna_prices[product]

print(price)
