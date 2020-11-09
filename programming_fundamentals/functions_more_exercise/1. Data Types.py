def data_types(typ, value):
	if typ == "int":
		result = f"{int(value) * 2}"
	elif typ == "real":
		result = f"{float(value) * 1.5:.2f}"
	else:
		result = f"${value}$"
	return result


read_type = input()
read_value = input()

print(data_types(read_type, read_value))
