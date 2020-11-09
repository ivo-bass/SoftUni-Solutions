number = float(input())
unit_in = input()
unit_out = input()
result = 0

if unit_out == 'm':
    if unit_in == 'cm':
        result = number / 100
    elif unit_in == 'mm':
        result = number / 1000
elif unit_out == 'cm':
    if unit_in == 'm':
        result = number * 100
    elif unit_in == 'mm':
        result = number / 10
elif unit_out == 'mm':
    if unit_in == 'm':
        result = number * 1000
    elif unit_in == 'cm':
        result = number * 10

print(f"{result:.3f}")
