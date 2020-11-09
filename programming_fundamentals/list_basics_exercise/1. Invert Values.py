string = input()

int_list = list(string.split())
reversed_items_list = [-int(i) for i in int_list]

print(reversed_items_list)
