factor = int(input())
count = int(input())

li = [i for i in range(factor, count*factor + 1, factor)]

print(li)
