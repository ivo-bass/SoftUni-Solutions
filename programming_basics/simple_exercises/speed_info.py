speed = float(input())
output = ''

if speed <= 10:
    output = 'slow'
elif speed <= 50:
    output = 'average'
elif speed <= 150:
    output = 'fast'
elif speed <= 1000:
    output = 'ultra fast'
elif speed > 1000:
    output = 'extremely fast'

print(output)
