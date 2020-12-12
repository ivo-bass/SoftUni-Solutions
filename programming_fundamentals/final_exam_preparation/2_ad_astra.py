from re import findall

data = input()
pattern = r"([#|/|])([a-zA-Z\s]+)\1(\d\d/\d\d/\d\d)\1(\d{1,5})\1"
matches = findall(pattern, data)

total_calories = 0
for match in matches:
	total_calories += int(match[3])

print(f"You have food to last you for: {int(total_calories / 2000)} days!")
for match in matches:
	print(f"Item: {match[1]}, Best before: {match[2]}, Nutrition: {match[3]}")
