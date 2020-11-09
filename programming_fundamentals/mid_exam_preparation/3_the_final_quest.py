class Message:
	def __init__(self, seq):
		self.seq = seq

	def __repr__(self):
		return " ".join(self.seq)

	def delete_word(self, index):
		if index in range(0, len(self.seq)-1):
			self.seq.remove(self.seq[index + 1])

	def swap(self, w1, w2):
		if w1 in self.seq and w2 in self.seq:
			i1, i2 = self.seq.index(w1), self.seq.index(w2)
			self.seq[i1], self.seq[i2] = self.seq[i2], self.seq[i1]

	def put(self, word, index):
		if index - 1 in range(0, len(self.seq)-1):
			if index - 1 == len(self.seq) - 1:
				self.seq.append(word)
			else:
				self.seq.insert(index - 1, word)

	def sort_seq(self):
		self.seq = sorted(self.seq, key=str.lower, reverse=True)

	def replace_words(self, w1, w2):
		if w2 in self.seq:
			index = self.seq.index(w2)
			self.seq[index] = w1


def main():
	msg = Message(input().split())

	data = input()
	while not data == "Stop":
		command = data.split()
		action = command[0]
		if action == "Delete":
			index = int(command[1])
			msg.delete_word(index)
		elif action == "Swap":
			word1, word2 = command[1], command[2]
			msg.swap(word1, word2)
		elif action == "Put":
			word, index = command[1], command[2]
			index = int(index)
			msg.put(word, index)
		elif action == "Sort":
			msg.sort_seq()
		elif action == "Replace":
			word1, word2 = command[1], command[2]
			msg.replace_words(word1, word2)
		data = input()

	print(msg)


if __name__ == '__main__':
	main()
