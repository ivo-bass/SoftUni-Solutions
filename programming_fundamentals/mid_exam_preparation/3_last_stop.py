class Gallery:
	def __init__(self, seq):
		self.sequence = seq

	def change(self, old, new):
		if old in self.sequence:
			index = self.sequence.index(old)
			self.sequence[index] = new

	def hide(self, num):
		if num in self.sequence:
			self.sequence.remove(num)

	def switch(self, num1, num2):
		if num1 in self.sequence and num2 in self.sequence:
			index1, index2 = self.sequence.index(num1), self.sequence.index(num2)
			self.sequence[index1], self.sequence[index2] = self.sequence[index2], self.sequence[index1]

	def insert_p(self, index, num):
		if index in range(len(self.sequence)):
			self.sequence.insert(index + 1, num)

	def reverse(self):
		self.sequence = self.sequence[::-1]

	def print_gallery(self):
		print(" ".join(self.sequence))


def main():
	gallery = Gallery(input().split())
	data = input()
	while not data == "END":
		command = data.split()
		action = command[0]
		if action == "Change":
			current_num, changed_num = command[1], command[2]
			gallery.change(current_num, changed_num)
		elif action == "Hide":
			num = command[1]
			gallery.hide(num)
		elif action == "Switch":
			num1, num2 = command[1], command[2]
			gallery.switch(num1, num2)
		elif action == "Insert":
			index, num = command[1], command[2]
			index = int(index)
			gallery.insert_p(index, num)
		elif action == "Reverse":
			gallery.reverse()
		data = input()
	gallery.print_gallery()


if __name__ == '__main__':
	main()
