x_end = int(input())
y_end = int(input())
max_passwords_count = int(input())

a = 35
b = 64
while max_passwords_count > 0:
    for x in range(1, x_end + 1):
        for y in range(1, y_end + 1):
            a_ascii = chr(a)
            a += 1
            if a == 56:
                a = 35
            b_ascii = chr(b)
            b += 1
            if b == 97:
                b = 64
            password = f"{a_ascii}{b_ascii}{x}{y}{b_ascii}{a_ascii}"
            print(password, end="|")
            max_passwords_count -= 1
            if max_passwords_count <= 0:
                break
        if max_passwords_count <= 0:
            break
    else:
        break
