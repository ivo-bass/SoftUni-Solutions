first_list = input().split(', ')
second_list = input().split(', ')

result = []
for word1 in first_list:
	for word2 in second_list:
		if word1 in word2 and word1 not in result:
			result.append(word1)

# result = [word1 for word2 in second_list for word1 in first_list if word1 in word2]
print(result)
