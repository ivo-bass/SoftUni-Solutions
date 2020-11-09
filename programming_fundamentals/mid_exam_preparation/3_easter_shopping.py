class ShopList:
	def __init__(self, shops):
		self.shops = shops

	def include(self, shop):
		self.shops.append(shop)

	def visit(self, position, count_shops):
		while not count_shops <= 0:
			if position == "first":
				self.shops.pop(0)
				count_shops -= 1
			elif position == "last":
				self.shops.pop()
				count_shops -= 1

	def prefer(self, i1, i2):
		self.shops[i1], self.shops[i2] = self.shops[i2], self.shops[i1]

	def place(self, shop, index):
		self.shops.insert(index, shop)


def is_valid(i, li):
	if i < len(li):
		return True
	return False


def main():
	shop_list = ShopList(input().split())
	number_of_commands = int(input())

	for n in range(number_of_commands):
		command = input().split()
		action = command[0]
		if action == "Include":
			shop = command[1]
			shop_list.include(shop)
		elif action == "Visit":
			position = command[1]
			count_shops = int(command[2])
			if count_shops > len(shop_list.shops):
				continue
			shop_list.visit(position, count_shops)
		elif action == "Prefer":
			i_1 = int(command[1])
			i_2 = int(command[2])
			if is_valid(i_1, shop_list.shops) and is_valid(i_2, shop_list.shops):
				shop_list.prefer(i_1, i_2)
		elif action == "Place":
			shop = command[1]
			i = int(command[2]) + 1
			if is_valid(i, shop_list.shops):
				shop_list.place(shop, i)
	print("Shops left:")
	print(*shop_list.shops)


if __name__ == '__main__':
	main()
