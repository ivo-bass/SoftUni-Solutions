number_of_inputs = int(input())

result = 0

for _ in range(number_of_inputs):
    ch = input()
    result += ord(ch)

print(f"The sum equals: {result}")
