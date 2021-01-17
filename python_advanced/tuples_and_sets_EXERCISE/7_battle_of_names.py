n = int(input())

odd_set = set()
even_set = set()

for line in range(1, n + 1):
    name = input()
    val_sum = 0
    for ch in name:
        value = ord(ch)
        val_sum += value
    val_sum //= line
    if val_sum % 2 == 0:
        even_set.add(val_sum)
    else:
        odd_set.add(val_sum)

even_sum = sum(even_set)
odd_sum = sum(odd_set)

if odd_sum == even_sum:
    result = tuple(odd_set.union(even_set))
    print(', '.join(map(str, result)))
elif odd_sum > even_sum:
    result = tuple(odd_set.difference(even_set))
    print(', '.join(map(str, result)))
    pass
elif odd_sum < even_sum:
    result = tuple(odd_set.symmetric_difference(even_set))
    print(', '.join(map(str, result)))
