def collect(inv, i):
	if i not in inv:
		inv.append(i)
	return inv


def drop(inv, i):
	if i in inv:
		inv.remove(i)
	return inv


def combine_items(inv, i):
	old, new = i.split(":")
	if old in inv:
		inv.insert(inv.index(old) + 1, new)
	return inv


def renew(inv, i):
	if i in inv:
		inv.remove(i)
		inv.append(i)
	return inv


inventory = input().split(", ")
data = input()
while not data == "Craft!":
	command, item = data.split(" - ")
	if command == "Collect":
		inventory = collect(inventory, item)
	elif command == "Drop":
		inventory = drop(inventory, item)
	elif command == "Combine Items":
		inventory = combine_items(inventory, item)
	elif command == "Renew":
		inventory = renew(inventory, item)
	data = input()

print(", ".join(inventory))
