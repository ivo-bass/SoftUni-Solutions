month = input()
count = int(input())

st_prices = {'May': 50, 'June': 75.2, 'July': 76,
             'August': 76, 'September': 75.20, 'October': 50}
app_prices = {'May': 65, 'June': 68.7, 'July': 77,
              'August': 77, 'September': 68.7, 'October': 65}

st_price = st_prices[month] * count
app_price = app_prices[month] * count

if count > 14 and month in ('May', 'October'):
    st_price *= 0.7
elif count > 14 and month in ('June', 'September'):
    st_price *= 0.8
elif count > 7 and month in ('May', 'October'):
    st_price *= 0.95

if count > 14:
    app_price *= 0.9

print(f"Apartment: {app_price:.2f} lv.")
print(f"Studio: {st_price:.2f} lv.")
