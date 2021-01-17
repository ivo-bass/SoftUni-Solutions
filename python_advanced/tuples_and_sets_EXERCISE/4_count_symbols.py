text = input()

symbols = {}

for ch in text:
    if not ch in symbols:
        symbols[ch] = 0
    symbols[ch] += 1

symbols = dict(sorted(symbols.items()))

for char, count in symbols.items():
    print(f'{char}: {count} time/s')
