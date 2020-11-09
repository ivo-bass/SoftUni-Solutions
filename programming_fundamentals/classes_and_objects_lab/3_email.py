class Email:
	def __init__(self, sender, receiver, content, is_sent=False):
		self.sender = sender
		self.receiver = receiver
		self.content = content
		self.is_sent = is_sent

	def send(self):
		self.is_sent = True

	def get_info(self):
		return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


class Box:
	def __init__(self):
		self.emails = []

	def add_email(self, email):
		self.emails.append(email)

	def send_emails(self, indexes):
		for i in indexes:
			self.emails[i].send()

	def print_mailbox(self):
		for email in self.emails:
			print(email.get_info())


def main():
	box = Box()
	command = input()
	while not command == "Stop":
		sender, receiver, content = command.split()
		mail = Email(sender, receiver, content)
		box.add_email(mail)
		command = input()

	indexes = [int(i) for i in input().split(", ")]
	box.send_emails(indexes)
	box.print_mailbox()


if __name__ == '__main__':
	main()
