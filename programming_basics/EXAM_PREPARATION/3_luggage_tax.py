width = int(input())
height = int(input())
depth = int(input())
priority = input()

volume = width * height * depth
taxes = {"true": {50 < volume <= 100: 0,
                  100 < volume <= 200: 10,
                  200 < volume <= 300: 20},
         "false": {50 < volume <= 100: 25,
                   100 < volume <= 200: 50,
                   200 < volume <= 300: 100}}
tax = 0
if volume > 50:
    tax = taxes[priority][True]

print(f"Luggage tax: {tax:.2f}")
