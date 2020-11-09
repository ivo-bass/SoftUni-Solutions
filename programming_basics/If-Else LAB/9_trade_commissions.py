city = input()
sales = float(input())

commission = 'error'
commissions = {'Sofia': {0 <= sales <= 500: 0.05,
                         500 < sales <= 1000: 0.07,
                         1000 < sales <= 10000: 0.08,
                         sales > 10000: 0.12},
               'Varna': {0 <= sales <= 500: 0.045,
                         500 < sales <= 1000: 0.075,
                         1000 < sales <= 10000: 0.10,
                         sales > 10000: 0.13},
               'Plovdiv': {0 <= sales <= 500: 0.055,
                           500 < sales <= 1000: 0.08,
                           1000 < sales <= 10000: 0.12,
                           sales > 10000: 0.145}}

if sales >= 0 and city in commissions.keys():
    commission = f"{commissions[city][True] * sales:.2f}"

print(commission)
