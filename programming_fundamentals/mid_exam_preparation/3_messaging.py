class ChatBox:
	def __init__(self):
		self.history = []

	def chat(self, msg):
		self.history.append(msg)

	def delete_msg(self, msg):
		if msg in self.history:
			self.history.remove(msg)

	def edit_msg(self, old_msg, new_msg):
		if old_msg in self.history:
			index = self.history.index(old_msg)
			self.history[index] = new_msg

	def pin_msg(self, msg):
		if msg in self.history:
			self.history.remove(msg)
			self.history.append(msg)

	def spam(self, msg_list):
		for msg in msg_list:
			self.history.append(msg)

	def end(self):
		for msg in self.history:
			print(msg)


def main():
	chat_box = ChatBox()
	data = input()
	while not data == "end":
		command = data.split()
		action = command[0]
		if action == "Chat":
			msg = command[1]
			chat_box.chat(msg)
		elif action == "Delete":
			msg = command[1]
			chat_box.delete_msg(msg)
		elif action == "Edit":
			old, new = command[1], command[2]
			chat_box.edit_msg(old, new)
		elif action == "Pin":
			msg = command[1]
			chat_box.pin_msg(msg)
		elif action == "Spam":
			msg_list = command[1:]
			chat_box.spam(msg_list)
		data = input()
	chat_box.end()


if __name__ == '__main__':
	main()
