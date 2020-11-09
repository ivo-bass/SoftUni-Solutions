start = input()
end = input()
exception = input()

abc = list(map(chr, range(ord(start), ord(end)+1)))
if exception in abc:
    abc.remove(exception)
combinations = []
count = 0

for ch1 in abc:
    for ch2 in abc:
        for ch3 in abc:
            combination = f"{ch1}{ch2}{ch3}"
            count += 1
            combinations.append(combination)

print(*combinations, end=" ")
print(count)
