class Vehicle:
	def __init__(self, typ, model, price):
		self.type = typ
		self.model = model
		self.price = price
		self.owner = None

	def buy(self, money, owner):
		if self.owner:
			return "Car already sold"
		else:
			if money < self.price:
				return "Sorry, not enough money"
			else:
				self.owner = owner
				change = f"{money - self.price:.2f}"
				return f"Successfully bought a {self.type}. Change: {change}"

	def sell(self):
		if self.owner:
			self.owner = None
		else:
			return "Vehicle has no owner"

	def __repr__(self):
		if self.owner:
			return f"{self.model} {self.type} is owned by: {self.owner}"
		else:
			return f"{self.model} {self.type} is on sale: {self.price}"
