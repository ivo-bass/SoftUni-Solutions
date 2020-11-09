class Storage:
	def __init__(self, capacity):
		self.capacity = capacity
		self.free_space = capacity
		self.storage = []

	def add_product(self, product):
		if self.free_space > 0:
			self.storage.append(product)
			self.free_space -= 1

	def get_products(self):
		return self.storage
