string_list = input()

int_list = [int(i) for i in string_list.split(", ")]

for integer in int_list:
	if integer == 0:
		int_list.remove(integer)
		int_list.append(integer)

print(int_list)
