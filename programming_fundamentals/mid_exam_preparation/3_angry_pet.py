class Pet:
	def __init__(self, items, entry_index):
		self.items = items
		self.entry_index = entry_index
		self.entry_price = self.items[entry_index]
		self.left_sum = 0
		self.right_sum = 0

	def filter_by_type(self, li, type_):
		if type_ == "cheap":
			return list(filter(lambda x: x < self.entry_price, li))
		elif type_ == "expensive":
			return list(filter(lambda x: x >= self.entry_price, li))

	def filter_by_price(self, li, price):
		if price == "positive":
			return list(filter(lambda x: x > 0, li))
		elif price == "negative":
			return list(filter(lambda x: x < 0, li))
		return li

	def go_left(self, items, prices):
		left_part = self.items[:self.entry_index]
		valid_types = self.filter_by_type(left_part, items)
		valid_left_items = self.filter_by_price(valid_types, prices)
		self.left_sum = sum(valid_left_items)

	def go_right(self, items, prices):
		right_part = self.items[self.entry_index + 1:]
		valid_types = self.filter_by_type(right_part, items)
		valid_right_items = self.filter_by_price(valid_types, prices)
		self.right_sum = sum(valid_right_items)

	def destroy(self, items, prices):
		self.go_left(items, prices)
		self.go_right(items, prices)
		position = "Left"
		if self.right_sum > self.left_sum:
			position = "Right"
			print(f"{position} – {self.right_sum}")
		else:
			print(f"{position} – {self.left_sum}")


tom = Pet([int(s) for s in input().split()], int(input()))
tom.destroy(input(), input())
