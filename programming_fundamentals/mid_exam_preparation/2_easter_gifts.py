class GiftList:
	def __init__(self, gifts):
		self.gifts = gifts

	def out_of_stock(self, gift):
		for index in range(len(self.gifts)):
			if self.gifts[index] == gift:
				self.gifts[index] = "None"

	def required(self, gift, index):
		if int(index) in range(len(self.gifts)):
			self.gifts[index] = gift

	def just_in_case(self, gift):
		self.gifts[-1] = gift

	def no_money(self):
		self.gifts = list(filter(lambda x: x != "None", self.gifts))
		print(*self.gifts)

	def correct_list(self):
		command = input()
		while not command == "No Money":
			action, value = command.split(maxsplit=1)
			if action == "OutOfStock":
				self.out_of_stock(value)
			elif action == "Required":
				name, ind = value.split()
				self.required(name, int(ind))
			elif action == "JustInCase":
				self.just_in_case(value)
			command = input()


gift_list = GiftList(input().split())
gift_list.correct_list()
gift_list.no_money()
