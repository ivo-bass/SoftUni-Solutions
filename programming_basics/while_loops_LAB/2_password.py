name = input()
password = input()
user_input = input()

while user_input != password:
    user_input = input()

print(f"Welcome {name}!")
