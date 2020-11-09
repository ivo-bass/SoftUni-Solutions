transactions = int(input())

balance = 0

while transactions > 0:
    transactions -= 1
    trans_sum = float(input())
    if trans_sum < 0:
        print("Invalid operation!")
        break
    print(f"Increase: {trans_sum:.2f}")
    balance += trans_sum

print(f"Total: {balance:.2f}")
