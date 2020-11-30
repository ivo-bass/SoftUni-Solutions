import re

key_pattern = r"([star])"
info_pattern = r"((?<=@)[A-Za-z]+)[^@!>\-]*((?<=:)\d+)[^@:>\-]*((?<=!)[AD](?=!))[^@:]*((?<=->)\d+)"
#
# name_pattern = r"(?<=@)([A-Za-z]+)"
# population_pattern = r"(?<=:)(\d+)"
# attack_type_pattern = r"(?<=!)([AD])(?=!)"
# soldier_count_pattern = r"(?<=->)\d+"
# sep = r"[^@!>:-]*"

attacked_planets = []
destroyed_planets = []

n = int(input())
for _ in range(n):
	encrypted = input()
	decrypted = ""
	key_matches = re.findall(key_pattern, encrypted, re.IGNORECASE)
	key = len(key_matches)
	for char in encrypted:
		decrypted += chr(ord(char) - key)

	match = re.findall(info_pattern, decrypted)
	if match:
		name = match[0][0]
		population = match[0][1]
		attack_type = match[0][2]
		soldier_count = match[0][3]
		if attack_type == "A":
			attacked_planets.insert(0, name)
		elif attack_type == "D":
			destroyed_planets.insert(0, name)

print(f"Attacked planets: {len(attacked_planets)}")
for name in attacked_planets:
	print(f"-> {name}")
print(f"Destroyed planets: {len(destroyed_planets)}")
for name in destroyed_planets:
	print(f"-> {name}")
