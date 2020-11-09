voucher_value = int(input())

tickets = 0
others = 0
while True:
    purchase = input()
    if purchase == 'End':
        break
    if len(purchase) > 8:
        price = ord(purchase[0]) + ord(purchase[1])
        if price <= voucher_value:
            tickets += 1
            voucher_value -= price
        else:
            break
    else:
        price = ord(purchase[0])
        if price <= voucher_value:
            others += 1
            voucher_value -= price
        else:
            break

print(f'{tickets}')
print(f'{others}')
