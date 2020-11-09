text = input()

vowels_values = {'a': 1, 'e': 2, 'i': 3, 'o': 4, 'u': 5}
total_sum = 0
for char in text:
    if char in vowels_values.keys():
        total_sum += vowels_values[char]

print(total_sum)
