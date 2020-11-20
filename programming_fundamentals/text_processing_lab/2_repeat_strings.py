data = input().split()
result = ""
for word in data:
	result += word * len(word)
print(result)
