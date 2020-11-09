age = int(input())

rules = {age<=14: 'drink toddy',
         14<age<=18: 'drink coke',
         18<age<=21: 'drink beer',
         age>21: 'drink whisky'}

print(f"{rules[True]}")
