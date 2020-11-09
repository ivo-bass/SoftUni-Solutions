"""As a good friend, you decide to buy presents for your friends.
Create a program that helps you plan the gifts for your friends and family.
First, you are going to receive the gifts you plan on buying on a single line,
separated by space, in the following format:
"{gift1} {gift2} {gift3} … {gift_n}"
Then you will start receiving commands until you read the "No Money" message.
"""

gifts_input = input()
gifts = list(gifts_input.strip().split())


def out_of_stock(command_, list_):
	"""Find the gifts with this name in your collection,
	if there are any, and change their values to 'None'."""
	for i in range(len(list_)):
		if list_[i] == command_[1]:
			list_[i] = "None"
	return list_


def required(command_, list_):
	"""Replace the value of the current gift on the
	given index with this gift, if the index is valid."""
	if int(command_[2]) in range(len(list_)):
		list_[int(command_[2])] = command_[1]
	return list_


def just_in_case(command_, list_):
	"""Replace the value of your last gift with this one."""
	list_[-1] = command_[1]
	return list_


def no_money(list_):
	"""Print the gifts on a single line, except the ones with value
	'None', separated by a single space in the following format:
	'{gift1} {gift2} {gift3}… {giftn}'."""
	for _ in list_:
		if "None" in list_:
			list_.remove("None")
	print(*list_)


while True:
	command_string = input()
	if command_string == "No Money":
		no_money(gifts)
		break
	command = list(command_string.split())
	if command[0] == "OutOfStock":
		gifts = out_of_stock(command, gifts)
	elif command[0] == "Required":
		gifts = required(command, gifts)
	elif command[0] == "JustInCase":
		gifts = just_in_case(command, gifts)
	else:
		pass
