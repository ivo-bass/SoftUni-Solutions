snowballs = int(input())
best_value = 0
best_snowball = {}

for snowball in range(snowballs):
    snow = int(input())
    time = int(input())
    quality = int(input())

    value = int((snow / time) ** quality)
    if value > best_value:
        best_value = value
        best_snowball = {'best_snow': snow, 'best_time': time, 'best_value': value, 'best_quality': quality}

print(f"{best_snowball['best_snow']} : {best_snowball['best_time']} = {best_snowball['best_value']} ({best_snowball['best_quality']})")
