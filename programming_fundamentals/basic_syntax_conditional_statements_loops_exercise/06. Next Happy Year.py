year = int(input())

while True:
    year += 1
    string = str(year)
    if len(set(string)) == len(string):
        print(string)
        break
