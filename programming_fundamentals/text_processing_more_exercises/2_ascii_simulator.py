valid_range = range(ord(input())+1, ord(input()))
print(sum([ord(char) for char in input() if ord(char) in valid_range]))
