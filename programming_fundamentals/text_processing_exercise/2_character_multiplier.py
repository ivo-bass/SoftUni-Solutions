string_1, string_2 = input().split()

total_sum = 0

str1_codes = [ord(c) for c in string_1]
str2_codes = [ord(c) for c in string_2]

longer = str1_codes if len(str1_codes) >= len(str2_codes) else str2_codes
shorter = str1_codes if len(str1_codes) < len(str2_codes) else str2_codes

for index in range(len(longer)):
	if index in range(len(shorter)):
		total_sum += longer[index] * shorter[index]
	else:
		total_sum += longer[index]

print(total_sum)
