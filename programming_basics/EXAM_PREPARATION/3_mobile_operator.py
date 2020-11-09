years = input()
offer = input()
internet = input()
months = int(input())

offers = {
    'one': {"Small": 9.98, "Middle": 18.99, "Large": 25.98, "ExtraLarge": 35.99},
    'two': {"Small": 8.58, "Middle": 17.09, "Large": 23.59, "ExtraLarge": 31.79}
}
fee = offers[years][offer]
if internet == 'yes':
    if fee <= 10:
        fee += 5.5
    elif fee <= 30:
        fee += 4.35
    else:
        fee += 3.85
if years == 'two':
    fee *= 0.9625

total = fee * months

print(f"{total:.2f} lv.")