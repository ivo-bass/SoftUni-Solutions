class Cupid:
	def __init__(self, neighbourhood):
		self.li = neighbourhood
		self.position = 0

	def jump(self, length):
		self.position += length
		if self.position >= len(self.li):
			self.position = 0
		if self.li[self.position] == 0:
			print(f"Place {self.position} already had Valentine's day.")
		else:
			self.li[self.position] -= 2
			if self.li[self.position] <= 0:
				self.li[self.position] = 0
				print(f"Place {self.position} has Valentine's day.")

	def stop(self):
		print(f"Cupid's last position was {self.position}.")
		failed_count = len(list(filter(None, self.li)))
		if sum(self.li) == 0:
			print("Mission was successful.")
		else:
			print(f"Cupid has failed {failed_count} places.")


def heart_delivery():
	data = input()
	neighbourhood = [int(s) for s in data.split("@")]
	cupid = Cupid(neighbourhood)
	while not (command := input()) == "Love!":
		length = int(command.split()[1])
		cupid.jump(length)
	cupid.stop()


if __name__ == '__main__':
	heart_delivery()
