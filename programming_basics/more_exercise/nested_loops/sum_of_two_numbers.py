start = int(input())
end = int(input())
magic_n = int(input())

counter = 0
is_magical = False

for x in range(start, end + 1):
    for y in range(start, end + 1):
        result = x + y
        counter += 1
        if result == magic_n:
            is_magical = True
            print(f"Combination N:{counter} ({x} + {y} = {magic_n})")
            break
    if is_magical:
        break

if not is_magical:
    print(f"{counter} combinations - neither equals {magic_n}")
