from math import pi

shape = input()

if shape == 'square':
    a = float(input())
    area = a * a

elif shape == 'rectangle':
    a = float(input())
    b = float(input())
    area = a * b

elif shape == 'circle':
    r = float(input())
    area = pi * r * r
elif shape == 'triangle':
    a = float(input())
    h_a = float(input())
    area = a * h_a / 2
else:
    area = ''

print(f'{area:.3f}')
