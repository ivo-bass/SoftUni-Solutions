from re import findall

participants = input().split(", ")
results = {k: 0 for k in participants}

data = input()
while not data == "end of race":
	name = "".join(findall(r"[A-Za-z]", data))
	distance = sum([int(s) for s in findall(r"[\d]", data)])
	if name in results:
		results[name] += distance
	data = input()

top_runners_list = sorted(results.items(), key=lambda x: -x[1])
print(f"1st place: {top_runners_list[0][0]}")
print(f"2nd place: {top_runners_list[1][0]}")
print(f"3rd place: {top_runners_list[2][0]}")
