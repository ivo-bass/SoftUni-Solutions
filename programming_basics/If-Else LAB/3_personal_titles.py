age = float(input())
gender = input()
title = ''

if age >= 16:
    if gender == 'm':
        title = 'Mr.'
    elif gender == 'f':
        title = 'Ms.'
elif age < 16:
    if gender == 'm':
        title = 'Master'
    elif gender == 'f':
        title = 'Miss'

print(title)
