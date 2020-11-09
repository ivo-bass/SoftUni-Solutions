n = int(input())

valid_combinations = 0
for x in range(n+1):
    for y in range(n+1):
        for z in range(n+1):
            result = x + y + z
            if result == n:
                valid_combinations += 1

print(valid_combinations)
