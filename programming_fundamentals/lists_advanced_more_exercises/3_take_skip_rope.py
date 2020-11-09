def take(count, i, li, res):
	for ind in range(i, i + count):
		if ind in range(len(li)):
			res.append(li[ind])
	i = i + count
	return i, res


def skip(count, i, li):
	if i + count in range(len(li)):
		i = i + count
	else:
		i = len(li) - 1
	return i


data = [s for s in input()]

nums = [int(d) for d in data if d.isnumeric()]
strings = [s for s in data if not s.isnumeric()]
take_list = [nums[i] for i in range(len(nums)) if i % 2 == 0]
skip_list = [nums[i] for i in range(len(nums)) if not i % 2 == 0]

i = 0
result = []
for index in range(len(take_list)):
	take_count = take_list[index]
	skip_count = skip_list[index]
	i, result = take(take_count, i, strings, result)
	i = skip(skip_count, i, strings)

print("".join(result))
