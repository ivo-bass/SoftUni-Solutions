class Comment:

	def __init__(self, username, content, likes=0):
		self.username = username
		self.content = content
		self.likes = likes


comment1 = Comment("pesho", "I like this class")
comment2 = Comment("gosho", "What?", likes=10)

print(comment1.username)
print(comment1.content)
print(comment1.likes)

print(comment2.content, "|", comment2.likes)