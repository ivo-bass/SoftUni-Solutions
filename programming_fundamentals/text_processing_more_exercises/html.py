def print_title(text):
	print("<h1>")
	print(f"    {text}")
	print("</h1>")


def print_content(text):
	print("<article>")
	print(f"    {text}")
	print("</article>")


def print_comment(text):
	print("<div>")
	print(f"    {text}")
	print("</div>")


title, content, comment = input(), input(), input()
print_title(title)
print_content(content)
while not comment == "end of comments":
	print_comment(comment)
	comment = input()
