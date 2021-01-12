expression = input()

stack = []
for index in range(len(expression)):
	char = expression[index]
	if char == '(':
		stack.append(index)
	elif char == ')':
		start = stack.pop()
		print(expression[start:index+1])
