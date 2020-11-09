start = int(input())
end = int(input())
magic_num = int(input())

combination = 0
combination_found = False
for x in range(start, end+1):
    for y in range(start, end+1):
        combination += 1
        if x + y == magic_num:
            print(f"Combination N:{combination} ({x} + {y} = {magic_num})")
            combination_found = True
            break
    if combination_found:
        break

if not combination_found:
    print(f"{combination} combinations - neither equals {magic_num}")
