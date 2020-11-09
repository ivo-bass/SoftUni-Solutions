number = int(input())
loading_bar = ".........."
result = "%" * (number//10) + loading_bar[number//10:]

if result == "%%%%%%%%%%":
	print("100% Complete!")
	print(f"[{result}]")
else:
	print(f"{number}% [{result}]")
	print("Still loading...")
