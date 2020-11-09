control = int(input())  # 4->144

counter = 0
is_password = False
password = ""
for a in range(1, 10):
    for b in range(a + 1, 10):
        for c in range(1, 10):
            for d in range(1, c):
                if a * b + c * d == control:
                    counter += 1
                    combination = f"{a}{b}{c}{d}"
                    print(combination, end=" ")
                    if counter == 4:
                        is_password = True
                        password = combination

if is_password:
    print(f"\nPassword: {password}")
else:
    print(f"\nNo!")
