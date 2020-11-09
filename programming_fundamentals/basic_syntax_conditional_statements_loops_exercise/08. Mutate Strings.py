first = input()
second = input()

new = ''
for i in range(len(first)):
    new = second[:i+1] + first[i+1:]
    if new != first:
        first = new
        print(first)
