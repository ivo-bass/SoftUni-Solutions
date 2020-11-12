class Sequence:
	def __init__(self, seq):
		self.seq = seq
	
	def __repr__(self):
		return ", ".join(self.seq)

	def reverse_seq(self, start, count):
		reversed_part = list(reversed(self.seq[start:start+count]))
		self.seq = self.seq[:start] + reversed_part + self.seq[start+count:]

	def sort_seq(self, start, count):
		sorted_part = list(sorted(self.seq[start:start + count]))
		self.seq = self.seq[:start] + sorted_part + self.seq[start + count:]

	def remove_seq(self, count):
		self.seq = self.seq[count:]


seq = Sequence(input().split())

data = input()
while not data == "end":
	command = data.split()
	action = command[0]
	
	if action == "reverse":
		start, count = int(command[2]), int(command[4])
		seq.reverse_seq(start, count)
	elif action == "sort":
		start, count = int(command[2]), int(command[4])
		seq.sort_seq(start, count)
	elif action == "remove":
		count = int(command[1])
		seq.remove_seq(count)
	data = input()

print(seq)
