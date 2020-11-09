# TODO Solve this problem!

soldiers = [int(i) for i in input().strip().split()]
counter = int(input())
result = []


def kill(counter_, li):
	index = (counter_ - 1) % len(li)
	while len(li) > 1:
		result.append(li[index])
		li.pop(index)
		index = (index + counter_ - 1) % len(li)
	if len(li) == 1:
		result.append(li[0])


kill(counter, soldiers)
string = str(result).replace(" ", "")
print(string)
